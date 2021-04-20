---
title: D through H Commands
author: NVIDIA
weight: 1103
toc: 3
right_toc_levels: 1
pdfhidden: true
---

This topic includes all commands that begin with `netq d*`, `netq e*`, `netq f*`, `netq g*`, and `netq h*`.

## netq decommission

Decommissions a switch or host currently running NetQ Agent. This removes information about the switch or host from the NetQ database. Before decommissioning a switch, you should stop and disable the NetQ Agent.

You might need to decommission a switch when you:

- Change the hostname of the switch or host being monitored
- Move the switch or host being monitored from one data center to another
- RMA the switch or host being monitored

### Syntax

```
netq decommission
    <hostname-to-decommission>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname-to-decommission\> | Decommission the switch with this hostname |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| Before 2.1.2 | Introduced |

### Sample Usage

```
cumulus@switch:~$ sudo systemctl stop netq-agent
cumulus@switch:~$ sudo systemctl disable netq-agent

cumulus@switch:~$ netq decommission leaf28
Successfully decommissioned node leaf28
```

### Related Commands

None

- - -

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

### Related Commands

- netq add events-config
- netq show events-config

- - -

## netq del notification

Removes a channel, filter, rule, or proxy component from an event notification configuration. This is commonly done when:

- You retire selected channels from a given notification application (Slack, PagerDuty, <!-- vale off -->Syslog<!-- vale on -->, or Email) and you no longer need the configuration in NetQ
- A filter was temporary; for debugging for example
- A rule no longer applies
- A proxy is no longer needed or desired

### Syntax

Four forms of this command are available, one for each component of the configuration.

```
netq del notification channel <text-channel-name-anchor>
netq del notification filter <text-filter-name-anchor>
netq del notification proxy
netq del notification rule <text-rule-name-anchor>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| channel | \<text-channel-name-anchor\> | Remove this channel from event notification configurations |
| filter | \<text-filter-name-anchor\> | Remove this filter from event notification configurations |
| proxy | NA | Remove the notification proxy and send notification messages directly to the NetQ appliance or VM |
| rule | \<text-rule-name-anchor\> | Remove this rule from event notification configurations |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

Remove channel

```
cumulus@switch:~$ netq del notification channel slk-netq-events

cumulus@switch:~$ netq show notification channel
Matching config_notify records:
Name            Type             Severity         Channel Info
--------------- ---------------- ---------------- ------------------------
pd-netq-events  pagerduty        info             integration-key: 1234567
                                                    890
```

Remove filter

```
cumulus@switch:~$ netq del notification filter bgpSpine

cumulus@switch:~$ netq show notification filter
Matching config_notify records:
Name            Order      Severity         Channels         Rules
--------------- ---------- ---------------- ---------------- ----------
swp52Drop       1          error            NetqDefaultChann swp52
                                            el
vni42           2          warning          pd-netq-events   evpnVni
configChange    3          info             slk-netq-events  sysconf
svcDown         4          critical         slk-netq-events  svcStatus
critTemp        5          critical         pd-netq-events   switchLeaf
                                                            04
                                                            overTemp
```

Remove proxy

```
cumulus@switch:~$ netq del notification proxy
Successfully overwrote notifier proxy to null
```

Remove rule

```
cumulus@switch:~$ netq del notification rule swp52

cumulus@switch:~$ netq show notification rule
Matching config_notify records:
Name            Rule Key         Rule Value
--------------- ---------------- --------------------
bgpHostname     hostname         spine-01
evpnVni         vni              42
overTemp        new_s_crit       24
svcStatus       new_status       down
switchLeaf04    hostname         leaf04
sysconf         configdiff       updated
```

### Related Commands

- netq add notification
- netq show notification

- - -

- - - 

## netq del tca

Removes a threshold-based event notification rule. Use `netq show tca` to find the event name. If you prefer to disable the rule rather than remove it, refer to `netq add tca`.

### Syntax

```
netq del tca
    tca_id <tca-rule-name>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| tca_id | \<tca-rule-name\> | Remove the threshold-based rule with this event name |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq del tca tca_id TCA_RXBYTES_UPPER_1
Successfully deleted TCA TCA_RXBYTES_UPPER_1
```

### Related Commands

- netq add tca
- netq show tca

- - -

## netq del trace

Removes a scheduled trace, whether created using the NetQ UI or CLI. Use `netq show trace summary` to obtain the relevant trace name.

{{<notice note>}}
Both standard user and administrative users can remove scheduled traces. No notification is generated on removal. Be sure to communicate with other users before removing a scheduled trace to avoid confusion and support issues.
{{</notice>}}

### Syntax

```
netq del trace 
    <text-trace-name>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-trace-name\> | Remove the scheduled trace with this name |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq show trace summary json
[
    {
        "job_end_time": 1605300327131,
        "job_req_time": 1604424893944,
        "job_start_time": 1605300318198,
        "jobid": "f8d6a2c5-54db-44a8-9a5d-9d31f4e4701d",
        "status": "Complete",
        "status_details": "1",
        "trace_name": "leaf01toborder01",
        "trace_params": {
            "alert_on_failure": "0",
            "dst": "10.10.10.63",
            "src": "10.10.10.1",
            "vlan": "-1",
            "vrf": ""
        }
    },
...

cumulus@switch:~$ netq del trace leaf01toborder01
Successfully deleted schedule trace leaf01toborder01
```

### Related Commands

- netq add trace name
- netq show trace summary

- - -

- - -

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
| NA | \<text-validation-name\> | Remove the scheduled validation with this name |

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

Displays the syntax for all commands or ones containing a particular keyword, a list of all commands and options, or a summary of command formatting.

### Syntax

```
netq help [<text-keywords>]
netq help list
netq help verbose
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| list | NA | Display all NetQ commands in the terminal window |
| verbose | NA | Display NetQ command formatting rules |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-keywords\> | Display syntax for commands with these keywords |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 1.x | Introduced |

### Sample Usage

Show syntax for all commands with the `agent` keyword

```
cumulus@switch:~$ netq agent help OR netq help agent
Commands:
    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config del agent kubernetes-monitor
    netq check agents [label <text-label-name> | hostnames <text-list-hostnames>] [include <agent-number-range-list> | exclude <agent-number-range-list>] [around <text-time>] [json]
    netq show unit-tests agent [json]
    netq config (add|del) agent (stats|sensors)
...
```

Show all NetQ commands

```
cumulus@switch:~$ netq help list

netq - Query data across all nodes in fabric

Usage:
   netq help [<text-keywords>]
   netq help verbose
   netq help list

   netq <hostname> show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
   netq show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [subnet|supernet|gateway] [around <text-time>] [json]
   netq <hostname> show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
   netq show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [subnet|supernet|gateway] [around <text-time>] [json]
...
```

Show the NetQ command format rules

```
cumulus@netq-ts:~$ netq help verbose

netq commands have the following format:
    netq [<hostname>] action object [options]

[] denotes an optional parameter or keyword
<> denotes a parameter to be specified such as an IP prefix, addr etc.

Hitting the TAB key will automatically show the available options.
Partial keywords are also accepted; e.g.: 'netq show ip ro 4.0.0.1'.
...
```

### Related Commands

None

- - -
