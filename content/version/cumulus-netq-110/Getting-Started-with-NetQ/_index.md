---
title: Getting Started with NetQ
author: Cumulus Networks
weight: 11
aliases:
 - /display/NETQ110/Getting-Started-with-NetQ
 - /pages/viewpage.action?pageId=7111298
pageID: 7111298
product: Cumulus NetQ
version: 1.1.0
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
---
NetQ is comprised of two main install components: the NetQ Telemetry
Server, and the `cumulus-netq` metapackage which gets installed on
Cumulus Linux switches. Additionally, for host network visibility and
containers, you can install host OS-specific metapackages.

This section walks through the basic install and setup steps for
installing and running NetQ on the following supported operating
systems:

  - Cumulus Linux

  - Ubuntu 16.04

  - Red Hat Enterprise Linux 7

  - CentOS 7

{{%notice tip%}}

Before you get started, you should review the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115012060387)
for this version.

{{%/notice%}}

## <span>Install the NetQ Telemetry Server</span>

The NetQ Telemetry Server comprises a set of individual Docker
containers that each contain a separate service for the `redis`
database, the Service Console, the NetQ CLI and NetQ Notifier. It is
available in one of two formats:

  - VMware ESXi 6.5 virtual machine

  - A QCOW/KVM image for use on Ubuntu 16.04 and Red Hat Enterprise
    Linux 7 hosts

{{%notice note%}}

Cumulus Networks recommends the telemetry server is installed on an
out-of-band management network to ensure it can monitor in-band network
issues without being affected itself. Ideally, you should run the
telemetry server on a separate, powerful server for maximum usability
and performance. For more information on system requirements, refer to
the [How Far Back in Time Can You
Travel](Performing-Network-Diagnostics.html#src-7111314_PerformingNetworkDiagnostics-matrix)
section.

{{%/notice%}}

{{%notice note%}}

The NetQ telemetry server containers are completely separate from any
containers you may have on the hosts you are monitoring with NetQ. The
NetQ containers will not overwrite the host containers and vice versa.

{{%/notice%}}

1.  Download the NetQ Telemetry Server virtual machine. On the
    [Downloads](https://cumulusnetworks.com/downloads/) page, select
    *NetQ* from the **Product** menu, then click **Download** for the
    appropriate hypervisor — KVM or VMware.

2.  Import the virtual machine into your
    [KVM](https://docs.cumulusnetworks.com/display/VX/Libvirt+and+KVM+QEMU+Installation+on+Ubuntu+16.04)
    or
    [VMware](https://docs.cumulusnetworks.com/display/VX/VMware+vSphere+-+ESXi+5.5)
    hypervisor.

3.  Start the NetQ Telemetry Server. There are two default user accounts
    you can use to log in:
    
      - The primary username is *admin*, and the default password is
        *CumulusNetQ\!*.
    
      - The alternate username is *cumulus*, and its password is
        *CumulusLinux\!*.

Once the NetQ Telemetry Server is installed, you need to configure NetQ
Notifier.

In addition, if you intend to use NetQ with applications like PagerDuty
or Slack, you need to configure those applications to receive
notifications from NetQ Notifier.

{{%notice tip%}}

Note the external IP address of the host where the telemetry server is
running, as you need this to correctly configure the NetQ Agent on every
node you want to monitor. The telemetry server gets its IP address from
DHCP; to get the IP address, run `ifconfig eth0` on the telemetry
server.

{{%/notice%}}

## <span id="src-7111298_GettingStartedwithNetQ-agent" class="confluence-anchor-link"></span><span>Install the NetQ Agent</span>

In order to manage a node with NetQ Agent and send notifications with
NetQ Notifier, you need to install an OS-specific metapackage on each
node. The node can be a:

  - Cumulus Linux switch running version 3.3.0 or later

  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7

  - Linux virtual machine running one of the above Linux operating
    systems

The metapackage contains the NetQ Agent and the NetQ command line
interface.

Install the metapackage on each node to monitor, then configure the NetQ
Agent on the node.

### <span>Installing on a Cumulus Linux Switch</span>

1.  Edit `/etc/apt/sources.list` and add the following line:
    
        cumulus@switch:~$ sudo nano /etc/apt/sources.list
        deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-latest

2.  Update the local `apt` repository, then install the metapackage on
    the switch:
    
        cumulus@switch:~$ sudo apt-get update && sudo apt-get install cumulus-netq

### <span>Installing on an Ubuntu, Red Hat or CentOS Server</span>

To install NetQ on Linux servers running Ubuntu, Red Hat or CentOS,
please read the [Host Pack
documentation](https://docs.cumulusnetworks.com/display/HOSTPACK/Installing+NetQ+on+the+Host).

## <span id="src-7111298_GettingStartedwithNetQ-nodeconfig" class="confluence-anchor-link"></span><span>Configuring the NetQ Agent on a Node</span>

Once you install the NetQ packages and configure the NetQ Telemetry
Server, you need to configure NetQ on each Cumulus Linux switch to
monitor that node on your network.

1.  To ensure useful output, ensure that
    [NTP](https://docs.cumulusnetworks.com/display/CL31/Setting+Date+and+Time)
    is running.

2.  On the host, after you install the NetQ metapackage, restart
    `rsyslog` so logs are sent to the correct destination:
    
        cumulus@switch:~$ sudo systemctl restart rsyslog

3.  Link the host to the telemetry server you configured above; in the
    following example, the IP address for the telemetry server host is
    *198.51.100.10*:
    
        cumulus@switch:~$ netq config add server 198.51.100.10
    
    This command updated the configuration in the
    `/etc/cts/netq/netq.yml` file. It also enables the NetQ CLI.

4.  Restart the `netq` services.
    
        cumulus@switch:~$ netq config agent restart
    
    {{%notice note%}}
    
    If you see the following error, it means you haven't added the
    telemetry server or the server wasn't configured:
    
        cumulus@switch:~$ netq config agent start
        Error: Please specify IP address of DB server
    
    {{%/notice%}}

### <span id="src-7111298_GettingStartedwithNetQ-vrf" class="confluence-anchor-link"></span><span>Configuring the Agent to Use a VRF</span>

If you want the NetQ Agent to communicate with the telemetry server only
via a [VRF](/display/NETQ110/Virtual+Routing+and+Forwarding+-+VRF),
including a [management VRF](/display/NETQ110/Management+VRF), you need
to specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the telemetry server over it, configure the agent like this:

    cumulus@switch:~$ netq config add server 198.51.100.10 vrf mgmt

Then you need to stop and disable the `netqd` service, then enable and
start the service in the VRF:

    cumulus@switch:~$ sudo systemctl stop netqd.service
    cumulus@switch:~$ sudo systemctl disable netqd.service
    cumulus@switch:~$ sudo systemctl enable netqd@mgmt.service
    cumulus@switch:~$ sudo systemctl start netqd@mgmt.service

### <span id="src-7111298_GettingStartedwithNetQ-port" class="confluence-anchor-link"></span><span>Configuring the Agent to Communicate over a Specific Port</span>

By default, NetQ uses port 6379 for communication between the telemetry
server and NetQ Agents. If you want the NetQ Agent to communicate with
the telemetry server via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq config add server 198.51.100.10 port 7379

## <span id="src-7111298_GettingStartedwithNetQ-notifier" class="confluence-anchor-link"></span><span>Configuring NetQ Notifier on the Telemetry Server</span>

NetQ Notifier listens to events from the telemetry server database. When
NetQ Notifier is running on the NetQ Telemetry Server, it sends out
alerts. NetQ Notifier runs on the NetQ Telemetry Server only; the NetQ
Agents on the nodes only communicate with it.

You need to configure two things for NetQ Notifier:

  - The events for which you want to receive notifications/alerts, like
    sensors or BGP session notifications.

  - The integrations for where to send those notifications; by default,
    they are `rsyslog`, PagerDuty and Slack.

NetQ Notifier sends out alerts based on the configured log level, which
is one of the following:

  - debug: Used for debugging-related messages.

  - info: Used for informational, high-volume messages.

  - warning: Used for warning conditions.

  - error: Used for error conditions.

The default log level setting is *info*, so NetQ Notifier sends out
alerts for info, warning and error conditions.

By default, all notifications/alerts are enabled, and logged in
`/var/log/netq-notifier.log`. You only need to edit the notifications if
there is something you don't want to monitor.

NetQ Notifier is already integrated with `rsyslog`. To integrate with
PagerDuty or Slack, you need to specify some parameters.

To configure alerts and integrations on the NetQ Telemetry Server:

1.  Stop and disable the following services on the telemetry server, as
    they are not necessary (and you will enable the `netq-notifier`
    service in a later step):
    
        cumulus@ts:~$ sudo systemctl stop cts-notifier-watch.timer cts-notifier-watch cts-notifier
        cumulus@ts:~$ sudo systemctl disable cts-notifier-watch.timer cts-notifier-watch cts-notifier

2.  As the sudo user, open `/etc/cts/netq/netq.yml` in a text editor.

3.  Configure the following in the `/etc/cts/netq/netq.yml` file:
    
      - Change the log level: If you want a more restrictive level than
        info.
    
      - Configure application notifications: To customize any
        notifications, uncomment the relevant section under
        **netq-notifier Configurations** and make changes accordingly.
    
      - Configure PagerDuty and Slack integrations. You can see where to
        input the information for these integrations in the [example
        `netq.yml` file](#src-7111298_GettingStartedwithNetQ-example)
        below.
        
          - For PagerDuty, enter the API access key (also called the
            [authorization
            token](https://v2.developer.pagerduty.com/docs/authentication))
            and the
            [integration](https://v2.developer.pagerduty.com/docs/events-api-v2)
            key (also called the service\_key or routing\_key).
        
          - For Slack, enter the webhook URL. To get the webhook URL, in
            the Slack dropdown menu, click **Apps & integrations**, then
            click **Manage** \> **Custom Integrations** \> **Incoming
            WebHooks** \> select **Add Configuration** \> select the
            channel to receive the notifications such as
            *\#netq-notifier* in the **Post to Channel** dropdown \>
            then click **Add Incoming WebHook integration**. The URL
            produced by Slack looks similar to the one pictured below:
            
            {{% imgOld 0 %}}
            
            Copy the URL from the **Webhook URL** field into the
            `/etc/cts/netq/netq.yml` file under the **Slack
            Notifications** section. Uncomment the lines in the sections
            labeled *netq-notifier*, *notifier-integrations* and
            *notifier-filters*, then add the webhook URL value provided
            by Slack:
            
                netq-notifier:
                  log_level: info
                 
                ...
                 
                notifier-integrations:
                  - name: notifier-slack-channel-1
                    type: slack
                    webhook: "https://hooks.slack.com/services/sometext/moretext/evenmoretext"
                    severity: INFO,
                    tag: "@netqts-sys"
                 
                ...
                 
                notifier-filters:
                  - name: default
                    rule:
                    output:
                      - ALL
    
    When you are finished editing the file, save and close it.

4.  Stop then start the NetQ Notifier daemon to apply the new
    configuration:
    
        cumulus@netq-appliance:~$ docker-compose  -p "netq" -f "${CFG_DIR}/docker/netq-base-compose.yml" stop netq-notifier
        cumulus@netq-appliance:~$ docker-compose  -p "netq" -f "${CFG_DIR}/docker/netq-base-compose.yml" start netq-notifier
    
    {{%notice note%}}
    
    If your webhook does not immediately send a message to your channel,
    look for errors in syntax. Check the log file located at
    `/var/log/docker/cts-netq-notifier.log`.
    
    {{%/notice%}}

## <span id="src-7111298_GettingStartedwithNetQ-example" class="confluence-anchor-link"></span><span>Example /etc/cts/netq/netq.yml Configuration</span>

In the following sample `/etc/cts/netq/netq.yml` file on the NetQ
Telemetry Server itself. Note that the `netq.yml` looks different on a
NetQ switch or host (for example, the backend server IP address and port
would be uncommented and listed).

    cumulus@netq-appliance:~$ cat /etc/cts/netq/netq.yml 
    ## Netq configuration File.
    ## Configuration is also read from files in /etc/netq/config.d/ and have
    ## precedence over config in /etc/cts/netq/netq.yml.
     
    ## ----- Common configurations -----
     
    ## Backend Configuration for all netq agents and apps on this host.
    ##
    #backend:
    #  server: 
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
     
    ## Netq Notifier configuration
    ##
    ## log_level: Could be debug, info, warning or error. Default is info.
    ##
    #netq-notifier:
    #  log_level: info
    ## Slack Notifications
    ##
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

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
