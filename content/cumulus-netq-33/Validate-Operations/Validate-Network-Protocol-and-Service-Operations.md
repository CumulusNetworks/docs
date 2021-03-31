---
title: Validate Network Protocol and Service Operations
author: NVIDIA
weight: 1020
toc: 4
---
NetQ lets you validate the operation of the network protocols and services running in your network either on demand or on a scheduled basis. NetQ provides three NetQ UI card workflows and several NetQ CLI validation commands to accomplish these checks on protocol and service operations:

- Validation Request card
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
    - View results on On-demand and Scheduled Validation Result cards

For a more general understanding of how well your network is operating, refer to the {{<link title="Validate Overall Network Health">}} topic.

## Create On-demand Validations

When you want to validate the operation of one or more network protocols and services right now, you can create and run on-demand validations using the NetQ UI or the NetQ CLI.

### Create an On-demand Validation for a Single Protocol or Service

You can create on-demand validations that contain checks for a single protocol or service if you suspect that service may have issues.

{{< tabs "TabID35" >}}

{{< tab "Validation Request" >}}

To create and run a request containing checks on a single protocol or service all within the NetQ UI:

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

2. On the right side of the card, select the protocol or service you want to validate by clicking on its name.

    When selected it becomes highlighted and **Run Now** and **Save as New** become active. Click the name again to remove it to select a different protocol or service.

    This example shows the selection of BGP.

    {{<figure src="/images/netq/valid-request-large-bgp-3.2.0.png" width="500">}}

3. Click **Run Now**.  

    The associated Validation Result card is opened on your workbench. Refer to {{<link title="Validate Network Protocol and Service Operations#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

{{< /tab >}}

{{< tab "netq check" >}}

To create and run a request containing checks on a single protocol or service all within the NetQ CLI, run the relevant `netq check` command:

```
netq check agents [hostnames <text-list-hostnames>] [include <agent-number-range-list> | exclude <agent-number-range-list>] [around <text-time>] [json]
netq check bgp [hostnames <text-list-hostnames>] [vrf <vrf>] [include <bgp-number-range-list | |exclude <bgp-number-range-list>] [around <text-time>] [json | summary]
netq check clag [hostnames <text-list-hostnames> ] [include <clag-number-range-list> | exclude <clag-number-range-list>] [around <text-time>] [json | summary]
netq check cl-version [hostnames <text-list-hostnames>] [match-version <cl-ver> | min-version <cl-ver>] [include <version-number-range-list> | exclude <version-number-range-list>] [around <text-time>] [json | summary]
netq check evpn [mac-consistency] [hostnames <text-list-hostnames>] [include <evpn-number-range-list> | exclude <evpn-number-range-list>] [around <text-time>] [json | summary]
netq check interfaces [hostnames <text-list-hostnames>] [include <interface-number-range-list> | exclude <interface-number-range-list>] [around <text-time>] [json | summary]
netq check license [hostnames <text-list-hostnames>] [include <license-number-range-list> | exclude <license-number-range-list>] [around <text-time>] [json | summary]netq check mlag [hostnames <text-list-hostnames> ] [include <mlag-number-range-list> | exclude <mlag-number-range-list>] [around <text-time>] [json | summary]
netq check mtu [hostnames <text-list-hostnames>] [unverified] [include <mtu-number-range-list> | exclude <mtu-number-range-list>] [around <text-time>] [json | summary]
netq check ntp [hostnames <text-list-hostnames>] [include <ntp-number-range-list> | exclude <ntp-number-range-list>] [around <text-time>] [json | summary]
netq check ospf [hostnames <text-list-hostnames>] [include <ospf-number-range-list> | exclude <ospf-number-range-list>] [around <text-time>] [json | summary]
netq check sensors [hostnames <text-list-hostnames>] [include <sensors-number-range-list> | exclude <sensors-number-range-list>] [around <text-time>] [json | summary]
netq check vlan [hostnames <text-list-hostnames>] [unverified] [include <vlan-number-range-list> | exclude <vlan-number-range-list>] [around <text-time>] [json | summary]
netq check vxlan [hostnames <text-list-hostnames>] [include <vxlan-number-range-list> | exclude <vxlan-number-range-list>] [around <text-time>] [json | summary]
```

All of the `netq check` commands have a summary and test results section. Some have additional summary information.

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

Refer to {{<link title="Validate Network Protocol and Service Operations#Validation Examples" text="Vaildation Examples">}} for similar examples with other protocols and services.

{{< /tab >}}

{{< tab "netq add validation" >}}

To create a request containing checks on a single protocol or service in the NetQ CLI and view results in the NetQ UI, run:

```
netq add validation type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf)
```

This example shows the creation of an on-demand BGP validation.

```
cumulus@switch:~$ netq add validation type bgp
Running job 7958faef-29e0-432f-8d1e-08a0bb270c91 type bgp
```

The associated Validation Result card is accessible from the full-screen Validation Request card. Refer to {{<link title="Validate Network Protocol and Service Operations#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

{{< /tab >}}

{{< /tabs >}}

### Create an On-demand Validation for Multiple Protocols or Services

You can create on-demand validations that contain checks for more than on protocol or service at the same time using the NetQ UI. This is handy when the protocols are strongly related with respect to a possible issue or if you only want to create one validation request.

To create and run a request containing checks for more than one protocol and/or service:

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

2. On the right side of the card, select the protocols and services you want to validate by clicking on their names.

    This example shows the selection of BGP and EVPN.

    {{<figure src="/images/netq/valid-request-bgp-evpn-222.png" width="500">}}

3. Click **Run Now** to start the validation.  

    The associated on-demand validation result cards (one per protocol and service selected) are accessible from the full-screen Validation Request card. Refer to {{<link title="Validate Network Protocol and Service Operations#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

    {{<figure src="/images/netq/valid-request-medium-bgpevpn-running-230.png" width="420">}}

### Create an On-demand Validation with Selected Tests

Using the `include <bgp-number-range-list>` and `exclude <bgp-number-range-list>` options of the `netq check` command, you can include or exclude one or more of the various checks performed during the validation.

First determine the number of the tests you want to include or exclude. Refer to {{<link title="Validation Checks#bgp-validation-tests" text="BGP Validation Tests">}} for a description of these tests. Then run the check command.

This example shows a BGP validation that includes only the session establishment and router ID tests. Note that you can obtain the same results using either of the `include` or `exclude` options and that the test that is not run is marked as *skipped*.

```
cumulus@switch:~$ netq show unit-tests bgp
   0 : Session Establishment     - check if BGP session is in established state
   1 : Address Families          - check if tx and rx address family advertisement is consistent between peers of a BGP session
   2 : Router ID                 - check for BGP router id conflict in the network

Configured global result filters:
Configured per test result filters:

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

Refer to {{<link title="Validate Network Protocol and Service Operations#Validation Examples" text="Vaildation Examples">}} for similar examples with other protocols and services.

### Run an Existing Scheduled Validation On Demand

You may find that although you have a validation scheduled to run at a later time, you would like to run it now.

To run a scheduled validation now:

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

    Optionally, change to the small or medium card using the card size picker.

2. Select the validation from the **Validation** dropdown list.  

    {{<figure src="/images/netq/valid-request-small-plus-medium-selection-230.png" width="420">}}
    {{<figure src="/images/netq/valid-request-large-valid-selection-222.png" width="500">}}

3. Click **Go** or **Run Now**.  

    The associated Validation Result card is opened on your workbench. Refer to {{<link url="#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

    {{<figure src="/images/netq/valid-request-medium-default-bgp-running-230.png" width="200">}}

## View On-demand Validation Results

After you have started an on-demand trace, the results are displayed based on how you created the validation request.

{{< tabs "TabID236" >}}

{{< tab "Validation Request card" >}}

The On-demand Validation Result card workflow enables you to view the results of on-demand validation requests. When a request has started processing, the associated medium Validation Result card is displayed on your workbench with an indicator that it is running. When multiple network protocols or services are included in a validation, a validation result card is opened for each protocol and service. After an on-demand validation request has completed, the results are available in the same Validation Result card/s.

{{<notice tip>}}
It may take a few minutes for all results to be presented if the load on the NetQ system is heavy at the time of the run.
{{</notice>}}

To view the results:

1. Locate the medium On-demand Validation Result card on your workbench for the protocol or service that was run.  

    You can identify it by the on-demand result icon, <img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/>, protocol or service name, and the date and time that it was run.  

    **Note:** You may have more than one card open for a given protocol or service, so be sure to use the date and time on the card to ensure you are viewing the correct card.  

    {{<figure src="/images/netq/od-valid-result-bgp-medium-date-highlight-230.png" width="420">}}

2. Note the total number and distribution of results for the tested devices and sessions (when appropriate). Are there many failures?

3. Hover over the charts to view the total number of warnings or failures and what percentage of the total results that represents for both devices and sessions.

4. Switch to the large on-demand Validation Result card using the card size picker.

    {{<figure src="/images/netq/od-valid-result-bgp-large-230.png" width="500">}}

5. If there are a large number of device warnings or failures, view the devices with the most issues in the table on the right. By default, this table displays the **Most Active** devices. Click on a device name to open its switch card on your workbench.

6. To view the most recent issues, select **Most Recent** from the filter above the table.

7. If there are a large number of devices or sessions with warnings or failures, the protocol or service may be experiencing issues. View     the health of the protocol or service as a whole by clicking **Open** \<*network service*\> **Card** when available.

8. To view all data available for all on-demand validation results for a given protocol, switch to the full screen card.

    {{<figure src="/images/netq/od-valid-result-bgp-fullscr-300.png" width="700">}}

9. Double-click in a given result row to open details about the validation.

    From this view you can:

<div style="padding-left: 18px;">
<ul>
<li>See a summary of the validation results by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-right-2.svg" width="14" height="14"/> in the banner under the title. Toggle the arrow to close the summary.

{{<figure src="/images/netq/od-valid-result-bgp-details-summary-fullscr.png" width="300">}}</li>
<li>See detailed results of each test run to validate the protocol or service. When errors or warnings are present, the nodes and relevant detail is provided.

{{<figure src="/images/netq/od-valid-result-bgp-tests-fullscr.png" width="700">}}</li>
<li>Export the data by clicking <strong>Export</strong>.</li>
<li>Return to the validation jobs list by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" width="14" height="14"/>.</li>
</ul>
</div>

You may find that comparing various results gives you a clue as to why certain devices are experiencing more warnings or failures. For example, more failures occurred between certain times or on a particular device.

{{< /tab >}}

{{< tab "netq check" >}}

The results of the `netq check` command are displayed in the terminal window where you ran the command. Refer to {{<link title="Validate Network Protocol and Service Operations#create-on-demand-validations" text="Create On-demand Validations">}}.

{{< /tab >}}

{{< tab "netq add validation" >}}

After you have run the netq add validation command, you are able to view the results in the NetQ UI.

1. Open the NetQ UI and log in.

2. Open the workbench where the associated On-demand Trace Result card has been placed.

To view more details for this and other traces, refer to Detailed On-demand Trace Results.

{{< /tab >}}

{{< /tabs >}}

## On-Demand CLI Validation Examples

This section provides on-demand validation examples for a variety of protocols and elements.

{{< expand "NetQ Agent Validation" >}}

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

{{< /expand >}}

{{< expand "BGP Validations" >}}

### Perform a BGP Validation

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

{{< /expand >}}

{{< expand "CLAG Validations" >}}

### Perform a CLAG Validation

The default validation runs a networkwide CLAG connectivity and configuration check on all nodes running the CLAG service. This example shows results for a fully successful validation.

```
cumulus@switch:~$ netq check clag
clag check result summary:

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

This example shows representative results for one or more failures, warnings, or errors. In particular, you can see that you have duplicate system MAC addresses.

```
cumulus@switch:~$ netq check clag
clag check result summary:

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

### Perform a CLAG Validation with Selected Tests

Using the `include <clag-number-range-list>` and `exclude <clag-number-range-list>` options, you can include or exclude one or more of the various checks performed during the validation. You can select from the following CLAG validation tests:

| Test Number | Test Name |
| :---------: | --------- |
| 0 | Peering |
| 1 | Backup IP |
| 2 | <!-- vale off -->Clag<!-- vale on --> Sysmac |
| 3 | VXLAN <!-- vale off -->Anycast IP<!-- vale on --> |
| 4 | Bridge Membership |
| 5 | Spanning Tree |
| 6 | Dual Home |
| 7 | Single Home |
| 8 | Conflicted Bonds |
| 9 | ProtoDown Bonds |
| 10 | SVI |

Refer to {{<link url="#clag-validation-tests" text="CLAG Validation Tests">}} for descriptions of these tests.

To include only the CLAG SysMAC test during a validation:

```
cumulus@switch:~$ netq check clag include 2
clag check result summary:

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
cumulus@switch:~$ netq check clag exclude 1-3
clag check result summary:

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

{{< /expand >}}

{{< expand "Cumulus Linux Version Validation" >}}

### Perform a Cumulus Linux Version Validation

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

{{< /expand >}}

{{< expand "EVPN Validations" >}}

### Perform an EVPN Validation

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

| Test Number | Test Name |
| :---------: | --------- |
| 0 | EVPN BGP Session |
| 1 | EVPN VNI Type Consistency |
| 2 | EVPN Type 2 |
| 3 | EVPN Type 3 |
| 4 | EVPN Session |
| 5 | Vlan Consistency |
| 6 | Vrf Consistency |

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

{{< /expand >}}

{{< expand "Interface Validations" >}}

### Perform an Interfaces Validation

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

{{< /expand >}}

{{< expand "License Validation" >}}

### Perform a License Validation

You can also check for any nodes that have invalid licenses without going to each node. Because switches do not operate correctly without a valid license you might want to verify that your Cumulus Linux licenses on a regular basis.

This example shows that all licenses on switches are valid.

```
cumulus@switch:~$ netq check license
license check result summary:

Checked nodes       : 12
Total nodes         : 12
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Licenses    : 8
Failed Licenses     : 0

License validity Test   : passed,
```

{{%notice tip%}}
This command checks every node, meaning every switch and host in the network. Hosts do not require a Cumulus Linux license, so the number of licenses checked might be smaller than the total number of nodes checked.
{{%/notice%}}

{{< /expand >}}

{{< expand "MTU Validation" >}}

### Perform a Link MTU Validation  

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

{{< /expand >}}

{{< expand "MLAG Validations" >}}

### Perform an MLAG Validation

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

{{< /expand >}}

{{< expand "NTP Validation" >}}

### Perform an NTP Validation

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

{{< /expand >}}

{{< expand "OSPF Validation" >}}

### Perform an OSPF Validation

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

{{< /expand >}}

{{< expand "Sensors Validation" >}}

### Perform a Sensors Validation

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

{{< /expand >}}

{{< expand "VLAN Validation" >}}

### Perform a VLAN Validation

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

{{< /expand >}}

{{< expand "VXLAN Validation" >}}

### Perform a VXLAN Validation

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

{{< /expand >}}

## Create Scheduled Validations

When you want to see validation results on a regular basis, it is useful to configure a scheduled validation request to avoid re-creating the request each time. You can create up to 15 scheduled validations for a given NetQ system.

{{%notice note%}}

By default a scheduled validation for each protocol and service is run every hour. You do not need to create a scheduled validation for these unless you want it to run at a different interval. Default validations cannot be removed, but are not counted as part of the 15-validation limit.

{{%/notice%}}

You can create scheduled validations using the NetQ UI and the NetQ CLI.

### Create a Scheduled Validation for a Single Protocol or Service

You might want to create a scheduled validation that runs more often than the default validation if you are investigating an issue with a protocol or service. You might also want to create a scheduled validation that runs less often than the default validation if you are interested in a longer term performance trend. Use the following instructions based on how you want to create the validation.

{{< tabs "TabID1258" >}}

{{< tab "Validation Request" >}}

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

2. On the right side of the card, select the protocol or service you want to validate by clicking on its name.

    When selected it becomes highlighted and **Run Now** and **Save as New** become active. Click the name again to remove it to select a different protocol or service.

    This example shows the selection of BGP.

    {{<figure src="/images/netq/valid-request-large-bgp-3.2.0.png" width="500">}}

3. Enter the schedule frequency (30 min, 1 hour, 3 hours, 6 hours, 12 hours, or 1 day) by selecting it from the **Run every** list. Default is hourly.

    {{<figure src="/images/netq/schedule-frequency-selection-222.png" width="300">}}

4. Select the time to start the validation runs, by clicking in the Starting field. Select a day and click **Next**, then select the starting time and click **OK**.  

    {{<img src="/images/netq/date-selection-222.png" width="150">}} {{<img src="/images/netq/time-selection-222.png" width="150">}}

5. Verify the selections were made correctly.

    This example shows a scheduled validation for BGP to run avery 12 hours beginning November 12th at 12:15 p.m.

      {{<figure src="/images/netq/valid-request-bgp-12hr-320.png" width="500" >}}

6. Click **Save As New**.

7. Enter a name for the validation.

<div style="padding-left: 18px;"><div class="notices note"><p>Spaces and special characters are <em>not</em> allowed in validation request names.</p></div></div>

    {{<figure src="/images/netq/sch-valid-request-specify-name-320.png" width="250">}}

8. Click **Save**.

    The validation can now be selected from the Validation listing (on the small, medium or large size card) and run immediately using **Run Now**, or you can wait for it to run the first time according to the schedule you specified. Refer to {{<link title="Validate Network Protocol and Service Operations#view-scheduled-validation-results" text="View Scheduled Validation Results">}}. Note that the number of scheduled validations is now two (15 allowed minus 13 remaining = 2).

    {{<figure src="/images/netq/sch-valid-run-now-320.png" width="500">}}

{{< /tab >}}

{{< tab "netq add validation" >}}

To create a scheduled request containing checks on a single protocol or service in the NetQ CLI and view results in the NetQ UI, run:

```
netq add validation name <text-new-validation-name> type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf) interval <text-time-min>
```

This example shows the creation of a BGP validation run every 15 minutes for debugging.

```
cumulus@switch:~$ netq add validation name Bgp15m type bgp interval 15m
Successfully added Bgp15m running every 15m
```

The associated Validation Result card is accessible from the full-screen Scheduled Validation Result card. Refer to {{<link title="Validate Network Protocol and Service Operations#view-scheduled-validation-results" text="View Scheduled Validation Results">}}.

You might want to remove this validation once you complete your analysis. Refer to {{<link title="Validate Network Protocol and Service Operations#delete-a-scheduled-validation" text="Delete a Scheduled Validation">}}.

{{< /tab >}}

{{< /tabs >}}

### Create a Scheduled Validation for Multiple Protocols or Services

Sometimes it is useful to run validations on more than one protocol simultaneously. This gives a view into any potential relationship between the protocols or services status. For example, you might want to compare NTP with Agent validations if NetQ Agents are losing connectivity or the data appears to be collected at the wrong time. It would help determine if loss of time synchronization is causing the issue.

You can create simultaneous validations using the NetQ UI. You can come close using the NetQ CLI.

{{< tabs "TabID1333" >}}

{{< tab "NetQ UI" >}}

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

2. On the right side of the card, select the protocols and services you want to include in the validation. In this example we have chosen the Agents and NTP services.

      {{<figure src="/images/netq/valid-request-agents-ntp-222.png" width="500">}}

3. Enter the schedule frequency (30 min, 1 hour, 3 hours, 6 hours, 12 hours, or 1 day) by selecting it from the **Run every** list. Default is hourly.

    {{<figure src="/images/netq/schedule-frequency-selection-222.png" width="300">}}

4. Select the time to start the validation runs, by clicking in the Starting field. Select a day and click **Next**, then select the starting time and click **OK**.  

    {{<img src="/images/netq/date-selection-222.png" width="150">}} {{<img src="/images/netq/time-selection-222.png" width="150">}}

5. Verify the selections were made correctly.

    {{<figure src="/images/netq/valid-request-agents-ntp-save-as-new-222.png" width="500">}}

6. Click **Save As New**.

7. Enter a name for the validation.

<div style="padding-left: 18px;"><div class="notices note"><p>Spaces and special characters are <em>not</em> allowed in validation request names.</p></div></div>

      {{<figure src="/images/netq/save-valid-name-example.png" width="250">}}

8. Click **Save**.

    The validation can now be selected from the Validation listing (on the small, medium or large size card) and run immediately using **Run Now**, or you can wait for it to run the first time according to the schedule you specified. Refer to {{<link title="Validate Network Protocol and Service Operations#view-scheduled-validation-results" text="View Scheduled Validation Results">}}. Note that the number of scheduled validations is now two (15 allowed minus 13 remaining = 2).

    {{<figure src="/images/netq/valid-request-select-sched-222.png" width="500">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To create simultaneous validations for multiple protocols and services with the NetQ CLI, you create each of the desired validations as quickly as possible so they start as close to the same time. To schedule multiple protocol and service validations, run:

```
netq add validation name <text-new-validation-name> type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf) interval <text-time-min>
```

This example creates scheduled validations for Agents and NTP:

```
cumulus@switch:~$ netq add validation name Agents30m type agents interval 30m
Successfully added Agents30m running every 30m
cumulus@switch:~$ netq add validation name Ntp30m type ntp interval 30m
Successfully added Ntp30m running every 30m
```

The associated Validation Result cards are accessible from the full-screen Scheduled Validation Result card. Refer to {{<link title="Validate Network Protocol and Service Operations#view-scheduled-validation-results" text="View Scheduled Validation Results">}}.

{{< /tab >}}

{{< /tabs >}}

## View Scheduled Validation Results

After creating scheduled validations with either the NetQ UI or the NetQ CLI, the results are shown in the Scheduled Validation Result card. When a request has completed processing, you can access the Validation Result card from the full-screen Validation Request card. Each protocol and service has its own validation result card, but the content is similar on each.

### Granularity of Data Shown Based on Time Period

On the medium and large Validation Result cards, the status of the runs is represented in heat maps stacked vertically; one for passing runs,  one for runs with warnings, and one for runs with failures. Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all validations during that time period pass, then the middle block is 100% saturated (white) and the warning and failure blocks are zero % saturated (gray). As warnings and errors increase in saturation, the passing block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks and regions.

{{<figure src="/images/netq/sch-valid-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### Access and Analyze the Scheduled Validation Results

Once a scheduled validation request has completed, the results are available in the corresponding Validation Result card.

To access the results:

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

2. Change to the full-screen card using the card size picker to view all scheduled validations.

    {{<figure src="/images/netq/valid-request-fullscr-300.png" width="700">}}

3. Select the validation results you want to view.

4. Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}} (Open Card). This opens the medium Scheduled Validation Result card/s for the selected items.

    {{<figure src="/images/netq/sch-valid-result-medium-222.png" width="425">}}

To analyze the results:

1. Note the distribution of results. Are there many failures? Are they concentrated together in time? Has the protocol or service recovered after the failures?

2. Hover over the heat maps to view the status numbers and what percentage of the total results that represents for a given region. The tooltip also shows the number of devices included in the validation and the number with warnings and/or failures. This is useful when you see the failures occurring on a small set of devices, as it might point to an issue with the devices rather than the network service.

    {{<figure src="/images/netq/sch-valid-result-medium-bgp-popup-222.png" width="200">}}

3. Optionally, click **Open** \<*network service*\> **Card** link to open the medium individual Network Services card. Your current card is not closed.

4. Switch to the large Scheduled Validation card using the card size picker.

5. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18">}} to expand the chart.

    {{<figure src="/images/netq/sch-valid-result-large-bgp-expand-chart-230.png" width="500">}}

6. Collapse the heat map by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18">}}.

    {{<figure src="/images/netq/sch-valid-result-large-bgp-collapse-chart-230.png" width="500">}}

7. If there are a large number of warnings or failures, view the devices with the most issues by clicking **Most Active** in the filter above the table. This might help narrow the failures down to a particular device or small set of devices that you can investigate further.

8. Select the **Most Recent** filter above the table to see the events that have occurred in the near past at the top of the list.

9. Optionally, view the health of the protocol or service as a whole by clicking **Open** \<*network service*\> **Card** (when available).

10. You can view the configuration of the request that produced the results shown on this card workflow, by hovering over the card and clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18">}}. If you want to change the configuration, click **Edit Config** to open the large Validation Request card, pre-populated with the current configuration. Follow the instructions in {{<link title="Validate Network Protocol and Service Operations#modify-a-scheduled-validation" text="Modify a Scheduled Validation">}} to make your changes.

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

## Manage Scheduled Validations

You can modify any scheduled validation that you created or remove it altogether at any time. Default validations cannot be removed, modified, or disabled.

### Modify a Scheduled Validation

At some point you might want to change the schedule or validation types that are specified in a scheduled validation request.

{{%notice info%}}

When you update a scheduled request, the results for all future runs of the validation will be different than the results of previous runs of the validation.

{{%/notice%}}

To modify a scheduled validation:

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

2. Select the validation from the **Validation** dropdown list.

    {{<figure src="/images/netq/valid-request-selection.png" width="250">}}

3. Edit the schedule or validation types.

    This example adds EVPN to the validation.

    {{<figure src="/images/netq/valid-request-edit-320.png" width="500">}}

4. Click **Update**.

5. Click **Yes** to complete the changes, or change the name of the previous version of this scheduled validation.

    {{<figure src="/images/netq/sch-valid-update-confirmation-320.png" width="300">}}

    1. Click the *change name* link.

    2. Edit the name.

        {{<figure src="/images/netq/sch-valid-edit-name-on-update-320.png" width="300">}}

    3. Click **Update**.

    4. Click **Yes** to complete the changes, or repeat these steps until you have the name you want.

    The validation can now be selected from the Validation listing (on the small, medium or large size card) and run immediately using **Run Now**, or you can wait for it to run the first time according to the schedule you specified. Refer to {{<link title="Validate Network Protocol and Service Operations#view-scheduled-validation-results" text="View Scheduled Validation Results">}}.

### Delete a Scheduled Validation

You can remove a user-defined scheduled validation at any time using the NetQ UI or the NetQ CLI. Default validations cannot be removed.

{{< tabs "TabID1538" >}}

{{< tab "NetQ UI" >}}

1. Open the Validation Request card.

    Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}}. Click **Validation**. Click on card. Click **Open Cards**.

2. Change to the full-screen card using the card size picker.

3. Select one or more validations to remove.

    {{<figure src="/images/netq/sch-valid-remove-320.png" width="700">}}

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}}.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

1. Determine the name of the scheduled validation you want to remove. Run:

    ```
    netq show validation summary [name <text-validation-name>] type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf) [around <text-time-hr>] [json]
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
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 20:13:29 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 20:12:25 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    BGP12hr         scheduled        5818f911-d9e 10                         0                        10                     Thu Nov 12 20:10:09 2020
                                    2-4927-9cc1-
                                    6972899a3422
    Bgp30m          scheduled        4c78cdf3-24a 10                         0                        10                     Thu Nov 12 20:08:46 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 20:08:20 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp15m          scheduled        2e891464-637 10                         0                        10                     Thu Nov 12 19:58:57 2020
                                    a-4e89-a692-
                                    3bf5f7c8fd2a
    Bgp15m          scheduled        2e891464-637 10                         0                        10                     Thu Nov 12 19:54:47 2020
                                    a-4e89-a692-
                                    3bf5f7c8fd2a
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 19:54:15 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 19:45:21 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Bgp30m          scheduled        4c78cdf3-24a 0                          0                        0                      Thu Nov 12 19:43:33 2020
                                    6-4ecb-a39d-
                                    0c2ec265505f
    Default validat scheduled        dec4c560-ebd 10                         0                        10                     Thu Nov 12 19:42:25 2020
    ion                              0-4e57-8203-
                                    4bd872d7ca28
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

{{< /tab >}}

{{< /tabs >}}
