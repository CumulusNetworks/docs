---
title: C Commands
author: NVIDIA
weight: 1102
toc: 3
right_toc_levels: 1
pdfhidden: true
---
<!-- vale NVIDIA.HeadingTitles = NO -->

This topic includes all commands that begin with `netq c*`, including all `netq check` and `netq config` commands.

**About Validation Commands**

Three sets of validation commands are available, all for verifying the health and performance of network protocols and services:

- The original on-demand validation commands. These commands all begin with `netq check`. You use them to validate various elements in your network fabric at the current time or a time in the past. They allow filtering by hostname, can include or exclude selected tests, and some have additional options. The results appear in the NetQ CLI immediately.
- Use the newer set of validation commands to create on-demand or scheduled validations with the results appearing in the NetQ UI Validation Result cards. These commands begin with `netq add validation`. You use them to validate various elements in your network fabric currently or on a regular basis. No filtering on results is available within the commands as you do that through the NetQ UI.
- The validation management commands. These present a list of all jobs and job settings, and the ability to remove validations.

Refer to {{<link title="Validation Checks">}} for a description of the tests run as part of each validation. This topic describes the `netq check` commands, with the others described elsewhere based on the command names.

**About Config Commands**

You must run the `netq config` commands with sudo privileges.

- - -

## netq check agents

Validates the communication status of all nodes (leafs, spines, and hosts) running the NetQ Agent in your network fabric. The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings

### Syntax

```
netq check agents
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
    [include <agents-number-range-list> | exclude <agents-number-range-list>]
    [around <text-time>]
    [streaming]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames with to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
## netq check bgp

Validates that all configured route peering is established in your network fabric by looking for consistency across BGP sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state. If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.
<!-- vale on -->

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Total number of BGP sessions at the specified time
- Number of sessions that have failed to establish a connection

### Syntax

```
netq check bgp
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [vrf <vrf>]
    [check_filter_id <text-check-filter-id>]
    [include <bgp-number-range-list> | exclude <bgp-number-range-list>]
    [around <text-time>]
    [streaming]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| vrf | \<vrf\> | When you configure a VRF, the accepted values include: <ul><li>default: use the default routing table</li><li> mgmt: use management routing table</li><li>\<custom\>: use user-defined routing table</li></ul> |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
- netq show bgp
- netq show unit-tests bgp
- netq add validation
- netq add validation name
<!-- vale on -->
- - -

<!-- vale off -->
## netq check cl-version
<!-- vale on -->

Verifies the Cumulus Linux version is consistent across nodes, matches a specified version, or is greater than or equal to a specified version, based on the options chosen.

### Syntax

```
netq check cl-version
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [match-version <cl-ver> | min-version <cl-ver>]
    [check_filter_id <text-check-filter-id>]
    [include <version-number-range-list> | exclude <version-number-range-list>]
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
| match-version | \<cl-ver\> | Identifies all switches with a Cumulus Linux version other than the one specified with this option. Specify `cl-ver` values in *x.y.z* format, for example 4.2.0.
| min-version | \<cl-ver\> | Identifies all switches with a Cumulus Linux version older than the one specified with this option. Specify `cl-ver` values in *x.y.z* format, for example 3.7.12. |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings

### Syntax

```
netq check clag
    [label <text-label-name> | hostnames <text-list-hostnames> ]
    [check_filter_id <text-check-filter-id>]
    [include <clag-number-range-list> | exclude <clag-number-range-list>]
    [around <text-time>]
    [streaming]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
## netq check evpn
<!-- vale on -->
Verifies communication status for all nodes (leafs, spines, and hosts) running instances of Ethernet VPN (EVPN) in your network fabric. In particular, it looks for such items as:

- BGP and EVPN session establishment
- VNI type consistency
- VLAN consistency among participating devices
- VRF consistency among participating devices

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Total number of VNIs
- Number of failed BGP sessions
- Total number of sessions

### Syntax

```
netq check evpn
    [mac-consistency]
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
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
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
- netq show evpn
- netq show unit-tests evpn
- netq add validation
- netq add validation name
<!-- vale on -->
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
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Number of ports validated
- Number of ports that failed validation
- Number of unverified ports (no peer found for the node)

### Syntax

```
netq check interfaces
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
    [include <interface-number-range-list> | exclude <interface-number-range-list>]
    [around <text-time>]
    [streaming]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings

### Syntax

```
netq check mlag
    [label <text-label-name> | hostnames <text-list-hostnames> ]
    [check_filter_id <text-check-filter-id>]
    [include <mlag-number-range-list> | exclude <mlag-number-range-list>]
    [around <text-time>]
    [streaming]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary informationand test results. Do not display details for tests that failed or had warnings.. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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

Verifies consistency of the maximum transmission unit (MTU) across all links in your network fabric. The command verifies the MTU consistency at the level appropriate to the specific type of link. For example, bond interfaces have their MTU enforced at the bond level and not at the individual slave level. For MLAG/CLAG bonds, verification confirms whether both ends of the bond have the same MTU value configured for their local instance of the bond. You can also view nodes without a peer link.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Number of links validated
- Number of links that failed validation
- Number of links that had warnings

### Syntax

```
netq check mtu
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [unverified]
    [check_filter_id <text-check-filter-id>]
    [include <mtu-number-range-list> | exclude <mtu-number-range-list>]
    [around <text-time>]
    [streaming]
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
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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

Verifies network time synchronization using NTP for all nodes (leafs, spines, and hosts) in your network fabric. Nodes that are not in time synchronization with the NetQ appliance or VM might report data with an incorrect timestamp or lose communication altogether.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Number of nodes found that are unknown to NetQ
- Number of NTP servers available for synchronization

### Syntax

```
netq check ntp
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
    [include <ntp-number-range-list> | exclude <ntp-number-range-list>]
    [around <text-time>]
    [streaming]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
## netq check ospf

Validates that all configured route peering is established in your network fabric by looking for consistency across OSPF sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state.
<!-- vale on -->

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation (reporting session failures)
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Number of nodes with failed adjacencies
- Total number of adjacencies

### Syntax

```
netq check ospf
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
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
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
- netq show ospf
- netq show unit-tests ospf
- netq add validation
- netq add validation name
<!-- vale on -->
- - -

## netq check sensors

Verifies the status of temperature, cooling fan, and power supply sensors for all nodes in your network fabric.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Number of sensors validated
- Number of sensors that failed validation

### Syntax

```
netq check sensors
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
    [include <sensors-number-range-list> | exclude <sensors-number-range-list>]
    [around <text-time>]
    [streaming]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| label | \<text-label-name\> | Reserved |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| streaming | NA | Perform a streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings
- Total number of links found
- Number of links that failed validation

### Syntax

```
netq check vlan
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [unverified]
    [check_filter_id <text-check-filter-id>] 
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
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
## netq check vxlan
<!-- vale on -->
Verifies consistency of the virtual extensible local area network (VXLAN) nodes and interfaces across all links in your network fabric. In particular, it looks for consistent VXLAN configuration and BUM replication errors.

The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings

### Syntax

```
netq check vxlan
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
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
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
<!-- vale off -->
- netq show vxlan
- netq show unit-tests vxlan
- netq add validation
- netq add validation name
<!-- vale on -->
- - -

<!-- vale off -->
## netq config add agent cluster-servers
<!-- vale on -->

Configures the server cluster where the NetQ Agents on monitored switches and hosts should send their collected data. You can also provide a specific port or VRF to use for the communication. Note that you must restart the NetQ Agent to enable the configuration.

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

A release appears here if there were changes to the command; otherwise it is not listed.

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
- netq config restart agent

- - -

## netq config add agent command

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. This command lets you fine tune which events the agent can poll and vary the frequency of polling. Note that you must restart the NetQ Agent to enable the configuration.

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

A release appears here if there were changes to the command; otherwise it is not listed.

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

Configures the NetQ Agent use no more than a specified maximum percentage (between 40 and 60 percent) of the CPU resources of the switch. If you run the command without a value, NetQ assumes a limit of 40%. Cumulus Linux versions 3.6 or later or 4.1.0 or later must be running on the switch for this setting to take effect. Note that you must restart the NetQ Agent to enable the configuration.

For more detail about this feature, refer to this [Knowledge Base]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}) article.

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
| NA | \<text-limit-number\> | Set the threshold for the maximum percentage of CPU resources that the NetQ Agent can use |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
- netq config restart agent

- - -

## netq config add agent frr-monitor

Configures the NetQ Agent to monitor the Free Range Router (FRR) function when running in a Docker container. Typically FRR runs as a service. Note that you must restart the NetQ Agent to enable the configuration.

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
| NA | \<text-frr-docker-name\> | Collect statistics about the FRR docker container with this name pattern, used by `grep` |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

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
- netq config restart agent

- - -

## netq config add agent kubernetes-monitor

Configures the NetQ Agent to monitor kubernetes containers on the switch and to set how often to collect this information (between 10 and 120 seconds). Note that you must restart the NetQ Agent to enable the configuration.

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

A release appears here if there were changes to the command; otherwise it is not listed.

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
- netq config restart agent

- - -

## netq config add agent loglevel

Configures the amount of information to log about the NetQ Agent activity, from only critical issues to every available message. Identified issues get logged to */var/log/netq-agent.log* file. The default log level is *info*.

- Error: Logs only events classified as errors
- Warning: Logs events classified as warnings and errors
- Info: Logs events classified as info, warning, and errors
- Debug: Logs all events

You should return a log level of info or higher after you finish debugging. Note that you must restart the NetQ Agent for to enable the configuration.

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

A release appears here if there were changes to the command; otherwise it is not listed.

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
- netq config restart agent

- - -

## netq config add agent opta-discovery-servers

Configures the range of IP addresses to search as part of the lifecycle management discovery process (when NetQ is looking for Cumulus Linux switches not running NetQ).

Ranges can be contiguous, for example *192.168.0.24-64*, or non-contiguous, for example *192.168.0.24-64,128-190,235*, but they must be within a single subnet. You can include a maximum of 50 addresses in an address range; if necessary, break the range into smaller ranges.

### Syntax

```
netq config add agent opta-discovery-servers 
    <text-opta-discovery-ips> 
    [vrf <text-vrf-name>]
    [port <text-discovery-server-port>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| opta-discovery-servers | \<text-opta-discovery-ips\> | Look for Cumulus Linux switches not running NetQ within this range of IP addresses |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| vrf | \<text-vrf-name\> | Look for Cumulus Linux switches with the specified IP addresses that use the VRF with this name. When unspecified, the command uses the *default* VRF. |
| port | \<text-discovery-server-port\> | Look for Cumulus Linux switches with the specified IP addresses that use this port. When unspecified, the command uses port 31980. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

### Sample Usage

Configure a range of IP addresses to search for switches without NetQ

```
cumulus@switch:~$ netq config add agent opta-discovery-servers 192.168.0.24-64,128-190
Updated agent discovery servers 192.168.0.24-64,128-190 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config restart agent

- - -

## netq config add agent sensors

Configures the NetQ Agent to collect information from the sensors on the switch chassis, including fan, power supply, and temperature data. You must run this command from the chassis.

### Syntax

```
netq config add agent sensors
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| sensors | NA | Collect information from all chassis sensors |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

Configure sensor monitoring

```
cumulus@chassis:~$ netq config add agent sensors
Successfully added sensors monitor. Please restart netq-agent (netq config restart agent)

cumulus@chassis:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent sensors
- netq config del agent sensors
- netq config restart agent

- - -

## netq config add agent server

Configures the destination (NetQ appliance or VM) for the data collected by the NetQ Agent and for API requests.

### Syntax

```
netq config add agent server
    <text-opta-ip>
    [port <text-opta-port>]
    [vrf <text-vrf-name>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server | \<text-opta-ip\> | Use the appliance or VM with this IP address to receive NetQ Agent data and API requests |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| port | \<text-opta-port\> | Use this port on the appliance or VM to receive NetQ Agent data and API requests |
| vrf | \<text-vrf-name\> | Use this VRF on the appliance or VM to receive NetQ Agent data and API requests |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

Configure destination server with default port and VRF

```
cumulus@switch:~$ netq config add agent server 192.168.200.250
Updated agent server 192.168.200.250 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config del agent server
- netq config restart agent

- - -

## netq config add agent stats

Configures the NetQ Agent to collect and send interface statistics.

### Syntax

```
netq config add agent stats
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| stats | NA | Collect and send interface statistics |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config add agent stats
stats config added. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent stats
- netq config del agent stats
- netq config restart agent

- - -

## netq config add agent wjh

Configures the NetQ Agent to collect and send What Just Happened events occurring on NVIDIA Spectrum&trade; switches. Refer to the {{<link title="WJH Event Messages Reference" text="WJH events reference">}} for a list of supported WJH events and to {{<link title="Configure and Monitor What Just Happened" text="WJH configuration">}} for configuration information.

### Syntax

```
netq config add agent wjh
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh | NA | Collect and send What Just Happened events |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

```
cumulus@chassis:~$ netq config add agent wjh
Successfully added WJH monitor. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config show agent wjh
- netq config del agent wjh
- netq config add agent wjh-drop-filter
- netq config add agent wjh-threshold
- netq config restart agent

- - -

## netq config add agent wjh-drop-filter

Filters the WJH events at the NetQ Agent before the NetQ system processes them. NetQ performs the filtering on a drop-type basis. You can filter the drop type further by specifying one or more drop reasons or severities. This command only applies to NVIDIA Spectrum switches.

### Syntax

```
netq config add agent wjh-drop-filter
    drop-type <text-wjh-drop-type> 
    [drop-reasons <text-wjh-drop-reasons>]
    [severity <text-drop-severity-list>]
```

### Required Arguments

<!-- vale off -->
| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-drop-filter | NA | Collect and send WJH events filtered by drop type, reason or severity |
| drop-type | \<text-wjh-drop-type\> | Only collect and send WJH events with this drop type. Valid drop types include *acl*, *buffer*, *l1*, *l2*, *router*, and *tunnel*. |
<!-- vale on -->

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| drop-reasons | \<text-wjh-drop-reasons\> | Only collect and send WJH events with these drop reasons. When you desire more than one drop reason, you should format this value as a comma-separated list, without spaces. Valid drop reasons vary according to the drop type. Refer to the {{<link title="WJH Event Messages Reference" text="WJH events reference">}}. |
| severity | \<text-drop-severity-list\> | Only collect and send WJH events with these severities. When you desire more than one severity, you should format this value as a comma-separated list, without spaces. Valid severities include *Notice*, *Warning*, and *Error*. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config add agent wjh-drop-filter drop-type l1 drop-reasons PORT_ADMIN_DOWN,BAD_SIGNAL_INTEGRITY

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config del agent wjh-drop-filter
- netq config add agent wjh
- netq config add agent wjh-threshold
- netq config restart agent

- - -

## netq config add agent wjh-threshold

WJH latency and congestion metrics depend on threshold settings to trigger the events. NetQ measures packet latency as the time spent inside a single system (switch). It measures congestion as a percentage of buffer occupancy on the switch. When configured, the NetQ Agent collects and sends these WJH triggered events when a metric crosses the high and low thresholds.

This command only applies to NVIDIA Spectrum switches.

### Syntax

```
netq config add agent wjh-threshold
    (latency|congestion)
    (<text-tc-list>|all)
    (<text-port-list>|all)
    <text-th-hi>
    <text-th-lo>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-threshold | NA | Collect and send WJH latency or congestion events triggered by the specified high and low thresholds |
| latency | NA | Collect and send WJH latency events |
| congestion | NA | Collect and send WJH congestion events |
| NA | \<text-tc-list\> or all | Only send events for these traffic classes, or use *all* for all traffic classes. When you desire more than one traffic class, you should format this value should as a comma-separated list, without spaces. |
| NA | \<text-port-list\> or all | Only send events occurring on these ports, or use *all* for all ports. When you desire more than one port, you should format this value as a comma-separated list, without spaces. For example *swp1,swp2,swp3,swp4*. |
| NA | \<text-th-hi\> | Trigger an event when the latency is greater than this amount of time, or when buffer occupancy is greater than this percentage. |
| NA | \<text-th-lo\> | Trigger an event when the latency is less than this amount of time, or when buffer occupancy is less than this percentage. |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

### Sample Usage

Create latency thresholds for Class *3* traffic on port *swp1* where the upper threshold is *10* and the lower threshold is *1*.

```
cumulus@switch:~$ sudo netq config add agent wjh-threshold latency 3 swp1 10 1
```

Create congestion thresholds for Class *4* traffic on port *swp1* where the upper threshold is *200* and the lower threshold is *10*.

```
cumulus@switch:~$ sudo netq config add agent wjh-threshold congestion 4 swp1 200 10
```

### Related Commands

- netq config show agent wjh-threshold
- netq config del agent wjh-threshold
- netq config add agent wjh
- netq config add agent wjh-drop-filter
- netq config restart agent

- - -
<!-- vale off -->
## netq config add cli server
<!-- vale on -->
Configures the NetQ CLI on the switch or host where you run this command. Cloud deployments require the `access-key` and `secret-key` options or the `cli-keys-file` option, as well as the `premises` option.

When the NetQ CLI is not configured, you can run only `netq config` and `netq help` commands, and you must use `sudo` to run them.

For additional configuration information, refer to the {{<link title="Install the NetQ System" text="NetQ User Guide">}}.

### Syntax

```
netq config add cli server
    <text-gateway-dest>
    [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>]
    [vrf <text-vrf-name>]
    [port <text-gateway-port>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server | \<text-gateway-dest\> | Hostname or IP address of the NetQ appliance or VM in on-premises deployments, or gateway IP address or domain name for cloud/remote deployments. |
| access-key | \<text-access-key\> | Access key obtained from NetQ UI for cloud/remote deployments |
| secret-key | \<text-secret-key\> | Secret key obtained from NetQ UI for cloud/remote deployments |
| premises | \<text-premises-name\> | Name of the premises with the data you want to monitor. When you have multiple premises, you must run this command again to view data from another premises. |
| <!-- vale off -->cli-keys-file<!-- vale on --> | \<text-key-file\> | Use the access and secret keys contained in this file for cloud/remote deployments, rather than providing keys individually. Value must include entire path to the file. |

### Options

| Argument | Value | Description |
| ---- | ---- | ---- |
| vrf | \<text-vrf-name\> | Use this VRF for communication with the telemetry server (NetQ appliance, VM, or cloud gateway). This should be the same VRF where you set the routing tables for connectivity to the telemetry server. Typically this is the management VRF. |
| port | \<text-gateway-port\> | Use this port for communication with the telemetry server (NetQ appliance, VM, or cloud gateway). The default port is 32708 for on-premises deployments and 443  for cloud deployments. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.3.1 | Dropped second form of command |
| 2.3.0 | Split command into two: the first for when you want to specify the premises (syntax as shown above), the second for when you want to use the first premises in your list of premises (same syntax minus the premises option). |
| 2.2.2 | Changed `premise` argument to `premises`. |
| 2.2.0 | Added `access-key`, `secret-key`, and `premise` as required arguments for cloud deployments. Added `vrf` and `port` options. |
| 2.1.x | Introduced |

### Sample Usage

On-premises

```
cumulus@switch:~$ sudo netq config add cli server 10.0.1.1 vrf mgmt port 32000
cumulus@switch:~$ sudo netq config restart cli
```

Cloud/remote

```
cumulus@switch:~# sudo netq config add cli server api.netq.cumulusnetworks.com access-key 45d11f46bc09986db64612c590204054b1f12bc05219324a7d66084cf741779c secret-key zHoQ9feNlScNuGBVzUNqr0c0kJL+FAZbhEz8YtW2Rc0= premises NewYork 
cumulus@switch:~# sudo netq config restart cli
```

### Related Commands
<!-- vale off -->
- netq config show cli
- netq config del cli server
- netq config restart cli
<!-- vale on -->
- - -

## netq config add color

<!-- vale off -->
Configures command output to presents results in color for many commands. Results with errors are shown in <span style="color: #ff0000;">red</span>, and warnings are shown in <span style="color: #ffcc00;">yellow</span>. Results without errors or warnings are shown in either black or <span style="color: #00ff00;">green</span>. VTEPs are shown in <span style="color: #0000ff;">blue</span>. A node in the *pretty* output of a trace command is shown in **bold**, and a router interface is wrapped in angle brackets (\< \>). Outputs are shown with color cues as soon as you run the command.
<!-- vale on -->

### Syntax

```
netq config add color
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| color | NA | Display command output using color |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config add color
Color coded output config added
```

### Related Commands

- netq config del color

- - -

## netq config agent factory-reset commands

Resets the factory default settings for NetQ Agent modular commands, removing any manual adjustments made to data to collect and polling frequency.

### Syntax

```
netq config agent factory-reset commands 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| factory-reset commands | NA | Reset NetQ Agent polling data and frequency to factory settings |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config agent factory-reset commands
Netq Command factory reset successful
```

### Related Commands

- netq config add agent command
- netq config show agent commands

- - -

## netq config del agent cluster-servers

For deployments using a cluster server configuration, this command removes the IP addresses of all cluster servers configured to receive NetQ Agent data.

### Syntax

```
netq config del agent cluster-servers
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cluster-servers | NA | Remove all cluster servers configured to receive NetQ Agent data |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent cluster-servers
Deleted agent cluster servers 10.10.0.101,10.20.0.101 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config add agent cluster-servers
- netq config restart agent

- - -

## netq config del agent cpu-limit

Removes the CPU usage limit for the NetQ Agent on this device.

### Syntax

```
netq config del agent cpu-limit
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cpu-limit | NA | Remove CPU usage limit for the NetQ Agent on this device |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent cpu-limit
Successfully deleted agent CPU limit
Please restart agent(netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent cpu-limit
- netq config add agent cpu-limit
- netq config restart agent

- - -

## netq config del agent frr-monitor

Disables NetQ Agent from monitoring FRR running in a Docker container. This *does not* disable NetQ Agent from monitoring FRR running as a service.

### Syntax

```
netq config del agent frr-monitor
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| frr-monitor | NA | Stop the NetQ Agent from monitoring FRR when running in a container |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent frr-monitor
Successfully deleted FRR docker monitoring for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent frr-monitor
- netq config add agent frr-monitor
- netq config restart agent

- - -

## netq config del agent kubernetes-monitor

Disables NetQ Agent from monitoring Kubernetes container activity on a switch.

### Syntax

```
netq config del agent kubernetes-monitor
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| kubernetes-monitor | NA | Stop the NetQ Agent from monitoring Kubernetes containers |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent kubernetes-monitor
Successfully deleted kubernetes monitoring for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent kubernetes-monitor
- netq config add agent kubernetes-monitor
- netq config restart agent

- - -

## netq config del agent loglevel

Disables NetQ Agent logging on a switch.

### Syntax

```
netq config del agent loglevel
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| loglevel | NA | Stops the NetQ Agent from logging events about the agent |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent loglevel
Successfully deleted logger for netq-agent. Please restart service.

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent loglevel
- netq config add agent loglevel
- netq config restart agent

- - -

## netq config del agent sensors

Disables NetQ Agent from collecting fan, power supply unit, and temperature sensors for a switch chassis.

### Syntax

```
netq config del agent sensors
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| sensors | NA | Stops the NetQ Agent from monitoring chassis sensors |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent sensors
cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config show agent sensors
- netq config add agent sensors
- netq config restart agent

- - -

## netq config del agent server

Removes the destination (NetQ appliance or VM) for the data collected by the NetQ Agent and for API requests.

### Syntax

```
netq config del agent server
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server | NA | Delete the current destination of NetQ Agent data and API requests |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent server
Deleted agent server 127.0.0.1 port 31980 vrf default. Please restart netq-agent (netq config restart agent)

cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config add agent server
- netq config restart agent

- - -

## netq config del agent stats

Disables the NetQ Agent from collecting interface statistics on a switch.

### Syntax

```
netq config del agent stats
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| stats | NA | Stop NetQ Agent from collecting interface statistics |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent stats
stats config deleted
```

### Related Commands

- netq config show agent stats
- netq config add agent stats
- netq config restart agent

- - -

## netq config del agent wjh

Disables the NetQ Agent from collecting What Just Happened events on a switch.

### Syntax

```
netq config del agent wjh
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh | NA | Stop NetQ Agent from collecting WJH information |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent wjh
cumulus@switch:~$ netq config restart agent
```

### Related Commands

- netq config del agent wjh
- netq config del agent wjh-threshold
- netq config show agent wjh
- netq config add agent wjh
- netq config restart agent

- - -

## netq config del agent wjh-drop-filter

Delete a What Just Happened event filter on a switch.

### Syntax

```
netq config del agent wjh-drop-filter
    drop-type <text-wjh-drop-type> 
    [drop-reasons <text-wjh-drop-reasons>]
    [severity <text-drop-severity-list>]
```

### Required Arguments

<!-- vale off -->
| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-drop-filter | NA | Delete existing WJH event filter |
| drop-type | \<text-wjh-drop-type\> | Delete WJH event filter with this drop type. Valid drop types include *acl*, *buffer*, *l1*, *l2*, *router*, and *tunnel*. |
<!-- vale on -->

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| drop-reasons | \<text-wjh-drop-reasons\> | Delete WJH event filter with these drop reasons. When you desire more than one drop reason, you should format this value as a comma-separated list, without spaces. Valid drop reasons vary according to the drop type. Refer to the {{<link title="WJH Event Messages Reference" text="WJH events reference">}}. |
| severity | \<text-drop-severity-list\> | Delete WJH event filter with these severities. When you desire more than one severity, you should format this value as a comma-separated list, without spaces. Valid severities include *Notice*, *Warning*, and *Error*. |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent wjh-drop-filter drop-type l1 drop-reasons PORT_ADMIN_DOWN,BAD_SIGNAL_INTEGRITY

cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!
```

### Related Commands

- netq config add agent wjh-drop-filter
- netq config add/del agent wjh
- netq config del agent wjh-threshold
- netq config restart agent

- - -

## netq config del agent wjh-threshold

Remove latency or congestion thresholds for WJH events.

### Syntax

```
netq config del agent wjh-threshold
    (latency|congestion)
    (<text-tc-list>|all)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-threshold | NA | Remove latency or congestion events triggered by thresholds |
| latency | NA | Remove latency event thresholds |
| congestion | NA | Remove congestion event thresholds |
| NA | \<text-tc-list\> or all | Remove latency or congestion events for these traffic classes, or use *all* for all traffic classes. When you desire more than one traffic class, you should format this value as a comma-separated list, without spaces. |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del agent wjh-threshold latency 3

cumulus@switch:~$ netq config del agent wjh-threshold congestion 4
```

### Related Commands

- netq config show agent wjh-threshold
- netq config add agent wjh-threshold
- netq config del agent wjh
- netq config del agent wjh-drop-filter
- netq config restart agent

- - -
<!-- vale off -->
## netq config del cli server
<!-- vale on -->
Removes the NetQ CLI configuration from a switch.

### Syntax

```
netq config del cli server
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| <!-- vale off -->cli server<!-- vale on --> | NA | Delete the current NetQ CLI configuration |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del cli server
```

### Related Commands
<!-- vale off -->
- netq config add cli server
- netq config show cli
- netq config restart agent
<!-- vale on -->
- - -

## netq config del color

Disables color cues in command output. This command takes effect immediately.

### Syntax

```
netq config del color
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| color | NA | Remove color from command outputs |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config del color
Color coded output config deleted
```

### Related Commands

- netq config add color

- - -

## netq config reload parser

Loads the NetQ configuration file.

### Syntax

```
netq config reload parser
```

### Required Arguments

None

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config reload parser
Parser reloaded
```

### Related Commands

None

- - -

## netq config restart

Restarts the NetQ Agent or CLI daemons on a switch. Use this command after making changes to the NetQ Agent or CLI configurations.

### Syntax

```
netq config restart agent

netq config restart cli
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| agent | NA | Restart the NetQ Agent daemon (`netq-agent`) |
| <!-- vale off -->cli <!-- vale on -->| NA | Restart the NetQ CLI daemon (`netq-cli`) |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config restart agent
Restarting netq-agent... Success!

cumulus@switch:~$ netq config restart cli 
Restarting NetQ CLI... Success!
```

### Related Commands

- netq config (start|stop) agent

- - -
<!-- vale off -->
## netq config select cli premise
<!-- vale on -->
In a multi-premises deployment, this command configures the NetQ CLI to view data from the given premises.

### Syntax

```
netq config select cli
    premise <text-premise>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| premise | \<text-premise\> | Show data from this premises in the NetQ CLI command outputs |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config select cli premise Boston
```

### Related Commands

None

- - -

## netq config show agent

Displays the configuration of the NetQ Agent on a switch.

### Syntax

```
netq config show agent
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

Standard output

```
cumulus@switch:~$ netq config show agent 
netq-agent             value      default
---------------------  ---------  ---------
exhibitport
exhibiturl
server                 127.0.0.1  127.0.0.1
cpu-limit              100        100
agenturl
enable-opta-discovery  False      False
agentport              8981       8981
port                   31980      31980
vrf                    default    default
()
```

JSON output

```
cumulus@switch:~$ netq config show agent json
{
    "defaults":{
        "agentport":8981,
        "agenturl":"",
        "cpu-limit":"100",
        "enable-opta-discovery":false,
        "exhibitport":"",
        "exhibiturl":"",
        "port":31980,
        "server":"127.0.0.1",
        "vrf":"default"
    },
    "netq-agent":{
        "agentport":8981,
        "cpu-limit":"100",
        "enable-opta-discovery":false,
        "frr_docker":false,
        "frr_docker_name":"",
        "opta-discovery-servers":"192.168.0.24-64,128-190",
        "port":31980,
        "server":"127.0.0.1",
        "stats":true,
        "vrf":"default"
    }
}
```

### Related Commands
<!-- vale off -->
- netq config show all
- netq config show cli
- netq config add agent
- netq config del agent
<!-- vale on -->
- - -

## netq config show agent commands

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. This command displays the configuration of these commands, including the definition of the commands, which are active, and how often they run. You can also filter by the service key to view a given command.

### Syntax

<!-- vale off -->
```
netq config show agent commands
    [service-key <text-service-key-anchor>]
    [json]
```
<!-- vale on -->

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| commands | NA | View the configuration of all NetQ Agent modular commands |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| service-key | \<text-service-key-anchor\> | View the configuration of the NetQ Agent command with this service key (name) |
| json | NA | View the configuration information for the specified NetQ Agent commands in JSON format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced |

### Sample Usage

Show configuration for all commands

```
cumulus@switch:~$ netq config show agent commands
 Service Key        Period    Active       Command
------------------  --------  --------  ---------------------------------------------------
ports               3600      yes       Netq Predefined Command
proc-net-dev        30        yes       Netq Predefined Command
agent_stats         300       yes       Netq Predefined Command
agent_util_stats    30        yes       Netq Predefined Command
ssd-util-json       86400     yes       /usr/sbin/smartctl -a /dev/sda
lldp-json           30        yes       /usr/sbin/lldpctl -f json
resource-util-json  30        yes       findmnt / -n -o FS-OPTIONS
os-release          N/A       yes       cat /etc/os-release
eprom               N/A       yes       /usr/cumulus/bin/decode-syseeprom -j
lscpu               N/A       yes       /usr/bin/lscpu
meminfo             N/A       yes       cat /proc/meminfo
lsblk               N/A       yes       lsblk -d -n -o name,size,type,vendor,tran,rev,model
dmicode             N/A       yes       dmidecode -t 17
is-opta             N/A       yes       cat /etc/app-release
```

Show configuration for specific command

```
cumulus@switch:~$ netq config show agent commands service-key agent_stats
 Service Key       Period  Active       Command
---------------  --------  --------  -----------------------
agent_stats           300  yes       Netq Predefined Command
```

### Related Commands

- netq config add agent commands
- netq config agent factory-reset commands

- - -

<!-- vale off -->
## netq config show agent cpu-limit
<!-- vale on -->

Displays the maximum percentage of CPU resources of the switch that a NetQ Agent might use. When restricted by the `netq config add agent cpu-limit` command, the value is between 40 and 60 percent.

For more detail about this feature, refer to this [Knowledge Base]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}) article.

### Syntax

```
netq config show agent cpu-limit
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cpu-limit | NA | View the maximum percentage of CPU resource that the NetQ Agent can use |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

Unlimited

```
cumulus@switch:~$ netq config show agent cpu-limit
CPU Limit
-----------
100%
()
```

Limited

```
cumulus@switch:~$ netq config show agent cpu-limit
CPU Limit
-----------
60%
()
```

### Related Commands

- netq config add agent cpu-limit
- netq config del agent cpu-limit

- - -

<!-- vale off -->
## netq config show agent frr-monitor
<!-- vale on -->

Displays the NetQ Agent Free Range Router (FRR) function monitoring configuration on a switch. If configured, FRR monitoring occurs on FRR running in a Docker container. If not configured, FRR is likely running as a service.

### Syntax

```
netq config show agent frr-monitor
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| frr-monitor | NA | Display FRR monitoring configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

With FRR running in a Docker container

```
cumulus@switch:~$ netq config show agent frr-monitor
FRR Docker Monitoring    FRR Docker Name
-----------------------  -----------------
true                     kube-system
()
```

With FRR running as a service

```
cumulus@switch:~$ netq config show agent frr-monitor
FRR Docker Monitoring    FRR Docker Name
-----------------------  -----------------
false
()

```

### Related Commands

- netq config add agent frr-monitor
- netq config del agent frr-monitor

- - -

<!-- vale off -->
## netq config show agent kubernetes-monitor

Displays the NetQ Agent Kubernetes monitoring configuration on a switch, included whether it is enabled and the polling period.
<!-- vale on -->

### Syntax

```
netq config show agent kubernetes-monitor
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| kubernetes-monitor | NA | Display the kubernetes monitoring configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config show agent kubernetes-monitor 
Monitor     Enabled      Poll Period
----------  ---------  -------------
kubernetes  true                 120
()
```

### Related Commands

- netq config add agent kubernetes-monitor
- netq config del agent kubernetes-monitor

- - -

## netq config show agent loglevel

Displays the amount of information logged about the NetQ Agent activity, from only critical issues to every available message. Identified issues get logged to the `/var/log/netq-agent.log` file. The default log level is *info*.

- Error: Logs only events classified as errors
- Warning: Logs events classified as warnings and errors
- Info: Logs events classified as info, warning, and errors
- Debug: Logs all events

### Syntax

```
netq config show agent loglevel
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| loglevel | NA | Display the NetQ Agent logging level configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

Configure NetQ Agent to log only errors

```
cumulus@switch:~$ netq config show agent loglevel 
Log Level
-----------
info
()
```

### Related Commands

- netq config add agent loglevel
- netq config del agent loglevel

- - -

## netq config show agent sensors

Displays the NetQ Agent sensors configuration on a chassis.

### Syntax

```
netq config show agent sensors
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| sensors | NA | Display NetQ Agent sensors configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

With sensor monitoring configured

```
cumulus@chassis:~$ netq config show agent sensors

```

Without sensor monitoring configured

```
cumulus@chassis:~$ netq config show agent sensors

```

### Related Commands

- netq config add agent sensors
- netq config del agent sensors

- - -

## netq config show agent stats

Displays whether you configured the NetQ Agent for interface statistics monitoring on a switch (true) or not (false).

### Syntax

```
netq config show agent stats
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| stats | NA | Display status of interface statistics |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

Standard output

```
cumulus@switch:~$ netq config show agent stats
Stats
-------
true
()
```

JSON-formatted output

```
cumulus@switch:~$ netq config show agent stats json
{
    "stats":true
}
```

### Related Commands

- netq config add agent stats
- netq config del agent stats

- - -

## netq config show agent wjh

Displays whether you configured the NetQ Agent for What Just Happened event monitoring on an NVIDIA Spectrum switch. Refer to {{<link title="Configure and Monitor What Just Happened" text="WJH configuration">}} for setting up WJH monitoring.

### Syntax

```
netq config show agent wjh
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh | NA | Display NetQ Agent What Just Happened monitoring configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

```
cumulus@chassis:~$ netq config show agent wjh
```

### Related Commands

- netq config add agent wjh
- netq config del agent wjh
- netq config show agent wjh-threshold

- - -

<!-- vale off -->
## netq config show agent wjh-threshold
<!-- vale on -->

Displays whether you configured the NetQ Agent with WJH latency and congestion thresholds on an NVIDIA Spectrum switch.

### Syntax

```
netq config show agent wjh-threshold
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| wjh-threshold | NA | Display NetQ Agent WJH latency and congestion thresholds configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config show agent wjh-threshold
```

### Related Commands

- netq config add agent wjh-threshold
- netq config del agent wjh-threshold
- netq config show agent wjh

- - -

## netq config show all

Displays the configuration of the NetQ Agent and NetQ CLI on a switch.

### Syntax

```
netq config show all
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config show all 
netq-agent             value      default
---------------------  ---------  ---------
exhibitport
exhibiturl
server                 127.0.0.1  127.0.0.1
cpu-limit              100        100
agenturl
enable-opta-discovery  False      False
agentport              8981       8981
port                   31980      31980
vrf                    default    default
()
netq-cli     value            default
-----------  ---------------  ---------
server       192.168.200.250  127.0.0.1
netq-user
premises     0
port         32708            32708
count        2000             2000
vrf          default          default
api-logging  False            False
()
```

### Related Commands
<!-- vale off -->
- netq config show agent
- netq config show cli
<!-- vale on -->
- - -
<!-- vale off -->
## netq config show cli
<!-- vale on -->
Displays the configuration of the NetQ CLI on a switch.

### Syntax

```
netq config show cli
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config show cli
netq-cli     value            default
-----------  ---------------  ---------
server       192.168.200.250  127.0.0.1
netq-user
premises     0
port         32708            32708
count        2000             2000
vrf          default          default
api-logging  False            False
()
```

### Related Commands

- netq config show agent
- netq config show all

- - -

## netq config start agent

Starts the NetQ Agent on a switch.

### Syntax

```
netq config start agent
```

### Required Arguments

None

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config start agent 
Starting netq-agent... Success!
```

### Related Commands

- netq config show agent
- netq config stop agent
- netq config restart agent

- - -

## netq config status agent

Displays the operational status of the NetQ Agent on a switch.

### Syntax

```
netq config status agent
```

### Required Arguments

None

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config status agent 
netq-agent... Running

cumulus@switch:~$ netq config status agent 
netq-agent...stopped

```

### Related Commands

- netq config show agent
- netq config stop agent
- netq config restart agent

- - -
<!-- vale off -->
## netq config status cli
<!-- vale on -->
Displays the operational status of the NetQ CLI on a switch.

### Syntax

```
netq config status cli
```

### Required Arguments

None

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config status cli
NetQ CLI... Running

```

### Related Commands
<!-- vale off -->
- netq config show cli
- netq config restart cli
<!-- vale on -->
- - -

## netq config stop agent

Stops the NetQ Agent on a switch.

### Syntax

```
netq config stop agent
```

### Required Arguments

None

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq config stop agent
Stopping netq-agent... Success!
```

### Related Commands

- netq config show agent
- netq config start agent
- netq config restart agent

- - -
<!-- vale NVIDIA.HeadingTitles = YES -->