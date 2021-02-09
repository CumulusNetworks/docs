---
title: C Commands
author: NVIDIA
weight: 1102
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---

This topic includes all commands that begin with `netq c*`, including all `netq check` and `netq config` commands.

**About Validation Commands**

There are three sets of validation commands, all for verifying the health and performance of network protocols and services:

- The original on-demand validation commands. These commands all begin with `netq check`. They are used to validate various elements in your network fabric at the current time or a time in the past. They allow filtering by hostname, can include or exclude selected tests, and some have additional options. The results are presented in the NetQ CLI immediately.
- The newer set of validation commands are used to create on-demand or scheduled validations with the results being displayed in the NetQ UI Validation Result cards. These commands begin with `netq add validation`. They are used to validate various elements in your network fabric currently or on a regular basis. No filtering on results is available within the commands as that is accomplished through the NetQ UI.
- The validation management commands. These present a list of all jobs and job settings, and the ability to remove validations.

Refer to {{<link title="Validation Checks">}} for a description of the tests run as part of each validation. The `netq check`commands are described here. The others are described elsewhere based on the command names.

**About Config Commands**

The `netq config` commands must be run with sudo privileges.

- - -

## netq check agents

Validates the communication status of all nodes (leafs, spines, and hosts) running the NetQ Agent in your network fabric. The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings

### Syntax

```
netq check agents
   [label <text-label-name> | hostnames <text-list-hostnames>]
   [include <agent-number-range-list> | exclude <agent-number-range-list>]
   [around <text-time>]
   [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames with to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

Basic validation: all devices, all tests, currently

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

Validation for selected devices

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

### Related Commands

- netq show agents
- netq show unit-tests agent
- netq add validation
- netq add validation name
- netq config agent

- - -

## netq check bgp

Validates that all configured route peering is established in your network fabric by looking for consistency across BGP sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state. If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Total number of BGP sessions at the specified time
- Number of sessions that have failed to establish a connection

### Syntax

```
netq check bgp
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [vrf <vrf>]
    [include <bgp-number-range-list> | exclude <bgp-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show bgp
- netq show unit-tests bgp
- netq add validation
- netq add validation name

- - -

## netq check cl-version

Verifies the Cumulus Linux version is consistent across nodes, matches a specified version, or is greater than or equal to a specified version, based on the options chosen.

### Syntax

```
netq check cl-version [label <text-label-name> | hostnames <text-list-hostnames>] [match-version <cl-ver> | min-version <cl-ver>] [include <version-number-range-list> | exclude <version-number-range-list>] [around <text-time>] [json | summary]
```

### Required Arguments

None

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show unit-tests cl-version

- - -

## netq check clag

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

### Syntax

```
netq check clag
    [label <text-label-name> | hostnames <text-list-hostnames> ]
    [include <clag-number-range-list> | exclude <clag-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show clag
- netq show unit-tests clag
- netq add validation
- netq add validation name

- - -

## netq check evpn

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

### Syntax

```
netq check evpn
    [mac-consistency]
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <evpn-number-range-list> | exclude <evpn-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 2.2.0 | Added `mac-consistency` option. Removed `hostname` and `vni` options. |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show evpn
- netq show unit-tests evpn
- netq add validation
- netq add validation name

- - -

## netq check interfaces

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

### Syntax

```
netq check interfaces
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <interface-number-range-list> | exclude <interface-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 2.1.0 | Removed host and peer options (`physical-hostname`, `physical-port`, `peer-physical-hostname`, `peer-physical-port`) and `unverified` option |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show interfaces
- netq show unit-tests interfaces
- netq add validation
- netq add validation name

- - -

## netq check license

Verifies license status for all nodes (leafs, spines, and hosts) in your network fabric. In particular, it looks for the validity of the Cumulus Linux license on each node.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of licenses validated
- Number of licenses that failed validation

### Syntax

```
netq check license
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <license-number-range-list> | exclude <license-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show unit-tests license
- netq add validation
- netq add validation name

- - -

## netq check mlag

Verifies MLAG session consistency by identifying all MLAG peers with errors or misconfigurations in the NetQ domain. In particular, it looks for such items as:

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

### Syntax

```
netq check mlag
    [label <text-label-name> | hostnames <text-list-hostnames> ]
    [include <mlag-number-range-list> | exclude <mlag-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

Basic validation: All devices, all tests, currently

```
cumulus@switch:~$ netq check mlag
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
cumulus@switch:~$ netq check mlag hostnames leaf01,leaf02
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
cumulus@switch:~$ netq check mlag exclude 2
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

### Related Commands

- netq show mlag
- netq show unit-tests mlag
- netq add validation
- netq add validation name

- - -

## netq check mtu

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

### Syntax

```
netq check mtu
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [unverified]
    [include <mtu-number-range-list> | exclude <mtu-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show unit-tests mtu
- netq add validation
- netq add validation name

- - -

## netq check ntp

Verifies network time synchronization using NTP for all nodes (leafs, spines, and hosts) in your network fabric. Nodes that are not in time synchronization with the NetQ appliance or VM may report data with an incorrect timestamp or lose communication altogether.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of nodes found that are unknown to NetQ
- Number of NTP servers available for synchronization

### Syntax

```
netq check ntp [label <text-label-name> | hostnames <text-list-hostnames>] [include <ntp-number-range-list> | exclude <ntp-number-range-list>] [around <text-time>] [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show ntp
- netq show unit-tests ntp
- netq add validation
- netq add validation name

- - -

## netq check ospf

Validates that all configured route peering is established in your network fabric by looking for consistency across OSPF sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation (reporting session failures)
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of nodes with failed adjacencies
- Total number of adjacencies

### Syntax

```
netq check ospf
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <ospf-number-range-list> | exclude <ospf-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show ospf
- netq show unit-tests ospf
- netq add validation
- netq add validation name

- - -

## netq check sensors

Verifies the status of temperature, cooling fan, and power supply sensors for all nodes in your network fabric.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Number of sensors validated
- Number of sensors that failed validation

### Syntax

```
netq check sensors
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <sensors-number-range-list> | exclude <sensors-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show sensors
- netq show unit-tests sensors
- netq add validation
- netq add validation name

- - -

## netq check vlan

Verifies consistency of the virtual local area network (VLAN) nodes and interfaces across all links in your network fabric. In particular, it looks for link neighbor and MLAG bond consistency. You can also identify nodes without peers.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings
- Total number of links found
- Number of links that failed validation

### Syntax

```
netq check vlan
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [unverified]
    [include <vlan-number-range-list> | exclude <vlan-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show vlan
- netq show unit-tests vlan
- netq add validation
- netq add validation name

- - -

## netq check vxlan

Verifies consistency of the virtual extensible local area network (VXLAN) nodes and interfaces across all links in your network fabric. In particular, it looks for consistent VXLAN configuration and BUM replication errors.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have not been heard from in 90 seconds (rotten)
- Number of nodes with warnings

### Syntax

```
netq check vxlan
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [include <vxlan-number-range-list> | exclude <vxlan-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. The value is written using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Added `hostnames` option |
| 2.4.0 | Added `include` and `exclude` options; output changed to include individual test status |
| 1.x | Introduced |

### Sample Usage

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

### Related Commands

- netq show vxlan
- netq show unit-tests vxlan
- netq add validation
- netq add validation name

- - -

## netq config add agent cluster-servers

Configures the server cluster where the NetQ Agents on monitored switches and hosts should send their collected data. You can also provide a specific port or VRF to use for the communication. Note that you must restart the NetQ Agent for the configuration to be enabled.

### Syntax

```
netq config add agent cluster-servers
    <text-opta-ip-list>
    [port <text-opta-port>]
    [vrf <text-vrf-name>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-opta-ip-list\> | Comma-separated list (no spaces) of IP addresses or hostnames of switches to include in server cluster |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| port | \<text-opta-port\> | Use the port with this name on each switch to receive data; default is port 31980 |
| vrf | \<text-vrf-names\> | Use the VRF with this name on each switch to receive data; default VRF is *default* |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

Configure cluster with default port and VRF

```
cumulus@switch:~$ netq config add agent cluster-servers leaf01,leaf02,spine01
Updated agent for cluster servers leaf01,leaf02,spine01 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config del agent cluster-servers

- - -

## netq config add agent command

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. This command lets you fine tune which events the agent can poll and vary the frequency of polling.

Refer to the {{<link title="Manage NetQ Agents/#change-netq-agent-polling-data-and-frequency" text="NetQ User Guide">}} for details of the commands, including their service keys and default polling intervals.

### Syntax

```
netq config add agent command
    service-key <text-service-key-anchor>
    [poll-period <text-cmd-periodicity>]
    [command <text-cmd-text>]
    [enable True | enable False]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| service-key | \<text-service-key-anchor\> | Modify the NetQ Agent command with this service key (name) |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| poll-period | \<text-cmd-periodicity\> | Set the polling period for the NetQ Agent command with the designated service key |
| command | \<text-cmd-text\> | Run this executable command for the NetQ Agent command with the designated service key |
| enable | True, False | Enable (True) or disable (False) the NetQ Agent command with the designated service key |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced |

### Sample Usage

Modify polling frequency for a command

```
cumulus@switch:~$ netq config add agent command service-key lldp-json poll-period 60
Successfully added/modified Command service lldpd command /usr/sbin/lldpctl -f json
```

Disable a command

```
cumulus@switch:~$ netq config add agent command service-key ospf-neighbor-json enable False
Command Service ospf-neighbor-json is disabled
```

### Related Commands

- netq config show agent commands
- netq config agent factory-reset commands

- - -

## netq config add agent cpu-limit

Configures the NetQ Agent use no more than a specified maximum percentage (between 40 and 60 percent) of the CPU resources of the switch. If the command is run without a value, NetQ assumes a limit of 40%. Cumulus Linux versions 3.6 or later or 4.1.0 or later must be running on the switch for this setting to take effect.

For more detail about this feature, refer to this {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches/" text="Knowledge Base">}} article.

### Syntax

```
netq config add agent cpu-limit
    [<text-limit-number>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-limit-number\> | Set the threshold for the maximum percentage of CPU resource that the NetQ Agent is allowed to use |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

Set CPU usage limit by NetQ Agent to 60 percent

```
cumulus@switch:~$ netq config add agent cpu-limit 60
Successfully set agent CPU limit to 60
Please restart agent(netq config restart agent)
'netq-agent'
cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent cpu-limit
- netq config del agent cpu-limit
- netq config (start|stop|status|restart) agent

- - -

## netq config add agent frr-monitor

Configures the NetQ Agent to monitor the Free Range Router (FRR) function on the switch.

### Syntax

```
netq config add agent frr-monitor
    [<text-frr-docker-name>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-frr-docker-name\> | Collect statistics about the FRR docker container with this name |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

Configure NetQ Agent to collect FRR statistics

```
cumulus@switch:~$ netq config add agent frr-monitor frr
Successfully added FRR docker monitoring for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent frr-monitor
- netq config del agent frr-monitor
- netq config (start|stop|status|restart) agent

- - -

## netq config add agent kubernetes-monitor

Configures the NetQ Agent to monitor kubernetes containers on the switch and to set how often to collect this information (between 10 and 120 seconds).

### Syntax

```
netq config add agent kubernetes-monitor
    [poll-period <text-duration-period>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| poll-period | \<text-duration-period\> | Collect statistics about kubernetes containers at this frequency, in seconds |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

Configure NetQ Agent to monitor kubernetes containers

```
cumulus@switch:~$ netq config add agent kubernetes-monitor
Successfully added kubernetes monitor. Please restart netq-agent.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

Configure the polling frequency for kubernetes container data collection

```
cumulus@switch:~$ netq config add agent kubernetes-monitor poll-period 120
Successfully added kubernetes monitor. Please restart netq-agent.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent kubernetes-monitor
- netq config del agent kubernetes-monitor
- netq config (start|stop|status|restart) agent

- - -

## netq config add agent loglevel

Configures the amount of information to log about the NetQ Agent activity, from only critical issues to every available message. Identified issues are logged to */var/log/netq-agent.log* file. The default log level is *info*.

- Error: Logs only events classified as errors
- Warning: Logs events classified as warnings and errors
- Info: Logs events classified as info, warning, and errors
- Debug: Logs all events

It is recommended to return a log level of info or higher after you have completed debugging.

### Syntax

```
netq config add agent loglevel
    [debug|error|info|warning]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | debug, error, info, warning | Log NetQ Agent events with this severity |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

Configure NetQ Agent to log only errors

```
cumulus@switch:~$ netq config add agent loglevel error
Successfully added logging for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent loglevel
- netq config del agent loglevel
- netq config (start|stop|status|restart) agent

- - -



netq config add agent server
    <text-opta-ip>
    [port <text-opta-port>]
    [vrf <text-vrf-name>]

netq config add agent (stats|sensors)

netq config add agent wjh 2.4.1

netq config add agent wjh-threshold
    (latency|congestion)
    <text-tc-list>
    <text-port-list>
    <text-th-hi>
    <text-th-lo>
3.2.0


### Related Commands

- netq config (start|stop|status|restart) agent
- netq config del agent
- netq config show agent

- - -

netq config agent factory-reset commands