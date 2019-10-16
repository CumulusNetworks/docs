---
title: Integrate with Event Notification Applications
author: Cumulus Networks
weight: 200
aliases:
 - /display/NETQ/Integrate+with+Third-party+Software+and+Hardware
 - /pages/viewpage.action?pageId=12320911
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
After you have installed NetQ applications package and the NetQ Agents,
you may want to configure some of the additional capabilities that NetQ
offers. This topic describes how to install, setup, and configure these
capabilities.

## Integrate NetQ with an Event Notification Application

To take advantage of the numerous event messages generated and processed
by NetQ, you must integrate with third-party event notification
applications. You can integrate NetQ with the PagerDuty and Slack tools.
You may integrate with one or both of these applications.

Each network protocol and service in the NetQ Platform receives the raw
data stream from the NetQ Agents, processes the data and delivers events
to the Notification function. Notification then stores, filters and
sends messages to any configured notification applications. Filters are
based on rules you create. You must have at least one rule per filter.

{{<figure src="/images/netq/event-notif-arch.png">}}

{{%notice note%}}

You may choose to implement a proxy server (that sits between the NetQ
Platform and the integration channels) that receives, processes and
distributes the notifications rather than having them sent directly to
the integration channel. If you use such a proxy, you must configure
NetQ with the proxy information.

{{%/notice%}}

In either case, notifications are generated for the following types of
events:

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
      - PTM
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

### Event Message Format

Messages have the following structure:
`<message-type><timestamp><opid><hostname><severity><message>`

| Element      | Description                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| message type | Category of event; *bgp*, *clag*, *configdiff*, *evpn*, *link*, *lldp*, *lnv*, *node*, *ntp*, *ospf*, *port*, *sensor*, *services*, *trace*, *vlan* or *vxlan* |
| timestamp    | Date and time event occurred                                                                                                     |
| opid         | Identifier of the service or process that generated the event                                                                    |
| hostname     | Hostname of network device where event occurred                                                                                  |
| severity     | Severity level in which the given event is classified; *debug*, *error*, *info*, *warning,* or *critical*                        |
| message      | Text description of event                                                                                                        |

For example:

{{<figure src="/images/netq/event-msg-format.png">}}

To set up the integrations, you must configure NetQ with at least one
channel. Optionally, you can define rules and filters to refine what
messages you want to view and where to send them. You can also configure
a proxy server to receive, process, and forward the messages. This is
accomplished using the NetQ CLI in the following order:

{{<figure src="/images/netq/notif-config-wkflow.png">}}

### Notification Commands Overview

The NetQ Command Line Interface (CLI) is used to filter and send
notifications to third-party tools based on severity, service,
event-type, and device. You can use TAB completion or the `help` option
to assist when needed. The command syntax is:

    ##Proxy
    netq add notification proxy <text-proxy-hostname> [port <text-proxy-port>]
    netq show notification proxy
    netq del notification proxy
     
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

### Configure a Proxy Server

To send notification messages through a proxy server instead of directly
to a notification channel, you configure NetQ with the hostname and
optionally a port of a proxy server. If no port is specified, NetQ
defaults to port 80. Only one proxy server is currently supported. To
simplify deployment, configure your proxy server before configuring
channels, rules, or filters.To configure the proxy server:

    cumulus@switch:~$ netq add notification proxy <text-proxy-hostname> [port <text-proxy-port]
    cumulus@switch:~$ netq add notification proxy proxy4
    Successfully configured notifier proxy proxy4:80

You can view the proxy server settings by running the `netq show
notification proxy` command.

    cumulus@switch:~$ netq show notification proxy
    Matching config_notify records:
    Proxy URL          Slack Enabled              PagerDuty Enabled
    ------------------ -------------------------- ----------------------------------
    proxy4:80          yes                        yes

You can remove the proxy server by running the `netq del notification
proxy` command. This changes the NetQ behavior to send events directly
to the notification channels.

    cumulus@switch:~$ netq del notification proxy
    Successfully overwrote notifier proxy to null

### Create Channels

Create one or more PagerDuty and Slack channels to present the
notifications.

#### Configure a PagerDuty Channel

NetQ sends notifications to PagerDuty as PagerDuty events.

For example:

{{<figure src="/images/netq/NetQ-PagerDuty-ex-output.png">}}

To configure the NetQ notifier to send notifications to PagerDuty:

1.  Configure the following options using the `netq add notification
    channel` command:

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

#### Configure a Slack Channel

NetQ Notifier sends notifications to Slack as incoming webhooks for a
Slack channel you configure. For example:

{{<figure src="/images/netq/slack-ex-output.png">}}

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

2.  Configure the following options in the ` netq config add
    notification channel` command:

    <table>
    <colgroup>
    <col style="width: 20%" />
    <col style="width: 80%" />
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


    {{<figure src="/images/netq/slack-add-webhook-ex.png">}}

### Create Rules

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

<table class="confluenceTable">

<thead class=" ">

<tr>

<td class="confluenceTh" rowspan="1" colspan="1">

Service

</td>

<td class="confluenceTh" rowspan="1" colspan="1">

Rule Key

</td>

<td class="confluenceTh" rowspan="1" colspan="1">

Description

</td>

<td class="confluenceTh" rowspan="1" colspan="1">

Example Rule Values

</td>

</tr>

</thead>

<tfoot class=" ">

</tfoot>

<tbody class=" ">

<tr>

<td class="confluenceTd" rowspan="9" colspan="1">

BGP

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

bgp

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf11, exit01, spine-4

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

peer

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a peer switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server4, leaf-3, exit02, spine06

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

desc

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Text description

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

 

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

vrf

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Name of VRF interface

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

mgmt, default

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous state of the BGP service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Established, Failed

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of the BGP service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Established, Failed

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_last_reset_time

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous time that BGP service was reset

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Apr3, 2019, 4:17 pm

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_last_reset_time

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Most recent time that BGP service was reset

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Apr8, 2019, 11:38 am

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="6" colspan="1">

MLAG (CLAG)

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

clag

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf-9, exit01, spine04

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_conflicted_bonds

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous pair of interfaces in a conflicted bond

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

swp7 swp8, swp3 swp4

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_conflicted_bonds

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current pair of interfaces in a conflicted bond

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

swp11 swp12, swp23 swp24

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_state_protodownbond

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous state of the bond

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

protodown, up

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_state_protodownbond

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of the bond

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

protodown, up

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="5" colspan="1">

ConfigDiff

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

configdiff

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf11, exit01, spine-4

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

vni

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Virtual Network Instance identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

12, 23

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous state of the configuration file

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

created, modified

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of the configuration file

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

created, modified

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="7" colspan="1">

EVPN

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

evpn

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf-9, exit01, spine04

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

vni

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Virtual Network Instance identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

12, 23

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_in_kernel_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous VNI state, in kernel or not

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

true, false

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_in_kernel_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current VNI state, in kernel or not

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

true, false

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_adv_all_vni_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous VNI advertising state, advertising all or not

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

true, false

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_adv_all_vni_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current VNI advertising state, advertising all or not

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

true, false

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="3" colspan="1">

Link

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

link

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf-6, exit01, spine7

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

ifname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Software interface name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

eth0, swp53

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="7" colspan="1">

LLDP

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

lldp

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf41, exit01, spine-5, tor-36

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

ifname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Software interface name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

eth1, swp12

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_peer_ifname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous software interface name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

eth1, swp12, swp27

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_peer_ifname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Curent software interface name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

eth1, swp12, swp27

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_peer_hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous user-defined, text-based name for a peer switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf41, exit01, spine-5, tor-36

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_peer_hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current user-defined, text-based name for a peer switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf41, exit01, spine-5, tor-36

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="4" colspan="1">

Node

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

node

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf41, exit01, spine-5, tor-36

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

ntp_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of NTP service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

in sync, not sync

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

db_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of DB

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Add, Update, Del, Dead

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="4" colspan="1">

NTP

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

ntp

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf-9, exit01, spine04

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous state of service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

in sync, not sync

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

in sync, not sync

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="20" colspan="1">

Port

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

port

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf13, exit01, spine-8, tor-36

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

ifname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Interface name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

eth0, swp14

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_speed

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous speed rating of port

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

10 G, 25 G, 40 G, unknown

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_transreceiver

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous transceiver

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

40G Base-CR4, 25G Base-CR

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_vendor_name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous vendor name of installed port module

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Amphenol, OEM, Mellanox, Fiberstore, Finisar

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_serial_number

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous serial number of installed port module

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

MT1507VS05177, AVE1823402U, PTN1VH2

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_supported_fec

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous forward error correction (FEC) support status

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

none, Base R, RS

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_advertised_fec

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous FEC advertising state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

true, false, not reported

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_fec

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous FEC capability

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

none

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_autoneg

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous activation state of auto-negotiation

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

on, off

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_speed

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current speed rating of port

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

10 G, 25 G, 40 G

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_transreceiver

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current transceiver

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

40G Base-CR4, 25G Base-CR

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_vendor_name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current vendor name of installed port module

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Amphenol, OEM, Mellanox, Fiberstore, Finisar

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_part_number

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current part number of installed port module

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

SFP-H10GB-CU1M, MC3309130-001, 603020003

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_serial_number

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current serial number of installed port module

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

MT1507VS05177, AVE1823402U, PTN1VH2

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_supported_fec

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current FEC support status

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

none, Base R, RS

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_advertised_fec

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current FEC advertising state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

true, false

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_fec

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current FEC capability

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

none

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_autoneg

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current activation state of auto-negotiation

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

on, off

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="10" colspan="1">

Sensors

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

sensor

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Fan: fan1, fan-2  
Power Supply Unit: psu1, psu2  
Temperature: psu1temp1, temp2

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf-26, exit01, spine2-4

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous state of a fan, power supply unit, or thermal sensor

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Fan: ok, absent, bad  
PSU: ok, absent, bad  
Temp: ok, busted, bad, critical

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of a fan, power supply unit, or thermal sensor

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Fan: ok, absent, bad  
PSU: ok, absent, bad  
Temp: ok, busted, bad, critical

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_s_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous state of a fan or power supply unit.

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Fan: up, down  
PSU: up, down

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_s_state

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current state of a fan or power supply unit.

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Fan: up, down  
PSU: up, down

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_s_max

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current maximum temperature threshold value

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Temp: 110

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_s_crit

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current critical high temperature threshold value

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Temp: 85

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_s_lcrit

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current critical low temperature threshold value

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Temp: -25

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_s_min

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current minimum temperature threshold value

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Temp: -50

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="7" colspan="1">

Services

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

message_type

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Network protocol or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

services

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

hostname

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

User-defined, text-based name for a switch or host

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

server02, leaf03, exit01, spine-8

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

name

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Name of service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

clagd, lldpd, ssh, ntp, netqd, net-agent

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_pid

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous process or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

12323, 52941

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_pid

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current process or service identifier

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

12323, 52941

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

old_status

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Previous status of service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

up, down

</td>

</tr>

<tr>

<td class="confluenceTd" rowspan="1" colspan="1">

new_status

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

Current status of service

</td>

<td class="confluenceTd" rowspan="1" colspan="1">

up, down

</td>

</tr>

</tbody>

</table>

{{%notice note%}}

Rule names are case sensitive, and no wildcards are permitted. Rule
names may contain spaces, but must be enclosed with single quotes in
commands. It is easier to use dashes in place of spaces or mixed case
for better readability. For example, use bgpSessionChanges or
BGP-session-changes or BGPsessions, instead of 'BGP Session Changes'.

Use Tab completion to view the command options syntax.

{{%/notice%}}

#### Example Rules

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

#### View the Rule Configurations

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

### Create Filters

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

{{<figure src="/images/netq/NQ-2x-Filter-Process-Flow.png">}}

{{%notice note%}}

Filter names may contain spaces, but *must* be enclosed with single
quotes in commands. It is easier to use dashes in place of spaces or
mixed case for better readability. For example, use bgpSessionChanges or
BGP-session-changes or BGPsessions, instead of 'BGP Session Changes'.
Filter names are also case sensitive.

{{%/notice%}}

#### Example Filters

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

#### View the Filter Configurations

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

#### Reorder Filters

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

## Example Notification Configurations

Putting all of these channel, rule, and filter definitions together you
create a complete notification configuration. The following are example
notification configurations are created using the three-step process
outlined above. Refer to [Integrate NetQ with an Event Notification
Application](#integrate-netq-with-an-event-notification-application)
for details and instructions for creating channels, rules, and filters.

### Create a Notification for BGP Events from a Selected Switch

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

### Create a Notification for Warnings on a Given EVPN VNI

In this example, we created a notification integration with a PagerDuty
channel called *pd-netq-events*. We then created a rule *evpnVni* and a
filter called *3vni42* for any warnings messages from VNI 42 on the EVPN
overlay network. The result is that any warning severity event messages
from VNI 42 are filtered to the *pd-netq-events* channel.

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

### Create a Notification for Configuration File Changes

In this example, we created a notification integration with a Slack
channel called *slk-netq-events*. We then created a rule *sysconf* and a
filter called *configChange* for any configuration file update messages.
The result is that any configuration update messages are filtered to the
*slk-netq-events* channel.

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

### Create a Notification for When a Service Goes Down

In this example, we created a notification integration with a Slack
channel called *slk-netq-events*. We then created a rule *svcStatus* and
a filter called *svcDown* for any services state messages indicating a
service is no longer operational. The result is that any service down
messages are filtered to the *slk-netq-events* channel.

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

### Create a Filter to Drop Notifications from a Given Interface

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

### Create a Notification for a Given Device that has a Tendency to Overheat (using multiple rules)

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

### View Notification Configurations in JSON Format

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

## Manage Event Notification Integrations

You might need to modify event
notification configurations at some point in the lifecycle of your
deployment. Optionally, you might want to configure a proxy.

### Remove an Event Notification Channel

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

### Delete an Event Notification Rule

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

### Delete an Event Notification Filter

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

## Integrate with a Hardware Chassis

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
    is disabled on a chassis to avoid this duplication . To enable
    sensor data on a line card, edit `/etc/netq/netq.yml` or
    `/etc/netq/config.d/user.yml` and set the `send_chassis_sensor_data`
    keyword to *true*, then restart the NetQ Agent with `netq config
    agent restart`. Configuring NetQ in this way prevents any
    duplication of data in the NetQ database.

        cumulus@chassis:~$ sudo nano /etc/netq/netq.yml
         
        ...
        netq-agent:
          send_chassis_sensor_data: true
        ...

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
