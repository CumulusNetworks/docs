---
title: Integrate NetQ with Notification Applications
author: Cumulus Networks
weight: 200
toc: 3
---
After you have installed the NetQ applications package and the NetQ Agents,
you may want to configure some of the additional capabilities that NetQ
offers. This topic describes how to integrate NetQ with an event notification application.

## Integrate NetQ with an Event Notification Application

To take advantage of the numerous event messages generated and processed
by NetQ, you must integrate with third-party event notification
applications. You can integrate NetQ with Syslog, PagerDuty and Slack tools.
You may integrate with one or more of these applications simultaneously.

In an on-premises deployment, the NetQ On-premises Appliance or VM receives the raw data stream from the NetQ Agents, processes the data, stores, and delivers events to the Notification function. Notification then filters and sends messages to any configured notification applications. In a cloud deployment, the NetQ Cloud Appliance or VM passes the raw data stream on to the NetQ Cloud service for processing and delivery.

{{<figure src="/images/netq/event-notif-arch-300.png">}}

{{<notice note>}}

You may choose to implement a proxy server (that sits between the NetQ
Platform and the integration channels) that receives, processes and
distributes the notifications rather than having them sent directly to
the integration channel. If you use such a proxy, you must configure
NetQ with the proxy information.

{{</notice>}}

In either case, notifications are generated for the following types of
events:

| Category | Events |
| --- | --- | 
| Network Protocols | <ul><li>BGP status and session state</li><li>CLAG (MLAG) status and session state</li><li>EVPN status and session state</li><li>LLDP status</li><li>OSPF status and session state </li><li>VLAN status and session state \*</li><li>VXLAN status and session state \*</li></ul> |
| Interfaces | <ul><li>Link status</li><li>Ports and cables status</li><li>MTU status</li></ul> |
| Services | <ul><li>NetQ Agent status</li><li>PTM</li><li>SSH \*</li><li>NTP status\*</li></ul> |
| Traces | <ul><li>On-demand trace status</li><li>Scheduled trace status</li></ul> |
| Sensors | <ul><li>Fan status</li><li>PSU (power supply unit) status</li><li>Temperature status</li></ul> |
| System Software | <ul><li>Configuration File changes</li><li>Running Configuration File changes</li><li>Cumulus Linux License status</li><li>Cumulus Linux Support status</li><li>Software Package status</li><li>Operating System version</li></ul> |
| System Hardware | <ul><li>Physical resources status</li><li>BTRFS status</li><li>SSD utilization status</li><li>Threshold Crossing Alerts (TCAs)</li></ul> |

*\* This type of event can only be viewed in the CLI with this release.*

Refer to the {{<link title="Events Reference">}} for descriptions and examples of these events.

### Event Message Format

Messages have the following structure:
`<message-type><timestamp><opid><hostname><severity><message>`

| Element  | Description  |
| ----------- | -------------- |
| message type | Category of event; *agent*, *bgp*, *clag*, *clsupport*, *configdiff*, *evpn*, *license*, *link*, *lldp*, *mtu*, *node*, *ntp*, *ospf*, *packageinfo*, *ptm*, *resource*, *runningconfigdiff*, *sensor*, *services*, *ssdutil*, *tca*, *trace*, *version*, *vlan* or *vxlan* |
| timestamp    | Date and time event occurred  |
| opid         | Identifier of the service or process that generated the event |
| hostname     | Hostname of network device where event occurred |
| severity     | Severity level in which the given event is classified; *debug*, *error*, *info*, *warning,* or *critical* |
| message      | Text description of event  |

For example:

{{<figure src="/images/netq/event-msg-format.png">}}

To set up the integrations, you must configure NetQ with at least one channel, one rule, and one filter. To refine what messages you want to view and where to send them, you can add additional rules and filters and set thresholds on supported event types. You can also configure a proxy server to receive, process, and forward the messages. This is accomplished using the NetQ CLI in the following order:

{{<figure src="/images/netq/notif-config-wkflow.png">}}

### Notification Commands Overview

The NetQ Command Line Interface (CLI) is used to filter and send notifications to third-party tools based on severity, service, event-type, and device. You can use TAB completion or the `help` option to assist when needed.

The command syntax for standard events is:

    ##Channels
    netq add notification channel slack <text-channel-name> webhook <text-webhook-url> [severity info|severity warning|severity error|severity debug] [tag <text-slack-tag>]
    netq add notification channel pagerduty <text-channel-name> integration-key <text-integration-key> [severity info|severity warning|severity error|severity debug]
    netq add notification channel syslog <text-channel-name> hostname <text-syslog-hostname> port <text-syslog-port> [severity info | severity warning | severity error | severity debug]
    netq add notification channel email <text-channel-name> to <text-email-toids>  [smtpserver <text-email-hostname>] [smtpport <text-email-port>] [login <text-email-id>] [password <text-email-password>] [severity info | severity warning | severity error | severity debug]
     
    ##Rules and Filters
    netq add notification rule <text-rule-name> key <text-rule-key> value <text-rule-value>
    netq add notification filter <text-filter-name> [severity info|severity warning|severity error|severity debug] [rule <text-rule-name-anchor>] [channel <text-channel-name-anchor>] [before <text-filter-name-anchor>|after <text-filter-name-anchor>]
     
    ##Management
    netq del notification channel <text-channel-name-anchor>
    netq del notification filter <text-filter-name-anchor>
    netq del notification rule <text-rule-name-anchor>
    netq show notification [channel|filter|rule] [json]

The command syntax for events with user-configurable thresholds is:

    ##Rules
    netq add tca event_id <event-name> scope <regex-filter> [severity <critical|info>] threshold <value>

    ##Management
    netq add tca tca_id <tca-rule-name> is_active <true|false>
    netq add tca tca_id <tca-rule-name> channel drop <channel-name>
    netq del tca tca_id <tca-rule-name>
    netq show tca [tca_id <tca-rule-name>]

The command syntax for a server proxy is:

    ##Proxy
    netq add notification proxy <text-proxy-hostname> [port <text-proxy-port>]
    netq show notification proxy
    netq del notification proxy

The various command options are described in the following sections where they are used.

## Configure Basic NetQ Event Notifications

The simplest configuration you can create is one that sends all events generated by all interfaces to a single notification application. This is described here. For more granular configurations and examples, refer to {{<link url="#configure-advanced-netq-event-notifications" text="Configure Advanced NetQ Event Notifications">}}.

A notification configuration must contain one channel, one rule, and one filter. Creation of the configuration follows this same path:

1. Add a channel (Slack, Pagerduty, syslog, email)
2. Add a rule that accepts all interface events
3. Add a filter that associates this rule with the newly created channel

### Create Your Channel

#### Create a PagerDuty Channel

Configure a channel using the integration key for your PagerDuty setup. Verify the configuration.

    cumulus@switch:~$ netq add notification channel pagerduty pd-netq-events integration-key c6d666e210a8425298ef7abde0d1998
    Successfully added/updated channel pd-netq-events
    
    cumulus@switch:~$ netq show notification channel
    Matching config_notify records:
    Name            Type             Severity         Channel Info
    --------------- ---------------- ---------------- ------------------------
    pd-netq-events  pagerduty        info             integration-key: c6d666e
                                                    210a8425298ef7abde0d1998      

#### Create a Slack Channel

Create an *incoming webhook* as described in the documentation for your version of Slack. Verify the configuration.

    cumulus@switch:~$ netq add notification channel slack slk-netq-events webhook https://hooks.slack.com/services/text/moretext/evenmoretext
    Successfully added/updated channel slk-netq-events
        
    cumulus@switch:~$ netq show notification channel
    Matching config_notify records:
    Name            Type             Severity Channel Info
    --------------- ---------------- -------- ----------------------
    slk-netq-events slack            info     webhook:https://hooks.s
                                            lack.com/services/text/
                                            moretext/evenmoretext

#### Create a syslog Channel

Create the channel using the syslog server hostname (or IP address) and port. Verify the configuration.

    cumulus@switch:~$ netq add notification channel syslog syslog-netq-events hostname syslog-server port 514
    Successfully added/updated channel syslog-netq-events
        
    cumulus@switch:~$ netq show notification channel
    Matching config_notify records:
    Name            Type             Severity Channel Info
    --------------- ---------------- -------- ----------------------
    syslog-netq-eve syslog            info     host:syslog-server
    nts                                        port: 514

#### Create an Email Channel

The configuration is different depending on whether you are using the on-prem or cloud version of NetQ. 

For an **on-prem** deployment, do the following:

1. Set up an SMTP server. The server can be internal or public.
1. Create a user account (login and password) on the SMTP server. Notifications are sent to this address.
1. Configure the notification channel using the following command format:

       netq add notification channel email <text-channel-name> to <text-email-toids>  [smtpserver <text-email-hostname>] [smtpport <text-email-port>] [login <text-email-id>] [password <text-email-password>] [severity info | severity warning | severity error | severity debug]

For example:

    cumulus@switch:~$ netq add notification channel email onprem-email to netq-notifications@domain.com smtpserver smtp.domain.com smtpport 587 login smtphostlogin@domain.com password MyPassword123 

For a **cloud** deployment, no SMTP configuration is required as the NetQ cloud uses the NETQ SMTP server to push email notifications. Use the following format:

    netq add notification channel email <text-channel-name> to <text-email-toids>

For example:

    cumulus@switch:~$ netq add notification channel email cloud-email to netq-cloud-notifications@domain.com

### Create a Rule

Create and verify a rule that accepts all interface events. Verify the configuration.

    cumulus@switch:~$ netq add notification rule all-ifs key ifname value ALL
    Successfully added/updated rule all-ifs
    
    cumulus@switch:~$ netq show notification rule
    Matching config_notify records:
    Name            Rule Key         Rule Value
    --------------- ---------------- --------------------
    all-interfaces  ifname           ALL

### Create a Filter

Create a filter to tie the rule to the channel. Verify the configuration.

For PagerDuty:

    cumulus@switch:~$ netq add notification filter notify-all-ifs rule all-ifs channel pd-netq-events
    Successfully added/updated filter notify-all-ifs
    
    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    notify-all-ifs  1          info             pd-netq-events   all-ifs

For Slack:

    cumulus@switch:~$ netq add notification filter notify-all-ifs rule all-ifs channel slk-netq-events
    Successfully added/updated filter notify-all-ifs

    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    notify-all-ifs  1          info             slk-netq-events   all-ifs

For Syslog:

    cumulus@switch:~$ netq add notification filter notify-all-ifs rule all-ifs channel syslog-netq-events
    Successfully added/updated filter notify-all-ifs

    cumulus@switch:~$ netq show notification filter
    Matching config_notify records:
    Name            Order      Severity         Channels         Rules
    --------------- ---------- ---------------- ---------------- ----------
    notify-all-ifs  1          info             syslog-netq-events all-ifs

NetQ is now configured to send all interface events to your selected channel.

## Configure Advanced NetQ Event Notifications

If you want to create more granular notifications based on such items as selected devices, characteristics of devices, or protocols, or you want to use a proxy server, you need more than the basic notification configuration. Details for creating these more complex notification configurations are included here.

### Configure a Proxy Server

To send notification messages through a proxy server instead of directly
to a notification channel, you configure NetQ with the hostname and
optionally a port of a proxy server. If no port is specified, NetQ
defaults to port 80. Only one proxy server is currently supported. To
simplify deployment, configure your proxy server before configuring
channels, rules, or filters.To configure the proxy server:

    cumulus@switch:~$ netq add notification proxy <text-proxy-hostname> [port <text-proxy-port]
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

Create one or more PagerDuty, Slack, or syslog channels to present the
notifications.

#### Configure a PagerDuty Channel

NetQ sends notifications to PagerDuty as PagerDuty events.

For example:

{{<figure src="/images/netq/NetQ-PagerDuty-ex-output.png">}}

To configure the NetQ notifier to send notifications to PagerDuty:

1.  Configure the following options using the `netq add notification channel` command:

    | Option | Description   |
    | ------ | ------------- |
    | CHANNEL\_TYPE \<text-channel-name\>      | The third-party notification channel and name; use *pagerduty* in this case.                                                                                       |
    | integration-key \<text-integration-key\> | The {{<exlink url="https://v2.developer.pagerduty.com/docs/events-api-v2" text="integration">}} key is also called the service\_key or routing\_key. The default is an empty string (""). |
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

2.  Configure the following options in the `netq config add notification channel` command:

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

<table>
<tr>
<th>Service</th>
<th>Rule Key</th>
<th>Description</th>
<th>Example Rule Values</th>
</tr>
<tr>
<td rowspan="9">BGP</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>bgp</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf11, exit01, spine-4</td>
</tr>
<tr>
<td>peer</td>
<td>User-defined, text-based name for a peer switch or host</td>
<td>server4, leaf-3, exit02, spine06</td>
</tr>
<tr>
<td>desc</td>
<td>Text description</td>
<td> </td>
</tr>
<tr>
<td>vrf</td>
<td>Name of VRF interface</td>
<td>mgmt, default</td>
</tr>
<tr>
<td>old_state</td>
<td>Previous state of the BGP service</td>
<td>Established, NotEstd</td>
</tr>
<tr>
<td>new_state</td>
<td>Current state of the BGP service</td>
<td>Established, NotEstd</td>
</tr>
<tr>
<td>old_last_reset_time</td>
<td>Previous time that BGP service was reset</td>
<td>Apr3, 2019, 4:17 pm</td>
</tr>
<tr>
<td>new_last_reset_time</td>
<td>Most recent time that BGP service was reset</td>
<td>Apr8, 2019, 11:38 am</td>
</tr>
<tr>
<td rowspan="6">MLAG (CLAG)</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>clag</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf-9, exit01, spine04</td>
</tr>
<tr>
<td>old_conflicted_bonds</td>
<td>Previous pair of interfaces in a conflicted bond</td>
<td>swp7 swp8, swp3 swp4</td>
</tr>
<tr>
<td>new_conflicted_bonds</td>
<td>Current pair of interfaces in a conflicted bond</td>
<td>swp11 swp12, swp23 swp24</td>
</tr>
<tr>
<td>old_state_protodownbond</td>
<td>Previous state of the bond</td>
<td>protodown, up</td>
</tr>
<tr>
<td>new_state_protodownbond</td>
<td>Current state of the bond</td>
<td>protodown, up</td>
</tr>
<tr>
<td rowspan="5">ConfigDiff</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>configdiff</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf11, exit01, spine-4</td>
</tr>
<tr>
<td>vni</td>
<td>Virtual Network Instance identifier</td>
<td>12, 23</td>
</tr>
<tr>
<td>old_state</td>
<td>Previous state of the configuration file</td>
<td>created, modified</td>
</tr>
<tr>
<td>new_state</td>
<td>Current state of the configuration file</td>
<td>created, modified</td>
</tr>
<tr>
<td rowspan="7">EVPN</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>evpn</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf-9, exit01, spine04</td>
</tr>
<tr>
<td>vni</td>
<td>Virtual Network Instance identifier</td>
<td>12, 23</td>
</tr>
<tr>
<td>old_in_kernel_state</td>
<td>Previous VNI state, in kernel or not</td>
<td>true, false</td>
</tr>
<tr>
<td>new_in_kernel_state</td>
<td>Current VNI state, in kernel or not</td>
<td>true, false</td>
</tr>
<tr>
<td>old_adv_all_vni_state</td>
<td>Previous VNI advertising state, advertising all or not</td>
<td>true, false</td>
</tr>
<tr>
<td>new_adv_all_vni_state</td>
<td>Current VNI advertising state, advertising all or not</td>
<td>true, false</td>
</tr>
<tr>
<td rowspan="3">Link</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>link</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf-6, exit01, spine7</td>
</tr>
<tr>
<td>ifname</td>
<td>Software interface name</td>
<td>eth0, swp53</td>
</tr>
<tr>
<td rowspan="7">LLDP</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>lldp</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf41, exit01, spine-5, tor-36</td>
</tr>
<tr>
<td>ifname</td>
<td>Software interface name</td>
<td>eth1, swp12</td>
</tr>
<tr>
<td>old_peer_ifname</td>
<td>Previous software interface name</td>
<td>eth1, swp12, swp27</td>
</tr>
<tr>
<td>new_peer_ifname</td>
<td>Current software interface name</td>
<td>eth1, swp12, swp27</td>
</tr>
<tr>
<td>old_peer_hostname</td>
<td>Previous user-defined, text-based name for a peer switch or host</td>
<td>server02, leaf41, exit01, spine-5, tor-36</td>
</tr>
<tr>
<td>new_peer_hostname</td>
<td>Current user-defined, text-based name for a peer switch or host</td>
<td>server02, leaf41, exit01, spine-5, tor-36</td>
</tr>
<tr>
<td rowspan="4">Node</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>node</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf41, exit01, spine-5, tor-36</td>
</tr>
<tr>
<td>ntp_state</td>
<td>Current state of NTP service</td>
<td>in sync, not sync</td>
</tr>
<tr>
<td>db_state</td>
<td>Current state of DB</td>
<td>Add, Update, Del, Dead</td>
</tr>
<tr>
<td rowspan="4">NTP</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>ntp</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf-9, exit01, spine04</td>
</tr>
<tr>
<td>old_state</td>
<td>Previous state of service</td>
<td>in sync, not sync</td>
</tr>
<tr>
<td>new_state</td>
<td>Current state of service</td>
<td>in sync, not sync</td>
</tr>
<tr>
<td rowspan="20">Port</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>port</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf13, exit01, spine-8, tor-36</td>
</tr>
<tr>
<td>ifname</td>
<td>Interface name</td>
<td>eth0, swp14</td>
</tr>
<tr>
<td>old_speed</td>
<td>Previous speed rating of port</td>
<td>10 G, 25 G, 40 G, unknown</td>
</tr>
<tr>
<td>old_transreceiver</td>
<td>Previous transceiver</td>
<td>40G Base-CR4, 25G Base-CR</td>
</tr>
<tr>
<td>old_vendor_name</td>
<td>Previous vendor name of installed port module</td>
<td>Amphenol, OEM, Mellanox, Fiberstore, Finisar</td>
</tr>
<tr>
<td>old_serial_number</td>
<td>Previous serial number of installed port module</td>
<td>MT1507VS05177, AVE1823402U, PTN1VH2</td>
</tr>
<tr>
<td>old_supported_fec</td>
<td>Previous forward error correction (FEC) support status</td>
<td>none, Base R, RS</td>
</tr>
<tr>
<td>old_advertised_fec</td>
<td>Previous FEC advertising state</td>
<td>true, false, not reported</td>
</tr>
<tr>
<td>old_fec</td>
<td>Previous FEC capability</td>
<td>none</td>
</tr>
<tr>
<td>old_autoneg</td>
<td>Previous activation state of auto-negotiation</td>
<td>on, off</td>
</tr>
<tr>
<td>new_speed</td>
<td>Current speed rating of port</td>
<td>10 G, 25 G, 40 G</td>
</tr>
<tr>
<td>new_transreceiver</td>
<td>Current transceiver</td>
<td>40G Base-CR4, 25G Base-CR</td>
</tr>
<tr>
<td>new_vendor_name</td>
<td>Current vendor name of installed port module</td>
<td>Amphenol, OEM, Mellanox, Fiberstore, Finisar</td>
</tr>
<tr>
<td>new_part_number</td>
<td>Current part number of installed port module</td>
<td>SFP-H10GB-CU1M, MC3309130-001, 603020003</td>
</tr>
<tr>
<td>new_serial_number</td>
<td>Current serial number of installed port module</td>
<td>MT1507VS05177, AVE1823402U, PTN1VH2</td>
</tr>
<tr>
<td>new_supported_fec</td>
<td>Current FEC support status</td>
<td>none, Base R, RS</td>
</tr>
<tr>
<td>new_advertised_fec</td>
<td>Current FEC advertising state</td>
<td>true, false</td>
</tr>
<tr>
<td>new_fec</td>
<td>Current FEC capability</td>
<td>none</td>
</tr>
<tr>
<td>new_autoneg</td>
<td>Current activation state of auto-negotiation</td>
<td>on, off</td>
</tr>
<tr>
<td rowspan="10">Sensors</td>
<td>sensor</td>
<td>Network protocol or service identifier</td>
<td>Fan: fan1, fan-2  
Power Supply Unit: psu1, psu2  
Temperature: psu1temp1, temp2</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf-26, exit01, spine2-4</td>
</tr>
<tr>
<td>old_state</td>
<td>Previous state of a fan, power supply unit, or thermal sensor</td>
<td>Fan: ok, absent, bad  
PSU: ok, absent, bad  
Temp: ok, busted, bad, critical</td>
</tr>
<tr>
<td>new_state</td>
<td>Current state of a fan, power supply unit, or thermal sensor</td>
<td>Fan: ok, absent, bad  
PSU: ok, absent, bad  
Temp: ok, busted, bad, critical</td>
</tr>
<tr>
<td>old_s_state</td>
<td>Previous state of a fan or power supply unit.</td>
<td>Fan: up, down  
PSU: up, down</td>
</tr>
<tr>
<td>new_s_state</td>
<td>Current state of a fan or power supply unit.</td>
<td>Fan: up, down  
PSU: up, down</td>
</tr>
<tr>
<td>new_s_max</td>
<td>Current maximum temperature threshold value</td>
<td>Temp: 110</td>
</tr>
<tr>
<td>new_s_crit</td>
<td>Current critical high temperature threshold value</td>
<td>Temp: 85</td>
</tr>
<tr>
<td>new_s_lcrit</td>
<td>Current critical low temperature threshold value</td>
<td>Temp: -25</td>
</tr>
<tr>
<td>new_s_min</td>
<td>Current minimum temperature threshold value</td>
<td>Temp: -50</td>
</tr>
<tr>
<td rowspan="7">Services</td>
<td>message_type</td>
<td>Network protocol or service identifier</td>
<td>services</td>
</tr>
<tr>
<td>hostname</td>
<td>User-defined, text-based name for a switch or host</td>
<td>server02, leaf03, exit01, spine-8</td>
</tr>
<tr>
<td>name</td>
<td>Name of service</td>
<td>clagd, lldpd, ssh, ntp, netqd, net-agent</td>
</tr>
<tr>
<td>old_pid</td>
<td>Previous process or service identifier</td>
<td>12323, 52941</td>
</tr>
<tr>
<td>new_pid</td>
<td>Current process or service identifier</td>
<td>12323, 52941</td>
</tr>
<tr>
<td>old_status</td>
<td>Previous status of service</td>
<td>up, down</td>
</tr>
<tr>
<td>new_status</td>
<td>Current status of service</td>
<td>up, down</td>
</tr>
</table>

{{<notice note>}}
Rule names are case sensitive, and no wildcards are permitted. Rule
names may contain spaces, but must be enclosed with single quotes in
commands. It is easier to use dashes in place of spaces or mixed case
for better readability. For example, use bgpSessionChanges or
BGP-session-changes or BGPsessions, instead of 'BGP Session Changes'.

Use Tab completion to view the command options syntax.
{{</notice>}}

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

{{<notice note>}}
Filter names may contain spaces, but <em>must</em> be enclosed with single
quotes in commands. It is easier to use dashes in place of spaces or
mixed case for better readability. For example, use bgpSessionChanges or
BGP-session-changes or BGPsessions, instead of 'BGP Session Changes'.
Filter names are also case sensitive.
{{</notice>}}

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

{{<notice tip>}}
You do not need to reenter all the severity, channel, and rule
information for existing rules if you only want to change their
processing order.
{{</notice>}}

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

### Suppress Events

Cumulus NetQ can generate many network events. You can configure whether to suppress any events from appearing in NetQ output. By default, all events are delivered.

You can suppress an event until a certain period of time; otherwise, the event is suppressed for 2 years. Providing an end time eliminates the generation of messages for a short period of time, which is useful when you are testing a new network configuration and the switch may be generating many messages.

You can suppress events for the following types of messages:

- agent: NetQ Agent messages
- bgp: BGP-related messages
- btrfsinfo: Messages related to the BTRFS file system in Cumulus Linux
- clag: MLAG-related messages
- clsupport: Messages generated when creating the `cl-support script`
- configdiff: Messages related to the difference between two configurations
- evpn: EVPN-related messages
- link: Messages related to links, including state and interface name
- ntp: NTP-related messages
- ospf: OSPF-related messages
- sensor: Messages related to various sensors
- services: Service-related information, including whether a service is active or inactive
- ssdutil: Messages related to the storage on the switch

#### Add an Event Suppression Configuration

When you add a new configuration, you can specify a scope, which limits the suppression in the following order:

1. Hostname.
1. Severity.
1. Message type-specific filters. For example, the target VNI for EVPN messages, or the interface name for a link message.

NetQ has a predefined set of filter conditions. To see these conditions, run `netq show events-config show-filter-conditions`:

```
cumulus@leaf01:~$ netq show events-config show-filter-conditions

Matching config_events records:
Message Name             Filter Condition Name                      Filter Condition Hierarchy                           Filter Condition Description
------------------------ ------------------------------------------ ---------------------------------------------------- --------------------------------------------------------
evpn                     vni                                        3                                                    Target VNI
evpn                     severity                                   2                                                    Severity critical/info
evpn                     hostname                                   1                                                    Target Hostname
clsupport                fileAbsName                                3                                                    Target File Absolute Name
clsupport                severity                                   2                                                    Severity critical/info
clsupport                hostname                                   1                                                    Target Hostname
link                     new_state                                  4                                                    up / down
link                     ifname                                     3                                                    Target Ifname
link                     severity                                   2                                                    Severity critical/info
link                     hostname                                   1                                                    Target Hostname
ospf                     ifname                                     3                                                    Target Ifname
ospf                     severity                                   2                                                    Severity critical/info
ospf                     hostname                                   1                                                    Target Hostname
sensor                   new_s_state                                4                                                    New Sensor State Eg. ok
sensor                   sensor                                     3                                                    Target Sensor Name Eg. Fan, Temp
sensor                   severity                                   2                                                    Severity critical/info
sensor                   hostname                                   1                                                    Target Hostname
configdiff               old_state                                  5                                                    Old State
configdiff               new_state                                  4                                                    New State
configdiff               type                                       3                                                    File Name
configdiff               severity                                   2                                                    Severity critical/info
configdiff               hostname                                   1                                                    Target Hostname
ssdutil                  info                                       3                                                    low health / significant health drop
ssdutil                  severity                                   2                                                    Severity critical/info
ssdutil                  hostname                                   1                                                    Target Hostname
agent                    db_state                                   3                                                    Database State
agent                    severity                                   2                                                    Severity critical/info
agent                    hostname                                   1                                                    Target Hostname
ntp                      new_state                                  3                                                    yes / no
ntp                      severity                                   2                                                    Severity critical/info
ntp                      hostname                                   1                                                    Target Hostname
bgp                      vrf                                        4                                                    Target VRF
bgp                      peer                                       3                                                    Target Peer
bgp                      severity                                   2                                                    Severity critical/info
bgp                      hostname                                   1                                                    Target Hostname
services                 new_status                                 4                                                    active / inactive
services                 name                                       3                                                    Target Service Name Eg.netqd, mstpd, zebra
services                 severity                                   2                                                    Severity critical/info
services                 hostname                                   1                                                    Target Hostname
btrfsinfo                info                                       3                                                    high btrfs allocation space / data storage efficiency
btrfsinfo                severity                                   2                                                    Severity critical/info
btrfsinfo                hostname                                   1                                                    Target Hostname
clag                     severity                                   2                                                    Severity critical/info
clag                     hostname                                   1                                                    Target Hostname
cumulus@leaf01:~$
```

For example, to create a configuration called `mybtrfs` that suppresses OSPF-related events on leaf01 for the next 10 minutes, run:

```
netq add events-config events_config_name mybtrfs message_type ospf scope '[{"scope_name":"hostname","scope_value":"leaf01"},{"scope_name":"severity","scope_value":"*"}]' suppress_until 600
```

#### Remove an Event Suppression Configuration

To remove an event suppression configuration, run `netq del events-config events_config_id <text-events-config-id-anchor>`.

```
cumulus@leaf01:~$ netq del events-config events_config_id eventsconfig_10
Successfully deleted Events Config eventsconfig_10
cumulus@leaf01:~$
```

#### Show Event Suppression Configurations

You can view all event suppression configurations, or you can filter by a specific configuration or message type.

```
cumulus@leaf01:~$ netq show events-config events_config_id eventsconfig_1

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
eventsconfig_1       job_cl_upgrade_2d89c btrfsinfo            {"hostname":"spine04","info":"*","severity":"*"}             True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clag                 {"hostname":"spine04","severity":"*"}                        True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clsupport            {"fileAbsName":"*","hostname":"spine04","severity":"*"}      True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c configdiff           {"new_state":"*","old_state":"*","type":"*","hostname":"spin True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      e04","severity":"*"}                                                2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c evpn                 {"hostname":"spine04","vni":"*","severity":"*"}              True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c link                 {"ifname":"*","new_state":"*","hostname":"spine04","severity True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      ":"*"}                                                              2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ntp                  {"new_state":"*","hostname":"spine04","severity":"*"}        True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ospf                 {"ifname":"*","hostname":"spine04","severity":"*"}           True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c sensor               {"sensor":"*","new_s_state":"*","hostname":"spine04","severi True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      ty":"*"}                                                            2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c services             {"new_status":"*","name":"*","hostname":"spine04","severity" True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      :"*"}                                                               2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ssdutil              {"hostname":"spine04","info":"*","severity":"*"}             True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_10      job_cl_upgrade_2d89c btrfsinfo            {"hostname":"fw2","info":"*","severity":"*"}                 True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c clag                 {"hostname":"fw2","severity":"*"}                            True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c clsupport            {"fileAbsName":"*","hostname":"fw2","severity":"*"}          True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c link                 {"ifname":"*","new_state":"*","hostname":"fw2","severity":"* True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                      "}                                                                  2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c ospf                 {"ifname":"*","hostname":"fw2","severity":"*"}               True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c sensor               {"sensor":"*","new_s_state":"*","hostname":"fw2","severity": True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                      "*"}                                                                2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
cumulus@leaf01:~$
```

If you are filtering for a message type, you must include the `show-filter-conditions` keyword to show the conditions associated with that message type and the hierarchy in which they're processed.

```
cumulus@leaf01:~$ netq show events-config message_type evpn show-filter-conditions

Matching config_events records:
Message Name             Filter Condition Name                      Filter Condition Hierarchy                           Filter Condition Description
------------------------ ------------------------------------------ ---------------------------------------------------- --------------------------------------------------------
evpn                     vni                                        3                                                    Target VNI
evpn                     severity                                   2                                                    Severity critical/info
evpn                     hostname                                   1                                                    Target Hostname
cumulus@leaf01:~$
```

## Examples of Advanced Notification Configurations

Putting all of these channel, rule, and filter definitions together you
create a complete notification configuration. The following are example
notification configurations are created using the three-step process
outlined above. Refer to {{<link url="#integrate-netq-with-an-event-notification-application" text="Integrate NetQ with an Event Notification Application">}} for details and instructions for creating channels, rules, and filters.

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

## Manage NetQ Event Notification Integrations

You might need to modify event notification configurations at some point in the lifecycle of your deployment.

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

## Configure Threshold-based Event Notifications

NetQ supports a set of events that are triggered by crossing a user-defined threshold, called TCA events. These events allow detection and prevention of network failures for selected interface, utilization,  sensor, forwarding, and ACL events.

The simplest configuration you can create is one that sends a TCA event generated by all devices and all interfaces to a single notification application. Use the `netq add tca` command to configure the event. Its syntax is:

```
netq add tca [event_id <text-event-id-anchor>]  [scope <text-scope-anchor>] [tca_id <text-tca-id-anchor>]  [severity info | severity critical] [is_active true | is_active false] [suppress_until <text-suppress-ts>] [threshold <text-threshold-value> ] [channel <text-channel-name-anchor> | channel drop <text-drop-channel-name>]
```

A notification configuration must contain one rule. Each rule must contain a scope and a threshold. Optionally, you can specify an associated channel.  *Note: If a rule is not associated with a channel, the event information is only reachable from the database.* If you want to deliver events to one or more notification channels (syslog, Slack, or PagerDuty), create them by following the instructions in {{<link title="#Create Your Channel" text="Create Your Channel">}}, and then return here to define your rule.

### Supported Events

The following events are supported:

{{< tabs "TabID1475" >}}

{{< tab "ACL Resources" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Number of ingress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Number of egress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Number of ingress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Number of egress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Number of ingress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Number of egress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Number of ingress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Number of egress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Number of ingress ACL 802.1 filters on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Number of ACL port range checkers on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_REGIONS_UPPER | Number of ACL regions on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_ACL_MIRROR_UPPER | Number of ingress ACL mirrors on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_18B_RULES_UPPER | Number of ACL 18B rules on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_32B_RULES_UPPER | Number of ACL 32B rules on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ACL_54B_RULES_UPPER | Number of ACL 54B rules on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv6 addresses on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Digital Optics" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_INPUT_POWER_UPPER | Transceiver Input power (mW) for the digital optical module on a given switch or host is greater than maximum threshold |
| TCA_INPUT_POWER_LOWER | Transceiver Input power (mW) for the digital optical module on a given switch or host is less than minimum threshold |
| TCA_LASER_BIAS_UPPER | Laser bias current (mA) for the digital optical module on a given switch or host is greater than maximum threshold |
| TCA_LASER_BIAS_LOWER | Laser bias current (mA) for the digital optical module on a given switch or host is less than minimum threshold |
| TCA_LASER_OUTPUT_POWER_UPPER | Laser output power (mW) for the digital optical module on a given switch or host is greater than maximum threshold |
| TCA_LASER_OUTPUT_POWER_LOWER | Laser output power (mW) for the digital optical module on a given switch or host is less than minimum threshold |
| TCA_MODULE_TEMPERATURE_UPPER | Digital optical module temperature (&deg;C) on a given switch or host is greater than maximum threshold |
| TCA_MODULE_TEMPERATURE_LOWER | Digital optical module temperature (&deg;C) on a given switch or host is less than minimum threshold |
| TCA_TRANSCEIVER_VOLTAGE_UPPER | Transceiver voltage (mV) on a given switch or host is greater than maximum threshold |
| TCA_TRANSCEIVER_VOLTAGE_LOWER | Transceiver voltage (mV) on a given switch or host is less than minimum threshold |

{{< /tab >}}

{{< tab "Forwarding Resources" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Number of routes on a given switch or host is greater than maximum threshold |
| TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Number of multicast routes on a given switch or host is greater than maximum threshold |
| TCA_TCAM_MAC_ENTRIES_UPPER | Number of MAC addresses on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV4_ROUTE_UPPER | Number of IPv4 routes on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV4_HOST_UPPER | Number of IPv4 hosts on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV6_ROUTE_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| TCA_TCAM_IPV6_HOST_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| TCA_TCAM_ECMP_NEXTHOPS_UPPER | Number of equal cost multi-path (ECMP) next hop entries on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Interface Statistics" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_RXBROADCAST_UPPER  |  rx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| TCA_RXBYTES_UPPER |  rx_bytes per second on a given switch or host is greater than maximum threshold |
| TCA_RXMULTICAST_UPPER |  rx_multicast per second on a given switch or host is greater than maximum threshold |
| TCA_TXBROADCAST_UPPER |  tx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| TCA_TXBYTES_UPPER     |  tx_bytes per second on a given switch or host is greater than maximum threshold |
| TCA_TXMULTICAST_UPPER |  tx_multicast bytes per second on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Resource Utilization" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_CPU_UTILIZATION_UPPER | CPU utilization (%) on a given switch or host is greater than maximum threshold |
| TCA_DISK_UTILIZATION_UPPER  |  Disk utilization (%) on a given switch or host is greater than maximum threshold |
| TCA_MEMORY_UTILIZATION_UPPER  |  Memory utilization (%) on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< tab "Sensors" >}}

| Event ID | Description |
| ---------- | -------------- |
| TCA_SENSOR_FAN_UPPER  |  Switch sensor reported fan speed on a given switch or host is greater than maximum threshold |
| TCA_SENSOR_POWER_UPPER|  Switch sensor reported power (Watts) on a given switch or host is greater than maximum threshold |
| TCA_SENSOR_TEMPERATURE_UPPER  |  Switch sensor reported temperature (&deg;C) on a given switch or host is greater than maximum threshold |
| TCA_SENSOR_VOLTAGE_UPPER  |  Switch sensor reported voltage (Volts) on a given switch or host is greater than maximum threshold |

{{< /tab >}}

{{< /tabs >}}

### Define a Scope

A scope is used to filter the events generated by a given rule. Scope values are set on a per TCA rule basis. All rules can be filtered on Hostname. Some rules can also be filtered by other parameters, as shown in this table. *Note*: Scope parameters must be entered in the order defined.

{{< tabs "TabID373" >}}

{{< tab "ACL Resources" >}}

| Event ID | Scope Parameters |
| ---------- | -------------- |
| TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Hostname |
| TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Hostname |
| TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Hostname |
| TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Hostname |
| TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Hostname |
| TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Hostname |
| TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Hostname |
| TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Hostname |
| TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Hostname |
| TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Hostname |
| TCA_TCAM_ACL_REGIONS_UPPER | Hostname |
| TCA_TCAM_IN_ACL_MIRROR_UPPER | Hostname |
| TCA_TCAM_ACL_18B_RULES_UPPER | Hostname |
| TCA_TCAM_ACL_32B_RULES_UPPER | Hostname |
| TCA_TCAM_ACL_54B_RULES_UPPER | Hostname |
| TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Hostname |
| TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Hostname |

{{< /tab >}}

{{< tab "Digital Optics" >}}

These are only available when using the NetQ CLI.

| Event ID | Scope Parameters |
| ---------- | -------------- |
| TCA_INPUT_POWER_UPPER  |  Hostname |
| TCA_INPUT_POWER_LOWER  |  Hostname |
| TCA_LASER_BIAS_UPPER  |  Hostname |
| TCA_LASER_BIAS_LOWER  |  Hostname |
| TCA_LASER_OUTPUT_POWER_UPPER  |  Hostname |
| TCA_LASER_OUTPUT_POWER_LOWER  |  Hostname |
| TCA_MODULE_TEMPERATURE_UPPER  |  Hostname |
| TCA_MODULE_TEMPERATURE_LOWER  |  Hostname |
| TCA_TRANSCEIVER_VOLTAGE_UPPER  |  Hostname |
| TCA_TRANSCEIVER_VOLTAGE_LOWER  |  Hostname |

{{< /tab >}}

{{< tab "Forwarding Resources" >}}

| Event ID | Scope Parameters |
| ---------- | -------------- |
| TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Hostname |
| TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Hostname |
| TCA_TCAM_MAC_ENTRIES_UPPER | Hostname |
| TCA_TCAM_ECMP_NEXTHOPS_UPPER | Hostname |
| TCA_TCAM_IPV4_ROUTE_UPPER | Hostname |
| TCA_TCAM_IPV4_HOST_UPPER | Hostname |
| TCA_TCAM_IPV6_ROUTE_UPPER | Hostname |
| TCA_TCAM_IPV6_HOST_UPPER | Hostname |

{{< /tab >}}

{{< tab "Interface Statistics" >}}

| Event ID | Scope Parameters |
| ---------- | -------------- |
| TCA_RXBROADCAST_UPPER  | Hostname, Interface |
| TCA_RXBYTES_UPPER | Hostname, Interface |
| TCA_RXMULTICAST_UPPER | Hostname, Interface |
| TCA_TXBROADCAST_UPPER | Hostname, Interface |
| TCA_TXBYTES_UPPER | Hostname, Interface |
| TCA_TXMULTICAST_UPPER | Hostname, Interface |

{{< /tab >}}

{{< tab "Resource Utilization" >}}

| Event ID | Scope Parameters |
| ---------- | -------------- |
| TCA_CPU_UTILIZATION_UPPER | Hostname |
| TCA_DISK_UTILIZATION_UPPER  | Hostname |
| TCA_MEMORY_UTILIZATION_UPPER  | Hostname |

{{< /tab >}}

{{< tab "Sensors" >}}
| Event ID | Scope Parameters |
| ---------- | -------------- |
| TCA_SENSOR_FAN_UPPER  | Hostname, Sensor Name |
| TCA_SENSOR_POWER_UPPER| Hostname, Sensor Name |
| TCA_SENSOR_TEMPERATURE_UPPER  | Hostname, Sensor Name |
| TCA_SENSOR_VOLTAGE_UPPER  | Hostname, Sensor Name |

{{< /tab >}}

{{< /tabs >}}

Scopes are defined with regular expressions, as follows. When two paramaters are used, they are separated by a comma, but no space. When as asterisk (*) is used alone, it must be entered inside either single or double quotes. Single quotes are used here.

{{< tabs "TabID1668" >}}

{{< tab "Hostname" >}}

| Scope Value | Example | Result |
| --------------- | ---------- | -------- |
| \<hostname> | leaf01 | Deliver events for the specified device |
| \<partial-hostname>\* | leaf\* | Deliver events for devices with hostnames starting with specified text (*leaf*) |
| \'\*\' | \'\*\' | Deliver events for all devices |

{{< /tab >}}

{{< tab "Hostname, Interface">}}

| Scope Value | Example | Result |
| --------------- | ---------- | -------- |
| \<hostname>,\<interface> | leaf01,swp9 | Deliver events for the specified interface (*swp9*) on the specified device (*leaf01*) |
| \<hostname>,\'\*\' | leaf01,\'\*\' | Deliver events for all interfaces on the specified device (*leaf01*) |
| \'\*\',\<interface> | \'\*\',swp9 | Deliver events for the specified interface (*swp9*) on all devices |
| \'\*\',\'\*\' | \'\*\',\'\*\' | Deliver events for all devices and all interfaces |
| \<partial-hostname>\*,\<interface> | leaf*,swp9 | Deliver events for the specified interface (*swp9*) on all devices with hostnames starting with the specified text (*leaf*) |
| \<hostname>,\<partial-interface>\* | leaf01,swp* | Deliver events for all interface with names starting with the specified text (*swp*) on the specified device (*leaf01*) |

{{< /tab >}}

{{< tab "Hostname, Sensor Name">}}

| Scope Value | Example | Result |
| --------------- | ---------- | -------- |
| \<hostname>,\<sensorname> | leaf01,fan1 | Deliver events for the specified sensor (*fan1*) on the specified device (*leaf01*) |
| \'\*\',\<sensorname> | \'\*\',fan1 | Deliver events for the specified sensor (*fan1*) for all devices |
|  \<hostname>,\'\*\' | leaf01,\'\*\' | Deliver events for all sensors on the specified device (*leaf01*) |
| \<partial-hostname>\*,\<interface> | leaf*,fan1 | Deliver events for the specified sensor (*fan1*) on all devices with hostnames starting with the specified text (*leaf*) |
| \<hostname>,\<partial-sensorname>\* | leaf01,fan* | Deliver events for all sensors with names starting with the specified text (*fan*) on the specified device (*leaf01*) |
| \'\*\',\'\*\' | \'\*\',\'\*\' | Deliver events for all sensors on all devices |

{{< /tab >}}

{{< /tabs >}}

<!-- ADD New params for acl and forwarding resources, dom? -->

### Create a TCA Rule

Now that you know which events are supported and how to set the scope, you can create a basic rule to deliver one of the TCA events to a notification channel using the `netq add tca` command. Note that the event ID is case sensitive and must be in all caps.

For example, this rule tells NetQ to deliver an event notification to the *tca_slack_ifstats*  pre-configured Slack channel when the CPU utilization exceeds 95% of its capacity on any monitored switch:

```
netq add tca event_id TCA_CPU_UTILIZATION_UPPER scope '*' channel tca_slack_ifstats threshold 95
```

This rule tells NetQ to deliver an event notification to the *tca_pd_ifstats* PagerDuty channel when the number of transmit bytes per second (Bps) on the *leaf12* switch exceeds 20,000 Bps on any interface:

```
netq add tca event_id TCA_TXBYTES_UPPER scope leaf12,'*' channel tca_pd_ifstats threshold 20000
```

This rule tells NetQ to deliver an event notification to the *syslog-netq* syslog channel when the temperature on sensor *temp1* on the *leaf12* switch exceeds 32 degrees Celcius:

```
netq add tca event_id TCA_SENSOR_TEMPERATURE_UPPER scope leaf12,temp1 channel syslog-netq threshold 32
```

For a Slack channel, the event messages should be similar to this:

{{<figure src="/images/netq/tca-events-slack-example-240.png" width="500">}}

### Set the Severity of a Threshold-based Event

In addition to defining a scope for TCA rule, you can also set a severity of either info or critical. To add a severity to a rule, use the `severity` option. 

For example, if you want add a critical severity to the CPU utilization rule you created earlier:

```
netq add tca event_id TCA_CPU_UTILIZATION_UPPER scope '*' severity critical channel tca_slack_resources threshold 95
```

Or if an event is important, but not critical. Set the `severity` to *info*:

```
netq add tca event_id TCA_TXBYTES_UPPER scope leaf12,'*' severity info channel tca_pd_ifstats threshold 20000
```

### Create Multiple Rules for a TCA Event

You are likely to want more than one rule around a particular event. For example, you might want to:

- Monitor the same event but for a different interface, sensor, or device
- Send the event notification to more than one channel
- Change the threshold for a particular device that you are troubleshooting
- etc.

```
netq add tca event_id TCA_SENSOR_TEMPERATURE_UPPER scope leaf*,temp1 channel syslog-netq threshold 32

netq add tca event_id TCA_SENSOR_TEMPERATURE_UPPER scope '*',temp1 channel tca_sensors,tca_pd_sensors threshold 32

netq add tca event_id TCA_SENSOR_TEMPERATURE_UPPER scope leaf03,temp1 channel syslog-netq threshold 29
```

Now you have four rules created (the original one, plus these three new ones) all based on the TCA_SENSOR_TEMPERATURE_UPPER event. To identify the various rules, NetQ automatically generates a TCA name for each rule. As each rule is created, an *\_#* is added to the event name. The TCA Name for the first rule created is then TCA_SENSOR_TEMPERATURE_UPPER_1, the second rule created for this event is TCA_SENSOR_TEMPERATURE_UPPER_2, and so forth.

### Suppress a Rule

During troubleshooting or maintenance of switches you may want to suppress a rule to prevent erroneous event messages. Using the `suppress_until` option allows you to prevent the rule from being applied for a designated amout of time (in seconds). When this time has passed, the rule is automatically reenabled.

For example, to suppress the disk utilization event for an hour:

```
cumulus@switch:~$ netq add tca tca_id TCA_DISK_UTILIZATION_UPPER_1 suppress_until 3600
Successfully added/updated tca TCA_DISK_UTILIZATION_UPPER_1
```

### Remove a Channel from a Rule

You can stop sending events to a particular channel using the `drop` option:

```
cumulus@switch:~$ netq add tca tca_id TCA_DISK_UTILIZATION_UPPER_1 channel drop tca_slack_resources
Successfully added/updated tca TCA_DISK_UTILIZATION_UPPER_1
```

## Manage Threshold-based  Event Notifications

Once you have created a bunch of rules, you might to manage them; view a list of the rules, disable a rule, delete a rule, and so forth.

### Show Threshold-based Event Rules

You can view all TCA rules or a particular rule using the `netq show tca` command:

Example 1: Display All TCA Rules

```
cumulus@switch:~$ netq show tca
Matching config_tca records:
TCA Name                     Event Name           Scope                      Severity         Channel/s          Active Threshold          Suppress Until
---------------------------- -------------------- -------------------------- ---------------- ------------------ ------ ------------------ ----------------------------
TCA_CPU_UTILIZATION_UPPER_1  TCA_CPU_UTILIZATION_ {"hostname":"leaf01"}      critical         tca_slack_resource True   1                  Sun Dec  8 14:17:18 2019
                             UPPER                                                            s
TCA_DISK_UTILIZATION_UPPER_1 TCA_DISK_UTILIZATION {"hostname":"leaf01"}      info                                False  80                 Mon Dec  9 05:03:46 2019
                             _UPPER
TCA_MEMORY_UTILIZATION_UPPER TCA_MEMORY_UTILIZATI {"hostname":"leaf01"}      info             tca_slack_resource True   1                  Sun Dec  8 11:53:15 2019
_1                           ON_UPPER                                                         s
TCA_RXBYTES_UPPER_1          TCA_RXBYTES_UPPER    {"ifname":"swp3","hostname info             tca-tx-bytes-slack True   100                Sun Dec  8 17:22:52 2019
                                                  ":"leaf01"}
TCA_RXMULTICAST_UPPER_1      TCA_RXMULTICAST_UPPE {"ifname":"swp3","hostname info             tca-tx-bytes-slack True   0                  Sun Dec  8 10:43:57 2019
                             R                    ":"leaf01"}
TCA_SENSOR_FAN_UPPER_1       TCA_SENSOR_FAN_UPPER {"hostname":"leaf01","s_na info             tca_slack_sensors  True   0                  Sun Dec  8 12:30:14 2019
                                                  me":"*"}
TCA_SENSOR_TEMPERATURE_UPPER TCA_SENSOR_TEMPERATU {"hostname":"leaf01","s_na critical         tca_slack_sensors  True   10                 Sun Dec  8 14:05:24 2019
_1                           RE_UPPER             me":"*"}
TCA_TXBYTES_UPPER_1          TCA_TXBYTES_UPPER    {"ifname":"swp3","hostname critical         tca-tx-bytes-slack True   100                Sun Dec  8 14:19:46 2019
                                                  ":"leaf01"}
TCA_TXMULTICAST_UPPER_1      TCA_TXMULTICAST_UPPE {"ifname":"swp3","hostname info             tca-tx-bytes-slack True   0                  Sun Dec  8 16:40:14 2269
                             R                    ":"leaf01"}
```

Example 2: Display a Specific TCA Rule

```
cumulus@switch:~$ netq show tca tca_id TCA_TXMULTICAST_UPPER_1
Matching config_tca records:
TCA Name                     Event Name           Scope                      Severity         Channel/s          Active Threshold          Suppress Until
---------------------------- -------------------- -------------------------- ---------------- ------------------ ------ ------------------ ----------------------------
TCA_TXMULTICAST_UPPER_1      TCA_TXMULTICAST_UPPE {"ifname":"swp3","hostname info             tca-tx-bytes-slack True   0                  Sun Dec  8 16:40:14 2269
                             R                    ":"leaf01"}
```

### Disable a TCA Rule

Where the `suppress` option temporarily disables a TCA rule, you can use the `is_active` option to disable a rule indefinitely. To disable a rule, set the option to *false*. To reenable it, set the option to *true*.

```
cumulus@switch:~$ netq add tca tca_id TCA_DISK_UTILIZATION_UPPER_1 is_active false
Successfully added/updated tca TCA_DISK_UTILIZATION_UPPER_1
```

### Delete a TCA Rule

If disabling a rule is not sufficient, and you want to remove a rule altogether, you can do so using the `netq del tca` command.

```
cumulus@switch:~$ netq del tca tca_id TCA_RXBYTES_UPPER_1
Successfully deleted TCA TCA_RXBYTES_UPPER_1
```

### Resolve Scope Conflicts

There may be occasions where the scope defined by the multiple rules for a given TCA event may overlap each other. In such cases, the TCA rule with the most specific scope that is still true is used to generate the event.

To clarify this, consider this example. Three events have occurred:

- First event on switch *leaf01*, interface *swp1*
- Second event on switch *leaf01*, interface *swp3*
- Third event on switch *spine01*, interface *swp1*

NetQ attempts to match the TCA event against hostname and interface name with three TCA rules with different scopes:

- Scope 1 send events for the *swp1* interface on switch *leaf01* (very specific)
- Scope 2 send events for all interfaces on switches that start with *leaf* (moderately specific)
- Scope 3 send events for all switches and interfaces (very broad)

The result is:

- For the first event, NetQ applies the scope from rule 1 because it matches scope 1 exactly
- For the second event, NetQ applies the scope from rule 2 because it does not match scope 1, but does match scope 2
- For the third event, NetQ applies the scope from rule 3 because it does not match either scope 1 or scope 2

In summary:

| Input Event | Scope Parameters | TCA Scope 1 | TCA Scope 2 | TCA Scope 3 | Scope Applied |
| --- | --- | --- | --- | --- | --- |
 leaf01,swp1 | Hostname, Interface | \'\*\',\'\*\' | leaf\*,\'\*\' | leaf01,swp1 | Scope 3 |
| leaf01,swp3 | Hostname, Interface | \'\*\',\'\*\' | leaf\*,\'\*\' | leaf01,swp1 | Scope 2 |
| spine01,swp1 | Hostname, Interface | \'\*\',\'\*\' | leaf\*,\'\*\' | leaf01,swp1 | Scope 1 |
