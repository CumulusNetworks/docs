---
title: Validate Network Protocol and Service Operations
author: NVIDIA
weight: 1020
toc: 4
---
NetQ lets you validate the operation of the network protocols and services running in your network either on demand or on a scheduled basis. NetQ provides three NetQ UI card workflows and several NetQ CLI validation commands to accomplish these checks on protocol and service operations:

- Validate Network card
    - Create a new on-demand or scheduled validation request or run a scheduled validation on demand
    - View a preview of all scheduled validations
- On-demand Validation Result card
    - View the number of devices and sessions tested and their status
    - View job configuration
- Scheduled Validation Result card
    - View the number and status of runs, filter by failures, paths, and warnings
    - View job configuration
- `netq check` command
    - Create and run an on-demand validation
    - View summary results, individual test status, and protocol or service specific info in the terminal window
- `netq add validation` command
    - Create an on-demand or scheduled validation
    - View results inline

For a more general understanding of how well your network is operating, refer to the {{<link title="Validate Overall Network Health">}} topic.

<!-- vale off -->
## On-demand Validations
<!-- vale on -->

When you want to validate the operation of one or more network protocols and services right now, you can create and run on-demand validations using the NetQ UI or the NetQ CLI.

<!-- vale off -->
### Create an On-demand Validation
<!-- vale on -->

You can create on-demand validations that contain checks for protocols or services that you suspect may have issues.

Using the NetQ UI, you can create an on-demand validation for multiple protocols or services at the same time. This is handy when the protocols are strongly related regarding a possible issue or if you only want to create one validation request.

{{<tabs "On-demand Validation">}}

{{<tab "Validate Network">}}

To create and run a request containing checks on one or more protocols or services within the NetQ UI:

1. Open the Validate Network card.

   Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} (**Validation**), then click **Create a validation**.

2. On the left side of the card, select the protocols or services you want to validate by clicking on their names, then click **Next**.

   This example shows BGP.

   {{<figure src="/images/netq/validate-network-4.0.0.png" width="600">}}

3. Specify which workbench you want to run the check on. To run the check in the past, click **Past** and choose the time from when you want the check to start.

   {{<figure src="/images/netq/validate-network-schedule-4.0.0.png" width="400">}}

4. Click **Run** to start the check.

   The associated On-demand Validation Result card opens on your workbench. If you selected more than one protocol or service, a card opens for each selection. Refer to {{<link title="Validate Network Protocol and Service Operations#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

   {{<figure src="/images/netq/validate-network-result-4.0.0.png" width="600">}}

{{</tab>}}

{{<tab "netq check">}}

To create and run a request containing checks on a single protocol or service all within the NetQ CLI, run the relevant `netq check` command:

```
netq check agents [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <agent-number-range-list> | exclude <agent-number-range-list>] [around <text-time>] [streaming] [json]
netq check bgp [label <text-label-name> | hostnames <text-list-hostnames>] [vrf <vrf>] [check_filter_id <text-check-filter-id>] [include <bgp-number-range-list> | exclude <bgp-number-range-list>] [around <text-time>] [streaming] [json | summary]
netq check cl-version [label <text-label-name> | hostnames <text-list-hostnames>] [match-version <cl-ver> | min-version <cl-ver>] [check_filter_id <text-check-filter-id>] [include <version-number-range-list> | exclude <version-number-range-list>] [around <text-time>] [json | summary]
netq check clag [label <text-label-name> | hostnames <text-list-hostnames> ] [check_filter_id <text-check-filter-id>] [include <clag-number-range-list> | exclude <clag-number-range-list>] [around <text-time>] [streaming] [json | summary]
netq check evpn [mac-consistency] [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <evpn-number-range-list> | exclude <evpn-number-range-list>] [around <text-time>] [json | summary]
netq check interfaces [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <interface-number-range-list> | exclude <interface-number-range-list>] [around <text-time>] [streaming] [json | summary]
netq check mlag [label <text-label-name> | hostnames <text-list-hostnames> ] [check_filter_id <text-check-filter-id>] [include <mlag-number-range-list> | exclude <mlag-number-range-list>] [around <text-time>] [streaming] [json | summary]
netq check mtu [label <text-label-name> | hostnames <text-list-hostnames>] [unverified] [check_filter_id <text-check-filter-id>] [include <mtu-number-range-list> | exclude <mtu-number-range-list>] [around <text-time>] [streaming] [json | summary]
netq check ntp [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <ntp-number-range-list> | exclude <ntp-number-range-list>] [around <text-time>] [streaming] [json | summary]
netq check ospf [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <ospf-number-range-list> | exclude <ospf-number-range-list>] [around <text-time>] [json | summary]
netq check sensors [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <sensors-number-range-list> | exclude <sensors-number-range-list>] [around <text-time>] [streaming] [json | summary]
netq check vlan [label <text-label-name> | hostnames <text-list-hostnames>] [unverified] [check_filter_id <text-check-filter-id>] [include <vlan-number-range-list> | exclude <vlan-number-range-list>] [around <text-time>] [json | summary]
netq check vxlan [label <text-label-name> | hostnames <text-list-hostnames>] [check_filter_id <text-check-filter-id>] [include <vxlan-number-range-list> | exclude <vxlan-number-range-list>] [around <text-time>] [json | summary]
```

All `netq check` commands have a summary and test results section. Some have additional summary information.

This example shows a validation of the EVPN protocol.

```
cumulus@switch:~$ netq check evpn
evpn check result summary:

Total nodes         : 6
Checked nodes       : 6
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Total VNIs          : 5
Failed BGP Sessions : 0
Total Sessions      : 30

EVPN BGP Session Test            : passed
EVPN VNI Type Consistency Test   : passed
EVPN Type 2 Test                 : skipped
EVPN Type 3 Test                 : passed
EVPN Session Test                : passed
Vlan Consistency Test            : passed
Vrf Consistency Test             : passed
L3 VNI RMAC Test                 : skipped
```

{{</tab>}}

{{<tab "netq add validation">}}

To create a request containing checks on a single protocol or service in the NetQ CLI, run:

```
netq add validation type (bgp | evpn | interfaces | mlag | mtu | ntp | ospf | sensors | vlan | vxlan) [alert-on-failure]
```

This example shows the creation of an on-demand BGP validation.

```
cumulus@switch:~$ netq add validation type bgp
Running job 7958faef-29e0-432f-8d1e-08a0bb270c91 type bgp
```

The associated Validation Result card is accessible from the full-screen Validate Network card. Refer to {{<link title="Validate Network Protocol and Service Operations#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

{{</tab>}}

{{</tabs>}}

<!-- vale off -->
### Create an On-demand Validation with Selected Tests
<!-- vale on -->

You can include or exclude one or more of the various checks performed during a validation. Refer to {{<link title="Validation Checks">}} for a description of the tests for each protocol or service.

{{<tabs "Selected Tests">}}

{{<tab "NetQ UI">}}

To create and run a request containing checks on one or more protocols or services within the NetQ UI:

1. Open the Validate Network card.

   Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} (**Validation**), then click **Create a validation**.

2. On the left side of the card, select the protocols or services you want to validate by clicking on their names. For each protocol or service, select or deselect the tests you want to include or exclude.

   This example shows BGP.

   {{<figure src="/images/netq/validate-network-select-bgp-check-4.0.0.png" width="700">}}

   After you've made your selection, click **Next**.

3. Specify which workbench you want to run the check on. To run the check in the past, click **Past** and choose the time from when you want the check to start.

   {{<figure src="/images/netq/validate-network-schedule-4.0.0.png" width="400">}}

4. Click **Run** to start the check.

   The associated On-demand Validation Result card opens on your workbench. If you selected more than one protocol or service, a card opens for each selection. Refer to {{<link title="Validate Network Protocol and Service Operations#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

   {{<figure src="/images/netq/on-demand-validation-result-select-bgp-4.0.0.png" width="600">}}

{{</tab>}}

{{<tab "netq check">}}

Using the `include <bgp-number-range-list>` and `exclude <bgp-number-range-list>` options of the `netq check` command, you can include or exclude one or more of the various checks performed during the validation.

First determine the number of the tests you want to include or exclude. Refer to {{<link title="Validation Checks">}} for a description of these tests and to get the test numbers for the tests to include or exclude. You can also get the test numbers and descriptions when you run the `netq show unit-tests` command.

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

{{</tabs>}}

### Run an Existing Scheduled Validation On Demand

You may find that although you have a validation scheduled to run at a later time, you would like to run it now.

To run a scheduled validation now:

1. Open the Validate Network card.

   Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} (**Validation**), then click **Run an existing validation**.

2. Select one or more validations you want to run by clicking their names, then click **View**.

   {{<figure src="/images/netq/validate-network-select-existing-4.0.0.png" width="420">}}

3. The associated Validation Result cards open on your workbench. Refer to {{<link url="#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

    {{<figure src="/images/netq/valid-request-medium-default-bgp-evpn-running-4.0.0.png" width="400">}}

### View On-demand Validation Results

After you have started an on-demand validation, the results are displayed based on how you created the validation request.

{{<tabs "View Validations">}}

{{<tab "Validate Network card">}}

The On-demand Validation Result card workflow enables you to view the results of on-demand validation requests. When a request has started processing, the associated large Validation Result card is displayed on your workbench with an indicator that it is running. When multiple network protocols or services are included in a validation, a validation result card is opened for each protocol and service. After an on-demand validation request has completed, the results are available in the same Validation Result cards.

{{<notice tip>}}
It may take a few minutes for results to appear if the load on the NetQ system is heavy at the time of the run.
{{</notice>}}

To view the results:

1. Locate the large On-demand Validation Result card on your workbench for the protocol or service check that was run.  

    You can identify it by the on-demand result icon, <img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/>, protocol or service name, and the date and time that it was run.  

   {{<figure src="/images/netq/validate-network-result-4.0.0.png" width="600">}}

   {{%notice note%}}

You may have more than one card open for a given protocol or service, so be sure to use the date and time on the card to ensure you are viewing the correct card.  

   {{%/notice%}}

2. Note the total number and distribution of results for the tested devices and sessions (when appropriate). Are there many failures?

3. Hover over the charts to view the total number of warnings or failures and what percentage of the total results that represents for both devices and sessions.

4. To get more information about the errors reported, hover over the right side of the test and click **More Details**.

   {{<figure src="/images/netq/validation-result-error-details-bgp-4.0.0.png" width="700">}}

5. To view all data available for all on-demand validation results for a given protocol, click **Show All Results** to switch to the full screen card.    

You may find that comparing various results gives you a clue as to why certain devices are experiencing more warnings or failures. For example, more failures occurred between certain times or on a particular device.

{{</tab>}}

{{<tab "netq check">}}

The results of the `netq check` command are displayed in the terminal window where you ran the command. See {{<link title="Validate Network Protocol and Service Operations#on-demand-cli-validation-examples" text="On-demand CLI Validation Examples">}} below.

{{</tab>}}

{{<tab "netq add validation">}}

The results of the `netq add validation` command are displayed in the terminal window where you ran the command. See {{<link title="Validate Network Protocol and Service Operations#on-demand-cli-validation-examples" text="On-demand CLI Validation Examples">}} below.

{{</tab>}}


{{</tabs>}}

#### On-Demand CLI Validation Examples

This section provides on-demand validation examples for a variety of protocols and elements.

{{<tabs "CLI Examples">}}

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

Using the `vrf <vrf>` option of the `netq check bgp` command, you can validate the BGP service where communication is occurring through a particular virtual route. In this example, the VRF of interest is named *vrf1*.

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

Refer to {{<link url="#bgp-validation-tests" text="BGP Validation Tests">}} for a description of these tests.

To include only the session establishment and router ID tests during a validation, run either of these commands:

```
cumulus@switch:~$ netq check bgp include 0,2

cumulus@switch:~$ netq check bgp exclude 1
```

Either way, a successful validation output would be similar to the following:

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

### Perform an EVPN Validation for a Time in the Past

Using the `around` option, you can view the state of the EVPN service at a time in the past. Be sure to include the UOM.

```
cumulus@switch:~$ netq check evpn around 4d
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

Refer to {{<link url="#evpn-validation-tests" text="EVPN Validation Tests">}} for descriptions of these tests.

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

### Perform an Interfaces Validation for a Time in the Past

Using the `around` option, you can view the state of the interfaces at a time in the past. Be sure to include the UOM.

```
cumulus@switch:~$ netq check interfaces around 6h
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

Refer to {{<link url="#interface-validation-tests" text="Interface Validation Tests">}} for descriptions of these tests.

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

Refer to {{<link url="#mlag-validation-tests" text="MLAG Validation Tests">}} for descriptions of these tests.

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

The default validation checks for synchronization of the NTP server with all nodes in the network. It is always important to have your devices in time synchronization to ensure configuration and management events can be tracked and correlations can be made between events.

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

The default validation runs a networkwide OSPF connectivity and configuration check on all nodes running the OSPF service. This example shows results several errors in the Timers and Interface MTU tests.

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

{{<tab "Sensors">}}

Hardware platforms have a number sensors to provide environmental data about the switches. Knowing these are all within range is a good check point for maintenance.

For example, if you had a temporary HVAC failure and you are concerned that some of your nodes are beginning to overheat, you can run this validation to determine if any switches have already reached the maximum temperature threshold.

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

Validate that VLANS are configured and operating properly:

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

Validate that VXLANs are configured and operating properly:

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
Both asymmetric and symmetric VXLAN configurations are validated with this command.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

## Scheduled Validations

When you want to see validation results on a regular basis, it is useful to configure a scheduled validation request to avoid re-creating the request each time. You can create up to 15 scheduled validations for a given NetQ system.

{{%notice note%}}

By default, a scheduled validation for each protocol and service is run every hour. You do not need to create a scheduled validation for these unless you want it to run at a different interval. Default validations cannot be removed, but are not counted as part of the 15-validation limit.

{{%/notice%}}

### Create a Scheduled Validation

You can create scheduled validations using the NetQ UI and the NetQ CLI.

You might want to create a scheduled validation that runs more often than the default validation if you are investigating an issue with a protocol or service. You might also want to create a scheduled validation that runs less often than the default validation if you are interested in a longer term performance trend. Use the following instructions based on how you want to create the validation.

Sometimes it is useful to run validations on more than one protocol simultaneously. This gives a view into any potential relationship between the protocols or services status. For example, you might want to compare NTP with Agent validations if NetQ Agents are losing connectivity or the data appears to be collected at the wrong time. It would help determine if loss of time synchronization is causing the issue. You create simultaneous validations using the NetQ UI only.

{{<tabs "New Scheduled Validation">}}

{{<tab "Validation Request">}}

1. Open the Validate Network card.

   Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} (**Validation**), then click **Create a validation**.

2. On the left side of the card, select the protocols or services you want to validate by clicking on their names, then click **Next**.

3. Select whether you want to run the check now or later, and on which workbench.

   To run the check now, select how frequently it repeats and on which workbench to run the check.

   To run the check later, click **Later** then choose when to start the check, how frequently to repeat the check (every 30 minutes, 1 hour, 3 hours, 6 hours, 12 hours, or 1 day), and on which workbench to run the check.

   {{<figure src="/images/netq/validate-network-schedule-4.0.0.png" width="400">}}

4. Click **Schedule** to schedule the check.

   To see the card with the other network validations, click **View**. If you selected more than one protocol or service, a card opens for each selection.
   
   {{<figure src="/images/netq/validate-network-view-bgp-check-4.0.0.png" width="200">}}

   To view the card on your workbench, click **Open card**. If you selected more than one protocol or service, a card opens for each selection.

   {{<figure src="/images/netq/scheduled-validation-result-bgp-4.0.0.png" width="200">}}

{{</tab>}}

{{<tab "netq add validation">}}

To create a scheduled request containing checks on a single protocol or service in the NetQ CLI, run:

```
netq add validation name <text-new-validation-name> type (agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | sensors | vlan | vxlan) interval <text-time-min>
```

This example shows the creation of a BGP validation run every 15 minutes for debugging.

```
cumulus@switch:~$ netq add validation name Bgp15m type bgp interval 15m
Successfully added Bgp15m running every 15m
```

The associated Validation Result card is accessible from the full-screen Scheduled Validation Result card. Refer to {{<link title="Validate Network Protocol and Service Operations#view-scheduled-validation-results" text="View Scheduled Validation Results">}}.

You might want to remove this validation after you complete your analysis. Refer to {{<link title="Validate Network Protocol and Service Operations#delete-a-scheduled-validation" text="Delete a Scheduled Validation">}}.

{{</tab>}}

{{</tabs>}}

### View Scheduled Validation Results

After creating scheduled validations with either the NetQ UI or the NetQ CLI, the results are shown in the Scheduled Validation Result card. When a request has completed processing, you can access the Validation Result card from the full-screen Validations card. Each protocol and service has its own validation result card, but the content is similar on each.

#### Granularity of Data Shown Based on Time Period

On the medium and large Validation Result cards, the status of the runs is represented in heat maps stacked vertically; one for passing runs, one for runs with warnings, and one for runs with failures. Depending on the time period of data on the card, the number of smaller time blocks indicate that the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all validations during that time period pass, then the middle block is 100% saturated (white) and the warning and failure blocks are zero % saturated (gray). As warnings and errors increase in saturation, the passing block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks and regions.

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

Once a scheduled validation request has completed, the results are available in the corresponding Validation Result card.

To access the results:

1. Open the Validate Network card.

   Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} (**Validation**), then click **Open an existing validation**.

2. Select the validation results you want to view, then click **View results**.

    {{<figure src="/images/netq/validations-picker-4.0.0.png" width="500">}}

3. The medium Scheduled Validation Result card(s) for the selected items open.

    {{<figure src="/images/netq/sch-valid-result-medium-222.png" width="425">}}

To analyze the results:

1. Note the distribution of results. Are there many failures? Are they concentrated together in time? Has the protocol or service recovered after the failures?

2. Hover over the heat maps to view the status numbers and what percentage of the total results that represents for a given region. The tooltip also shows the number of devices included in the validation and the number with warnings and/or failures. This is useful when you see the failures occurring on a small set of devices, as it might point to an issue with the devices rather than the network service.

    {{<figure src="/images/netq/sch-valid-result-medium-bgp-popup-222.png" width="200">}}

3. Optionally, click **Open** \<*network service*\> **Card** link to open the medium individual Network Services card. Your current card does not close.

4. Switch to the large Scheduled Validation card using the card size picker.

5. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18">}} to expand the chart.

    {{<figure src="/images/netq/sch-valid-result-large-bgp-expand-chart-230.png" width="500">}}

6. Collapse the heat map by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18">}}.

    {{<figure src="/images/netq/sch-valid-result-large-bgp-collapse-chart-230.png" width="500">}}

7. If there are a large number of warnings or failures, view the devices with the most issues by clicking **Most Active** in the filter above the table. This might help narrow the failures down to a particular device or small set of devices that you can investigate further.

8. Select the **Most Recent** filter above the table to see the events that have occurred in the near past at the top of the list.

9. Optionally, view the health of the protocol or service as a whole by clicking **Open** \<*network service*\> **Card** (when available).

10. You can view the configuration of the request that produced the results shown on this card workflow, by hovering over the card and clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18">}}. If you want to change the configuration, click **Edit Config** to open the large Validate Network card, pre-populated with the current configuration. Follow the instructions in {{<link title="Validate Network Protocol and Service Operations#modify-a-scheduled-validation" text="Modify a Scheduled Validation">}} to make your changes.

11. To view all data available for all scheduled validation results for the given protocol or service, click **Show All Results** or switch to the full screen card.

    {{<figure src="/images/netq/sch-valid-result-fullscr-bgp-241.png" width="700">}}

12. Look for changes and patterns in the results. Scroll to the right. Are there more failed sessions or nodes during one or more validations?

13. Double-click in a given result row to open details about the validation.

    From this view you can:
    - See a summary of the validation results by clicking {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-right-2.svg" width="14" height="14">}} in the banner under the title. Toggle the arrow to close the summary.

        {{<figure src="/images/netq/od-valid-result-bgp-details-summary-fullscr.png" width="300">}}

    - See detailed results of each test run to validate the protocol or service. When errors or warnings are present, the nodes and relevant detail is provided.

        {{<figure src="/images/netq/od-valid-result-bgp-tests-fullscr.png" width="700">}}

    - Export the data by clicking **Export**.

    - Return to the validation jobs list by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" width="14" height="14">}}.

    You may find that comparing various results gives you a clue as to why certain devices are experiencing more warnings or failures. For  example, more failures occurred between certain times or on a particular device.

### Manage Scheduled Validations

You can modify any scheduled validation that you created or remove it altogether at any time. Default validations cannot be removed, modified, or disabled.

#### Modify a Scheduled Validation

At some point you might want to change the schedule or validation types that are specified in a scheduled validation request. This creates a new validation request and the original validation has the *(old)* label applied to the name. The old validation can no longer be edited.

{{%notice info%}}

When you update a scheduled request, the results for all future runs of the validation will be different than the results of previous runs of the validation.

{{%/notice%}}

To modify a scheduled validation:

1. Open the Validate Network card.

    Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} (**Validation**), then click **Show all scheduled validations**.

2. Hover over the validation then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/> to edit it.

    {{<figure src="/images/netq/validations-edit-4.0.0.png" width="250">}}

3. Select which checks to add or remove from the validation request.

    {{<figure src="/images/netq/validations-edit-select-4.0.0.png" width="700">}}

4. Click **Update**.

5. Change the schedule for the validation, then click **Update**.

    {{<figure src="/images/netq/validations-edit-schedule-4.0.0.png" width="500">}}

    The validation can now be selected from the Validation list (on the small, medium or large size card) and run immediately using **Open an existing validation**, or you can wait for it to run the first time according to the schedule you specified. Refer to {{<link title="Validate Network Protocol and Service Operations#view-scheduled-validation-results" text="View Scheduled Validation Results">}}.

#### Delete a Scheduled Validation

You can remove a user-defined scheduled validation at any time using the NetQ UI or the NetQ CLI. Default validations cannot be removed.

{{<tabs "Delete Scheduled Validation">}}

{{<tab "NetQ UI">}}

1. Open the Validate Network card.

    Click {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} (**Validation**), then click **Show all scheduled validations**.

2. Hover over the validation you want to remove.

    {{<figure src="/images/netq/sch-valid-remove-4.0.0.png" width="700">}}

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}}, then click **Yes** to confirm.

{{</tab>}}

{{<tab "NetQ CLI">}}

1. Determine the name of the scheduled validation you want to remove. Run:

    ```
    netq show validation summary [name <text-validation-name>] type (agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | sensors | vlan | vxlan) [around <text-time-hr>] [json]
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

2. Remove the validation. Run:

    ```
    netq del validation <text-validation-name>
    ```

    This example removes the scheduled validation named *Bgp15m*.

    ```
    cumulus@switch:~$ netq del validation Bgp15m
    Successfully deleted validation Bgp15m
    ```

3. Repeat these steps for additional scheduled validations you want to remove.

{{</tab>}}

{{</tabs>}}
