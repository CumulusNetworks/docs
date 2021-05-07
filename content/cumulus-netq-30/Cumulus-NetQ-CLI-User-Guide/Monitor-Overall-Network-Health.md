---
title: Monitor Overall Network Health
author: Cumulus Networks
weight: 500
toc: 3
---
NetQ provides the information you need to monitor the health of your network fabric, devices, and interfaces. You are able to easily validate the operation and view the configuration across the entire network from switches to hosts to containers. For example, you can monitor the operation of routing protocols and virtual network configurations, the status of NetQ Agents and hardware components, and the operation and efficiency of interfaces. When issues are present, NetQ makes it easy to identify and resolve them. You can also see when changes have occurred to the network, devices, and interfaces by viewing their operation, configuration, and status at an earlier point in time.

## Validate Network Health

NetQ `check` commands validate the various elements of your network fabric, looking for inconsistencies in configuration across your fabric, connectivity faults, missing configuration, and so forth, and then and display the results for your assessment. They can be run from any node in the network.

### Validate the Network Fabric

You can validate the following network fabric elements:

```
cumulus@switch:~$ netq check
    agents      :  Netq agent
    bgp         :  BGP info
    cl-version  :  Cumulus Linux version
    clag        :  Cumulus Multi-chassis LAG
    evpn        :  EVPN
    interfaces  :  network interface port
    license     :  License information
    mlag        :  Multi-chassis LAG (alias of clag)
    mtu         :  Link MTU
    ntp         :  NTP
    ospf        :  OSPF info
    sensors     :  Temperature/Fan/PSU sensors
    vlan        :  VLAN
    vxlan       :  VXLAN data path
```

## Validation Commands

The validation commands have been changed in this release:

- You can view more detail about the validation tests that are run with each command
- You can filter these tests to run only those tests of interest

{{%notice info%}}
If you are running scripts based on the older version of the `netq check` commands and want to stay with the old output, edit the *netq.yml* file to include `old-check: true` in the `netq-cli` section of the file. For example:

```
netq-cli:
  port: 32708
  server: 127.0.0.1
  old-check: true
```
  
Then run `netq config restart cli` to apply the change.

If you update your scripts to work with the new version of the commands, simply change the `old-check` value to *false* or remove it. Then restart the CLI.
{{%/notice%}}

The new syntax of the `netq check` commands is:

```
netq check agents [hostnames <text-list-hostnames>] [include <agent-number-range-list> | exclude <agent-number-range-list>] [around <text-time>] [json]
netq check bgp [hostnames <text-list-hostnames>] [vrf <vrf>] [include <bgp-number-range-list> | exclude <bgp-number-range-list>] [around <text-time>] [json | summary]
netq check mlag [hostnames <text-list-hostnames> ] [include <mlag-number-range-list> | exclude <mlag-number-range-list>] [around <text-time>] [json | summary]
netq check evpn [mac-consistency] [hostnames <text-list-hostnames>] [include <evpn-number-range-list> | exclude <evpn-number-range-list>] [around <text-time>] [json | summary]
netq check interfaces [hostnames <text-list-hostnames>] [include <interface-number-range-list> | exclude <interface-number-range-list>] [around <text-time>] [json | summary]
netq check license [hostnames <text-list-hostnames>] [include <license-number-range-list> | exclude <license-number-range-list>] [around <text-time>] [json | summary]
netq check mtu [hostnames <text-list-hostnames>] [unverified] [include <mtu-number-range-list> | exclude <mtu-number-range-list>] [around <text-time>] [json | summary]
netq check ntp [hostnames <text-list-hostnames>] [include <ntp-number-range-list> | exclude <ntp-number-range-list>] [around <text-time>] [json | summary]
netq check ospf [hostnames <text-list-hostnames>] [include <ospf-number-range-list> | exclude <ospf-number-range-list>] [around <text-time>] [json | summary]
netq check sensors [hostnames <text-list-hostnames>] [include <sensors-number-range-list> | exclude <sensors-number-range-list>] [around <text-time>] [json | summary]
netq check vlan [hostnames <text-list-hostnames>] [unverified] [include <vlan-number-range-list> | exclude <vlan-number-range-list>] [around <text-time>] [json | summary]
netq check vxlan [hostnames <text-list-hostnames>] [include <vxlan-number-range-list> | exclude <vxlan-number-range-list>] [around <text-time>] [json | summary]
```

Each of the check commands provides a starting point for troubleshooting configuration and connectivity issues within your network in real time.

{{%notice tip%}}
Use `netq check mlag` in place of `netq check clag` from NetQ 2.4 onward. `netq check clag` remains available for automation scripts, but you should begin migrating to `netq check mlag` to maintain compatibility with future NetQ releases.
{{%/notice%}}

You can view only the summary of the validation results by running the `netq check` commands with `summary` option; for example, `netq check agents summary` or `netq check evpn summary`. This summary displays such data as the total number of nodes checked, how many failed a test, total number of sessions checked, how many of these that failed, and so forth.

You can view more information about the individual tests that are run as part of the validation, including individual tests for agents.

You can run validations for a time in the past and output the results in JSON format if desired. The `around` option enables users to view the network state at an earlier time. The `around` option value requires an integer *plus* a unit of measure (UOM), with no space between them. The following are valid UOMs:

| UOM | Command Value | Example|
| --- | ------------- | -------|
| day(s) | <#>d | 3d |
| hour(s) | <#>h | 6h |
| minute(s) | <#>m | 30m |
| second(s) | <#>s | 20s |

{{%notice tip%}}
If you want to go back in time by months or years, use the equivalent number of days.
{{%/notice%}}

You can include or exclude one or more of the various tests performed during the validation. Each test is assigned a number, which is used to identify which tests to run. By default, all tests are run. The value of `<protocol-number-range-list>` is a number list separated by commas, or a range using a dash, or a combination of these. Do not use spaces after commas. For example:

- include 1,3,5
- include 1-5
- include 1,3-5
- exclude 6,7
- exclude 6-7
- exclude 3,4-7,9

The output indicates whether a given test passed, failed, or was skipped.

{{%notice tip%}}
Output from the `netq check` commands are color-coded; green for successful results and red for failures, warnings, and errors. Use the `netq config add color` command to enable the use of color.
{{%/notice%}}

### What the NetQ Validation System Checks

Each of the `netq check` commands perform a set of validation tests appropriate to the protocol or element being validated.

To view the list of tests run for a given protocol or service, use either `netq show unit-tests <protocol/service>` or perform a tab completion on `netq check <protocol/service> [include|exclude]`.

This section describes these tests.

### NetQ Agent Validation Tests

The `netq check agents` command looks for an agent status of Rotten for each node in the network. A *Fresh* status indicates the Agent is running as expected. The Agent sends a heartbeat every 30 seconds, and if three consecutive heartbeats are missed, its status changes to *Rotten*. This check only runs one test:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Agent Health | Checks for nodes that have failed or lost communication |

### BGP Validation Tests

The `netq check bgp` command runs the following tests to establish session sanity:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Session Establishment | Checks that BGP sessions are in an established state |
| 1 | Address Families | Checks if transmit and receive address family advertisement is consistent between peers of a BGP session |
| 2 | Router ID | Checks for BGP router ID conflict in the network |

### CLAG Validation Tests

The `netq check clag` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Peering | Checks if: <ul><li>CLAG peerlink is up</li><li>CLAG peerlink bond slaves are down (not in full capacity and redundancy)</li><li>Peering is established between two nodes in a CLAG pair</li></ul> |
| 1 | Backup IP | Checks if: <ul><li>CLAG backup IP configuration is missing on a CLAG node</li><li>CLAG backup IP is correctly pointing to the CLAG peer and its connectivity is available</li></ul> |
| 2 | Clag Sysmac | Checks if: <ul><li>CLAG Sysmac is consistently configured on both nodes in a CLAG pair</li><li>there is any duplication of a CLAG sysmac within a bridge domain </li></ul> |
| 3 | VXLAN Anycast IP | Checks if the VXLAN anycast IP address is consistently configured on both nodes in a CLAG pair |
| 4 | Bridge Membership | Checks if the CLAG peerlink is part of bridge |
| 5 | Spanning Tree | Checks if: <ul><li>STP is enabled and running on the CLAG nodes</li><li>CLAG peerlink role is correct from STP perspective</li><li>the bridge ID is consistent between two nodes of a CLAG pair</li><li>the VNI in the bridge has BPDU guard and BPDU filter enabled</li></ul> |
| 6 | Dual Home | Checks for: <ul><li>CLAG bonds that are not in dually connected state</li><li>dually connected bonds have consistent VLAN and MTU configuration on both sides</li><li>STP has consistent view of bonds' dual connectedness</li></ul> |
| 7 | Single Home | Checks for: <ul><li>singly connected bonds</li><li>STP has consistent view of bond's single connectedness</li></ul> |
| 8 | Conflicted Bonds | Checks for bonds in CLAG conflicted state and shows the reason |
| 9 | ProtoDown Bonds | Checks for bonds in protodown state and shows the reason |
| 10 | SVI | Checks if: <ul><li>an SVI is configured on both sides of a CLAG pair</li><li>SVI on both sides have consistent MTU setting</li></ul> |

### Cumulus Linux Version Tests

The `netq check cl-version` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Cumulus Linux Image Version | Checks the following: <ul><li>no version specified, checks that all switches in the network have consistent version</li><li><em>match-version</em> specified, checks that a switch's OS version is equal to the specified version</li><li><em>min-version</em> specified, checks that a switch's OS version is equal to or greater than the specified version</li></ul> |

### EVPN Validation Tests

The `netq check evpn` command runs the following tests to establish session sanity:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | EVPN BGP Session | Checks if: <ul><li>BGP EVPN sessions are established</li><li>the EVPN address family advertisement is consistent</li></ul> |
| 1 | EVPN VNI Type Consistency | Because a VNI can be of type L2 or L3, checks that for a given VNI, its type is consistent across the network |
| 2 | EVPN Type 2 | Checks for consistency of IP-MAC binding and the location of a given IP-MAC across all VTEPs |
| 3 | EVPN Type 3 | Checks for consistency of replication group across all VTEPs |
| 4 | EVPN Session | For each EVPN session, checks if: <ul><li><em>adv_all_vni</em> is enabled</li><li>FDB learning is disabled on tunnel interface</li></ul> |
| 5 | Vlan Consistency | Checks for consistency of VLAN to VNI mapping across the network |
| 6 | Vrf Consistency | Checks for consistency of VRF to L3 VNI mapping across the network |

### Interface Validation Tests

The `netq check interfaces` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Admin State | Checks for consistency of administrative state on two sides of a physical interface |
| 1 | Oper State | Checks for consistency of operational state on two sides of a physical interface |
| 2 | Speed | Checks for consistency of the speed setting on two sides of a physical interface |
| 3 | Autoneg | Checks for consistency of the auto-negotiation setting on two sides of a physical interface |

### License Validation Tests

The `netq check license` command runs the following test:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | License Validity | Checks for validity of license on all switches |

### Link MTU Validation Tests

The `netq check mtu` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Link MTU Consistency | Checks for consistency of MTU setting on two sides of a physical interface |
| 1 | VLAN interface | Checks if the MTU of an SVI is no smaller than the parent interface, substracting the VLAN tag size |
| 2 | Bridge interface | Checks if the MTU on a bridge is not arbitrarily smaller than the smallest MTU among its members |

### MLAG Validation Tests

The `netq check mlag` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Peering | Checks if: <ul><li>MLAG peerlink is up</li><li>MLAG peerlink bond slaves are down (not in full capacity and redundancy)</li><li>Peering is established between two nodes in a MLAG pair</li></ul> |
| 1 | Backup IP | Checks if: <ul><li>MLAG backup IP configuration is missing on a MLAG node</li><li>MLAG backup IP is correctly pointing to the MLAG peer and its connectivity is available</li></ul> |
| 2 | Clag Sysmac | Checks if: <ul><li>MLAG Sysmac is consistently configured on both nodes in a MLAG pair</li><li>there is any duplication of a MLAG sysmac within a bridge domain </li></ul> |
| 3 | VXLAN Anycast IP | Checks if the VXLAN anycast IP address is consistently configured on both nodes in an MLAG pair |
| 4 | Bridge Membership | Checks if the MLAG peerlink is part of bridge |
| 5 | Spanning Tree | Checks if: <ul><li>STP is enabled and running on the MLAG nodes</li><li>MLAG peerlink role is correct from STP perspective</li><li>the bridge ID is consistent between two nodes of a MLAG pair</li><li>the VNI in the bridge has BPDU guard and BPDU filter enabled</li></ul> |
| 6 | Dual Home | Checks for: <ul><li>MLAG bonds that are not in dually connected state</li><li>dually connected bonds have consistent VLAN and MTU configuration on both sides</li><li>STP has consistent view of bonds' dual connectedness</li></ul> |
| 7 | Single Home | Checks for: <ul><li>singly connected bonds</li><li>STP has consistent view of bond's single connectedness</li></ul> |
| 8 | Conflicted Bonds | Checks for bonds in MLAG conflicted state and shows the reason |
| 9 | ProtoDown Bonds | Checks for bonds in protodown state and shows the reason |
| 10 | SVI | Checks if: <ul><li>an SVI is configured on both sides of a MLAG pair</li><li>SVI on both sides have consistent MTU setting</li></ul> |

### NTP Validation Tests

The `netq check ntp` command runs the following test:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | NTP Sync | Checks if the NTP service is running and in sync state |

### OSPF Validation Tests

The `netq check ospf` command runs the following tests to establish session sanity:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Router ID | Checks for OSPF router ID conflicts in the network |
| 1 | Adjacency | Checks or OSPF adjacencies in a down or unknown state |
| 2 | Timers | Checks for consistency of OSPF timer values in an OSPF adjacency |
| 3 | Network Type | Checks for consistency of network type configuration in an OSPF adjacency |
| 4 | Area ID | Checks for consistency of area ID configuration in an OSPF adjacency |
| 5 | Interface MTU | Checks for MTU consistency in an OSPF adjacency |
| 6 | Service Status | Checks for OSPF service health in an OSPF adjacency |

### Sensor Validation Tests

The `netq check sensors` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | PSU sensors | Checks for power supply unit sensors that are not in ok state |
| 1 | Fan sensors | Checks for fan sensors that are not in ok state |
| 2 | Temperature sensors | Checks for temperature sensors that are not in ok state |

### VLAN Validation Tests

The `netq check vlan` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Link Neighbor VLAN Consistency | Checks for consistency of VLAN configuration on two sides of a port or a bond |
| 1 | CLAG Bond VLAN Consistency | Checks for consistent VLAN membership of a CLAG bond on each side of the CLAG pair |

### VXLAN Validation Tests

The `netq check vxlan` command runs the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | VLAN Consistency | Checks for consistent VLAN to VXLAN mapping across all VTEPs |
| 1 | BUM replication | Checks for consistent replication group membership across all VTEPs |

## Validation Examples

This section provides validation examples for a variety of protocols and elements.

### Perform a NetQ Agent Validation

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

### Perform a BGP Validation

The default validation runs a network-wide BGP connectivity and configuration check on all nodes running the BGP service:

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

### Perform a CLAG Validation

The default validation runs a network-wide CLAG connectivity and configuration check on all nodes running the CLAG service. This example shows results for a fully successful validation.

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
| 2 | Clag Sysmac |
| 3 | VXLAN Anycast IP |
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

### Perform an EVPN Validation

The default validation runs a network-wide EVPN connectivity and configuration check on all nodes running the EVPN service. This example shows results for a fully successful validation.

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

### Perform an Interfaces Validation

The default validation runs a network-wide connectivity and configuration check on all interfaces. This example shows results for a fully successful validation.

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

### Perform an MLAG Validation

The default validation runs a network-wide MLAG connectivity and configuration check on all nodes running the MLAG service. This example shows results for a fully successful validation.

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
| 2 | Clag Sysmac |
| 3 | VXLAN Anycast IP |
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

### Perform an OSPF Validation

The default validation runs a network-wide OSPF connectivity and configuration check on all nodes running the OSPF service. This example shows results several errors in the Timers and Interface MTU tests.

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

## Validation Check Result Filtering

You can create filters to suppress false alarms or uninteresting errors and warnings that can be a nuisance in CI workflows. For example, certain configurations permit a singly-connected CLAG bond and the standard error that is generated is not useful.

{{%notice note%}}
Filtered errors and warnings related to validation checks do NOT generate notifications and are not counted in the alarm and info event totals. They are counted as part of suppressed notifications instead.
{{%/notice%}}

The filters are defined in the  `check-filter.yml` file in the `/etc/netq/` directory. You can create a rule for individual check commands or you can create a global rule that applies to all tests run by the check command. Additionally, you can create a rule specific to a particular test run by the check command.

Each rule must contain at least one `match` criteria and an `action` response. The only action currently available is *filter*. The match can be comprised of multiple criteria, one per line, creating a logical AND. Matches can be made against any column in the validation check output. The match criteria values *must match* the case and spacing of the column names in the corresponding `netq check` output and are parsed as regular expressions.

This example shows a global rule for the BGP checks that indicates any events generated by the *DataVrf* virtual route forwarding interface coming from *swp3* or *swp7.* are to be suppressed. It also shows a test-specific rule to filter all Address Families events from devices with hostnames starting with *exit-1* or *firewall*.

```
bgp:
    global:
        - rule:
            match:
                VRF: DataVrf
                Peer Name: (swp3|swp7.)
            action:
                filter
    tests:
        Address Families:
            - rule:
                match:
                    Hostname: (^exit1|firewall)
                action:
                    filter
```

### Create Filters for Provisioning Exceptions

You can configure filters to change validation errors to warnings that would normally occur due to the default expectations of the `netq check` commands. This applies to all protocols and services, except for Agents. For example, if you have provisioned BGP with configurations where a BGP peer is not expected or desired, you will get errors that a BGP peer is missing. By creating a filter, you can remove the error in favor of a warning.

To create a validation filter:

1. Navigate to the */etc/netq* directory.

2. Create or open the *check_filter.yml*  file using your text editor of choice.

    This file contains the syntax to follow to create one or more rules for one or more protocols or services. Create your own rules, and/or edit and un-comment any example rules you would like to use.

    ```
    # Netq check result filter rule definition file.  This is for filtering
    # results based on regex match on one or more columns of each test result.
    # Currently, only action 'filter' is supported. Each test can have one or
    # more rules, and each rule can match on one or more columns.  In addition,
    # rules can also be optionally defined under the 'global' section and will
    # apply to all tests of a check.
    #
    # syntax:
    #
    # <check name>:
    #   tests:
    #     <test name, as shown in test list when using the include/exclude and tab>:
    #       - rule:
    #           match:
    #             <column name>: regex
    #             <more columns and regex.., result is AND>
    #           action:
    #             filter
    #       - <more rules..>
    #   global:
    #     - rule:
    #         . . .
    #     - rule:
    #         . . .
    #
    # <another check name>:
    #   . . .
    #
    # e.g.
    #
    # bgp:
    #   tests:
    #     Address Families:
    #       - rule:
    #           match:
    #             Hostname: (^exit*|^firewall)
    #             VRF: DataVrf1080
    #             Reason: AFI/SAFI evpn not activated on peer
    #           action:
    #             filter
    #       - rule:
    #           match:
    #             Hostname: exit-2
    #             Reason: SAFI evpn not activated on peer
    #           action:
    #             filter
    #     Router ID:
    #       - rule:
    #           match:
    #             Hostname: exit-2
    #           action:
    #             filter
    #
    # evpn:
    #   tests:
    #     EVPN Type 2:
    #       - rule:
    #           match:
    #             Hostname: exit-1
    #           action:
    #             filter
    #
    ```

## View Network Details

The `netq show` commands display a wide variety of content about the network and its various elements. You can show content for the following:

```
cumulus@switch:~$ netq show [TAB]
    agents                   :  Netq agent
    bgp                      :  BGP info
    cl-btrfs-info            :  Btrfs Information
    cl-manifest              :  Manifest Information
    cl-pkg-info              :  Package Information
    cl-resource              :  add help text
    cl-ssd-util              :  SSD Utilization Information
    clag                     :  Cumulus Multi-chassis LAG
    ethtool-stats            :  Interface statistics
    events                   :  Display changes over time
    evpn                     :  EVPN
    interface-stats          :  Interface statistics
    interface-utilization    :  Interface utils
    interfaces               :  network interface port
    inventory                :  Inventory information
    ip                       :  IPv4 related info
    ipv6                     :  IPv6 related info
    job-status               :  add help text
    kubernetes               :  Kubernetes Information
    lldp                     :  LLDP based neighbor info
    mac-history              :  Mac history info for a mac address
    macs                     :  Mac table or MAC address info
    mlag                     :  Multi-chassis LAG (alias of clag)
    notification             :  Send notifications to Slack or PagerDuty
    ntp                      :  NTP
    opta-health              :  Display health of apps on the OPTA
    opta-platform            :  Appliance version info and uptime
    ospf                     :  OSPF info
    recommended-pkg-version  :  Current host information to be considered
    resource-util            :  add help text
    sensors                  :  Temperature/Fan/PSU sensors
    services                 :  System services
    tca                      :  Threshold Crossing Alerts
    trace                    :  Control plane trace path across fabric
    unit-tests               :  Show list of unit tests for netq tests
    validation               :  Schedule a validation check
    vlan                     :  VLAN
    vxlan                    :  VXLAN data path
    wjh-drop                 :  add help text
```

For example, to validate status of the NetQ agents running in the fabric, run `netq show agents`. A *Fresh* status indicates the Agent is running as expected. The Agent sends a heartbeat every 30 seconds, and if three consecutive heartbeats are missed, its status changes to
*Rotten*.

```
cumulus@switch:~$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
border01          Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 18:16:00 2020  Wed Apr 29 16:38:24 2020  Wed Apr 29 16:38:24 2020   Sun May  3 16:40:32 2020
border02          Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 18:10:31 2020  Wed Apr 29 16:38:22 2020  Wed Apr 29 16:38:22 2020   Sun May  3 16:53:06 2020
fw1               Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 18:20:18 2020  Wed Apr 29 16:38:35 2020  Wed Apr 29 16:38:35 2020   Sun May  3 16:40:29 2020
fw2               Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 18:35:24 2020  Wed Apr 29 16:38:29 2020  Wed Apr 29 16:38:29 2020   Sun May  3 16:40:07 2020
leaf01            Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 18:05:01 2020  Wed Apr 29 16:38:23 2020  Wed Apr 29 16:38:23 2020   Sun May  3 16:40:06 2020
leaf02            Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 17:59:26 2020  Wed Apr 29 16:38:32 2020  Wed Apr 29 16:38:32 2020   Sun May  3 16:40:20 2020
leaf03            Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 18:05:01 2020  Wed Apr 29 16:38:11 2020  Wed Apr 29 16:38:11 2020   Sun May  3 16:40:41 2020
oob-mgmt-server   Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 00:31:08 2020  Fri Apr 24 00:31:20 2020  Wed Apr 29 16:39:15 2020   Sun May  3 16:40:01 2020
server01          Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 01:30:14 2020  Fri Apr 24 01:30:27 2020  Wed Apr 29 16:39:16 2020   Sun May  3 16:41:15 2020
server02          Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 01:30:14 2020  Fri Apr 24 01:30:26 2020  Wed Apr 29 16:39:19 2020   Sun May  3 16:40:51 2020
server03          Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 01:30:13 2020  Wed Apr 29 16:46:24 2020  Wed Apr 29 16:46:24 2020   Sun May  3 16:47:01 2020
server04          Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 01:30:14 2020  Fri Apr 24 01:30:27 2020  Wed Apr 29 16:39:16 2020   Sun May  3 16:41:33 2020
server05          Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 01:30:13 2020  Wed Apr 29 16:46:26 2020  Wed Apr 29 16:46:26 2020   Sun May  3 16:47:12 2020
server06          Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 01:30:13 2020  Fri Apr 24 01:30:27 2020  Wed Apr 29 16:38:47 2020   Sun May  3 16:40:24 2020
server07          Fresh            yes      2.4.1-ub18.04u26~1581351889.c5ec3e5  Fri Apr 24 00:43:06 2020  Fri Apr 24 00:43:18 2020  Wed Apr 29 16:39:16 2020   Mon May  4 13:25:24 2020
spine01           Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 17:54:53 2020  Wed Apr 29 16:38:18 2020  Wed Apr 29 16:38:18 2020   Sun May  3 17:12:12 2020
spine02           Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 17:49:37 2020  Wed Apr 29 16:38:28 2020  Wed Apr 29 16:38:28 2020   Sun May  3 16:39:50 2020
spine03           Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 17:49:40 2020  Wed Apr 29 16:38:12 2020  Wed Apr 29 16:38:12 2020   Sun May  3 16:40:06 2020
spine04           Fresh            yes      3.0.0-cl3u27~1587646213.c5bc079      Mon Apr 27 17:48:20 2020  Wed Apr 29 16:38:24 2020  Wed Apr 29 16:38:24 2020   Sun May  3 16:40:18 2020

```

Some additional examples follow.

View the status of BGP:

```
cumulus@switch:~$ netq show bgp
Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
exit01            swp44(internet)              vrf1            65041      25253      2/-/-        Fri Apr 19 16:00:40 2019
exit01            swp51(spine01)               default         65041      65020      8/-/59       Fri Apr 19 16:00:40 2019
exit01            swp52(spine02)               default         65041      65020      8/-/59       Fri Apr 19 16:00:40 2019
exit02            swp44(internet)              vrf1            65042      25253      7/-/-        Fri Apr 19 16:00:40 2019
exit02            swp51(spine01)               default         65042      65020      8/-/59       Fri Apr 19 16:00:40 2019
exit02            swp52(spine02)               default         65042      65020      8/-/59       Fri Apr 19 16:00:40 2019
leaf01            peerlink.4094(leaf02)        default         65011      65011      9/-/34       Fri Apr 19 16:00:40 2019`
leaf01            swp51(spine01)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
leaf01            swp52(spine02)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
leaf02            peerlink.4094(leaf01)        default         65011      65011      9/-/34       Fri Apr 19 16:00:40 2019
leaf02            swp51(spine01)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
leaf02            swp52(spine02)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
leaf03            peerlink.4094(leaf04)        default         65012      65012      9/-/34       Fri Apr 19 16:00:40 2019
leaf03            swp51(spine01)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
leaf03            swp52(spine02)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
leaf04            peerlink.4094(leaf03)        default         65012      65012      9/-/34       Fri Apr 19 16:00:40 2019
leaf04            swp51(spine01)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
leaf04            swp52(spine02)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
spine01           swp1(leaf01)                 default         65020      65011      3/-/14       Fri Apr 19 16:00:40 2019
spine01           swp2(leaf02)                 default         65020      65011      3/-/14       Fri Apr 19 16:00:40 2019
spine01           swp29(exit02)                default         65020      65042      1/-/3        Fri Apr 19 16:00:40 2019
spine01           swp3(leaf03)                 default         65020      65012      3/-/14       Fri Apr 19 16:00:40 2019
spine01           swp30(exit01)                default         65020      65041      1/-/3        Fri Apr 19 16:00:40 2019
spine01           swp4(leaf04)                 default         65020      65012      3/-/14       Fri Apr 19 16:00:40 2019
spine02           swp1(leaf01)                 default         65020      65011      3/-/12       Fri Apr 19 16:00:40 2019
spine02           swp2(leaf02)                 default         65020      65011      3/-/12       Fri Apr 19 16:00:40 2019
spine02           swp29(exit02)                default         65020      65042      1/-/3        Fri Apr 19 16:00:40 2019
spine02           swp3(leaf03)                 default         65020      65012      3/-/12       Fri Apr 19 16:00:40 2019
spine02           swp30(exit01)                default         65020      65041      1/-/3        Fri Apr 19 16:00:40 2019
spine02           swp4(leaf04)                 default         65020      65012      3/-/12       Fri Apr 19 16:00:40 2019
```

View the status of your VLANs:

```
cumulus@switch:~$ netq show vlan
Matching vlan records:
Hostname          VLANs                     SVIs                      Last Changed
----------------- ------------------------- ------------------------- -------------------------
exit01            4001                      4001                      Tue Mar 17 19:52:16 2020
exit02            4001                      4001                      Tue Mar 17 19:52:16 2020
leaf01            1,13,24,4001              13 24 4001                Tue Mar 17 19:52:16 2020
leaf02            1,13,24,4001              13 24 4001                Tue Mar 17 19:52:16 2020
leaf03            1,13,24,4001              13 24 4001                Tue Mar 17 19:52:16 2020
leaf04            1,13,24,4001              13 24 4001                Tue Mar 17 19:52:16 2020
```

View the status of the hardware sensors:

```
cumulus@switch:~$ netq show sensors all
Matching sensors records:
Hostname          Name            Description                         State      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- ----------------------------------- -------------------------
exit01            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 23:02:35 2019
exit01            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 23:02:35 2019
exit01            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 23:02:35 2019
exit01            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 23:02:35 2019
exit01            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 23:02:35 2019
exit01            fan6            fan tray 3, fan 2                   ok                                             Wed Feb  6 23:02:35 2019
exit01            psu1fan1        psu1 fan                            ok                                             Wed Feb  6 23:02:35 2019
exit01            psu2fan1        psu2 fan                            ok                                             Wed Feb  6 23:02:35 2019
exit02            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 23:03:35 2019
exit02            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 23:03:35 2019
exit02            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 23:03:35 2019
exit02            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 23:03:35 2019
exit02            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 23:03:35 2019
exit02            fan6            fan tray 3, fan 2                   ok                                             Wed Feb  6 23:03:35 2019
exit02            psu1fan1        psu1 fan                            ok                                             Wed Feb  6 23:03:35 2019
exit02            psu2fan1        psu2 fan                            ok                                             Wed Feb  6 23:03:35 2019
leaf01            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 23:01:12 2019
leaf01            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 23:01:12 2019
leaf01            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 23:01:12 2019
leaf01            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 23:01:12 2019
leaf01            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 23:01:12 2019
leaf01            fan6            fan tray 3, fan 2                   ok                                             Wed Feb  6 23:01:12 2019
leaf01            psu1fan1        psu1 fan                            ok                                             Wed Feb  6 23:01:12 2019
leaf01            psu2fan1        psu2 fan                            ok                                             Wed Feb  6 23:01:12 2019
leaf02            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 22:59:54 2019
leaf02            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 22:59:54 2019
leaf02            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 22:59:54 2019
leaf02            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 22:59:54 2019
leaf02            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 22:59:54 2019
...
```
