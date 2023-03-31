---
title: Validate Network Protocol and Service Operations
author: NVIDIA
weight: 1020
toc: 4
---
NetQ lets you validate the operation of the protocols and services running in your network either on demand or according to a schedule. For a general understanding of how well your network is operating, refer to the {{<link title="Validate Overall Network Health">}}.

<!-- vale off -->
## On-demand Validations
<!-- vale on -->

When you want to validate the operation of one or more network protocols and services right now, you can create and run on-demand validations using the NetQ UI or the NetQ CLI.

<!-- vale off -->
### Create an On-demand Validation
<!-- vale on -->
Using the NetQ UI, you can create an on-demand validation for multiple protocols or services at the same time. This is handy when the protocols are strongly related regarding a possible issue or if you only want to create one validation request.

{{<tabs "On-demand Validation">}}

{{<tab "Validate Network">}}

To create and run a request containing checks on one or more protocols or services within the NetQ UI:

1. In the workbench header, click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation**, then click **Create a validation**. Choose whether the on-demand validation should run on all devices or on specific {{<link title="Validate Network Protocol and Service Operations#validate-device-groups" text="device groups.">}}

2. On the left side of the card, select the protocols or services you want to validate by clicking on their names, then click **Next**.

   This example shows BGP:

   {{<figure src="/images/netq/validate-network-bgp.png" width="800">}}

3. Select **Now** and specify a workbench:

   {{<figure src="/images/netq/validate-network-schedule-4.0.0.png" width="400">}}

4. Click **Run** to start the check. It might take a few minutes for results to appear if the load on the NetQ system is heavy at the time of the run.

   The respective On-demand Validation Result card opens on your workbench. If you selected more than one protocol or service, a card opens for each selection. To view additional information about the errors reported, hover over a check and click **View details**. To view all data for all on-demand validation results for a given protocol, click **Show all results**.

   {{<figure src="/images/netq/on-demand-bgp-validation.png" width="600">}}

{{</tab>}}

{{<tab "netq check">}}

To create and run a request containing checks on a single protocol or service all within the NetQ CLI, run the relevant `netq check` command:

```
netq check addresses [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <addr-number-range-list> | exclude <addr-number-range-list>] [around <text-time>] [json | summary]
netq check agents [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <agents-number-range-list> | exclude <agents-number-range-list>] [around <text-time>] [json]
netq check bgp [label <text-label-name> | hostnames <text-list-hostnames>] [vrf <vrf>] [check_filter_id <text-check-filter-id>] [include <bgp-number-range-list> | exclude <bgp-number-range-list>] [around <text-time>] [json | summary]
netq check cl-version [label <text-label-name> | hostnames <text-list-hostnames>] [match-version <cl-ver> | min-version <cl-ver>] [check_filter_id <text-check-filter-id>] [include <version-number-range-list> | exclude <version-number-range-list>] [around <text-time>] [json | summary]
netq check clag [label <text-label-name> | hostnames <text-list-hostnames> ] [check_filter_id <text-check-filter-id>] [include <clag-number-range-list> | exclude <clag-number-range-list>] [around <text-time>] [json | summary]
netq check evpn [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <evpn-number-range-list> | exclude <evpn-number-range-list>] [around <text-time>] [json | summary]
netq check interfaces [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <interfaces-number-range-list> | exclude <interfaces-number-range-list>] [around <text-time>] [json | summary]
netq check mlag [label <text-label-name> | hostnames <text-list-hostnames> ] [check_filter_id <text-check-filter-id>] [include <mlag-number-range-list> | exclude <mlag-number-range-list>] [around <text-time>] [json | summary]
netq check mtu [label <text-label-name> | hostnames <text-list-hostnames>] [unverified] [check_filter_id <text-check-filter-id>] [include <mtu-number-range-list> | exclude <mtu-number-range-list>] [around <text-time>] [json | summary]
netq check ntp [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <ntp-number-range-list> | exclude <ntp-number-range-list>] [around <text-time>] [json | summary]
netq check ospf [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <ospf-number-range-list> | exclude <ospf-number-range-list>] [around <text-time>] [json | summary]
netq check roce [streaming] [hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <roce-number-range-list> | exclude <roce-number-range-list>] [around <text-time>] [json | summary]
netq check sensors [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <sensors-number-range-list> | exclude <sensors-number-range-list>] [around <text-time>] [json | summary]
netq check vlan [label <text-label-name> | hostnames <text-list-hostnames>] [unverified] [check_filter_id <text-check-filter-id>] [include <vlan-number-range-list> | exclude <vlan-number-range-list>] [around <text-time>] [json | summary]
netq check vxlan [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <vxlan-number-range-list> | exclude <vxlan-number-range-list>] [around <text-time>] [json | summary]
```

All `netq check` commands have a summary and test results section. Some have additional summary information.

Using the `include <bgp-number-range-list>` and `exclude <bgp-number-range-list>` options of the `netq check` command, you can include or exclude one or more of the various checks performed during the validation.

First determine the number of the tests you want to include or exclude. Refer to {{<link title="Validation Tests Reference">}} for a description of these tests and to get the test numbers for the tests to include or exclude. You can also get the test numbers and descriptions when you run the `netq show unit-tests` command.

Then run the `netq check` command.

The following example shows a BGP validation that includes only the session establishment and router ID tests. Note that you can obtain the same results using either of the `include` or `exclude` options and that the test that is not run is marked as *skipped*.

```
cumulus@switch:~$ netq show unit-tests bgp
   0 : Session Establishment     - check if BGP session is in established state
   1 : Address Families          - check if tx and rx address family advertisement is consistent between peers of a BGP session
   2 : Router ID                 - check for BGP router id conflict in the network

Configured global result filters:
Configured per test result filters:
```

```
cumulus@switch:~$ netq check bgp include 0,2
bgp check result summary:

Total nodes         : 10
Checked nodes       : 10
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Total Sessions      : 54
Failed Sessions     : 0

Session Establishment Test   : passed
Address Families Test        : skipped
Router ID Test               : passed
```

```
cumulus@switch:~$ netq check bgp exclude 1
bgp check result summary:

Total nodes         : 10
Checked nodes       : 10
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Total Sessions      : 54
Failed Sessions     : 0

Session Establishment Test   : passed
Address Families Test        : skipped
Router ID Test               : passed
```

{{</tab>}}

{{<tab "netq add validation">}}

To create a request containing checks on a single protocol or service in the NetQ CLI, run:

```
netq add validation type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf | roce | addr) [alert-on-failure]
```
The associated Validation Result card is accessible from the full-screen Validate Network card.

{{</tab>}}

{{</tabs>}}

### Run an Existing Scheduled Validation On Demand

To run a scheduled validation now:

1. Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation**, then click **Existing validations**.

2. Select one or more validations you want to run by clicking their names, then click **View results**.

3. The associated Validation Result cards open on your workbench.
### On-Demand CLI Validation Examples

This section provides CLI validation examples for a variety of protocols and elements. Refer to {{<link url="Validation-Tests-Reference" text="Validation Tests Reference">}} for descriptions of these tests.

{{<tabs "CLI Examples">}}

{{<tab "Addresses">}}

The duplicate address detection validation tests looks for duplicate IPv4 and IPv6 addresses assigned to interfaces across devices in the inventory, and checks for duplicate /32 host routes in each VRF.

```
cumulus@switch:mgmt:~$ netq check addresses
addr check result summary:

Total nodes         : 25
Checked nodes       : 25
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0
Skipped Nodes       : 0


IPV4 Duplicate Address Test   : passed
IPV6 Duplicate Address Test   : passed

```

{{</tab>}}

{{<tab "Agent">}}

The default validation confirms that the NetQ Agent is running on all monitored nodes and provides a summary of the validation results. This example shows the results of a fully successful validation.

```
cumulus@switch:~$ netq check agents
agent check result summary:

Checked nodes       : 13
Total nodes         : 13
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Agent Health Test   : passed
```

{{</tab>}}

{{<tab "BGP">}}

The default validation runs a networkwide BGP connectivity and configuration check on all nodes running the BGP service:

```
cumulus@switch:~$ netq check bgp
bgp check result summary:

Checked nodes       : 8
Total nodes         : 8
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Total Sessions      : 30
Failed Sessions     : 0

Session Establishment Test   : passed
Address Families Test        : passed
Router ID Test               : passed

```

This example indicates that all nodes running BGP and all BGP sessions are running properly. If there were issues with any of the nodes, NetQ would provide information about each node to aid in resolving the issues.

### Perform a BGP Validation for a Particular VRF

Using the `vrf <vrf>` option of the `netq check bgp` command, you can validate the BGP service where communication is occurring through a particular virtual route. In this example, the name of the VRF of interest is *vrf1*.

```
cumulus@switch:~$ netq check bgp vrf vrf1
bgp check result summary:

Checked nodes       : 2
Total nodes         : 2
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Total Sessions      : 2
Failed Sessions     : 0

Session Establishment Test   : passed
Address Families Test        : passed
Router ID Test               : passed
```

### Perform a BGP Validation with Selected Tests

Using the `include <bgp-number-range-list>` and `exclude <bgp-number-range-list>` options, you can include or exclude one or more of the various checks performed during the validation. You can select from the following BGP validation tests:

| Test Number | Test Name |
| :---------: | --------- |
| 0 | Session Establishment |
| 1 | Address Families |
| 2 | Router ID |

To include only the session establishment and router ID tests during a validation, run either of these commands:

```
cumulus@switch:~$ netq check bgp include 0,2

cumulus@switch:~$ netq check bgp exclude 1
```

Either way, a successful validation output should be similar to the following:

```
bgp check result summary:

Checked nodes       : 8
Total nodes         : 8
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Total Sessions      : 30
Failed Sessions     : 0

Session Establishment Test   : passed,
Address Families Test        : skipped
Router ID Test               : passed,
```

### Perform a BGP Validation and Output Results to JSON File

This example shows the default BGP validation results as it appears in a JSON file.

```
cumulus@switch:~$ netq check bgp json
{
    "tests":{
        "Session Establishment":{
            "suppressed_warnings":0,
            "errors":[

            ],
            "suppressed_errors":0,
            "passed":true,
            "warnings":[

            ],
            "duration":0.0000853539,
            "enabled":true,
            "suppressed_unverified":0,
            "unverified":[

            ]
        },
        "Address Families":{
            "suppressed_warnings":0,
            "errors":[

            ],
            "suppressed_errors":0,
            "passed":true,
            "warnings":[

            ],
            "duration":0.0002634525,
            "enabled":true,
            "suppressed_unverified":0,
            "unverified":[

            ]
        },
        "Router ID":{
            "suppressed_warnings":0,
            "errors":[

            ],
            "suppressed_errors":0,
            "passed":true,
            "warnings":[

            ],
            "duration":0.0001821518,
            "enabled":true,
            "suppressed_unverified":0,
            "unverified":[

            ]
        }
    },
    "failed_node_set":[

    ],
    "summary":{
        "checked_cnt":8,
        "total_cnt":8,
        "rotten_node_cnt":0,
        "failed_node_cnt":0,
        "warn_node_cnt":0
    },
    "rotten_node_set":[

    ],
    "warn_node_set":[

    ],
    "additional_summary":{
        "total_sessions":30,
        "failed_sessions":0
    },
    "validation":"bgp"
}
```

{{</tab>}}

{{<tab "CL Version">}}

The default validation (using no options) checks that all switches in the network have a consistent version.

```
cumulus@switch:~$ netq check cl-version
version check result summary:

Checked nodes       : 12
Total nodes         : 12
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0


Cumulus Linux Image Version Test   : passed
```

{{</tab>}}

{{<tab "EVPN">}}

The default validation runs a networkwide EVPN connectivity and configuration check on all nodes running the EVPN service. This example shows results for a fully successful validation.

```
cumulus@switch:~$ netq check evpn
evpn check result summary:

Checked nodes       : 6
Total nodes         : 6
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Failed BGP Sessions : 0
Total Sessions      : 16
Total VNIs          : 3

EVPN BGP Session Test            : passed,
EVPN VNI Type Consistency Test   : passed,
EVPN Type 2 Test                 : passed,
EVPN Type 3 Test                 : passed,
EVPN Session Test                : passed,
Vlan Consistency Test            : passed,
Vrf Consistency Test             : passed,
```
### Perform an EVPN Validation with Selected Tests

Using the `include <evpn-number-range-list>` and `exclude <evpn-number-range-list>` options, you can include or exclude one or more of the various checks performed during the validation. You can select from the following EVPN validation tests:

<!-- vale off -->
| Test Number | Test Name |
| :---------: | --------- |
| 0 | EVPN BGP Session |
| 1 | EVPN VNI Type Consistency |
| 2 | EVPN Type 2 |
| 3 | EVPN Type 3 |
| 4 | EVPN Session |
| 5 | L3 VNI RMAC |
| 6 | VLAN Consistency |
| 7 | VRF Consistency |
<!-- vale on -->

To run only the EVPN Type 2 test:

```
cumulus@switch:~$ netq check evpn include 2
evpn check result summary:

Checked nodes       : 6
Total nodes         : 6
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Failed BGP Sessions : 0
Total Sessions      : 0
Total VNIs          : 3

EVPN BGP Session Test            : skipped
EVPN VNI Type Consistency Test   : skipped
EVPN Type 2 Test                 : passed,
EVPN Type 3 Test                 : skipped
EVPN Session Test                : skipped
Vlan Consistency Test            : skipped
Vrf Consistency Test             : skipped
```

To exclude the BGP session and VRF consistency tests:

```
cumulus@switch:~$ netq check evpn exclude 0,6
evpn check result summary:

Checked nodes       : 6
Total nodes         : 6
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Failed BGP Sessions : 0
Total Sessions      : 0
Total VNIs          : 3

EVPN BGP Session Test            : skipped
EVPN VNI Type Consistency Test   : passed,
EVPN Type 2 Test                 : passed,
EVPN Type 3 Test                 : passed,
EVPN Session Test                : passed,
Vlan Consistency Test            : passed,
Vrf Consistency Test             : skipped
```

To run only the first five tests:

```
cumulus@switch:~$ netq check evpn include 0-4
evpn check result summary:

Checked nodes       : 6
Total nodes         : 6
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Failed BGP Sessions : 0
Total Sessions      : 16
Total VNIs          : 3

EVPN BGP Session Test            : passed,
EVPN VNI Type Consistency Test   : passed,
EVPN Type 2 Test                 : passed,
EVPN Type 3 Test                 : passed,
EVPN Session Test                : passed,
Vlan Consistency Test            : skipped
Vrf Consistency Test             : skipped
```

{{</tab>}}

{{<tab "Interfaces">}}

The default validation runs a networkwide connectivity and configuration check on all interfaces. This example shows results for a fully successful validation.

```
cumulus@switch:~$ netq check interfaces
interface check result summary:

Checked nodes       : 12
Total nodes         : 12
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Unverified Ports    : 56
Checked Ports       : 108
Failed Ports        : 0

Admin State Test   : passed,
Oper State Test    : passed,
Speed Test         : passed,
Autoneg Test       : passed,
```
### Perform an Interfaces Validation with Selected Tests

Using the `include <interface-number-range-list>` and `exclude <interface-number-range-list>` options, you can include or exclude one or more of the various checks performed during the validation. You can select from the following interface validation tests:

| Test Number | Test Name |
| :---------: | --------- |
| 0 | Admin State |
| 1 | Oper State |
| 2 | Speed |
| 3 | Autoneg |

{{</tab>}}

{{<tab "MTU">}}

The default validate verifies that all corresponding interface links have matching MTUs. This example shows no mismatches.

```
cumulus@switch:~$ netq check mtu
mtu check result summary:

Checked nodes       : 12
Total nodes         : 12
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Warn Links          : 0
Failed Links        : 0
Checked Links       : 196

Link MTU Consistency Test   : passed,
VLAN interface Test         : passed,
Bridge interface Test       : passed,
```

{{</tab>}}

{{<tab "MLAG">}}

The default validation runs a networkwide MLAG connectivity and configuration check on all nodes running the MLAG service. This example shows results for a fully successful validation.

```
cumulus@switch:~$ netq check mlag
mlag check result summary:

Checked nodes       : 4
Total nodes         : 4
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Peering Test             : passed,
Backup IP Test           : passed,
Clag SysMac Test         : passed,
VXLAN Anycast IP Test    : passed,
Bridge Membership Test   : passed,
Spanning Tree Test       : passed,
Dual Home Test           : passed,
Single Home Test         : passed,
Conflicted Bonds Test    : passed,
ProtoDown Bonds Test     : passed,
SVI Test                 : passed,
```

{{%notice note%}}

You can also run this check using `netq check clag` and get the same results.

{{%/notice%}}

This example shows representative results for one or more failures, warnings, or errors. In particular, you can see that you have duplicate system MAC addresses.

```
cumulus@switch:~$ netq check mlag
mlag check result summary:

Checked nodes       : 4
Total nodes         : 4
Rotten nodes        : 0
Failed nodes        : 2
Warning nodes       : 0

Peering Test             : passed,
Backup IP Test           : passed,
Clag SysMac Test         : 0 warnings, 2 errors,
VXLAN Anycast IP Test    : passed,
Bridge Membership Test   : passed,
Spanning Tree Test       : passed,
Dual Home Test           : passed,
Single Home Test         : passed,
Conflicted Bonds Test    : passed,
ProtoDown Bonds Test     : passed,
SVI Test                 : passed,

Clag SysMac Test details:
Hostname          Reason
----------------- ---------------------------------------------
leaf01            Duplicate sysmac with leaf02/None            
leaf03            Duplicate sysmac with leaf04/None            
```

### Perform an MLAG Validation with Selected Tests

Using the `include <mlag-number-range-list>` and `exclude <mlag-number-range-list>` options, you can include or exclude one or more of the various checks performed during the validation. You can select from the following MLAG validation tests:

| Test Number | Test Name |
| :---------: | --------- |
| 0 | Peering |
| 1 | Backup IP |
| 2 | <!-- vale off -->Clag<!-- vale on --> Sysmac |
| 3 | VXLAN <!-- vale off -->Anycast<!-- vale on --> IP |
| 4 | Bridge Membership |
| 5 | Spanning Tree |
| 6 | Dual Home |
| 7 | Single Home |
| 8 | Conflicted Bonds |
| 9 | ProtoDown Bonds |
| 10 | SVI |

To include only the CLAG SysMAC test during a validation:

```
cumulus@switch:~$ netq check mlag include 2
mlag check result summary:

Checked nodes       : 4
Total nodes         : 4
Rotten nodes        : 0
Failed nodes        : 2
Warning nodes       : 0

Peering Test             : skipped
Backup IP Test           : skipped
Clag SysMac Test         : 0 warnings, 2 errors,
VXLAN Anycast IP Test    : skipped
Bridge Membership Test   : skipped
Spanning Tree Test       : skipped
Dual Home Test           : skipped
Single Home Test         : skipped
Conflicted Bonds Test    : skipped
ProtoDown Bonds Test     : skipped
SVI Test                 : skipped

Clag SysMac Test details:
Hostname          Reason
----------------- ---------------------------------------------
leaf01            Duplicate sysmac with leaf02/None
leaf03            Duplicate sysmac with leaf04/None
```

To exclude the backup IP, CLAG SysMAC, and VXLAN anycast IP tests during a validation:

```
cumulus@switch:~$ netq check mlag exclude 1-3
mlag check result summary:

Checked nodes       : 4
Total nodes         : 4
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Peering Test             : passed,
Backup IP Test           : skipped
Clag SysMac Test         : skipped
VXLAN Anycast IP Test    : skipped
Bridge Membership Test   : passed,
Spanning Tree Test       : passed,
Dual Home Test           : passed,
Single Home Test         : passed,
Conflicted Bonds Test    : passed,
ProtoDown Bonds Test     : passed,
SVI Test                 : passed,
```

{{</tab>}}

{{<tab "NTP">}}

The default validation checks for synchronization of the NTP server with all nodes in the network. It is always important to have your devices in time synchronization to ensure that you can track configuration and management events and can make correlations between events.

This example shows that *server04* has an error.

```
cumulus@switch:~$ netq check ntp
ntp check result summary:

Checked nodes       : 12
Total nodes         : 12
Rotten nodes        : 0
Failed nodes        : 1
Warning nodes       : 0

Additional summary:
Unknown nodes       : 0
NTP Servers         : 3

NTP Sync Test   : 0 warnings, 1 errors,

NTP Sync Test details:
Hostname          NTP Sync Connect Time
----------------- -------- -------------------------
server04          no       2019-09-17 19:21:47
```

{{</tab>}}

{{<tab "OSPF">}}

The default validation runs a networkwide OSPF connectivity and configuration check on all nodes running the OSPF service. This example shows errors in the timers and interface MTU tests.

```
cumulus@switch:~# netq check ospf
Checked nodes: 8, Total nodes: 8, Rotten nodes: 0, Failed nodes: 4, Warning nodes: 0, Failed Adjacencies: 4, Total Adjacencies: 24

Router ID Test        : passed
Adjacency Test        : passed
Timers Test           : 0 warnings, 4 errors
Network Type Test     : passed
Area ID Test          : passed
Interface Mtu Test    : 0 warnings, 2 errors
Service Status Test   : passed

Timers Test details:
Hostname          Interface                 PeerID                    Peer IP                   Reason                                        Last Changed
----------------- ------------------------- ------------------------- ------------------------- --------------------------------------------- -------------------------
spine-1           downlink-4                torc-22                   uplink-1                  dead time mismatch                            Mon Jul  1 16:18:33 2019 
spine-1           downlink-4                torc-22                   uplink-1                  hello time mismatch                           Mon Jul  1 16:18:33 2019 
torc-22           uplink-1                  spine-1                   downlink-4                dead time mismatch                            Mon Jul  1 16:19:21 2019 
torc-22           uplink-1                  spine-1                   downlink-4                hello time mismatch                           Mon Jul  1 16:19:21 2019 

Interface Mtu Test details:
Hostname          Interface                 PeerID                    Peer IP                   Reason                                        Last Changed
----------------- ------------------------- ------------------------- ------------------------- --------------------------------------------- -------------------------
spine-2           downlink-6                0.0.0.22                  27.0.0.22                 mtu mismatch                                  Mon Jul  1 16:19:02 2019 
tor-2             uplink-2                  0.0.0.20                  27.0.0.20                 mtu mismatch                                  Mon Jul  1 16:19:37 2019
```

{{</tab>}}

{{<tab "RoCE">}}

The RoCE validation tests look for consistent RoCE and QoS configurations across nodes.


```
cumulus@switch:mgmt:~$ netq check roce
roce check result summary:

Total nodes         : 12
Checked nodes       : 12
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0
Skipped nodes       : 0


RoCE mode Test                 : passed
RoCE Classification Test       : passed
RoCE Congestion Control Test   : passed
RoCE Flow Control Test         : passed
RoCE ETS mode Test             : passed

```

{{</tab>}}

{{<tab "Sensors">}}

Hardware platforms have a number of sensors that provide environmental data about the switches. Knowing these are all within range is a good check point for maintenance.

For example, if you had a temporary HVAC failure and you have concerns that some of your nodes are beginning to overheat, you can run this validation to determine if any switches have already reached the maximum temperature threshold.

```
cumulus@switch:~$ netq check sensors
sensors check result summary:

Checked nodes       : 8
Total nodes         : 8
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Sensors     : 136
Failed Sensors      : 0

PSU sensors Test           : passed,
Fan sensors Test           : passed,
Temperature sensors Test   : passed,
```

{{</tab>}}

{{<tab "VLAN">}}

Validate the VLAN configuration and that they are operating properly:

```
cumulus@switch:~$ netq check vlan
vlan check result summary:

Checked nodes       : 12
Total nodes         : 12
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Failed Link Count   : 0
Total Link Count    : 196

Link Neighbor VLAN Consistency Test   : passed,
Clag Bond VLAN Consistency Test       : passed,
```

{{</tab>}}

{{<tab "VXLAN">}}

Validate the VXLAN configuration and that they are operating properly:

```
cumulus@switch:~$ netq check vxlan
vxlan check result summary:

Checked nodes       : 6
Total nodes         : 6
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Vlan Consistency Test   : passed,
BUM replication Test    : passed,
```

{{%notice tip%}}
This command validates both asymmetric and symmetric VXLAN configurations.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

## Scheduled Validations

When you want to see validation results on a regular basis, it is useful to configure a scheduled validation request to avoid re-creating the request each time. You can create up to 15 scheduled validations for a given NetQ system.

{{%notice note%}}

By default, a scheduled validation for each protocol and service runs every hour. You do not need to create a scheduled validation for these unless you want it to run at a different interval. You cannot remove the default validations, but they do not count as part of the 15-validation limit.

{{%/notice%}}

### Schedule a Validation

You might want to create a scheduled validation that runs more often than the default validation if you are investigating an issue with a protocol or service. You might also want to create a scheduled validation that runs less often than the default validation if you prefer a longer term performance trend.

Sometimes it is useful to run validations on more than one protocol simultaneously. This gives a view into any potential relationship between the protocols or services status. For example, you might want to compare NTP with Agent validations if NetQ Agents are losing connectivity or the data <!-- vale off -->appears to be collected<!-- vale on --> at the wrong time. It would help determine if loss of time synchronization is causing the issue. Simultaneous validations are displayed in the NetQ UI.

{{<tabs "New Scheduled Validation">}}

{{<tab "Validation Request">}}

1. Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation**, then click **Create a validation**. Choose whether the scheduled validation should run on all devices or on specific {{<link title="Validate Network Protocol and Service Operations#validate-device-groups" text="device groups.">}}

2. On the left side of the card, select the protocols or services you want to validate by clicking on their names, then click **Next**.

3. Click **Later** then choose when to start the check and how frequently to repeat the check (every 30 minutes, 1 hour, 3 hours, 6 hours, 12 hours, or 1 day).

4. Click **Schedule**.

   To see the card with the other network validations, click **View**. If you selected more than one protocol or service, a card opens for each selection. To view the card on your workbench, click **Open card**.
   
   {{<figure src="/images/netq/agent-validation-test-card.png" width="200">}}

{{</tab>}}

{{<tab "netq add validation">}}

To create a scheduled request containing checks on a single protocol or service in the NetQ CLI, run:

```
netq add validation name <text-new-validation-name> type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf | roce | addr) interval <text-time-min> [alert-on-failure]
```

This example shows the creation of a BGP validation run every 15 minutes for debugging.

```
cumulus@switch:~$ netq add validation name Bgp15m type bgp interval 15m
Successfully added Bgp15m running every 15m
```

The associated Validation Result card is accessible from the full-screen Scheduled Validation Result card.

{{</tab>}}

{{</tabs>}}

### View Scheduled Validation Results

After creating scheduled validations with either the NetQ UI or the NetQ CLI, the results appear in the Scheduled Validation Result card. When a request has completed processing, you can access the Validation Result card from the full-screen Validations card. Each protocol and service has its own validation result card, but the content is similar on each.

#### Granularity of Data Shown Based on Time Period

On the medium and large Validation Result cards, vertically stacked heat maps represent the status of the runs; one for passing runs, one for runs with warnings, and one for runs with failures. Depending on the time period of data on the card, the number of smaller time blocks indicate that the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results appear by how saturated the color is for each block. If all validations during that time period pass, then the middle block is 100% saturated (white) and the warning and failure blocks are zero % saturated (gray). As warnings and errors increase in saturation, the passing block is proportionally reduced in saturation. The example heat map for a time period of 24 hours shown here uses the most common time periods from the table showing the resulting time blocks and regions.

{{<figure src="/images/netq/sch-valid-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

#### Access and Analyze the Scheduled Validation Results

After a scheduled validation request has completed, the results are available in the corresponding Validation Result card.

To access the results:

1. In the workbench header, select {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation**, then click **Existing validations**.

2. Select the validation results you want to view, then click **View results**.

3. The medium Scheduled Validation Result card(s) for the selected items appear on your workbench.

    {{<figure src="/images/netq/validation-results-existing-medium.png" width="425">}}

To analyze the results:

1. Note the distribution of results. Are there many failures? Are they concentrated together in time? Has the protocol or service recovered after the failures?

2. Hover over the heat maps to view the status numbers and what percentage of the total results that represents for a given region. The tooltip also shows the number of devices included in the validation and the number with warnings and/or failures. This is useful when you see the failures occurring on a small set of devices, as it might point to an issue with the devices rather than the network service.

    {{<figure src="/images/netq/failed-vxlan-scheduled-validation.png" width="200">}}

3. Switch to the large Scheduled Validation card using the card size picker.

4. The card displays a chart alongside events metrics. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18">}} to expand or collapse the chart.

    {{<figure src="/images/netq/failed-vxlan-validation-large-chart.png" width="500">}}

5. You can view the configuration of the request that produced the results shown on this card, by hovering over the card and clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18">}}.

6. To view all data available for all scheduled validation results for the given protocol or service, switch to the full-screen card.

    {{<figure src="/images/netq/full-screen-vxlan-scheduled-validation.png" width="900">}}

6. In the Checks box, hover over an individual check and select **View details** for additional information:

    {{<figure src="/images/netq/bum-replication-details.png" width="900">}}

### Manage Scheduled Validations

You can edit or delete any scheduled validation that you created. Default validations cannot be edited or deleted, but can be disabled.

#### Edit a Scheduled Validation

At some point you might want to change the schedule or validation types that are specified in a scheduled validation request. This creates a new validation request and the original validation has the *(old)* label applied to the name. The old validation can no longer be edited.

{{%notice info%}}

When you update a scheduled request, the results for all future runs of the validation will be different from the results of previous runs of the validation.

{{%/notice%}}

To edit a scheduled validation:

1. Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation**, then click **Scheduled validations**.

2. Hover over the validation then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/> Edit.

    {{<figure src="/images/netq/validations-edit-4.0.0.png" width="250">}}

3. Select which checks to add or remove from the validation request, then click **Update**.

5. Change the schedule for the validation, then click **Update**.

    You can run the modified validation immediately or wait for it to run according to the schedule you specified.

#### Delete a Scheduled Validation

You can remove a user-defined scheduled validation using the NetQ UI or the NetQ CLI. Default validations cannot be deleted, but they can be disabled.

{{<tabs "Delete Scheduled Validation">}}

{{<tab "NetQ UI">}}

1. Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation**, then click **Scheduled validations**.

2. Hover over the validation you want to remove.

    {{<figure src="/images/netq/sch-valid-remove-4.0.0.png" width="700">}}

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}}, then click **Yes** to confirm.

4. To disable a default validation, select the {{<img src="/images/netq/navigation-menu-horizontal.svg" height="18" width="18">}} icon on the card for the desired validation and select **Disable validation**. Validation checks can be enabled from the same menu.

{{<figure src="/images/netq/validation-disable-check.png" alt="validation card presenting option to disable validation" width="250">}}

{{</tab>}}

{{<tab "NetQ CLI">}}

1. Determine the name of the scheduled validation you want to remove:

    ```
    netq show validation summary [name <text-validation-name>] type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf | roce | addr) [around <text-time-hr>] [json]
    ```

    This example shows all scheduled validations for BGP.

    ```
    cumulus@switch:~$ netq show validation summary type bgp
    Name            Type             Job ID       Checked Nodes              Failed Nodes             Total Nodes            Timestamp
    --------------- ---------------- ------------ -------------------------- ------------------------ ---------------------- -------------------------
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 20:38:20 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp15m          scheduled        2e891464-637 10                         0                        10                     Thu Nov 12 20:28:58 2020
                                    a-4e89-a692-
                                    3bf5f7c8fd2a
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 20:24:14 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 20:15:20 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp15m          scheduled        2e891464-637 10                         0                        10                     Thu Nov 12 20:13:57 2020
                                    a-4e89-a692-
                                    3bf5f7c8fd2a
    ...
    ```

2. To remove the validation, run:

    ```
    netq del validation <text-validation-name>
    ```

    This example removes the scheduled validation named *Bgp15m*.

    ```
    cumulus@switch:~$ netq del validation Bgp15m
    Successfully deleted validation Bgp15m
    ```

3. Repeat these steps to remove additional scheduled validations.

{{</tab>}}

{{</tabs>}}

## Validate Device Groups

Both on-demand and scheduled validations can run on specific {{<link title="Device Groups" text="device groups.">}} To create a validation for a device group rather than all devices:

1. Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation**, then click **Create a validation**. Choose **Run on group of switches:**

{{<figure src="/images/netq/new-validation-group.png" width="500">}}

2. Select which group to run the validation on:

{{<figure src="/images/netq/validation-select-group.png" width="500">}}

3. Select the protocols or services you want to validate, then click **Next**.

4. Select which individual validations to run for each service. Individual checks can be disabled by clicking {{<img src="/images/netq/check-circle-out.svg" width="14">}}.

5. Choose whether to run the validation now or schedule it for another time, then click **Run**.
