---
title: A and B Commands
author: NVIDIA
weight: 1101
toc: 3
right_toc_levels: 1
pdfhidden: true
---

This topic includes all commands that begin with `netq a*` and `netq b*`.

<!-- vale off -->
## netq add events-config
<!-- vale on -->

Enables suppression of any of the various system events, excluding them from event displays. By default all events are delivered. You can suppress events for:

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
| message_type | \<text-message-type-anchor\> | <!-- vale off -->Type of message to be suppressed. Values include *agent*, *bgp*, *btrfsinfo*, *clag*, *clsupport*, *configdiff*, *evpn*, *link*, *ntp*, *ospf*, *sensor*, *services*, and *ssdutil*. <!-- vale on -->|
| scope | \<text-events-scope-anchor\> | Rule, in the form of a regular expression, indicating which devices, subset of devices or attributes to suppress |
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

NetQ events are presented to the user through event notification channels. NetQ supports four channel types: email, PagerDuty, Slack, or `syslog`. This command configures these channels.

{{<notice note>}}
You must have at least one channel, one rule, and one filter to fully configure a notification.
{{</notice>}}

### Syntax

A form of this command is available for each channel type.

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
| syslog | NA | Create a <!-- vale off -->Syslog<!-- vale on --> channel to receive event notifications |
| NA | \<text-channel-name\> | Name of the channel |
| to | \<text-email-toids\> | Comma-separated list of recipient email addresses; no spaces are allowed |
| integration-key | \<text-integration-key\> | {{<exlink url="https://support.pagerduty.com/docs/services-and-integrations#create-a-generic-events-api-integration/" text="Service or routing key">}} generated for your PagerDuty Service. Default is an empty string (""). |
| webhook | \<text-webhook-url\> | Incoming webhook created in your Slack instance |
| hostname | \<text-syslog-hostname\> | Name of the syslog server to receive notifications |
| port | \<text-syslog-port\> | Name of the port on the syslog server to receive notifications |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| smtpserver | \<<text-email-hostname\> | Send notifications to the SMTP server with this hostname |
| smtpport | \<<text-email-port\> | Send notifications to this port on the SMTP server |
| login | \<text-email-id\> | Email address for authentication |
| password | \<text-email-password\> | Password for authentication |
| severity | info, warning, error, debug | Only send notifications with this severity. Default severity is info. |
| tag | \<text-slack-tag\> | Short text appended to a Slack notification to highlight particular channels or people. The tag value must be preceded by the @ sign. For example, @netq-info or @net-admin. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Added Email channel type |
| 2.1.2 | Introduced. Replaced `netq config ts add notifier channel`.  |

### Sample Usage

Create an email channel

```
cumulus@switch:~$ netq add notification channel email onprem-email to netq-notifications@domain.com smtpserver smtp.domain.com smtpport 587 login smtphostlogin@domain.com password MyPassword123
Successfully added/updated channel onprem-email
```

Create a PagerDuty channel

```
cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key c6d666e210a8425298ef7abde0d1998
Successfully added/updated channel pd-netq-events
```

Create a Slack channel

```
cumulus@switch:~$ netq add notification channel slack slk-netq-events webhook https://hooks.slack.com/services/text/moretext/evenmoretext
Successfully added/updated channel slk-netq-events
```

<!-- vale off -->
Create a Syslog channel
<!-- vale on -->

```
cumulus@switch:~$ netq add notification channel syslog syslog-netq-events hostname syslog-server port 514
Successfully added/updated channel syslog-netq-events
```

Refer to the {{<link title="Configure System Event Notifications">}} topic in the *NetQ User Guide* for more information and complete notification configurations.

### Related Commands

- netq del notification channel
- netq add notification rule
- netq add notification filter
- netq add notification proxy
- netq show notification

 - - -

## netq add notification filter

Event notification filters tie notification rules to the notification channels. Filters can limit events being sent to only those with a given severity. You can insert filters before or after other filters to achieve the level of filtering desired. Refer to {{<link title="Configure System Event Notifications/#create-filters" text="Create Filters">}} for implementation details and additional examples.

{{<notice note>}}
You must have at least one channel, one rule, and one filter to fully configure a notification.
{{</notice>}}

### Syntax

```
netq add notification filter
    <text-filter-name>
    [severity info | severity warning | severity error | severity debug]
    rule <text-rule-name-anchor>]
    [channel <text-channel-name-anchor>]
    [before <text-filter-name-anchor> | after <text-filter-name-anchor>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-filter-name\> | Name of the filter |
| rule | \<text-rule-name-anchor\> | Name of the rule where this filter is to be applied |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| severity | info, warning, error, debug | Only filter notifications with this severity. Default severity is info. |
| channel | \<text-channel-name-anchor\> | Name of the rule where this filter is to be applied |
| before | \<text-filter-name-anchor\> | Insert this filter before the filter with this name |
| after | \<text-filter-name-anchor\> | Insert this filter after the filter with this name |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced. Replaced `netq config ts add notifier filter`. |

### Sample Usage

Create filter and assign to Email channel

```
cumulus@switch:~$ netq add notification filter notify-all-ifs rule all-interfaces channel onprem-email
Successfully added/updated filter notify-all-ifs
```

Create a filter and assign to Slack channel

```
cumulus@switch:~$ netq add notification filter notify-all-ifs rule all-interfaces channel slk-netq-events
Successfully added/updated filter notify-all-ifs
```

### Related Commands

- netq del notification filter
- netq add notification rule
- netq add notification channel
- netq add notification proxy
- netq show notification

- - -

## netq add notification rule

Event notification rules define which events are included in or excluded from a notification. Rules are comprised of a key-value pair. Each key has a defined set of values available for filtering against. Refer to {{<link title="Configure System Event Notifications/#create-rules" text="Create Rules">}} for implementation details and additional examples.

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced. Replaced `netq config ts add notifier rule`. |

### Sample Usage

Create rule to send all interface events

```
cumulus@switch:~$ netq add notification rule all-interfaces key ifname value ALL
Successfully added/updated rule all-ifs
```

Create EVPN rule based on a VNI

```
cumulus@switch:~$ netq add notification rule evpnVni key vni value 42
Successfully added/updated rule evpnVni
```

### Related Commands

- netq del notification rule
- netq add notification filter
- netq add notification channel
- netq add notification proxy
- netq show notification

- - -

## netq add notification proxy

To send event notification messages through a proxy server instead of directly to a notification channel, you configure NetQ with the hostname, and optionally a port, of a proxy server. If no port is specified, NetQ defaults to port 80. Only one proxy server is currently supported. To simplify deployment, configure your proxy server before configuring channels, rules, or filters.

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.1.2 | Introduced |

### Sample Usage

Create proxy for event notification on default port

```
cumulus@switch:~$ netq add notification proxy proxy4
Successfully configured notifier proxy proxy4:80
```

### Related Commands

- netq del notification proxy
- netq add notification channel
- netq add notification rule
- netq add notification filter
- netq show notification

- - -

## netq add tca

NetQ supports a set of events that are triggered by crossing a user-defined threshold, called TCA events. These events allow detection and prevention of network failures for selected ACL resources, digital optics, forwarding resources, interface errors and statistics, link flaps, resource utilization, and sensor events. A complete list can be found in the {{<link title="TCA Event Messages Reference">}}.

A TCA event notification configuration must contain one rule. Each rule must contain a scope and a threshold. Optionally, you can specify an associated channel.  *Note: If a rule is not associated with a channel, the event information is only reachable from the database.* If you want to deliver events to one or more notification channels (Email, syslog, Slack, or PagerDuty), create them first using {{<link title="#netq add notification channel">}}.

### Syntax

Two forms of the command are available; one that uses the `event_id` argument used to create the notification, and one that uses the `tca_id` argument used to modify an existing notification.

```
netq add tca event_id
    <text-event-id-anchor>
    scope <text-scope-anchor>
    [severity info | severity critical]
    [is_active true | is_active false]
    [suppress_until <text-suppress-ts>]
    [threshold_type user_set | threshold_type vendor_set]
    threshold <text-threshold-value>
    [channel <text-channel-name-anchor> | channel drop <text-drop-channel-name>]

netq add tca tca_id
    <text-tca-id-anchor>
    [scope <text-scope-anchor>]
    [severity info | severity critical]
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
| scope | \<text-scope-anchor\> | Regular expression that filters the events. When two parameters are used, they are separated by a comma, but no space. When an asterisk (*) is used alone, it must be entered inside either single or double quotes. |
| threshold | \<text-threshold-value\> | Value when crossed that triggers the event |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| severity | info, critical | Only include events with this severity |
| is_active | true, false | Activate or deactivate the TCA event rule |
| suppress_until | \<text-suppress-ts\>| Suppress this event rule until the specified time; formatted as seconds from now |
| threshold_type | user_set, vendor_set | Apply threshold specified in `threshold` option or the default specified by the vendor for this attribute |
| channel | \<text-channel-name-anchor\>| Send the events to the channel with this name |
| channel drop | \<text-drop-channel-name\> | Stop sending events to the channel with this name |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Added `threshold_type` option. Changed order of `tca_id` and `scope` options. |
| 2.4.0 | Introduced |

### Sample Usage

Basic threshold-based event notification

```
cumulus@switch:~$ netq add tca event_id TCA_CPU_UTILIZATION_UPPER scope leaf* threshold 80
Successfully added/updated tca
```

Create threshold-based event notification and deliver to an existing syslog channel

```
cumulus@switch:~$ netq add tca event_id TCA_SENSOR_TEMPERATURE_UPPER scope leaf12,temp1 threshold 32 channel syslog-netq-events
Successfully added/updated tca
```

### Related Commands

- netq del tca
- netq show tca
- netq add notification channel

- - -

## netq add trace

Create an on-demand trace and see the results in the On-demand Trace Results card of the NetQ UI rather than in text form in your terminal window. Refer to {{<link title="Verify Network Connectivity">}} for additional information. Note that the tracing function only knows about addresses that have already been learned. If you find that a path is invalid or incomplete, you may need to ping the identified device so that its address becomes known.

### Syntax

Two forms of this command are available; one for layer 2 tracing and one for layer 3 tracing.

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

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

Create a layer 3 trace through a given VRF

```
cumulus@switch:~$ netq add trace 10.1.10.104 from 10.1.10.101 vrf RED
```

Create a layer2 trace through a given VLAN

```
cumulus@switch:~$ netq add trace 44:38:39:00:00:3e vlan 10 from 44:38:39:00:00:32
```

### Related Commands

- netq add trace name
- netq del trace
- netq show trace
- netq show events type trace

- - -

## netq add trace name

Create a scheduled trace and see the results in the Scheduled Trace Results card of the NetQ UI rather than in text form in your terminal window. Refer to {{<link title="Verify Network Connectivity">}} for additional information. Note that the tracing function only knows about addresses that have already been learned. If you find that a path is invalid or incomplete, you may need to ping the identified device so that its address becomes known.

### Syntax

Two forms of this command are available; one for layer 2 tracing and one for layer 3 tracing.

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
| interval | \<text-time-min\> | How often to run the trace, in minutes |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| vlan | 1-4096 | Create a layer 2 trace through this VLAN |
| vrf | \<vrf\> | Create a layer 2 or 3 trace through this VRF |
| alert-on-failure | NA | Generate an event when the trace fails |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

Layer 3 trace

```
cumulus@switch:~$ netq add trace name Lf01toBor01Daily 10.10.10.63 from 10.10.10.1 interval 1440m
Successfully added/updated Lf01toBor01Daily running every 1440m
```

Layer 2 trace

```
cumulus@switch:~$ netq add trace name Svr01toSvr04x3Hrs 44:38:39:00:00:3e vlan 10 from 10.1.10.101 interval 180m
Successfully added/updated Svr01toSvr04x3Hrs running every 180m
```

### Related Commands

- netq add trace
- netq del trace
- netq show trace
- netq show events type trace

- - -

## netq add validation name

Creates a validation for various protocols and services to be run on a regular interval, with results displayed inline. A maximum of 15 scheduled validations can be configured, not including the default scheduled validations.

### Syntax

```
netq add validation
    name <text-new-validation-name>
    type (agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | sensors | vlan | vxlan)
    interval <text-time-min>
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| name | user defined | Unique name for the validation |
| type | <!-- vale off -->agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, sensors, vlan or vxlan <!-- vale on -->| Protocol or service to be validated |
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

Creates an on-demand validation for various protocols and services, with results displayed inline.

### Syntax

```
netq add validation
    type (agents | bgp | evpn | interfaces | mlag | mtu | ntp | ospf | sensors | vlan | vxlan)
    [alert-on-failure]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| type | agents, bgp, evpn, interfaces, mlag, mtu, ntp, ospf, sensors, vlan or vxlan | Protocol or service to be validated |

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

Load the installation program onto the network switches and hosts in either a single server or server cluster arrangement. This command is the same for any deployment model.

### Syntax

```
netq bootstrap master
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    tarball <text-tarball-name>
    [pod-ip-range <text-master-ip>]

netq bootstrap worker
    tarball <text-tarball-name>
    master-ip <text-master-ip>
    [password <text-password>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| master | NA | Load the installation program onto the single NetQ server or master server in a cluster |
| interface | \<text-opta-ifname\> | Name of the interface on the NetQ appliance or VM where the server listens for NetQ Agents |
| ip-addr | \<text-ip-addr\> | IP address of the interface on the NetQ appliance or VM where the server listens for NetQ Agents |
| worker | NA | Load the installation program onto worker nodes in a NetQ server cluster |
| tarball | \<text-tarball-name\> | Full path of the installation file; for example, */mnt/installables/netq-bootstrap-4.0.0.tgz* |
| master-ip | \<text-master-ip\> | IP address fo the master server in a NetQ server cluster |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| pod-ip-range | \<<text-master-ip\> | Change the IP address range to this range for Flannel container environments when you have a conflict. NetQ overrides the default Flannel address range (10.1.0.0/16) with 10.244.0.0/16. |
| password | \<text-password\> | Passphrase for access to the worker node |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.2.0 | Added `pod-ip-range` option to master form of command |
| 3.1.0 | Added `password` option to worker form of command |
| 2.4.1 | Added `ip-addr` option |
| 2.4.0 | Introduced |

### Sample Usage

Bootstrap single server or master server in a server cluster

```
cumulus@switch:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-4.0.0.tgz
```

Bootstrap worker node in server cluster

```
cumulus@switch:~$ netq bootstrap worker tarball /mnt/installables/netq-bootstrap-4.0.0.tgz  master-ip 192.168.10.20
```

### Related Commands

- netq bootstrap reset
- netq bootstrap master upgrade

- - -

## netq bootstrap reset

Reset the node to prepare it for loading the installation program. In on-premises deployments with database on site, you can choose whether to save the current data or discard it (default) during the reset process. All data is saved by default in remotely hosted database deployments.

### Syntax

```
netq bootstrap reset
    [keep-db | purge-db]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| keep-db | NA | Save existing data before resetting the node. Only applies to deployments with local databases. |
| purge-db | NA | Discard existing data when resetting the node. Only applies to deployments with local databases. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Added `keep-db` and `purge-db` options |
| 2.4.0 | Introduced |

### Sample Usage

Prepare node for bootstrapping (purge data)

```
cumulus@switch:~$ netq bootstrap reset
```

Prepare node for bootstrapping while keeping existing data

```
cumulus@switch:~$ netq bootstrap reset keep-db
```

### Related Commands

- netq bootstrap
- netq bootstrap master upgrade

- - -

## netq bootstrap master upgrade

Loads master node with a new NetQ installer in an existing server cluster deployment.

{{%notice note%}}

This command applies only when upgrading from NetQ 3.1.1 and earlier.

{{%/notice%}}

### Syntax

```
netq bootstrap master upgrade
    <text-tarball-name>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-tarball-name\> | Full path of the installation file; for example, */mnt/installables/netq-bootstrap-4.0.0.tgz*  |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

Basic bootstrap

```
cumulus@switch:~$ netq bootstrap master upgrade mnt/installables/netq-bootstrap-4.0.0.tgz
```

### Related Commands

- netq bootstrap
- netq bootstrap reset

- - -
