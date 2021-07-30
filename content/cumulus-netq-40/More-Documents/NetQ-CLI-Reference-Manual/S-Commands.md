---
title: S Commands
author: Cumulus Networks
weight: 1106
toc: 3
right_toc_levels: 1
pdfhidden: true
---
<!-- vale NVIDIA.HeadingTitles = NO -->
This topic includes all commands that begin with `netq s*`.

<!-- vale off -->
## netq show address-history
<!-- vale on -->

Displays where an IPv4 or IPv6 address has lived in your network fabric in the last 24 hours. The output provides:

- When the address was last changed
- The switch or hostname where the address resides
- The interface where the address resides
- The address prefix and mask
- The associated VRF

By default, each row in the output is a thread (or group) sorted by VLAN.

### Syntax

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-prefix\> | Display results for the switches and hosts with this address prefix |

### Options

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
<li><strong>d</strong>: days</li>
<li><strong>h</strong>: hours</li>
<li><strong>m</strong>: minutes</li>
<li><strong>s</strong>: seconds</li>
<li><strong>now</strong>
</ul>

The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{</notice>}}

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands

- netq show mac-history

- - -

## netq show agents

Displays basic configuration, health, and connectivity status for all nodes or a specific node running NetQ Agent in your network fabric. This command gives you an easy way to see if any NetQ Agents or their nodes have lost power, may have difficulty communicating with the telemetry server, and whether agents are running different versions of software. Any of these situations could cause problems in the operation of your network.

The output provides:

- Whether each node has been heard recently (last 90 seconds)
- If each node is in time synchronization with the NetQ appliance or virtual machine
- The NetQ Agent software version currently running on the node
- How long the node has been operationally up
- How long the NetQ Agent has been operationally up
- The last time the NetQ Agent was reinitialized
- When the last change was made to the any of these items

### Syntax

```
netq [<hostname>] show agents
    [fresh | dead | rotten | opta]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Filter output to view status for the switch or host with this name |
| fresh | NA | Filter output for devices where the NetQ Agent is communicating with the appliance or VM as expected |
| dead | NA | Filter output for devices where the NetQ Agent has been decommisioned by a user |
| rotten | NA | Filter output for devices where the NetQ Agent has not communicated with the appliance or VM in the last two minutes |
| opta | NA | Filter output for the NetQ Agent installed on the appliance or VM |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands

- netq show unit-tests agent
- netq show events
- netq check agents
- netq config add agent
- netq config del agent

- - -
<!-- vale off -->
## netq show bgp
<!-- vale on -->
Displays the health of all BGP sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The neighbor nodes for a given node
- What routing tables (VRF) is used by that node and neighbor
- The autonomous system number (ASN) assigned to the node
- The peer ASN for each neighbor node
- The received address prefix for IPv4/IPv6/EVPN when session is established
- When the last change was made to any of these items

If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.

### Syntax

```
netq [<hostname>] show bgp
    [<bgp-session>|asn <number-asn>]
    [vrf <vrf>]
    [established|failed]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | <!-- vale off -->\<bgp-session\><!-- vale on --> | Only display results for this particular BGP session; for example 5468354 |
| asn | \<number-asn\> | Only display results for nodes using this ASN; for example 65013 |
| vrf | \<vrf\> | Only display results for sessions run on this VRF; for example default, mgmt, or vrf10 |
| established | NA | Only display established BGP sessions |
| failed | NA | Only display failed BGP sessions |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands
<!-- vale off -->
- netq show unit-tests bgp
- netq show events
- netq check bgp
<!-- vale on -->
- - -

<!-- vale off -->
## netq show cl-btrfs-info
<!-- vale on -->

Displays status about disk utilization on a given device or all devices networkwide with BTRFS and Cumulus Linux 3.x installed. The output provides the following information for each device:

- Percentage of disk that is currently allocated
- Amount of space remaining (unallocated)
- Size of the largest data chunk
- Amount of space unused by data chunks
- Whether a rebalance of the disk is recommended
- When the last change was made to any of these items

For details about when a rebalance is recommended, refer to [When to Rebalance BTRFS Partitions]({{<ref "/knowledge-base/Configuration-and-Usage/Storage/When-to-Rebalance-BTRFS-Partitions">}}).

### Syntax

```
netq [<hostname>] cl-btrfs-info
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

### Sample Usage

Basic show: all devices in last 24 hours

```
cumulus@switch:~$ netq show cl-btrfs-info
Matching btrfs_info records:
Hostname          Device Allocated     Unallocated Space    Largest Chunk Size   Unused Data Chunks S Rebalance Recommende Last Changed
                                                                                 pace                 d
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf01            37.79 %              3.58 GB              588.5 MB             771.91 MB            yes                  Wed Sep 16 21:25:17 2020
```

### Related Commands

- netq show cl-ssd-util

- - -

<!-- vale off -->
## netq show cl-manifest
<!-- vale on -->

Displays the Cumulus Linux OS versions supported for a given device or all devices networkwide. The output provides the following information for each device:

- ASIC vendor the OS supports
- CPU architecture the OS supports
- Cumulus Linux version associated with the indicated ASIC and CPU

### Syntax

```
netq [<hostname>] cl-manifest
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

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

### Related Commands

- netq show cl-pkg-info
- netq show recommended-pkg-version

- - -

<!-- vale off -->
## netq show cl-pkg-info
<!-- vale on -->

Displays the versions for all software packages installed on a given device or all devices networkwide. The output provides the following information for each device:

- Package name and version
- Cumulus Linux version
- Package status
- When the last change was made to any of these items

The output can become very large for all devices and packages. When viewing results in a terminal window, consider filtering by hostname or package name to reduce the length of the output. Wildcards are not allowed for `hostname` or `text-package-name`.

### Syntax

```
netq [<hostname>] cl-pkg-info
    [<text-package-name>]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<text-package-name\> | Only display results for the software package with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

### Sample Usage

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

### Related Commands

- netq show recommended-pkg-version
- netq show cl-manifest

- - -

## netq show cl-resource

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

### Syntax

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| acl | NA | Display results for ACLs |
| forwarding | NA | Display results for forwarding resources |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ingress | NA | Only display results for the incoming ACLs |
| egress | NA | Only display results for the outgoing ACLs |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

Basic show: All devices, all ACLS

```
cumulus@switch:~$ netq leaf01 show cl-pkg-info

```

### Related Commands

- netq show recommended-pkg-version
- netq show cl-manifest

- - -

## netq show cl-ssd-util

Displays utilization of 3ME3 solid state drives (SSDs) for a given device or all devices networkwide. These are primarily found in on-premises deployment. Tracking SSD utilization over time enables you to see any downward trend or instability of the drive before you receive an alarm. The output provides the following information for each drive:

- Percentage of PE cycles remaining for the drive
- Count of current PE cycles used by this drive
- Total number of PE cycles supported for this drive
- The drive model information
- When the last change was made to any of these items

### Syntax

```
netq [<hostname>] show cl-ssd-util
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

### Sample Usage

Basic show: All drives, for a given device

```
cumulus@switch:~$ netq spine02 show cl-ssd-util
Hostname        Remaining PE Cycle (%)  Current PE Cycles executed      Total PE Cycles supported       SSD Model               Last Changed
spine02         80                      576                             2880                            M.2 (S42) 3ME3          Thu Oct 31 00:15:06 2019
```

### Related Commands

- netq show cl-btrfs-info

- - -

## netq show clag

Displays the health of all CLAG sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The peer nodes for a given node
- The system MAC address used for the session between the nodes
- The operational state of the session (up or down)
- The operational state of the backup IP address (up or down)
- The total number of bonds
- The number of dual-connected bonds
- When the last change was made to any of these items

If the total number of bonds does not match the number of dual-connected bonds, there might be a configuration issue.

### Syntax

```
netq [<hostname>] show clag
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands

- netq show unit-tests clag
- netq show events
- netq check clag

- - -

## netq show dom

Displays the performance degradation or complete outage of any digital optics modules (DOMs) on one or all devices. You can filter the output by interface for laser and module types, and by channel for laser type.

The output provides the following information for each device and interface:

- Alarm and warning thresholds
- Current value, by channel for laser type
- When any of these items was last changed

### Syntax

Two forms of this command are available: one for laser power and current and one for temperature and voltage.

```
netq [<hostname>] show dom type (laser_rx_power|laser_output_power|laser_bias_current)
    [interface <text-dom-port-anchor>]
    [channel_id <text-channel-id>]
    [around <text-time>]
    [json]

netq [<hostname>] show dom type (module_temp|module_voltage)
    [interface <text-dom-port-anchor>]
    [around <text-time>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| laser_rx_power | NA | Display current value and threshold alarms for transceiver input power (mW) on the DOMs |
| laser_output_power | NA | Display current value and threshold alarms for laser output power (mW) on the DOMs |
| laser_bias_current | NA | Display current value and threshold alarms for laser bias current (mA) on the DOMs |
| module_temp | NA | Display current value and threshold alarms for temperature (°C) on the DOMs |
| module_voltage | NA | Display current value and threshold alarms for transceiver voltage (V) on the DOMs |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| interface | \<text-dom-port-anchor\> | Only display results for the interface with this port name |
| channel_id | \<text-channel-id\> | Only display laser results for the channel with this ID |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Renamed `module_temperature` keyword to `module_temp` |
| 3.1.0 | Introduced |

### Sample Usage

Show module temperature of DOMs on given device

```
cumulus@switch:~$ netq spine01 show dom type module_temp
Matching dom records:
Hostname          Interface  type                 high_alarm_threshold low_alarm_threshold  high_warning_thresho low_warning_threshol value                Last Updated
                                                                                            ld                   d
----------------- ---------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
spine01           swp53s0    module_temperature   {‘degree_c’: 85,     {‘degree_c’: -10,    {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 32,     Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 185}     ‘degree_f’: 14}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 89.6}
spine01           swp35      module_temperature   {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 27.82,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 82.08}
spine01           swp55      module_temperature   {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 26.29,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 79.32}
spine01           swp9       module_temperature   {‘degree_c’: 78,     {‘degree_c’: -13,    {‘degree_c’: 73,     {‘degree_c’: -8,     {‘degree_c’: 25.57,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 172.4}   ‘degree_f’: 8.6}     ‘degree_f’: 163.4}   ‘degree_f’: 17.6}    ‘degree_f’: 78.02}
spine01           swp56      module_temperature   {‘degree_c’: 78,     {‘degree_c’: -10,    {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 29.43,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 172.4}   ‘degree_f’: 14}      ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 84.97}
spine01           swp53s2    module_temperature   {‘degree_c’: 85,     {‘degree_c’: -10,    {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 32,     Wed Jul  1 15:25:55 2020
                                                  ‘degree_f’: 185}     ‘degree_f’: 14}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 89.6}
spine01           swp6       module_temperature   {‘degree_c’: 80,     {‘degree_c’: -10,    {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 25.04,  Wed Jul  1 15:25:55 2020
                                                  ‘degree_f’: 176}     ‘degree_f’: 14}      ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 77.07}
spine01           swp7       module_temperature   {‘degree_c’: 85,     {‘degree_c’: -5,     {‘degree_c’: 80,     {‘degree_c’: 0,      {‘degree_c’: 24.14,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 185}     ‘degree_f’: 23}      ‘degree_f’: 176}     ‘degree_f’: 32}      ‘degree_f’: 75.45}
spine01           swp53s3    module_temperature   {‘degree_c’: 85,     {‘degree_c’: -10,    {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 32,     Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 185}     ‘degree_f’: 14}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 89.6}
spine01           swp11      module_temperature   {‘degree_c’: 95,     {‘degree_c’: -50,    {‘degree_c’: 93,     {‘degree_c’: -48,    {‘degree_c’: 23.75,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 203}     ‘degree_f’: -58}     ‘degree_f’: 199.4}   ‘degree_f’: -54.4}   ‘degree_f’: 74.75}
spine01           swp49      module_temperature   {‘degree_c’: 65,     {‘degree_c’: 10,     {‘degree_c’: 60,     {‘degree_c’: 15,     {‘degree_c’: 23.18,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 149}     ‘degree_f’: 50}      ‘degree_f’: 140}     ‘degree_f’: 59}      ‘degree_f’: 73.72}
spine01           swp12      module_temperature   {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 32.31,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 90.16}
spine01           swp53s1    module_temperature   {‘degree_c’: 85,     {‘degree_c’: -10,    {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 32,     Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 185}     ‘degree_f’: 14}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 89.6}
spine01           swp34      module_temperature   {‘degree_c’: 80,     {‘degree_c’: -10,    {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 24.93,  Wed Jul  1 15:25:55 2020
                                                  ‘degree_f’: 176}     ‘degree_f’: 14}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 76.87}
spine01           swp3       module_temperature   {‘degree_c’: 90,     {‘degree_c’: -40,    {‘degree_c’: 85,     {‘degree_c’: -40,    {‘degree_c’: 25.15,  Wed Jul  1 15:25:55 2020
                                                  ‘degree_f’: 194}     ‘degree_f’: -40}     ‘degree_f’: 185}     ‘degree_f’: -40}     ‘degree_f’: 77.27}
spine01           swp8       module_temperature   {‘degree_c’: 78,     {‘degree_c’: -13,    {‘degree_c’: 73,     {‘degree_c’: -8,     {‘degree_c’: 24.1,   Wed Jul  1 15:25:55 2020
                                                  ‘degree_f’: 172.4}   ‘degree_f’: 8.6}     ‘degree_f’: 163.4}   ‘degree_f’: 17.6}    ‘degree_f’: 75.38}
spine01           swp52      module_temperature   {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 20.55,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 68.98}
spine01           swp10      module_temperature   {‘degree_c’: 78,     {‘degree_c’: -13,    {‘degree_c’: 73,     {‘degree_c’: -8,     {‘degree_c’: 25.39,  Wed Jul  1 15:25:55 2020
                                                  ‘degree_f’: 172.4}   ‘degree_f’: 8.6}     ‘degree_f’: 163.4}   ‘degree_f’: 17.6}    ‘degree_f’: 77.7}
spine01           swp31      module_temperature   {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 27.05,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 80.69}
```

### Related Commands

None

- - -

## netq show ethtool-stats

Displays transmit and receive statistics for network interfaces on one or all devices, including frame errors, ACL drops, buffer drops and more. You can filter the output by device and view the statistics for a time in the past.

### Syntax

```
netq <hostname> show interface-stats
    port <physical-port>
    (rx|tx)
    [extended]
    [around <text-time>]
    [json]
```

### Required Arguments

<!-- vale off -->
| Argument | Value | Description |
| ---- | ---- | ---- |
| port | \<physical-port\> | Only display results for the port with this name |
| rx | NA | Only display receive statistics |
| tx | NA | Only display transmit statistics |
<!-- vale on -->

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| extended | NA | Display additional statistics; does not include statistics presented with standard output |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | The `port`, `rx` and `tx` options changed from optional to required. Removed the `min` option. Added the `extended` option. |
| 2.4.0 | Introduced |

### Sample Usage

Show transmit statistics for a given switch interface and switch in the network

```
cumulus@switch:~$ netq leaf01 show ethtool-stats port swp50 tx
Matching ethtool_stats records:
Hostname          Interface                 HwIfOutOctets        HwIfOutUcastPkts     HwIfOutMcastPkts     HwIfOutBcastPkts     HwIfOutDiscards      HwIfOutErrors        HwIfOutQDrops        HwIfOutNonQDrops     HwIfOutQLen          HwIfOutPausePkt      SoftOutErrors        SoftOutDrops         SoftOutTxFifoFull    Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp50                     8749                 0                    44                   0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    Tue Apr 28 22:09:57 2020
```

Shoe the additional statistics

```
cumulus@switch:~$ netq leaf01 show ethtool-stats port swp50 rx extended

Matching ethtool_stats records:
Hostname          Interface                 HwIfInPfc0Pkt        HwIfInPfc1Pkt        HwIfInPfc2Pkt        HwIfInPfc3Pkt        HwIfInPfc4Pkt        HwIfInPfc5Pkt        HwIfInPfc6Pkt        HwIfInPfc7Pkt        Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp50                     0                    0                    0                    0                    0                    0                    0                    0                    Tue Apr 28 22:09:25 2020
```

Show statistics in JSON format

```
cumulus@leaf01:~$ netq leaf01 show ethtool-stats port swp50 tx json
{
    "ethtool_stats":[
        {
            "hwifoutoctets":12571,
            "hwifoutucastpkts":0,
            "hwifoutpausepkt":0,
            "softouttxfifofull":0,
            "hwifoutmcastpkts":58,
            "hwifoutbcastpkts":0,
            "softouterrors":0,
            "interface":"swp50",
            "lastUpdated":1588112216.0,
            "softoutdrops":0,
            "hwifoutdiscards":0,
            "hwifoutqlen":0,
            "hwifoutnonqdrops":0,
            "hostname":"leaf01",
            "hwifouterrors":0,
            "hwifoutqdrops":0
	}
    ],
    "truncatedResult":false
}
```

```
cumulus@leaf01:~$ netq leaf01 show ethtool-stats port swp50 tx extended json
{
    "ethtool_stats":[
        {
            "hostname":"leaf01",
            "hwifoutq5wreddrops":0,
            "hwifoutq3wreddrops":0,
            "hwifoutpfc3pkt":0,
            "hwifoutq6wreddrops":0,
            "hwifoutq9wreddrops":0,
            "hwifoutq2wreddrops":0,
            "hwifoutq8wreddrops":0,
            "hwifoutpfc7pkt":0,
            "hwifoutpfc4pkt":0,
            "hwifoutpfc6pkt":0,
            "hwifoutq7wreddrops":0,
            "hwifoutpfc0pkt":0,
            "hwifoutpfc1pkt":0,
            "interface":"swp50",
            "hwifoutq0wreddrops":0,
            "hwifoutq4wreddrops":0,
            "hwifoutpfc2pkt":0,
            "lastUpdated":1588112216.0,
            "hwifoutwreddrops":0,
            "hwifoutpfc5pkt":0,
            "hwifoutq1wreddrops":0
	}
    ],
    "truncatedResult":false
}
```

### Related Commands

- netq show interface-stats
- netq show interface-untilization

- - -

## netq show events

Display system events that have occurred in the last 24 hours. Optionally, view events for a time in the past. You can filter the output by event severity and event type. The output provides the following information for each device:

- Message type
- Event severity (info, error, warning, critical, debug)
- Descriptive event message
- When the event occurred

### Syntax

```
netq [<hostname>] show events
    [level info | level error | level warning | level critical | level debug]
    [type agents|bgp|btrfsinfo|clag|clsupport|configdiff|evpn|interfaces|interfaces-physical|lcm|lldp|macs|mtu|ntp|os|ospf|roceconfig|sensors|services|tca_roce|trace|vlan|vxlan]
    [between <text-time> and <text-endtime>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| level | info, error, warning, critical, or debug | Only display events with this severity level |
| type | agents, bgp, btrfsinfo, clag, clsupport, configdiff, evpn, interfaces, interfaces-physical, lcm, lldp, macs, mtu, ntp, os, ospf, roceconfig, sensors, services, tca_roce, trace, vlan or vxlan | Display events for the type with this name |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Added `type lcm` option |
| 3.0.0 | Removed `type lnv` option |
| 2.3.1 | Added `type btrfsinfo` option |
| 2.1.x | Introduced; replaced `netq show changes` command |

### Sample Usage

Show all events in the last 3 days

```
cumulus@switch:~$ netq show events between now and 3d
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf02            evpn                     critical         VNI 4002 state changed from up to d Thu Dec 10 22:00:36 2020
                                                            own
leaf02            evpn                     critical         VNI 4001 state changed from up to d Thu Dec 10 22:00:36 2020
                                                            own
leaf02            evpn                     critical         VNI 10 state changed from up to dow Thu Dec 10 22:00:36 2020
                                                            n
leaf02            evpn                     critical         VNI 30 state changed from up to dow Thu Dec 10 22:00:36 2020
                                                            n
leaf02            evpn                     critical         VNI 20 state changed from up to dow Thu Dec 10 22:00:36 2020
                                                            n
leaf02            evpn                     critical         VNI 4002 state changed from up to d Thu Dec 10 20:42:39 2020
                                                            own
leaf02            evpn                     critical         VNI 4001 state changed from up to d Thu Dec 10 20:42:39 2020
                                                            own
...
border02          evpn                     critical         VNI 4002 state changed from up to d Thu Dec 10 03:24:10 2020
                                                            own
border02          evpn                     critical         VNI 4001 state changed from up to d Thu Dec 10 03:24:10 2020
                                                            own
border02          evpn                     critical         VNI 4002 state changed from up to d Thu Dec 10 02:58:20 2020
                                                            own
border02          evpn                     critical         VNI 4001 state changed from up to d Thu Dec 10 02:58:20 2020
                                                            own
border02          evpn                     critical         VNI 4002 state changed from up to d Thu Dec 10 02:32:16 2020
                                                            own
...
leaf02            services                 info             Service netqd status changed from i Thu Dec 10 06:49:15 2020
                                                            nactive to active
leaf02            services                 info             Service netqd status changed from i Thu Dec 10 06:22:22 2020
                                                            nactive to active
leaf02            services                 info             Service netqd status changed from i Thu Dec 10 06:21:20 2020
                                                            nactive to active
leaf02            services                 info             Service netqd status changed from i Thu Dec 10 06:20:19 2020
                                                            nactive to active
leaf02            services                 info             Service netqd status changed from i Thu Dec 10 06:14:06 2020
                                                            nactive to active
...
```

Show critical events for a particular service

```
cumulus@switch:~$ netq show events level critical type clag between now and 3d
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            clag                     critical         Peer state changed to down          Thu Dec 10 18:53:44 2020
leaf02            clag                     critical         Peer state changed to down          Thu Dec 10 18:39:00 2020
border01          clag                     critical         Peer state changed to down          Thu Dec 10 02:21:59 2020
border01          clag                     critical         Peer state changed to down          Thu Dec 10 02:19:55 2020
border01          clag                     critical         Peer state changed to down          Thu Dec 10 02:16:50 2020
border01          clag                     critical         Peer state changed to down          Thu Dec 10 02:14:47 2020
border01          clag                     critical         Peer state changed to down          Wed Dec  9 23:02:34 2020
border01          clag                     critical         Peer state changed to down          Wed Dec  9 22:56:25 2020
border02          clag                     critical         Peer state changed to down          Wed Dec  9 22:53:27 2020
border01          clag                     critical         Peer state changed to down          Wed Dec  9 22:53:20 2020
border01          clag                     critical         Peer state changed to down          Wed Dec  9 22:47:10 2020
border02          clag                     critical         Peer state changed to down          Wed Dec  9 22:25:32 2020
```

### Related Commands

None
<!-- show notification?? -->

- - -

## netq show events-config

Displays all event suppression configurations. Optionally, you can filter by a specific configuration or message type. The output when viewing one or all event suppression configurations provides the following information for each configuration:

- Configuration identifier and name
- Message type
- Scope of the suppression
- When the suppression no longer applies

When you filter by a message type, you must include the `show-filter-conditions` keyword to display the conditions associated with that message type and the hierarchy in which they are processed. The output in this case provides the following information for each message type:

- Message name
- Filter condition name, hierarchy, and description

### Syntax

```
netq show events-config
    [events_config_id <text-events-config-id-anchor>]
    [show-filter-conditions | message_type <text-message-type-anchor> show-filter-conditions]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| events_config_id | \<text-events-config-id-anchor\> | Only display results for the switch or host with this name |
| show-filter-conditions | NA | Only display results for sessions using the VNI with this name |
| message_type | \<text-message-type-anchor\> | Only display results for configurations with this type. Values include <!-- vale off -->*agent*, *bgp*, *btrfsinfo*, *clag*, *clsupport*, *configdiff*, *evpn*, *link*, *ntp*, *ospf*, *sensor*, *services*, and *ssdutil*.<!-- vale on --> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

Show a given event suppression configuration

```
cumulus@switch:~$ netq show events-config events_config_id eventsconfig_1

Matching config_events records:
Events Config ID     Events Config Name   Message Type         Scope                                                        Active Suppress Until
-------------------- -------------------- -------------------- ------------------------------------------------------------ ------ --------------------
eventsconfig_1       job_cl_upgrade_2d89c agent                {"db_state":"*","hostname":"spine02","severity":"*"}         True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine02
eventsconfig_1       job_cl_upgrade_2d89c bgp                  {"vrf":"*","peer":"*","hostname":"spine04","severity":"*"}   True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c btrfsinfo            {"hostname":"spine04","info":"*","severity":"*"}             True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clag                 {"hostname":"spine04","severity":"*"}                        True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clsupport            {"fileAbsName":"*","hostname":"spine04","severity":"*"}      True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c configdiff           {"new_state":"*","old_state":"*","type":"*","hostname":"spin True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      e04","severity":"*"}                                                2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c evpn                 {"hostname":"spine04","vni":"*","severity":"*"}              True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c link                 {"ifname":"*","new_state":"*","hostname":"spine04","severity True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      ":"*"}                                                              2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ntp                  {"new_state":"*","hostname":"spine04","severity":"*"}        True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ospf                 {"ifname":"*","hostname":"spine04","severity":"*"}           True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c sensor               {"sensor":"*","new_s_state":"*","hostname":"spine04","severi True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      ty":"*"}                                                            2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c services             {"new_status":"*","name":"*","hostname":"spine04","severity" True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      :"*"}                                                               2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ssdutil              {"hostname":"spine04","info":"*","severity":"*"}             True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_10      job_cl_upgrade_2d89c btrfsinfo            {"hostname":"fw2","info":"*","severity":"*"}                 True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c clag                 {"hostname":"fw2","severity":"*"}                            True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c clsupport            {"fileAbsName":"*","hostname":"fw2","severity":"*"}          True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c link                 {"ifname":"*","new_state":"*","hostname":"fw2","severity":"* True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                      "}                                                                  2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c ospf                 {"ifname":"*","hostname":"fw2","severity":"*"}               True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c sensor               {"sensor":"*","new_s_state":"*","hostname":"fw2","severity": True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                      "*"}                                                                2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
```

Show filter conditions for EVPN event suppression configurations

```
cumulus@switch:~$ netq show events-config message_type evpn show-filter-conditions

Matching config_events records:
Message Name             Filter Condition Name                      Filter Condition Hierarchy                           Filter Condition Description
------------------------ ------------------------------------------ ---------------------------------------------------- --------------------------------------------------------
evpn                     vni                                        3                                                    Target VNI
evpn                     severity                                   2                                                    Severity critical/info
evpn                     hostname                                   1                                                    Target Hostname
```
<!-- vale off -->
## netq show evpn
<!-- vale on -->
Displays the health of all EVPN sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides the following for each session:

- The VNI used
- The address of the VNI endpoint
- Whether the session is part of a layer 2 or layer 3 configuration
- The associated VRF or VLAN when defined
- Whether the associated VNI is in the kernel
- The export and import route targets used for filtering
- When the last change was made to any of these items

### Syntax

```
netq [<hostname>] show evpn
    [vni <text-vni>]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| <!-- vale off -->vni | \<text-vni\><!-- vale on --> | Only display results for sessions using the VNI with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands
<!-- vale off -->
- netq show unit-tests evpn
- netq show events
- netq check evpn
<!-- vale on -->
- - -

## netq show interfaces

Displays the health of all interfaces or a single interface on all nodes or a specific node in your network fabric currently or for a time in the past. You can filter by the interface type, state of the interface, or the remote interface. For a given switch or host, you can view the total number of configured interfaces.

The output provides the following for each device:

- The name of the interface
- The type of interface
- The state of the interface (up or down)
- The associated VRF, VLANs, PVID, MTU, and LLDP peer
- When the last change was made to any of these items
- The total number of interfaces on a given device

### Syntax

Four forms of the command are available, based on whether you want to view interface health for all devices or a given device, and whether you want to filter by an interface type.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name. This is only required when the `count` option is used. |
| type | <!-- vale off -->bond, bridge, eth, loopback, macvlan, swp, vlan, vrf, or vxlan<!-- vale on --> | Only display results for the specified interface type |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<remote-interface\> | Only display results for local interfaces with this remote interface |
| state | \<remote-interface-state\> | Only display results for remote interfaces in the specified state&mdash;up or down |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| count | NA | Display the total number of interface on the specified switch or host. The `hostname` option is required when using this option. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands

- netq show events
- netq check interfaces
- netq show unit-tests interfaces

- - -

<!-- vale off -->
## netq show interface-stats
<!-- vale on -->

Displays performance statistics for the physical interfaces on switches in your network. The NetQ Agent collects the statistics every 30 seconds. Statistics are not collected for non-physical interfaces, such as bonds, bridges, and VXLANs. You can filter the output by interface or to view only error statistics. The ouput provides the following information for each switch and interface:

- **Transmit**: tx_bytes, tx_carrier, tx_colls, tx_drop, tx_errs, tx_packets
- **Receive**: rx_bytes, rx_drop, rx_errs, rx_frame, rx_multicast, rx_packets
- When any of these items were last changed

### Syntax

```
netq [<hostname>] show interface-stats
    [errors | all]
    [<physical-port>]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for switch or host with this name |
| errors | NA | Only display transmit and receive error statistics |
| all | NA | Display all statistics |
| NA | \<physical-port\> | Only display results for the interface with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.2.1 | Introduced |
| 2.2.0 | Early access |

### Sample Usage

Show all statistics

```
cumulus@switch:~$ netq show interface-stats
Matching proc_dev_stats records:
Hostname          Interface                 RX Packets           RX Drop              RX Errors            TX Packets           TX Drop              TX Errors            Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
border01          swp1                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:46 2020
border01          swp54                     5073123              0                    0                    5063783              0                    0                    Mon Dec 14 22:52:46 2020
border01          swp52                     5066658              0                    0                    4765656              0                    0                    Mon Dec 14 22:52:46 2020
border01          swp4                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:46 2020
border01          swp53                     5068600              0                    0                    5045430              0                    0                    Mon Dec 14 22:52:46 2020
border01          swp3                      6269292              0                    0                    9419916              0                    0                    Mon Dec 14 22:52:46 2020
border01          swp49                     13272261             0                    0                    13775656             0                    0                    Mon Dec 14 22:52:46 2020
border01          swp51                     5070658              0                    0                    5012296              0                    0                    Mon Dec 14 22:52:46 2020
border01          swp2                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:46 2020
border01          swp50                     13324872             0                    0                    12815151             0                    0                    Mon Dec 14 22:52:46 2020
border02          swp1                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:40 2020
border02          swp54                     5062672              1                    0                    5038338              0                    0                    Mon Dec 14 22:52:40 2020
border02          swp52                     5060971              0                    0                    4740480              0                    0                    Mon Dec 14 22:52:40 2020
border02          swp4                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:40 2020
border02          swp53                     5057642              1                    0                    5039327              0                    0                    Mon Dec 14 22:52:40 2020
border02          swp3                      6264055              0                    0                    6266544              0                    0                    Mon Dec 14 22:52:40 2020
border02          swp49                     13775643             0                    0                    13272245             0                    0                    Mon Dec 14 22:52:40 2020
border02          swp51                     5062516              1                    0                    5031044              0                    0                    Mon Dec 14 22:52:40 2020
border02          swp2                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:40 2020
border02          swp50                     12815137             0                    0                    13324858             0                    0                    Mon Dec 14 22:52:40 2020
fw1               swp1                      9419887              0                    0                    6269271              0                    0                    Mon Dec 14 22:52:19 2020
fw1               swp2                      6266531              0                    0                    6264041              0                    0                    Mon Dec 14 22:52:19 2020
fw1               swp49                     0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:19 2020
fw2               swp2                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:36 2020
fw2               swp49                     0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:36 2020
fw2               swp1                      0                    0                    0                    0                    0                    0                    Mon Dec 14 22:52:36 2020
leaf01            swp54                     420818               0                    0                    423181               0                    0                    Mon Dec 14 22:52:40 2020
leaf01            swp53                     422209               0                    0                    426090               0                    0                    Mon Dec 14 22:52:40 2020
leaf01            swp3                      527422               2                    0                    794268               0                    0                    Mon Dec 14 22:52:40 2020
leaf02            swp54                     5062516              1                    0                    5118197              0                    0                    Mon Dec 14 22:52:35 2020
leaf02            swp53                     5077584              1                    0                    5052566              0                    0                    Mon Dec 14 22:52:35 2020
leaf02            swp3                      6366020              0                    0                    6432546              0                    0                    Mon Dec 14 22:52:35 2020
leaf03            swp54                     5087433              1                    0                    5042929              0                    0                    Mon Dec 14 22:52:32 2020
leaf03            swp53                     5063037              1                    0                    4881323              0                    0                    Mon Dec 14 22:52:32 2020
leaf03            swp3                      6360717              0                    0
...
```

Show statistics for a given interface

```
cumulus@switch:~$ netq show interface-stats swp2
Matching proc_dev_stats records:
Hostname          Interface                 RX Packets           RX Drop              RX Errors            TX Packets           TX Drop              TX Errors            Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
border01          swp2                      0                    0                    0                    0                    0                    0                    Tue Dec 15 15:47:23 2020
border02          swp2                      0                    0                    0                    0                    0                    0                    Tue Dec 15 15:47:09 2020
fw1               swp2                      6327111              0                    0                    6324616              0                    0                    Tue Dec 15 15:47:07 2020
fw2               swp2                      0                    0                    0                    0                    0                    0                    Tue Dec 15 15:46:54 2020
spine03           swp2                      5097329              0                    0                    5124570              0                    0                    Tue Dec 15 15:47:00 2020
spine04           swp2                      5167364              0                    0                    5111678              0                    0                    Tue Dec 15 15:47:18 2020
```

### Related Commands

- netq show interface-utilization
- netq show ethtool-stats

- - -

<!-- vale off -->
## netq show interface-utilization
<!-- vale on -->

Displays utilization (transmit and receive) and port speed for physical interfaces on switches in your network. NetQ collects this data every 30 seconds. You can filter the output by port name, data direction, and time.

### Syntax

```
netq [<hostname>] show interface-utilization
    [<text-port>]
    [tx|rx]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

<!-- vale off -->
| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<text-port\> | Only display results for the port with this name |
| tx | NA | Only display results for transmit data |
| rx | NA | Only display results for receive data |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
<!-- vale on -->

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Changed `interface-utils` keyword to `interface-utilization` |
| 2.3.0 | Introduced |

### Sample Usage

Show utilization for a given device

```
cumulus@switch:~$ netq spine01 show interface-utilization
Matching port_stats records:
Hostname          Interface                 RX Bytes (30sec)     RX Drop (30sec)      RX Errors (30sec)    RX Util (%age)       TX Bytes (30sec)     TX Drop (30sec)      TX Errors (30sec)    TX Util (%age)       Port Speed           Last Changed
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
spine01           swp6                      2652                 0                    0                    0                    2650                 0                    0                    0                    1G                   Tue Dec 15 16:02:57
                                                                                                                                                                                                                                         2020
spine01           swp5                      2547                 0                    0                    0                    2545                 0                    0                    0                    1G                   Tue Dec 15 16:02:57
                                                                                                                                                                                                                                         2020
```

Show utilization for all devices, transmit only

```
cumulus@switch:~$ netq show interface-utilization tx
Matching port_stats records:
Hostname          Interface                 TX Bytes (30sec)     TX Drop (30sec)      TX Errors (30sec)    TX Util (%age)       Port Speed           Last Changed
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
border01          swp1                      0                    0                    0                    0                    Unknown              Tue Dec 15 16:04:01
                                                                                                                                                     2020
border01          swp54                     2539                 0                    0                    0                    1G                   Tue Dec 15 16:04:01
                                                                                                                                                     2020
border01          swp52                     1679                 0                    0                    0                    1G                   Tue Dec 15 16:04:01
                                                                                                                                                     2020
border01          swp4                      0                    0                    0                    0                    Unknown              Tue Dec 15 16:04:01
                                                                                                                                                     2020
border01          swp53                     2539                 0                    0                    0                    1G                   Tue Dec 15 16:04:01
                                                                                                                                                     2020
border01          swp3                      4714                 0                    0                    0                    1G                   Tue Dec 15 16:04:01
                                                                                                                                                     2020
border01          swp49                     7708                 0                    0                    0                    1G                   Tue Dec 15 16:04:01
                                                                                                                                                     2020
border01          swp51                     2711                 0                    0                    0                    1G                   Tue Dec 15 16:04:01
...
```

### Related Commands

- netq show interface-stats
- netq show ethtool-stats

- - -

## netq show inventory

Displays information about the hardware and software components deployed on a given device or all devices networkwide. The output provides details specific to the component selected.

### Syntax

Eight forms of this command are available based on the inventory component you want to view.

```
netq [<hostname>] show inventory brief
    [opta]
    [json]

netq [<hostname>] show inventory asic
    [vendor <asic-vendor>| model <asic-model>| model-id <asic-model-id>]
    [opta]
    [json]

netq [<hostname>] show inventory board
    [vendor <board-vendor>|model <board-model>]
    [opta]
    [json]

netq [<hostname>] show inventory cpu
    [arch <cpu-arch>]
    [opta]
    [json]

netq [<hostname>] show inventory disk
    [name <disk-name>|transport <disk-transport>| vendor <disk-vendor>]
    [opta]
    [json]

netq [<hostname>] show inventory memory
    [type <memory-type>|vendor <memory-vendor>]
    [opta]
    [json]

netq [<hostname>] show inventory os
    [version <os-version>|name <os-name>]
    [opta]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| brief | NA | Only display summary information; hostname, switch, OS, CPU architecture, ASIC vendor, ports |
| asic | NA | Only display ASIC information; hostname, vendor, model, model ID, core bandwidth, ports |
| board | NA | Only display motherboard information; hostname, vendor, model, base MAC address, serial number, part number, revision, manufacturing date |
| cpu | NA | Only display processor information; hostname, architecture, model, frequency, number of cores |
| disk | NA | Only display disk information; hostname, disk name and type, transport, size, vendor, model |
| memory | NA | Only display memory information; hostname, memory name, type, size, speed, vendor, serial number |
| os | NA | Only display operating system information; hostname, OS name, version, when changed |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| vendor | \<asic-vendor\>, \<board-vendor\>, \<disk-vendor\>, \<memory-vendor\> | Only display results for the ASIC, board, disk, or memory vendor with this name |
| model | \<asic-model\>, \<board-model\> | Only display results for ASIC or board model with this name |
| model-id | \<asic-model-id\> | Only display results for ASIC models with this ID |
| arch | \<cpu-arch\> | Only display results for CPUs with this architecure |
| transport | \<disk-transport\> | Only display results for disks with this transport method |
| type | \<memory-type\> | Only display results for memory of this type |
| version | \<os-version\> | Only display results for operating systems of this version |
| name | \<os-name\> | Only display results for operating systems with this name |
| opta | NA | Only display results for the NetQ appliance or VM (not other switches or hosts) |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 4.0.0 | Removed license commands and options |
| 2.1.2 | Added `status` keyword to license form of command |
| 1.x | Introduced |

### Sample Usage

Show inventory summary

```
cumulus@switch:~$ netq show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
border01          VX                   CL              x86_64   VX              N/A
border02          VX                   CL              x86_64   VX              N/A
fw1               VX                   CL              x86_64   VX              N/A
fw2               VX                   CL              x86_64   VX              N/A
leaf01            VX                   CL              x86_64   VX              N/A
leaf02            VX                   CL              x86_64   VX              N/A
leaf03            VX                   CL              x86_64   VX              N/A
oob-mgmt-server   N/A                  Ubuntu          x86_64   N/A             N/A
server01          N/A                  Ubuntu          x86_64   N/A             N/A
server02          N/A                  Ubuntu          x86_64   N/A             N/A
server03          N/A                  Ubuntu          x86_64   N/A             N/A
server04          N/A                  Ubuntu          x86_64   N/A             N/A
server05          N/A                  Ubuntu          x86_64   N/A             N/A
server06          N/A                  Ubuntu          x86_64   N/A             N/A
server07          N/A                  Ubuntu          x86_64   N/A             N/A
spine01           VX                   CL              x86_64   VX              N/A
spine02           VX                   CL              x86_64   VX              N/A
spine03           VX                   CL              x86_64   VX              N/A
spine04           VX                   CL              x86_64   VX              N/A
```

Show ASIC information

```
cumulus@switch:~$ netq show inventory asic
Matching inventory records:
Hostname          Vendor               Model                          Model ID                  Core BW        Ports
----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
dell-z9100-05     Broadcom             Tomahawk                       BCM56960                  2.0T           32 x 100G-QSFP28
mlx-2100-05       Mellanox             Spectrum                       MT52132                   N/A            16 x 100G-QSFP28
mlx-2410a1-05     Mellanox             Spectrum                       MT52132                   N/A            48 x 25G-SFP28 & 8 x 100G-QSFP28
mlx-2700-11       Mellanox             Spectrum                       MT52132                   N/A            32 x 100G-QSFP28
qct-ix1-08        Broadcom             Tomahawk                       BCM56960                  2.0T           32 x 100G-QSFP28
qct-ix7-04        Broadcom             Trident3                       BCM56870                  N/A            32 x 100G-QSFP28
st1-l1            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-l2            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-l3            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-s1            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
st1-s2            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
```

Show OS information

```
cumulus@switch:~$ netq show inventory os
Matching inventory records:
Hostname          Name            Version                              Last Changed
----------------- --------------- ------------------------------------ -------------------------
border01          CL              3.7.13                               Tue Jul 28 18:49:46 2020
border02          CL              3.7.13                               Tue Jul 28 18:44:42 2020
fw1               CL              3.7.13                               Tue Jul 28 19:14:27 2020
fw2               CL              3.7.13                               Tue Jul 28 19:12:50 2020
leaf01            CL              3.7.13                               Wed Jul 29 16:12:20 2020
leaf02            CL              3.7.13                               Wed Jul 29 16:12:21 2020
leaf03            CL              3.7.13                               Tue Jul 14 21:18:21 2020
leaf04            CL              3.7.13                               Tue Jul 14 20:58:47 2020
oob-mgmt-server   Ubuntu          18.04                                Mon Jul 13 21:01:35 2020
server01          Ubuntu          18.04                                Mon Jul 13 22:09:18 2020
server02          Ubuntu          18.04                                Mon Jul 13 22:09:18 2020
server03          Ubuntu          18.04                                Mon Jul 13 22:09:20 2020
server04          Ubuntu          18.04                                Mon Jul 13 22:09:20 2020
server05          Ubuntu          18.04                                Mon Jul 13 22:09:20 2020
server06          Ubuntu          18.04                                Mon Jul 13 22:09:21 2020
server07          Ubuntu          18.04                                Mon Jul 13 22:09:21 2020
server08          Ubuntu          18.04                                Mon Jul 13 22:09:22 2020
spine01           CL              3.7.12                               Mon Aug 10 19:55:06 2020
spine02           CL              3.7.12                               Mon Aug 10 19:55:07 2020
spine03           CL              3.7.12                               Mon Aug 10 19:55:09 2020
spine04           CL              3.7.12                               Mon Aug 10 19:55:08 2020
```

### Related Commands

- netq config agent cpu-limit
- netq show resource-util

- - -

## netq show ip/ipv6 addresses

Displays the IPv4 or IPv6 addresses configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address or prefix, and VRF. A count of addresses can be obtained for a given device. The output provides the following information for each address:

- Hostname of the device with the address
- Interface on the device with the address
- VRF, when configured, on the interface with the address
- When the last change was made to any of these items

### Syntax

Two sets of IP address commands are available, one for IPv4 and one for IPv6.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ip | NA | Display TCP IPv4 addresses |
| ipv6 | NA | Display TCP IPv6 addresses |

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address with `subnet`, `supernet`, and `gateway` options |
| 2.1.2 | Removed `changes` and `between` options |

### Sample Usage

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

### Related Commands

- netq show ip/ipv6 neighbors
- netq show ip/ipv6 routes

- - -

## netq show ip/ipv6 neighbors

Displays the IPv4 or IPv6 neighbors configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address, address and VRF, or VRF. A count of neighbors can be obtained for a given device, or for a given device and MAC address. The output provides the following information for each address:

- Hostname of neighbor
- Interface of neighbor
- MAC address of neighbor
- VRF, when configured, of neighbor
- Whether this address owned by the neighbor or learned from by host
- When the last change was made to any of these items

### Syntax

Two sets of IP neighbors commands are available, one for IPv4 and one for IPv6.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ip | NA | Display TCP IPv4 neighbors |
| ipv6 | NA | Display TCP IPv6 neighbors |

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address with `subnet`, `supernet`, and `gateway` options |
| 2.1.2 | Removed `changes` and `between` options |

### Sample Usage

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

### Related Commands

- netq show ip/ipv6 addresses
- netq show ip/ipv6 routes

- - -

## netq show ip routes

Displays the IPv4 or IPv6 routes configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address, address and prefix, VRF, and route origin. A count of routes can be obtained for a given device. The output provides the following information for each route:

- Whether this route originated with this device or not
- VRF used for the route
- Address prefix used for the route
- Hostname of the device with the route
- Next hops the route takes
- When the last change was made to any of these items

### Syntax

Two sets of IP routes commands are available, one for IPv4 and one for IPv6.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| ip | NA | Display TCP IPv4 routes |
| ipv6 | NA | Display TCP IPv6 routes |

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address with `subnet`, `supernet`, and `gateway` options |
| 2.1.2 | Removed `changes` and `between` options |

### Sample Usage

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

### Related Commands

- netq show ip/ipv6 addresses
- netq show ip/ipv6 neighbors

- - -

<!-- vale off -->
## netq show job-status
<!-- vale on -->

Displays the status of installation and upgrade jobs running on your NetQ appliance or VM.

### Syntax

```
netq show job-status <text-opta-ip>
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-opta-ip\> | Display the status of jobs running on the appliance or VM with this IP address |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

Show job status

```
cumulus@switch:~$ netq show job-status 192.168.200.250
```

### Related Commands

None

- - -

## netq show kubernetes

Displays the configuration and health of the non-NetQ Kubernetes components in your container environment. This command enables you to:

- Identify and locate pods, deployment, replica-set and services deployed within the network using IP, name, label, and so forth
- Track network connectivity of all pods of a service, deployment and replica set
- Locate what pods have been deployed adjacent to a top of rack (ToR) switch

Outputs vary according to the component of the kubernetes cluster you want to view.

{{<notice tip>}}
Kubernetes monitoring must be enabled on NetQ Agents. Refer to the <code>netq config add agent</code> command to enable monitoring.
{{</notice>}}

### Syntax

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
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cluster | NA | Only display kubernetes cluster information |
| node | NA | Only display kubernetes node information |
| daemon-set | Only display kubernetes daemon-set information |
| deployment | NA | Only display kubernetes node information |
| pod | NA | Only display kubernetes node information |
| replication-controller | NA | Only display kubernetes node information |
| replica-set | NA | Only display kubernetes node information |
| service | NA | Only display kubernetes node information |
| connectivity | NA | Only display connectivity information for the daemon-set, deployment, or service |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| name | \<kube-cluster-name\>, \<kube-node-name\>, \<kube-ds-name\>, \<kube-deployment-name\>, \<kube-pod-name\>, \<kube-rc-name\>, \<kube-rs-name\>, \<kube-service-name\> | Only display results for the Kubernetes component with this name |
| components | NA | TBD |
| cluster | \<kube-cluster-name>\ | Only display results for the cluster with this name |
| label | \<kube-node-label\>, \<kube-ds-label\>, \<kube-deployment-label\>, \<kube-pod-label\>, \<kube-rc-label\>, \<kube-rs-label\>, \<kube-service-label\> | Only display results for components with this label |
| namespace | \<namespace\> | Only display results for clusters and nodes within this namespace |
| pod-ip | \<<kube-pod-ipaddress\> | Only display results for the pod with this IP address |
| service-cluster-ip | \<kube-service-cluster-ip\> | Only display results for the service cluster with this IP address |
| service-external-ip | \<kube-service-external-ip\> | Only display results for the service with this external IP address |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

Show health of clusters

```
cumulus@host:~$ netq show kubernetes cluster
Matching kube_cluster records:
Master                   Cluster Name     Controller Status    Scheduler Status Nodes
------------------------ ---------------- -------------------- ---------------- --------------------
server11:3.0.0.68        default          Healthy              Healthy          server11 server13 se
                                                                                rver22 server11 serv
                                                                                er12 server23 server
                                                                                24
server12:3.0.0.69        default          Healthy              Healthy          server12 server21 se
                                                                                rver23 server13 serv
                                                                                er14 server21 server
                                                                                22
```

Show health of pods

```
cumulus@host:~$ netq show kubernetes pod
Matching kube_pod records:
Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
server11:3.0.0.68        default      cumulus-frr-8vssx    3.0.0.70         server13     pod-template-generat Running  cumulus-frr:f8cac70bb217 Fri Feb  8 01:50:50 2019
                                                                                            ion:1 name:cumulus-f
                                                                                            rr controller-revisi
                                                                                            on-hash:3710533951
server11:3.0.0.68        default      cumulus-frr-dkkgp    3.0.5.135        server24     pod-template-generat Running  cumulus-frr:577a60d5f40c Fri Feb  8 01:50:50 2019
                                                                                            ion:1 name:cumulus-f
                                                                                            rr controller-revisi
                                                                                            on-hash:3710533951
server11:3.0.0.68        default      cumulus-frr-f4bgx    3.0.3.196        server11     pod-template-generat Running  cumulus-frr:1bc73154a9f5 Fri Feb  8 01:50:50 2019
                                                                                            ion:1 name:cumulus-f
                                                                                            rr controller-revisi
                                                                                            on-hash:3710533951
server11:3.0.0.68        default      cumulus-frr-gqqxn    3.0.2.5          server22     pod-template-generat Running  cumulus-frr:3ee0396d126a Fri Feb  8 01:50:50 2019
                                                                                            ion:1 name:cumulus-f
                                                                                            rr controller-revisi
                                                                                            on-hash:3710533951`
...
```

Show connectivity for a service

```
cumulus@host:~$ netq show kubernetes service name calico-etcd connectivity
    calico-etcd -- calico-etcd-pfg9r -- server11:swp1:torbond1 -- swp6:hostbond2:torc-11
                                     -- server11:swp2:torbond1 -- swp6:hostbond2:torc-12
                                     -- server11:swp3:NetQBond-2 -- swp16:NetQBond-16:edge01
                                     -- server11:swp4:NetQBond-2 -- swp16:NetQBond-16:edge02
    calico-etcd -- calico-etcd-btqgt -- server12:swp1:torbond1 -- swp7:hostbond3:torc-11
                                     -- server12:swp2:torbond1 -- swp7:hostbond3:torc-12
                                     -- server12:swp3:NetQBond-2 -- swp17:NetQBond-17:edge01
                                     -- server12:swp4:NetQBond-2 -- swp17:NetQBond-17:edge02
```

Refer to {{<link title="Monitor Container Environments Using Kubernetes API Server">}} for more usage examples.

### Related Commands

- netq config add agent kubernetes-monitor
- netq config del agent kubernetes-monitor
- netq config show agent kubernetes-monitor
- netq show impact kubernetes

- - -

## netq show impact kubernetes

Displays the impact on pods, services, replica sets or deployments when a specific ToR switch becomes unavilable.

{{<notice tip>}}
Kubernetes monitoring must be enabled on NetQ Agents. Refer to the <code>netq config add agent</code> command to enable monitoring.
{{</notice>}}

Outputs vary according to the component of the kubernetes cluster you want to view. The output is color coded (not shown in the examples) so you can clearly see the impact: green shows no impact, yellow shows partial impact, and red shows full impact. Use the `netq config add color` command to view the colored output.

### Syntax

```
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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| deployment | NA | Only display kubernetes node information |
| replica-set | NA | Only display kubernetes node information |
| service | NA | Only display kubernetes node information |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| master | \<kube-master-node\> | Only display results for the master node with this name |
| name | \<kube-deployment-name\>, \<kube-rs-name\>, \<kube-service-name\> | Only display results for the Kubernetes component with this name |
| cluster | \<kube-cluster-name>\ | Only display results for the cluster with this name |
| namespace | \<namespace\> | Only display results for clusters and nodes within this namespace |
| label | \<kube-node-label\>, \<kube-ds-label\>, \<kube-deployment-label\>, \<kube-pod-label\>, \<kube-rc-label\>, \<kube-rs-label\>, \<kube-service-label\> | Only display results for components with this label |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

Show impact on service availabilty based on the loss of particular node

```
cumulus@host:~$ netq server11 show impact kubernetes service name calico-etcd
calico-etcd -- calico-etcd-pfg9r -- server11:swp1:torbond1 -- swp6:hostbond2:torc-11
                                    -- server11:swp2:torbond1 -- swp6:hostbond2:torc-12
                                    -- server11:swp3:NetQBond-2 -- swp16:NetQBond-16:edge01
                                    -- server11:swp4:NetQBond-2 -- swp16:NetQBond-16:edge02
```

Show impact on the Kubernetes deployment if host or switch becomes unavailable

```
cumulus@host:~$ netq torc-21 show impact kubernetes deployment name nginx
nginx -- nginx-8586cf59-wjwgp -- server22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                -- server22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                -- server22:swp3:NetQBond-2 -- swp20:NetQBond-20:edge01
                                -- server22:swp4:NetQBond-2 -- swp20:NetQBond-20:edge02
        -- nginx-8586cf59-c82ns -- server12:swp2:NetQBond-1 -- swp23:NetQBond-23:edge01
                                -- server12:swp3:NetQBond-1 -- swp23:NetQBond-23:edge02
                                -- server12:swp1:swp1 -- swp6:VlanA-1:tor-1
        -- nginx-8586cf59-26pj5 -- server24:swp2:NetQBond-1 -- swp29:NetQBond-29:edge01
                                -- server24:swp3:NetQBond-1 -- swp29:NetQBond-29:edge02
                                -- server24:swp1:swp1 -- swp8:VlanA-1:tor-2

cumulus@server11:~$ netq server12 show impact kubernetes deployment name nginx
nginx -- nginx-8586cf59-wjwgp -- server22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                -- server22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                -- server22:swp3:NetQBond-2 -- swp20:NetQBond-20:edge01
                                -- server22:swp4:NetQBond-2 -- swp20:NetQBond-20:edge02
        -- nginx-8586cf59-c82ns -- server12:swp2:NetQBond-1 -- swp23:NetQBond-23:edge01
                                -- server12:swp3:NetQBond-1 -- swp23:NetQBond-23:edge02
                                -- server12:swp1:swp1 -- swp6:VlanA-1:tor-1
        -- nginx-8586cf59-26pj5 -- server24:swp2:NetQBond-1 -- swp29:NetQBond-29:edge01
                                -- server24:swp3:NetQBond-1 -- swp29:NetQBond-29:edge02
```

### Related Commands

- netq config add agent kubernetes-monitor
- netq config del agent kubernetes-monitor
- netq config show agent kubernetes-monitor
- netq config add color
- netq show kubernetes

- - -

## netq show lldp

Displays the health of all LLDP sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. You can filter the output to show sessions for a particular peer interface port. The output provides the following for each session:

- The interface on the local device
- The hostname and interface of the peer device
- When the last change was made to any of these items

### Syntax

```
netq [<hostname>] show lldp
    [<remote-physical-interface>]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<remote-physical-interface\> | Only display results for sessions using the interface port with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands

- netq show events
- netq check lldp

- - -

## netq show mac-commentary

Displays descriptive information about changes to a given MAC address on a specific VLAN. Commentary is provided for the following MAC address-related events:

- When a MAC address is configured or unconfigured
- When a bond enslaved or removed as a slave
- When bridge membership changes
- When a MAC address is learned or installed by control plane on tunnel interface
- When a MAC address is flushed or expires
- When a MAC address moves

### Syntax

```
netq [<hostname>] show mac-commentary
    <mac>
    vlan <1-4096>
    [between <text-time> and <text-endtime>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<mac\> | Display descriptive summary of MAC moves for this MAC address |
| vlan | \<1-4096\> | Display descriptive summary of MAC moves for the VLAN with this ID |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq show mac-commentary 44:38:39:be:ef:ff vlan 4002
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Thu Oct  1 14:25:18 2020  border01         4002   44:38:39:be:ef:ff configured on interface bridge
Thu Oct  1 14:25:18 2020  border02         4002   44:38:39:be:ef:ff configured on interface bridge
```

### Related Commands

- netq show mac-history
- netq show ip/ipv6 addresses

- - -

## netq show mac-history

Displays when a MAC address is learned, when and where it moved in the network after that, if there was a duplicate at any time, and so forth. By default, the various history threads are displayed in the output grouped by VLAN and timestamp (chronologically). You can filter the output based on the options used:

- Changes made between two points in time: use the `between` option
- Only the differences in the changes between two points in time: use the `diff` option
- The output grouped by selected output fields: use the `listby` option
- Each change that was made for the MAC address on a particular VLAN: use the `vlan` option

The default time range used is now to one hour ago. You can view the output in JSON format as well.

### Syntax

```
netq [<hostname>] show mac-history
    <mac>
    [vlan <1-4096>]
    [diff]
    [between <text-time> and <text-endtime>]
    [listby <text-list-by>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<mac\> | Display history for this MAC address |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| vlan | \<1-4096\> | Only display MAC changes for the VLAN with this ID |
| diff | NA | Only display the subset of changes that occurred within a time range defined by the `between` option |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| listby | \<text-list-by\> | Display output in groups based on the specified output field |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Introduced |

### Sample Usage

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

### Related Commands

- netq show mac-commentary
- netq show ip/ipv6 addresses

- - -

## netq show macs

Displays MAC addresses for monitored switches networkwide, currently or for a time in the past. For a given switch, you can view the total number of MAC addresses associated with that switch. You can filter the output based on VLAN, egress port, and origination status.

The output displays the following information for each MAC address:

- Whether this addresses is owned by the switch or learned from a peer
- VLAN associated with this address for a given switch
- Switch that uses this address
- Egress port on the switch
- When the last change was made to any of these items

This command does not show MAC addresses for hosts.

### Syntax

Three forms of this command are available: the basic command which shows all MAC addresses networkwide, one to  view MAC addresses or a count of addresses for a given switch, and one to view MAC addresses on a given switch and egress port.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch with this name |
| egress-port | \<egress-port\> | Only display results for the switch with this egress port |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<mac\> | Display history for this MAC address |
| vlan | \<1-4096\> | Only display MAC addresses that use the VLAN with this ID |
| origin | NA | Only display results for addresses that are owned by the specified switch or switches |
| count | NA | Display the total number of MAC addresses used by the specified switch; can only used when the `hostname` option is defined |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
|  | Introduced before 2.1 |

### Sample Usage

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

### Related Commands

- netq show mac-commentary
- netq show mac-history

- - -

## netq show mlag

Displays the health of all MLAG sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The peer nodes for a given node
- The system MAC address used for the session between the nodes
- The operational state of the session (up or down)
- The operational state of the backup IP address (up or down)
- The total number of bonds
- The number of dual-connected bonds
- When the last change was made to any of these items

If the total number of bonds does not match the number of dual-connected bonds, there might be a configuration issue.

### Syntax

```
netq [<hostname>] show mlag
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands

- netq show events type clag
- netq check mlag
- netq show unit-tests mlag

- - -

## netq show neighbor-history

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

### Syntax

```
netq [<hostname>] show neighbor-history
    <text-ipaddress>
    [ifname <text-ifname>]
    [diff]
    [between <text-time> and <text-endtime>]
    [listby <text-list-by>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch with this name |
| NA | \<text-ipaddress\> | Display history for this IPv4 or IPv6 address |
| ifname | \<text-ifname\> | Only display results for the interface with this name |
| diff | NA | Only display the differences associated with each change |
| between | \<text-time\> and \<text-endtime\> | Only display results between the snapshots taken at these times |
| listby | \<text-list-by\> | Display results by the specified attribute. Attributes include the interface name or index, VRF name, remote status, MAC address, if the address is an IPv6 address, and hostname. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

### Sample Usage

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

### Related Commands

- netq show address-history
- netq show mac-history

- - -

## netq show notification

Displays the configuration of notification channels, filters, rules, or the proxy (if configured). Email, PagerDuty, Slack, and syslog channels are supported. The output varies according to the component you want to view.

### Syntax

```
netq show notification
    (channel|filter|rule|proxy)
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| channel | NA | Display all channel configurations |
| filter | NA | Displayy all filter configurations |
| rule | NA | Display all rule configurations |
| proxy | NA | Display the proxy configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.2.x | Added `proxy` keyword |
| 2.1.2 | Introduced. Replaced the `netq config ts add notifier` command. |

### Sample Usage

Show notification channels

```
cumulus@netq-ts:~$ netq show notification channel

Matching config_notify records:
Name            Type             Severity         Channel Info
--------------- ---------------- ---------------- ------------------------
cloud-email    email            error            password: TEiO98BOwlekUP
                                                     TrFev2/Q==, port: 587,
                                                     isEncrypted: True,
                                                     host: netqsmtp.domain.com,
                                                     from: netqsmtphostlogin@doma
                                                     in.com,
                                                     id: smtphostlogin@domain
                                                     .com,
                                                     to: netq-notifications@d
                                                     omain.com
pd-netq-events  pagerduty        debug            integration_key: c6d666e
                                                  210a8425298ef7abde0d1998
slk-netq-events slack            debug            webhook: https://hooks.s
                                                  lack.com/services/text/m
                                                  oretext/evenmoretext
syslog-netq-eve syslog           debug            syslog_hostname: 10.10.2
nts                                               0.35, syslog_port: 514
```

Show filters

```
cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    swp52Drop       1          error            NetqDefaultChann swp52
                                                el
    bgpSpine        2          info             pd-netq-events   bgpHostnam
                                                                 e
    vni42           3          warning          pd-netq-events   evpnVni
    configChange    4          info             slk-netq-events  sysconf
    newFEC          5          info             slk-netq-events  fecSupport
    svcDown         6          critical         slk-netq-events  svcStatus
    critTemp        7          critical         onprem-email     overTemp
```

Show rules

```
cumulus@switch:~$ netq show notification rule
Matching config_notify records:
Name            Rule Key         Rule Value
--------------- ---------------- --------------------
bgpHostname     hostname         spine-01
evpnVni         vni              42
fecSupport      new_supported_fe supported
                c
overTemp        new_s_crit       24
svcStatus       new_status       down
swp52           port             swp52
sysconf         configdiff       updated
```

Show proxy

```
cumulus@switch:~$ netq show notification proxy
Matching config_notify records:
Proxy URL          Slack Enabled              PagerDuty Enabled
------------------ -------------------------- ----------------------------------
proxy4:80          yes                        yes
```

Refer to {{<link title="Configure System Event Notifications">}} for more detail about configuring notifications.

### Related Commands

- netq add notification
- netq del notification
- netq add tca
- netq del tca
- netq show tca

- - -

## netq show ntp

Displays whether the all or a specific node is in time synchronization with the NetQ appliance or VM currently or for a time in the past. The output provides:

- The synchronization status
- The current time server being used for synchronization
- The number of hierarchical levels the switch or host is from reference clock
- The NTP application used to obtain and synchronize the clock on the node

### Syntax

```
netq [<hostname>] show ntp
    [out-of-sync | in-sync]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| out-of-sync | NA | Only display results for devices that are out of synchronization with the NetQ appliance or VM |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq check ntp
- netq show unit-tests ntp

- - -

## netq show opta-health

Displays the status of the various applications and services running on the NetQ On-premises Appliance or the virtual machine. For the NetQ Cloud Appliance or VM, this command displays a simple statement indicating overall health.

Note that when running this command as part of an installation, it takes between 5 and 10 minutes for the applications and services to become fully operational.

### Syntax

```
netq show opta-health
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

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

### Related Commands

- netq show opta-platform

- - -

## netq show opta-platform

Displays the version of NetQ running on the switch, how long it has been running, and the last time it was re-initialized.

### Syntax

```
netq show opta-platform
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Modified keyword name from `platform` to `opta-platform` |
| 2.3.0 | Introduced as `netq show platform` |

### Sample Usage

```
cumulus@nswitch:~$ netq show opta-platform
Matching platform records:
Version                              Uptime                    Reinitialize Time
------------------------------------ ------------------------- --------------------------
3.2.0                                Fri Oct  2 22:04:17 2020  Wed Nov 11 21:53:57 2020

```

### Related Commands

- netq show opta-health

- - -
<!-- vale off -->
## netq show ospf
<!-- vale on -->
Displays the health of all OSPF sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The host interface
- The routing domain (area)
- Whether numbered or unnumbered protocol is being used
- The operational state of the session (up or down)
- The hostname and interface of the peer node
- When the last change was made to any of these items

### Syntax

```
netq [<hostname>] show ospf
    [<remote-interface>]
    [area <area-id>]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<remote-interface\> | Only display results for the host inteface with this name |
| area | \<area-id\> | Only display results for devices in this routing domain |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands
<!-- vale off -->
- netq show events
- netq check ospf
- netq show unit-tests ospf
<!-- vale on -->
- - -

## netq show recommended-pkg-version

When you have a software manifest in place, this command displays which software packages and versions are recommended for upgrade based on the installed Cumulus Linux release. You can then compare that to what is installed on your switch(es) to determine if it differs from the manifest. Such a difference might occur if one or more packages have been upgraded separately from the Cumulus Linux software itself.

The output provides the following information for each package:

- Hostname of the switch where the package resides
- Cumulus Linux release ID
- ASIC vendor supported
- CPU architecture supported
- Name and version of the package
- When the last change was made to any of these items

### Syntax

<!-- vale off -->
```
netq [<hostname>] show recommended-pkg-version
    [release-id <text-release-id>]
    [package-name <text-package-name>]
    [json]
```
<!-- vale on -->

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch with this name |
| release-id | \<text-release-id\> | Only display results for the Cumulus Linux release with this ID; x.y.z format |
| package-name | \<text-package-name\> | Only display results for the software package with this name |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

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

### Related Commands

- netq show cl-manifest
- netq show cl-pkg-info

- - -

## netq show resource-util

Displays the utilization of compute resources&mdash;CPU, disk and memory&mdash;consumed by one or all switches and hosts in your network.

The output provides the following information for each switch or host:

- Hostname of the device
- CPU utilization for one or all devices
- Memory utilization for one or all devices
- Disk name
- Total disk storage, amount used, and percentage of total
- When the last change was made to any of these items

### Syntax

Two forms of this command are available; one for CPU and memory utilization, and one for disk utilization.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| disk | \<text-diskname\> | Display disk utilization |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the device with this name |
| cpu | NA | Display utilization for CPUs on one or more devices |
| memory | NA | Display utilization for memory on one or more devices |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

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

### Related Commands

- netq show cl-resource forwarding
- netq show cl-resource acl

- - -

## netq show sensors

Displays the status of all fan, power supply, and temperature sensors on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The sensor name and user-defined description
- The operational state of the sensor
- Any messages, when available
- When the last change was made to any of these items

### Syntax

Four forms of this command are available based on whether you want to view data for all sensors or only one category of sensors.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| all | NA | Display data for all sensors |
| fan | \<fan-name\> | Display data for all fan sensors or the one specified using the `fan-name` value |
| psu | \<psu-name\> | Display data for all power supply unit sensors or the one specified using the`psu-name` value |
| temp | \<temp-name\> | Display data for all temperature sensors or the one specified using the `temp-name` value |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show events
- netq check sensors
- netq show unit-tests sensors

- - -

## netq show services

Displays configuration and health of system-level services for one or all switches and hosts, currently or for a time in the past. You can filter the output by switch, service, VRF, and status. Supported services include:
<!-- vale off -->
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
- **syslog**: System event logging service
- **vrf**: VRF (Virtual Route Forwarding) service
- **zebra**: GNU Zebra routing daemon
<!-- vale on -->
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

### Syntax

Two forms of this command are available; one for all information, and one for a particular status.

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

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| status | ok, warning, error, fail | Only display services with this status |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<service-name\> | Only display results for the service with this name (refer to above list) |
| vrf | \<vrf\> | Only display results for services using this VRF |
| active | NA | Only display results for currently running services |
| monitored | NA | Only display results for monitored services |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

None

- - -

## netq show tca

Displays the configuration information for all user-specified threshold-based event notifications. You can filter the output by the identifier of the configuration. The output provides the following information for each notification configuration:

- Configuration name
- Name of the event being managed
- Scope indicating what is to be included or excluded from management by this configuration
- Event severity
- Channels that receive the events
- Whether the configuration is currently active, disabled, or suppressed
- Threshold value, unit of measure, and type
- When suppression of these events ends (if configured)

### Syntax

```
netq show tca
    [tca_id <text-tca-id-anchor>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| tca_id | \<text-tca-id-anchor\> | Only display results for the configuration with this ID/name |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

Show all TCA event configurations

```
cumulus@switch:~$ netq show tca
Matching config_tca records:
TCA Name                     Event Name           Scope                      Severity Channel/s          Active Threshold          Unit     Threshold Type Suppress Until
---------------------------- -------------------- -------------------------- -------- ------------------ ------ ------------------ -------- -------------- ----------------------------
TCA_CPU_UTILIZATION_UPPER_1  TCA_CPU_UTILIZATION_ {"hostname":"leaf01"}      info     pd-netq-events,slk True   87                 %        user_set       Fri Oct  9 15:39:35 2020
                             UPPER                                                    -netq-events
TCA_CPU_UTILIZATION_UPPER_2  TCA_CPU_UTILIZATION_ {"hostname":"*"}           critical slk-netq-events    True   93                 %        user_set       Fri Oct  9 15:39:56 2020
                             UPPER
TCA_DOM_BIAS_CURRENT_ALARM_U TCA_DOM_BIAS_CURRENT {"hostname":"leaf*","ifnam critical slk-netq-events    True   0                  mA       vendor_set     Fri Oct  9 16:02:37 2020
PPER_1                       _ALARM_UPPER         e":"*"}
TCA_DOM_RX_POWER_ALARM_UPPER TCA_DOM_RX_POWER_ALA {"hostname":"*","ifname":" info     slk-netq-events    True   0                  mW       vendor_set     Fri Oct  9 15:25:26 2020
_1                           RM_UPPER             *"}
TCA_SENSOR_TEMPERATURE_UPPER TCA_SENSOR_TEMPERATU {"hostname":"leaf","s_name critical slk-netq-events    True   32                 degreeC  user_set       Fri Oct  9 15:40:18 2020
_1                           RE_UPPER             ":"temp1"}
TCA_TCAM_IPV4_ROUTE_UPPER_1  TCA_TCAM_IPV4_ROUTE_ {"hostname":"*"}           critical pd-netq-events     True   20000              %        user_set       Fri Oct  9 16:13:39 2020
                             UPPER
```

Show a specific TCA configuration

```
cumulus@switch:~$ netq show tca tca_id TCA_TXMULTICAST_UPPER_1
Matching config_tca records:
TCA Name                     Event Name           Scope                      Severity         Channel/s          Active Threshold          Suppress Until
---------------------------- -------------------- -------------------------- ---------------- ------------------ ------ ------------------ ----------------------------
TCA_TXMULTICAST_UPPER_1      TCA_TXMULTICAST_UPPE {"ifname":"swp3","hostname info             tca-tx-bytes-slack True   0                  Sun Dec  8 16:40:14 2269
                             R                    ":"leaf01"}
```

### Related Commands

- netq add tca
- netq del tca
- netq show notification

- - -

## netq show trace

Displays the configuration settings for a given scheduled trace, summary results of all scheduled traces, or full results of scheduled traces. Use the summary form to obtain the job ID. The output varies based on the form of the command. Note that on-demand trace results are shown in the terminal window when the command is run.

### Syntax

Three forms of this command are available.

```
netq show trace results <text-job-id>
    [json]

netq show trace settings
    [name <text-trace-name>]
    [json]

netq show trace summary
    [name <text-trace-name>]
    [around <text-time-hr>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| results | NA | Display the full results, including the available paths, for all scheduled trace requests |
| NA | \<text-job-id\> | Only display results for the trace request with this job ID |
| settings | NA | Display trace configuration settings for a given trace request |
| summary | NA | Display only the name, job ID, status, and duration of all scheduled trace results currently or at a time in the past |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| name | \<text-trace-name\> | Only display summary results or configuration settings for the trace with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

Show full results for given trace

```
cumulus@switch:~$ netq show trace summary name Lf01toBor01Daily json
cumulus@switch:~$ netq show trace results f501f9b0-cca3-4fa1-a60d-fb6f495b7a0e
```

Show configuration settings

```
cumulus@switch:~$ netq show trace settings name Lf01toBor01Daily
```

Show summary results for last 24 hours

```
cumulus@switch:~$ netq show trace summary
Name            Job ID       Status           Status Details               Start Time           End Time
--------------- ------------ ---------------- ---------------------------- -------------------- ----------------
leaf01toborder0 f8d6a2c5-54d Complete         0                            Fri Nov  6 15:04:54  Fri Nov  6 15:05
1               b-44a8-9a5d-                                               2020                 :21 2020
                9d31f4e4701d
New Trace       0e65e196-ac0 Complete         1                            Fri Nov  6 15:04:48  Fri Nov  6 15:05
                5-49d7-8c81-                                               2020                 :03 2020
                6e6691e191ae
Svr01toSvr04Hrl 4c580c97-8af Complete         0                            Fri Nov  6 15:01:16  Fri Nov  6 15:01
y               8-4ea2-8c09-                                               2020                 :44 2020
                038cde9e196c
Abc             c7174fad-71c Complete         1                            Fri Nov  6 14:57:18  Fri Nov  6 14:58
                a-49d3-8c1d-                                               2020                 :11 2020
                67962039ebf9
Lf01toBor01Dail f501f9b0-cca Complete         0                            Fri Nov  6 14:52:35  Fri Nov  6 14:57
y               3-4fa1-a60d-                                               2020                 :55 2020
                fb6f495b7a0e
L01toB01Daily   38a75e0e-7f9 Complete         0                            Fri Nov  6 14:50:23  Fri Nov  6 14:57
                9-4e0c-8449-                                               2020                 :38 2020
                f63def1ab726
leaf01toborder0 f8d6a2c5-54d Complete         0                            Fri Nov  6 14:34:54  Fri Nov  6 14:57
1               b-44a8-9a5d-                                               2020                 :20 2020
                9d31f4e4701d
leaf01toborder0 f8d6a2c5-54d Complete         0                            Fri Nov  6 14:04:54  Fri Nov  6 14:05
1               b-44a8-9a5d-                                               2020                 :20 2020
                9d31f4e4701d
New Trace       0e65e196-ac0 Complete         1                            Fri Nov  6 14:04:48  Fri Nov  6 14:05
                5-49d7-8c81-                                               2020                 :02 2020
                6e6691e191ae
Svr01toSvr04Hrl 4c580c97-8af Complete         0                            Fri Nov  6 14:01:16  Fri Nov  6 14:01
y               8-4ea2-8c09-                                               2020                 :43 2020
                038cde9e196c
...
L01toB01Daily   38a75e0e-7f9 Complete         0                            Thu Nov  5 15:50:23  Thu Nov  5 15:58
                9-4e0c-8449-                                               2020                 :22 2020
                f63def1ab726
leaf01toborder0 f8d6a2c5-54d Complete         0                            Thu Nov  5 15:34:54  Thu Nov  5 15:58
1               b-44a8-9a5d-                                               2020                 :03 2020
                9d31f4e4701d
```

### Related Commands

- netq add trace
- netq del trace
- netq trace (on-demand)
- netq show events type trace

- - -

## netq show unit-tests

Displays a list of all validation tests that are run for the associated `netq check` command. The output provides an ID, name, and brief description of each validation test.

Refer to {{<link title="Validate Operations" text="Validate Operations">}} for additional usage information.

### Syntax

```
netq show unit-tests agent [json]
netq show unit-tests bgp [json]
netq show unit-tests clag [json]
netq show unit-tests cl-version [json]
netq show unit-tests evpn [json]
netq show unit-tests interfaces [json]
netq show unit-tests mlag [json]
netq show unit-tests mtu [json]
netq show unit-tests ntp [json]
netq show unit-tests ospf [json]
netq show unit-tests sensors [json]
netq show unit-tests vlan [json]
netq show unit-tests vxlan [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| <!-- vale off -->agent, bgp, clag, cl-version, evpn, interfaces, mlag, mtu, ntp, ospf, sensors, vlan, or vxlan<!-- vale on --> | NA | Display tests run during standard validation for the protocol or service with this name |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Swapped the order of the `unit-tests` keyword and the protocol or service name |
| 2.3.1 | Introduced |

### Sample Usage

Show tests for BGP

```
cumulus@netq-ts:~$ netq show unit-tests bgp
   0 : Session Establishment     - check if BGP session is in established state
   1 : Address Families          - check if tx and rx address family advertisement is consistent between peers of a BGP session
   2 : Router ID                 - check for BGP router id conflict in the network

Configured global result filters:

Configured per test result filters:
```

### Related Commands

- netq show events
- netq check sensors

- - -

## netq show validation settings

Displays one or all scheduled validations, including their name, type, cadence, when the validation began, when it was created, and whether it is currently active. This is useful for obtaining the name of a scheduled validations for use in other validation commands.

### Syntax

```
netq show validation settings
    [name <text-validation-name>]
    [type agents|bgp|evpn|interfaces|mlag|mtu|ntp|ospf|sensors|vlan|vxlan]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| name | \<text-validation-name\> | Filter output to view settings for the scheduled validation with this name |
| type | <!-- vale off -->agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, sensors, vlan, or vxlan<!-- vale on --> | Filter output to view settings for only the indicated protocol or service |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

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
```

### Related Commands

- netq add validation name
- netq del validation
- netq show validation summary

- - -

## netq show validation summary

Displays summary status of a scheduled validation for a given protocol or service, including their name, type, job ID, number of nodes validated, number of nodes that failed validation, number of nodes running the protocol or service, and time when the validation was run.

### Syntax

```
netq show validation summary
    [name <text-validation-name>]
    type (agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | sensors | vlan | vxlan)
    [around <text-time-hr>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| type | <!-- vale off -->agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, sensors, vlan or vxlan <!-- vale on --> | Show validation runs summary for the indicated protocol or service |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| name | \<text-validation-name\> | Filter output to view settings for the scheduled validation with this name |
| around | \<text-time-hr\> | Show summary status for this time in the past. Value must be specified in hours and include the *h* time unit. Default is 24 hours. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

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

### Related Commands

- netq add validation name
- netq del validation
- netq show validation settings

- - -

## netq show vlan

Displays the configuration of all VLANs on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The switch or hostname
- The VLANs associated with that node
- The SVIs (switch virtual interfaces) associated with that node
- When the last change was made to any of these items

### Syntax

```
netq [<hostname>] show vlan
    [<1-4096>]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<1-4096\> | Only display results for the VLAN with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands

- netq show events
- netq show interfaces
- netq show macs
- netq check vlan
- netq show unit-tests vlan

- - -
<!-- vale off -->
## netq show vxlan
<!-- vale on -->
Displays the configuration of all VXLANs on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The switch or hostname
- The VNI associated with that node
- The protocol used over the interface
- The VTEP IP for the node
- The replication list, if appropriate
- When the last change was made to any of these items

### Syntax

```
netq [<hostname>] show vxlan
    [vni <text-vni>]
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| <!-- vale off -->vni | \<text-vni\><!-- vale on --> | Only display results for the VNI with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

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

### Related Commands
<!-- vale off -->
- netq show events
- netq show interfaces
- netq check vxlan
- netq show unit-tests vxlan
<!-- vale on -->
- - -

## netq show wjh-drops

Displays packet drops due to buffer congestion, incorrect routing, tunnel, ACL and layer 1 and 2 problems that are captured by the WJH (What just happened) feature on NVIDIA switches. You can filter all drops by ingress port and severity. You can filter drops of a particular type by various attributes. The output varies according to the type of drop. Refer to the {{<link title="WJH Event Messages Reference">}} for descriptions of the supported drop reasons.

{{<notice note>}}
Cumulus Linux 4.0.0 or later and NetQ Agent 2.4.0 or later are required to view this drop information. The NetQ Agent must also be configured to collect this data.

Additionally, using <em>wjh_dump.py</em> on a NVIDIA platform that is running Cumulus Linux 4.0 and the NetQ 2.4.0 Agent causes the NetQ WJH client to stop receiving packet drop call backs. To prevent this issue, run <em>wjh_dump.py</dm> on a different system than the one where the NetQ Agent has WJH enabled, or disable <em>wjh_dump.py</em> and restart the NetQ Agent.
{{</notice>}}

### Syntax

<!-- vale off -->
```
netq [<hostname>] show wjh-drop
    [ingress-port <text-ingress-port>]
    [severity <text-severity>]
    [details]
    [between <text-time> and <text-endtime>]
    [around <text-time>]
    [json]

netq [<hostname>] show wjh-drop <text-drop-type>
    [ingress-port <text-ingress-port>]
    [severity <text-severity>]
    [reason <text-reason>]
    [src-ip <text-src-ip>]
    [dst-ip <text-dst-ip>]
    [proto <text-proto>]
    [src-port <text-src-port>]
    [dst-port <text-dst-port>]
    [src-mac <text-src-mac>]
    [dst-mac <text-dst-mac>]
    [egress-port <text-egress-port>]
    [traffic-class <text-traffic-class>]
    [rule-id-acl <text-rule-id-acl>]
    [between <text-time> and <text-endtime>]
    [around <text-time>]
    [json]
```
<!-- vale on -->

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-drop-type\> | Only display results for this category of drops |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display drops for the switch or host with this name |
| ingress-port | \<text-ingress-port\> | Only display drops for the ingress port with this name |
| severity | \<text-severity\> | Only display drops with this severity; *error*, *warning*, or *notice* |
| details | NA | Display drop count and reason for all drop types |
| reason | \<text-reason\> | Only display drops with this reason |
| src-ip | \<text-src-ip\> | Only display drops with this source IP address |
| dst-ip | \<text-dst-ip\> | Only display drops with this destination IP address |
| proto | \<text-proto\> | Only display drops from the protocol with this name |
| src-port | \<text-src-port\> | Only display drops with this source port name |
| dst-port | \<text-dst-port\> | Only display drops with this destination port name |
| src-mac | \<text-src-mac\> | Only display drops with this source MAC address |
| dst-mac | \<text-dst-mac\> | Only display drops with this destination MAC address |
| egress-port | \<text-egress-port\> | Only display drops for the egress port with this name |
| traffic-class | \<text-traffic-class\> | Only display drops with this traffic class |
| rule-id-acl | \<text-rule-id-acl\> | Only display ACL drops with this rule ID |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>The start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Removed `changes` option. Use `netq show events` command instead. |

### Sample Usage

Show drops for a given switch or host

```
cumulus@switch:~$ netq leaf03 show wjh-drop between now and 7d
Matching wjh records:
Drop type          Aggregate Count
------------------ ------------------------------
L1                 560
Buffer             224
Router             144
L2                 0
ACL                0
Tunnel             0
```

Show drops for a particular drop type

```
cumulus@mlx-2700-03:mgmt:~$ netq show wjh-drop l2
Matching wjh records:
Hostname          Ingress Port             Reason                                        Agg Count          Src Ip           Dst Ip           Proto  Src Port         Dst Port         Src Mac            Dst Mac            First Timestamp                Last Timestamp
----------------- ------------------------ --------------------------------------------- ------------------ ---------------- ---------------- ------ ---------------- ---------------- ------------------ ------------------ ------------------------------ ----------------------------
mlx-2700-03       swp1s2                   Port loopback filter                          10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  0c:ff:ff:ff:ff:ff  Mon Dec 16 11:54:15 2019       Mon Dec 16 11:54:15 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:53:17 2019       Mon Dec 16 11:53:17 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 0.0.0.0          0.0.0.0          0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:40:44 2019       Mon Dec 16 11:40:44 2019
```

Show drops of a given severity

```
cumulus@switch:~$ netq show wjh-drop acl
Matching wjh records:
Hostname          Ingress Port             Reason                                        Severity         Agg Count          Src Ip           Dst Ip           Proto  Src Port         Dst Port         Src Mac            Dst Mac            Acl Rule Id            Acl Bind Point               Acl Name         Acl Rule         First Timestamp                Last Timestamp
----------------- ------------------------ --------------------------------------------- ---------------- ------------------ ---------------- ---------------- ------ ---------------- ---------------- ------------------ ------------------ ---------------------- ---------------------------- ---------------- ---------------- ------------------------------ ----------------------------
leaf01            swp2                     Ingress router ACL                            Error            49                 55.0.0.1         55.0.0.2         17     8492             21423            00:32:10:45:76:89  00:ab:05:d4:1b:13  0x0                    0                                                              Tue Oct  6 15:29:13 2020       Tue Oct  6 15:29:39 2020
```

### Related Commands

- netq config add agent wjh
- netq config add agent wjh-threshold
- netq config add agent wjh-drop-filter
- netq config restart agent

- - -
<!-- vale NVIDIA.HeadingTitles = YES -->