---
title: Integrate with Third-party Software and Hardware
author: Cumulus Networks
weight: 73
aliases:
 - /display/NETQ/Integrate+with+Third-party+Software+and+Hardware
 - /pages/viewpage.action?pageId=10456260
pageID: 10456260
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
After you have installed NetQ applications package and the NetQ Agents,
you may want to configure some of the additional capabilities that NetQ
offers. This topic describes how to install, setup, and configure these
capabilities.

## <span id="src-10456260_IntegratewithThird-partySoftwareandHardware-IntegrateNotification" class="confluence-anchor-link"></span><span>Integrate NetQ with an Event Notification Application</span>

<span style="color: #000000;"> To take advantage of the numerous event
messages generated and processed by NetQ, you must integrate with
third-party event notification applications </span> . You can integrate
NetQ with the PagerDuty and Slack tools. You may integrate with one or
both of these applications.

Each network protocol and service in the NetQ Platform receives the raw
data stream <span style="color: #ff0000;">
<span style="color: #000000;"> from the NetQ Agents, processes the data
and delivers events to the Notification function. Notification then
stores, filters </span> </span> and sends messages to any configured
notification applications <span style="color: #000000;"> . Filters are
based on rules you create. You must have at least one rule per filter.
</span>

{{% imgOld 0 %}}

Notifications are generated for the following types of events:

  - Network Protocols
    
      - BGP status and session state
    
      - CLAG (MLAG) status and session state
    
      - EVPN status and session state
    
      - LLDP status
    
      - LNV status and session state \*
    
      - OSFP status and session state \*
    
      - VLAN status and session state \*
    
      - VXLAN status and session state \*

  - Interfaces
    
      - Link status
    
      - Ports and cables status

  - Services status
    
      - NetQ Agent status
    
      - SSH \*
    
      - NTP status \*

  - Trace status

  - Sensors
    
      - Fan status
    
      - PSU (power supply unit) status
    
      - Temperature status

  - System
    
      - Configuration File changes
    
      - Cumulus Linux License status \*
    
      - Cumulus Linux Support status

*\* This type of event can only be viewed in the CLI with this release.*

### <span>Event Message Format</span>

Messages have the following structure:
`<message-type><timestamp><opid><hostname><severity><message>`

| Element      | Description                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| message type | Category of event; *bgp, clag, configdiff, evpn, link, lldp, lnv, node, ntp, ospf, port, sensor, services, trace, vlan or vxlan* |
| timestamp    | Date and time event occurred                                                                                                     |
| opid         | Identifier of the service or process that generated the event                                                                    |
| hostname     | Hostname of network device where event occurred                                                                                  |
| severity     | Severity level in which the given event is classified; *debug*, *error*, *info*, *warning,* or *critical*                        |
| message      | Text description of event                                                                                                        |

For example:

{{% imgOld 1 %}}

To set up the integrations, you must configure NetQ with channels, rules
and filters to tell NetQ what messages you want to view and where to
send them. This is accomplished using the NetQ CLI in the following
manner:

{{% imgOld 2 %}}

### <span>Notification Commands Overview</span>

The NetQ Command Line Interface (CLI) is used to filter and send
notifications to third-party tools based on severity, service,
event-type, and device. You can use TAB completion or the `help` keyword
to assist when needed. The command syntax is:

    ##Channels
    netq add notification channel slack <text-channel-name> webhook <text-webhook-url> [severity info|severity warning|severity error|severity debug] [tag <text-slack-tag>]
    netq add notification channel pagerduty <text-channel-name> integration-key <text-integration-key> [severity info|severity warning|severity error|severity debug]
     
    ##Rules and Filters
    netq add notification rule <text-rule-name> key <text-rule-key> value <text-rule-value>
    netq add notification filter <text-filter-name> [severity info|severity warning|severity error|severity debug] [rule <text-rule-name-anchor>] [channel <text-channel-name-anchor>] [before <text-filter-name-anchor>|after <text-filter-name-anchor>]
     
    ##Management
    netq del notification channel <text-channel-name-anchor>
    netq del notification filter <text-filter-name-anchor>
    netq del notification rule <text-rule-name-anchor>
    netq show notification [channel|filter|rule] [json]

The options are described in the following sections where they are used.

### <span>Create Channels</span>

Create one or more PagerDuty and Slack channels to present the
notifications.

#### <span id="src-10456260_IntegratewithThird-partySoftwareandHardware-PDcli" class="confluence-anchor-link"></span><span>Configure a PagerDuty Channel</span>

NetQ sends notifications to PagerDuty as PagerDuty events.

For example:

{{% imgOld 3 %}}

To configure the NetQ notifier to send notifications to PagerDuty:

1.  Configure the following options using the `netq``  add notification
    channel ` command:
    
    | Option                                   | Description                                                                                                                                                        |
    | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | CHANNEL\_TYPE \<text-channel-name\>      | The third-party notification channel and name; use *pagerduty* in this case.                                                                                       |
    | integration-key \<text-integration-key\> | The [integration](https://v2.developer.pagerduty.com/docs/events-api-v2) key is also called the service\_key or routing\_key. The default is an empty string (""). |
    | severity                                 | (Optional) The log level to set, which can be one of *info*, *warning*, *error*, *critical* or *debug*. The severity defaults to *info*.                           |
    

        cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key c6d666e210a8425298ef7abde0d1998
        Successfully added/updated channel pd-netq-events

2.  Verify that the channel is configured properly.
    
    ``` 
    cumulus@switch:~$ netq show notification channel
    Matching config_notify records:
    Name            Type             Severity         Channel Info
    --------------- ---------------- ---------------- ------------------------
    pd-netq-events  pagerduty        info             integration-key: c6d666e
                                                      210a8425298ef7abde0d1998      
    ```

#### <span>Configure a Slack Channel</span>

NetQ Notifier sends notifications to Slack as incoming webhooks for a
Slack channel you configure. For example:

{{% imgOld 4 %}}

To configure NetQ to send notifications to Slack:

1.  If needed, create one or more Slack channels on which to receive the
    notifications.
    
    1.  Click **+** next to **Channels**.
    
    2.  Enter a name for the channel, and click **Create Channel**.
    
    3.  Navigate to the new channel.
    
    4.  Click **+ Add an app** link below the channel name to open the
        application directory.
    
    5.  In the search box, start typing *incoming* and select **
        **Incoming WebHooks** when it appears.
    
    6.  Click **Add Configuration** and enter the name of the channel
        you created (where you want to post notifications).
    
    7.  Click **Add Incoming WebHooks integration**.
    
    8.  Save WebHook URL in a text file for use in next step.

2.  Configure the following options in the ` netq  ``config add
    notification channel` command:
    
    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>CHANNEL_TYPE &lt;text-channel-name&gt;</p></td>
    <td><p>The third-party notification channel name; use <em>slack</em> in this case.</p></td>
    </tr>
    <tr class="even">
    <td><p>WEBHOOK</p></td>
    <td><p>Copy the WebHook URL from the text file OR in the desired channel, locate the initial message indicating the addition of the webhook, click <strong>incoming-webhook</strong> link, click <strong>Settings</strong>.</p>
    <p>Example URL: <code>https://hooks.slack.com/services/text/moretext/evenmoretext</code></p></td>
    </tr>
    <tr class="odd">
    <td><p>severity</p></td>
    <td><p>The log level to set, which can be one of <em>error, warning, info,</em> or <em>debug</em>. The severity defaults to <em>info</em>.</p></td>
    </tr>
    <tr class="even">
    <td><p>tag</p></td>
    <td><p>Optional tag appended to the Slack notification to highlight particular channels or people. The tag value must be preceded by the @ sign. For example, <em>@netq-info</em>.</p></td>
    </tr>
    </tbody>
    </table>
    
        cumulus@switch:~$ netq add notification channel slack slk-netq-events webhook https://hooks.slack.com/services/text/moretext/evenmoretext
        Successfully added/updated channel netq-events

3.  Verify the channel is configured correctly.  
    From the CLI:
    
    ``` 
    cumulus@switch:~$ netq show notification channel 
    Matching config_notify records:
    Name            Type             Severity Channel Info
    --------------- ---------------- -------- ----------------------
    slk-netq-events slack            info     webhook:https://hooks.s
                                              lack.com/services/text/
                                              moretext/evenmoretext                                     
    ```
    
    From the Slack Channel:  
      
    
    {{% imgOld 5 %}}

### <span id="src-10456260_IntegratewithThird-partySoftwareandHardware-FilterRule" class="confluence-anchor-link"></span><span>Create Rules </span>

Each rule is comprised of a single key-value pair. The key-value pair
indicates what messages to include or drop from event information sent
to a notification channel. You can create more than one rule for a
single filter. Creating multiple rules for a given filter can provide a
very defined filter. For example, you can specify rules around hostnames
or interface names, enabling you to filter messages specific to those
hosts or interfaces. You should have already defined the PagerDuty or
Slack channels (as described earlier).

There is a fixed set of valid rule keys. Values are entered as regular
expressions and *vary according to your deployment*.

Service

Rule Key

Description

Example Rule Values

BGP

message\_type

Network protocol or service identifier

bgp

hostname

User-defined, text-based name for a switch or host

server02, leaf11, exit01, spine-4

peer

User-defined, text-based name for a peer switch or host

server4, leaf-3, exit02, spine06

desc

Text description

 

vrf

Name of VRF interface

mgmt, default

old\_state

Previous state of the BGP service

Established, Failed

new\_state

Current state of the BGP service

Established, Failed

old\_last\_reset\_time

Previous time that BGP service was reset

Apr3, 2019, 4:17 pm

new\_last\_reset\_time

Most recent time that BGP service was reset

Apr8, 2019, 11:38 am

MLAG (CLAG)

message\_type

Network protocol or service identifier

<span style="color: #000000;"> clag </span>

hostname

User-defined, text-based name for a switch or host

server02, leaf-9, exit01, spine04

old\_conflicted\_bonds

Previous pair of interfaces in a conflicted bond

swp7 swp8, swp3 swp4

new\_conflicted\_bonds

Current pair of interfaces in a conflicted bond

swp11 swp12, swp23 swp24

old\_state\_protodownbond

Previous state of the bond

protodown, up

new\_state\_protodownbond

Current state of the bond

protodown, up

ConfigDiff

message\_type

Network protocol or service identifier

configdiff

hostname

User-defined, text-based name for a switch or host

server02, leaf11, exit01, spine-4

vni

Virtual Network Instance identifier

12, 23

old\_state

Previous state of the configuration file

created, modified

new\_state

Current state of the configuration file

created, modified

EVPN

message\_type

Network protocol or service identifier

evpn

hostname

User-defined, text-based name for a switch or host

server02, leaf-9, exit01, spine04

vni

Virtual Network Instance identifier

12, 23

old\_in\_kernel\_state

Previous VNI state, in kernel or not

true, false

new\_in\_kernel\_state

Current VNI state, in kernel or not

true, false

old\_adv\_all\_vni\_state

Previous VNI advertising state, advertising all or not

true, false

new\_adv\_all\_vni\_state

Current VNI advertising state, advertising all or not

true, false

Link

message\_type

Network protocol or service identifier

<span style="color: #000000;"> link </span>

hostname

User-defined, text-based name for a switch or host

server02, leaf-6, exit01, spine7

ifname

Software interface name

<span style="color: #000000;"> eth0, swp53 </span>

LLDP

message\_type

Network protocol or service identifier

<span style="color: #000000;"> lldp </span>

 

hostname

User-defined, text-based name for a switch or host

server02, leaf41, exit01, spine-5, tor-36

 

ifname

Software interface name

eth1, swp12

 

old\_peer\_ifname

Previous software interface name

eth1, swp12, swp27

 

new\_peer\_ifname

Curent software interface name

eth1, swp12, swp27

 

old\_peer\_hostname

Previous user-defined, text-based name for a peer switch or host

server02, leaf41, exit01, spine-5, tor-36

 

new\_peer\_hostname

Current user-defined, text-based name for a peer switch or host

server02, leaf41, exit01, spine-5, tor-36

Node

message\_type

Network protocol or service identifier

node

 

hostname

User-defined, text-based name for a switch or host

server02, leaf41, exit01, spine-5, tor-36

 

ntp\_state

Current state of NTP service

in sync, not sync

 

db\_state

Current state of DB

Add, Update, Del, Dead

NTP

message\_type

Network protocol or service identifier

ntp

 

hostname

User-defined, text-based name for a switch or host

server02, leaf-9, exit01, spine04

 

old\_state

Previous state of service

in sync, not sync

 

new\_state

Current state of service

in sync, not sync

Port

message\_type

Network protocol or service identifier

<span style="color: #000000;"> port </span>

 

hostname

User-defined, text-based name for a switch or host

server02, leaf13, exit01, spine-8, tor-36

 

ifname

Interface name

<span style="color: #000000;"> eth0, swp14 </span>

 

old\_speed

Previous speed rating of port

10 G, 25 G, 40 G, unknown

 

old\_transreceiver

Previous transceiver

<span style="color: #000000;"> 40G Base-CR4,
<span style="color: #000000;"> 25G Base-CR </span> </span>

 

old\_vendor\_name

Previous vendor name of installed port module

Amphenol, OEM, Mellanox, Fiberstore, Finisar

 

old\_serial\_number

Previous serial number of installed port module

<span style="color: #000000;"> MT1507VS05177,
<span style="color: #000000;"> AVE1823402U,
<span style="color: #000000;"> PTN1VH2 </span> </span> </span>

 

old\_supported\_fec

Previous forward error correction (FEC) support status

none, Base R, RS

 

old\_advertised\_fec

Previous FEC advertising state

true, false, not reported

 

old\_fec

Previous FEC capability

none

 

old\_autoneg

Previous activation state of auto-negotiation

on, off

 

new\_speed

Current speed rating of port

10 G, 25 G, 40 G

 

new\_transreceiver

Current transceiver

<span style="color: #000000;"> 40G Base-CR4, </span>
<span style="color: #000000;"> 25G Base-CR </span>

 

new\_vendor\_name

Current vendor name of installed port module

Amphenol, OEM, Mellanox, Fiberstore, Finisar

 

new\_part\_number

Current part number of installed port module

<span style="color: #000000;"> SFP-H10GB-CU1M,
<span style="color: #000000;"> MC3309130-001,
<span style="color: #000000;"> 603020003 </span> </span> </span>

 

new\_serial\_number

Current serial number of installed port module

<span style="color: #000000;"> MT1507VS05177, </span>
<span style="color: #000000;"> AVE1823402U, PTN1VH2 </span>

 

new\_supported\_fec

Current FEC support status

none, Base R, RS

 

new\_advertised\_fec

Current FEC advertising state

true, false

 

new\_fec

Current FEC capability

none

 

new\_autoneg

Current activation state of auto-negotiation

on, off

Sensors

sensor

Network protocol or service identifier

<span style="color: #000000;"> <span style="color: #000000;"> Fan:
</span> <span style="color: #000000;"> fan1, fan-2 </span>  
Power Supply Unit: psu1, psu2  
Temperature: psu1temp1, temp2  
</span>

 

hostname

User-defined, text-based name for a switch or host

server02, leaf-26, exit01, spine2-4

 

old\_state

Previous state of a fan, power supply unit, or thermal sensor

Fan: ok, absent, bad  
PSU: ok, absent, bad  
Temp: ok, busted, bad, critical

 

new\_state

Current state of a fan, power supply unit, or thermal sensor

Fan: ok, absent, bad  
PSU: ok, absent, bad  
Temp: ok, busted, bad, critical

 

old\_s\_state

Previous state of a fan or power supply unit.

Fan: up, down  
PSU: up, down

 

new\_s\_state

Current state of a fan or power supply unit.

Fan: up, down  
PSU: up, down

 

new\_s\_max

Current maximum temperature threshold value

Temp: 110

 

new\_s\_crit

Current critical high temperature threshold value

Temp: 85

 

new\_s\_lcrit

Current critical low temperature threshold value

Temp: -25

 

new\_s\_min

Current minimum temperature threshold value

Temp: -50

Services

message\_type

Network protocol or service identifier

services

 

hostname

User-defined, text-based name for a switch or host

<span style="color: #000000;"> server02, leaf03, exit01, spine-8 </span>

 

name

Name of service

clagd, lldpd, ssh, ntp, netqd, net-agent

 

old\_pid

Previous process or service identifier

12323, 52941

 

new\_pid

Current process or service identifier

12323, 52941

 

old\_status

Previous status of service

up, down

 

new\_status

Current status of service

up, down

{{%notice info%}}

Rule names are case sensitive, and no wildcards are permitted. Rule
names may contain spaces, but must be enclosed with single quotes in
commands. It is easier to use dashes in place of spaces or mixed case
for better readability. For example, use bgpSessionChanges or
BGP-session-changes or BGPsessions, instead of 'BGP Session Changes'.

Use Tab completion to view the command options syntax.

{{%/notice%}}

#### <span>Example Rules</span>

Create a BGP Rule Based on Hostname:

    cumulus@switch:~$ netq add notification rule bgpHostname key hostname value spine-01 
    Successfully added/updated rule bgpHostname 

Create a Rule Based on a Configuration File State Change:

    cumulus@switch:~$ netq add notification rule sysconf key configdiff value updated
    Successfully added/updated rule sysconf

Create an EVPN Rule Based on a VNI:

    cumulus@switch:~$ netq add notification rule evpnVni key vni value 42
    Successfully added/updated rule evpnVni

Create an Interface Rule Based on FEC Support:

    cumulus@switch:~$ netq add notification rule fecSupport key new_supported_fec value supported
    Successfully added/updated rule fecSupport

Create a Service Rule Based on a Status Change:

    cumulus@switch:~$ netq add notification rule svcStatus key new_status value down
    Successfully added/updated rule svcStatus

Create a Sensor Rule Based on a Threshold:

    cumulus@switch:~$ netq add notification rule overTemp key new_s_crit value 24
    Successfully added/updated rule overTemp

Create an Interface Rule Based on Port:

    cumulus@switch:~$ netq add notification rule swp52 key port value swp52 
    Successfully added/updated rule swp52 

#### <span>View the Rule Configurations</span>

Use the `netq show notification` command to view the rules on your
platform.

    cumulus@switch:~$ netq show notification rule 
     
    Matching config_notify records:
    Name            Rule Key         Rule Value
    --------------- ---------------- --------------------
    bgpHostname     hostname         spine-01
    evpnVni         vni              42
    fecSupport      new_supported_fe supported
                    c
    overTemp        new_s_crit       24
    svcStatus       new_status       down
    swp52           port             swp52
    sysconf         configdiff       updated

### <span id="src-10456260_IntegratewithThird-partySoftwareandHardware-NotifierFilters" class="confluence-anchor-link"></span><span>Create Filters</span>

You can limit or direct event messages using filters. Filters are
created based on rules you define; like those in the previous section.
Each filter contains one or more rules. When a message matches the rule,
it is sent to the indicated destination. Before you can create filters,
you need to have already defined the rules and configured PagerDuty
and/or Slack channels (as described earlier).

As filters are created, they are added to the bottom of a filter list.
By default, filters are processed in the order they appear in this list
(from top to bottom) until a match is found. This means that each event
message is first evaluated by the first filter listed, and if it matches
then it is processed, ignoring all other filters, and the system moves
on to the next event message received. If the event does not match the
first filter, it is tested against the second filter, and if it matches
then it is processed and the system moves on to the next event received.
And so forth. Events that do not match any filter are ignored.

You may need to change the order of filters in the list to ensure you
capture the events you want and drop the events you do not want. This is
possible using the *before* or *after* keywords to ensure one rule is
processed before or after another.

This diagram shows an example with four defined filters with sample
output results.

{{% imgOld 6 %}}

{{%notice info%}}

Filter names may contain spaces, but *must* be enclosed with single
quotes in commands. It is easier to use dashes in place of spaces or
mixed case for better readability. For example, use bgpSessionChanges or
BGP-session-changes or BGPsessions, instead of 'BGP Session Changes'.
Filter names are also case sensitive.

{{%/notice%}}

#### <span>Example Filters</span>

Create a filter for BGP Events on a Particular Device:

    cumulus@switch:~$ netq add notification filter bgpSpine rule bgpHostname channel pd-netq-events 
    Successfully added/updated filter bgpSpine

Create a Filter for a Given VNI in Your EVPN Overlay:

    cumulus@switch:~$ netq add notification filter vni42 severity warning rule evpnVni channel pd-netq-events
    Successfully added/updated filter vni42

Create a Filter for when a Configuration File has been Updated:

    cumulus@switch:~$ netq add notification filter configChange severity info rule sysconf channel slk-netq-events
    Successfully added/updated filter configChange

Create a Filter to Monitor Ports with FEC Support:

    cumulus@switch:~$ netq add notification filter newFEC rule fecSupport channel slk-netq-events
    Successfully added/updated filter newFEC

Create a Filter to Monitor for Services that Change to a Down State:

    cumulus@switch:~$ netq add notification filter svcDown severity error rule svcStatus channel slk-netq-events
    Successfully added/updated filter svcDown

Create a Filter to Monitor Overheating Platforms:

    cumulus@switch:~$ netq add notification filter critTemp severity error rule overTemp channel pd-netq-events 
    Successfully added/updated filter critTemp

Create a Filter to Drop Messages from a Given Interface, and match
against this filter before any other filters. To create a drop style
filter, do not specify a channel. To put the filter first, use the
*before* option.

    cumulus@switch:~$ netq add notification filter swp52Drop severity error rule swp52 before bgpSpine
    Successfully added/updated filter swp52Drop

#### <span>View the Filter Configurations</span>

Use the `netq show notification` command to view the filters on your
platform.

    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    swp52Drop       1          error            NetqDefaultChann swp52
                                                el
    bgpSpine        2          info             pd-netq-events   bgpHostnam
                                                                 e
    vni42           3          warning          pd-netq-events   evpnVni
    configChange    4          info             slk-netq-events  sysconf
    newFEC          5          info             slk-netq-events  fecSupport
    svcDown         6          critical         slk-netq-events  svcStatus
    critTemp        7          critical         pd-netq-events   overTemp

#### <span>Reorder Filters</span>

When you look at the results of the `netq show notification filter`
command above, you might notice that although you have the drop-based
filter first (no point in looking at something you are going to drop
anyway, so that is good), but the critical severity events are processed
last, per the current definitions. If you wanted to process those before
lesser severity events, you can reorder the list using the *before* and
*after* options.

For example, to put the two critical severity event filters just below
the drop filter:

    cumulus@switch:~$ netq add notification filter critTemp after swp52Drop
    Successfully added/updated filter critTemp
    cumulus@switch:~$ netq add notification filter svcDown before bgpSpine
    Successfully added/updated filter svcDown

{{%notice tip%}}

You do not need to reenter all the severity, channel, and rule
information for existing rules if you only want to change their
processing order.

{{%/notice%}}

Run the `netq show notification` command again to verify the changes:

    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    swp52Drop       1          error            NetqDefaultChann swp52
                                                el
    critTemp        2          critical         pd-netq-events   overTemp
    svcDown         3          critical         slk-netq-events  svcStatus
    bgpSpine        4          info             pd-netq-events   bgpHostnam
                                                                 e
    vni42           5          warning          pd-netq-events   evpnVni
    configChange    6          info             slk-netq-events  sysconf
    newFEC          7          info             slk-netq-events  fecSupport

## <span>Example Notification Configurations</span>

Putting all of these channel, rule, and filter definitions together you
create a complete notification configuration. The following are example
notification configurations are created using the three-step process
outlined above. Refer to [Integrate NetQ with an Event Notification
Application](#src-10456260_IntegratewithThird-partySoftwareandHardware-IntegrateNotification)
for details and instructions for creating channels, rules, and filters.

### <span>Create a Notification for BGP Events from a Selected Switch</span>

In this example, we created a notification integration with a PagerDuty
channel called *pd-netq-events*. We then created a rule *bgpHostname*
and a filter called *4bgpSpine* for any notifications from *spine-01*.
The result is that any info severity event messages from Spine-01 are
filtered to the *pd-netq-events* ** channel.

    cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key 1234567890
    Successfully added/updated channel pd-netq-events
    cumulus@switch:~$ netq add notification rule bgpHostname key node value spine-01
    Successfully added/updated rule bgpHostname
     
    cumulus@switch:~$ netq add notification filter bgpSpine rule bgpHostname channel pd-netq-events
    Successfully added/updated filter bgpSpine
    cumulus@switch:~$ netq show notification channel
    Matching config_notify records:
    Name            Type             Severity         Channel Info
    --------------- ---------------- ---------------- ------------------------
    pd-netq-events  pagerduty        info             integration-key: 1234567
                                                      890   
                                                                                  
    cumulus@switch:~$ netq show notification rule 
    Matching config_notify records:
    Name            Rule Key         Rule Value
    --------------- ---------------- --------------------
    bgpHostname     hostname         spine-01
     
    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    bgpSpine        1          info             pd-netq-events   bgpHostnam
                                                                 e

### <span>Create a Notification for Warnings on a Given EVPN VNI</span>

In this example, we created a notification integration with a PagerDuty
channel called *pd-netq-events*. We then created a rule *evpnVni* and a
filter called *3vni42* for any warnings messages from VNI 42 on the EVPN
overlay network. The result is that any warning severity event messages
from VNI 42 are filtered to the *pd-netq-events* ** channel.

    cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key 1234567890
    Successfully added/updated channel pd-netq-events
     
    cumulus@switch:~$ netq add notification rule evpnVni key vni value 42
    Successfully added/updated rule evpnVni
     
    cumulus@switch:~$ netq add notification filter vni42 rule evpnVni channel pd-netq-events
    Successfully added/updated filter vni42
     
    cumulus@switch:~$ netq show notification channel
    Matching config_notify records:
    Name            Type             Severity         Channel Info
    --------------- ---------------- ---------------- ------------------------
    pd-netq-events  pagerduty        info             integration-key: 1234567
                                                      890   
                                                                                  
    cumulus@switch:~$ netq show notification rule 
    Matching config_notify records:
    Name            Rule Key         Rule Value
    --------------- ---------------- --------------------
    bgpHostname     hostname         spine-01
    evpnVni         vni              42
     
    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    bgpSpine        1          info             pd-netq-events   bgpHostnam
                                                                 e
    vni42           2          warning          pd-netq-events   evpnVni

### <span>Create a Notification for Configuration File Changes</span>

In this example, we created a notification integration with a Slack
channel called *slk-netq-events*. We then created a rule *sysconf* and a
filter called *configChange* for any configuration file update messages.
The result is that any configuration update messages are filtered to the
*slk-netq-events* ** channel.

    cumulus@switch:~$ netq add notification channel slack slk-netq-events webhook https://hooks.slack.com/services/text/moretext/evenmoretext
    Successfully added/updated channel slk-netq-events
     
    cumulus@switch:~$ netq add notification rule sysconf key configdiff value updated
    Successfully added/updated rule sysconf
     
    cumulus@switch:~$ netq add notification filter configChange severity info rule sysconf channel slk-netq-events
    Successfully added/updated filter configChange
     
    cumulus@switch:~$ netq show notification channel 
    Matching config_notify records:
    Name            Type             Severity Channel Info
    --------------- ---------------- -------- ----------------------
    slk-netq-events slack            info     webhook:https://hooks.s
                                              lack.com/services/text/
                                              moretext/evenmoretext     
     
    cumulus@switch:~$ netq show notification rule 
    Matching config_notify records:
    Name            Rule Key         Rule Value
    --------------- ---------------- --------------------
    bgpHostname     hostname         spine-01
    evpnVni         vni              42
    sysconf         configdiff       updated
     
    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    bgpSpine        1          info             pd-netq-events   bgpHostnam
                                                                 e
    vni42           2          warning          pd-netq-events   evpnVni
    configChange    3          info             slk-netq-events  sysconf

### <span>Create a Notification for When a Service Goes Down</span>

In this example, we created a notification integration with a Slack
channel called *slk-netq-events*. We then created a rule *svcStatus* and
a filter called *svcDown* for any services state messages indicating a
service is no longer operational. The result is that any service down
messages are filtered to the *slk-netq-events* ** channel.

    cumulus@switch:~$ netq add notification channel slack slk-netq-events webhook https://hooks.slack.com/services/text/moretext/evenmoretext
    Successfully added/updated channel slk-netq-events
     
    cumulus@switch:~$ netq add notification rule svcStatus key new_status value down
    Successfully added/updated rule svcStatus
     
    cumulus@switch:~$ netq add notification filter svcDown severity error rule svcStatus channel slk-netq-events
    Successfully added/updated filter svcDown
     
    cumulus@switch:~$ netq show notification channel 
    Matching config_notify records:
    Name            Type             Severity Channel Info
    --------------- ---------------- -------- ----------------------
    slk-netq-events slack            info     webhook:https://hooks.s
                                              lack.com/services/text/
                                              moretext/evenmoretext     
     
    cumulus@switch:~$ netq show notification rule 
    Matching config_notify records:
    Name            Rule Key         Rule Value
    --------------- ---------------- --------------------
    bgpHostname     hostname         spine-01
    evpnVni         vni              42
    svcStatus       new_status       down
    sysconf         configdiff       updated
     
    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    bgpSpine        1          info             pd-netq-events   bgpHostnam
                                                                 e
    vni42           2          warning          pd-netq-events   evpnVni
    configChange    3          info             slk-netq-events  sysconf
    svcDown         4          critical         slk-netq-events  svcStatus

### <span>Create a Filter to Drop Notifications from a Given Interface</span>

In this example, we created a notification integration with a Slack
channel called *slk-netq-events*. We then created a rule *swp52* and a
filter called *swp52Drop* that drops all notifications for events from
interface *swp52*.

    cumulus@switch:~$ netq add notification channel slack slk-netq-events webhook https://hooks.slack.com/services/text/moretext/evenmoretext
    Successfully added/updated channel slk-netq-events
     
    cumulus@switch:~$ netq add notification rule swp52 key port value swp52 
    Successfully added/updated rule swp52
     
    cumulus@switch:~$ netq add notification filter swp52Drop severity error rule swp52 before bgpSpine
    Successfully added/updated filter swp52Drop
     
    cumulus@switch:~$ netq show notification channel 
    Matching config_notify records:
    Name            Type             Severity Channel Info
    --------------- ---------------- -------- ----------------------
    slk-netq-events slack            info     webhook:https://hooks.s
                                              lack.com/services/text/
                                              moretext/evenmoretext     
     
    cumulus@switch:~$ netq show notification rule 
    Matching config_notify records:
    Name            Rule Key         Rule Value
    --------------- ---------------- --------------------
    bgpHostname     hostname         spine-01
    evpnVni         vni              42
    svcStatus       new_status       down
    swp52           port             swp52
    sysconf         configdiff       updated
     
    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    swp52Drop       1          error            NetqDefaultChann swp52
                                                el
    bgpSpine        2          info             pd-netq-events   bgpHostnam
                                                                 e
    vni42           3          warning          pd-netq-events   evpnVni
    configChange    4          info             slk-netq-events  sysconf
    svcDown         5          critical         slk-netq-events  svcStatus

### <span>Create a Notification for a Given Device that has a Tendency to Overheat (using multiple rules)</span>

In this example, we created a notification when switch *leaf04* has
passed over the high temperature threshold. Two rules were needed to
create this notification, one to identify the specific device and one to
identify the temperature trigger. We sent the message to the
*pd-netq-events* channel.

``` 
cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key 1234567890
Successfully added/updated channel pd-netq-events
 
cumulus@switch:~$ netq add notification rule switchLeaf04 key hostname value leaf04
Successfully added/updated rule switchLeaf04
cumulus@switch:~$ netq add notification rule overTemp key new_s_crit value 24
Successfully added/updated rule overTemp
 
cumulus@switch:~$ netq add notification filter critTemp rule switchLeaf04 channel pd-netq-events 
Successfully added/updated filter critTemp
cumulus@switch:~$ netq add notification filter critTemp severity critical rule overTemp channel pd-netq-events
Successfully added/updated filter critTemp
 
cumulus@switch:~$ netq show notification channel 
Matching config_notify records:
Name            Type             Severity         Channel Info
--------------- ---------------- ---------------- ------------------------
pd-netq-events  pagerduty        info             integration-key: 1234567
                                                  890
        
cumulus@switch:~$ netq show notification rule 
Matching config_notify records:
Name            Rule Key         Rule Value
--------------- ---------------- --------------------
bgpHostname     hostname         spine-01
evpnVni         vni              42
overTemp        new_s_crit       24
svcStatus       new_status       down
switchLeaf04    hostname         leaf04
swp52           port             swp52
sysconf         configdiff       updated
cumulus@switch:~$ netq show notification filter
Matching config_notify records:
Name            Order      Severity         Channels         Rules
--------------- ---------- ---------------- ---------------- ----------
swp52Drop       1          error            NetqDefaultChann swp52
                                            el
bgpSpine        2          info             pd-netq-events   bgpHostnam
                                                             e
vni42           3          warning          pd-netq-events   evpnVni
configChange    4          info             slk-netq-events  sysconf
svcDown         5          critical         slk-netq-events  svcStatus
critTemp        6          critical         pd-netq-events   switchLeaf
                                                             04
                                                             overTemp                                                
```

### <span>View Notification Configurations in JSON Format</span>

You can view configured integrations using the `netq show notification`
commands. To view the channels, filters, and rules, run the three
flavors of the command. Include the `json` option to display
JSON-formatted output.

For example:

    cumulus@switch:~$ netq show notification channel json
    {
        "config_notify":[
            {
                "type":"slack",
                "name":"slk-netq-events",
                "channelInfo":"webhook:https://hooks.slack.com/services/text/moretext/evenmoretext",
                "severity":"info"
            },
            {
                "type":"pagerduty",
                "name":"pd-netq-events",
                "channelInfo":"integration-key: 1234567890",
                "severity":"info"
        }
        ],
        "truncatedResult":false
    }
     
    cumulus@switch:~$ netq show notification rule json
    {
        "config_notify":[
            {
                "ruleKey":"hostname",
                "ruleValue":"spine-01",
                "name":"bgpHostname"
            },
            {
                "ruleKey":"vni",
                "ruleValue":42,
                "name":"evpnVni"
            },
            {
                "ruleKey":"new_supported_fec",
                "ruleValue":"supported",
                "name":"fecSupport"
            },
            {
                "ruleKey":"new_s_crit",
                "ruleValue":24,
                "name":"overTemp"
            },
            {
                "ruleKey":"new_status",
                "ruleValue":"down",
                "name":"svcStatus"
            },
            {
                "ruleKey":"configdiff",
                "ruleValue":"updated",
                "name":"sysconf"
        }
        ],
        "truncatedResult":false
    }
     
    cumulus@switch:~$ netq show notification filter json
    {
        "config_notify":[
            {
                "channels":"pd-netq-events",
                "rules":"overTemp",
                "name":"1critTemp",
                "severity":"critical"
            },
            {
                "channels":"pd-netq-events",
                "rules":"evpnVni",
                "name":"3vni42",
                "severity":"warning"
            },
            {
                "channels":"pd-netq-events",
                "rules":"bgpHostname",
                "name":"4bgpSpine",
                "severity":"info"
            },
            {
                "channels":"slk-netq-events",
                "rules":"sysconf",
                "name":"configChange",
                "severity":"info"
            },
            {
                "channels":"slk-netq-events",
                "rules":"fecSupport",
                "name":"newFEC",
                "severity":"info"
            },
            {
                "channels":"slk-netq-events",
                "rules":"svcStatus",
                "name":"svcDown",
                "severity":"critical"
        }
        ],
        "truncatedResult":false
    }

## <span>Manage Event Notification Integrations</span>

<span style="color: #36424a;"> You might need to modify event
notification configurations at some point in the lifecycle of your
deployment. </span>

### <span>Remove an Event Notification Channel</span>

You can delete an event notification integration using the `netq config
del notification` command. You can verify it has been removed using the
related `show` command.

For example, to remove a Slack integration and verify it is no longer in
the configuration:

    cumulus@switch:~$ netq del notification channel slk-netq-events
    cumulus@switch:~$ netq show notification channel
    Matching config_notify records:
    Name            Type             Severity         Channel Info
    --------------- ---------------- ---------------- ------------------------
    pd-netq-events  pagerduty        info             integration-key: 1234567
                                                      890

### <span>Delete an Event Notification Rule</span>

To delete a rule, use the following command, then verify it has been
removed:

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

### <span>Delete an Event Notification Filter</span>

To delete a filter, use the following command, then verify it has been
removed:

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

## <span>Integrate with a Hardware Chassis</span>

NetQ can run within a [Facebook Backpack
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/backpack/),
[Cumulus Express CX-10256-S
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/cx10256s-omp800/)
or [Edgecore OMP-800
chassis](https://cumulusnetworks.com/products/cumulus-express/getting-started/cx10256s-omp800/).

Keep the following issues in mind if you intend to use NetQ with a
chassis:

  - You must assign a unique hostname to every node that runs the NetQ
    Agent. By default, all the fabric cards in the chassis have the same
    hostname.

  - The NetQ Agent must be installed on every line card.

  - No information is returned about the ASIC when you run `netq show
    inventory asic`. This is a known issue.

  - Since the chassis sensor information is shared, every line card and
    fabric card can report the same sensor data. By default, sensor data
    is disabled on a chassis <span style="color: #000000;"> to avoid
    this duplication </span> . To enable sensor data on a line card,
    edit `/etc/netq/netq.yml` or `/etc/netq/config.d/user.yml` and set
    the `send_chassis_sensor_data` keyword to *true*, then restart the
    NetQ Agent with `netq config agent restart`. Configuring NetQ in
    this way prevents any duplication of data in the NetQ database.
    
        cumulus@chassis:~$ sudo nano /etc/netq/netq.yml
         
        ...
        netq-agent:
          send_chassis_sensor_data: true
        ...
