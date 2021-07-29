---
title: Validate Operations
author: NVIDIA
weight: 1000
toc: 2
---
When you discover operational anomalies, you can validate that the devices, hosts, network protocols and services are operating as expected. You can also compare the current operation with past operation. With NetQ, you can view the overall health of your network at a glance and then delve deeper for periodic checks or as conditions arise that require attention. When issues are present, NetQ makes it easy to identify and resolve them. You can also see when changes have occurred to the network, devices, and interfaces by viewing their operation, configuration, and status at an earlier point in time.

NetQ enables you to validate the:

- Overall health of the network
- Operation of the network protocols and services running in your network (either on demand or on a scheduled basis)
- Configuration of physical layer protocols and services

Validation support is available in the NetQ UI and the NetQ CLI as shown here.

| Item | NetQ UI | NetQ CLI |
| --- | :---: | :---: |
| Agents | Yes | Yes |
| BGP | Yes | Yes |
| Cumulus Linux version | No | Yes |
| EVPN | Yes | Yes |
| Interfaces | Yes | Yes |
| LLDP | No | Yes |
| MLAG (CLAG) | Yes | Yes |
| MTU | Yes | Yes |
| NTP | Yes | Yes |
| OSPF | Yes | Yes |
| Sensors | Yes | Yes |
| VLAN | Yes | Yes |
| VXLAN | Yes | Yes |

## Validation with the NetQ UI

The NetQ UI uses the following cards to create validations and view results for these protocols and services:

- Network Health
- Validation Request
- On-demand and Scheduled Validation Results

For a general understanding of how well your network is operating, the Network Health card workflow is the best place to start as it contains the highest-level view and performance roll-ups. Refer to the {{<link title="NetQ UI Card Reference" text="NetQ UI Card Reference">}} for details about the components on these cards.

## Validation with the NetQ CLI

The NetQ CLI uses the `netq check` commands to validate the various elements of your network fabric, looking for inconsistencies in configuration across your fabric, connectivity faults, missing configuration, and so forth, and then display the results for your assessment. They can be run from any node in the network.

The NetQ CLI has many other validation features and considerations.

### Set a Time Period

You can run validations for a time in the past and output the results in JSON format if desired. The `around` option enables users to view the network state at an earlier time. The `around` option value requires an integer *plus* a unit of measure (UOM), with no space between them. The following are valid UOMs:

| UOM | Command Value | Example|
| --- | ------------- | -------|
| days | <#>d | 3d |
| hours | <#>h | 6h |
| minutes | <#>m | 30m |
| seconds | <#>s | 20s |

{{%notice tip%}}
If you want to go back in time by months or years, use the equivalent number of days.
{{%/notice%}}

### Improve Output Readability

You can the readability of the validation outputs using color. Green output indicates successful results and red output indicates results with failures, warnings, and errors. Use the `netq config add color` command to enable the use of color.

### View Default Validation Tests

To view the list of tests run for a given protocol or service by default, use either `netq show unit-tests <protocol/service>` or perform a tab completion on `netq check <protocol/service> [include|exclude]`. Refer to {{<link title="Validation Checks">}} for a description of the individual tests.

### Select the Tests to Run

You can include or exclude one or more of the various tests performed during the validation. Each test is assigned a number, which is used to identify which tests to run. Refer to {{<link title="Validation Checks">}} for a description of the individual tests. By default, all tests are run. The `<protocol-number-range-list>` value is used with the `include` and `exclude` options  to indicate which tests to include. It is a number list separated by commas, or a range using a dash, or a combination of these. Do not use spaces after commas. For example:

- include 1,3,5
- include 1-5
- include 1,3-5
- exclude 6,7
- exclude 6-7
- exclude 3,4-7,9

The output indicates whether a given test passed, failed, or was skipped.

## Validation Check Result Filtering

You can create filters to suppress false alarms or uninteresting errors and warnings that can be a nuisance in CI workflows. For example, certain configurations permit a singly connected CLAG bond and the standard error that is generated is not useful.

{{%notice note%}}
Filtered errors and warnings related to validation checks do NOT generate notifications and are not counted in the alarm and info event totals. They are counted as part of suppressed notifications instead.
{{%/notice%}}

The filters are defined in the `check-filter.yml` file in the `/etc/netq/` directory. You can create a rule for individual check commands or you can create a global rule that applies to all tests run by the check command. Additionally, you can create a rule specific to a particular test run by the check command.

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

You can configure filters to change validation errors to warnings that would normally occur due to the default expectations of the `netq check` commands. This applies to all protocols and services, except for Agents. For example, if you provision BGP with configurations where a BGP peer is not expected or desired, then errors that a BGP peer is missing occur. By creating a filter, you can remove the error in favor of a warning.

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

If you update your scripts to work with the new version of the commands, simply change the `old-check` value to *false* or remove it. Then restart the CLI.

{{%notice tip%}}
Use `netq check mlag` in place of `netq check clag` from NetQ 2.4 onward. `netq check clag` remains available for automation scripts, but you should begin migrating to `netq check mlag` to maintain compatibility with future NetQ releases.
{{%/notice%}}

## Related Information

- {{<link title="Manage Configurations">}}
- {{<link title="Monitor Operations">}}
- {{<link title="NetQ UI Card Reference">}}
