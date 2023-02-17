---
title: del
author: NVIDIA
weight: 1103
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
## netq del check-filter

Removes filter from `netq check` command to reenable event notifications.

### Syntax

```
netq del check-filter 
    check_filter_id <text-check-filter-id>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| check_filter_id | \<text-check-filter-id\> | Delete the specified validation filter |

### Options

None

### Related Commands

- `netq add check-filter`
- `netq show check-filter`

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

- ```netq add events-config```
- ```netq show events-config```

- - -

## netq del notification

Removes a channel, filter, rule, or proxy component from an event notification configuration. This is commonly done when:

- You retire selected channels from a given notification application (Slack, PagerDuty, `syslog`, or email) and you no longer need the configuration in NetQ
- A filter was temporary (for example, when debugging)
- A rule no longer applies
- A proxy is no longer required

### Syntax

Four forms of this command are available, one for each component of the configuration:

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

### Sample Usage

Remove notification channel:

```
cumulus@switch:~$ netq del notification channel slk-netq-events

cumulus@switch:~$ netq show notification channel
Matching config_notify records:
Name            Type             Severity         Channel Info
--------------- ---------------- ---------------- ------------------------
pd-netq-events  pagerduty        info             integration-key: 1234567
                                                    890
```

Remove notification rule:

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

- ```netq add notification```
- ```netq show notification```

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

### Sample Usage

```
cumulus@switch:~$ netq del tca tca_id TCA_RXBYTES_UPPER_1
Successfully deleted TCA TCA_RXBYTES_UPPER_1
```

### Related Commands

- ```netq add tca```
- ```netq show tca```

- - -

## netq del trace

Removes a scheduled trace. Use `netq show trace summary` to obtain the relevant trace name.

{{<notice note>}}
Both standard user and administrative roles can remove scheduled traces. The removal does not generate a notification. Be sure to communicate with other users before removing a scheduled trace to avoid confusion and support issues.
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

- ```netq add trace name```
- ```netq show trace summary```

- - -

## netq del validation

Removes a scheduled validation. Useful when you have created a scheduled validation for troubleshooting and you no longer need it, or if you are reaching your maximum of 15 scheduled validations and you want to <!-- vale off -->prioritize<!-- vale on --> one validation over another. Use the related `netq show validation settings` command to view the names of existing scheduled validations.

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
### Sample Usage

```
cumulus@switch:~$ netq del validation Bgp15m
Successfully deleted validation Bgp15m
```

### Related Commands

- ```netq add validation```
- ```netq show validation settings```