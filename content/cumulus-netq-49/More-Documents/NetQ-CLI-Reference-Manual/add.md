---
title: add
author: NVIDIA
weight: 1101
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq add check-filter

You can add filters to `netq check` commands to suppress validation failures based on hostnames, failure reason, and other parameters. Refer to {{<link title="Validation Checks/#validation-check-result-filtering">}} for step-by-step instructions. 

### Syntax

```
 netq add check-filter 
    [check_filter_id <text-check-filter-id>] 
    [check_name <text-check-name-anchor>] 
    [test_name <text-test-name-anchor>] 
    [scope <text-check-scope-anchor> | scope-append <text-check-scope-anchor>] 
    [is_active true | is_active false] 
    [suppress_until <text-suppress-until>]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| check_filter_id | \<text-check-filter-id\> | Identifier for filter |
| check_name | \<text-check-name-anchor\> | Name of validation check |
| test_name | \<text-test-name-anchor\> | Name of validation test |
| scope | \<text-check-scope-anchor\> | Name of scope |
| scope-append | \<text-check-scope-anchor\> | Appends defined scope to existing configuration |
| is_active | true, false | Enables or disables configuration |
| suppress_until | \<text-suppress-until\> | Amount of time, in seconds, to suppress the specified events |

### Sample Usage

```
cumulus@switch:~$ netq add check-filter check_name roce test_name 'RoCE Classification' scope '[{"Reason": "Invalid traffic-class mapping for switch-priority 4.Expected 0 Got 3"}]' is_active true
Successfully added/updated Check Filter 
```

### Related Commands

- netq del check-filter
- netq show check-filter
 - - -

## netq add events-config

Suppresses system events, excluding them from event displays. You can suppress events for:

- Two years (default): useful when you do not want to see the events
- A designated amount of time: useful when you want to temporarily suppress events due to maintenance, or when testing a new network configuration

Events are displayed after the designated amount of time has passed.

### Syntax

```
netq add events-config
    [events_config_id <text-events-config-id-anchor>]
    [events_config_name <text-events-config-name-anchor>]
    [message_type <text-message-type-anchor>]
    [events_id <text-events-id-anchor>]
    [scope <text-events-scope-anchor>]
    [is_active true | is_active false]
    [suppress_until <text-suppress-until>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| events_config_id | \<text-events-config-id-anchor\> | Identifier for existing configuration; use to edit existing configuration |
| events_config_name | \<text-events-config-name-anchor\> | User-defined name for the configuration |
| message_type | \<text-message-type-anchor\> | <!-- vale off -->Type of message to suppress. Values include *agent*, *bgp*, *btrfsinfo*, *clag*, *clsupport*, *configdiff*, *evpn*, *link*, *ntp*, *ospf*, *sensor*, *services*, and *ssdutil*. <!-- vale on -->|
| events_id | <text-events-id-anchor\> | Identifier for events |
| scope | \<text-events-scope-anchor\> | Rule, in the form of a regular expression, indicating which devices, subset of devices or attributes to suppress |
| is_active | true, false | Enables or disables configuration |
| suppress_until | \<text-suppress-until\> | Amount of time, in seconds, to suppress the specified events |

### Sample Usage

Add a configuration called `mybtrfs` that suppresses OSPF-related events on leaf01 for the next 10 minutes:

```
netq add events-config events_config_name mybtrfs message_type ospf scope '[{"scope_name":"hostname","scope_value":"leaf01"},{"scope_name":"severity","scope_value":"*"}]' suppress_until 600
```

### Related Commands

- ```netq del events-config```
- ```netq show events-config```

 - - -

## netq add notification channel

NetQ presents events to the user through notification channels. NetQ supports five channel types: email, PagerDuty, Slack, `syslog`, and generic (a webhook channel that sends notifications to third-party applications). This command configures these channels.

{{<notice note>}}
You must have at least one channel, one rule, and one filter to fully configure a notification.
{{</notice>}}

### Syntax

A form of this command is available for each channel type:

```
netq add notification channel email
    <text-channel-name>
    to <text-email-toids>
    [smtpserver <text-email-hostname>]
    [smtpport <text-email-port>]
    [login <text-email-id>]
    [password <text-email-password>]
    [severity info | severity error]

netq add notification channel pagerduty
    <text-channel-name>
    integration-key <text-integration-key>
    [severity info | severity error]

netq add notification channel slack
    <text-channel-name>
    webhook <text-webhook-url>
    [severity info | severity error]
    [tag <text-slack-tag>]

netq add notification channel syslog
    <text-channel-name>
    hostname <text-syslog-hostname>
    port <text-syslog-port>
    [severity info | severity error]

netq add notification channel generic 
    <text-channel-name> 
    webhook <text-webhook-url> 
    [severity info | severity error ] 
    [use-ssl True | use-ssl False] 
    [auth-type basic-auth generic-username <text-generic-username> generic-password <text-generic-password> | auth-type api-key key-name <text-api-key-name> key-value <text-api-key-value>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| email | NA | Create an email channel to receive event notifications |
| pagerduty | NA | Create a PagerDuty channel to receive event notifications |
| slack | NA | Create a Slack channel to receive event notifications |
| syslog | NA | Create a <!-- vale off -->Syslog<!-- vale on --> channel to receive event notifications |
| generic | NA | Create a generic channel to receive event notifications |
| NA | \<text-channel-name\> | Name of the channel |
| to | \<text-email-toids\> | Comma-separated list of recipient email addresses; you cannot add spaces |
| integration-key | \<text-integration-key\> | {{<exlink url="https://support.pagerduty.com/docs/services-and-integrations#create-a-generic-events-api-integration/" text="Service or routing key">}} generated for your PagerDuty service. Default is an empty string (""). |
| webhook | \<text-webhook-url\> | Incoming webhook created in your instance |
| hostname | \<text-syslog-hostname\> | Name of the syslog server to receive notifications |
| port | \<text-syslog-port\> | Name of the port on the syslog server to receive notifications |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| smtpserver | \<text-email-hostname\> | Send notifications to the SMTP server with this hostname |
| smtpport | \<text-email-port\> | Send notifications to this port on the SMTP server |
| login | \<text-email-id\> | Email address for authentication |
| password | \<text-email-password\> | Password for authentication |
| severity | info, error | Only send notifications with this severity. Default severity is info. |
| auth-type | <!-- Add these -->| Specify authentication method |
| use-ssl | True, False | Enable SSL encryption |
| tag | \<text-slack-tag\> | Short text appended to a Slack notification to highlight particular channels or people. You must introduce the tag value with the @ sign. For example, *@netq-info* or *@net-admin*. |

### Sample Usage

Create an email channel

```
cumulus@switch:~$ netq add notification channel email onprem-email to netq-notifications@domain.com smtpserver smtp.domain.com smtpport 587 login smtphostlogin@domain.com password MyPassword123
Successfully added/updated channel onprem-email
```

Create a PagerDuty channel:

```
cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key c6d666e210a8425298ef7abde0d1998
Successfully added/updated channel pd-netq-events
```

Create a Slack channel:

```
cumulus@switch:~$ netq add notification channel slack slk-netq-events webhook https://hooks.slack.com/services/text/moretext/evenmoretext
Successfully added/updated channel slk-netq-events
```

<!-- vale off -->
Create a Syslog channel:
<!-- vale on -->

```
cumulus@switch:~$ netq add notification channel syslog syslog-netq-events hostname syslog-server port 514
Successfully added/updated channel syslog-netq-events
```

Refer to {{<link title="Configure System Event Notifications">}} for more information and complete notification configurations.

### Related Commands

- `netq del notification channel`
- `netq add notification rule`
- `netq add notification filter`
- `netq add notification proxy`
- `netq show notification`

 - - -

## netq add notification filter

Event notification filters tie notification rules to the notification channels. Filters can limit events so only those with a given severity get sent. You can insert filters before or after other filters to achieve the level of filtering desired. Refer to {{<link title="Configure System Event Notifications/#create-filters" text="Create Filters">}} for implementation details and additional examples.

{{<notice note>}}
You must have at least one channel, one rule, and one filter to fully configure a notification.
{{</notice>}}

### Syntax

```
netq add notification filter
    <text-filter-name>
    [severity info | severity error]
    [rule <text-rule-name-anchor>]
    [channel <text-channel-name-anchor>]
    [before <text-filter-name-anchor> | after <text-filter-name-anchor>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-filter-name\> | Name of the filter |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| severity | info, error | Only filter notifications with this severity. Default severity is *info*. |
| rule | \<text-rule-name-anchor\> | Name of the rule for where to apply this filter |
| channel | \<text-channel-name-anchor\> | Name of the channel for where to apply this filter.|
| before | \<text-filter-name-anchor\> | Insert this filter before the filter with this name. |
| after | \<text-filter-name-anchor\> | Insert this filter after the filter with this name. |

### Sample Usage

Create filter and assign it to an email channel:

```
cumulus@switch:~$ netq add notification filter notify-all-ifs rule all-interfaces channel onprem-email
Successfully added/updated filter notify-all-ifs
```

Create a filter and assign to a Slack channel:

```
cumulus@switch:~$ netq add notification filter notify-all-ifs rule all-interfaces channel slk-netq-events
Successfully added/updated filter notify-all-ifs
```

### Related Commands

- ```netq del notification filter```
- ```netq add notification rule```
- ```netq add notification channel```
- ```netq add notification proxy```
- ```netq show notification```

- - -

## netq add notification rule

Event notification rules define which events to include or exclude from a notification. Rules are a key-value pair. Each key has a defined set of values available for filtering against. Refer to {{<link title="Configure System Event Notifications/#create-rules" text="Create Rules">}} for implementation details and additional examples.

{{<notice note>}}
You must have at least one channel, one rule, and one filter to fully configure a notification.
{{</notice>}}

### Syntax

```
netq add notification rule
    <text-rule-name>
    key <text-rule-key>
    value <text-rule-value>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-rule-name\> | Name of the rule |
| key | \<text-rule-key\> | Only send events with this key |
| value | \<text-rule-value\> | Only send events with this key value |

### Options

None
### Sample Usage

Create rule to send all interface events:

```
cumulus@switch:~$ netq add notification rule all-interfaces key ifname value ALL
Successfully added/updated rule all-ifs
```

Create EVPN rule based on a VNI:

```
cumulus@switch:~$ netq add notification rule evpnVni key vni value 42
Successfully added/updated rule evpnVni
```

### Related Commands

- ```netq del notification rule```
- ```netq add notification filter```
- ```netq add notification channel```
- ```netq add notification proxy```
- ```netq show notification```

- - -

## netq add notification proxy

To send event notifications through a proxy server instead of directly to a notification channel, configure NetQ with the hostname, and optionally a proxy server port. If you do not specify a port, NetQ defaults to port 80. Only one proxy server is currently supported. To simplify deployment, configure your proxy server before configuring channels, rules, or filters.

### Syntax

```
netq add notification proxy
    <text-proxy-hostname>
    [port <text-proxy-port>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-proxy-hostname\> | Send notifications to the proxy server with this name |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| port | \<text-proxy-port\> | Send notifications to the port on the proxy server with this name |

### Sample Usage

Create proxy for event notification on default port

```
cumulus@switch:~$ netq add notification proxy proxy4
Successfully configured notifier proxy proxy4:80
```

### Related Commands

- ```netq del notification proxy```
- ```netq add notification channel```
- ```netq add notification rule```
- ```netq add notification filter```
- ```netq show notification```

- - -

## netq add tca

NetQ supports a set of events that trigger after crossing a user-defined threshold, called TCA events. These events allow detection and prevention of network failures for selected ACL resources, digital optics, forwarding resources, interface errors and statistics, link flaps, resource utilization, and sensor events. You can find a complete list in the {{<link title="Threshold-Crossing Events Reference">}}.

A TCA event notification configuration must contain one rule. Each rule must contain a scope and a threshold. Optionally, you can specify an associated channel.  *Note: If a rule is not associated with a channel, the event information is only reachable from the database.* If you want to deliver events to one or more notification channels, create the channels before you create TCA events with ```netq add notification channel```.

### Syntax

Two forms of the command are available: one that uses the `event_id` argument used to create the notification, and one that uses the `tca_id` argument used to modify an existing notification.

```
netq add tca event_id <text-event-id-anchor>
    [scope <text-scope-anchor>]
    [severity info | severity error]
    [is_active true | is_active false]
    [suppress_until <text-suppress-ts>]
    [threshold_type user_set | threshold_type vendor_set]
    [threshold <text-threshold-value>]
    [channel <text-channel-name-anchor> | channel drop <text-drop-channel-name>]

netq add tca tca_id <text-tca-id-anchor>
    [scope <text-scope-anchor>]
    [severity info | severity error]
    [is_active true | is_active false]
    [suppress_until <text-suppress-ts>]
    [threshold_type user_set | threshold_type vendor_set]
    [threshold <text-threshold-value>]
    [channel <text-channel-name-anchor> | channel drop <text-drop-channel-name>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| event_id | \<text-event-id-anchor\> | Create threshold-based event rule for the type of event with this ID |
| tca_id | \<text-tca-id-anchor\> | Modify the existing threshold-based event with this ID |


### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| scope | \<text-scope-anchor\> | Regular expression that filters the events. When you use two parameters, separate them with a comma, but no space. When you use an asterisk (*) alone, you must surround it with either single or double quotes. |
| severity | info, error | Only include events with this severity |
| is_active | true, false | Activate or deactivate the TCA event rule |
| suppress_until | \<text-suppress-ts\>| Suppress this event rule until the specified time, formatted as seconds from now |
| threshold_type | user_set, vendor_set | Apply threshold specified in `threshold` option or the default specified by the vendor for this attribute |
| threshold | \<text-threshold-value\> | Value that, when crossed, triggers the event |
| channel | \<text-channel-name-anchor\>| Send the events to the channel with this name |
| channel drop | \<text-drop-channel-name\> | Stop sending events to the channel with this name |

### Sample Usage

Basic threshold-based event notification:

```
cumulus@switch:~$ netq add tca event_id TCA_CPU_UTILIZATION_UPPER scope leaf* threshold 80
Successfully added/updated tca
```

Create threshold-based event notification and deliver to an existing syslog channel:

```
cumulus@switch:~$ netq add tca event_id TCA_SENSOR_TEMPERATURE_UPPER scope leaf12,temp1 threshold 32 channel syslog-netq-events
Successfully added/updated tca
```

Change the threshold for the rule *TCA_CPU_UTILIZATION_UPPER_1* to a value of 96 percent. *This overwrites the existing threshold value.*

```
cumulus@switch:~$ netq add tca tca_id TCA_CPU_UTILIZATION_UPPER_1 threshold 96
```


### Related Commands

- ```netq del tca```
- ```netq show tca```
- ```netq add notification channel```

- - -

## netq add trace

Create an on-demand trace and see the results in the On-demand Trace Results card in the NetQ UI rather than in text form in your terminal window. Refer to {{<link title="Verify Network Connectivity">}} for additional information. Note that the tracing function only knows about already learned addresses. If you find that a path is invalid or incomplete, you could ping the identified device so that its address becomes known.

### Syntax

Two forms of this command are available: one for layer 2 tracing and one for layer 3 tracing.

```
netq add trace <mac>
    [vlan <1-4096>]
    from (<src-hostname> | <ip-src>)
    [vrf <vrf>]
    [alert-on-failure]

netq add trace <ip>
    from (<src-hostname> | <ip-src>)
    [vrf <vrf>]
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<mac\> | Create a layer 2 trace to this MAC address |
| NA | \<ip\> | Create a layer 3 trace to this IPv4 or IPv6 address |
| from | \<src-hostname\>, \<ip-src\> | Create a trace beginning at the device with this hostname or IPv4/v6 address |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| vlan | 1-4096 | Create a layer 2 trace through this VLAN |
| vrf | \<vrf\> | Create a layer 2 or 3 trace through this VRF |
| alert-on-failure | NA | Generate an event when the trace fails |

### Sample Usage

Create a layer 3 trace through a given VRF:

```
cumulus@switch:~$ netq add trace 10.1.10.104 from 10.1.10.101 vrf RED
```

Create a layer 2 trace through a given VLAN:

```
cumulus@switch:~$ netq add trace 44:38:39:00:00:3e vlan 10 from 44:38:39:00:00:32
```

### Related Commands

- ```netq add trace name```
- ```netq del trace```
- ```netq show trace```
- ```netq show events type trace```

- - -

## netq add trace name

Create a scheduled trace and see the results in the Scheduled Trace Results card in the NetQ UI rather than in text form in your terminal window. Refer to {{<link title="Verify Network Connectivity">}} for additional information. Note that the tracing function only knows about already learned addresses. If you find that a path is invalid or incomplete, ping the identified device so that its address becomes known.

### Syntax

Two forms of this command are available: one for layer 2 tracing and one for layer 3 tracing.

```
netq add trace name
    <text-new-trace-name>
    <mac>
    [vlan <1-4096>]
    from (<src-hostname> | <ip-src>)
    [vrf <vrf>]
    interval <text-time-min>
    [alert-on-failure]

netq add trace name
    <text-new-trace-name>
    <ip>
    from (<src-hostname> | <ip-src>)
    [vrf <vrf>]
    interval <text-time-min>
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| name | \<text-new-trace-name\> | Unique name (per user) for the trace |
| NA | \<mac\> | Create a layer 2 trace to this MAC address |
| NA | \<ip\> | Create a layer 3 trace to this IPv4 or IPv6 address |
| from | \<src-hostname\>, \<ip-src\> | Create a trace beginning at the device with this hostname or IPv4/v6 address |
| interval | \<text-time-min\> | Set how often to run the trace, in minutes |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| vlan | 1-4096 | Create a layer 2 trace through this VLAN |
| vrf | \<vrf\> | Create a layer 2 or 3 trace through this VRF |
| alert-on-failure | NA | Generate an event if the trace fails |

### Sample Usage

Create a layer 3 trace that runs every 24 hours (1440 minutes):

```
cumulus@switch:~$ netq add trace name Lf01toBor01Daily 10.10.10.63 from 10.10.10.1 interval 1440m
Successfully added/updated Lf01toBor01Daily running every 1440m
```

Create a layer 2 trace that runs every 3 hours (180 minutes):

```
cumulus@switch:~$ netq add trace name Svr01toSvr04x3Hrs 44:38:39:00:00:3e vlan 10 from 10.1.10.101 interval 180m
Successfully added/updated Svr01toSvr04x3Hrs running every 180m
```

### Related Commands

- ```netq add trace```
- ```netq del trace```
- ```netq show trace```
- ```netq show events type trace```

- - -

## netq add validation

Creates a validation for various protocols and services to run on a regular interval, with results displayed inline. You can configure a maximum of 15 scheduled validations, not including the default scheduled validations.

### Syntax

```
netq add validation
    name <text-new-validation-name>
    type (addr | agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | roce | sensors | vlan | vxlan)
    interval <text-time-min>
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| name | user defined | Unique name for the validation |
| type | addr, agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, roce, sensors, vlan, or vxlan | Protocol or service to validate |
| interval | \<text-time-min\> | Frequency to run the validation, in minutes. Value must include time unit of *m*, minutes. Default scheduled validations per type run every 60 minutes. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| alert-on-failure | NA | Generate an event if the validation fails |

### Sample Usage

BGP validation that runs on all devices, every 15 minutes:

```
cumulus@switch:~$ netq add validation name Bgp15m type bgp interval 15m
```

### Related Commands

- ```netq add validation```
- ```netq del validation```
- ```netq show validation settings```
- ```netq show validation summary```

- - -

## netq add validation type

Creates an on-demand validation for various protocols and services, with results displayed inline.

### Syntax

```
netq add validation
    type (addr | agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | roce | sensors | vlan | vxlan)
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| type | addr, agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, roce, sensors, vlan, or vxlan | Protocol or service to validate |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| alert-on-failure | NA | Generate an event if the validation fails |

### Sample Usage

Create a BGP validation:

```
cumulus@switch:~$ netq add validation type bgp
```

### Related Commands

- ```netq add validation```
- ```netq del validation```
- ```netq show validation settings```
- ```netq show validation summary```
