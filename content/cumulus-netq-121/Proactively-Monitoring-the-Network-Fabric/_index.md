---
title: Proactively Monitoring the Network Fabric
author: Cumulus Networks
weight: 19
aliases:
 - /display/NETQ121/Proactively+Monitoring+the+Network+Fabric
 - /pages/viewpage.action?pageId=8356545
pageID: 8356545
product: Cumulus NetQ
version: "1.2"
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---

NetQ continually and algorithmically checks for various network events
(see below) and sends real-time alerts via *NetQ Notifier* to notify
users that a network event occurs. When alerted, you can determine
precisely where the fault occurred so you can remediate quickly.

You can create filters for how to handle notifications and you can also
ignore notifications.

## NetQ Notifier</span>

The NetQ Notifier's role within the NetQ suite of applications is to
deliver alerts to users through mediums such as Slack and syslog,
informing users of network events.

{{% imgOld 0 %}}

Notifications can be generated for the following network events:

  - Agent node state

  - Backend connections

  - Fan

  - License

  - NTP

  - OS

  - Port

  - PSU

  - Services

  - Temperature

When a notification arrives, what should you do next? Typically, you
could run `netq check` commands; see [Performing Network
Diagnostics](/cumulus-netq-121/Performing-Network-Diagnostics)
for more information. For a thorough example, read about troubleshooting
[MLAG node
failures](/cumulus-netq-121/Proactively-Monitoring-the-Network-Fabric/MLAG-Troubleshooting-with-NetQ).

### Log Message Format</span>

Messages have the following structure:

    <timestamp> <node> <service>[PID]: <level> <type>: <message>

For example:

    2017-08-28T22:43:32.794669+00:00 spine01 netq-notifier[13232]: INFO: filter#default: BGP: leaf01 peerlink-1.4094: session state changed from failed to established

### Supported Integrations</span>

NetQ supports the ability to send notifications to the following
applications:

  - **PagerDuty**: NetQ Notifier sends notifications to PagerDuty as
    PagerDuty events.  
    
    {{% imgOld 1 %}}
    
    {{%notice note%}}
    
    If NetQ generates multiple notifications, on the order of 50/second
    (which could happen when a node reboots or when one peer in an MLAG
    pair disconnects), PagerDuty does not see all these notifications.
    You may see warnings in the `netq-notifier.log` file like this:
    
        2017-09-20T20:39:48.222458+00:00 rdsq1 netq-notifier[1]: WARNING: Notifier: notifier-pagerduty: Request failed with exception: Code: 429, msg: {"status":"throttle exceeded","message":"Requests for this service are arriving too quickly.  Please retry later."}
    
    This is a known limitation in PagerDuty at this time.
    
    {{%/notice%}}

  - **Slack**: NetQ Notifier sends notifications to Slack as incoming
    webhooks for a Slack channel you configure. For example:
    
    {{% imgOld 2 %}}

  - **rsyslog:** Using `rsyslog`, NetQ Notifier sends alerts and events
    to the `/var/log/netq-notifier.log` file by default, but
    notifications can also be sent to ELK/Logstash or Splunk.
    
    {{% imgOld 3 %}}

  - **Splunk**: NetQ integrates with Splunk using `rsyslog`, a standard
    mechanism to capture log files in Linux. Splunk provides plugins to
    handle `rsyslog` inputs.
    
    {{% imgOld 4 %}}

  - **ELK/Logstash**: NetQ integrates with ELK/Logstash using `rsyslog`.
    ELK also provides plugins to handle `rsyslog` inputs.
    
    {{% imgOld 5 %}}

### Configuring an Integration</span>

You need to define to which applications NetQ sends notifications. By
default, NetQ sends notifications only to `syslog`.

To configure PagerDuty or Slack, you need to edit the
`/etc/netq/netq.yml` configuration file.

    cumulus@switch:~$ sudo nano /etc/netq/netq.yml
     
    ...
     
    ## a) Filter notifications to integrations (Slack or PD) based on Severity,
    ## i.e., WARNING to PD, INFO to Slack
    # notifier-integrations:
    # - name: notifier-slack-channel-1
    #   type: slack
    #   webhook: "https://<slack-webhook1"
    #   severity: INFO  <==== Set the severity type here
    #   tag: "<@slack-tag1>"
    # - name: notifier-pagerduty
    #   type: pagerduty
    #   severity: WARNING <==== Set the severity type here
    #   api_access_key: "<API Key>"
    #   api_integration_key: "<API Integration Key>"
    #
     
    ...

{{%notice tip%}}

For Slack notifications, the contents of *tag* is added to the
notification message to be sent, which is useful for setting alerts for
notifications within Slack.

In order to tag users, enclose the username and "@" sign in angled
brackets, like this: *\<@cumulus\>*.

{{%/notice%}}

You need to do some extra steps to be able to export NetQ data to
[ELK](#src-8356545_ProactivelyMonitoringtheNetworkFabric-elk) or
[Splunk](#src-8356545_ProactivelyMonitoringtheNetworkFabric-splunk) (see
below).

After you modify the NetQ configuration, you must restart the
`netq-notifier` service on the telemetry server:

    cumulus@switch:~$ sudo systemctl restart netq-notifier.service

### Filtering Notifications</span>

By default, NetQ sends all notifications in response to network events.
You can filter this according to your needs.

A filter has three components, a *rule*, an *action* and *output*:

  - **Rule**: A set of conditions against which an incoming event is
    matched. If an incoming event matches the rule, the event
    information is passed to the action. The rule is a dictionary of
    key-value pairs, where the "key" is an item associated with the
    event and "value" is the value of that item. For example:  
    rule:  
    hostname: leaf01  
    ifname: swp1  
      
    If the default rule is not specified or if it is empty, a match
    always results. You can make NetQ Notifier continue matching filters
    even if a match is found, by adding *terminate\_on\_match: False* to
    the filter. Values specified in the rule are matched with those
    received in a event using [Python regular
    expressions](https://docs.python.org/2/library/re.html). NetQ also
    matches for message severity and sends a notification only if the
    event is above the given severity. Message severity levels are:
    INFO, WARNING, ERROR and CRITICAL in ascending order.

  - **Action**: The action to perform if the rule matches. The action
    takes the event provided by the rule stage and generates a message
    dictionary with a message and its severity. Multiple actions can be
    prescribed in the action list. An action is typically a Python
    function that is provided with NetQ or you can write a custom one
    yourself. If no action is provided, NetQ defaults to a generic
    handler that looks at the event, and based on that event runs the
    relevant notification function.

  - **Output**: The integrations that will receive the notification. The
    output contains the message and severity. If the output is *None*
    the notification is not sent to any integration, including `syslog`.
    If the output is empty, the message is sent only to `syslog`.
    Otherwise, the notification is sent to the list of integrations
    specified in the output list as well as to `syslog`. If ALL is
    specified, the notification is sent to all integrations.

For example, to send BGP session state notifications to particular Slack
channel, in this case, *slack-channel-BGP*, do the following:

    cumulus@switch:~$ sudo nano /etc/netq/netq.yml
     
    ...
     
    ## e) Send BGP Session state notifications to particular slack channel
    ## (slack-channel-BGP), rest to another one (slack-channel-catchall)
    # notifier-filters:
    # - name: BGP slack channel
    # rule:
    # type: BgpSession
    # output:
    # - slack-channel-BGP
     
     
    ...

To drop notifications, set the output to None for the given rule in the
`/etc/netq/netq.yml` file. For example, you can drop all notifications
from leaf01 by configuring the following:

    cumulus@switch:~$ sudo nano /etc/netq/netq.yml
     
    ...
     
    ## b) Drop all notifications coming from a switch/host say, leaf01
    # notifier-filters:
    # - name: leaf01 drop
    #   rule:
    #     hostname: leaf01
    #   output:
    #     - None
    # - name: default
    #   rule:
    #   output:
    #     - ALL
     
    ...

### Example netq.yml File</span>

<summary>/etc/netq/netq.yml file contents </summary>

    cumulus@switch:~$ cat /etc/netq/netq.yml
    ## Netq configuration File.
    ## Configuration is also read from files in /etc/netq/config.d/ and have
    ## precedence over config in /etc/netq/netq.yml.
    ## ----- Common configurations -----
    ## Backend Configuration for all netq agents and apps on this host.
    ##
    backend:
      server: 10.0.0.165
    #  port: 6379
    ## ----- netq-agent configurations -----
    ## Netq Agent Configuration
    ##
    ## log_level: Could be debug, info, warning or error. Default is info.
    ##
    #netq-agent:
    #  log_level: info
    ## Docker Agent Configuration
    ##
    ## docker_enable: Enable Docker monitoring. Default is True.
    ## docker_poll_period: Docker poll period in secs. Default is 15 secs.
    ##
    #docker:
    #  enable: true
    #  poll_period: 15
    ## ----- netq configurations -----
    ## Netq configuration
    ##
    ## log_level: Could be debug, info, warning or error. Default is info.
    ##
    #netqd:
    #  log_level: info
    ## ----- netq-notifier configurations -----
    ## Netq Notifier Configuration
    ##
    ## log_level: Could be debug, info, warning or error. Default is info.
    ##
    # netq-notifier:
    #  log_level: debug
    ## NetQ Notifier Filter Configuration
    ##
    ## NetQ Notifier sends notifications to integrations(syslog, slack or pagerduty)
    ## based on the events that are happening across the network.
    ## Notifications are generated based on the filters that have been specified in
    ## "notifier-filters".  NetQ Agents generate an event when something interesting
    ## happens on the host (switch or server) its running on. The Notifier is always
    ## listening for these events and once it receives an event, it makes it go
    ## through a set of filters.
    ##
    ## A filter has 3 stages:
    ## a) Rule: Defines a set of conditions against which an incoming event is
    ## matched. Input to this stage is an incoming event and the event is sent to
    ## the next stage if there is a match. If there is a match, the event
    ## information is passed to the action stage. The rule is a dictionary of
    ## key-value pairs, where the "key" is an item associated with the event and
    ## "value" is the value of that item,
    ## e.g. type: Link
    ##      hostname: leaf-01
    ##      ifname: swp1
    ## The Default rule, if none is specified or if it is empty, is to always assume
    ## a match.
    ## Notifier-filter rules are matched sequentially and we stop only when a match
    ## is found. You can make the notifier continue matching filters even if a match
    ## is found, by adding "terminate_on_match: False" to the filter.Values
    ## specified in the rule are matched with those received in a event using python
    ## regular expressions  https://docs.python.org/2/library/re.html
    ## We can also match for message severity and print messages only if it is above
    ## the given severity. Message severity levels are: INFO, WARNING, ERROR and
    ## CRITICAL in ascending order.
    ##
    ## b) Action: action to perform if the "rule" is matched.  The action stage
    ## take the event provided by the "rule" stage and generates a message
    ## dictionary with a message and its severity. Multiple actions can be
    ## prescribed in the "action" list. "action" is typically a python function that
    ## is provided with the tool or a custom one written by the user. If no action
    ## is provided, we default to a generic handler which looks at the event and
    ## based on the event runs the relevant notification function.
    ##
    ## c) output: This stage takes the message dictionary provided by the action
    ## stage and sends the message and severity to the right integration to display
    ## the message. If the output is None the message is not sent to any integration
    ## or syslog. If output is empty, the message is sent only to syslog. Else the
    ## message is sent to the list of integrations specified in the output list and
    ## syslog. If ALL is specified, the message is sent to all integrations.
    ## Integrations are defined in notifier-integrations.
    ##
    ## The config file comes with the following default filter:
    ##
    ## notifier-filters:
    ## - name: default
    ##   rule:
    ##   output:
    ##     - ALL
    ##
    ## which is an empty rule, empty action and output to all. This defaults to
    ## match all rules and then perform the default action which is to run the
    ## generic handler mentioned in the action stage above.
    ##
    ## NetQ Integration Configuration
    ##
    ## The integrations refer to the external tool where you would like to receive
    ## the notification. An integration is added as a list element to
    ## "notifier-integrations". Each integration must have a "name" and "type".
    ## Severity is optional and lets you send messages above that level to the
    ## integration. Allowed values are: INFO, WARNING, ERROR, CRITICAL in increasing
    ## order. Currently allowed "type" are "slack" and "pagerduty". You can define
    ## multiple slack or PD integrations.
    ##
    ##For Slack integration, along with a name and "type: slack", you also need to
    ## also provide the Incoming Webhook of the channel. The webhook URL for your
    ## channel can be found or created in Slack at:
    ##   Apps -> Custom Integrations -> Incoming Webhooks.
    ## Tags are optional and are strings that are attached to the end of th
    ## notification message.
    ## E.g.
    # notifier-integrations:
    # - name: notifier-slack-channel-1
    #   type: slack
    #   webhook: "https://<slack-webhook1>"
    #   severity: INFO,
    #   tag: "@slack-tag1"
    ##
    ## For pagerDuty, along with name and "type: pagerduty", you also need to
    ## provide the "api_access_key" and "api_integration_key" from Pagerduty.
    ## A unique API Access Key which can be created on your PagerDuty website at:
    ## Configuration -> API Access -> Create New API Key
    ## An 'Integration Key' can be created/found on your PagerDuty website at:
    ## Configuration -> Services -> Add New Service -> New Integration ->
    ##   Select Integration Type as 'Use our API directly: Events API v2'.
    ## E.g. pagerduty integration along with slack
    # notifier-integrations:
    # - name: notifier-slack-channel-1
    #   type: slack
    #   webhook: "https://<slack-webhook1>"
    #   severity: INFO
    #   tag: "@slack-tag1"
    # - name: notifier-pagerduty
    #   type: pagerduty
    #   severity: WARNING
    #   api_access_key: <API Key>
    #   api_integration_key: <API Integration Key>
    ##
    ## Customizing Notifications
    ## Here are some examples on how to customize your notifications:
    ##
    ## a) Filter notifications to integrations (Slack or PD) based on Severity,
    ## i.e., WARNING to PD, INFO to Slack
    # notifier-integrations:
    # - name: notifier-slack-channel-1
    #   type: slack
    #   webhook: "https://<slack-webhook1"
    #   severity: INFO  <==== Set the severity type here
    #   tag: "@slack-tag1"
    # - name: notifier-pagerduty
    #   type: pagerduty
    #   severity: WARNING <==== Set the severity type here
    #   api_access_key: "<API Key>"
    #   api_integration_key: "<API Integration Key>"
    #
    ##
    ## b) Drop all notifications coming from a switch/host say, leaf-01
    # notifier-filters:
    # - name: leaf-01 drop
    #   rule:
    #     hostname: leaf-01
    #   output:
    #     - None
    # - name: default
    #   rule:
    #   output:
    #     - ALL
    ##
    ## c) Drop all notifications coming from switches whose name starts with leaf
    # notifier-filters:
    # - name: leaf drop
    #   rule:
    #     hostname: "leaf-.*"
    #   output:
    #     - None
    # - name: default
    #   rule:
    #   output:
    #     - ALL
    ##
    ## d) Drop all notifications coming from a particular link, e.g. leaf-01 swp1
    # notifier-filters:
    # - name: leaf-01 swp1 drop
    #   rule:
    #     type: Link
    #     hostname: leaf-01
    #     ifname: swp1
    #   output:
    #     - None
    # - name: default
    #   rule:
    #   output:
    #    - ALL
    ##
    ## e) Send BGP Session state notifications to particular slack channel
    ## (slack-channel-BGP), rest to another one (slack-channel-catchall)
    # notifier-filters:
    # - name: BGP slack channel
    #   rule:
    #     type: BgpSession
    #   output:
    #     - slack-channel-BGP
    # - name: default
    #   rule:
    #   output:
    #     - slack-channel-catchall
    ##
    ## f) Send BgpSession notifications based on severity to different slack channels
    # notifier-filters:
    # - name: BGP severity slack channel
    #   rule:
    #     type: BgpSession
    #     severity: WARNING
    #   output:
    #     - slack-channel-BGP-info
    # - name: default
    #   rule:
    #   output:
    #     - slack-channel-catchall
    ##
    ## g) Drop all temperature related alerts
    # notifier-filters:
    # - name: temp drop
    #   rule:
    #     type: Temp
    #   output:
    #     - None
    # - name: default
    #   rule:
    #   output:
    #     - ALL
    notifier-filters:
      - name: default
        rule:
        output:
          - ALL

### <span id="src-8356545_ProactivelyMonitoringtheNetworkFabric-elk" class="confluence-anchor-link"></span>Exporting to ELK</span>

To export NetQ Notifier data to ELK via Logstash, on the host running
the NetQ Telemetry Server and NetQ Notifier, configure the notifier to
send the logs to a Logstash instance. In the following example, Logstash
is on a host with the IP address 192.168.50.30, using port 51414:

    # rsyslog - logstash configuration 
    sed -i '/$netq_notifier_log/a if $programname == "netq-notifier" then @@192.168.50.30:51414' /etc/rsyslog.d\
    /50-netq-notifier.conf

Then restart `rsyslog`:

    root@ts_host:~# systemctl restart rsyslog

On the server running Logstash, create a file in `/etc/logstash/conf.d/`
called `notifier_logstash.conf`, and paste in the following text, using
the IP address and port you specified earlier:

    root@ts_host:~# vi /etc/logstash/conf.d/notifier_logstash.conf
     
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

Then restart Logstash:

    root@logstash_host:~# systemctl restart logstash

NetQ Notifier logs now appear in `/tmp/logstash_notifier.log` on the
Logstash host.

### <span id="src-8356545_ProactivelyMonitoringtheNetworkFabric-splunk" class="confluence-anchor-link"></span>Exporting to Splunk</span>

To export NetQ Notifier data to Splunk, on the host running the NetQ
Telemetry Server and NetQ Notifier, configure the notifier to send the
logs to Splunk. In the following example, Splunk is on a host with the
IP address 192.168.50.30, using port 51414:

    # rsyslog - splunk configuration 
    sed -i '/$netq_notifier_log/a if $programname == "netq-notifier " then @@192.168.50.30:51415' /etc/rsyslog.d\
    /50-netq-notifier.conf

Then restart `rsyslog`:

    root@ts_host:~# systemctl restart rsyslog

To configure Splunk, do the following:

1.  In Splunk in a browser, choose **Add Data** \> **monitor** \>
    **TCP** \> **Port**, and set it to *51415*.

2.  Click **Next**, then choose **Source Type (syslog)** \> **Review**
    \> **Done**.

NetQ Notifier messages now appear in Splunk.

### Precisely Locating an Issue on the Network</span>

NetQ helps you locate exactly where you have an issue on your network.
Use `netq check` or `netq trace` to locate a fault, then run `netq show
changes` to see what could have caused it.

For example, checking the state of the VLANs on your network, you can
see where some nodes have mismatched VLANs with their peers:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><code>cumulus@leaf01:~$ netq check vlan </code><br />
<code>Checked Nodes: 25, Checked Links: 775, Failed Nodes: 3, Failed Links: 6 Vlan and/or PVID mismatch found on following links </code><br />
<code>Hostname Interface Vlans Peer Peer Interface Peer Vlans Error</code><br />
<code>-------- ----------- ----------------- ------- ---------------- ----------------- -----------------</code><br />
<code>server01 torbond1 103-106,1000-1005 leaf02 hostbond2 101-106,1000-1005 VLAN set Mismatch</code><br />
<code>server01 torbond1 103-106,1000-1005 leaf01 hostbond2 101-106,1000-1005 VLAN set Mismatch</code><br />
<code>server02 torbond1 102-106,1000-1005 leaf02 hostbond3 101-106,1000-1005 VLAN set Mismatch</code><br />
<code>server02 torbond1 102-106,1000-1005 leaf01 hostbond3 101-106,1000-1005 VLAN set Mismatch</code><br />
<code>server03 torbond1 102-106,1000-1005 leaf04 hostbond2 101-106,1000-1005 VLAN set Mismatch</code><br />
<code>server03 torbond1 102-106,1000-1005 leaf03 hostbond2 101-106,1000-1005 VLAN set Mismatch</code></p></td>
</tr>
</tbody>
</table>

### <span id="src-8356545_ProactivelyMonitoringtheNetworkFabric-ntp" class="confluence-anchor-link"></span>Detecting Out of Sync Nodes</span>

NetQ includes commands to assist in determining if any nodes are out of
sync. Use `netq check ntp` to determine if any nodes are out of sync,
and `netq show services ntp` and `netq show ntp` to review the records:

    cumulus@switch:~$ netq check ntp
    Total Nodes: 18, Checked Nodes: 18, Rotten Nodes: 7, Unknown Nodes: 0, failed NTP Nodes: 8
    Hostname        NTP Sync    Connect Time
    --------------  ----------  -------------------
    act-5712-12     Rotten      2017-09-01 09:15:30
    act-6712-06     Rotten      2017-09-01 09:16:02
    act-7712-04     Rotten      2017-09-01 09:16:05
    cel-smallxp-13  no          2017-08-26 01:15:00
    dell-s4000-10   Rotten      2017-09-01 09:14:53
    dell-s6000-22   Rotten      2017-09-01 09:15:29
    mlx-2410-02     Rotten      2017-09-01 09:16:23
    qct-ly8-04      Rotten      2017-09-01 09:14:56

    cumulus@switch:~$ netq show services ntp
    Matching services records are:
    Node             Service      PID  VRF      Enabled    Active    Monitored    Status    Up Time    Last Changed
    ---------------  ---------  -----  -------  ---------  --------  -----------  --------  ---------  --------------
    leaf01           ntp          913  default  yes        yes       no           ok        2h ago     2h ago
    leaf02           ntp          911  default  yes        yes       no           ok        2h ago     2h ago
    leaf03           ntp          909  default  yes        yes       no           ok        2h ago     2h ago
    leaf04           ntp          910  default  yes        yes       no           ok        2h ago     2h ago
    oob-mgmt-server  ntp          729  default  yes        yes       no           ok        2h ago     2h ago
    spine01          ntp          909  default  yes        yes       no           ok        2h ago     2h ago
    spine02          ntp          909  default  yes        yes       no           ok        2h ago     2h ago

    cumulus@switch:~$ netq show ntp
    Hostname        NTP Sync    Current Server    Stratum
    --------------  ----------  ----------------  ---------
    act-5712-12     -           -                 -
    act-6712-06     -           -                 -
    act-7712-04     -           -                 -
    cel-bs01-fc1    yes         chimera.buffero   2
    cel-bs01-fc2    yes         104.156.99.226    2
    cel-bs01-fc4    yes         104.156.99.226    2
    cel-bs01-lc101  yes         chimera.buffero   2
    cel-bs01-lc102  yes         secure.visionne   2
    cel-bs01-lc201  yes         chimera.buffero   2
    cel-bs01-lc202  yes         secure.visionne   2
    cel-bs01-lc301  yes         chimera.buffero   2
    cel-bs01-lc401  yes         104.156.99.226    2
    cel-bs01-lc402  yes         chimera.buffero   2
    cel-smallxp-13  no          -                 16
    dell-s4000-10   -           -                 -
    dell-s6000-22   -           -                 -
    mlx-2410-02     -           -                 -
    qct-ly8-04      -           -                 -
    {code}

{{%notice warning%}}

These commands require `systemd` in order to run correctly.

{{%/notice%}}

## Extending NetQ with Custom Services Using curl</span>

You can extend NetQ to monitor parameters beyond what it monitors by
default. For example, you can create a service that runs a series of
pings to a known host or between two known hosts to ensure that
connectivity is valid. Or you can create a service that curls a URL and
sends the output to `/dev/null`. This method works with the [NetQ time machine](/cumulus-netq-121/Proactively-Monitoring-the-Network-Fabric/)
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

## Exporting NetQ Data</span>

Data from the NetQ Telemetry Server can be exported in a number of ways.
First, you can use the `json` option to output check and show commands
to JSON format for parsing in other applications.

For example, you can check the state of BGP on your network with `netq
check bgp`:

    cumulus@leaf01:~$ netq check bgp 
    Total Nodes: 25, Failed Nodes: 2, Total Sessions: 228 , Failed Sessions: 2,
    Node       Peer Name  Peer Hostname Reason       Time 
    ---------- ---------- ------------- ------------ ------- 
    exit01     swp6.2     spine01       Rotten Agent 15h ago 
    spine01    swp3.2     exit01        Idle         15h ago

When you show the output in JSON format, this same command looks like
this:

    cumulus@leaf01:~$ netq check bgp json 
    {
        "failedNodes": [
            {
                "node": "exit-1", 
                "reason": "Idle", 
                "peerId": "firewall-1", 
                "neighbor": "swp6.2", 
                "time": "15h ago"
            }, 
            {
                "node": "firewall-1", 
                "reason": "Idle", 
                "peerId": "exit-1", 
                "neighbor": "swp3.2", 
                "time": "15h ago"
            }
        ], 
        "summary": {
            "checkedNodeCount": 25, 
            "failedSessionCount": 2, 
            "failedNodeCount": 2, 
            "totalSessionCount": 228
        }
    }


</details>
