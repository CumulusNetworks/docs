---
title: check
author: NVIDIA
weight: 1102
toc: 3
right_toc_levels: 1
pdfhidden: true
---
<!-- vale NVIDIA.HeadingTitles = NO -->

Three sets of validation commands are available, all for verifying the health and performance of network protocols and services:

- `netq check` commands. These commands validate various elements in your network fabric. They allow filtering by hostname, can include or exclude selected tests, and some have additional options. The results appear in the NetQ CLI. Commands with a `streaming` option run streaming checks by default to return results faster. To run a non-streaming validation, include the `legacy` option.  
- `netq add validation` commands. Use {{<link url="add/#netq-add-validation-name" text="these commands">}} to validate various elements in your network fabric. The results appear in the Validation Result cards in the UI, where you can filter them.
- Validation management commands. `netq show validation settings` displays a list of all jobs and job settings and `netq del validation` allows you to remove validations.

Refer to {{<link title="Validation Checks">}} for a description of the tests run as part of each validation.

- - -
## netq check addresses

Searches for duplicate IPv4 and IPv6 addresses assigned to interfaces across devices in the inventory, and checks for duplicate /32 host routes in each VRF.

### Syntax

```
netq check addresses 
    [label <text-label-name> | hostnames <text-list-hostnames>] 
    [check_filter_id <text-check-filter-id>] 
    [include <addr-number-range-list> | exclude <addr-number-range-list>]
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
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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

### Related Commands
- ```netq show address-history```
- ```netq add validation```

## netq check agents

Validates the communication status of all nodes (leafs, spines, and hosts) running the NetQ Agent in your network fabric. The output displays the status (passed/failed/skipped) of all tests and a summary including:

- Total number of nodes found
- Number of nodes validated
- Number of nodes that failed the validation
- Number of nodes that have been silent for 90 seconds (rotten)
- Number of nodes with warnings

### Syntax

```
netq check agents streaming
    [hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
    [include <agents-number-range-list> | exclude <agents-number-range-list>]
    [around <text-time>]
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<agent-number-range-list\> | Include the specified validation tests |
| exclude | \<agent-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

Basic validation that runs all tests on all devices:

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

Validation for selected devices:

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

Basic validation that checks device states as they were 4 hours ago:

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

- ```netq show agents```
- ```netq show unit-tests agent```
- ```netq add validation```
- ```netq config agent```

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
    [streaming | legacy]
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
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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
- ```netq show bgp```
- ```netq show unit-tests bgp```
- ```netq add validation```
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
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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

- ```netq show unit-tests cl-version```

- - -

## netq check clag

Verifies CLAG session consistency by identifying all CLAG peers with errors or misconfigurations in the NetQ domain. In particular, it looks for:

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
    [streaming | legacy]
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
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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

Validate only selected devices:

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

- ```netq show clag```
- ```netq show unit-tests clag```
- ```netq add validation```

- - -
<!-- vale off -->
## netq check evpn
<!-- vale on -->
Verifies communication status for all nodes (leafs, spines, and hosts) running instances of Ethernet VPN (EVPN) in your network fabric. In particular, it looks for:

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
    [label <text-label-name> | hostnames <text-list-hostnames>]
    [check_filter_id <text-check-filter-id>]
    [include <evpn-number-range-list> | exclude <evpn-number-range-list>]
    [around <text-time>]
    [streaming | legacy]
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
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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
- ```netq show evpn```
- ```netq show unit-tests evpn```
- ```netq add validation```
<!-- vale on -->
- - -

## netq check interfaces

Verifies interface communication status for all nodes (leafs, spines, and hosts) or an interface between specific nodes in your network fabric. In particular, it looks for:

- Administrative and operational state status
- Link speed consistency
- Autonegotiation-settings consistency

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
    [streaming | legacy]
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
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings.. |

### Sample Usage

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

Basic validation without error information:

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

- ```netq show interfaces```
- ```netq show unit-tests interfaces```
- ```netq add validation```

- - -

## netq check mlag

Verifies MLAG session consistency by identifying all MLAG peers with errors or misconfigurations in the NetQ domain. In particular, it looks for:

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
    [streaming | legacy]
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
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON file format instead of default on-screen text format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |
### Sample Usage

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

Validate only selected devices:

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

Exclude selected validation tests:

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

- ```netq show mlag```
- ```netq show unit-tests mlag```
- ```netq add validation```

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
    [streaming | legacy]
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
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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

Add nodes without peer links to output:

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

- ```netq show unit-tests mtu```
- ```netq add validation```

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
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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

- ```netq show ntp```
- ```netq show unit-tests ntp```
- ```netq add validation```

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
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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
- ```netq show ospf```
- ```netq show unit-tests ospf```
- ```netq add validation```
<!-- vale on -->
- - -
## netq check roce

Searches for consistent RoCE and QoS configurations across nodes.
### Syntax

```
netq check roce
    [streaming]
    [hostnames <text-list-hostnames>] 
    [check_filter_id <text-check-filter-id>] 
    [include <roce-number-range-list> | exclude <roce-number-range-list>] 
    [around <text-time>] 
    [json | summary]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| hostnames | \<text-list-hostnames\> | Comma-separated list (no spaces) of hostnames to include in validation |
| check_filter_id | \<text-check-filter-id> | Include the specific filter for a validation |
| include | \<roce-number-range-list\> | Include the specified validation tests |
| exclude | \<roce-number-range-list\> | Exclude the specified validation tests |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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
### Related Commands

- ```netq show roce-counters``` 
- ```netq show roce-config```
- ```netq show roce-counters pool```
- ```netq show events```
- ```netq show unit-tests```

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
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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

- ```netq show sensors```
- ```netq show unit-tests sensors```
- ```netq add validation```

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
    [streaming | legacy]
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
| streaming | NA | Perform a streaming query check |
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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

- ```netq show vlan```
- ```netq show unit-tests vlan```
- ```netq add validation```

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
    [streaming | legacy]
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
| legacy | NA | Perform a non-streaming query check |
| json | NA | Display the output in JSON format |
| summary | NA | Display only the summary information and test results. Do not display details for tests that failed or had warnings. |

### Sample Usage

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
- ```netq show vxlan```
- ```netq show unit-tests vxlan```
- ```netq add validation```
<!-- vale on -->
<!-- vale NVIDIA.HeadingTitles = YES -->