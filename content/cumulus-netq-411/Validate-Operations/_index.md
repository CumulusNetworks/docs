---
title: Validation Checks
author: NVIDIA
weight: 750
toc: 2
---

NetQ periodically runs default validations to verify whether devices, hosts, network protocols, and services are operating as expected. These validations measure what NetQ expects from a healthy network against the data it receives from the network it is monitoring. When NetQ detects an anomaly or inconsistency, the system will broadcast an event.

NetQ excludes certain checks from running by default. You can run an {{<link title="Validate Network Protocol and Service Operations#on-demand-validations" text="on-demand validation">}} or {{<link title="Validate Network Protocol and Service Operations#schedule-a-validation" text="schedule a validation">}} to view validation results for those protocols and services.

| Item | NetQ UI | NetQ CLI | Run by Default | Frequency |
| --- | :---: | :---: | :---: |  :---: |
| Addresses | Yes | Yes | No | N/A |
| Agents | Yes | Yes |  Yes |  60 mins |
| BGP | Yes | Yes | Yes |  60 mins |
| Cumulus Linux version | No | Yes |  No | N/A |
| EVPN | Yes | Yes |  Yes | 60 mins |
| Interfaces | Yes | Yes |  Yes |  60 mins |
| MLAG (CLAG) | Yes | Yes |  Yes |  60 mins |
| MTU | Yes | Yes | Yes |  60 mins |
| NTP | Yes | Yes | Yes |  60 mins |
| OSPF | Yes | Yes | Yes |  60 mins |
| RoCE | Yes | Yes | No | N/A |
| Sensors | Yes | Yes |  Yes |  60 mins |
| Topology | Yes | Yes | No | N/A |
| VLAN | Yes | Yes | Yes |  60 mins |
| VXLAN | Yes | Yes | Yes |  60 mins |

Refer to the {{<link title="Validation Tests Reference" text="Validation Reference">}} for a comprehensive breakdown of each test included in each category.
## View and Run Validations in the UI

The Validation Summary card displays a summary of a subset of validation checks from the past 24 hours. Select {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation** in the header to create or schedule new validation checks, as well as view previous checks.

{{<figure src="/images/netq/val-summary-460.png" width="200" alt="">}}


## Validation with the NetQ CLI

The NetQ CLI uses the {{<link title="check" text="netq check commands">}} to validate the various elements of your network fabric, looking for inconsistencies in configurations across your fabric, connectivity faults, missing configurations, and so forth. You can run commands from any node in the network.

To view the list of tests for a given protocol or service, use either {{<link title="show" text="netq show unit-tests">}} or perform a tab completion on `netq check <protocol/service> [include|exclude]`.

### Select Which Tests to Run

<!-- vale off -->
You can include or exclude one or more of the various tests performed during the validation by including or excluding the test's {{<link title="Validation Tests Reference" text="identification number">}}. The `check` command's `<protocol-number-range-list>` value is used with the `include` and `exclude` options to indicate which tests to include. It is a number list separated by commas, or a range using a dash, or a combination of these. Do not use spaces after commas. For example:
<!-- vale on -->

- include 1,3,5
- include 1-5
- include 1,3-5
- exclude 6,7
- exclude 6-7
- exclude 3,4-7,9

The output indicates whether a given test passed, failed, or was skipped.
### Example Validation Test

The following example displays a list of all the checks included in a BGP validation, along with their respective test numbers and filters, if any: 

```
cumulus@switch:~$ netq show unit-tests bgp
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
The following BGP validation includes only the session establishment (test number 0) and router ID (test number 2) tests. Note that you can obtain the same results using either of the `include` or `exclude` options and that the tests that are not run are marked *skipped*.
```
cumulus@switch:~$ netq check bgp include 0,2
bgp check result summary:

Total nodes         : 13
Checked nodes       : 0
Failed nodes        : 0
Rotten nodes        : 13
Warning nodes       : 0
Skipped nodes       : 0

Additional summary:
Failed Sessions     : 0
Total Sessions      : 0

Session Establishment Test   : passed
Address Families Test        : skipped
Router ID Test               : passed
Hold Time Test               : skipped
Keep Alive Interval Test     : skipped
Ipv4 Stale Path Time Test    : skipped
Ipv6 Stale Path Time Test    : skipped
Interface MTU Test           : skipped
```