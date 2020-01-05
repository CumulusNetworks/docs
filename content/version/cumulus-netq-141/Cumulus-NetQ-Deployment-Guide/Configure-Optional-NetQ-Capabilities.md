---
title: Configure Optional NetQ Capabilities
author: Cumulus Networks
weight: 91
aliases:
 - /display/NETQ141/Configure+Optional+NetQ+Capabilities
 - /pages/viewpage.action?pageId=10453429
pageID: 10453429
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
After you have installed the Telemetry Server and the NetQ Agents, you
may want to configure some of the additional capabilities that NetQ
offers. This topic describes how to install, setup, and configure these
capabilities.

## Activate Early Access Features

NetQ contains [early access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined)
features that provide advanced access to new functionality before it
becomes generally available. The telemetry-based early access features
are bundled into the `netq-apps` package (installed automatically with
NetQ) ; there is no specific EA package like there typically is with
Cumulus Linux.

You enable early access features by running the ` netq config add
 `command. You disable the early access features by running the `netq
config del` command.

For example, to activate a feature:

1.  Log on to any switch or server running NetQ.

2.  Activate the early access feature set.

        cumulus@switch:~$ netq config add experimental

3.  Try out the features and provide feedback to your sales
    representative.  
    Usage information is contained in the [Cumulus NetQ Telemetry User
    Guide](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/).

The NetQ Image and Provisioning Management (IPM) application are
installed automatically, but not enabled.

To enable the IPM application:

1.  Log on to the NetQ Telemetry Server.

        <machine-name>:~<username>$ ssh cumulus@<telemetry-server-name-or-ip-address>
        cumulus@ts:~$

2.  Open required ports.

3.  Enable and start the IPM application (named *tips-appliance*).

        cumulus@ts:~$ sudo systemctl enable tips-appliance  
        Created symlink from /etc/systemd/system/multi-user.target.wants/tips-appliance.service to /lib/systemd/system/tips-appliance.service.
         
        cumulus@ts:~$ sudo systemctl start tips-appliance

    Once the IPM application is running, the IPM Command Line Interface,
    *TIPCTL*, is available. TIPCTL is the user interface used to
    activate, configure, and monitor the IPM application and services.

4.  Try out the application and provide feedback to your sales
    representative.  
    Usage information is contained in the [Cumulus NetQ Image and
    Provisioning Management User
    Guide](/version/cumulus-netq-141/Cumulus-NetQ-Image-and-Provisioning-Management-User-Guide/).

## Integrate NetQ with an Event Notification Application

By default, alert messages are sent to `rsyslog`; however, other
third-party tools may be configured to receive the alert messages . Once
you have observed the events received in `rsyslog` for some period of
time, you can more easily determine which events you want to direct to a
given notification application and how you might assign the events to
various event channels. You can integrate NetQ with a number of
third-party notification applications, including PagerDuty, Slack,
Elastic Logstash, and Splunk. You may integrate with one or more of
these applications with or without filtering the events sent. To set up
the integrations, you must configure the NetQ Notifier component on the
Telemetry Server.

### NetQ Notifier

NetQ Notifier is responsible for delivering alerts to users through
mediums such as Slack and syslog, informing users of network events.
NetQ Notifier listens for events on the
public subscription channel and writes them to
`/var/log/netq-notifier.log`. As events occur, NetQ Notifier
sends alert messages to `rsyslog`. NetQ Agents communicate directly with
NetQ Notifier. Note that if you are running the TS in [HA
mode](#src-10453429_ConfigureOptionalNetQCapabilities-HAConfig), then
NetQ Notifier only runs on the master instance of the TS and is
responsible for accepting messages for publication from all of the TS
instances (master and slaves).

{{% imgOld 0 %}}

Notifications can be generated for the following types of events:

  - BGP session state
  - Fan
  - License
  - Link
  - LNV session state
  - MLAG session state
  - NTP
  - OS
  - Port
  - PSU (power supply unit)
  - Services
  - Temperature

The NetQ Notifier is preconfigured to monitor for *all* events and
publish *all* alert messages. No additional configuration is required;
however, you can modify this default behavior to:

  - Limit the events that are logged: NetQ Notifier sends out alerts
    based on the configured logging level. If you want to change the
    default logging level of *info* to increase or decrease the set of
    events that are logged, refer to [Configure NetQ Notifier
    Logging](#src-10453429_ConfigureOptionalNetQCapabilities-NotifierLog).

  - Limit the events that are published: If you do not want to receive
    alerts for all events, you can limit the messages to publish by
    creating a NetQ Notifier filter. Refer to [Create NetQ Notifier
    Filters](#src-10453429_ConfigureOptionalNetQCapabilities-NotifierFilters)
    for details.

  - Use an alternate tool to view alerts: You can integrate NetQ
    Notifier with third-party event notification applications.
    Integration consists of setting a few parameters in the NetQ
    configuration file to identify the output, and then creating a
    filter to publish messages on that channel ([Create NetQ Notifier
    Filters](#src-10453429_ConfigureOptionalNetQCapabilities-NotifierFilters)).

NetQ Notifier was installed as part of the TS virtual machine
installation process and resides in the TS VM. You control the operation
of NetQ Notifier using `systemd` commands (such as `systemctl stop|start
netq-notifier`). You configure NetQ Notifier using the NetQ Notifier
CLI, or by manually editing the ` /etc/netq/netq.yml  `configuration
file.

#### Log Message Format

Messages have the following structure:

`<timestamp> <node> <service>[PID]: <level>: filter#<name>: <type>:
<message>`

| Element          | Description                                                                                                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timestamp        | Date and time event occurred in UTC format                                                                                                                                              |
| node             | Hostname of network node where event occurred                                                                                                                                           |
| service \[PID\]  | Service and Process IDentifier that generated the event                                                                                                                                 |
| level            | Logging level in which the given event is classified; *debug*, *error*, *info*, or *warning*                                                                                            |
| filter\#\<name\> | Name of filter that captured the event; a name of *none* indicates no notification is sent (even if logged); a name of *default* indicates no filter is applied (all messages are sent) |
| type             | Category of event; *BgpSession*, *Fan*, *License*, *Link*, *LnvSession*, *ClagSession*, *NTP*, *OS*, *Port*, *PSU*, *Services*, or *Temp*                                               |
| message          | Text description of event, including the node where the event occurred                                                                                                                  |

For example:

{{% imgOld 1 %}}

#### Default Output

Using `rsyslog`, a standard mechanism to capture log files in Linux,
NetQ Notifier sends alerts and events to the
`/var/log/netq-notifier.log`.

### NetQ Notifier CLI Overview

The NetQ Notifier Command Line Interface (CLI) is used to filter and
send notifications to third-party tools based on severity, service,
event-type, and device. The CLI enables you to configure these items
without editing the configuration file, reducing the risk of errors. The
commands must be run from the Telemetry Server. All commands begin with
`netq config ts`. You can use TAB completion or the help keyword to
assist when needed.

| Command       | Description                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------- |
| add           | Adds or modifies Notifier configuration, including filters, or sets master data node for DB cluster |
| del           | Removes existing Notifier configuration                                                             |
| reset-cluster | Resets DB cluster to force into known state                                                         |
| restart       | Restarts the Notifier daemon                                                                        |
| show          | Displays current DB server configuration or Notifier integrations                                   |
| start         | Starts the Notifier daemon                                                                          |
| status        | Display Notifier status                                                                             |
| stop          | Stop Notifier daemon                                                                                |

The command syntax is:

    ##Integrations
    netq config ts add notifier integration slack <text-integration-name> webhook <text-webhook-url> [severity <debug|info|warning|error>] [tag @<text-slack-tag>]
    netq config ts add notifier integration pagerduty <text-integration-name> api-access-key <text-api-access-key> api-integration-key <text-api-integration-key> [severity <debug|info|warning|error>]
     
    ##Filters
    netq config ts add notifier filter <text-filter-name> [before <text-filter-name-anchor>] [after <text-filter-name-anchor>] [rule <text-rule-key> <text-rule-value>] [output <text-integration-name-anchor>]
     
    ##Logging
    netq config ts add notifier loglevel [debug|error|info|warning] [json]
     
    ##Management
    netq config ts del notifier (slack|pagerduty) <text-integration-name-anchor>
    netq config ts del notifier filter <text-filter-name-anchor>
    netq config ts del notifier loglevel
     
    netq config ts (start|stop|restart|status) notifier
    netq config ts show notifier [<ip-server>|<text-server-name>|config] [json]
    netq config ts reset-cluster

The options are described in the following sections where they are used.

### Configure NetQ Notifier Logging

The logging level used by the NetQ Notifier determines what types of
messages are published and what messages are suppressed. Five levels of
logging are available, as shown in this table.

| Logging Level | Description  |
| ------------- | ------------ |
| debug         | Sends notifications for all debugging-related, informational, warning, error, and critical messages. |
| info          | Sends notifications for critical, informational, warning, and error messages (default).  |
| warning       | Sends notifications for critical, warning, and error messages. |
| error         | Sends notifications for critical and errors messages. |
| critical      | Sends notifications for critical messages. |

You can view the messages in the NetQ Notifier log, as shown here, or
use the notification applications for easier viewing.

    ...
    2018-10-01T18:46:00.337079+00:00 cumulus netq-notifier[5617]: INFO: filter#default: Link: mlx-2700-03 swp3s1: state changed from down to up
    2018-10-01T18:46:01.455979+00:00 cumulus netq-notifier[5617]: INFO: filter#default: Link: mlx-2700-03 hostbond3 (Local Node/s tor-1 and Ports swp3s0 <==> Remote Node/s hosts-11 and Ports swp1) (master: VlanA-1): state changed from down to up
    2018-10-01T18:46:02.590245+00:00 cumulus netq-notifier[5617]: INFO: filter#default: Link: mlx-2700-03 hostbond5 (Local Node/s tor-1 and Ports swp3s2 <==> Remote Node/s hosts-13 and Ports swp1) (master: VlanA-1): state changed from down to up
    2018-10-01T18:46:29.585642+00:00 cumulus netq-notifier[5617]: INFO: filter#default: Port: mlx-2700-03 swp3s2: port is now plugged
    2018-10-01T18:46:30.782686+00:00 cumulus netq-notifier[5617]: INFO: filter#default: Port: mlx-2700-03 swp3s3: port is now plugged
    2018-10-01T18:25:45.527880+00:00 cumulus netq-notifier[5617]: INFO: netq-notifier: Notifier processing messages because local REDIS is a master.
    2018-10-01T18:34:15.278120+00:00 cumulus netq-notifier[5617]: WARNING: filter#default: Port: mlx-2700-03 swp17: port is now empty
    2018-10-01T18:35:47.043010+00:00 cumulus netq-notifier[5617]: INFO: filter#default: Port: mlx-2700-03 swp17: port is now plugged
    2018-10-01T18:43:23.802855+00:00 cumulus netq-notifier[5617]: WARNING: filter#default: Link: mlx-2700-03 swp3s3: state changed from up to down
    2018-10-01T18:43:25.195741+00:00 cumulus netq-notifier[5617]: WARNING: filter#default: Link: mlx-2700-03 swp3s0: state changed from up to down
    2018-10-01T18:43:26.583027+00:00 cumulus netq-notifier[5617]: WARNING: filter#default: Link: mlx-2700-03 swp3s2: state changed from up to down
    netq-notifier.log:2018-09-26T23:45:19.622756+00:00 cumulus netq-notifier[2201]: CRITICAL: filter#default: Temp: act-omp03-lc101 temp95: state is absent
    netq-notifier.log:2018-09-26T23:45:19.623445+00:00 cumulus netq-notifier[2201]: CRITICAL: filter#default: Temp: act-omp03-lc101 temp96: state is absent
    netq-notifier.log:2018-09-26T23:45:19.624140+00:00 cumulus netq-notifier[2201]: CRITICAL: filter#default: Temp: act-omp03-lc101 temp97: state is absent
    netq-notifier.log:2018-09-26T23:45:19.624806+00:00 cumulus netq-notifier[2201]: CRITICAL: filter#default: Temp: act-omp03-lc101 temp98: state is absent
    netq-notifier.log:2018-09-26T23:45:19.625486+00:00 cumulus netq-notifier[2201]: CRITICAL: filter#default: Temp: act-omp03-lc101 temp99: state is absent
    netq-notifier.log.1:2018-09-27T22:37:28.380181+00:00 cumulus netq-notifier[844]: CRITICAL: filter#default: PSU: act-461054p-03 psu1: state is bad
    ...

**Example: Configure debug-level logging**

1.  Set the logging level to *debug.*

        cumulus@ts:~$ netq config ts add notifier loglevel debug

2.  Restart the NetQ Agent.

        cumulus@ts:~$ netq config ts restart notifier
        Restarting netq-notifier... Success!

3.  Verify connection to Telemetry Server.

        cumulus@ts:~$ netq config ts show server
        Server            Role       Master                             Replicas                           Status           Last Changed
        ----------------- ---------- ---------------------------------- ---------------------------------- ---------------- ----------------
        192.168.1.254     master     192.168.1.254                      -                                  ok               -

**Example: Configure warning-level logging**

    cumulus@switch:~$ netq config ts add notifier loglevel warning
    cumulus@switch:~$ netq config ts restart notifier
    cumulus@switch:~$ netq config ts show server

**Example: Disable NetQ Notifier Logging**

If you have set the logging level to
*debug* for troubleshooting, it is recommended that you either change
the logging level to a less heavy mode or completely disable agent
logging altogether when you are finished troubleshooting.

To change the logging level, run the
following command and restart the agent service:

    cumulus@switch:~$ netq config ts add notifier loglevel <LOG_LEVEL> 
    cumulus@switch:~$ netq config ts restart notifier

To disable all logging:

    cumulus@switch:~$ netq config ts del notifier loglevel 
    cumulus@switch:~$ netq config ts restart notifier

### Configure PagerDuty Using NetQ Notifier CLI

NetQ Notifier sends notifications to PagerDuty as PagerDuty events.

For example:

{{% imgOld 2 %}}

{{%notice note%}}

If NetQ generates multiple notifications, on the order of 50/second
(which can happen when a node reboots or when one peer in an MLAG pair
disconnects), PagerDuty does not see all these notifications. You may
see warnings in the netq-notifier.log file similar to this:

`2017-09-20T20:39:48.222458+00:00 rdsq1 netq-notifier[1]: WARNING:
Notifier: notifier-pagerduty: Request failed with exception: Code: 429,
msg: {"status":"throttle exceeded","message":"Requests for this service
are arriving too quickly. Please retry later."}`

This is a known limitation in PagerDuty at this time.

{{%/notice%}}

To configure NetQ Notifier to send notifications to PagerDuty:

1.  Configure the following options using the ` netq  ``config ts add
    notifier integration` command:

    | Option              | Description                                                                                                                                                        |
    | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | INTEGRATION\_TYPE   | The third-party notification system; use *pagerduty* in this case and provide a name for the integration.                                                          |
    | api-access-key      | The required API access key is also called the [authorization token](https://v2.developer.pagerduty.com/docs/authentication).                                      |
    | api-integration-key | The [integration](https://v2.developer.pagerduty.com/docs/events-api-v2) key is also called the service\_key or routing\_key. The default is an empty string (""). |
    | severity            | The log level to set, which can be one of *info*, *warning*, *error*, *critical* or *debug*. The severity defaults to *info*.                                      |


2.  Restart the NetQ Notifier service  
    For example:

        cumulus@ts:~$ netq config ts add notifier integration pagerduty pager-duty-test api-access-key 1234567890 api-integration-key 9876543210
        cumulus@ts:~$ netq config ts restart notifier

    These commands create a new notifier-integration configuration in
    the `/etc/netq/netq.yml` file.

        cumulus@ts:~$ cat /etc/netq/netq.yml
        backend:
          port: 6379
          role: master
          server: 127.0.0.1
        notifier-filters:
        - name: default
          output:
          - ALL
          rule:
        notifier-integrations:
        - api_access_key: 1234567890
          api_integration_key: 9876543210
          name: pager-duty-test
          severity: info
          type: pagerduty

### Configure Slack Using NetQ Notifier CLI

NetQ Notifier sends notifications to Slack as incoming webhooks for a
Slack channel you configure.

For example:

{{% imgOld 3 %}}

To configure NetQ Notifier to send notifications to Slack:

1.  If needed, create one or more Slack channels on which to receive the
    notifications.

    1.  Click + next to **Channels**.

    2.  Enter a name for the channel, and click **Create Channel**.

2.  Create an incoming WebHook.

    1.  Select **Customize Slack** from the Slack dropdown menu.

    2.  Click **Workspaces** in the top right corner, and select the
        workspace where the channel is located.

    3.  Click **Add Applications**, and select **Incoming WebHooks**.

    4.  Click **Add Configuration** and enter the name of the channel
        you created (where you want to post notifications).

    5.  Click **Add Incoming WebHooks integration**.

    6.  Save WebHook URL in a text file for use in next step.

3.  Configure the following options in the ` netq  ``config ts add
    notifier integration` command:

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
    <td><p>INTEGRATION_TYPE<br />
    INTEGRATION_NAME</p></td>
    <td><p>The third-party notification system; use <em>slack</em> in this case and provide a name for the integration.</p></td>
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
    <td><p>Optional tag appended to the Slack notification to highlight particular channels or people. The tag value must be preceded by the @ sign. For example, <em>@ts-info</em>.</p></td>
    </tr>
    </tbody>
    </table>

4.  Restart the NetQ Notifier service.  
    For example:

        cumulus@ts:~$ netq config ts add notifier integration slack slack-test webhook https://hooks.slack.com/services/text/moretext/evenmoretext severity warning tag @ts-warning
        cumulus@ts:~$ netq config ts restart notifier

    These commands create a new notifier-integration configuration in
    the `/etc/netq/netq.yml` file.

        cumulus@redis-1:~$ cat /etc/netq/netq.yml
        backend:
          port: 6379
          role: master
          server: 127.0.0.1
        notifier-filters:
        - name: default
          output:
          - ALL
          rule:
        notifier-integrations:
        - name: slack-test
          severity: warning
          tag: '@ts-warning'
          type: slack
          webhook: https://hooks.slack.com/services/text/moretext/evenmoretext

### Configure PagerDuty Manually

If you prefer to edit the `netq.yml` file directly, rather than use the
NetQ Notifier CLI, you can do so.

To configure alerts and PagerDuty integrations on the NetQ Telemetry
Server:

1.  As a sudo user, open `/etc/netq/netq.yml` in a text editor.

2.  Optionally, change the logging level, if you want a more restrictive
    level than *info* by adding the following two lines to the file:

        ...
        netq-notifier:
          log_level: warning
        ...

3.  Configure PagerDuty: Input the information for this integration into
    the notifier-integrations stanza, using the syntax shown in the
    example:

    1.  Add the notifier-integrations stanza.

    2.  Add a name, such as *notifier-pagerduty or netq-notifier*. Note:
        no spaces are allowed in the name. Use a dash instead if you
        want to separate words as shown here.

    3.  Add the type of *pagerduty*.

    4.  Add the message severity level, *debug*, *info*, *warning*,
        *error*, or *critical*.

    5.  Add the API access key (also called the [authorization
        token](https://v2.developer.pagerduty.com/docs/authentication))
        and the
        [integration](https://v2.developer.pagerduty.com/docs/events-api-v2)
        key (also called the service\_key or routing\_key).

            notifier-integrations:
              - name: notifier-pagerduty
                type: pagerduty
                severity: WARNING (does this need to be in all caps?)
                api_access_key: <API Key>
                api_integration_key: <API Integration Key>

4.  When you are finished editing the file, save and close it.

5.  Stop then start the NetQ Notifier daemon to apply the new
    configuration.

        cumulus@ts:~$ sudo systemctl restart netq-notifier

### Configure Slack Manually

If you prefer to edit the `netq.yml` file directly, rather than using
the NetQ Notifier CLI, you can do so.

To configure alerts and Slack integrations on the NetQ Telemetry Server:

1.  As a sudo user, open `/etc/netq/netq.yml` in a text editor.

2.  Optionally, change the logging level, if you want a more restrictive
    level than *info* by adding the following two lines to the file.

        ...
        netq-notifier:
          log_level: warning
        ...

3.  Configure Slack: Input the information for this integration into the
    notifier-integrations stanza, using the syntax shown in the example.

    1.  Add the the notifier-integrations stanza.

    2.  Add a name, such as *notifier-slack-channel-1* or
        *netq-notifier*. Note: no spaces are allowed in the name. Use a
        dash instead if you want to separate words as shown here.

    3.  Add the type of *slack*.

    4.  Add the webhook URL. To obtain this:

        1.  In the desired Slack channel, locate the initial message
            indicating the addition of the integration, click
            **incoming-webhook** link, click **Settings**.

            {{% imgOld 4 %}}

        2.  The URL produced by Slack looks similar to the one shown
            here:

            {{% imgOld 5 %}}

    5.  Add the message severity level, *debug*, *info*, *warning*, or
        *error*.

    6.  Optionally add a tag, such as *@netqts-sys* or *@ts-info*.

            notifier-integrations:
              - name: notifier-slack-channel-1
                type: slack
                webhook: "https://hooks.slack.com/services/sometext/moretext/evenmoretext"
                severity: INFO
                tag: "@netqts-sys"

4.  When you are finished editing the file, save and close it.

5.  Stop then start the NetQ Notifier daemon to apply the new
    configuration.

        cumulus@netq-appliance:~$ sudo systemctl restart netq-notifier

    {{%notice tip%}}

If your webhook does not immediately send a message to your channel,
 look for errors in syntax. Check the log file located at
 `/var/log/netq-notifier.log`.

    {{%/notice%}}

### View Integrations

You can view configured integrations using the `netq config ts show
notifier` command. Include the `json` option to display JSON-formatted
output.

For example:

    cumulus@ts:~$ netq config ts show notifier integration
    Integration Name    Attribute    Value
    ------------------  -----------  -----------------------------------------------------------
    slack-test          type         slack
                        tag          @ts-info
                        webhook      https://hooks.slack.com/services/text/moretext/evenmoretext
                        severity     info
    pager-duty-test     api_integration_key  9876543210
                        type                 pagerduty
                        severity             info
                        api_access_key       1234567890
     
    Filter Name    Attribute    Value
    -------------  -----------  -------
    default        output       ALL
                   rule

### Export Notifications to ELK

NetQ Notifier integrates with ELK/Logstash using plugins to handle
`rsyslog` inputs.

For example:  

{{% imgOld 6 %}}

To configure NetQ Notifier to send data to ELK through Logstash:

1.  On the host running the Telemetry Server and NetQ Notifier,
    configure the notifier to send the logs to a Logstash instance by
    adding the following to the logstash configuration file.  
    In this example, the Logstash instance is on a host with the IP
    address 192.168.50.30, using port 51414.

        # rsyslog - logstash configuration
        sed -i '/$netq_notifier_log/a if $programname == "netq-notifier" then @@192.168.50.30:51414' /etc/rsyslog.d\
        /50-netq-notifier.conf

2.  Restart `rsyslog`.

        root@ts:~# systemctl restart rsyslog

3.  On the server running the Logstash instance at the address specified
    earlier, create a file in `/etc/logstash/conf.d/` called
    `notifier_logstash.conf`. Then add the following definition, using
    the port you specified earlier.

        root@ts:~# vi /etc/logstash/conf.d/notifier_logstash.conf
         
        input {
            syslog {
                type => syslog
                port => 51414                                                                
            }
        }
        output {
            file {
                path => "/tmp/logstash_notifier.log"                                                                                  
            }
        }

4.  Restart Logstash.

        root@logstash_host:~# systemctl restart logstash

NetQ Notifier logs now appear in `/tmp/logstash_notifier.log` on the
Logstash host.

### Export Notifications to Splunk

NetQ integrates with Splunk using plugins to handle `rsyslog` inputs.

For example:

{{% imgOld 7 %}}

To configure NetQ Notifier to send data to Splunk for display:

1.  On the host running the Telemetry Server and NetQ Notifier,
    configure the notifier to send the logs to a Splunk by adding the
    following to the Splunk configuration file.  
    In this example, Splunk is installed on a host with the IP address
    192.168.50.30, using port 51414.

        # rsyslog - splunk configuration
        sed -i '/$netq_notifier_log/a if $programname == "netq-notifier " then @@192.168.50.30:51415' /etc/rsyslog.d\
        /50-netq-notifier.conf

2.  Restart `rsyslog`.

        root@ts:~# systemctl restart rsyslog

3.  Open Splunk in a browser, choose **Add Data** \> **monitor** \>
    **TCP** \> **Port**, and set it to *51415*.

4.  Click **Next**, then choose **Source Type (syslog)** \> **Review**
    \> **Done**.

NetQ Notifier messages now appear in Splunk.

## Create NetQ Notifier Filters

You can limit or direct log messages sent by NetQ Notifier using
filters. Filters are created based on rules you define. Each filter
contains one or more rules. Each rule contains a single key-value pair.
When a message matches the rule, it is sent to the indicated
destination. The default rule is matches all messages. You can specify
rules using entities such as hostnames or interface names in the regular
expression, enabling you to filter messages specific to those hosts or
interfaces. Additionally, you can send log messages to PagerDuty or a
given Slack channel using the *output* keyword; you need to have already
defined the PagerDuty or Slack configurations (as described earlier).

By default, filters are processed in the order they appear in the
`netq.yml` configuration file (from top to bottom) until a match is
found. This means that each event message is first evaluated by the
first filter listed, and if it matches then it is processed, ignoring
all other filters, and the system moves on to the next event message
received. If the event does not match the first filter, it is tested
against the second filter, and if it matches then it is processed and
the system moves on to the next event received. And so forth. Events
that do not match any filter are ignored. This diagram shows an example
with four defined filters with sample output results.

{{% imgOld 8 %}}

When you create a new filter, it is automatically added to the top of
the list, before all others, so you may need to rearrange them to ensure
you capture the events you want and drop the events you do not want.
Optionally, you can use a *before* or *after* keyword to ensure one rule
is processed before or after another.

{{%notice note%}}

Filter names may contain spaces, but must be enclosed with single quotes
in commands. It is easier to use dashes in place of spaces or mixed case
for better readability. For example, use bgpSessionChanges or
BGP-session-changes or BGPsessions, instead of 'BGP Session Changes'.
Filter names are also case sensitive.

{{%/notice%}}

You must restart the NetQ Notifier service after configuring filters so
they can take effect; run the `netq config ts restart notifier` command.

### Build Filter Rules

Each rule is comprised of a single key-value pair. Creating multiple
rules for a given filter can provide a very defined filter. There is a
fixed set of valid rule keys. Values are entered as regular expressions
and *vary according to your deployment*.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Rule Key</p></th>
<th><p>Rule Values</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BgpSession</p></td>
<td><p>Regular expression identifying a hostname, peer name, ASN, or VRF</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>peer_name: server4, leaf*, exit02, spine0*</p></li>
<li><p>asn: 65020, 65012</p></li>
<li><p>vrf: mgmt, default</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>ClagSession</p></td>
<td><p>Regular expression identifying a hostname or CLAG system MAC address</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>Clag_sysmac: 44:38:39:00:00:5C</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Fan</p></td>
<td><p>Regular expression identifying a hostname, sensor name, or sensor description</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>s_name: fan*</p></li>
<li><p>s_desc: 'fan 1, tray*'</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>hostname</p></td>
<td><p>Regular expression identifying a hostname</p>
<p>For example, hosts-0* or spine*.</p></td>
</tr>
<tr class="odd">
<td><p>License</p></td>
<td><p>Regular expression identifying a hostname or license name</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>name: Cumulus Linux, Ubuntu, CentOS</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Link</p></td>
<td><p>Regular expression identifying a hostname, interface name, or kind of link</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>ifname: eth0, swp*</p></li>
<li><p>kind: bond, bridge, eth, loopback, macvlan, swp, vlan, vrf, vxlan</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>LnvSession</p></td>
<td><p>Regular expression identifying a hostname or role</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>OS</p></td>
<td><p>Regular expression identifying a hostname</p>
<p>For example, hosts-0* or spine*.</p></td>
</tr>
<tr class="odd">
<td><p>Port</p></td>
<td><p>Regular expression identifying a hostname or interface name</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>ifname : eth0, swp*</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>PSU</p></td>
<td><p>Regular expression identifying a hostname, sensor name</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>s_nam e: psu*, psu2</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Services</p></td>
<td><p>Regular expression identifying a hostname, service name, or VRF</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>name: clagd, lldpd, ssh, ntp, netqd, net-agent</p></li>
<li><p>vrf: mgmt, default</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Temp</p></td>
<td><p>Regular expression identifying a hostname, sensor name, sensor description</p>
<p>Examples:</p>
<ul>
<li><p>hostname: server02, leaf*, exit01, spine0*</p></li>
<li><p>s_name: psu1temp*, temp*</p></li>
<li><p>s_desc: 'board sensor near fan'</p></li>
</ul></td>
</tr>
</tbody>
</table>

{{%notice note%}}

Rules are case sensitive. Use Tab completion to view the command options
syntax.

{{%/notice%}}

### Specify Output Location

The filter results may be output to a defined integration (integration
name), to syslog (*default*), to all integrations and syslog (*all*), or
not at all (*None*).

### Example: Create a Filter for Events from Selected Switches

In this example, we created a NetQ Notifier integration with an existing
Slack channel called *slack-channel-leaf-alerts*. We then created a
filter called *leaf-filter* for any notifications that mention switches
named *leaf-0\**. The result is that any log messages mentioning one of
those host names is filtered to the *slack-channel-leaf-alerts* channel.

    cumulus@ts:~$ netq config ts add notifier integration slack slack-channel-leaf-alerts webhook https://hooks.slack.com/services/text/moretext/evenmoretext severity info
    cumulus@ts:~$ netq config ts add notifier filter leaf-filter rule hostname leaf-0* output slack-channel-leaf-alerts
    cumulus@ts:~$ netq config ts restart notifier
    cumulus@ts:~$ netq config ts show notifier
    Integration Name           Attribute    Value
    -------------------------  -----------  -----------------------------------------------------------
    slack-channel-leaf-alerts  type         slack
                               webhook      https://hooks.slack.com/services/text/moretext/evenmoretext
                               severity     info
     
     
    Filter Name    Attribute    Value
    -------------  -----------  -------------------------
    leaf-filter    output       slack-channel-leaf-alerts
                   rule         hostname: leaf-0*
    default        output       ALL
                   rule

### Example: Verify NetQ Notifier Status

In this example, we are looking to see whether the NetQ Notifier is up
and running. If it were not, we would want to restart it.

    cumulus@ts:/$ netq config ts status notifier
    netq-notifier... Running

### Example: Add Multiple Rules to a Filter

In this example, we created a filter with three rules to drop
notifications from a particular link.

    cumulus@ts:~$ netq config ts add notifier filter leaf01-swp1-drop rule type Link output None
    cumulus@ts:~$ netq config ts add notifier filter leaf01-swp1-drop rule hostname leaf01 output None
    cumulus@ts:~$ netq config ts add notifier filter leaf01-swp1-drop rule ifname swp1 output None
    cumulus@ts:~$ netq config ts restart notifier
    cumulus@ts:!$ netq config ts show notifier
    Integration Name           Attribute    Value
    -------------------------  -----------  -----------------------------------------------------------
    None
     
    Filter Name       Attribute    Value
    -------------     -----------  -------------------------
    leaf01-swp1-drop  output       None
                      rule         type: Link
                                   hostname: leaf01
                                   ifname: swp1

    default        output       ALL
                   rule

### Example: Place One Filter Before or After Another Filter

In this example, we created a filter, *interface-filter*, that is
processed after *bgp-filter* (an existing filter) and sent the
notifications to a defined slack channel, *slack-channel-if-alerts*. Use
the **before** keyword to place the new filter before the *bgp-filter*.
Note that you must restart the Notifier for this configuration change to
take effect. Verify the configuration using the `show` command.

    cumulus@ts:~$ netq config ts add notifier filter interface-filter after bgp-filter rule Port swp* output slack-channel-if-alerts
    cumulus@ts:~$ netq config ts restart notifier
    cumulus@ts:!$ netq config ts show notifier
    Integration Name           Attribute    Value
    -------------------------  -----------  -----------------------------------------------------------
    slack-channel-bgp-alerts   type         slack
                               webhook      https://hooks.slack.com/services/text/moretext/evenmoretext
                               severity     info
    slack-channel-if-alerts    type         slack
                               webhook      https://hooks.slack.com/services/text/moretext/evenmoretext
                               severity     info
     
    Filter Name    Attribute    Value
    -------------  -----------  -------------------------
    bgp-filter     output       slack-channel-bgp-alerts
                   rule         BgpSession: all
    if-filter      output       slack-channel-if-alerts
                   rule         Port: swp*
    default        output       ALL
                   rule

Alternately, you may edit the `netq.yml` file directly adding the
following integrations and filters:

    cumulus@ts:~$ nano netq.yml
    ...
    notifier-integrations:
      - name: slack-channel-bgp-alerts
        type: slack
        webhook: "https://hooks.slack.com/services/sometext/moretext/evenmoretext"
        severity: INFO
      - name: slack-channel-if-alerts
        type: slack
        webhook: "https://hooks.slack.com/services/sometext/moretext/evenmoretext"
        severity: INFO
     
    notifier-filters:
      - name: bgp-filter
        rule:
          BgpSession: all
        output:
          - slack-channel-bgp-alerts
      - name: if-filter
        rule:
          Port: swp*
        output:
          - slack-channel-if-alerts
    ...
    cumulus@ts:~$ netq config ts restart notifier

### Example: Create a Filter to Drop Notifications from a Given Interface

In this example, we created a filter, *ifswp21drop*, that drops
notifications for events from interface *swp21*. Make sure to capitalize
the Port rule option. Note that you must restart the Notifier for this
configuration change to take effect.

    cumulus@ts:~$ netq config ts add notifier filter ifswp1drop rule Port swp21
    cumulus@ts:~$ netq config ts add notifier filter ifswp1drop output None
    cumulus@ts:~$ netq config ts restart notifier

or

    cumulus@ts:~$ nano netq.yml
    ...
    notifier-filters:
      - name: ifswp21drop
        rule:
          Port: swp21
        output:
          - None
    ...
    cumulus@ts:~$ netq config ts restart notifier

### Example: Create a Filter to Send BGP Session State Notifications to Slack

In this example, we created a filter, *BGPslackchannel*, to send BGP
session state notifications to an existing Slack channel,
*slack-channel-BGP*, and all other event notifications to a generic
Slack channel, *slack-channel-catchall*. The Slack integration should be
created before creating the filter. Note that you must restart the
Notifier for this configuration change to take effect.

    cumulus@ts:~$ netq config ts add notifier filter BGPslackchannel rule BgpSession all
    cumulus@ts:~$ netq config ts add notifier filter BGPslackchannel output slack-channel-BGP
    cumulus@ts:~$ netq config ts add notifier filter default output slack-channel-catchall
    cumulus@ts:~$ netq config ts restart notifier

or

    notifier-filters:
      - name: BGPslackchannel
        rule:
          type: BgpSession
        output:
          - slack-channel-BGP
     - name: default
       rule:
       output:
         - slack-channel-catchall

### Example: Create a Filter to Drop All Temperature-Related Event Notifications

In this example, we created a filter, tempDrop, to drop all temperature
related event notifications. Note: capitalization is important with
these rules. Use Tab completion to view the command options syntax.
Restart the Notifier for this configuration change to take effect.

    cumulus@ts:~$ netq config ts add notifier filter tempDrop rule Temp all
    cumulus@ts:~$ netq config ts add notifier filter tempDrop output None
    cumulus@ts:~$ netq config ts restart notifier

### Example: Create a Filter for License Validation Event Notifications

In this example, we created a filter, license-valid, to notify persons
with access to a PagerDuty messages on the pager-duty-license channel
when an invalid license is detected on *spine01*. Note: capitalization
is important with these rules. Use Tab completion to view the command
options syntax. Restart the Notifier for this configuration change to
take effect.

    cumulus@ts:~$ netq config ts add notifier pagerduty pager-duty-license api-access-key 1234567890 api-integration-key 9876543210
    cumulus@ts:~$ netq config ts add notifier filter license-valid rule License spine01
    cumulus@ts:~$ netq config ts add notifier filter license-valid output pager-duty-license
    cumulus@ts:~$ netq config ts restart notifier
     
    cumulus@ts:~$ netq config ts show notifier integration
    Integration Name    Attribute    Value
    ------------------  -----------  -----------------------------------------------------------
    pager-duty-license  api_integration_key  9876543210
                        type                 pagerduty
                        severity             info
                        api_access_key       1234567890
     
    Filter Name     Attribute    Value
    -------------   -----------  -------
    license-expired output      pager-duty-license
                    rule        License: spine01
    default         output      ALL
                    rule

## Configure High Availability Mode

NetQ supports high availability - that is, the ability to continue
functioning even in the absence of a single failure of a Telemetry
Server node. To make the NetQ Telemetry Server highly available (*HA
mode*), you need to run three instances of the Telemetry Server.
Currently, exactly three instances are supported in HA mode. Of the
three instances, one is considered the *master* and is writeable while
the other two are read-only *replicas*. Each server instance is mapped
to port 6379 on the host. A Redis
*[sentinel](https://redis.io/topics/sentinel)* on each Telemetry Server
host monitors the health of the database cluster and decides which
database is the current master. If the master becomes unavailable, the
sentinel promotes one of the replicas to become the new master. Each
sentinel runs on port 26379.

HA mode is optional.

### Configure HA Mode

Perform the following steps to configure HA Mode:

{{% imgOld 9 %}}

1.  Install the Telemetry Server image on three separate physical hosts
    to form a database cluster.

    1.  Use the instructions for installing the TS here.

        {{%notice note%}}

For proper operation of the HA mode you must specify the IP
addresses for the Telemetry Servers. You cannot use DNS names.

        {{%/notice%}}

    2.  Note the IP address of each instance.

2.  Enable HA Mode  
    These steps assume three Telemetry Servers, ts01 (the original one
    which was [already
    configured](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
    as the Telemetry Server), ts02 and ts03, which are assigned IP
    addresses 10.0.0.5, 10.0.0.6 and 10.0.0.7, respectively. The servers
    are all assumed to be up and reachable and can communicate with each
    other.  
    On each Telemetry Server, specify the IP address of the master and
    both replicas, and then restart the netq-notifier service. Wait at
    least 30 seconds between each instance of the command.

        cumulus@ts01:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.7
        cumulus@ts01:~$ sudo systemctl restart netq-notifier.service

        cumulus@ts02:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.7
        cumulus@ts02:~$ sudo systemctl restart netq-notifier.service

        cumulus@ts03:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.7
        cumulus@ts03:~$ sudo systemctl restart netq-notifier.service

3.  Verify that HA mode is configured on the three Telemetry Servers.  
    Each server should indicate that ts01 (using IP address 10.0.0.5) is
    the master.

        cumulus@ts01:~$ netq config ts show server
        Server    Role     Master    Replicas            Status    Last Changed
        --------  -------  --------  ------------------  --------  --------------
        10.0.0.5  master   10.0.0.5  10.0.0.7, 10.0.0.6  ok        55s
        10.0.0.6  replica  10.0.0.5  -                   ok        55s
        10.0.0.7  replica  10.0.0.5  -                   ok        55s

        cumulus@ts02:~$ netq config ts show server
        Server    Role     Master    Replicas            Status    Last Changed
        --------  -------  --------  ------------------  --------  --------------
        10.0.0.5  master   10.0.0.5  10.0.0.7, 10.0.0.6  ok        55s
        10.0.0.6  replica  10.0.0.5  -                   ok        55s
        10.0.0.7  replica  10.0.0.5  -                   ok        55s

        cumulus@ts03:~$ netq config ts show server
        Server    Role     Master    Replicas            Status    Last Changed
        --------  -------  --------  ------------------  --------  --------------
        10.0.0.5  master   10.0.0.5  10.0.0.7, 10.0.0.6  ok        55s
        10.0.0.6  replica  10.0.0.5  -                   ok        55s
        10.0.0.7  replica  10.0.0.5  -                   ok        55s

4.  Update the NetQ Agent on each switch and server node you are
    monitoring to point to the HA cluster, and restart the NetQ Agent.

        cumulus@switch:~$ netq config add server 10.0.0.5 10.0.0.6 10.0.0.7
        Restarting netqd... Success!
        cumulus@switch:~$ netq config restart agent
        Restarting netq-agent... Success!

    You could automate this step to update all of the agents on your
    monitored nodes.

### Check Database Cluster Status

Run the following `show` command from one of the Telemetry Servers.

    cumulus@ts01:~$ netq config ts show server

Optionally, you can view detailed output for a specific server in the
cluster by specifying that server's IP address.

    cumulus@ts01:~$ netq config ts show server 10.0.0.7

### Restart HA Mode Services

You can restart the `netq-appliance` service using:

    cumulus@ts01:~$ sudo systemctl restart netq-appliance.service

### Change the Master Telemetry Server

You can change which Telemetry Server you want to be the master simply
by changing the order in which you specify them with the `netq config ts
add server` command. You need to run the following command on each
Telemetry Server, waiting at least 30 seconds in between updating the
configuration on each server.

For example, notice that the Telemetry Server *ts01* is the master in
the following configuration:

    cumulus@ts01:~$ netq config ts show server
    Server    Role     Master    Replicas            Status    Last Changed
    --------  -------  --------  ------------------  --------  --------------
    10.0.0.5  master   10.0.0.5  10.0.0.6, 10.0.0.7  ok        50s
    10.0.0.6  replica  10.0.0.5  -                   ok        50s
    10.0.0.7  replica  10.0.0.5  -                   ok        50s

To make the first replica the new master, run the following command on
each Telemetry Server (you don't need to change anything on the switch
and server nodes):

    cumulus@ts01:~$ netq config ts add server 10.0.0.6 10.0.0.5 10.0.0.7

    cumulus@ts02:~$ netq config ts add server 10.0.0.6 10.0.0.5 10.0.0.7

    cumulus@ts03:~$ netq config ts add server 10.0.0.6 10.0.0.5 10.0.0.7

Verify that *ts02* is the new master:

    cumulus@ts01:~$ netq config ts show server
    Server    Role     Master    Replicas            Status    Last Changed
    --------  -------  --------  ------------------  --------  --------------
    10.0.0.5  replica  10.0.0.6  -                   ok        28s
    10.0.0.6  master   10.0.0.6  10.0.0.7, 10.0.0.5  ok        28s
    10.0.0.7  replica  10.0.0.6  -                   ok        28s

### Replace a Replica with a New Server

If you need to replace a Telemetry Server with a different physical
system, follow the instructions include in this topic.

{{%notice note%}}

Do not try and replace the master server. You can only replace a
replica. If you need to replace the master, make it a replica first, as
described above.

{{%/notice%}}

For illustrative purposes, we are using the following cluster of
Telemetry Servers, where 10.0.0.5 (ts01) is the master, while 10.0.0.6
(ts02) and 10.0.0.7 (ts03) are the replicas.

    cumulus@ts01:~$ netq config ts show server
    Server    Role     Master    Replicas            Status    Last Changed
    --------  -------  --------  ------------------  --------  --------------
    10.0.0.5  master   10.0.0.5  10.0.0.6, 10.0.0.7  ok        14m:10s
    10.0.0.6  replica  10.0.0.5  -                   ok        14m:10s
    10.0.0.7  replica  10.0.0.5  -                   ok        14m:10s

In our example, you want to replace ts03 with ts04 (10.0.0.8):

1.  Bring up the new Telemetry Server (ts04) and make sure the
    connectivity is okay.

2.  Log in to the Telemetry Server you are replacing (ts03) and power it
    down:

        cumulus@ts03:~$ sudo shutdown

3.  Execute the following NetQ command on every Telemetry Server to
    create a cluster with the new Telemetry Server. Wait at least 30
    seconds between each instance of the command.

        cumulus@ts01:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.8

        cumulus@ts02:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.8

        cumulus@ts04:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.8

4.  Verify the HA status on one of the Telemetry Servers. The status
    should be the same on all the three Telemetry Servers indicating
    that ts01 (10.0.0.5) is the master.

        cumulus@ts01:~$ netq config ts show server
        Server    Role     Master    Replicas            Status    Last Changed
        --------  -------  --------  ------------------  --------  --------------
        10.0.0.5  master   10.0.0.5  10.0.0.6, 10.0.0.8  ok        5m:10s
        10.0.0.6  replica  10.0.0.5  -                   ok        5m:10s
        10.0.0.8  replica  10.0.0.5  -                   ok        5m:10s 

5.  Update the agent on each switch and server node to point to the new
    HA cluster, and restart the NetQ Agent on each node:

        cumulus@switch:~$ netq config add server 10.0.0.5 10.0.0.6 10.0.0.8
        Restarting netqd... Success!
        cumulus@switch:~$ netq config restart agent
        Restarting netq-agent... Success!

### Reset the Database Cluster

You can force a reset of the Redis HA cluster using:

    cumulus@netq-ts:~$ netq config ts reset-cluster

### Troubleshoot HA Mode

#### Relevant Services and Configuration Files

The following `systemd` services are involved in HA mode:

  - cts-auth.service: The Telemetry Server-side service that manages the
    configuration.
  - cts-auth.socket: The Telemetry Server-side authorization shim socket
    for the service console.
  - cts-backup.service: Runs a cron job to back up the Redis database.
  - cts-backup.timer: The timer for the backup service, with a minimum
    interval of 5 minutes.
  - netqd.service: The service for the Telemetry Server CLI for use
    locally on the server.
  - netq-appliance.service: Starts and stops all Telemetry Server
    services **except** for the `ts-gui` service.
  - netq-gui.service: Starts and stops Telemetry Server `ts-gui`
    service.
  - netq-influxdb.service: The service that manages the HA mode
    InfluxDB.
  - netq-notifier.service: Starts and stops the NetQ Notifier service.

The following configuration files are in the `/etc/cts/run/redis`
directory:

  - redis\_6379.conf: Contains the runtime Redis database configuration
    and state.
  - snt1.conf: Contains the runtime Redis sentinel configuration and
    state.

The following log file is in the `/var/log` directory:

  - netqd.log: The logs associated with running the NetQ CLI locally on
    the machine.

The NetQ Notifier log is:

  - /var/log/netq- notifier .log

Logging configurations are in:

  - /etc/rsyslog.d
  - /etc/logrotate.d

The following log files are in the `/var/log/cts` directory:

  - cts-backup.log
  - cts-docker-compose.log
  - cts-dockerd.log
  - cts-redis.log
  - cts-sentinel.log

The `/etc/cts/environment` file sets key environment variables that
control the behavior of the NetQ Telemetry Server.

  - `REDIS_MEMORY_PCT`: Setting this variable to a value between 10 and
    90 allocates that specified percent of the VM's memory to REDIS. The
    default value is 60. You can check the currrent allocation with the
    following command:

        vagrant@netq-1:~$ /usr/sbin/netq-adjust-mem --show
        Current maxmemory 2442384998 is 0.60 of 4070641664 available.

For more information about the log files, see the [Investigate NetQ
Issues](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Resolve-Issues/Investigate-NetQ-Issues)
topic.

#### One Replica Must Be Available Always

While HA mode is enabled, if both the replica servers go down, the
master database stops accepting writes. This causes the NetQ agents to
go into a rotten state.

This serves to avoid having multiple masters in a split-brain condition.
Please refer to the section "Example 2: basic setup with three boxes" on
the [Redis Sentinel page](https://redis.io/topics/sentinel) for more
details.

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

        cumulus@chassis-lc101:~$ sudo nano /etc/netq/netq.yml
         
        ...
        netq-agent:
          send_chassis_sensor_data: true
        ...

## Extending NetQ with Custom Services Using curl

You can extend NetQ to monitor parameters beyond what it monitors by
default. For example, you can create a service that runs a series of
pings to a known host or between two known hosts to ensure that
connectivity is valid. Or you can create a service that curls a URL and
sends the output to `/dev/null`. This method works with the [NetQ time
machine](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Resolve-Issues/Methods-for-Diagnosing-Network-Issues)
capability regarding `netq show services`.

1.  As the sudo user on a node running the NetQ agent, edit the
    `/etc/netq/config.d/netq-agent-commands.yml` file.

2.  Create the custom service. In the example below, the new service is
    called *web*. You need to specify:

      - The *period* in seconds.

      - The *key* that identifies the name of the service.

      - The command will *run* always. If you do not specify *always*
        here, you must enable the service manually using `systemctl`.

      - The *command* to run. In this case we are using `curl` to ping a
        web server.

    <!-- end list -->

        cumulus@leaf01:~$ sudo vi /etc/netq/config.d/netq-agent-commands.yml
         
        user-commands:
          - service: 'misc'
            commands:
              - period: "60"
                key: "config-interfaces"
                command: "/bin/cat /etc/network/interfaces"
              - period: "60"
                key: "config-ntp"
                command: "/bin/cat /etc/ntp.conf"
          - service: "zebra"
            commands:
              - period: "60"
                key: "config-quagga"
                command: ["/usr/bin/vtysh", "-c", "show running-config"]
         
          - service: "web"
            commands:
              - period: "60"
                key: "webping"
                run: "always"
                command: ['/usr/bin/curl https://cumulusnetworks.com/ -o /dev/null']

3.  After you save and close the file, restart the NetQ agent:

        cumulus@leaf01:~$ netq config agent restart

4.  You can verify the command is running by checking the
    `/var/run/netq-agent-running.json` file:

        cumulus@leaf01:~$ cat /var/run/netq-agent-running.json
        {"commands": [{"service": "smond", "always": false, "period": 30, "callback": {}, "command": "/usr/sbin/smonctl -j", "key": "smonctl-json"}, {"service": "misc", "always": false, "period": 30, "callback": {}, "command": "/usr/sbin/switchd -lic", "key": "cl-license"}, {"service": "misc", "always": false, "period": 30, "callback": {}, "command": null, "key": "ports"}, {"service": "misc", "always": false, "period": 60, "callback": null, "command": "/bin/cat /etc/network/interfaces", "key": "config-interfaces"}, {"service": "misc", "always": false, "period": 60, "callback": null, "command": "/bin/cat /etc/ntp.conf", "key": "config-ntp"}, {"service": "lldpd", "always": false, "period": 30, "callback": {}, "command": "/usr/sbin/lldpctl -f json", "key": "lldp-neighbor-json"}, {"service": "mstpd", "always": false, "period": 15, "callback": {}, "command": "/sbin/mstpctl showall json", "key": "mstpctl-bridge-json"}], "backend": {"server": "10.0.0.165"}}

5.  And you can see the service is running on the host when you run
    `netq show services`:

        cumulus@leaf01:~$ netq show services web

