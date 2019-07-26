---
title: Deployment Appendices
author: Cumulus Networks
weight: 95
aliases:
 - /display/NETQ141/Deployment+Appendices
 - /pages/viewpage.action?pageId=10453427
pageID: 10453427
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
<details>

This topic contains additional reference material that may be useful
when deploying the Cumulus NetQ software.

## <span id="src-10453427_DeploymentAppendices-example" class="confluence-anchor-link"></span>Example NetQ Switch Configuration File</span>

The following sample `netq.yml` file is located in /etc/netq/ on the
NetQ Telemetry Server. Note that `netq.yml` looks different on a switch
or host monitored by NetQ; for example, the backend server IP address
and port would be uncommented and listed .

{{%notice note%}}

Editing `/etc/netq/config.d` to configure NetQ Notifier or putting other
YML files in the `/etc/netq` directory overrides the configuration in
`/etc/netq/netq.yml`.

{{%/notice%}}

<summary>Example /etc/netq/netq.yml configuration file </summary>

    cumulus@netq-appliance:~$ cat /etc/netq/netq.yml 
    ## Netq configuration File.
    ## Configuration is also read from files in /etc/netq/config.d/ and have
    ## precedence over config in /etc/netq/netq.yml.
     
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
    ## Tags are optional and are strings that are attached to the end of the
    ## notification message.
    ## E.g.
    # notifier-integrations:
    # - name: notifier-slack-channel-1
    #   type: slack
    #   webhook: "https://<slack-webhook1>"
    #   severity: INFO
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

## <span id="src-10453427_DeploymentAppendices-PlaybkInstallNetq" class="confluence-anchor-link"></span>Example Ansible Playbook to Install NetQ on All Cumulus Switches</span>

The following example installs NetQ on all of your Cumulus switches,
including:

  - Setting the Management IP address

  - Verifying a sufficient Cumulus Linux release is installed

  - Applying the latest NetQ software package from the Cumulus
    repository

  - Setting the NetQ Agent to communicate over the management VRF

  - Restarting `rsyslog`

  - Restarting the NetQ Agent

This performs all of the required installation and configuration to get
NetQ installed and running. It assumes a management VRF and NTP has been
previously setup. You would need to expand this playbook to install
optional capabilities.

{{%notice info%}}

To run the playbook in your environment, you must replace the
`netq_server` IP address with your Telemetry Server IP address.

{{%/notice%}}

    - hosts: all
      gather_facts: false
      become: true
      remote_user: cumulus
      vars:
        netq_server: "192.168.0.254"
      tasks:
        - name: Collect CL Version
          shell: grep DISTRIB_RELEASE /etc/lsb-release | cut -d "=" -f2
          register: cl_version
          changed_when: false
     
        - name: Assert Cumulus Version Supports NetQ
          assert:
          that: "{{cl_version.stdout | version_compare('3.3.2', '>=') }}"
          msg: "Cumulus Linux version must be 3.3.2 or later to support NetQ. Version {{cl_version.stdout}} detected."
     
        - name: Add Cumulus Repo
          apt_repository:
            repo: deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-latest
            state: present
            update_cache: true
          tags:
            - netq_setup
     
        - name: Install NetQ (from Repo)
          apt:
            name: cumulus-netq
            update_cache: false
          tags:
            - netq_setup
     
        - name: Add netq server IP (VRF)
          command: netq config add server {{ netq_server }} vrf mgmt
          tags:
            - netq_setup
     
        - name: Restart Rsyslog
          service:
            name: rsyslog
            state: restarted
          tags:
            - netq_setup
     
        - name: Restart NetQ Agent
          command: netq config restart agent
          tags:
            - netq_setup

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
