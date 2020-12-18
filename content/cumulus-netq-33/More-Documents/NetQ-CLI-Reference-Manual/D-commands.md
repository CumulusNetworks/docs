---
title: D through H Commands
author: NVIDIA
weight: 1103
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---

This topic includes all commands that begin with `netq d*`, `netq e*`, `netq f*`, `netq g*`, and `netq h*`.

## netq decommission

netq decommission <hostname-to-decommission>

## netq del events-config

Removes an events suppression configuration. Useful when you no longer want to suppress the specified events. Consider modifying the configuration to disable or temporarily suspend the configuration.

### Syntax

```
netq del events-config
    events_config_id <text-events-config-id-anchor>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| events_config_id | \<text-events-config-id-anchor\> | Remove the event suppression configuration with this identifier |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

Obtain the configuration identifier, then remove it.

```
cumulus@switch:~$ netq show events-config events_config_id eventsconfig_1
Matching config_events records:
Events Config ID     Events Config Name   Message Type         Scope                                                        Active Suppress Until
-------------------- -------------------- -------------------- ------------------------------------------------------------ ------ --------------------
eventsconfig_1       job_cl_upgrade_2d89c agent                {"db_state":"*","hostname":"spine02","severity":"*"}         True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine02
eventsconfig_1       job_cl_upgrade_2d89c bgp                  {"vrf":"*","peer":"*","hostname":"spine04","severity":"*"}   True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
...

cumulus@switch:~$ netq del events-config events_config_id eventsconfig_10
Successfully deleted Events Config eventsconfig_10
```


## netq del
    notification   :  Send notifications to Slack or PagerDuty
    tca            :  Threshold Crossing Alerts
    trace          :  Control plane trace path across fabric
    validation     :  Schedule a validation check

## netq del notification

    netq del notification channel <text-channel-name-anchor>
    netq del notification filter <text-filter-name-anchor>
    netq del notification proxy
    netq del notification rule <text-rule-name-anchor>

## netq del tca

    netq del tca tca_id <tca-rule-name>

## netq del validation

Removes a scheduled validation. Useful when you have created a scheduled validation for troubleshooting and you no longer need it, or if you are reaching your maximum of 15 scheduled validations and you want to prioritize one validation over another. Use the related `netq show validation settings` command to view the names of existing scheduled validations.

### Syntax

```
netq del validation
    <text-validation-name>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-validation-name\> | Name of scheduled validation you want to remove |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq del validation Bgp15m
Successfully deleted validation Bgp15m
```

### Related Commands

- netq add validation name
- netq show validation settings

- - -

## netq help

cumulus@netq-ts:~$ netq help 
    <text-keywords>  :  add help text
    list             :  Show all help commands
    verbose          :  More help on help

    netq help [<text-keywords>]
   netq help verbose
   netq help list