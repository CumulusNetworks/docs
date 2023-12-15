---
title: Validation Checks
author: NVIDIA
weight: 750
toc: 2
---
When you discover operational anomalies, you can check whether the devices, hosts, network protocols, and services are operating as expected. NetQ lets you see when changes have occurred to the network, devices, and interfaces by viewing their operation, configuration, and status at an earlier point in time.

Validation support is available in the NetQ UI and the NetQ CLI for the following:

| Item | NetQ UI | NetQ CLI |
| --- | :---: | :---: |
| Addresses | Yes | Yes |
| Agents | Yes | Yes |
| BGP | Yes | Yes |
| Cumulus Linux version | No | Yes |
| EVPN | Yes | Yes |
| Interfaces | Yes | Yes |
| MLAG (CLAG) | Yes | Yes |
| MTU | Yes | Yes |
| NTP | Yes | Yes |
| OSPF | Yes | Yes |
| RoCE | Yes | Yes |
| Sensors | Yes | Yes |
| VLAN | Yes | Yes |
| VXLAN | Yes | Yes |

## View and Run Validations in the UI

The Validation Summary card displays a summary of validation checks from the past 24 hours. Select {{<img src="/images/netq/validation-icon.svg" height="18" width="18">}} **Validation** in the header to create or schedule new validation checks, as well as view previous checks.

{{<figure src="/images/netq/val-summary-460.png" width="200">}}


## Validation with the NetQ CLI

The NetQ CLI uses the {{<link title="check" text="netq check commands">}} to validate the various elements of your network fabric, looking for inconsistencies in configuration across your fabric, connectivity faults, missing configurations, and so forth. You can run commands from any node in the network.
### View Default Validation Tests

To view the list of tests run for a given protocol or service by default, use either `netq show unit-tests <protocol/service>` or perform a tab completion on `netq check <protocol/service> [include|exclude]`. Refer to {{<link title="Validation Tests Reference">}} for a description of the individual tests.

### Select Which Tests to Run

<!-- vale off -->
You can include or exclude one or more of the various tests performed during the validation. Each test is {{<link title="Validation Tests Reference" text="assigned a number">}}, which is used to identify the tests. By default, all tests are run. The `<protocol-number-range-list>` value is used with the `include` and `exclude` options to indicate which tests to include. It is a number list separated by commas, or a range using a dash, or a combination of these. Do not use spaces after commas. For example:
<!-- vale on -->

- include 1,3,5
- include 1-5
- include 1,3-5
- exclude 6,7
- exclude 6-7
- exclude 3,4-7,9

The output indicates whether a given test passed, failed, or was skipped.
### Example Validation Test

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

## Validation Check Result Filtering

You can create filters to suppress false alarms or uninteresting errors and warnings. For example, certain configurations permit a singly connected MLAG bond, which generates a standard error that is not useful.

{{%notice note%}}
Filtered errors and warnings related to validation checks do NOT generate notifications and are not counted in events totals. They are counted as part of suppressed notifications instead.
{{%/notice%}}

You define these filters in the `/etc/netq/check-filter.yml` file. You can create a rule for individual check commands or you can create a global rule that applies to all tests run by the check command. Additionally, you can create a rule specific to a particular test run by the check command.

<!-- vale off -->
Each rule must contain at least one `match` criteria and an `action` response. The only action currently available is *filter*. The match can comprise multiple criteria, one per line, creating a logical AND. You can match against any column in the validation check output. The match criteria values *must match* the case and spacing of the column names in the corresponding `netq check` output and are parsed as regular expressions.
<!-- vale on -->

This example shows a global rule for the BGP checks that suppresses any events generated by the *DataVrf* virtual route forwarding interface coming from *swp3* or *swp7.*. It also shows a test-specific rule to filter all Address Families events from devices with hostnames starting with *exit-1* or *firewall*.

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

You can configure filters to change validation errors to warnings that would normally occur due to the default expectations of the `netq check` commands. This applies to all protocols and services, except for agents. For example, if you provision BGP with configurations where a BGP peer is not expected or desired, then errors that a BGP peer is missing occur. By creating a filter, you can remove the error in favor of a warning.

To create a validation filter:

1. Navigate to the `/etc/netq` directory.

2. Create or open the `check_filter.yml` file using your text editor of choice.

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

### Use Validation Commands in Scripts

If you are running scripts based on the older version of the `netq check` commands and want to stay with the old output, edit the *netq.yml* file to include `old-check: true` in the `netq-cli` section of the file. For example:

```
netq-cli:
  port: 32708
  server: 127.0.0.1
  old-check: true
```
  
Then run `netq config restart cli` to apply the change.

If you update your scripts to work with the new version of the commands, change the `old-check` value to *false* or remove it. Then restart the CLI.