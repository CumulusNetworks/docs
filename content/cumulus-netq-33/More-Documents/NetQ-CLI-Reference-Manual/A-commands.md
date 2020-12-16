---
title: A and B Commands
author: NVIDIA
weight: 1101
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---

This topic includes all commands that begin with `netq a*` and `netq b*`.

## netq add events-config

Enables suppression of any of the numerous system events, excluding them from event displays. By default all events are delivered. You can suppress events for:

- Two years (default): useful when you do not want to see the events (essentially never show them)
- A period of time: useful when you want to temporarily suppress events due to maintenance (typically days), or when testing a new network configuration where the switch may generate many messages that are expected and not needed beyond this time period (typically minutes or hours)

Events are automatically sent after the designated amount of time has passed.

### Syntax

```
netq add events-config
    [events_config_id <text-events-config-id-anchor>]
    [events_config_name <text-events-config-name-anchor>]
    [message_type <text-message-type-anchor>]
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
| message_type | \<text-message-type-anchor\> | Type of message to be suppressed. Values include *agent*, *bgp*, *btrfsinfo*, *clag*, *clsupport*, *configdiff*, *evpn*, *link*, *ntp*, *ospf*, *sensor*, *services*, and *ssdutil*. |
| scope | \<text-events-scope-anchor\> | xxx |
| is_active | true, false | Enables or disables configuration |
| suppress_until | \<text-suppress-until\> | Amount of time, in seconds, to suppress the specified events |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

Add a configuration called `mybtrfs` that suppresses OSPF-related events on leaf01 for the next 10 minutes, run:

```
netq add events-config events_config_name mybtrfs message_type ospf scope '[{"scope_name":"hostname","scope_value":"leaf01"},{"scope_name":"severity","scope_value":"*"}]' suppress_until 600
```

### Related Commands

- netq del events-config
- netq show events-config

 - - -

## netq add notification channel

NetQ events are presented to the user through event notification channels. NetQ supports four channel types: email, PagerDuty, Slack, or Syslog. This command configures these channels.

### Syntax

There is a form of this command for each channel type.

```
netq add notification channel email
    <text-channel-name>
    to <text-email-toids>
    [smtpserver <text-email-hostname>]
    [smtpport <text-email-port>]
    [login <text-email-id>]
    [password <text-email-password>]
    [severity info | severity warning | severity error | severity debug]

netq add notification channel pagerduty
    <text-channel-name>
    integration-key <text-integration-key>
    [severity info | severity warning | severity error | severity debug]

netq add notification channel slack
    <text-channel-name>
    webhook <text-webhook-url>
    [severity info | severity warning | severity error | severity debug]
    [tag <text-slack-tag>]

netq add notification channel syslog
    <text-channel-name>
    hostname <text-syslog-hostname>
    port <text-syslog-port>
    [severity info | severity warning | severity error | severity debug]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| email | NA | Create an email channel to receive event notifications |
| pagerduty | NA | Create a PagerDuty channel to receive event notifications |
| slack | NA | Create a Slack channel to receive event notifications |
| syslog | NA | Create a Syslog channel to receive event notifications |
| NA | \<text-channel-name\> | Name of the channel |
| to | \<text-email-toids\> | Comma-separated list of recipient email addresses; no spaces are allowed |
| integration-key | \<text-integration-key\> | {{<link url="https://support.pagerduty.com/docs/services-and-integrations#create-a-generic-events-api-integration/" text="Service or routing key">}} generated for your PagerDuty Service |
| webhook | \<text-webhook-url\> | Incoming webhook created in your Slack instance |
| hostname | \<text-syslog-hostname\> | Name of the syslog server to receive notifications |
| port | \<text-syslog-port\> | Name of the port on the syslog server to receive notifications |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| events_config_id | \<text-events-config-id-anchor\> | Identifier for existing configuration; use to edit existing configuration |
| events_config_name | \<text-events-config-name-anchor\> | User-defined name for the configuration |
| message_type | \<text-message-type-anchor\> | Type of message to be suppressed. Values include *agent*, *bgp*, *btrfsinfo*, *clag*, *clsupport*, *configdiff*, *evpn*, *link*, *ntp*, *ospf*, *sensor*, *services*, and *ssdutil*. |
| scope | \<text-events-scope-anchor\> | xxx |
| is_active | true, false | Enables or disables configuration |
| suppress_until | \<text-suppress-until\> | Amount of time, in seconds, to suppress the specified events |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

Add a configuration called `mybtrfs` that suppresses OSPF-related events on leaf01 for the next 10 minutes, run:

```
netq add events-config events_config_name mybtrfs message_type ospf scope '[{"scope_name":"hostname","scope_value":"leaf01"},{"scope_name":"severity","scope_value":"*"}]' suppress_until 600
```

### Related Commands

- netq del events-config
- netq show events-config

 - - -

## netq add notification filter

   netq add notification filter <text-filter-name> [severity info | severity warning | severity error | severity debug] [rule <text-rule-name-anchor>] [channel <text-channel-name-anchor>] [before <text-filter-name-anchor> | after <text-filter-name-anchor>]

## netq add notification rule

   netq add notification rule <text-rule-name> key <text-rule-key> value <text-rule-value>

## netq add notification proxy
   netq add notification proxy <text-proxy-hostname> [port <text-proxy-port>]


## netq add tca

netq add tca [event_id <text-event-id-anchor>] [tca_id <text-tca-id-anchor>] [scope <text-scope-anchor>] [severity info | severity critical] [is_active true | is_active false] [suppress_until <text-suppress-ts>] [threshold_type user_set | threshold_type vendor_set] [ threshold <text-threshold-value> ] [channel <text-channel-name-anchor> | channel drop <text-drop-channel-name>]

(older version?)
    netq add tca event_id <event-name> scope <regex-filter> [severity <critical|info>] threshold <value>
    netq add tca tca_id <tca-rule-name> is_active <true|false>
    netq add tca tca_id <tca-rule-name> channel drop <channel-name>

## netq add trace (on-demand)

netq add trace <mac> [vlan <1-4096>] from (<src-hostname> | <ip-src>) [vrf <vrf>] [alert-on-failure]

netq add trace <ip> from (<src-hostname> | <ip-src>) [vrf <vrf>] [alert-on-failure]
    

## netq add trace (scheduled)
netq add trace name <text-new-trace-name> <mac> [vlan <1-4096>] from (<src-hostname> | <ip-src>) [vrf <vrf>] interval <text-time-min> [alert-on-failure]
netq add trace name <text-new-trace-name> <ip> from (<src-hostname> | <ip-src>) [vrf <vrf>] interval <text-time-min> [alert-on-failure]

## netq add validation name

Creates a validation for various protocols and services to be run on a regular interval, with results displayed in the associated Scheduled Validation Result cards in the NetQ UI. A maximum of 15 scheduled validation can be configured, not including the default scheduled validations.

### Syntax

```
netq add validation
    name <text-new-validation-name>
    type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf)
    interval <text-time-min>
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| name | user defined | Unique name for the validation |
| type | agents, bgp, evpn, interfaces, license, mlag, mtu, ntp, sensors, vlan, or vxlan | Protocol or service to be validated |
| interval | \<text-time-min\> | Frequency to run the validation, in minutes. Value must include time unit of *m*, minutes. Default scheduled validations per type run every 60 minutes. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| alert-on-failure | NA | Reserved |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

BGP validation; all devices, all tests, on a regular basis

```
cumulus@switch:~$ netq add validation name Bgp15m type bgp interval 15m
```

### Related Commands

- netq add validation
- netq del validation
- netq show validation settings
- netq show validation summary

- - -

## netq add validation type

Creates an on-demand validation for various protocols and services, with results displayed in the associated On-demand Validation Result cards in the NetQ UI.

### Syntax

```
netq add validation
    type (ntp | interfaces | license | sensors | evpn | vxlan | agents | mlag | vlan | bgp | mtu | ospf)
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| type | agents, bgp, evpn, interfaces, license, mlag, mtu, ntp, sensors, vlan, or vxlan | Protocol or service to be validated |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| alert-on-failure | NA | Reserved |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

BGP validation; all devices, all tests, currently

```
cumulus@switch:~$ netq add validation type bgp
```

### Related Commands

- netq add validation name
- netq del validation
- netq show validation settings
- netq show validation summary

- - -

## netq bootstrap

netq bootstrap reset [keep-db | purge-db]
    netq bootstrap master upgrade <text-tarball-name>
    netq bootstrap master (interface <text-opta-ifname>|ip-addr <text-ip-addr>) tarball <text-tarball-name> [pod-ip-range <text-pod-ip-range>]
    netq bootstrap worker tarball <text-tarball-name> master-ip <text-master-ip> [password <text-password>]
