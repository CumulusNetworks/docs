---
title: D through H Commands
author: NVIDIA
weight: 1103
---

This topic includes all commands that begin with `netq d*`, `netq e*`, `netq f*`, `netq g*`, and `netq h*`.

## netq decommission

netq decommission <hostname-to-decommission>

## netq del
    events-config  :  Events configured for suppression
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

## netq help

cumulus@netq-ts:~$ netq help 
    <text-keywords>  :  add help text
    list             :  Show all help commands
    verbose          :  More help on help

    netq help [<text-keywords>]
   netq help verbose
   netq help list