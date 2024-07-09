---
title: show
author: Cumulus Networks
weight: 1106
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
## netq show adaptive-routing config

Displays a list of switches that are running adaptive routing and RoCE settings for those switches. The second form of this command displays whether or not adaptive routing is running at the interface-level.
### Syntax

```
netq [<hostname>] show adaptive-routing config global 
    [between <text-time> and <text-endtime>] 
    [around <text-time>]
    [json]
```
```
netq [<hostname>] show adaptive-routing config interface 
    [<text-ifname>] 
    [between <text-time> and <text-endtime>] 
    [around <text-time>] 
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| NA | \<text-ifname\> | Only display results for the interface with this name |
| between | \<text-time\> and \<text-endtime\> | Only display results between the snapshots taken at these times |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq show adaptive-routing config global

Matching arconfig records:
Hostname          Is AR   Is RoCE  RoCE Mode Last Updated
                  Enabled Enabled
----------------- ------- -------- --------- --------------------------
torc-11           False   True     Lossy     Wed Oct 25 13:11:23 2023
torc-12           True    True     Lossless  Tue Oct 24 15:32:33 2023
```

```
cumulus@switch:~$ netq show adaptive-routing config interface

Matching arconfig records:
Hostname          Interface Is AR   Link Util  Link Util  Last Updated
                            Enabled Threshold  Threshold
                                    Disabled
----------------- --------- ------- ---------- ---------- --------------------------
torc-11           swp1      True    True       70         Tue Oct 24 15:32:33 2023
torc-11           swp2      False   True       60         Wed Oct 25 13:07:21 2023
torc-12           swp2      True    True       70         Tue Oct 24 15:32:33 2023
torc-12           swp1      True    True       70         Tue Oct 24 15:32:33 2023
```

### Related Commands

None

- - -
## netq show address-history
<!-- vale on -->

Displays where an IPv4 or IPv6 address has lived in your network fabric in the last 24 hours. The output displays:

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
| json | NA | Display the output in JSON format |

{{<notice note>}}
When entering a time value with the <code>between</code> option, you must include a numeric value <em>and</em> the unit of measure:
<ul>
<li><strong>d</strong>: days</li>
<li><strong>h</strong>: hours</li>
<li><strong>m</strong>: minutes</li>
<li><strong>s</strong>: seconds</li>
<li><strong>now</strong>
</ul>

You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{</notice>}}

### Sample Usage

Display address history for the past 24 hours:

```
cumulus@switch:~$ netq show address-history 10.10.10.3
Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Mon Nov 23 22:28:42 2020  leaf03            lo           10.10.10.3                     32       default
```

The following example displays a full chronology of changes for an IP address. A caret (^) notation indicates that the value from the row preceding it has not changed.

```
cumulus@switch:~$ netq show address-history 10.1.10.2/24

Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Tue Sep 29 15:35:21 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 15:35:24 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:07 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:08 2020  leaf01            vlan10       10.1.10.2                      24       RED
```

Show changes grouped by VRF:

```
cumulus@switch:~$ netq show address-history 10.1.10.104 listby vrf
Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Tue Nov 24 19:51:11 2020  server04          uplink       10.1.10.104                    24       default
```
The following example displays the history of an IP address between now and two hours ago. A caret (^) notation indicates that the value from the row preceding it has not changed.

```
cumulus@switch:~$ netq show address-history 10.1.10.2/24 between 2h and now

Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Tue Sep 29 15:35:21 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 15:35:24 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:07 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:08 2020  leaf01            vlan10       10.1.10.2                      24       RED
```
### Related Commands

- ```netq show mac-history```

- - -

## netq show agents

Displays basic configuration, health, and connectivity status for all nodes or a specific node running NetQ Agent in your network fabric. This command gives you an easy way to see if any NetQ Agents or their nodes have lost power, if they have difficulty communicating with the telemetry server, or whether agents are running different software versions.

The output displays:

<!-- vale off -->
- Whether each node has communicated recently (last 120 seconds)
- If each node is in time synchronization with the NetQ appliance or virtual machine
- The NetQ Agent software version currently running on the node
- How long the node has been operationally up
- How long the NetQ Agent has been operationally up
- The last time the NetQ Agent was reinitialized
- When the last change occurred for any of the above items
<!-- vale on -->

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
| dead | NA | Filter output for devices where a user decommissioned the NetQ Agent |
| rotten | NA | Filter output for devices where the NetQ Agent has not communicated with the appliance or VM in the last two minutes |
| opta | NA | Filter output for the NetQ Agent installed on the appliance or VM |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display agent status across all network nodes:

```
cumulus@switch:~$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
exit-1            Fresh            yes      4.11.0-cl4u48~1719858419.3db6af0a5   Mon Jul  1 19:29:33 2024  Mon Jul  1 20:11:31 2024  Mon Jul  8 18:33:15 2024   Tue Jul  9 15:13:14 2024
exit-2            Fresh            yes      4.11.0-cl4u48~1719858419.3db6af0a5   Mon Jul  1 19:29:34 2024  Mon Jul  1 20:11:52 2024  Mon Jul  8 18:33:12 2024   Tue Jul  9 15:13:17 2024
firewall-1        Fresh            yes      4.11.0-cl4u48~1719858419.3db6af0a5   Mon Jul  1 19:29:32 2024  Mon Jul  1 20:12:13 2024  Mon Jul  8 18:33:07 2024   Tue Jul  9 15:13:02 2024
firewall-2        Fresh            yes      4.11.0-cl4u48~1719858419.3db6af0a5   Mon Jul  1 19:29:32 2024  Mon Jul  1 20:12:42 2024  Mon Jul  8 18:33:13 2024   Tue Jul  9 15:13:05 2024
hostd-11          Fresh            yes      4.11.0-ub18.04u48~1719859179.3db6af0 Mon Jul  1 20:01:50 2024  Mon Jul  1 20:12:59 2024  Mon Jul  8 18:33:15 2024   Tue Jul  9 15:13:02 2024
hostd-21          Fresh            yes      4.11.0-ub18.04u48~1719859179.3db6af0 Mon Jul  1 20:02:50 2024  Mon Jul  1 20:13:15 2024  Mon Jul  8 18:32:52 2024   Tue Jul  9 15:13:11 2024
hosts-11          Fresh            yes      4.11.0-ub18.04u48~1719859179.3db6af0 Mon Jul  1 20:03:47 2024  Mon Jul  1 20:13:31 2024  Mon Jul  8 18:33:16 2024   Tue Jul  9 15:13:21 2024
hosts-13          Fresh            yes      4.11.0-ub18.04u48~1719859179.3db6af0 Mon Jul  1 20:04:48 2024  Mon Jul  1 20:13:46 2024  Mon Jul  8 18:33:18 2024   Tue Jul  9 15:13:08 2024
hosts-21          Fresh            yes      4.11.0-ub18.04u48~1719859179.3db6af0 Mon Jul  1 20:05:54 2024  Mon Jul  1 20:13:59 2024  Mon Jul  8 18:33:21 2024   Tue Jul  9 15:13:20 2024
...
```

Display all devices in a rotten state:

```
cumulus@switch:~$ netq show agents rotten
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
fw1               Rotten           no       3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:36:33 2020  Mon Nov  2 19:49:21 2020  Mon Nov  2 19:49:21 2020   Fri Nov 20 18:48:53 2020
fw2               Rotten           no       3.2.0-cl4u30~1601403318.104fb9ed     Fri Oct  2 20:36:32 2020  Mon
```

### Related Commands

- ```netq show unit-tests agent```
- ```netq show events```
- ```netq check agents```
- ```netq config add agent```
- ```netq config del agent```

- - -

<!-- vale off -->
## netq show bgp
<!-- vale on -->

Displays the health of all BGP sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

<!-- vale off -->
- The neighbor nodes for a given node
- What routing tables (VRF) that node and neighbor used
- The autonomous system number (ASN) assigned to the node
- The peer ASN for each neighbor node
- The received address prefix for IPv4/IPv6/EVPN when the session is established
- When the last change occurred for any of these items
<!-- vale on -->

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
| NA | <!-- vale off -->\<bgp-session\><!-- vale on --> | Only display results for this particular BGP session (for example, 5468354) |
| asn | \<number-asn\> | Only display results for nodes using this ASN (for example, 65013) |
| vrf | \<vrf\> | Only display results for sessions run on this VRF (for example, default, mgmt, or vrf10) |
| established | NA | Only display established BGP sessions |
| failed | NA | Only display failed BGP sessions |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display BGP sessions across all network nodes. This example shows each node, their neighbor, VRF, ASN, peer ASN, received address IPv4/IPv6/EVPN prefix, and the last time something changed.


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
...
```

View status of nodes running BGP with a given ASN:

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
- ```netq show unit-tests bgp```
- ```netq show events```
- ```netq check bgp```
<!-- vale on -->
- - -


## netq show check-filter

Displays filters currently applied to `netq check` commands. Refer to {{<link title="Validation Checks/#validation-check-result-filtering">}} for more information about suppressing tests associated with `netq check` commands.

Use this command to display check filter IDs, which must be specified when adding filters to a `netq check` command.

### Syntax

```
netq show check-filter 
    [check_filter_id <text-check-filter-id>|check_name <text-check-name-anchor>] 
    [show-check-catalog | check_name <text-check-name-anchor> show-check-catalog | check_name <text-check-name-anchor> show-reason-catalog ] 
    [json] 
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| check_filter_id | \<text-check-filter-id\> | Only display filters with a given ID |
| check_name | \<text-check-name-anchor\> |  Only display filters for a given validation test (for example, EVPN, BGP, etc.) |
| show-check-catalog | NA | Display conditions for the check type |
| show-reason-catalog | NA | Display the explanation associated with validation test errors and warnings  |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq show check-filter
Matching config_check records:
Check Filter ID      Check Name           Test Name            Scope                                                        Active Suppress Until
-------------------- -------------------- -------------------- ------------------------------------------------------------ ------ --------------------
roce_3               roce                 RoCE Classification  [{"Reason":"Invalid traffic-class mapping for switch-priority 4.Expected 0 Got 3"}]          
True   Sun May  4 09:20:54 2025   
```

### Related Commands

- `netq add check-filter`
- `netq check`
- `netq del check-filter`

- - -
## netq show cl-btrfs-info


Displays status about disk utilization on a given device or all devices networkwide with BTRFS and Cumulus Linux 3.x installed. The output provides the following information for each device:

- Percentage of disk currently allocated
- Amount of space remaining (unallocated)
- Size of the largest data chunk
- Amount of space unused by data chunks
- Whether the disk requires a rebalance
- When the last change occurred for any of these items

For details about when to perform a recommended rebalance, refer to [When to Rebalance BTRFS Partitions]({{<ref "/knowledge-base/Configuration-and-Usage/Storage/When-to-Rebalance-BTRFS-Partitions">}}).

### Syntax

```
netq [<hostname>] show cl-btrfs-info
    [around <text-time>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display disk utilization info:

```
cumulus@switch:~$ netq show cl-btrfs-info
Matching btrfs_info records:
Hostname          Device Allocated     Unallocated Space    Largest Chunk Size   Unused Data Chunks S Rebalance Recommende Last Changed
                                                                                 pace                 d
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf01            37.79 %              3.58 GB              588.5 MB             771.91 MB            yes                  Wed Sep 16 21:25:17 2020
```
Look for the **Rebalance Recommended** column. If the value in that column says *Yes*, then you are strongly encouraged to rebalance the BTRFS partitions. If it says *No*, then you can review the other values in the output to determine if you are getting close to needing a rebalance, and come back to view this data at a later time.
### Related Commands

- ```netq show cl-ssd-util```

- - -

<!-- vale off -->
## netq show cl-manifest
<!-- vale on -->

Displays the Cumulus Linux OS versions supported for a given device or all devices networkwide. The output provides the following information for each device:

- ASIC vendor the OS supports
- CPU architecture the OS supports
- Cumulus Linux version associated with the indicated ASIC and CPU
{{<notice note>}}
This command is supported on switches running Cumulus Linux 4.4.5 and earlier.
{{</notice>}}
### Syntax

```
netq [<hostname>] show cl-manifest
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| json | NA | Display the output in JSON format |

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

- ```netq show cl-pkg-info```
- ```netq show recommended-pkg-version```

- - -

<!-- vale off -->
## netq show cl-pkg-info
<!-- vale on -->

Displays the versions for all software packages installed on a given device or all devices networkwide. The output provides the following information for each device:

- Package name and version
- Cumulus Linux version
- Package status
- When the last change occurred for any of these items

The output can become very large for all devices and packages. When viewing results in a terminal window, consider filtering by hostname or package name to reduce the length of the output. Wildcards are not allowed for `hostname` or `text-package-name`.

### Syntax

```
netq [<hostname>] show cl-pkg-info
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
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq leaf01 show cl-pkg-info

Matching package_info records:
Hostname          Package Name             Version              CL Version           Package Status       Last Changed
----------------- ------------------------ -------------------- -------------------- -------------------- -------------------------
leaf01            freeipmi-common          1.6.3-1.1            Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            libsystemd0              241-7~deb10u4        Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
leaf01            arptables                0.0.4+snapshot201810 Cumulus Linux 4.2.1  installed            Tue Dec  1 22:38:39 2020
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

- ```netq show recommended-pkg-version```
- ```netq show cl-manifest```

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
    - When the last change occurred for any of these items
- For forwarding resources
    - Count and percentage of MAC address entries
    - Count and percentage of ECMP next hops
    - Count and percentage of IPv4/IPv6 host and route entries
    - Number of multicast routes
    - When the last change occurred for any of these items

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display the ACL resources for all configured switches:

```
cumulus@switch:~$ netq show cl-resource acl
Matching cl_resource records:
Hostname          In IPv4 filter       In IPv4 Mangle       In IPv6 filter       In IPv6 Mangle       In 8021x filter      In Mirror            In PBR IPv4 filter   In PBR IPv6 filter   Eg IPv4 filter       Eg IPv4 Mangle       Eg IPv6 filter       Eg IPv6 Mangle       ACL Regions          18B Rules Key        32B Rules Key        54B Rules Key        L4 Port range Checke Last Updated
                                                                                                                                                                                                                                                                                                                                                                  rs
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
act-5712-09       40,512(7%)           0,0(0%)              30,768(3%)           0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              32,256(12%)          0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              2,24(8%)             Tue Aug 18 20:20:39 2020
mlx-2700-04       0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              4,400(1%)            2,2256(0%)           0,1024(0%)           2,1024(0%)           0,0(0%)              Tue Aug 18 20:19:08 2020
```

Display forwarding resources for all configured switches:

```
cumulus@noc-pr:~$ netq show cl-resource forwarding
Matching cl_resource records:
Hostname          IPv4 host entries    IPv6 host entries    IPv4 route entries   IPv6 route entries   ECMP nexthops        MAC entries          Total Mcast Routes   Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
act-5712-09       0,16384(0%)          0,0(0%)              0,131072(0%)         23,20480(0%)         0,16330(0%)          0,32768(0%)          0,8192(0%)           Tue Aug 18 20:20:39 2020
mlx-2700-04       0,32768(0%)          0,16384(0%)          0,65536(0%)          4,28672(0%)          0,4101(0%)           0,40960(0%)          0,1000(0%)           Tue Aug 18 20:19:08 2020
```

Display the forwarding resources used by the *spine02* switch:

```
cumulus@switch:~$ netq spine02 show cl-resource forwarding
Matching cl_resource records:
Hostname          IPv4 host entries    IPv6 host entries    IPv4 route entries   IPv6 route entries   ECMP nexthops        MAC entries          Total Mcast Routes   Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
spine02           9,16384(0%)          0,0(0%)              290,131072(0%)       173,20480(0%)        54,16330(0%)         26,32768(0%)         0,8192(0%)           Mon Jan 13 03:34:11 2020
```

### Related Commands

- ```netq show recommended-pkg-version```
- ```netq show cl-manifest```

- - -

## netq show cl-ssd-util

Displays utilization of 3ME3 solid state drives (SSDs) for a given device or all devices networkwide. These are primarily found in on-premises deployment. Tracking SSD utilization over time enables you to see any downward trend or instability of the drive before you receive an event notification. The output provides the following information for each drive:

- Percentage of PE cycles remaining for the drive
- Count of current PE cycles used by this drive
- Total number of PE cycles supported for this drive
- The drive model information
- When the last change occurred for any of these items

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq spine02 show cl-ssd-util
Hostname        Remaining PE Cycle (%)  Current PE Cycles executed      Total PE Cycles supported       SSD Model               Last Changed
spine02         80                      576                             2880                            M.2 (S42) 3ME3          Thu Oct 31 00:15:06 2019
```

### Related Commands

- ```netq show cl-btrfs-info```

- - -
## netq show dom

Displays the performance degradation or complete outage of any digital optics modules (DOMs) on a given device. Several forms of this command are available: one for laser power and current, one for temperature and voltage, and two for bit error rate (BER). 

{{%notice note%}}
Bit error rate commands can only be run on Spectrum switches running Cumulus Linux version 5.4.0 or later.
{{%/notice%}}

### Syntax

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

netq <hostname> show dom ber 
    [json]

netq <hostname> show dom ber device
    [json]
```
<!--need to check of hostname is optional or required in the BER commands-->
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| laser_rx_power | NA | Display current value and threshold events for transceiver input power (mW) on the DOMs |
| laser_output_power | NA | Display current value and threshold events for laser output power (mW) on the DOMs |
| laser_bias_current | NA | Display current value and threshold events for laser bias current (mA) on the DOMs |
| module_temp | NA | Display current value and threshold events for temperature (°C) on the DOMs |
| module_voltage | NA | Display current value and threshold events for transceiver voltage (V) on the DOMs |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| interface | \<text-dom-port-anchor\> | Only display results for the interface with this port name |
| channel_id | \<text-channel-id\> | Only display laser results for the channel with this ID |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Show module temperature of DOMs on a given device:

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
...
```

Show bit error rate across all interfaces on a given device. If the output of this command is grayed-out, that indicates that the NetQ Agent is in a rotten state.
```
cumulus@switch:~$ netq spine01 show dom ber

ifname  speed raw ber   eff. ber  symbol err. active fec fc0 hist  ethernet phy mgr. advanced status timestamp
        gb/s                                                       protocol state    opcode
                                                                   active
------- ----- --------- --------- ----------- ---------- --------- -------- -------- --------------- ---------------
swp1    400   6e-08     1.5e-254  0           Standard_R 5         400G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
                                              44_514)
swp7    200   1.5e-254  1.5e-254  0           Standard_R N/A       200G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
                                              44_514)
swp8    200   1.5e-254  1.5e-254  0           Standard_R N/A       200G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
                                              44_514)
swp9    200   1.5e-254  1.5e-254  0           Standard_R N/A       200G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
                                              44_514)
swp10   200   1.5e-254  1.5e-254  0           Standard_R N/A       200G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
                                              44_514)
swp11   200   1.5e-254  1.5e-254  0           Standard_R N/A       200G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
                                              44_514)
swp12   200   1.5e-254  1.5e-254  0           Standard_R N/A       200G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
                                              44_514)
swp13   25    1.5e-254  1.5e-254  0           No FEC     N/A       25G      Active   0               Tue Jul  9 16:1
                                                                                                     8:27 2024
swp14   100   1.5e-254  1.5e-254  0           Standard_R N/A       100G     Active   0               Tue Jul  9 16:1
                                              S-FEC - (5                                             8:27 2024
```
```
cumulus@switch:~$ netq spine01 show dom ber device
ifname  module type            cable len module sn module pn   module tmp        time last  device id                      device fw ver.  timestamp
                               .(m)                                              clear(min)
------- ---------------------- --------- --------- ----------- ----------------- ---------- ------------------------------ --------------- ---------------
swp1    Optical Module (separa 0         MT2234JT0 MMS1V00-WM  49                299.3      663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
        ted)                             0061                                               2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp7    Passive copper cable   1         MT1926VS0 MCP1650-H00 0                 298.5      663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
                                         5127      AE30                                     2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp8    Passive copper cable   2         MT1927VS0 MCP1650-V00 0                 298.5      663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
                                         1221      2E26                                     2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp9    Passive copper cable   2         MT2047VS0 MCP1650-H00 0                 298.5      663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
                                         5432      2E26                                     2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp10   Passive copper cable   2         MT2047VS0 MCP1650-H00 0                 298.5      663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
                                         4393      2E26                                     2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp11   Passive copper cable   2         MT2236VB8 MCP1650-V00 0                 298.5      663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
                                         2266      2E26                                     2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp12   Passive copper cable   2         MT1927VS0 MCP1650-V00 0                 298.5      663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
                                         1325      2E26                                     2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp13   Passive copper cable   3         MT2047VS0 MCP1650-V00 0                 1585.8     663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
                                         3757      3E26                                     2de8300b4a0264bea2541d6c68c1f9                 9:13 2024
                                                                                            bec0
swp14   Passive copper cable   3         MT2047VS0 MCP1650-V00 0                 1585.7     663e9bebb78a3a66f1d5560350351d 34.2014.960     Tue Jul  9 16:4
```
### Related Commands

None

- - -

## netq show ecmp

Displays equal-cost multi-path (ECMP) routing data.
### Syntax

```
netq [<hostname>] show ecmp
    [group-id <text-group-id>]
    [between <text-time> and <text-endtime>]
    [around <text-time>]
    [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| group-id | \<text-group-id\> | Only display results for an ECMP group with this ID |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq show ecmp
Matching ecmp_info records:
Hostname          Group Id Imbalance Agg. Traffic Paths                     Start Time                 End Time
----------------- -------- --------- ------------ ------------------------- -------------------------- --------------------------
nvidia-cl-test-l1 42       0 %       0 b/s        port: swp43s0: (index:108 Wed Feb 28 02:54:00 2024   Wed Feb 28 02:57:00 2024
                                                  , hal-port:32) - 0 b/s,
                                                  port: swp43s1: (index:109
                                                  , hal-port:34) - 0 b/s,
                                                  port: swp44s0: (index:110
                                                  , hal-port:36) - 0 b/s,
                                                  port: swp44s1: (index:111
                                                  , hal-port:38) - 0 b/s,
                                                  port: swp42s0: (index:106
                                                  , hal-port:40) - 0 b/s,
                                                  port: swp42s1: (index:107
                                                  , hal-port:42) - 0 b/s,
                                                  port: swp41s0: (index:104
                                                  , hal-port:44) - 0 b/s,
                                                  port: swp41s1: (index:105
                                                  , hal-port:46) - 0 b/s,
                                                  port: swp47s0: (index:116
                                                  , hal-port:48) - 0 b/s,
                                                  port: swp47s1: (index:117
                                                  , hal-port:50) - 0 b/s,
                                                  port: swp48s0: (index:118
                                                  , hal-port:52) - 0 b/s,
                                                  port: swp48s1: (index:119
                                                  , hal-port:54) - 0 b/s,
                                                  port: swp46s0: (index:114
                                                  , hal-port:56) - 0 b/s,
                                                  port: swp46s1: (index:115
                                                  , hal-port:58) - 0 b/s,
                                                  port: swp45s0: (index:112
                                                  , hal-port:60) - 0 b/s,
                                                  port: swp45s1: (index:113
                                                  , hal-port:62) - 0 b/s
nvidia-cl-test-l1 42       0 %       0 b/s        port: swp43s0: (index:108 Wed Feb 28 02:51:00 2024   Wed Feb 28 02:54:00 2024
                                                  , hal-port:32) - 0 b/s,
                                                  port: swp43s1: (index:109
                                                  , hal-port:34) - 0 b/s,
                                                  port: swp44s0: (index:110
                                                  , hal-port:36) - 0 b/s,
                                                  port: swp44s1: (index:111
                                                  , hal-port:38) - 0 b/s,
                                                  port: swp42s0: (index:106
                                                  , hal-port:40) - 0 b/s,
                                                  port: swp42s1: (index:107
                                                  , hal-port:42) - 0 b/s,
                                                  port: swp41s0: (index:104
                                                  , hal-port:44) - 0 b/s,
                                                  port: swp41s1: (index:105
                                                  , hal-port:46) - 0 b/s,
                                                  port: swp47s0: (index:116
                                                  , hal-port:48) - 0 b/s,
                                                  port: swp47s1: (index:117
                                                  , hal-port:50) - 0 b/s,
                                                  port: swp48s0: (index:118
                                                  , hal-port:52) - 0 b/s,
                                                  port: swp48s1: (index:119
                                                  , hal-port:54) - 0 b/s,
                                                  port: swp46s0: (index:114
                                                  , hal-port:56) - 0 b/s,
                                                  port: swp46s1: (index:115
                                                  , hal-port:58) - 0 b/s,
                                                  port: swp45s0: (index:112
                                                  , hal-port:60) - 0 b/s,
                                                  port: swp45s1: (index:113
                                                  , hal-port:62) - 0 b/s

```

### Related Commands

- `netq show ecmp-hash-config`
- - -
## netq show ecmp-hash-config

Displays equal-cost multi-path (ECMP) hashing configuration.
### Syntax

```
netq [<hostname>] show ecmp-hash-config 
    [fields]
    [around <text-time>] 
    [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| fields| NA | Display the hash field view |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq show ecmp-hash-config 
Matching ecmp_hash records:
Hostname          Seed     Max Paths Resilient Hash Enable Resilient Hash Entries Symmetric Hash enable Last Updated
----------------- -------- --------- --------------------- ---------------------- --------------------- ------------------------
nvidia-cl-r1-s1   random   129       False                 64                     True                  Sun Feb 18 15:41:43 2024
nvidia-cl-r1-s2   random   129       False                 64                     True                  Sun Feb 11 16:37:13 2024
nvidia-cl-r1-s3   random   129       False                 64                     True                  Sun Feb 11 16:38:40 2024
nvidia-cl-r1-s4   random   129       False                 64                     True                  Tue Feb 20 20:49:49 2024
nvidia-cl-r2-s1   random   129       False                 64                     True                  Sun Feb 11 16:30:38 2024
nvidia-cl-r2-s2   random   129       False                 64                     True                  Thu Feb 15 05:46:03 2024
nvidia-cl-r2-s3   random   65        False                 64                     True                  Sun Feb 18 09:59:34 2024
nvidia-cl-r2-s4   random   129       False                 64                     True                  Tue Feb 20 07:10:39 2024
nvidia-cl-r3-s1   random   129       False                 64                     True                  Mon Feb 19 12:43:04 2024
nvidia-cl-r3-s2   random   129       False                 64                     True                  Sun Feb 11 16:30:38 2024
nvidia-cl-r3-s3   random   129       False                 64                     True                  Sun Feb 11 16:52:37 2024
nvidia-cl-r3-s4   random   129       False                 64                     True                  Sun Feb 11 17:11:14 2024
nvidia-cl-r4-s1   random   129       False                 64                     True                  Sun Feb 11 16:25:58 2024
nvidia-cl-r4-s2   random   65        False                 64                     True                  Mon Feb 19 09:40:51 2024
nvidia-cl-r4-s3   random   129       False                 64                     True                  Sun Feb 11 16:38:41 2024
nvidia-cl-r4-s4   random   129       False                 64                     True                  Sun Feb 11 16:25:57 2024
nvidia-cl-ssp1    random   129       False                 64                     True                  Sun Feb 11 17:37:49 2024
nvidia-cl-ssp2    random   65        False                 64                     True                  Mon Feb 19 09:41:06 2024
nvidia-cl-ssp3    random   129       False                 64                     True                  Sun Feb 11 16:38:45 2024
nvidia-cl-ssp4    random   129       False                 64                     True                  Thu Feb 15 15:21:50 2024
nvidia-cl-ssp5    random   129       False                 64                     True                  Tue Feb 20 12:53:29 2024
nvidia-cl-ssp6    random   129       False                 64                     True                  Sun Feb 11 18:07:59 2024
nvidia-cl-ssp7    random   129       False                 64                     True                  Sun Feb 11 17:10:05 2024
nvidia-cl-ssp8    random   129       False                 64                     True                  Sun Feb 11 17:48:49 2024
nvidia-cl-su2-l1  random   129       False                 64                     True                  Sun Feb 11 17:11:15 2024
nvidia-cl-su2-l2  random   129       False                 64                     True                  Sun Feb 11 16:38:13 2024
nvidia-cl-su2-l3  random   129       False                 64                     True                  Sun Feb 11 17:42:34 2024
nvidia-cl-su2-l4  random   129       False                 64                     True                  Sun Feb 11 17:05:59 2024
nvidia-cl-su3-l1  random   65        False                 64                     True                  Mon Feb 19 09:41:23 2024
nvidia-cl-su3-l2  random   129       False                 64                     True                  Sun Feb 11 16:30:37 2024
nvidia-cl-su3-l3  random   129       False                 64                     True                  Sun Feb 11 16:30:36 2024
nvidia-cl-su3-l4  random   129       False                 64                     True                  Sun Feb 11 16:41:50 2024
nvidia-cl-su4-l1  random   129       False                 64                     True                  Fri Feb 16 09:18:33 2024
nvidia-cl-su4-l2  random   129       False                 64                     True                  Sun Feb 11 16:25:57 2024
nvidia-cl-su4-l3  random   65        False                 64                     True                  Mon Feb 19 09:41:06 2024
nvidia-cl-su4-l4  random   129       False                 64                     True                  Sun Feb 11 17:14:05 2024
nvidia-cl-test-l1 random   89        False                 64                     True                  Wed Feb 28 01:27:08 2024
nvidia-cl-test-l2 random   89        False                 64                     True                  Wed Feb 28 01:26:39 2024
nvidia-cl-test-l3 random   89        False                 64                     True                  Wed Feb 28 01:27:18 2024
nvidia-cl-test-l4 random   89        False                 64                     True                  Wed Feb 28 01:26:50 2024
nvidia-cl-test-s1 random   97        False                 64                     True                  Tue Feb 27 22:34:36 2024
nvidia-cl-test-s2 random   97        False                 64                     True                  Wed Feb 28 01:58:56 2024
```

### Related Commands

- `netq show ecmp`
- - -
## netq show ethtool-stats

Displays transmit and receive statistics for network interfaces on one or all devices, including frame errors, ACL drops, buffer drops, and more. You can filter the output by device and view the statistics for a time in the past.

### Syntax

```
netq <hostname> show ethtool-stats
    port <physical-port>
    (rx|tx)
    [extended]
    [around <text-time>]
    [json]
```

### Required Arguments

### Options

<!-- vale off -->
| Argument | Value | Description |
| ---- | ---- | ---- |
| port | \<physical-port\> | Only display results for the interface with this name |
| rx | NA | Only display receive statistics |
| tx | NA | Only display transmit statistics |
<!-- vale on -->

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| extended | NA | Display additional statistics; does not include statistics presented with standard output |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Show transmit statistics for a given switch interface and switch in the network:

```
cumulus@switch:~$ netq leaf01 show ethtool-stats port swp50 tx
Matching ethtool_stats records:
Hostname          Interface                 HwIfOutOctets        HwIfOutUcastPkts     HwIfOutMcastPkts     HwIfOutBcastPkts     HwIfOutDiscards      HwIfOutErrors        HwIfOutQDrops        HwIfOutNonQDrops     HwIfOutQLen          HwIfOutPausePkt      SoftOutErrors        SoftOutDrops         SoftOutTxFifoFull    Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp50                     8749                 0                    44                   0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    Tue Apr 28 22:09:57 2020
```

### Related Commands

- ```netq show interface-stats```
- ```netq show interface-untilization```

- - -

## netq show events

Display system events that have occurred in the last 24 hours. <!--is this 24 hours or 1 hour?--> You can filter the output by event severity and event type. The output provides the following information for each device:

- Message type
- Event severity (info, error)
- Descriptive event message
- When the event occurred

Event querying is supported for a 72-hour window within the past 30 days.
### Syntax

```
netq [<hostname>] show events
    [severity info | severity error]
    [message_type agent|bgp|btrfsinfo|cable|clsupport|configdiff|evpn|interfaces|lcm|link|lldp|mlag|mtu|node|ntp|ospf|port|ptm|ptp|resource|roceconfig|runningconfigdiff|sensor|services|ssdutil|tca_bgp|tca_dom|tca_ecmp|tca_ethtool|tca_hostd_roce|tca_link|tca_procdevstats|tca_resource|tca_roce|tca_sensors|tca_services|tca_wjh|trace|vlan|vxlan]
    [between <text-time> and <text-endtime>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| severity | info, error| Only display events with this severity level |
| message_type | agent, bgp, btrfsinfo, cable, clsupport, configdiff, evpn, interfaces, lcm, link, lldp, mlag, mtu, node, ntp, ospf, port, ptm, ptp, resource, roceconfig, runningconfigdiff, sensor, services, ssdutil, tca_bgp, tca_dom, tca_ecmp, tca_ethtool, tca_hostd_roce, tca_link, tca_procdevstats, tca_resource, tca_roce, tca_sensors, tca_services, tca_wjh, trace, vlan, vxlan | Display events for the type with this name |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display all events from the past 3 days:

```
cumulus@switch:~$ netq show events between now and 3d
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf02            evpn                     error            VNI 4002 state changed from up to d Thu Dec 10 22:00:36 2020
                                                            own
leaf02            evpn                     error            VNI 4001 state changed from up to d Thu Dec 10 22:00:36 2020
                                                            own
leaf02            evpn                     error            VNI 10 state changed from up to dow Thu Dec 10 22:00:36 2020
                                                            n
leaf02            evpn                     error            VNI 30 state changed from up to dow Thu Dec 10 22:00:36 2020
                                                            n
leaf02            evpn                     error            VNI 20 state changed from up to dow Thu Dec 10 22:00:36 2020
                                                            n
leaf02            evpn                     error            VNI 4002 state changed from up to d Thu Dec 10 20:42:39 2020
                                                            own
leaf02            evpn                     error            VNI 4001 state changed from up to d Thu Dec 10 20:42:39 2020
                                                            own
...
border02          evpn                     error            VNI 4002 state changed from up to d Thu Dec 10 03:24:10 2020
                                                            own
border02          evpn                     error            VNI 4001 state changed from up to d Thu Dec 10 03:24:10 2020
                                                            own
border02          evpn                     error            VNI 4002 state changed from up to d Thu Dec 10 02:58:20 2020
                                                            own
border02          evpn                     error            VNI 4001 state changed from up to d Thu Dec 10 02:58:20 2020
                                                            own
border02          evpn                     error            VNI 4002 state changed from up to d Thu Dec 10 02:32:16 2020
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

Display events that have occurred on the leaf01 switch between now and an hour ago.

```
cumulus@switch:~$ netq leaf01 show events

Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:34:31 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
```
### Related Commands

None

- - -

## netq show events-config

Displays all event suppression configurations. Optionally, you can filter by a specific configuration or message type. The output displays the following information for each configuration:

- Configuration identifier and name
- Message type
- Scope of the suppression
- When the suppression no longer applies

When you filter by a message type, you must include the `show-filter-conditions` keyword to display the conditions associated with that message type and the processing hierarchy. The output in this case provides the following information for each message type:

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
| message_type | \<text-message-type-anchor\> | Only display results for configurations with this type. Values include <!-- vale off -->*agent*, *ar*, *bgp*, *btrfsinfo*, *clsupport*, *configdiff*, *evpn*, *lcm*, *link*, *lldp*, *mlag*, *mtu*, *ntp*, *ospf*, *packageinfo*, *ptm*, *ptp*, *roceconfig*, *runningconfigdiff*, *sensor*, *services*, and *ssdutil*<!-- vale on --> |
| json | NA | Display the output in JSON format |
### Sample Usage

Display a given event-suppression configuration:

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
...
```

Display filter conditions for EVPN event suppression configurations:

```
cumulus@switch:~$ netq show events-config message_type evpn show-filter-conditions

Matching config_events records:
Message Name             Filter Condition Name                      Filter Condition Hierarchy                           Filter Condition Description
------------------------ ------------------------------------------ ---------------------------------------------------- --------------------------------------------------------
evpn                     vni                                        3                                                    Target VNI
evpn                     severity                                   2                                                    Severity error/info
evpn                     hostname                                   1                                                    Target Hostname
```
### Related Commands

- ```netq show events```

- - -
## netq show evpn
<!-- vale on -->
Displays the health of all EVPN sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides the following for each session:

- The VNI used
- The address of the VNI endpoint
- Whether the session is part of a layer 2 or layer 3 configuration
- The associated VRF or VLAN when defined
- Whether the associated VNI is in the kernel
- The export and import route targets used for filtering
- When the last change occurred for any of these items

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

The example below shows the configuration and status for all devices, including the associated VNI, VTEP address, the import and export route (showing the BGP ASN and VNI path), and the last time a change occurred for each device running EVPN.

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

This example displays the EVPN configuration and status for VNI *4001*.

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
### Related Commands
<!-- vale off -->
- `netq show events message_type evpn`
- `netq show unit-tests evpn`
- `netq check evpn`
<!-- vale on -->
- - -
## netq show histogram

Displays a device's egress queue lengths as a histogram, grouped into bins. For more information, refer to {{<link title="Switches/#view-queue-lengths-in-histograms" text="Monitoring Switches">}}.

### Syntax

```
netq <hostname> show histogram interface <text-ifname> queue 
    [around <text-time>] 
    [between <text-time> and <text-endtime>] 
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch with this name |
| interface | \<text-ifname\> | Only display results for the interface with this name |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| json | NA | Display the output in JSON format |


### Sample Usage

Display data on *leaf01* for the interface *swp1*:

```
cumulus@switch:~$ netq leaf01 show histogram interface swp1 queue

Matching queue_histograms records:
Time                           Bin0     Bin1     Bin2     Bin3     Bin4     Bin5     Bin6     Bin7     Bin8     Bin9
------------------------------ -------- -------- -------- -------- -------- -------- -------- -------- -------- --------
Mon Jul  8 19:41:23 2024       992115   3434     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:22 2024       999438   3492     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:21 2024       999782   3337     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:20 2024       998757   3479     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:19 2024       997223   3391     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:18 2024       987939   3346     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:17 2024       999167   3412     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:16 2024       1000553  3401     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:15 2024       1000598  3420     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:14 2024       999258   3420     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:13 2024       1002366  3452     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:12 2024       998212   3467     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:11 2024       1002767  3361     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:10 2024       1002361  3385     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:09 2024       989952   3451     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:08 2024       998360   3474     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:07 2024       1002658  3536     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:06 2024       999199   3450     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:05 2024       999429   3420     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:04 2024       997595   3430     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:03 2024       999888   3454     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:02 2024       1000880  3523     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:01 2024       999824   3502     0        0        0        0        0        0        0        0
Mon Jul  8 19:41:00 2024       1001447  3413     0        0        0        0        0        0        0        0
Mon Jul  8 19:40:59 2024       995547   3366     0        0        0        0        0        0        0        0
Mon Jul  8 19:40:58 2024       986930   3393     0        0        0        0        0        0        0        0
Mon Jul  8 19:40:57 2024       998351   3417     0        0        0        0        0        0        0        0
Mon Jul  8 19:40:56 2024       999049   3442     0        0        0        0        0        0        0        0
Mon Jul  8 19:40:55 2024       988615   3439     0        0        0        0        0        0        0        0
Mon Jul  8 19:40:54 2024       992414   3298     0        0        0        0        0        0        0        0
Mon Jul  8 19:40:53 2024       997661   3407     0        0        0        0        0        0        0        0
```
### Related Commands

None
- - -
## netq show interfaces

Displays the health of all interfaces or a single interface on all nodes or a specific node in your network fabric currently or for a time in the past. You can filter by the interface type, state of the interface, or the remote interface. For a given switch or host, you can view the total number of configured interfaces.

The output provides the following for each device:

- The name of the interface
- The type of interface
- The state of the interface (up or down)
- The associated VRF, VLANs, PVID, MTU, and LLDP peer
- When the last change occurred for any of these items
- The total number of interfaces on a given device
- The module, vendor, part number, and performance info. for physical interfaces

### Syntax

Six forms of the command are available, based on whether you want to view interface health for all devices or a given device, and whether you want to filter by an interface type.

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

netq [<hostname>] show interfaces alias 
    [<remote-interface>] 
    [around <text-time>] 
    [json]

netq [<hostname>] show interfaces physical 
   [<physical-port>] 
   [empty|plugged] 
   [peer] 
   [vendor <module-vendor> | model <module-model>| module] 
   [around <text-time>]
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
| NA | \<hostname\> | Only display results for the switch or host with this name. |
| alias | NA | Only display results for the specified interface alias |
| physical | NA | Only display results for physical interfaces |
| type | <!-- vale off -->bond, bridge, eth, loopback, macvlan, swp, vlan, vrf, or vxlan<!-- vale on --> | Only display results for the specified interface type |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<remote-interface\> | Only display results for local interfaces with this remote interface |
| state | \<remote-interface-state\> | Only display results for remote interfaces in the specified state&mdash;up or down |
| NA | \<physical-port\> | Only display results for the interface with this name |
| NA | empty, plugged | Display switch ports with attached cables (plugged) or those without connectivity (empty) |
| NA | peer | Display connected peer ports |
| vendor | \<module-vendor\> |  Only display results from a particular vendor (for example, Mellanox) |
| model | \<module-model\> | Only display results from a particular model |
| module | NA | Display interface module information |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| count | NA | Display the total number of interface on the specified switch or host. You must specify the `hostname` option. |
| json | NA | Display the output in JSON format |
### Sample Usage

Display interfaces on a given device:

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
Display only VLAN results. The output displays the interface, its specified MTU, whether it is running over a VRF, and the last time it changed.

```
cumulus@switch:~$ netq show interfaces type vlan
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
border01          vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:48 2020
border01          vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:48 2020
border01          peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:48 2020
border02          vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:51 2020
border02          vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
border02          peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:51 2020
fw1               borderBond.20             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:25 2020
fw1               borderBond.10             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:25 2020
leaf01            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf02            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf03            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf04            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:29:06 2020
```

Display all MAC addresses associated with your vRR (virtual route reflector) interface configuration. This is useful for determining if the specified MAC address inside a VLAN is the same or different across your vRR configuration.

```
cumulus@switch:~$ netq show interfaces type macvlan
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    00:00:00:00:00:1a  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
yes    44:38:39:00:00:37  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
cumulus@netq-ts:~$ netq show interfaces type macvlan

Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
leaf01            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:28:42 2020
                                                                                        Mode: Private
leaf01            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:28:42 2020
                                                                                        Mode: Private
leaf01            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:28:42 2020
                                                                                        Mode: Private
leaf02            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:28:51 2020
                                                                                        Mode: Private
leaf02            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:28:51 2020
                                                                                        Mode: Private
leaf02            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:28:51 2020
                                                                                        Mode: Private
leaf03            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:28:23 2020
                                                                                        Mode: Private
leaf03            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:28:23 2020
                                                                                        Mode: Private
leaf03            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:28:23 2020
                                                                                        Mode: Private
leaf04            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:29:06 2020
                                                                                        Mode: Private
leaf04            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:29:06 2020
                                                                                        Mode: Private
leaf04            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:29:06 2020
```

Display cable information and status for all interface ports on all devices:

```
cumulus@switch:~$ netq show interfaces physical
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
border01          vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp54                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp49                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp2                      down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp3                      up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp52                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp1                      down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp53                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp4                      down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp50                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          eth0                      up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp51                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border02          swp49                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp54                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp52                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp53                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp4                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp3                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp1                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp2                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp51                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp50                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          eth0                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
fw1               swp49                     down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               eth0                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               swp1                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               swp2                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw2               vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               eth0                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               swp49                     down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               swp2                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               swp1                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
...
```

The following example displays detailed module information for the interface ports on the leaf02 switch:

```
cumulus@switch:~$ netq leaf02 show interfaces physical module
Matching cables records are:
Hostname          Interface                 Module    Vendor               Part No          Serial No                 Transceiver      Connector        Length Last Changed
----------------- ------------------------- --------- -------------------- ---------------- ------------------------- ---------------- ---------------- ------ -------------------------
leaf02            swp1                      RJ45      n/a                  n/a              n/a                       n/a              n/a              n/a    Thu Feb  7 22:49:37 2019
leaf02            swp2                      SFP       Mellanox             MC2609130-003    MT1507VS05177             1000Base-CX,Copp Copper pigtail   3m     Thu Feb  7 22:49:37 2019
                                                                                                                        er Passive,Twin
                                                                                                                        Axial Pair (TW)
leaf02            swp47                     QSFP+     CISCO                AFBR-7IER05Z-CS1 AVE1823402U               n/a              n/a              5m     Thu Feb  7 22:49:37 2019
leaf02            swp48                     QSFP28    TE Connectivity      2231368-1        15250052                  100G Base-CR4 or n/a              3m     Thu Feb  7 22:49:37 2019
                                                                                                                        25G Base-CR CA-L
                                                                                                                        ,40G Base-CR4               
leaf02            swp49                     SFP       OEM                  SFP-10GB-LR      ACSLR130408               10G Base-LR      LC               10km,  Thu Feb  7 22:49:37 2019
                                                                                                                                                        10000m
leaf02            swp50                     SFP       JDSU                 PLRXPLSCS4322N   CG03UF45M                 10G Base-SR,Mult LC               80m,   Thu Feb  7 22:49:37 2019
                                                                                                                        imode,                            30m,  
                                                                                                                        50um (M5),Multim                  300m  
                                                                                                                        ode,            
                                                                                                                        62.5um (M6),Shor
                                                                                                                        twave laser w/o
                                                                                                                        OFC (SN),interme
                                                                                                                        diate distance (
                                                                                                                        I)              
leaf02            swp51                     SFP       Mellanox             MC2609130-003    MT1507VS05177             1000Base-CX,Copp Copper pigtail   3m     Thu Feb  7 22:49:37 2019
                                                                                                                        er Passive,Twin
                                                                                                                        Axial Pair (TW)
leaf02            swp52                     SFP       FINISAR CORP.        FCLF8522P2BTL    PTN1VH2                   1000Base-T       RJ45             100m   Thu Feb  7 22:49:37 2019
```

The following example first determines which models (part numbers) exist on all the devices and then displays devices with a part number of QSFP-H40G-CU1M installed:

```
cumulus@switch:~$ netq show interfaces physical model
    2231368-1         :  2231368-1
    624400001         :  624400001
    QSFP-H40G-CU1M    :  QSFP-H40G-CU1M
    QSFP-H40G-CU1MUS  :  QSFP-H40G-CU1MUS
    n/a               :  n/a

cumulus@switch:~$ netq show interfaces physical model QSFP-H40G-CU1M
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
leaf01            swp50                     up         1G         off     QSFP+     OEM                  QSFP-H40G-CU1M   Thu Feb  7 18:31:20 2019
leaf02            swp52                     up         1G         off     QSFP+     OEM                  QSFP-H40G-CU1M   Thu Feb  7 18:31:20 2019
```

### Related Commands

- `netq show events`
- `netq check interfaces`
- `netq show unit-tests interfaces`

- - -

<!-- vale off -->
## netq show interface-stats
<!-- vale on -->

Displays performance statistics for the physical interfaces on switches in your network. The NetQ Agent collects the statistics every 30 seconds. Statistics are not collected for non-physical interfaces, such as bonds, bridges, and VXLANs. You can filter the output by interface or to display only errors. The output provides the following information for each switch and interface:

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display statistics for a given interface:

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

- ```netq show interface-utilization```
- ```netq show ethtool-stats```

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |
<!-- vale on -->

### Sample Usage

Display utilization for a given device:

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

Display utilization for all devices, transmit only:

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

- ```netq show interface-stats```
- ```netq show ethtool-stats```

- - -

## netq show inventory

Displays information about the hardware and software components deployed on a given device or all devices networkwide. The output provides details specific to the component selected.

### Syntax

Several forms of this command are available based on the inventory component you'd like to view:

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
| brief | NA | Only display summary information: hostname, switch, OS, CPU architecture, ASIC vendor, ports, NICs |
| asic | NA | Only display ASIC information: hostname, vendor, model, model ID, core bandwidth, ports |
| board | NA | Only display motherboard information: hostname, vendor, model, base MAC address, serial number, part number, revision, manufacturing date |
| cpu | NA | Only display processor information: hostname, architecture, model, frequency, number of cores |
| disk | NA | Only display disk information: hostname, disk name and type, transport, size, vendor, model |
| memory | NA | Only display memory information: hostname, memory name, type, size, speed, vendor, serial number |
| os | NA | Only display operating system information: hostname, OS name, version, when changed |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| vendor | \<asic-vendor\>, \<board-vendor\>, \<disk-vendor\>, \<memory-vendor\> | Only display results for the ASIC, board, disk, or memory vendor with this name |
| model | \<asic-model\>, \<board-model\> | Only display results for ASIC or board model with this name |
| model-id | \<asic-model-id\> | Only display results for ASIC models with this ID |
| arch | \<cpu-arch\> | Only display results for CPUs with this architecture |
| transport | \<disk-transport\> | Only display results for disks with this transport method |
| type | \<memory-type\> | Only display results for memory of this type |
| version | \<os-version\> | Only display results for operating systems of this version |
| name | \<os-name\> | Only display results for operating systems with this name |
| opta | NA | Only display results for the NetQ appliance or VM (not other switches or hosts) |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display an inventory summary:

```
cumulus@switch:~$ netq show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports                               NIC
----------------- -------------------- --------------- -------- --------------- ----------------------------------- -----------------------------------
neo-switch01      SN3700C              CL              x86_64   Spectrum-2      32 x 100G-QSFP28                    N/A
neo-switch02      SN3700C              CL              x86_64   Spectrum-2      32 x 100G-QSFP28                    N/A
r-3420-01         SN3420               CL              x86_64   Spectrum-2      48 x 25G-SFP28 & 12 x 100G-QSFP28   N/A
r-3700-01         SN3700V              CL              x86_64   Spectrum-2      32 x 200G-QSFP56                    N/A
r-3700-02         SN3700C              CL              x86_64   Spectrum-2      32 x 100G-QSFP28                    N/A
r-3700-03         SN3700C              CL              x86_64   Spectrum-2      32 x 100G-QSFP28                    N/A
ufm-switch19      MSN2700              CL              x86_64   Spectrum        32 x 100G-QSFP28                    N/A
ufm-switch29      SN3700C              CL              x86_64   Spectrum-2      32 x 100G-QSFP28                    N/A
```

Display ASIC information for all devices with a vendor of *NVIDIA*:

```
cumulus@switch:~$ netq show inventory asic vendor NVIDIA
Matching inventory records:
Hostname          Vendor               Model                          Model ID                  Core BW        Ports
----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
mlx-2100-05       NVIDIA               Spectrum                       MT52132                   N/A            16 x 100G-QSFP28
mlx-2410a1-05     NVIDIA               Spectrum                       MT52132                   N/A            48 x 25G-SFP28 & 8 x 100G-QSFP28
mlx-2700-11       NVIDIA               Spectrum                       MT52132                   N/A            32 x 100G-QSFP28
```

Display only the devices with a *Celestica* motherboard:

```
cumulus@switch:~$ netq show inventory board vendor celestica
Matching inventory records:
Hostname          Vendor               Model                          Base MAC           Serial No                 Part No          Rev    Mfg Date
----------------- -------------------- ------------------------------ ------------------ ------------------------- ---------------- ------ ----------
st1-l1            CELESTICA            Arctica 4806xp                 00:E0:EC:27:71:37  D2060B2F044919GD000011    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                    ne-XP
st1-l2            CELESTICA            Arctica 4806xp                 00:E0:EC:27:6B:3A  D2060B2F044919GD000060    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                    ne-XP
```

Display all the currently deployed architectures in the network, and then display devices with an *x86\_64* architecture:

```
cumulus@switch:~$ netq show inventory cpu arch
    x86_64  :  CPU Architecture
    
cumulus@switch:~$ netq show inventory cpu arch x86_64
Matching inventory records:
Hostname          Arch     Model                          Freq       Cores
----------------- -------- ------------------------------ ---------- -----
leaf01            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
leaf02            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
leaf03            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
leaf04            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
oob-mgmt-server   x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
server01          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
server02          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
server03          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
server04          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
spine01           x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
spine02           x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
```
### Related Commands

- `netq config agent cpu-limit`
- `netq show cl-manifest`
- `netq show cl-pkg-info` 
- `netq show dom type`
- `netq show resource-util`
- `netq show sensors`

- - -

## netq show ip/ipv6 addresses

Displays the IPv4 or IPv6 addresses configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address or prefix, and VRF. You can obtain a count of addresses for a given device. The output provides the following information for each address:

- Hostname of the device with the address
- Interface on the device with the address
- VRF, when configured, on the interface with the address
- When the last change occurred for any of these items

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
| vrf | \<vrf\> | Only display results for switches and hosts using this virtual route forwarding interface |
| subnet | NA | Only display results for addresses in the subnet |
| supernet | NA | Only display results for addresses in the supernet |
| gateway | NA | Only display results for addresses in the gateway |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

The following example shows all IPv4 addresses in the reference topology:

```
cumulus@switch:~$ netq show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.10.10.104/32           spine04           lo                        default         Mon Oct 19 22:28:23 2020
192.168.200.24/24         spine04           eth0                                      Tue Oct 20 15:46:20 2020
10.10.10.103/32           spine03           lo                        default         Mon Oct 19 22:29:01 2020
192.168.200.23/24         spine03           eth0                                      Tue Oct 20 15:19:24 2020
192.168.200.22/24         spine02           eth0                                      Tue Oct 20 15:40:03 2020
10.10.10.102/32           spine02           lo                        default         Mon Oct 19 22:28:45 2020
192.168.200.21/24         spine01           eth0                                      Tue Oct 20 15:59:36 2020
10.10.10.101/32           spine01           lo                        default         Mon Oct 19 22:28:48 2020
192.168.200.38/24         server08          eth0                      default         Mon Oct 19 22:28:50 2020
192.168.200.37/24         server07          eth0                      default         Mon Oct 19 22:28:43 2020
192.168.200.36/24         server06          eth0                      default         Mon Oct 19 22:40:52 2020
10.1.20.105/24            server05          uplink                    default         Mon Oct 19 22:41:08 2020
10.1.10.104/24            server04          uplink                    default         Mon Oct 19 22:40:45 2020
192.168.200.33/24         server03          eth0                      default         Mon Oct 19 22:41:04 2020
192.168.200.32/24         server02          eth0                      default         Mon Oct 19 22:41:00 2020
10.1.10.101/24            server01          uplink                    default         Mon Oct 19 22:40:36 2020
10.255.1.228/24           oob-mgmt-server   vagrant                   default         Mon Oct 19 22:28:20 2020
192.168.200.1/24          oob-mgmt-server   eth1                      default         Mon Oct 19 22:28:20 2020
10.1.20.3/24              leaf04            vlan20                    RED             Mon Oct 19 22:28:47 2020
10.1.10.1/24              leaf04            vlan10-v0                 RED             Mon Oct 19 22:28:47 2020
192.168.200.14/24         leaf04            eth0                                      Tue Oct 20 15:56:40 2020
10.10.10.4/32             leaf04            lo                        default         Mon Oct 19 22:28:47 2020
10.1.20.1/24              leaf04            vlan20-v0                 RED             Mon Oct 19 22:28:47 2020
...
```

Display all IP addresses on the *spine01* switch:

```
cumulus@switch:~$ netq spine01 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
192.168.200.21/24         spine01           eth0                      mgmt            Thu Sep 17 20:07:49 2020
10.10.10.101/32           spine01           lo                        default         Thu Sep 17 20:25:05 2020
```

Display all IP addresses using the *BLUE* VRF on the *leaf03* switch:

```
cumulus@switch:~$ netq leaf03 show ip addresses vrf BLUE
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.1.30.1/24              leaf03            vlan30-v0                 BLUE            Thu Sep 17 20:25:09 2020
10.1.30.2/24              leaf03            vlan30                    BLUE            Thu Sep 17 20:25:08 2020
```

The following example shows all IPv6 addresses in the reference topology:

```
cumulus@switch:~$ netq show ipv6 addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
fe80::4638:39ff:fe00:16c/ spine04           eth0                                      Mon Oct 19 22:28:23 2020
64
fe80::4638:39ff:fe00:27/6 spine04           swp5                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:2f/6 spine04           swp6                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:17/6 spine04           swp3                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:1f/6 spine04           swp4                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:7/64 spine04           swp1                      default         Mon Oct 19 22:28:23 2020
fe80::4638:39ff:fe00:f/64 spine04           swp2                      default         Mon Oct 19 22:28:23 2020
fe80::4638:39ff:fe00:2d/6 spine03           swp6                      default         Mon Oct 19 22:29:01 2020
4
fe80::4638:39ff:fe00:25/6 spine03           swp5                      default         Mon Oct 19 22:29:01 2020
4
fe80::4638:39ff:fe00:170/ spine03           eth0                                      Mon Oct 19 22:29:01 2020
64
fe80::4638:39ff:fe00:15/6 spine03           swp3                      default         Mon Oct 19 22:29:01 2020
4
...
```
The following example shows the IPv6 address information for the leaf01 switch:

```
cumulus@switch:~$ netq leaf01 show ipv6 addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
fe80::4638:39ff:febe:efaa leaf01            vlan4002                  BLUE            Mon Oct 19 22:28:22 2020
/64
fe80::4638:39ff:fe00:8/64 leaf01            swp54                     default         Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:59/6 leaf01            vlan10                    RED             Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:59/6 leaf01            vlan20                    RED             Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:59/6 leaf01            vlan30                    BLUE            Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:2/64 leaf01            swp51                     default         Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:4/64 leaf01            swp52                     default         Mon Oct 19 22:28:22 2020
fe80::4638:39ff:febe:efaa leaf01            vlan4001                  RED             Mon Oct 19 22:28:22 2020
/64
fe80::4638:39ff:fe00:6/64 leaf01            swp53                     default         Mon Oct 19 22:28:22 2020
fe80::200:ff:fe00:1c/64   leaf01            vlan30-v0                 BLUE            Mon Oct 19 22:28:22 2020
fe80::200:ff:fe00:1b/64   leaf01            vlan20-v0                 RED             Mon Oct 19 22:28:22 2020
fe80::200:ff:fe00:1a/64   leaf01            vlan10-v0                 RED             Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:59/6 leaf01            peerlink.4094             default         Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:59/6 leaf01            bridge                    default         Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:17a/ leaf01            eth0                                      Mon Oct 19 22:28:22 2020
64
```
The following example shows the number of IPv4 and IPv6 addresses on the leaf01 switch:

```
cumulus@switch:~$ netq leaf01 show ip addresses count
Count of matching address records: 9

cumulus@switch:~$ netq leaf01 show ipv6 addresses count
Count of matching address records: 17
```

### Related Commands

- `netq show ip/ipv6 neighbors`
- `netq show ip routes`

- - -

## netq show ip/ipv6 neighbors

Displays the IPv4 or IPv6 neighbors configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address, address and VRF, or VRF. You can obtain a count of neighbors for a given device, or for a given device and MAC address. The output provides the following information for each address:

- Hostname of neighbor
- Interface of neighbor
- MAC address of neighbor
- VRF, when configured, of neighbor
- Whether this address owned by the neighbor or learned from by host
- When the last change occurred for any of these items

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display all IPv4 neighbors on the *spine01* switch:

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
The following example shows all IPv4 neighbors using the RED VRF. Note that the VRF name is case-sensitive.

```
cumulus@switch:~$ netq show ip neighbors vrf RED
Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
10.1.10.2                 leaf04            vlan10                    44:38:39:00:00:5d  RED             no     Mon Oct 19 22:28:47 2020
10.1.20.2                 leaf04            vlan20                    44:38:39:00:00:5d  RED             no     Mon Oct 19 22:28:47 2020
10.1.10.3                 leaf03            vlan10                    44:38:39:00:00:5e  RED             no     Mon Oct 19 22:28:18 2020
10.1.20.3                 leaf03            vlan20                    44:38:39:00:00:5e  RED             no     Mon Oct 19 22:28:18 2020
10.1.10.2                 leaf02            vlan10                    44:38:39:00:00:59  RED             no     Mon Oct 19 22:28:30 2020
10.1.20.2                 leaf02            vlan20                    44:38:39:00:00:59  RED             no     Mon Oct 19 22:28:30 2020
10.1.10.3                 leaf01            vlan10                    44:38:39:00:00:37  RED             no     Mon Oct 19 22:28:22 2020
10.1.20.3                 leaf01            vlan20                    44:38:39:00:00:37  RED             no     Mon Oct 19 22:28:22 2020
```

Display all IPv6 addresses on the leaf03 switch:

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

- `netq show ip/ipv6 addresses`
- `netq show ip routes`

- - -

## netq show ip routes

Displays the IPv4 or IPv6 routes configured for a given device or all devices networkwide, currently or for a time in the past. You can filter the output by remote-interface, address, address and prefix, VRF, and route origin. You can obtain a count of routes for a given device. The output provides the following information for each route:

- Whether this route originated with this device or not
- VRF used for the route
- Address prefix used for the route
- Hostname of the device with the route
- Next hops the route takes
- When the last change occurred for any of these items

### Syntax

Two sets of IP routes commands are available, one for IPv4 and one for IPv6.

```
netq <hostname> show ip routes
    [<ipv4>|<ipv4/prefixlen>]
    [vrf <vrf>]
    [origin]
    [edge]
    [around <text-time>]
    [count]
    [json]

netq show ip routes
    [<ipv4>|<ipv4/prefixlen>]
    [vrf <vrf>]
    [origin]
    [edge]
    [around <text-time>]
    [json]

netq <hostname> show ipv6 routes
    [<ipv6>|<ipv6/prefixlen>]
    [vrf <vrf>]
    [origin]
    [edge]
    [around <text-time>]
    [count]
    [json]

netq show ipv6 routes
    [<ipv6>|<ipv6/prefixlen>]
    [vrf <vrf>]
    [origin]
    [edge]
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
| edge | NA | Display the edge switch that a route is learn from on hosts and network devices that do not run Cumulus Linux |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| count | NA | Display the count of routes for a given switch or host |
| json | NA | Display the output in JSON |

### Sample Usage

Display all IPv4 routes:

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
The following example shows the routes available for an IP address of 10.0.0.12. The result shows nine available routes:

```
cumulus@switch:~$ netq show ip routes 10.0.0.12
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no                     0.0.0.0/0                      spine04           Blackhole                           Mon Oct 19 22:28:23 2020
no                     0.0.0.0/0                      spine03           Blackhole                           Mon Oct 19 22:29:01 2020
no                     0.0.0.0/0                      spine02           Blackhole                           Mon Oct 19 22:28:46 2020
no                     0.0.0.0/0                      spine01           Blackhole                           Mon Oct 19 22:28:48 2020
no     default         0.0.0.0/0                      server08          192.168.200.1: eth0                 Mon Oct 19 22:28:50 2020
no     default         0.0.0.0/0                      server07          192.168.200.1: eth0                 Mon Oct 19 22:28:43 2020
no     default         10.0.0.0/8                     server06          10.1.30.1: uplink                   Mon Oct 19 22:40:52 2020
no     default         10.0.0.0/8                     server05          10.1.20.1: uplink                   Mon Oct 19 22:41:08 2020
no     default         10.0.0.0/8                     server04          10.1.10.1: uplink                   Mon Oct 19 22:40:45 2020
no     default         10.0.0.0/8                     server03          10.1.30.1: uplink                   Mon Oct 19 22:41:04 2020
no     default         10.0.0.0/8                     server02          10.1.20.1: uplink                   Mon Oct 19 22:41:00 2020
no     default         10.0.0.0/8                     server01          10.1.10.1: uplink                   Mon Oct 19 22:40:36 2020
no     default         0.0.0.0/0                      oob-mgmt-server   10.255.1.1: vagrant                 Mon Oct 19 22:28:20 2020
no     BLUE            0.0.0.0/0                      leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no                     0.0.0.0/0                      leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no     RED             0.0.0.0/0                      leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no     BLUE            0.0.0.0/0                      leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no                     0.0.0.0/0                      leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no     RED             0.0.0.0/0                      leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no     BLUE            0.0.0.0/0                      leaf02            Blackhole                           Mon Oct 19 22:28:30 2020
no                     0.0.0.0/0                      leaf02            Blackhole                           Mon Oct 19 22:28:30 2020
...
```

Display all IPv6 routes on the leaf03 switch:

```
cumulus@switch:~$ netq leaf03 show ipv6 routes
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no     RED             ::/0                           leaf03            Blackhole                           Thu Dec  3 22:28:58 2020
no                     ::/0                           leaf03            Blackhole                           Thu Dec  3 22:28:58 2020
no     BLUE            ::/0                           leaf03            Blackhole                           Thu Dec  3 22:28:58 2020
```
The following example shows all IPv4 routes owned by spine01 switch:

```
cumulus@switch:~$ netq spine01 show ip routes origin
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
yes                    192.168.200.0/24               spine01           eth0                                Mon Oct 19 22:28:48 2020
yes                    192.168.200.21/32              spine01           eth0                                Mon Oct 19 22:28:48 2020
yes    default         10.10.10.101/32                spine01           lo                                  Mon Oct 19 22:28:48 2020
```
This example shows the total number of IPv4 and IPv6 routes for all devices on the leaf01 switch.

```
cumulus@switch:~$ netq leaf01 show ip routes count
Count of matching routes records: 27
    
cumulus@switch:~$ netq leaf01 show ipv6 routes count
Count of matching routes records: 3
```
### Related Commands

- `netq show ip/ipv6 addresses`
- `netq show ip/ipv6 neighbors`

- - -
<!--
## netq show line-utilization

### Syntax

```
netq [<hostname>] show line-utilization 
   [port <text-port>] 
   [between <text-time> and <text-endtime>] 
   [around <text-time>] 
   [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| port | \<text-port\> | Only display results for the port with this name |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format |

### Sample Usage

### Related Commands
- - -
-->
## netq show lldp

Displays the health of all LLDP sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. You can filter the output to show sessions for a particular peer interface port. The output provides the following for each session:

- The interface on the local device
- The hostname and interface of the peer device
- When the last change occurred for any of these items

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format |

### Sample Usage

This example shows the Cumulus reference topology, where LLDP runs on all border, firewall, leaf and spine switches, servers, including the out-of-band management server.

```
cumulus@switch:~$ netq show lldp

Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
border01          swp3                      fw1               swp1                      Mon Oct 26 04:13:29 2020
border01          swp49                     border02          swp49                     Mon Oct 26 04:13:29 2020
border01          swp51                     spine01           swp5                      Mon Oct 26 04:13:29 2020
border01          swp52                     spine02           swp5                      Mon Oct 26 04:13:29 2020
border01          eth0                      oob-mgmt-switch   swp20                     Mon Oct 26 04:13:29 2020
border01          swp53                     spine03           swp5                      Mon Oct 26 04:13:29 2020
border01          swp50                     border02          swp50                     Mon Oct 26 04:13:29 2020
border01          swp54                     spine04           swp5                      Mon Oct 26 04:13:29 2020
border02          swp49                     border01          swp49                     Mon Oct 26 04:13:11 2020
border02          swp3                      fw1               swp2                      Mon Oct 26 04:13:11 2020
border02          swp51                     spine01           swp6                      Mon Oct 26 04:13:11 2020
border02          swp54                     spine04           swp6                      Mon Oct 26 04:13:11 2020
border02          swp52                     spine02           swp6                      Mon Oct 26 04:13:11 2020
border02          eth0                      oob-mgmt-switch   swp21                     Mon Oct 26 04:13:11 2020
border02          swp53                     spine03           swp6                      Mon Oct 26 04:13:11 2020
border02          swp50                     border01          swp50                     Mon Oct 26 04:13:11 2020
fw1               eth0                      oob-mgmt-switch   swp18                     Mon Oct 26 04:38:03 2020
fw1               swp1                      border01          swp3                      Mon Oct 26 04:38:03 2020
fw1               swp2                      border02          swp3                      Mon Oct 26 04:38:03 2020
fw2               eth0                      oob-mgmt-switch   swp19                     Mon Oct 26 04:46:54 2020
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Mon Oct 26 04:13:57 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Mon Oct 26 04:13:57 2020
leaf01            swp52                     spine02           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp49                     leaf02            swp49                     Mon Oct 26 04:13:57 2020
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Oct 26 04:13:57 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Mon Oct 26 04:13:57 2020
leaf01            swp53                     spine03           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp50                     leaf02            swp50                     Mon Oct 26 04:13:57 2020
leaf01            swp54                     spine04           swp1                      Mon Oct 26 04:13:57 2020
leaf01            swp51                     spine01           swp1                      Mon Oct 26 04:13:57 2020
...
```

Display session for a given host interface port:

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

- `netq show events`
- `netq check lldp`

- - -

## netq show mac-commentary

Displays descriptive information about changes to a given MAC address on a specific VLAN, including commentary for the following MAC address-related events:

<!-- vale off -->
- When a MAC address is configured or unconfigured
- When a bond enslaved or removed as a slave
- When bridge membership changes
- When a MAC address is learned or installed by control plane on tunnel interface
- When a MAC address is flushed or expires
- When a MAC address moves
<!-- vale on -->

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
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| json | NA | Display the output in JSON format |

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

- ```netq show mac-history```
- ```netq show ip/ipv6 addresses```

- - -

## netq show mac-history

<!-- vale off -->
Displays when a MAC address is learned, when and where it moved in the network after that, if there was a duplicate at any time, and so forth. By default, the command displays various history threads in the output grouped by VLAN and timestamp (chronologically). The default time range is between now and one hour ago.

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
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| listby | \<text-list-by\> | Display output in groups based on the specified output field |
| json | NA | Display the output in JSON format |

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


### Related Commands

- ```netq show mac-commentary```
- ```netq show ip/ipv6 addresses```

- - -

## netq show macs

Displays MAC addresses for monitored switches networkwide, currently or for a time in the past. For a given switch, you can view the total number of MAC addresses associated with that switch. You can filter the output based on VLAN, egress port, and origination status.

The output displays the following information for each MAC address:

- Whether the switch owned this address or the peer learned it
- VLAN associated with this address for a given switch
- Switch that uses this address
- Egress port on the switch
- When the last change occurred for any of these items

This command does not show MAC addresses for hosts.

### Syntax

Three forms of this command are available: the basic command which shows all MAC addresses networkwide, one to view MAC addresses or a count of addresses for a given switch, and one to view MAC addresses on a given switch and egress port.

```
netq show macs
    [<mac>]
    [vlan <1-4096>]
    [origin <text-origin>]
    [around <text-time>]
    [json]

netq <hostname> show macs
    [<mac>]
    [vlan <1-4096>]
    [origin <text-origin> | count]
    [around <text-time>]
    [json]

netq <hostname> show macs
    egress-port <egress-port>
    [<mac>]
    [vlan <1-4096>]
    [origin <text-origin>]
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
| origin | \<text-origin\> | Display the MAC addresses that originated with the device (true) or not (false) |
| count | NA | Display the total number of MAC addresses used by the specified switch; can only use this option when you define the `hostname` option |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format |

### Sample Usage

Display count of MAC addresses on a switch:

```
cumulus@switch:~$ netq leaf01 show macs count
Count of matching mac records: 50
```

Display MAC addresses that use a given egress port on a switch:

```
cumulus@switch:~$ netq leaf01 show macs egress-port bond3
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
no     44:38:39:00:00:36  30     leaf01            bond3                          no     Mon Dec  7 22:29:47 2020
no     46:38:39:00:00:36  30     leaf01            bond3                          no     Mon Dec  7 22:29:47 2020
no     46:38:39:00:00:3c  30     leaf01            bond3                          no     Mon Dec  7 22:29:47 2020
```

Display MAC addresses associated with VLAN 10. The command also provides the hostnames of the devices, the egress port for the interface, whether the MAC address originated from the given device, whether it learns the MAC address from the peer (`remote=yes`), and the last time the configuration changed.

```
cumulus@switch:~$ netq show macs vlan 10
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    00:00:00:00:00:1a  10     leaf04            bridge                         no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:37  10     leaf04            vni10                          no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:59  10     leaf04            vni10                          no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:38  10     leaf04            vni10                          yes    Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:3e  10     leaf04            bond1                          no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:3e  10     leaf04            bond1                          no     Tue Oct 27 22:29:07 2020
yes    44:38:39:00:00:5e  10     leaf04            bridge                         no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:32  10     leaf04            vni10                          yes    Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:5d  10     leaf04            peerlink                       no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:44  10     leaf04            bond1                          no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:32  10     leaf04            vni10                          yes    Tue Oct 27 22:29:07 2020
yes    36:ae:d2:23:1d:8c  10     leaf04            vni10                          no     Tue Oct 27 22:29:07 2020
yes    00:00:00:00:00:1a  10     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:59  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:37  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:38  10     leaf03            vni10                          yes    Tue Oct 27 22:28:24 2020
yes    36:99:0d:48:51:41  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:3e  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:5e  10     leaf03            peerlink                       no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:3e  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
...
```

The following example shows MAC addresses associated with the leaf02 switch and VLAN 10 that use the bridge port.

```
cumulus@netq-ts:~$ netq leaf02 show macs egress-port bridge vlan 10
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    00:00:00:00:00:1a  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
yes 
```
### Related Commands

- ```netq show mac-commentary```
- ```netq show mac-history```

- - -

## netq show mlag

Displays the health of all MLAG sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The peer nodes for a given node
- The system MAC address used for the session between the nodes
- The operational state of the session (up or down)
- The operational state of the backup IP address (up or down)
- The total number of bonds
- The number of dual-connected bonds
- When the last change occurred for any of these items

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format |

### Sample Usage

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

- ```netq show events type clag```
- ```netq check mlag```
- ```netq show unit-tests mlag```

- - -

## netq show neighbor-history

Displays when the neighbor configuration changed for an IP address. By default, the changes display in chronological order. You can filter the output by time and interface, and you can choose to view only differences or group the output by historical thread.

The output provides the following information for each neighbor change:

- When the neighbor configuration changed
- Switch associated with the change
- Interface used by the neighbor
- VRF used by the neighbor
- Whether the switch owned the address or the neighbor learned it
- IP and MAC addresses
- Whether the IP address is an IPv4 or IPv6 address
- Index of the IP interface address

By default, each row in the output is a thread (or group) sorted by VLAN and the time range used is now to one hour ago.

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
| json | NA | Display the output in JSON format |

### Sample Usage

The following example displays a full chronology of changes for an IP address neighbor. A caret (^) notation indicates that the value from the row preceding it has not changed.

```
cumulus@switch:~$ netq show neighbor-history 10.1.10.2

Matching neighborhistory records:
Last Changed              Hostname          Ifname       Vrf             Remote Ifindex        Mac Address        Ipv6     Ip Address
------------------------- ----------------- ------------ --------------- ------ -------------- ------------------ -------- -------------------------
Tue Sep 29 17:25:08 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:17 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
```
The following example displays the history of an IP address neighbor by hostname.

```
cumulus@switch:~$ netq show neighbor-history 10.1.10.2 listby hostname

Matching neighborhistory records:
Last Changed              Hostname          Ifname       Vrf             Remote Ifindex        Mac Address        Ipv6     Ip Address
------------------------- ----------------- ------------ --------------- ------ -------------- ------------------ -------- -------------------------
Tue Sep 29 17:25:08 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:17 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
```
The following example displays the history of an IP address neighbor between now and two hours ago.

```
cumulus@switch:~$ netq show neighbor-history 10.1.10.2 between 2h and now

Matching neighborhistory records:
Last Changed              Hostname          Ifname       Vrf             Remote Ifindex        Mac Address        Ipv6     Ip Address
------------------------- ----------------- ------------ --------------- ------ -------------- ------------------ -------- -------------------------
Tue Sep 29 15:35:18 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 15:35:22 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
Tue Sep 29 17:25:00 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:08 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
Tue Sep 29 17:25:08 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:14 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
```
### Related Commands

- ```netq show address-history```
- ```netq show mac-history```

- - -

## netq show notification

Displays the configuration of notification channels, filters, rules, or the proxy (if configured). Supported notification channels include email, PagerDuty, Slack, and `syslog`. The output varies according to the component you want to view. Refer to {{<link title="Configure System Event Notifications">}} for additional information.

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
| filter | NA | Display all filter configurations |
| rule | NA | Display all rule configurations |
| proxy | NA | Display the proxy configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON format |

### Sample Usage

Display notification channels:

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

Display rules:

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

### Related Commands

- ```netq add notification```
- ```netq del notification```
- ```netq add tca```
- ```netq del tca```
- ```netq show tca```

- - -

## netq show ntp

Displays whether all or a specific node is in time synchronization with the NetQ appliance or VM currently or for a time in the past. The output provides:

- The synchronization status
- The current time server used for synchronization
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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

The following example shows the time synchronization status for all devices in the NVIDIA reference architecture. 

All border, leaf, and spine switches rely on the out-of-band management server running *ntpq* to provide their time; they are all synchronized. The out-of-band management server uses the *titan.crash-ove* server running *ntpq* to obtain and maintain time synchronization. Meanwhile, the NetQ server uses the *eterna.binary.net* server running *chronyc* to obtain and maintain time synchronization. The firewall switches are not time synchronized (which is expected). The *Stratum* value indicates the number of hierarchical levels the switch or host is from the reference clock.

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

Display all devices in the network that are out of time synchronization, and therefore need further investigation:

```
cumulus@switch:~$ netq show ntp out-of-sync
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
internet          no       -                 16      ntpq
```

### Related Commands

- `netq check ntp`
- `netq show events message_type ntp`
- `netq show unit-tests ntp`

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
| json | NA | Display the output in JSON format |

### Sample Usage

On-premises appliance or VM:

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

### Related Commands

- ```netq show opta-platform```

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
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@nswitch:~$ netq show opta-platform
Matching platform records:
Version                              Uptime                    Reinitialize Time
------------------------------------ ------------------------- --------------------------
3.2.0                                Fri Oct  2 22:04:17 2020  Wed Nov 11 21:53:57 2020
```

### Related Commands

- ```netq show opta-health```

- - -
<!-- vale off -->
## netq show ospf
<!-- vale on -->

Displays the health of all OSPF sessions or a single session on all nodes or a specific node in your network fabric currently or for a time in the past. The output displays:

- The host interface
- The routing domain (area)
- Whether it uses a numbered or unnumbered protocol
- The operational state of the session (up or down)
- The hostname and interface of the peer node
- When the last change occurred for any of these items

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
| NA | \<remote-interface\> | Only display results for the host interface with this name |
| area | \<area-id\> | Only display results for devices in this routing domain |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

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

This example show OSPF sessions on the *leaf01* switch:

```
cumulus@switch:~$ netq leaf01 show ospf
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
```

This example shows OSPF sessions for all devices using the *swp51* interface on the host node.

```
cumulus@switch:~$ netq show ospf swp51
Matching ospf records:
Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
```

### Related Commands

- ```netq show events```
- ```netq check ospf```
- ```netq show unit-tests ospf```

- - -

## netq show ptp

Displays PTP clock and configuration details, including:

- Clock identifications and hierarchies
- Quality and accuracy information
- PTP port counters

### Syntax

```
   netq [<hostname>] show ptp clock-details 
    [around <text-time>] 
    [json]
   
   netq [<hostname>] show ptp global-config 
    [around <text-time>] 
    [json]

   netq [<hostname>] show ptp port-status [<text-port>] 
    [around <text-time>] 
    [json]

   netq [<hostname>] show ptp counters [<text-port>]
   (tx | rx)
   [around <text-time>] 
   [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| clock-details | NA | Display grandmaster, parent, and clock IDs and clock quality and accurarcy |
| global-config | NA | Display priority, offset from master, and mean path delay thresholds |
| port-status | NA | Display hierarchy information (master, slave) |
| counters | NA | Display PTP port counters |
| NA | tx, rx | Display transmit (Tx) or receive (Rx) data |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq show ptp clock-details
Matching ptp records:
Hostname          Clock Domain             Clock Identity               Parent Clock Id                GrandMaster ID               Clock Quality              Clock Accuracy               PTP Ports Configured                     Steps Removed
----------------- ------------------------ ---------------------------- ------------------------------ ---------------------------- -------------------------- ---------------------------- ---------------------------------------- --------------------------
mlx-3700c-21      0                        1c:34:da:ff:fe:2d:a1:48      1c34da.fffe.2da148-0           1c:34:da:ff:fe:2d:a1:48      248                        254                          1                                        0
mlx-3700c-22      0                        1c:34:da:ff:fe:2d:a0:48      1c34da.fffe.2da148-1           1c:34:da:ff:fe:2d:a1:48      248                        254                          1                                        1
```

```
cumulus@switch:~$ netq show ptp global-config
Matching ptp records:
Hostname          Slave Only           Priority1          Priority2          Domain Number              Two Step Flag              OffSet From Master Max Threshold                                 OffSet From Master Min Threshold                                 Mean Path Delay Threshold
----------------- -------------------- ------------------ ------------------ -------------------------- -------------------------- ---------------------------------------------------------------- ---------------------------------------------------------------- --------------------------------------------------
mlx-3700c-21      0                    128                128                0                          0                          51                                                               -49                                                              200
mlx-3700c-22      0                    129                128                0                          0                          50                                                               -50                                                              200
```
```
cumulus@switch:~$ netq show ptp port-status
Matching ptp records:
Hostname          Interface                 PTP Status
----------------- ------------------------- --------------------
mlx-3700c-21      swp29                     MASTER
mlx-3700c-22      swp29                     SLAVE
```
```
cumulus@netq-appliance:~$ netq show ptp counters tx
Matching ptp records:
Hostname          Interface            Announce             Delay Request        Delay Response       Follow Up            Delay Resp. Follow U Peer Delay Request   Peer Delay Response  Management           Signaling
                                                                                                                           p
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
mlx-3700c-21      swp29                114997               0                    200863               229985               0                    0                    0                    0                    229985
mlx-3700c-22      swp29                12                   0                    0                    16                   0                    0                    0                    0                    16
```

### Related Commands

None

- - -

## netq show recommended-pkg-version

When you have a software manifest in place, this command displays the software packages and versions recommended for upgrade based on the installed Cumulus Linux release. You can then compare that to the packages installed on your switch(es) to determine if it differs from the manifest. Such a difference might occur if you upgraded one or more packages separately from the Cumulus Linux software itself.

The output provides the following information for each package:

- Hostname of the switch where the package resides
- Cumulus Linux release ID
- ASIC vendor supported
- CPU architecture supported
- Name and version of the package
- When the last change occurred for any of these items

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
| json | NA | Display the output in JSON format |

### Sample Usage

Display the packages recommended for upgrade on the *leaf12* switch:

```
cumulus@switch:~$ netq leaf12 show recommended-pkg-version
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf12            3.7.1                vx                   x86_64               switchd              1.0-cl3u30           Wed Feb  5 04:36:30 2020
```

Display the version of the `switchd` package recommended for use with Cumulus Linux 3.7.2:

```
cumulus@switch:~$ netq act-5712-09 show recommended-pkg-version release-id 3.7.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
act-5712-09       3.7.2                bcm                  x86_64               switchd              1.0-cl3u31           Wed Feb  5 04:36:30 2020
```

### Related Commands

- ```netq show cl-manifest```
- ```netq show cl-pkg-info```

- - -

## netq show resource-util

Displays the utilization of compute resources&mdash;CPU, disk, and memory&mdash;consumed by one or all switches and hosts in your network.

The output provides the following information for each switch or host:

- Hostname of the device
- CPU utilization for one or all devices
- Memory utilization for one or all devices
- Disk name
- Total disk storage, amount used, and percentage of total
- When the last change occurred for any of these items

### Syntax

Two forms of this command are available: one for CPU and memory utilization, and one for disk utilization.

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display compute resources for all network switches:

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

Display memory utilization for a given switch:

```
cumulus@switch:~$ netq leaf01 show resource-util memory
Matching resource_util records:
Hostname          Memory Utilization   Last Updated
----------------- -------------------- ------------------------
leaf01            92                   Wed Dec  9 16:19:28 2020
```

Display disk information for all switches:

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

- ```netq show cl-resource forwarding```
- ```netq show cl-resource acl```

- - -

## netq show roce-config

Displays RoCE configuration.
### Syntax
```
netq [<hostname>] show roce-config
    [<text-port>] 
    [around <text-time>] 
    [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the device with this name |
| NA | \<text-port\> | Filter by a specified port |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq show roce-config

Matching roce records:
Hostname          Interface       RoCE Mode  Enabled TCs  Mode     ECN Max  ECN Min  SP->DSCP   SP->PCP  SP->PG   SP->TC   PFC SPs  PFC Rx     PFC Tx     ETS Mode   Last Changed
----------------- --------------- ---------- ------------ -------- -------- -------- ---------- -------- -------- -------- -------- ---------- ---------- ---------- -------------------------
mlx-3700c-23      swp16           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp27           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp32           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp23           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp25           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp5            Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp26           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp4            Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp18           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp12           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp9            Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp30           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp21           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp13           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp1            Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp24           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp15           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp17           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-23      swp22           Lossless   0,3          ECN      1502208  156672   2 -> 26    2 -> 2   2 -> 1   2 -> 0   2        disabled   enabled    dwrr       Thu Mar 30 04:42:18 2023
mlx-3700c-24      swp8            Lossy      0,3          ECN      1502208  156672   3 -> 26    3 -> 3   3 -> 1   3 -> 3   -        disabled   disabled   dwrr       Wed Mar 29 11:00:51 2023
...
```

### Related Commands

- `netq show roce-counters`
- `netq check roce`

- - -
## netq show roce-counters

Displays RoCE counters for switches, DPUs, and NICs.

### Syntax

```
netq [<hostname>] show roce-counters 
    [<text-port>] tx | rx [roce | general] 
    [around <text-time>] 
    [json]
```

```
netq [<hostname>] show roce-counters dpu 
    [around <text-time>] 
    [json]
```
```
netq [<hostname>] show roce-counters nic 
    [<text-device-name>]  
    [around <text-time>] 
    [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the device with this name |
| NA | tx | Display tx info |
| NA | rx | Display rx info |
| NA | \<text-device-name\>  | Only display results for the NIC with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display general and CNP Rx counters:

```
cumulus@switch:~$ netq show roce-counters rx general

Matching roce records:
Hostname          Interface            PG packets           PG bytes             no buffer discard    buffer usage         buffer max usage     PG usage             PG max usage
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
switch            swp1s1               1627273              152582910            0                    0                    1                    0                    1
switch            swp1s2               1627273              152582910            0                    0                    1                    0                    1
switch            swp63s1              1618361              160178796            0                    0                    2                    0                    2
switch            swp1s0               1627273              152582910            0                    0                    1                    0                    1
switch            swp63s3              1618361              160178796            0                    0                    2                    0                    2
switch            swp1s3               1627273              152582910            0                    0                    1                    0                    1
switch            swp63s0              1094532              120228456            0                    0                    1                    0                    1
switch            swp63s2              1618361              160178796            0                    0                    2                    0                    2
```

Display RoCE-specific Rx counters:

```
cumulus@switch:~$ netq show roce-counters rx roce

Matching roce records:
Hostname          Interface       PG packets   PG bytes     no buffer discard  PFC pause packets  PFC pause duration buffer usage buffer max usage   PG usage     PG max usage
----------------- --------------- ------------ ------------ ------------------ ------------------ ------------------ ------------ ------------------ ------------ ---------------
switch            swp1s1          0            0            0                  0                  0                  0            0                  0            0
switch            swp1s2          0            0            0                  0                  0                  0            0                  0            0
switch            swp63s1         0            0            0                  0                  0                  0            0                  0            0
switch            swp1s0          0            0            0                  0                  0                  0            0                  0            0
switch            swp63s3         0            0            0                  0                  0                  0            0                  0            0
switch            swp1s3          0            0            0                  0                  0                  0            0                  0            0
switch            swp63s0         0            0            0                  0                  0                  0            0                  0            0
switch            swp63s2         0            0            0                  0                  0                  0            0                  0            0
```

Display RoCE-specific Tx counters:

```
cumulus@switch:~$ netq show roce-counters tx roce 

Matching roce records:
Hostname          Interface       TC packets TC bytes   unicast no buffer discard PFC pause packets  PFC pause duration buffer usage buffer max usage   TC usage   TC max usage
----------------- --------------- ---------- ---------- ------------------------- ------------------ ------------------ ------------ ------------------ ---------- ---------------
switch            swp1s1          0          0          0                         0                  0                  0            0                  0          0
switch            swp1s2          0          0          0                         0                  0                  0            0                  0          0
switch            swp63s1         0          0          0                         0                  0                  0            0                  0          0
switch            swp1s0          0          0          0                         0                  0                  0            0                  0          0
switch            swp63s3         0          0          0                         0                  0                  0            0                  0          0
switch            swp1s3          0          0          0                         0                  0                  0            0                  0          0
switch            swp63s0         0          0          0                         0                  0                  0            0                  0          0
switch            swp63s2         0          0          0                         0                  0                  0            0                  0          0
```

To view counters for a specific switch port, include the switch name with the command:

```
cumulus@switch:~$ netq show roce-counters swp1s1 rx general 

Matching roce records:
Hostname          Interface            PG packets           PG bytes             no buffer discard    buffer usage         buffer max usage     PG usage             PG max usage
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
switch            swp1s1               1643392              154094520            0                    0                    1                    0                    1
```
Dislpay RoCE counters for BlueField DPUs:

```
cumulus@dpu:~$ netq show roce-counters dpu 

Matching roce records:
Hostname          Device Name          Port Name            Rx Prio3 Bytes       Rx Prio3 Buf Discard Rx Prio3 Packets     Rx Prio3 Cong Discar Rx Prio3 Discards    Tx Prio3 Bytes       Tx Prio3 Packets     Np Cnp Sent          Np Ecn Marked Roce P Rp Cnp Handled       Rp Cnp Ignored
                                                                                                                           d                                                                                                        ackets
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
r-netq-bf2-01-dpu pf0hpf               pf0hpf               0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
r-netq-bf2-01-dpu pf1hpf               pf1hpf               0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
r-netq-bf2-01-dpu enp3s0f1s0           enp3s0f1s0           0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
r-netq-bf2-01-dpu enp3s0f0s0           enp3s0f0s0           0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
r-netq-bf2-01-dpu en3f0pf0sf0          en3f0pf0sf0          0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
r-netq-bf2-01-dpu p0                   p0                   0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
r-netq-bf2-01-dpu en3f1pf1sf0          en3f1pf1sf0          0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
r-netq-bf2-01-dpu p1                   p1                   1.23 GB              0                    176                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
01
```

Display RoCE counters for ConnectX NICs:

```
cumulus@nic:~$ netq show roce-counters nic 

Matching roce records:
Hostname          Device Name          Port Name            Rx Prio3 Bytes       Rx Prio3 Buf Discard Rx Prio3 Packets     Rx Prio3 Cong Discar Rx Prio3 Discards    Tx Prio3 Bytes       Tx Prio3 Packets     Np Cnp Sent          Np Ecn Marked Roce P Rp Cnp Handled       Rp Cnp Ignored
                                                                                                                           d                                                                                                        ackets
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
fit-l-vrt-netq-40 ens7f1np1            ens7f1np1            146.28 GB            0                    2379794807           0                    0                    151.58 GB            149834335613         0 Bytes              0 Bytes              0                    0
fit-l-vrt-netq-40 ens8f1np1            ens8f1np1            0 Bytes              0                    0                    0                    0                    0 Bytes              0                    0 Bytes              0 Bytes              0                    0
```
### Related Commands

- `netq show roce-config`
- `netq show roce-counters pool`
- `netq check roce`
- `netq show events`

- - -

## netq show roce-counters pool

Displays RoCE counter pools.

### Syntax 

```
netq [<hostname>] show roce-counters pool 
    [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the device with this name |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq show roce-counters pool 

Matching roce records:
Hostname          Lossy Default Ingress Size     Roce Reserved Ingress Size     Lossy Default Egress Size      Roce Reserved Egress Size
----------------- ------------------------------ ------------------------------ ------------------------------ ------------------------------
switch            104823                         104823                         104823                         104823
```

### Related Commands

- ```netq show roce-config```
- ```netq check roce```
- ```netq show events```

- - -
## netq show sensors

Displays the status of all fan, power supply, and temperature sensors on all nodes or a specific node in your network fabric currently or for a time in the past. The output provides:

- The sensor name and user-defined description
- The operational state of the sensor
- Any messages, when available
- When the last change occurred for any of these items

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
| psu | \<psu-name\> | Display data for all power supply unit sensors or the one specified using the `psu-name` value |
| temp | \<temp-name\> | Display data for all temperature sensors or the one specified using the `temp-name` value |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display data for the *fan4* sensor on all nodes:

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

Display the state of all temperature sensors with the name *psu2temp1*:

```
cumulus@switch:~$ netq show sensors temp psu2temp1
Matching sensors records:
Hostname          Name            Description                         State      Temp     Critical Max      Min      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- -------- -------- -------- -------- ----------------------------------- -------------------------
border01          psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border02          psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
fw1               psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw2               psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
leaf01            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 18:30:07 2020
leaf02            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 18:08:38 2020
leaf03            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:20:34 2020
leaf04            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 14:20:22 2020
spine01           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 10:53:17 2020
spine02           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 10:54:07 2020
spine03           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 11:00:44 2020
spine04           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 10:52:00 2020
```
### Related Commands

- ```netq show events```
- ```netq check sensors```
- ```netq show unit-tests sensors```

- - -

## netq show services

Displays configuration and health of system-level services for one or all switches and hosts, currently or for a time in the past. You can filter the output by switch, service, VRF, and status. 

Supported services include:

- **aclinit**: `aclinit` service
- **acltool**: `acltool` service
- **bgp**: BGP (Border Gateway Protocol) service
- **bgpd**: BGP daemon
- **chrony**:  `chrony` service
- **clagd**: MLAG (Multi-chassis Link Aggregation) daemon
- **cumulus-chassis-ssh**: cumulus-chassis-ssh
- **cumulus-chassisd**: cumulus-chassisd
- **database**: database
- **dhcp_relay**: DHCP relay service
- **docker**: Docker container service
- **ledmgrd**: Switch LED manager daemon
- **lldp**: LLDP (Link Layer Discovery Protocol) service
- **lldpd**: LLDP daemon
- **mstpd**: MSTP (Multiple Spanning Tree Protocol) daemon
- **neighmgrd**: Neighbor manager daemon for BGP and OSPF
- **netq-agent**: NetQ Agent service
- **netqd**: NetQ application daemon
- **ntp**: Network Time Protocol (NTP) service
- **pmon**: Process monitor service
- **portwd**: Port watch daemon
- **ptmd**: PTM (Prescriptive Topology Manager) daemon
- **ptp4l**: PTP (Precision Time Protocol) service
- **pwmd**: Password manager daemon
- **radv**: Route advertiser service
- **rsyslog**: Rocket-fast system event logging processing service
- **smond**: System monitor daemon
- **ssh**: Secure shell service for switches and servers
- **status**: Show services with a given status (*ok*, *error*, *warning*, *fail*)
- **switchd**: Cumulus Linux `switchd` service for hardware acceleration
- **swss**: SONiC switch state service daemon
- **sx_sdk**: Spectrum ASIC SDK service
- **syncd**: Synchronization service
- **syslog**: System event logging service
- **teamd**: Network team service
- **vrf**: VRF (Virtual Route Forwarding) service
- **wd_keepalive**: Software watchdog service
- **zebra**: GNU Zebra routing daemon

The output provides the following information for each switch and host:

- Service name and ID
- VRF used by the service
- Whether the service is enabled, active, and monitored
- Status of the service
- How long the service has been up and running
- The last time any of these items changed

{{<notice tip>}}
Run <code>netq config add color</code> to display services that are not enabled, active, or monitored in red text.
{{</notice>}}

### Syntax

Two forms of this command are available: one for all information, and one for a particular status.

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
Use the following command to display the total CPU and memory usage from services:

```
netq [<hostname>] show services resource-util
    [<service-name>] 
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
| NA | \<service-name\> | Only display results for the service with this name |
| vrf | \<vrf\> | Only display results for services using this VRF |
| active | NA | Only display results for currently running services |
| monitored | NA | Only display results for monitored services |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display all services, switches, and hosts:

```
cumulus@switch:~$ netq show services
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
neo-switch01      pwmd                 11405 default         yes     yes    no        ok               72 day 8h ago             Tue Jul 18 13:59:28 2023
neo-switch01      lldpd                15988 default         yes     yes    yes       ok               50 day 10h ago            Tue Jul 18 13:59:42 2023
neo-switch01      docker               n/a   default         no      no     no        n/a              n/a                       Tue Jul 18 13:59:28 2023
neo-switch01      smond                11323 default         yes     yes    yes       ok               72 day 8h ago             Tue Jul 18 14:00:15 2023
neo-switch01      ssh                  1837  default         yes     yes    no        ok               72 day 8h ago             Tue Jul 18 13:59:28 2023
neo-switch01      dhcrelay             n/a   default         no      no     no        n/a              n/a                       Tue Jul 18 13:59:28 2023
neo-switch01      snmpd                n/a   default         no      no     no        n/a              n/a                       Tue Jul 18 13:59:28 2023
neo-switch01      mstpd                3671  default         yes     yes    yes       ok               72 day 8h ago             Tue Jul 18 14:00:14 2023
neo-switch01      netq-agent           16111 default         yes     yes    yes       ok               4h 56min ago              Tue Jul 18 13:59:28 2023
neo-switch01      switchd              15073 default         yes     yes    no        ok               50 day 10h ago            Tue Jul 18 13:59:28 2023
neo-switch01      bgpd                 2721  default         yes     yes    yes       ok               50 day 10h ago            Tue Jul 18 13:59:28 2023
neo-switch01      wd_keepalive         3471  default         yes     yes    no        ok               72 day 8h ago             Tue Jul 18 13:59:28 2023
neo-switch01      sx_sdk               13193 default         yes     yes    no        ok               50 day 10h ago            Tue Jul 18 13:59:28 2023
...
```

Display a given service:

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

Display services on a given switch or host:

```
cumulus@switch:~$ netq leaf02 show services
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
leaf02            air-agent            663   mgmt            yes     yes    no        ok               Tue Dec  8 21:15:00 2020  Tue Dec  8 21:15:00 2020
leaf02            snmpd                10098 mgmt            yes     yes    no        ok               Tue Dec  8 21:15:00 2020  Tue Dec  8 21:15:00 2020
leaf02            rsyslog              11937 default         yes     yes    no        ok               Tue Dec  8 21:15:00 2020  Tue Dec  8 21:15:00 2020
```

Display service CPU and memory usage from services across all switches:

```
cumulus@switch:~$ netq show services resource-util

Matching services records:
Hostname          Service              PID   VRF                  Enabled Active Uptime               CPU one Minute       CPU five Minute      Memory one Minute    Memory five Minute   Last Updated
----------------- -------------------- ----- -------------------- ------- ------ -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
r-3700-02         sx_sdk               19012 default              yes     yes    81 day 17h ago       7.7                  24.65                9.44                 9.44                 Tue Jul 18 18:49:19 2023
r-3700-03         sx_sdk               13627 default              yes     yes    81 day 18h ago       0                    17.82                9.44                 9.44                 Tue Jul 18 18:49:19 2023
r-3700-02         switchd              21100 default              yes     yes    81 day 17h ago       56.77                15.07                1.13                 1.13                 Tue Jul 18 18:49:19 2023
r-3700-03         switchd              15768 default              yes     yes    81 day 18h ago       0                    8.28                 1.11                 1.11                 Tue Jul 18 18:49:19 2023
neo-switch02      sx_sdk               1841  default              yes     yes    2h 29min ago         30.1                 6.55                 9.67                 9.67                 Tue Jul 18 18:49:19 2023
ufm-switch19      sx_sdk               2343  default              yes     yes    21h 3min ago         5.22                 5.73                 2.84                 2.84                 Tue Jul 18 18:49:19 2023
ufm-switch29      sx_sdk               2135  default              yes     yes    8 day 4h ago         2.88                 5.73                 9.54                 9.54                 Tue Jul 18 18:49:19 2023
r-3420-01         sx_sdk               1885  default              yes     yes    9 day 3h ago         5.28                 5.01                 9.3                  9.3                  Tue Jul 18 18:49:19 2023
ufm-switch29      clagd                7095  default              no      yes    8 day 4h ago         23.57                4.71                 0.63                 0.63                 Tue Jul 18 18:49:19 2023
r-3700-01         smond                7301  default              yes     yes    9 day 3h ago         0                    4.7                  0.2                  0.2                  Tue Jul 18 18:49:19 2023
... 
```
### Related Commands

- `netq show events`

- - -
## netq show status verbose

Displays the status of NetQ components after installation. Use this command to validate NetQ system readiness.

### Syntax

```
netq show status verbose
    [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@netq:~$ netq show status verbose
NetQ Live State: Active
Installation Status: FINISHED
Version: 4.10.1
Installer Version: 4.10.1
Installation Type: Standalone
Activation Key: EhVuZXRxLWasdW50LWdhdGV3YXkYsagDIixkWUNmVmhVV2dWelVUOVF3bXozSk8vb2lSNGFCaE1FR2FVU2dHK1k3RzJVPQ==
Master SSH Public Key: c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCfdsaHpjKzcwNmJiNVROOExRRXdLL3l5RVNLSHRhUE5sZS9FRjN0cTNzaHh1NmRtMkZpYmg3WWxKUE9lZTd5bnVlV2huaTZxZ0xxV3ZMYkpLMGdkc3RQcGdzNUlqanNMR3RzRTFpaEdNa3RZNlJYenQxLzh4Z3pVRXp3WTBWZDB4aWJrdDF3RGQwSjhnbExlbVk1RDM4VUdBVFVkMWQwcndLQ3gxZEhRdEM5L1UzZUs5cHFlOVdBYmE0ZHdiUFlaazZXLzM0ZmFsdFJxaG8rNUJia0pkTkFnWHdkZGZ5RXA1Vjc3Z2I1TUU3Q1BxOXp2Q1lXZW84cGtXVS9Wc0gxWklNWnhsa2crYlZ4MDRWUnN4ZnNIVVJHVmZvckNLMHRJL0FrQnd1N2FtUGxObW9ERHg2cHNHaU1EQkM0WHdud1lmSlNleUpmdTUvaDFKQ2NuRXpOVnVWRjUgcm9vdEBhbmlscmVzdG9yZQ==
Is Cloud: False
Kubernetes Cluster Nodes Status:
IP Address     Hostname       Role    NodeStatus
-------------  -------------  ------  ------------
10.188.46.243  10.188.46.243  Role    Ready
Task                                                                Status
------------------------------------------------------------------  --------
Prepared for download and extraction                                FINISHED
Completed setting up python virtual environment                     FINISHED
Checked connectivity from master node                               FINISHED
Installed Kubernetes control plane services                         FINISHED
Installed Calico CNI                                                FINISHED
Installed K8 Certificates                                           FINISHED
Updated etc host file with master node IP address                   FINISHED
Stored master node hostname                                         FINISHED
Generated and copied master node configuration                      FINISHED
Updated cluster information                                         FINISHED
Plugged in release bundle                                           FINISHED
Downloaded, installed, and started node service                     FINISHED
Downloaded, installed, and started port service                     FINISHED
Patched Kubernetes infrastructure                                   FINISHED
Removed unsupported conditions from master node                     FINISHED
Installed NetQ Custom Resource Definitions                          FINISHED
Installed Master Operator                                           FINISHED
Updated Master Custom Resources                                     FINISHED
Updated NetQ cluster manager custom resource                        FINISHED
Installed Cassandra                                                 FINISHED
Created new database                                                FINISHED
Updated Master Custom Resources                                     FINISHED
Updated Kafka Custom Resources                                      FINISHED
Read Config Key ConfigMap                                           FINISHED
Backed up ConfigKey                                                 FINISHED
Read ConfigKey                                                      FINISHED
Created Keys                                                        FINISHED
Verified installer version                                          FINISHED
...
```

### Related Commands

- `netq install`

- - -
## netq show stp topology

Displays the Spanning Tree Protocol (STP) topology on a bridge or switch. If you do not have a bridge in your configuration, the output indicates such.

### Syntax

```
   netq <hostname> show stp topology
   [around <text-time>]
   [json]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display results for the switch or host with this name |
| around | \<text-time\> | <p>Indicates how far to go back in time for the disk utilization information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display the STP topology as viewed from the spine1 switch:

```
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
                                    -- spine2:sw_clag300
                                    -- edge2:EdgeIntf(sng_hst2) -- hsedge21
                                    -- edge2:EdgeIntf(dual_host2) -- hdedge2
                                    -- edge2:EdgeIntf(dual_host1) -- hdedge1
                                    -- edge2:ClagIsl(peer-bond1) -- edge1
                                    -- edge1:EdgeIntf(sng_hst2) -- hsedge11
                                    -- edge1:EdgeIntf(dual_host2) -- hdedge2
                                    -- edge1:EdgeIntf(dual_host1) -- hdedge1
                                    -- edge1:ClagIsl(peer-bond1) -- edge2
```

### Related Commands

None

- - -
## netq show tca

Displays the configuration information for all user-specified threshold-based event notifications. You can filter the output by the identifier of the configuration. The output provides the following information for each notification configuration:

- Configuration name
- Name of the managed event
- Scope indicating what this configuration should include or exclude from management
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
| json | NA | Display the output in JSON format |

### Sample Usage

Show all TCA event configurations:

```
cumulus@switch:~$ netq show tca
Matching config_tca records:
TCA Name                     Event Name           Scope                      Severity Channel/s          Active Threshold          Unit     Threshold Type Suppress Until
---------------------------- -------------------- -------------------------- -------- ------------------ ------ ------------------ -------- -------------- ----------------------------
TCA_CPU_UTILIZATION_UPPER_1  TCA_CPU_UTILIZATION_ {"hostname":"leaf01"}      info     pd-netq-events,slk True   87                 %        user_set       Fri Oct  9 15:39:35 2020
                             UPPER                                                    -netq-events
TCA_CPU_UTILIZATION_UPPER_2  TCA_CPU_UTILIZATION_ {"hostname":"*"}           error    slk-netq-events    True   93                 %        user_set       Fri Oct  9 15:39:56 2020
                             UPPER
TCA_DOM_BIAS_CURRENT_ALARM_U TCA_DOM_BIAS_CURRENT {"hostname":"leaf*","ifnam error    slk-netq-events    True   0                  mA       vendor_set     Fri Oct  9 16:02:37 2020
PPER_1                       _ALARM_UPPER         e":"*"}
TCA_DOM_RX_POWER_ALARM_UPPER TCA_DOM_RX_POWER_ALA {"hostname":"*","ifname":" info     slk-netq-events    True   0                  mW       vendor_set     Fri Oct  9 15:25:26 2020
_1                           RM_UPPER             *"}
TCA_SENSOR_TEMPERATURE_UPPER TCA_SENSOR_TEMPERATU {"hostname":"leaf","s_name error    slk-netq-events    True   32                 degreeC  user_set       Fri Oct  9 15:40:18 2020
_1                           RE_UPPER             ":"temp1"}
TCA_TCAM_IPV4_ROUTE_UPPER_1  TCA_TCAM_IPV4_ROUTE_ {"hostname":"*"}           error    pd-netq-events     True   20000              %        user_set       Fri Oct  9 16:13:39 2020
                             UPPER
```

Show a specific TCA configuration:

```
cumulus@switch:~$ netq show tca tca_id TCA_TXMULTICAST_UPPER_1
Matching config_tca records:
TCA Name                     Event Name           Scope                      Severity         Channel/s          Active Threshold          Suppress Until
---------------------------- -------------------- -------------------------- ---------------- ------------------ ------ ------------------ ----------------------------
TCA_TXMULTICAST_UPPER_1      TCA_TXMULTICAST_UPPE {"ifname":"swp3","hostname info             tca-tx-bytes-slack True   0                  Sun Dec  8 16:40:14 2269
                             R                    ":"leaf01"}
```

### Related Commands

- ```netq add tca```
- ```netq del tca```
- ```netq show notification```

- - -

## netq show trace

Displays the configuration settings for a given scheduled trace, summary results of all scheduled traces, or full results of scheduled traces. Use the summary form to obtain the job ID. The output varies based on the form of the command. Note that on-demand trace results appear the terminal window when the command runs.

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display full results for given trace:

```
cumulus@switch:~$ netq show trace results e58bcf94-6922-40e4-ab2e-ff29aefe0120
Job ID                                             ID                        Errors       Warnings         Hops     MTU    Failure reason               Timestamp
-------------------------------------------------- ------------------------- ------------ ---------------- -------- ------ ---------------------------- -------------------------
e58bcf94-6922-40e4-ab2e-ff29aefe0120               1                         0            0                2        9216   N/A                          Tue Jan 16 08:25:02 2024
e58bcf94-6922-40e4-ab2e-ff29aefe0120               1                         0            0                2        9216   N/A                          Tue Jan 16 08:20:02 2024
e58bcf94-6922-40e4-ab2e-ff29aefe0120               1                         0            0                2        9216   N/A                          Tue Jan 16 08:15:02 2024
```

Display configuration settings:

```
cumulus@switch:~$ netq show trace settings name Lf01toBor01Daily
```

Display summary results for last 24 hours:

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
...
```

### Related Commands

- `netq add trace`
- `netq del trace`
- `netq trace`
- `netq show events type trace`

- - -

## netq show unit-tests

Displays a list of all validation tests that you can run for the associated `netq check` command. The output provides an ID, name, and brief description of each validation test.

### Syntax

```
netq show unit-tests address 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests agent 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests bgp
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests cl-version 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests evpn 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests interfaces 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests mlag 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests mtu 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests ntp 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests ospf 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests roce 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests sensors 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests topology 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests vlan 
    [check_filter_id <text-check-filter-id>] 
    [json]

netq show unit-tests vxlan 
    [check_filter_id <text-check-filter-id>] 
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| <!-- vale off -->address, agent, bgp, cl-version, evpn, interfaces, mlag, mtu, ntp, ospf, roce, sensors, topology, vlan, or vxlan<!-- vale on --> | NA | Display tests run during standard validation for the protocol or service with this name |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| check_filter_id | \<text-check-filter-id\> | Include the specific filter for a validation |
| json | NA | Display the output in JSON format |

### Sample Usage

Display list of BGP validation tests:

```
cumulus@netq-ts:~$ netq show unit-tests bgp
   0 : Session Establishment     - check if BGP session is in established state
   1 : Address Families          - check if tx and rx address family advertisement is consistent between peers of a BGP session
   2 : Router ID                 - check for BGP router id conflict in the network
   3 : Hold Time                 - check for mismatch of hold time between peers of a BGP session
   4 : Keep Alive Interval       - check for mismatch of keep alive interval between peers of a BGP session
   5 : Ipv4 Stale Path Time      - check for mismatch of ipv4 stale path timer between peers of a BGP session
   6 : Ipv6 Stale Path Time      - check for mismatch of ipv6 stale path timer between peers of a BGP session
   7 : Interface MTU             - check for consistency of Interface MTU for BGP peers

Configured global result filters:

Configured per test result filters:
```

### Related Commands

- ```netq show events```
- ```netq check```

- - -

## netq show validation settings

Displays one or all scheduled validations, including their name, type, cadence, when the validation began, its creation time, and whether it is currently active. This is useful for obtaining the name of a scheduled validation for use in other validation commands.

### Syntax

```
netq show validation settings
    [name <text-validation-name>]
    [type addr|agents|bgp|evpn|interfaces|mlag|mtu|ntp|ospf|roce|sensors|topology|vlan|vxlan]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| name | \<text-validation-name\> | Filter output to view settings for the scheduled validation with this name |
| type | <!-- vale off -->addr, agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, roce, sensors, topology, vlan, or vxlan<!-- vale on --> | Filter output to view settings for only the indicated protocol or service |
| json | NA | Display the output in JSON format |

### Sample Usage
<!-- update example-->
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

- ```netq add validation```
- ```netq del validation```
- ```netq show validation summary```

- - -

## netq show validation summary

Displays summary status of a scheduled validation for a given protocol or service, including their name, type, job ID, number of nodes validated, number of nodes that failed validation, number of nodes running the protocol or service, and time the validation last ran.

### Syntax

```
netq show validation summary
    [name <text-validation-name>]
    type (addr | agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | roce | sensors | topology | vlan | vxlan)
    [around <text-time-hr>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| type | <!-- vale off -->addr, agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, roce, sensors, topology, vlan or vxlan <!-- vale on --> | Show validation runs summary for the indicated protocol or service |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| name | \<text-validation-name\> | Filter output to view settings for the scheduled validation with this name |
| around | \<text-time-hr\> | Show summary status for this time in the past. You must specify the value in hours and include the *h* time unit. Default is 24 hours. |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Sample Usage

Display EVPN scheduled validations summary for the past 24 hours:

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

- ```netq add validation```
- ```netq del validation```
- ```netq show validation settings```

- - -

## netq show vlan

Displays the configuration of all VLANs on all nodes or a specific node in your network fabric currently or for a time in the past. The output displays:

- The switch or hostname
- The VLANs associated with that node
- The SVIs (switch virtual interfaces) associated with that node
- When the last change occurred for any of these items

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
| NA | \<1-4096\> | Only display results for the VLANs within this range |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

The following example shows the VLANs configured across a network based on the NVIDIA reference architecture:

```
cumulus@switch:~$ netq show vlan
Matching vlan records:
Hostname          VLANs                     SVIs                      Last Changed
----------------- ------------------------- ------------------------- -------------------------
border01          1,10,20,30,4001-4002                                Wed Oct 28 14:46:33 2020
border02          1,10,20,30,4001-4002                                Wed Oct 28 14:46:33 2020
leaf01            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf02            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf03            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf04            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
```
The following example shows the VLANs configured on the leaf02 switch:

```
cumulus@switch:~$ netq leaf02 show vlan
Matching vlan records:
Hostname          VLAN   Ports                               SVI  Last Changed
----------------- ------ ----------------------------------- ---- -------------------------
leaf02            20     bond2,vni20                         yes  Wed Oct 28 15:14:11 2020
leaf02            30     vni30,bond3                         yes  Wed Oct 28 15:14:11 2020
leaf02            1      peerlink                            no   Wed Oct 28 15:14:11 2020
leaf02            10     bond1,vni10                         yes  Wed Oct 28 15:14:11 2020
leaf02            4001   vniRED                              yes  Wed Oct 28 15:14:11 2020
leaf02            4002   vniBLUE                             yes  Wed Oct 28 15:14:11 2020
```
The following example shows that vlan 10 is running on the two border and four leaf switches:

```
cumulus@switch~$ netq show vlan 10
Matching vlan records:
Hostname          VLAN   Ports                               SVI  Last Changed
----------------- ------ ----------------------------------- ---- -------------------------
border01          10                                         no   Wed Oct 28 15:20:27 2020
border02          10                                         no   Wed Oct 28 15:20:28 2020
leaf01            10     bond1,vni10                         yes  Wed Oct 28 15:20:28 2020
leaf02            10     bond1,vni10                         yes  Wed Oct 28 15:20:28 2020
leaf03            10     bond1,vni10                         yes  Wed Oct 28 15:20:29 2020
leaf04            10     bond1,vni10                         yes  Wed Oct 28 15:20:29 2020
```

### Related Commands

- `netq show events message_type vlan`
- `netq show interfaces type vlan`
- `netq show macs`
- `netq check vlan`
- `netq show unit-tests vlan`

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
- When the last change occurred for any of these items

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
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. You write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

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

Display configuration for a given VNI:

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
- ```netq show events message_type vxlan```
- ```netq show interfaces type vxlan```
- ```netq check vxlan```
- ```netq show unit-tests vxlan```
<!-- vale on -->
- - -

## netq show wjh-drop

Displays packet drops due to buffer congestion, incorrect routing, tunnel, ACL and layer 1 and 2 problems on NVIDIA Spectrum switches. You can filter drops of a particular type by various attributes. The output varies according to the type of drop. Refer to the {{<link title="WJH Events Reference">}} for descriptions of the supported drop reasons and {{<link title="Configure and Monitor What Just Happened/#view-what-just-happened-metrics" text="View WJH Metrics">}} for more info on viewing and interpreting WJH data.

### Syntax

<!-- vale off -->
```
netq [<hostname>] show wjh-drop 
    [severity <text-severity>] 
    [details] 
    [between <text-fixed-time> and <text-fixed-endtime>] 
    [around <text-fixed-time>] 
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
    [vlan <text-vlan>]
    [between <text-time> and <text-endtime>] 
    [around <text-time>] 
    [json]
```
An additional command is available that aggregates WJH L1 errors that occur on the same ingress port.
```
netq [<hostname>] show wjh-drop l1 
    [ingress-port <text-ingress-port>] 
    [severity <text-severity>]
    [reason <text-reason>] 
    [port-aggregate <text-port-aggregate>] 
    [between <text-time> and <text-endtime>] 
    [around <text-time>] [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-drop-type\> | Only display results for this type of packet drop. Types include *l1*, *l2*, *router*, *tunnel*, *buffer*, and *acl*. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname\> | Only display drops for the switch or host with this name |
| severity | \<text-severity\> | Only display drops with this severity; *error*, *warning*, or *notice* |
| details | NA | Display drop count and reason for all drop types |
| ingress-port | \<text-ingress-port\> | Only display drops for the ingress port with this name |
| port-aggregate | \<text-port-aggregate\> | Aggregate drops according to their respective ports (True) or list all ports (False) |
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
| vlan | \<text-vlan\> | Display drops for the VLAN with this ID. VLANs range from 1-4096. |
| between | \<text-time\> and \<text-endtime\> | <p>Only display results between these two times. Times must include a numeric value <em>and</em> the unit of measure:<ul><li><strong>w</strong>: weeks</li><li><strong>d</strong>: days</li><li><strong>h</strong>: hours</li><li><strong>m</strong>: minutes</li><li><strong>s</strong>: seconds</li><li><strong>now</strong></li></ul></p><p>You can enter the start time (<code>text-time</code>) and end time (<code>text-endtime</code>) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.</p> |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |

### Sample Usage

Display drops for a given switch or host:

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

Display L2 drops:

```
cumulus@mlx-2700-03:mgmt:~$ netq show wjh-drop l2
Matching wjh records:
Hostname          Ingress Port             Reason                                        Agg Count          Src Ip           Dst Ip           Proto  Src Port         Dst Port         Src Mac            Dst Mac            First Timestamp                Last Timestamp
----------------- ------------------------ --------------------------------------------- ------------------ ---------------- ---------------- ------ ---------------- ---------------- ------------------ ------------------ ------------------------------ ----------------------------
mlx-2700-03       swp1s2                   Port loopback filter                          10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  0c:ff:ff:ff:ff:ff  Mon Dec 16 11:54:15 2019       Mon Dec 16 11:54:15 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:53:17 2019       Mon Dec 16 11:53:17 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 0.0.0.0          0.0.0.0          0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:40:44 2019       Mon Dec 16 11:40:44 2019
```

Display ACL drops:

```
cumulus@switch:~$ netq show wjh-drop acl
Matching wjh records:
Hostname          Ingress Port             Reason                                        Severity         Agg Count          Src Ip           Dst Ip           Proto  Src Port         Dst Port         Src Mac            Dst Mac            Acl Rule Id            Acl Bind Point               Acl Name         Acl Rule         First Timestamp                Last Timestamp
----------------- ------------------------ --------------------------------------------- ---------------- ------------------ ---------------- ---------------- ------ ---------------- ---------------- ------------------ ------------------ ---------------------- ---------------------------- ---------------- ---------------- ------------------------------ ----------------------------
leaf01            swp2                     Ingress router ACL                            Error            49                 55.0.0.1         55.0.0.2         17     8492             21423            00:32:10:45:76:89  00:ab:05:d4:1b:13  0x0                    0                                                              Tue Oct  6 15:29:13 2020       Tue Oct  6 15:29:39 2020
```

### Related Commands

- `netq config add agent wjh`
- `netq config add agent wjh-threshold`
- `netq config add agent wjh-drop-filter`
- `netq config restart agent`
