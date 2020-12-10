---
title: A and B Commands
author: NVIDIA
weight: 1101
---

This topic includes all commands that begin with `netq a*` and `netq b*`.

## netq add events-config

netq add events-config [events_config_id <text-events-config-id-anchor>] [events_config_name <text-events-config-name-anchor>] [message_type <text-message-type-anchor>] [scope <text-events-scope-anchor>] [is_active true | is_active false] [suppress_until <text-suppress-until>]


## netq add notification

netq add notification channel slack <text-channel-name> webhook <text-webhook-url> [severity info | severity warning | severity error | severity debug] [tag <text-slack-tag>]
   netq add notification channel pagerduty <text-channel-name> integration-key <text-integration-key> [severity info | severity warning | severity error | severity debug]
   netq add notification channel syslog <text-channel-name> hostname <text-syslog-hostname> port <text-syslog-port> [severity info | severity warning | severity error | severity debug]
   netq add notification channel email <text-channel-name> to <text-email-toids>  [smtpserver <text-email-hostname>] [smtpport <text-email-port>] [login <text-email-id>] [password <text-email-password>] [severity info | severity warning | severity error | severity debug]
   netq add notification filter <text-filter-name> [severity info | severity warning | severity error | severity debug] [rule <text-rule-name-anchor>] [channel <text-channel-name-anchor>] [before <text-filter-name-anchor> | after <text-filter-name-anchor>]
   netq add notification rule <text-rule-name> key <text-rule-key> value <text-rule-value>
   netq add notification proxy <text-proxy-hostname> [port <text-proxy-port>]


## netq add tca

netq add tca [event_id <text-event-id-anchor>] [tca_id <text-tca-id-anchor>] [scope <text-scope-anchor>] [severity info | severity critical] [is_active true | is_active false] [suppress_until <text-suppress-ts>] [threshold_type user_set | threshold_type vendor_set] [ threshold <text-threshold-value> ] [channel <text-channel-name-anchor> | channel drop <text-drop-channel-name>]

    netq add tca event_id <event-name> scope <regex-filter> [severity <critical|info>] threshold <value>
    netq add tca tca_id <tca-rule-name> is_active <true|false>
    netq add tca tca_id <tca-rule-name> channel drop <channel-name>

## netq add trace

netq add trace <mac> [vlan <1-4096>] from (<src-hostname> | <ip-src>) [vrf <vrf>] [alert-on-failure]
    netq add trace name <text-new-trace-name> <mac> [vlan <1-4096>] from (<src-hostname> | <ip-src>) [vrf <vrf>] interval <text-time-min> [alert-on-failure]
    netq add trace <ip> from (<src-hostname> | <ip-src>) [vrf <vrf>] [alert-on-failure]
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
