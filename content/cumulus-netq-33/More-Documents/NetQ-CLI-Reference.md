---
title: NetQ CLI Reference
author: Cumulus Networks
weight: 1100
toc: 3
right_toc_levels: 2
pdfhidden: true
draft: true
---
This reference provides details about each of the NetQ CLI commands, starting with the 2.4.0 release. For an overview of the CLI structure and usage, read {{<link title="NetQ Command Line Overview">}}. The commands are grouped into functional areas. When options are available, they should be used in the order listed.

## Validation Commands

There are three sets of validation commands:

- The original on-demand validation commands. These commands all begin with `netq check`. They are used to validate various elements in your network fabric at the current time or a time in the past. They allow filtering by hostname, can include or exclude selected tests, and some have additional options. The results are presented in the NetQ CLI immediately.
- The newer set of validation commands are used to create on-demand or scheduled validations with the results being displayed in the NetQ UI Validation Result cards. These commands begin with `netq add validation`. They are used to validate various elements in your network fabric currently or on a regular basis. No filtering on results is available within the commands as that is accomplished through the NetQ UI.
- The validation management commands. These present a list of all jobs and job settings, and the ability to remove validations.

Refer to {{<link title="Validation Checks">}} for a description of the tests run as part of each validation. The commands are described here in alphabetical order, regardless of membership in one of the three sets above.

- - -

### netq add validation

Creates an on-demand validation for various protocols and services, with results displayed in the associated On-demand Validation Result cards in the NetQ UI.

#### Syntax

```
netq add validation
    type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf)
    [alert-on-failure]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| type | agents, bgp, evpn, interfaces, license, mlag, mtu, ntp, sensors, vlan, or vxlan | Protocol or service to be validated |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| alert-on-failure | NA | Reserved |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

#### Sample Usage

BGP validation; all devices, all tests, currently

```
cumulus@switch:~$ netq add validation type bgp
```

#### Related Commands

- netq add validation name
- netq del validation
- netq show validation settings
- netq show validation summary

- - -

### netq add validation name

Creates a validation for various protocols and services to be run on a regular interval, with results displayed in the associated Scheduled Validation Result cards in the NetQ UI. A maximum of 15 scheduled validation can be configured, not including the default scheduled validations.

#### Syntax

```
netq add validation
    name <text-new-validation-name>
    type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf)
    interval <text-time-min>
    [alert-on-failure]
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| name | user defined | Unique name for the validation |
| type | agents, bgp, evpn, interfaces, license, mlag, mtu, ntp, sensors, vlan, or vxlan | Protocol or service to be validated |
| interval | \<text-time-min\> | Frequency to run the validation, in minutes. Value must include time unit of *m*, minutes. Default scheduled validations per type run every 60 minutes. |

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| alert-on-failure | NA | Reserved |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

#### Sample Usage

BGP validation; all devices, all tests, on a regular basis

```
cumulus@switch:~$ netq add validation name Bgp15m type bgp interval 15m
```

#### Related Commands

- netq add validation
- netq del validation
- netq show validation settings
- netq show validation summary

- - -

### netq check agents

Validates the communication status of all nodes (leafs, spines, and hosts) running the NetQ Agent in your network fabric. The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings

#### Syntax

```
netq check agents
   [label <text-label-name> | hostnames <text-list-hostnames>]
   [include <agent-number-range-list> | exclude <agent-number-range-list>]
   [around <text-time>]
   [json]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames with to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic Validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check agents
agent check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Agent Health Test   : passed
```

Validation for Selected Devices

```
cumulus@switch:~$ netq check agents hostnames leaf01,leaf02,leaf03,leaf04
agent check result summary:

Total nodes         : 4
Checked nodes       : 4
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Agent Health Test   : passed
```

Validation for a Time in the Past

```
cumulus@switch:~$ netq check agents around 4h
agent check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Agent Health Test   : passed
```

#### Related Commands

- netq show agents
- netq show unit-tests agent
- netq add validation
- netq add validation name
- netq config agent

- - -

### netq check bgp

Validates that all configured route peering is established in your network fabric by looking for consistency across BGP sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state. If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Total number of BGP sessions at the specified time
- Number of sessions that have failed to establish a connection

#### Syntax

```
netq check bgp
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [vrf <vrf>]
    [include <bgp-number-range-list> | exclude <bgp-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| vrf | \<vrf\> | When a VRF is configured, the accepted values include: <ul><li>default: use the default routing table</li><li> mgmt: use management routing table</li><li>\<custom\>: use user-defined routing table</li></ul> |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check bgp
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
Address Families Test        : passed
Router ID Test               : passed
```

#### Related Commands

- netq show bgp
- netq show unit-tests bgp
- netq add validation
- netq add validation name

- - -

### netq check cl-version

Verifies the Cumulus Linux version is consistent across nodes, matches a specified version, or is greater than or equal to a specified version, based on the options chosen.

#### Syntax

```
netq check cl-version [label <text-label-name> | hostnames <text-list-hostnames>] [match-version <cl-ver> | min-version <cl-ver>] [include <version-number-range-list> | exclude <version-number-range-list>] [around <text-time>] [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| match-version | \<cl-ver\> | Identifies all switches with a Cumulus Linux version other than the one specified with this option. `cl-ver` values are specified in x.y.z format, for example 4.2.0.
| min-version | \<cl-ver\> | Identifies all switches with a Cumulus Linux version older than the one specified with this option. `cl-ver` values are specified in x.y.z format, for example 3.7.12. |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices have the same version

```
cumulus@switch:~$ netq check cl-version
version check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Cumulus Linux Image Version Test   : passed
```

List devices which do not match a version

```
cumulus@switch:~$ netq check cl-version match-version 3.7.12
version check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 12
Rotten nodes        : 0
Warning nodes       : 0

Cumulus Linux Image Version Test   : 0 warnings, 12 errors

Cumulus Linux Image Version Test details:
Hostname          Entity       Version                              Reason
----------------- ------------ ------------------------------------ ---------------------------------------------
border01          OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
border02          OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
fw1               OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
fw2               OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
leaf01            OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
leaf02            OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
leaf03            OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
leaf04            OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
spine01           OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
spine02           OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
spine03           OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
spine04           OS           4.2.1                                unexpected os version 4.2.1, should be 3.7.12
```

List devices with a version greater than or equal to a version

```
cumulus@switch:~$ netq check cl-version min-version 3.7.12
version check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Cumulus Linux Image Version Test   : passed
```

#### Related Commands

- netq show unit-tests cl-version

- - -

### netq check clag

Verifies CLAG session consistency by identifying all CLAG peers with errors or misconfigurations in the NetQ domain. In particular, it looks for such items as:

- multiple link pairs with the same system MAC address
- any interfaces with only a single attachment
- peer connectivity
- conflicted bonds
- whether the backup IP address is pointing to the correct peer

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings

#### Syntax

```
netq check clag
    [label <text-label-name> | hostnames <text-list-hostnames> ]
    [include <clag-number-range-list> | exclude <clag-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check clag
clag check result summary:

Total nodes         : 6
Checked nodes       : 6
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Peering Test             : passed
Backup IP Test           : passed
Clag SysMac Test         : passed
VXLAN Anycast IP Test    : passed
Bridge Membership Test   : passed
Spanning Tree Test       : passed
Dual Home Test           : passed
Single Home Test         : passed
Conflicted Bonds Test    : passed
ProtoDown Bonds Test     : passed
SVI Test                 : passed
```

Validate only selected devices

```
cumulus@switch:~$ netq check clag hostnames leaf01,leaf02
clag check result summary:

Total nodes         : 2
Checked nodes       : 2
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Peering Test             : passed
Backup IP Test           : passed
Clag SysMac Test         : passed
VXLAN Anycast IP Test    : passed
Bridge Membership Test   : passed
Spanning Tree Test       : passed
Dual Home Test           : passed
Single Home Test         : passed
Conflicted Bonds Test    : passed
ProtoDown Bonds Test     : passed
SVI Test                 : passed
```

Exclude selected validation tests

```
cumulus@switch:~$ netq check clag exclude 2
clag check result summary:

Total nodes         : 6
Checked nodes       : 6
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Peering Test             : passed
Backup IP Test           : passed
Clag SysMac Test         : skipped
VXLAN Anycast IP Test    : passed
Bridge Membership Test   : passed
Spanning Tree Test       : passed
Dual Home Test           : passed
Single Home Test         : passed
Conflicted Bonds Test    : passed
ProtoDown Bonds Test     : passed
SVI Test                 : passed
```

#### Related Commands

- netq show clag
- netq show unit-tests clag
- netq add validation
- netq add validation name

- - -

### netq check evpn

Verifies communication status for all nodes (leafs, spines, and hosts) running instances of Ethernet VPN (EVPN) in your network fabric. In particular, it looks for such items as:

- BGP and EVPN session establishment
- VNI type consistency
- VLAN consistency among participating devices
- VRF consistency among participating devices

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Total number of VNIs
- Number of failed BGP sessions
- Total number of sessions

#### Syntax

```
netq check evpn
    [mac-consistency]
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <evpn-number-range-list> | exclude <evpn-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| mac-consistency | NA | Verifies if the MAC address associated with each end of the EVPN connection is
the same |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 2.2.0 | Added `mac-consistency` option. Removed `hostname` and `vni` options. |

#### Sample Usage

Basic validation: All devices, all tests, currently

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

#### Related Commands

- netq show evpn
- netq show unit-tests evpn
- netq add validation
- netq add validation name

- - -

### netq check interfaces

Verifies interface communication status for all nodes (leafs, spines, and hosts) or an interface between specific nodes in your network fabric. In particular, it looks for such items as:

- Administrative and operational state status
- Link speed consistency
- Autonegotiation settings consistency

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of ports validated
- Number of ports that failed validation
- Number of unverified ports (no peer was found for node)

#### Syntax

```
netq check interfaces
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <interface-number-range-list> | exclude <interface-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 2.1.0 | Removed host and peer options (`physical-hostname`, `physical-port`, `peer-physical-hostname`, `peer-physical-port`) and `unverified` option |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check interfaces
interface check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 6
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Ports       : 145
Failed Ports        : 12
Unverified Ports    : 69

Admin State Test   : passed
Oper State Test    : passed
Speed Test         : passed
Autoneg Test       : 0 warnings, 12 errors

Autoneg Test details:
Hostname          Interface                 Peer Hostname     Peer Interface            Message                             Last Changed
----------------- ------------------------- ----------------- ------------------------- ----------------------------------- -------------------------
server01          eth1                      leaf01            swp1                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server01          eth2                      leaf02            swp1                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server02          eth1                      leaf01            swp2                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server02          eth2                      leaf02            swp2                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server03          eth1                      leaf01            swp3                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server03          eth2                      leaf02            swp3                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server04          eth1                      leaf03            swp1                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server04          eth2                      leaf04            swp1                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server05          eth1                      leaf03            swp2                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server05          eth2                      leaf04            swp2                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server06          eth1                      leaf03            swp3                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
server06          eth2                      leaf04            swp3                      Autoneg mismatch (on, off)          Wed Nov 18 21:58:07 2020 
```

Basic validation without error information

```
cumulus@switch:~$ netq check interfaces summary
interface check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 6
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Ports       : 145
Failed Ports        : 12
Unverified Ports    : 69

Admin State Test   : passed
Oper State Test    : passed
Speed Test         : passed
Autoneg Test       : 0 warnings, 12 errors
```

#### Related Commands

- netq show interfaces
- netq show unit-tests interfaces
- netq add validation
- netq add validation name

- - -

### netq check license

Verifies license status for all nodes (leafs, spines, and hosts) in your network fabric. In particular, it looks for the validity of the Cumulus Linux license on each node.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of licenses validated
- Number of licenses that failed validation

#### Syntax

```
netq check license
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <license-number-range-list> | exclude <license-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check license
license check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Licenses    : 0
Failed Licenses     : 0

License validity Test   : passed
```

#### Related Commands

- netq show unit-tests license
- netq add validation
- netq add validation name

- - -

### netq check lnv

{{<notice info>}}
This command is not supported for NetQ 3.0.0 and later.
{{</notice>}}

- - -

### netq check mtu

Verifies consistency of the maximum transmission unit (MTU) across all links in your network fabric. MTU consistency is verified at the level that is appropriate to the specific type of link. For example, bond interfaces have their MTU enforced at the bond level and not at the individual slave level. For MLAG/CLAG bonds, verification confirms whether or not both ends of the bond have the same MTU value configured for their local instance of the bond. You can also view nodes without a peer link.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of links validated
- Number of links that failed validation
- Number of links that had warnings

#### Syntax

```
netq check mtu
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [unverified]
    [include <mtu-number-range-list> | exclude <mtu-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| unverified | NA | Find nodes without a known peer link |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check mtu
mtu check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 3
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Links       : 291
Failed Links        : 8
Warn Links          : 0

Link MTU Consistency Test   : 0 warnings, 8 errors
VLAN interface Test         : passed
Bridge interface Test       : passed

Link MTU Consistency Test details:
Hostname          Interface                 MTU    Peer              Peer Interface            Peer MTU Reason
----------------- ------------------------- ------ ----------------- ------------------------- -------- ---------------------------------------------
border01          bond3                     9000   fw1               borderBond                9216     MTU Mismatch                                 
border01          swp3                      9000   fw1               swp1                      9216     MTU Mismatch                                 
border02          bond3                     9000   fw1               borderBond                9216     MTU Mismatch                                 
border02          swp3                      9000   fw1               swp2                      9216     MTU Mismatch                                 
fw1               borderBond                9216   border01          bond3                     9000     MTU Mismatch                                 
fw1               borderBond                9216   border02          bond3                     9000     MTU Mismatch                                 
fw1               swp1                      9216   border01          swp3                      9000     MTU Mismatch                                 
fw1               swp2                      9216   border02          swp3                      9000     MTU Mismatch       
```

Add nodes without peer links to output.

```
cumulus@switch:~$ netq check mtu unverified
mtu check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 3
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Links       : 291
Failed Links        : 8
Warn Links          : 0

Link MTU Consistency Test   : 0 warnings, 8 errors
VLAN interface Test         : passed
Bridge interface Test       : passed

Link MTU Consistency Test details:
Hostname          Interface                 MTU    Peer              Peer Interface            Peer MTU Reason
----------------- ------------------------- ------ ----------------- ------------------------- -------- ---------------------------------------------
border01          bond3                     9000   fw1               borderBond                9216     MTU Mismatch                                 
border01          swp3                      9000   fw1               swp1                      9216     MTU Mismatch                                 
border02          bond3                     9000   fw1               borderBond                9216     MTU Mismatch                                 
border02          swp3                      9000   fw1               swp2                      9216     MTU Mismatch                                 
fw1               borderBond                9216   border01          bond3                     9000     MTU Mismatch                                 
fw1               borderBond                9216   border02          bond3                     9000     MTU Mismatch                                 
fw1               swp1                      9216   border01          swp3                      9000     MTU Mismatch                                 
fw1               swp2                      9216   border02          swp3                      9000     MTU Mismatch                                 

Link MTU Consistency Test unverified:
Hostname          Interface                 MTU    Peer              Peer Interface            Peer MTU Reason
----------------- ------------------------- ------ ----------------- ------------------------- -------- ---------------------------------------------
oob-mgmt-server   vagrant                   1500   -                 -                         -        No Peer link info
```

#### Related Commands

- netq show unit-tests mtu
- netq add validation
- netq add validation name

- - -

### netq check ntp

Verifies network time synchronization using NTP for all nodes (leafs, spines, and hosts) in your network fabric. Nodes that are not in time sychronization with the NetQ appliance or VM may report data with an incorrect timestamp or lose communication altogether.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of nodes found that are unknown to NetQ
- Number of NTP servers available for synchronization

#### Syntax

```
netq check ntp [label <text-label-name> | hostnames <text-list-hostnames>] [include <ntp-number-range-list> | exclude <ntp-number-range-list>] [around <text-time>] [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check ntp
ntp check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 2
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Unknown nodes       : 0
NTP Servers         : 2

NTP Sync Test   : 0 warnings, 2 errors

NTP Sync Test details:
Hostname          NTP Sync Connect Time
----------------- -------- -------------------------
fw1               no       2020-11-18 19:50:31
fw2               no       2020-11-18 19:50:46
```

#### Related Commands

- netq show ntp
- netq show unit-tests ntp
- netq add validation
- netq add validation name

- - -

### netq check ospf

Validates that all configured route peering is established in your network fabric by looking for consistency across OSPF sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation (reporting session failures)
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of nodes with failed adjacencies
- Total number of adjacencies

#### Syntax

```
netq check ospf
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <ospf-number-range-list> | exclude <ospf-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~# netq check ospf
ospf check result summary:

Total nodes: 8
Checked nodes: 8
Failed nodes: 4
Rotten nodes: 0
Warning nodes: 0

Additional summary:
Failed Adjacencies: 4
Total Adjacencies: 24

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

#### Related Commands

- netq show ospf
- netq show unit-tests ospf
- netq add validation
- netq add validation name

- - -

### netq check sensors

Verifies the status of temperature, cooling fan, and power supply sensors for all nodes in your network fabric.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of sensors validated
- Number of sensors that failed validation

#### Syntax

```
netq check sensors
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <sensors-number-range-list> | exclude <sensors-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check sensors
sensors check result summary:

Total nodes         : 13
Checked nodes       : 13
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Checked Sensors     : 102
Failed Sensors      : 0


PSU sensors Test           : passed
Fan sensors Test           : passed
Temperature sensors Test   : passed
```

#### Related Commands

- netq show sensors
- netq show unit-tests sensors
- netq add validation
- netq add validation name

- - -

### netq check vlan

Verifies consistency of the virtual local area network (VLAN) nodes and interfaces across all links in your network fabric. In particular, it looks for link neighbor and MLAG bond consistency. You can also identify nodes without peers.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Total number of links found
- Number of links that failed validation

#### Syntax

```
netq check vlan
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [unverified]
    [include <vlan-number-range-list> | exclude <vlan-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| unverified | NA | Find nodes with no peer |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check vlan
vlan check result summary:

Total nodes         : 21
Checked nodes       : 21
Failed nodes        : 3
Rotten nodes        : 0
Warning nodes       : 0

Additional summary:
Total Link Count    : 291
Failed Link Count   : 4

Link Neighbor VLAN Consistency Test   : 0 warnings, 4 errors
Clag Bond VLAN Consistency Test       : 0 warnings, 2 errors

Link Neighbor VLAN Consistency Test details:
Hostname          Interface                 VLANs                     Peer              Peer Interface            Peer VLANs                Message
----------------- ------------------------- ------------------------- ----------------- ------------------------- ------------------------- -----------------------------------
border01          bond3                     10,20,30                  fw1               borderBond                10,20                     bond3 VLAN set (10,20,30) mismatch 
                                                                                                                                            with peer fw1:borderBond (10,20)   
border02          bond3                     10,20,30                  fw1               borderBond                10,20                     bond3 VLAN set (10,20,30) mismatch 
                                                                                                                                            with peer fw1:borderBond (10,20)   
fw1               borderBond                10,20                     border01          bond3                     10,20,30                  borderBond VLAN set (10,20) mismatc
                                                                                                                                            h with peer border01:bond3 (10,20,3
                                                                                                                                            0)                                 
fw1               borderBond                10,20                     border02          bond3                     10,20,30                  borderBond VLAN set (10,20) mismatc
                                                                                                                                            h with peer border02:bond3 (10,20,3
                                                                                                                                            0)   

Clag Bond VLAN Consistency Test details:
Hostname          Interface                 VLANs                     Peer              Peer Interface            Peer VLANs                Message
----------------- ------------------------- ------------------------- ----------------- ------------------------- ------------------------- -----------------------------------
border01          bond3                     10,20,30                  -                 -                         -                         bond3 VLAN set (10,20,30) missing o
                                                                                                                                            n peerlink                         
border02          bond3                     10,20,30                  -                 -                         -                         bond3 VLAN set (10,20,30) missing o
                                                                                                                                            n peerlink
```

#### Related Commands

- netq show vlan
- netq show unit-tests vlan
- netq add validation
- netq add validation name

- - -

### netq check vxlan

Verifies consistency of the virtual extensible local area network (VXLAN) nodes and interfaces across all links in your network fabric. In particular, it looks for consistent VXLAN configuration and BUM replication errors.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings

#### Syntax

```
netq check vxlan
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <vxlan-number-range-list> | exclude <vxlan-number-range-list>]
    [around <text-time>]
    [json | summary]
```

#### Required Arguments

None

#### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |

#### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check vxlan
vxlan check result summary:

Total nodes         : 6
Checked nodes       : 6
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0

Vlan Consistency Test   : passed
BUM replication Test    : passed
```

#### Related Commands

- netq show vxlan
- netq show unit-tests vxlan
- netq add validation
- netq add validation name

- - -

### netq del validation

Removes a scheduled validation. Useful when you have created a scheduled validation for troubleshooting and you no longer need it, or if you are reaching your maximum of 15 scheduled validations and you want to prioritize one validation over another. Use the related `netq show validation settings` command to view the names of existing scheduled validations.

#### Syntax

```
netq del validation
    <text-validation-name>
```

#### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-validation-name\> | Name of scheduled validation you want to remove |

#### Options

None

#### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

#### Sample Usage

```
cumulus@switch:~$ netq del validation Bgp15m
Successfully deleted validation Bgp15m
```

#### Related Commands

- netq add validation name
- netq show validation settings

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
| around | \<text-time-hr\> | Show summary status for this time in the past. Value must be specified in hours and include the *hr* time unit. Default is 24 hours. |
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

## Show Commands

All of the NetQ show commands begin with netq show. They are used to view the health of various elements in your network fabric. They are described here in alphabetical order.

### netq show agents

Displays basic configuration, health, and connectivity status for all nodes or a specific node running NetQ Agent in your network fabric. The output provides:
whether each node has been heard recently (last 90 seconds), 
if it is in time synchronization [with the ts?], 
the NetQ Agent software version currently running on the node, 
how long the node has been up, 
how long the NetQ Agent has been up, 
the last time the NetQ Agent was reinitialized, and 
How long ago the last change was made to the [node or NetQ Agent configuration of status?].
Optionally you may also display the changes (add, delete, xxx) made to all nodes or a specific node.
This command gives you an easy way to see if any NetQ Agents or their nodes have lost power, may have difficulty communicating with the telemetry server, and whether agents are running different versions of software. Any of these situations could cause problems in the operation of your network.
Syntax
netq [<hostname>] show agents 
		[changes] 
		[json]
Required Arguments
	None
Optional Arguments
hostname
Text used to identify a particular node in your network fabric; for example, leaf01 or swp3.
changes
Display changes made to one or all nodes along with standard output.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
View status of all nodes with NetQ Agent installed
cumulus@ts:~$ netq show agents 
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
border01          Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:54 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:38 2020
border02          Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:57 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:33 2020
fw1               Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:44 2020  Tue Sep 29 21:24:48 2020  Tue Sep 29 21:24:48 2020   Thu Oct  1 16:07:26 2020
fw2               Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:42 2020  Tue Sep 29 21:24:48 2020  Tue Sep 29 21:24:48 2020   Thu Oct  1 16:07:22 2020
leaf01            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 16:49:04 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:10 2020
leaf02            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:14 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:30 2020
leaf03            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:37 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:24 2020
leaf04            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:35 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:13 2020
oob-mgmt-server   Fresh            yes      3.1.1-ub18.04u29~1599111022.78b9e43  Mon Sep 21 16:43:58 2020  Mon Sep 21 17:55:00 2020  Mon Sep 21 17:55:00 2020   Thu Oct  1 16:07:31 2020
server01          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:16 2020
server02          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:24 2020
server03          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:56 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:12 2020
server04          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:17 2020
server05          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:25 2020
server06          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:21 2020
server07          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:06:48 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:28 2020
server08          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:06:45 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:31 2020
spine01           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:34 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:20 2020
spine02           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:33 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:16 2020
spine03           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:34 2020  Tue Sep 29 21:25:07 2020  Tue Sep 29 21:25:07 2020   Thu Oct  1 16:07:20 2020
spine04           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:32 2020  Tue Sep 29 21:25:07 2020  Tue Sep 29 21:25:07 2020   Thu Oct  1 16:07:33 2020

View status of all nodes with NetQ Agents, and display the results in JSON format
cumulus@ts:~$ netq show agents json
{
    "agents":[
        {
            "status":"Fresh",
            "lastChanged":1526584467.1063349247,
            "reinitializeTime":1526068569.3166179657,
            "hostname":"server02",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068557.7966170311,
            "ntpSync":"yes",
            "agentUptime":1526068569.316617012
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.6665298939,
            "reinitializeTime":1526068569.3423800468,
            "hostname":"server04",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068557.8123779297,
            "ntpSync":"yes",
            "agentUptime":1526068569.3423779011
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.0170140266,
            "reinitializeTime":1526577085.9067358971,
            "hostname":"server01",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068558.8021190166,
            "ntpSync":"yes",
            "agentUptime":1526068570.452119112
        },
        {
            "status":"Fresh",
            "lastChanged":1526584461.5413489342,
            "reinitializeTime":1526068569.4015939236,
            "hostname":"server03",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068557.7815930843,
            "ntpSync":"yes",
            "agentUptime":1526068569.4015929699
        },
        {
            "status":"Fresh",
            "lastChanged":1526584444.7508759499,
            "reinitializeTime":1526068529.5848419666,
            "hostname":"spine02",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526059415.8448050022,
            "ntpSync":"yes",
            "agentUptime":1526068529.5848050117
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.869822979,
            "reinitializeTime":1526318846.8988080025,
            "hostname":"leaf04",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526055851.829241991,
            "ntpSync":"yes",
            "agentUptime":1526068529.5392420292
        },
        {
            "status":"Fresh",
            "lastChanged":1526584444.1613891125,
            "reinitializeTime":1526068529.5949180126,
            "hostname":"leaf02",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526053212.2249178886,
            "ntpSync":"yes",
            "agentUptime":1526068529.5949180126
        },
        {
            "status":"Fresh",
            "lastChanged":1526584444.1491498947,
            "reinitializeTime":1526068529.6256389618,
            "hostname":"leaf03",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526053793.9156200886,
            "ntpSync":"yes",
            "agentUptime":1526068529.6256198883
        },
        {
            "status":"Fresh",
            "lastChanged":1526584443.1579871178,
            "reinitializeTime":1526576730.014993906,
            "hostname":"spine01",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526057852.8196310997,
            "ntpSync":"yes",
            "agentUptime":1526068529.6696310043
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.865801096,
            "reinitializeTime":1526392781.1005580425,
            "hostname":"leaf01",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526053158.7921569347,
            "ntpSync":"yes",
            "agentUptime":1526068529.7521569729
        },
        {
            "status":"Fresh",
            "lastChanged":1526584456.1811571121,
            "reinitializeTime":1526576736.1758289337,
            "hostname":"switch",
            "version":"1.4.0-cl3u10~1525711818.58b9c8f",
            "sysUptime":1526283003.6326210499,
            "ntpSync":"yes",
            "agentUptime":1526314445.2926208973
	}
    ],
    "truncatedResult":false
}
Related Commands
netq check agents    

### netq show bgp

There are two forms of this command. One displays all nodes or a specific node running BGP in your network fabric. In this form, the output displays the following for each node::
the neighbor nodes to the given node, 
whether multiple routing tables (VRF) have been applied, 
the autonomous system number (ASN) assigned to the node, 
the peer ASN for each neighbor, 
the PfxRx [what is this?], and 
how long ago the last change was made to the node.
The second form of this command displays all of the changes (add, delete, xxx) made to the nodes running BGP over a period of time in addition to the metrics displayed for the first form. 
If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.
This command gives you an easy way to see [xxx]
Syntax
netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] 
		[vrf <default|mgmt>] 
		[around <text-time>] 
		[json]
OR
netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] 
		[vrf <default|mgmt>] 
		changes [between <text-time> and <text-endtime>]
		[json]

Required Arguments
changes
Display changes made to one or all nodes.
Optional Arguments
hostname
Text used to identify a particular node in your network fabric; for example, leaf01 or swp3.
bgp session
Only display results for the specified BGP session; for example 5468354.
asn <number-asn>
Only display results for the specified ASN number; for example 65013.
vrf (default|mgmt)
For nodes using VRF, indicate whether to use the default routing table or the management routing table. 
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
Between <text-time> and <text-endtime>
Indicates the time frame for which you want to view changes. [explain how this works--which variable is the more recent time???]
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
View status of all nodes running BGP
cumulus@ts:~$ netq show bgp 
Matching bgp records:
Hostname          Neighbor                         VRF              ASN        Peer ASN   PfxRx        Last Changed
----------------- -------------------------------- ---------------- ---------- ---------- ------------ ----------------
leaf01            swp51(spine01)                   default          65011      65020      5/-/23       2d:15h:2m:29s
leaf01            swp52(spine02)                   default          65011      65020      5/-/23       2d:15h:2m:29s
leaf02            swp51(spine01)                   default          65012      65020      6/-/23       5d:23h:30m:50s
leaf02            swp52(spine02)                   default          65012      65020      6/-/23       5d:23h:30m:50s
leaf03            swp51(spine01)                   default          65013      65020      5/-/24       5d:23h:30m:50s
leaf03            swp52(spine02)                   default          65013      65020      5/-/24       5d:23h:30m:50s
leaf04            swp51(spine01)                   default          65014      65020      6/-/24       5d:23h:30m:50s
leaf04            swp52(spine02)                   default          65014      65020      6/-/24       5d:23h:30m:50s
spine01           swp1(leaf01)                     default          65020      65011      2/-/12       1d:23h:11m:24s
spine01           swp2(leaf02)                     default          65020      65012      2/-/12       1d:23h:11m:24s
spine01           swp3(leaf03)                     default          65020      65013      2/-/12       1d:23h:11m:24s
spine01           swp4(leaf04)                     default          65020      65014      2/-/11       1d:23h:11m:24s
spine02           swp1(leaf01)                     default          65020      65011      2/-/12       5d:23h:30m:50s
spine02           swp2(leaf02)                     default          65020      65012      2/-/12       5d:23h:30m:50s
spine02           swp3(leaf03)                     default          65020      65013      2/-/12       5d:23h:30m:50s
spine02           swp4(leaf04)                     default          65020      65014      2/-/11       5d:23h:30m:50s
View the changes made to all nodes running BGP
cumulus@ts:~$ netq show agents changes
Matching bgp records:
Hostname          Neighbor                     VRF              ASN        Peer ASN   PfxRx        DbState  Last Changed
----------------- ---------------------------- ---------------- ---------- ---------- ------------ -------- ----------------
spine01           swp4(leaf04)                 default          65020      65014      2/-/11       Add      1d:23h:58m:13s
spine01           swp3(leaf03)                 default          65020      65013      2/-/12       Add      1d:23h:58m:13s
spine01           swp2(leaf02)                 default          65020      65012      2/-/12       Add      1d:23h:58m:13s
spine01           swp1(leaf01)                 default          65020      65011      2/-/12       Add      1d:23h:58m:13s
leaf01            swp52(spine02)               default          65011      65020      5/-/23       Add      2d:15h:49m:18s
leaf01            swp51(spine01)               default          65011      65020      5/-/23       Add      2d:15h:49m:18s
spine02           swp4(leaf04)                 default          65020      65014      2/-/10       Add      6d:0h:17m:39s
spine02           swp4(leaf04)                 default          65020      65014      2/-/11       Add      6d:0h:17m:39s
spine02           swp3(leaf03)                 default          65020      65013      2/-/10       Add      6d:0h:17m:39s
spine02           swp3(leaf03)                 default          65020      65013      2/-/12       Add      6d:0h:17m:39s
spine02           swp2(leaf02)                 default          65020      65012      2/-/10       Add      6d:0h:17m:39s
spine02           swp2(leaf02)                 default          65020      65012      2/-/12       Add      6d:0h:17m:39s
spine02           swp1(leaf01)                 default          65020      65011      2/-/10       Add      6d:0h:17m:39s
spine02           swp1(leaf01)                 default          65020      65011      2/-/11       Add      6d:0h:17m:39s
spine02           swp1(leaf01)                 default          65020      65011      2/-/12       Add      6d:0h:17m:39s
spine01           swp4(leaf04)                 default          65020      65014      2/-/2        Add      6d:0h:17m:39s
spine01           swp4(leaf04)                 default          65020      65014      2/-/10       Add      6d:0h:17m:39s
spine01           swp4(leaf04)                 default          65020      65014      2/-/11       Add      6d:0h:17m:39s
spine01           swp3(leaf03)                 default          65020      65013      2/-/2        Add      6d:0h:17m:39s
spine01           swp3(leaf03)                 default          65020      65013      2/-/10       Add      6d:0h:17m:39s
spine01           swp3(leaf03)                 default          65020      65013      2/-/12       Add      6d:0h:17m:39s
spine01           swp2(leaf02)                 default          65020      65012      2/-/2        Add      6d:0h:17m:39s
spine01           swp2(leaf02)                 default          65020      65012      2/-/10       Add      6d:0h:17m:39s
spine01           swp2(leaf02)                 default          65020      65012      2/-/12       Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/2        Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/10       Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/11       Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/12       Add      6d:0h:17m:39s
leaf04            swp52(spine02)               default          65014      65020      6/-/20       Add      6d:0h:17m:39s
leaf04            swp52(spine02)               default          65014      65020      6/-/23       Add      6d:0h:17m:39s
leaf04            swp52(spine02)               default          65014      65020      6/-/24       Add      6d:0h:17m:39s
leaf04            swp51(spine01)               default          65014      65020      6/-/20       Add      6d:0h:17m:39s
leaf04            swp51(spine01)               default          65014      65020      6/-/23       Add      6d:0h:17m:39s
leaf04            swp51(spine01)               default          65014      65020      6/-/24       Add      6d:0h:17m:39s
leaf03            swp52(spine02)               default          65013      65020      5/-/20       Add      6d:0h:17m:39s
leaf03            swp52(spine02)               default          65013      65020      5/-/23       Add      6d:0h:17m:39s
leaf03            swp52(spine02)               default          65013      65020      5/-/24       Add      6d:0h:17m:39s
leaf03            swp51(spine01)               default          65013      65020      5/-/20       Add      6d:0h:17m:39s
leaf03            swp51(spine01)               default          65013      65020      5/-/23       Add      6d:0h:17m:39s
leaf03            swp51(spine01)               default          65013      65020      5/-/24       Add      6d:0h:17m:39s
leaf02            swp52(spine02)               default          65012      65020      6/-/4        Add      6d:0h:17m:39s
leaf02            swp52(spine02)               default          65012      65020      6/-/20       Add      6d:0h:17m:39s
leaf02            swp52(spine02)               default          65012      65020      6/-/23       Add      6d:0h:17m:39s
leaf02            swp51(spine01)               default          65012      65020      6/-/4        Add      6d:0h:17m:39s
leaf02            swp51(spine01)               default          65012      65020      6/-/20       Add      6d:0h:17m:39s
leaf02            swp51(spine01)               default          65012      65020      6/-/23       Add      6d:0h:17m:39s
leaf01            swp52(spine02)               default          65011      65020      5/-/4        Add      6d:0h:17m:39s
leaf01            swp52(spine02)               default          65011      65020      5/-/20       Add      6d:0h:17m:39s
leaf01            swp52(spine02)               default          65011      65020      5/-/23       Add      6d:0h:17m:39s
leaf01            swp51(spine01)               default          65011      65020      5/-/4        Add      6d:0h:17m:39s
leaf01            swp51(spine01)               default          65011      65020      5/-/20       Add      6d:0h:17m:39s
leaf01            swp51(spine01)               default          65011      65020      5/-/23       Add      6d:0h:17m:39s
spine02           swp4(leaf04)                 default          65020      65014      2/-/2        Add      6d:0h:17m:40s
spine02           swp3(leaf03)                 default          65020      65013      2/-/2        Add      6d:0h:17m:40s
spine02           swp2(leaf02)                 default          65020      65012      2/-/2        Add      6d:0h:17m:40s
spine02           swp1(leaf01)                 default          65020      65011      2/-/2        Add      6d:0h:17m:40s
leaf04            swp52(spine02)               default          65014      65020      6/-/4        Add      6d:0h:17m:40s
leaf04            swp51(spine01)               default          65014      65020      6/-/4        Add      6d:0h:17m:40s
leaf03            swp52(spine02)               default          65013      65020      5/-/4        Add      6d:0h:17m:40s
leaf03            swp51(spine01)               default          65013      65020      5/-/4        Add      6d:0h:17m:40s
View status of nodes running BGP with particular ASN
cumulus@ts:~$ netq show bgp asn 65013
Matching bgp records:
Hostname          Neighbor                         VRF              ASN        Peer ASN   PfxRx        Last Changed
----------------- -------------------------------- ---------------- ---------- ---------- ------------ ----------------
leaf03            swp51(spine01)                   default          65013      65020      5/-/24       5d:23h:44m:57s
leaf03            swp52(spine02)                   default          65013      65020      5/-/24       5d:23h:44m:57s
View status of a specific node running BGP, and display the results in JSON format
cumulus@ts:~$ netq leaf02 show bgp json
{
    "bgp":[
        {
            "lastChanged":1526068547.0,
            "pfxrx":"6/-/23",
            "hostname":"leaf02",
            "peerAsn":65020,
            "vrf":"default",
            "neighbor":"swp51(spine01)",
            "asn":65012
        },
        {
            "lastChanged":1526068547.0,
            "pfxrx":"6/-/23",
            "hostname":"leaf02",
            "peerAsn":65020,
            "vrf":"default",
            "neighbor":"swp52(spine02)",
            "asn":65012
	}
    ],
    "truncatedResult":false
}
Related Commands
netq check bgp    

### netq show changes

Displays changes made to a specific node, identified by its name, IP address and/or VRF, in your network fabric. The output provides:
xxx 
xxx
This command gives you an easy way to see [xxx]
Syntax
 netq [<hostname>] show changes 
		[<ipv4>|<ipv6>|<ipv4> vrf <vrf>|<ipv6> vrf <vrf>|vrf <vrf>]
		between <text-time> and <text-endtime> 
		[json]
Required Arguments	
Between <text-time> and <text-endtime>
Indicates the time frame for which you want to view changes. [explain how this works--which variable is the more recent time???]
Optional Arguments
hostname
Text used to identify a particular node in your network fabric; for example, leaf01 or swp3.
<ipv4>
Display changes made to node with specified IP version 4 address. Do not indicate mask address.
<ipv6>
Display changes made to node with specified IP version 6 address. Do not indicate mask address.
vrf (default|mgmt)
For nodes using VRF, indicate whether to use the default routing table or the management routing table. 
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
View status of all nodes with NetQ Agent installed
cumulus@ts:~$ netq show agents 
Matching agents records:


cumulus@switch:~$ netq show 
    changes     :  How this infomation has changed with time
    clag        :  Cumulus Multi-chassis LAG
    docker      :  Docker Info
    evpn        :  EVPN
    interfaces  :  network interface port
    inventory   :  Inventory information
    ip          :  IPv4 related info
    ipv6        :  IPv6 related info
    kubernetes  :  Kubernetes Information
    lldp        :  LLDP based neighbor info
    lnv         :  Lightweight Network Virtualization info
    macs        :  Mac table or MAC address info
    ntp         :  NTP
    ospf        :  OSPF info
    sensors     :  Temperature/Fan/PSU sensors
    services    :  System services
    vlan        :  VLAN
    vxlan       :  VXLAN data path

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

   netq check clag [around <text-time>] [json]
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

   netq check vlan [unverified] [around <text-time>] [json]
   netq [<hostname>] show vlan [<1-4096>] [around <text-time>] [json]
   netq [<hostname>] show vlan [<1-4096>] changes [between <text-time> and <text-endtime>] [json]

   netq check bgp [vrf <vrf>] [around <text-time>] [json]
   netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] [around <text-time>] [json]
   netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]

   netq check mtu [unverified] [around <text-time>] [json]
   netq check ospf [around <text-time>] [json]
   netq [<hostname>] show ospf [<remote-interface>] [area <area-id>] [around <text-time>] [json]
   netq [<hostname>] show ospf [<remote-interface>] [area <area-id>] changes [between <text-time> and <text-endtime>] [json]

Options:
   all                          : Information about all sub components
   around                       : Go back in time to around ...
   between                      : Specify start and end times for output desired
   config                       : Configure NetQ
   count                        : Count of matching entries
   example                      : Show examples of usage and workflow
   help                         : Show usage info
   ip                           : IPv4 related info
   ipv6                         : IPv6 related info
   json                         : Provide output in JSON
   list                         : Show all help commands
   notifier                     : Start/Stop/Restart/Query status of netq notifier
   origin                       : Owner of route or mac
   show                         : Show fabric-wide info about specified object
   verbose                      : More help on help
   <example>                    : name of example
   <hostname>                   : Name of the remote node you want to query
   <ip-server>                  : IP address of DB server
   <ipv4>                       : IPv4 address (no mask)
   <ipv6>                       : IPv6 address (no mask)
   <ip>                         : IPv4 or v6 address (no mask)
   <ipv4/prefixlen>             : IPv4 address with mask
   <ipv6/prefixlen>             : IPv6 address with mask
   <ip/prefixlen>               : IPv4 or IPv6 address with mask
   <mac>                        : MAC address
   <role>                       : Docker Swarm Node Role (worker, master)
   <text-time>                  : Time string such as 10m, 30s, 1h
   <text-endtime>               : Time string such as 10m, 30s, 1h
   <vrf>                        : Backend VRF
   <text-vlan>                  : VLAN

   resolve                      : Annotate input with names and interesting info

   trace                        : Control plane trace path across fabric
   from                         : Starting node or IP
   vlan                         : VLAN
   vrf                          : VRF
   <ip-src>                     : Source IP address used in trace
   <1-4096>                     : VLAN number range
   <vrf>                        : Name of VRF
   <mac>                        : MAC address
   <src-hostname>               : Hostname of source node for trace

   adjacent                     : Adjacent to the node
   container                    : Container information
   docker                       : Docker Info
   image                        : Container image name
   portmap                      : Check docker container exposed ports
   name                         : Container
   network                      : Container network information
   service                      : Docker Service
   <container-id>               : Container Id
   <container-image>            : Container image name
   <container-name>             : Container Name
   <network-name>               : Network name
   <port>                       : L4 Port
   <proto>                      : IP Protocol
   <remote-physical-interface>  : Name of the physical interface on the remote node
   <swarm-service-name>         : Name of Docker Swarm service

   docker                       : Docker Info
   summary                      : Summary of container info
   <docker-version>             : Docker engine version

    docker-monitor              : Monitor docker containers
    poll-period                 : Poll period in seconds (default is 15 seconds)
    <text-duration-period>      : Number of seconds for poll period between 10-120 seconds, inclusive

   brief                        : Summary information
   docker                       : Docker Info
   driver                       : Docker network driver
   name                         : Network name
   network                      : Network information
   <network-name>               : Docker Network Name
   <network-driver>             : Network Driver Name

   docker                       : Docker Info
   service                      : Service Info
   impact                       : Impact due to node outage
   connectivity                 : Connectivity graph
   mode                         : Docker service mode
   name                         : Swarm service
   <swarm-service-name>         : Name of the swarm service
   <mode>                       : Name of swarm service mode
   cluster                      : Server Cluster
   docker                       : Docker Info
   network                      : Network information
   mode                         : Docker service mode
   node                         : Compute node
   node-name                    : Docker Swarm node name
   role                         : Cluster node role
   swarm                        : Docker Swarm
   <cluster-name>               : Cluster name
   <cluster-node>               : Docker Swarm cluster node name
   <node-name>                  : Docker Swarm node name
   <role>                       : Cluster node role
   <swarm-service-name>         : Name of Docker Swarm service
   ntp                     : NTP
   out-of-sync             : NTP out of sync nodes
   in-sync                 : NTP in sync nodes
   active                       : Service is active
   error                        : Service has errors
   fail                         : Service has failed
   ok                           : Service is OK
   monitored                    : Service output is analyzed by NetQ
   services                     : System services
   warning                      : Service has warnings
   <service-name>               : Name of service

   addresses                    : IPv4/v6 addresses
   bond                         : Name of bond on device
   bridge                       : Name of bridge on device
   eth                          : ethX interface
   interfaces                   : network interface port
   loopback                     : Loopback interface
   macvlan                      : macvlan interface
   swp                          : swpX interface
   vlan                         : VLAN
   vrf                          : VRF
   vxlan                        : VxLAN
   state                        : Interface State
   type                         : Network interface type (such as bond, bridge)
   <remote-interface>           : Name of the interface on the remote node
   <remote-physical-interface>  : Name of the physical intf on the remote node
   <remote-interface-state>     : Interface State
   neighbors                    : IP neighbor info (ARP/ND)

   routes                       : IPv4/v6 routes
   empty                        : Empty Physical Interface
   module                       : Interface Module Info
   physical                     : Physical Interfaces
   plugged                      : Plugged Physical Interface
   peer                         : Peer Physical Interface
   and                          : Specify Peer Physical Interface
   model                        : Interface Module Model
   vendor                       : Interface Module Vendor
   <module-vendor>              : Interface Module Vendor
   <module-model>               : Interface Module Model
   <physical-port>              : Physical Interface name
   <physical-hostname>          : Hostname
   <peer-physical-hostname>     : Peer Hostname
   <peer-physical-port>         : Peer Physical Interface

   arch                         : CPU Architecture
   asic                         : Network Processor
   board                        : Switch Board
   brief                        : Brief summary
   cpu                          : Management Processor
   cumulus                      : Cumulus Linux
   disk                         : Storage Disk
   inventory                    : Inventory information
   license                      : License information
   memory                       : Hardware RAM
   model                        : Model
   model-id                     : Model ID
   name                         : Name of disk or OS
   os                           : Operating System
   transport                    : Disk Transport
   type                         : Memory type
   vendor                       : Vendor
   version                      : Version
   <asic-vendor>                : Network ASIC Vendor
   <asic-model>                 : Network ASIC Model
   <asic-model-id>              : Network ASIC Model ID
   <board-vendor>               : Board Vendor
   <board-model>                : Board Model
   <cpu-arch>                   : CPU Architecture
   <disk-name>                  : Disk Name
   <disk-transport>             : Disk Transport
   <disk-vendor>                : Disk Vendor
   <inventory-search>           : Search inventory for e.g., dell, trident2, x86, qsfp28, ddr3
   <memory-type>                : Memory Type info
   <memory-vendor>              : Memory Vendor
   <os-version>                 : Operating System version
   <os-name>                    : Operating System name

   fan                          : Fan sensor
   psu                          : Power supply sensor
   sensors                      : Temperature/Fan/PSU sensors
   temp                         : Temperature sensor
   <fan-name>                   : Fan sensor name
   <psu-name>                   : Power supply sensor name
   <temp-name>                  : Temperature sensor name

   vni                          : Virtual Network Id (or Vxlan ID)
   <text-vni>                   : VNI number to query
   evpn                         : EVPN

   check                        : Perform fabric-wide checks
   lnv                          : Lightweight Network Virtualization info
   check                        : Perform fabric-wide checks
   vxlan                        : VXLAN data path

   agents                       : Netq agent

   changes                      : How this infomation has changed with time

   add                          : Add feature
   del                          : Delete or remove feature
   experimental                 : Experimental features
   addons                       : Custom or user-specified features
   config                       : Configuration of NetQ
   reload                       : Reload configuration
   parser                       : Command parser
   stats                        : Start pushing interface metrics(experimental)
   add                          : Add netq server configuration
   del                          : Delete or remove netq server configuration
   server                       : Backend DB server
   show                         : Display current netq server configuration
   <ip-master>                  : Master data node for cluster
   <ip-replica>                 : IP address of replica server node
   <ip-server>                  : IP address of backend NetQ server_addr
   <text-server-name>           : Hostname of backend NetQ server
   <1025-65535>                 : TCP port of backend NetQ server
   <text-vrf>                   : VRF info
   agent                        : Troubleshooting daemon
   restart                      : Restart daemon
   start                        : Start daemon
   stop                         : Stop daemon
   status                       : Display daemon status
   debug                        : Debug-level
   info                         : Informational (default)
   warning                      : Warning conditions
   error                        : Error conditions
   loglevel                     : Daemon logging information
   docker-monitor               : Monitor docker containers
   kubernetes-monitor           : Monitor kubernetes events


   find-duplicates              : Find Duplicate IP or MAC
   find-origin                  : Find Origin of Route/MAC
   ha-setup                     : High Availability Setup
   query                        : Query using SQL-like NetQ Query Language
   regexp                       : Using Regular Expressions
   startup                      : NetQ Quickstart
   stats                        : Enable Gathering Interface Statistics
   trace                        : Control Path Trace
   resolve macs                 : Annotate MAC entries
   resolve routes               : Annotate your routing output
   check bgp                    : Check BGP Status Across the Fabric
   check clag                   : Check CLAG Status Across the Fabric
   check mtu                    : Check MTU Consistency Across the Fabric   restart                      : Restart daemon
   start                        : Start daemon
   stop                         : Stop daemon
   status                       : Display daemon status
   add                          : Add netq server/notifier configuration
   del                          : Delete netq notifier configuration
   notifier                     : Netq notifier integration
   loglevel                     : Daemon logging information
   integration                  : Integration with other notification systems
   filter                       : Filter the output before notifying integration
   severity                     : Optional Severity for notification (default is info)
   tag                          : Tag included with notification
   slack                        : Integration type for Slack
   pagerduty                    : Integration type for Pager Duty
   before                       : Position the object before the named object
   webhook                      : Slack integrations use a webhook URL to post messages
   output                       : Send the Notification to the named Integrator
   debug                        : Service has debugs
   info                         : Service has info
   warning                      : Service has warnings
   error                        : Service has errors
   rule                         : Define a filter object and regex match string
   after                        : Position the object after the named object
   api-access-key               : Pager Duty API Access Key
   api-integration-key          : Pager Duty Integration Key
   BgpSession                   : When BGP session state changes
   ClagSession                  : When CLAG role, peer role, peer state changes
   LnvSession                   : When Lnv session state changes
   Link                         : Notify when link oper_state changes
   Port                         : Notify when port is empty, plugged
   Services                     : When active service state changes
   OS                           : Notify when OS version changes
   Temp                         : Notify when sensor s_state changes
   Fan                          : Notify when sensor s_state changes
   PSU                          : Notify when sensor s_state changes
   License                      : Notify when license state changes
   <text-filter-name>           : Name of the filter
   <text-filter-name-anchor>    : Filter name used for inserting new filter
   <text-notifier-name>         : Textual name for notifier integration or filter
   <text-rule-key>              : Textual filter key
   <text-rule-value>            : Regular Expression used to filter based on key
   <text-webhook-url>           : Webhook URL used to direct Slack notifications
   <text-slack-tag>             : Optional Tag to include with Slack notifications
   <text-api-access-key>        : Value for Pager Duty API Access Key
   <text-api-integration-key>   : Value of Pager Duty Integration Key

   add                          : Add netq server/notifier configuration
   reset-cluster                : Reset DB cluster to force into known state
   server                       : Backend DB server
   show                         : Display current netq server configuration
   ts                           : Telemetry server
   <ip-master>                  : Master data node for cluster
   <ip-replica>                 : IP address of replica server node
   <ip-server>                  : IP address of backend NetQ server_addr
   <text-server-name>           : Hostname of backend NetQ server
   decommission                 : Decommission a node
   purge                        : Purge all the information from the DB
   <hostname-to-purge>          : Name of node whose info needs to be purged
   cluster                      : Server Cluster
   components                   : Compute Node components
   deployment                   : Pod Deployment
   kubernetes                   : Kubernetes Information
   node                         : Compute Node
   label                        : Kubernetes node
   <kube-cluster-name>          : Cluster name
   <kube-node-name>             : Kubernetes node name
    kubernetes-monitor          : Monitor kubernetes events
    poll-period                 : Poll period in seconds (default is 15 seconds)
    <text-duration-period>      : Number of seconds for poll period between 10-120 seconds, inclusive
   daemon-set                   : Daemon Set
   <kube-ds-name>               : Kubernetes Daemon Set name
   <kube-ds-label>              : Kubernetes Daemon Set Label
   deployment                   : Pod Deployment
   <kube-deployment-label>      : Deployment label
   <kube-deployment-name>       : Kubernetes Replication Controller name
   name                         : Kubernetes pod
   namespace                    : Namespace
   pod                          : Pod (Container Group)
   pod-ip                       : Pod IP address
   <kube-node-name>             : Kubernetes Node Name
   <kube-pod-label>             : Kubernetes Pod Label
   <kube-pod-name>              : Kubernetes Pod name
   <namespace>                  : Namespace name
   <kube-pod-ipaddress>         : Kuberentes Pod IP address
   replication-controller       : Kubernetes Replication Controller
   replica-set                  : Kubernetes Replica Set
   <kube-rc-name>               : Kubernetes Replication Controller name
   <kube-rs-name>               : Kubernetes Replica Set name
   <kube-rc-label>              : Kubernetes Replication Controller Label
   <kube-rs-label>              : Kubernetes Replication Set Label
    service-external-ip         : Kubernetes Service External IP
    service-cluster-ip          : Kubernetes Service Cluster IP
   <kube-service-label>         : Kubernetes Service Label
   <kube-service-name>          : Kubernetes Service name
   <kube-service-cluster-ip>    : Kubernetes Service Cluster IP
   <kube-service-external-ip>   : Kubernetes Service External IP
   deployment                   : Pod Deployment
   master                       : Master Node
   replica-set                  : Replica Set

   <kube-deployment-label>      : Deployment label
   <kube-deployment-name>       : Kubernetes Replication Controller name
   <kube-master-node>           : Kubernetes Master Node name
   <kube-rc-name>               : Kubernetes Replication Controller name
   <kube-rs-name>               : Kubernetes Replica Set name
   <kube-rc-label>              : Kubernetes Replication Controller Label
   <kube-rs-label>              : Kubernetes Replication Set Label
   <kube-service-label>         : Kubernetes service Label
   <kube-service-name>          : Kubernetes service name

   clag                         : Cumulus Multi-chassis LAG

   lldp                         : LLDP based neighbor info

   macs                         : Mac table or MAC address info
   egress-port                  : Outgoing interface
   <egress-port>                : Name of outgoing interface
   <0-4096>                     : VLAN ID
   <1-4096>                     : VLAN ID, between 1-4096


   stp                          : Spanning Tree
   topology                     : Active STP topology

   vlan                         : VLAN
   clag                         : Cumulus Multi-chassis LAG
   unverified                   : Show also the unverifiable interfaces

   bgp                          : BGP info
   asn                          : BGP Autonomous System Number (ASN)
   <bgp-session>                : BGP session (IP Address or interface name)
   <number-asn>                 : Specific ASN of interest

   mtu                          : Link MTU
   unverified                   : Show also the unverifiable interfaces

   ospf                         : OSPF info
   area                         : OSPF area
   <area-id>                    : Specific value of OSPF area


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
