---
title: Getting Started with NetQ
author: Cumulus Networks
weight: 11
aliases:
 - /display/NETQ10/Getting-Started-with-NetQ
 - /pages/viewpage.action?pageId=6488202
pageID: 6488202
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
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
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115008149727)
for this version.

{{%/notice%}}

## <span>Install the NetQ Telemetry Server</span>

The NetQ Telemetry Server is a VMware ESXi 6.5 virtual machine,
comprising a set of individual Docker containers that each contain a
separate service for the ` redis  `database, the Service Console, the
NetQ CLI and NetQ Notifier.

{{%notice note%}}

Cumulus Networks recommends the telemetry server is installed on an
out-of-band management network to ensure it can monitor in-band network
issues without being affected itself. Ideally, you should run the
telemetry server on a separate, powerful server for maximum usability
and performance. For more information on system requirements, refer to
the [How Far Back in Time Can You
Travel](Performing-Network-Diagnostics.html#src-6488212_PerformingNetworkDiagnostics-matrix)
section.

{{%/notice%}}

{{%notice note%}}

The NetQ telemetry server containers are completely separate from any
containers you may have on the hosts you are monitoring with NetQ. The
NetQ containers will not overwrite the host containers and vice versa.

{{%/notice%}}

1.  Download the NetQ Telemetry Server VMware virtual machine. Select
    *NetQ* from the **Product** menu on the
    [Downloads](https://cumulusnetworks.com/downloads/) page.

2.  [Import the virtual machine](/cumulus-vx/Getting-Started/VMware-vSphere-ESXi-5.5/)
    into your hypervisor.

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

## <span>Install the NetQ Agent</span>

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

  - Update the local `apt` repository, then install the metapackage on
    the switch:

        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install cumulus-netq

### <span>Installing on an Ubuntu Server</span>

  - Reference and update the local `apt` repository, then install the
    metapackage on the server:

        root@ubuntu:~# wget -O- https://hostapps3.cumulusnetworks.com/setup/cumulus-host-ubuntu.pubkey | apt-key add -
        root@ubuntu:~# wget -O- https://hostapps3.cumulusnetworks.com/setup/cumulus-host-ubuntu-xenial.list > /etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list
        root@ubuntu:~# apt-get update ; apt-get install cumulus-netq

### <span>Installing on a Red Hat or CentOS Server</span>

  - Reference and update the local `yum` repository, then install the
    metapackage on the server:

        root@rhel7:~# rpm --import https://hostapps3.cumulusnetworks.com/setup/cumulus-host-el.pubkey
        root@rhel7:~# wget -O- https://hostapps3.cumulusnetworks.com/setup/cumulus-host-el.repo > /etc/yum.repos.d/cumulus-host-el.repo
        root@rhel7:~# yum install cumulus-netq

## <span id="src-6488202_GettingStartedwithNetQ-nodeconfig" class="confluence-anchor-link"></span><span>Configuring the NetQ Agent on a Node</span>

Once you install the NetQ packages and configure the NetQ Telemetry
Server, you need to configure NetQ on each node (Cumulus Linux switch or
Linux host) to monitor that node on your network.

1.  To ensure useful output, ensure that
    [NTP](/cumulus-linux/System-Configuration/Setting-Date-and-Time/)
    is running.

2.  On the host, after you install the NetQ metapackage, restart
    `rsyslog` so logs are sent to the correct destination:

        cumulus@switch:~$ sudo systemctl restart rsyslog

3.  **CentOS, RHEL or Ubuntu hosts only:** Enable and restart the
    `netqd` service:

        cumulus@server01:~$ sudo systemctl enable netqd ; sudo systemctl start netqd

4.  Link the host to the telemetry server you configured above; in the
    following example, the IP address for the telemetry server host is
    *198.51.100.10*:

        cumulus@switch:~$ netq add server 198.51.100.10

    This command updated the configuration in the `/etc/netq/netq.yml`
    file. It also enables the NetQ CLI.

5.  **Container hosts only:** Enable Docker by adding the following
    three lines to the `netq.yml` file on the container host:

        cumulus@server01:~$ sudo vi /etc/netq/netq.yml
         
        ...
         
        docker:
          enable: true
          poll_period: 15

6.  Restart the `netq` services.

        cumulus@switch:~$ netq agent restart

    {{%notice note%}}

    If you see the following error, it means you haven't added the
    telemetry server or the server wasn't configured:

        cumulus@switch:~$ netq agent start
        Error: Please specify IP address of DB server

    {{%/notice%}}

### <span id="src-6488202_GettingStartedwithNetQ-vrf" class="confluence-anchor-link"></span><span>Configuring the Agent to Use a VRF</span>

If you want the NetQ Agent to communicate with the telemetry server only
via a VRF, including a management VRF, you need to specify the VRF name
when configuring the NetQ Agent. For example, if the management VRF is
configured and you want the agent to communicate with the telemetry
server over it, configure the agent like this:

    cumulus@switch:~$ netq add server 198.51.100.10 vrf mgmt

### <span id="src-6488202_GettingStartedwithNetQ-port" class="confluence-anchor-link"></span><span>Configuring the Agent to Communicate over a Specific Port</span>

By default, NetQ uses port 6379 for communication between the telemetry
server and NetQ Agents. If you want the NetQ Agent to communicate with
the telemetry server via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq add server 198.51.100.10 port 7379

## <span>Configuring NetQ Notifier on the Telemetry Server</span>

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
`/var/log/docker/netq/notifier_1/netq-notifier.log`. You only need to
edit the notifications if there is something you don't want to monitor.

NetQ Notifier is already integrated with `rsyslog`. To integrate with
PagerDuty or Slack, you need to specify some parameters.

To configure alerts and integrations on the NetQ Telemetry Server:

1.  As the sudo user, open `/appliance/cfg/netq/netq.yml` in a text
    editor.

2.  Configure the following in the `/appliance/cfg/netq/netq.yml` file:

      - Change the log level: If you want a more restrictive level than
        info.

      - Configure application notifications: To customize any
        notifications, uncomment the relevant section under
        **netq-notifier Configurations** and make changes accordingly.

      - Configure PagerDuty and Slack integrations. You can see where to
        input the information for these integrations in the [example
        `netq.yml` file](#src-6488202_GettingStartedwithNetQ-example)
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
            then click **Add Incoming WebHook integration** the URL
            produced by Slack will look something like the one pictured
            below:  

            {{% imgOld 0 %}}


            Copy the URL from the Webhook URL field into the
            `/appliance/cfg/netq/netq.yml` file under the **Slack
            Notifications** section. Uncomment the Slack, enable, and
            webhook lines while adding the webhook URL value provided by
            Slack.

                ## Slack Notifications
                ##
                ## netq-notifier sends notifications to Slack using Incoming Webhooks.
                ## The webhook for your channel can be found or created on Slack at:
                ## Apps -> Custom Integrations -> Incoming Webhooks.
                ## Each webhook has a 'Webhook URL'. Please specify that for webhook.
                ##
                ## enable: true or false
                ## webhook:
                ##
                slack:
                  enable: true
                  webhook: https://hooks.slack.com/services/sometext/moretext/evenmoretext

    When you are finished editing the file, save and close it.

3.  Stop then start the NetQ Notifier daemon to apply the new
    configuration:

        cumulus@netq-appliance:~$ docker exec -it netq_netq-notifier_1 systemctl stop netq-notifier
        cumulus@netq-appliance:~$ docker exec -it netq_netq-notifier_1 systemctl start netq-notifier

## <span id="src-6488202_GettingStartedwithNetQ-example" class="confluence-anchor-link"></span><span>Example /etc/netq/netq.yml Configuration</span>

In the following sample `/etc/netq/netq.yml` file, notice that the NetQ
Telemetry Server is on a server with the IP address 198.51.100.10.

    cumulus@netq-appliance:~$ cat /etc/netq/netq.yml
    ## Netq configuration File.
    ## Configuration is also read from files in /etc/netq/config.d/ and have
    ## precedence over config in /etc/netq/netq.yml.
    ## ----- Common configurations -----
    ## Backend Configuration for all netq agents and apps on this host.
    ##
    backend:
      server: 198.51.100.10
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
    ## ----- netq-notifier Configurations -----
    ## Netq Notifier configuration
    ##
    ## log_level: Could be debug, info, warning or error. Default is info.
    ##
    #netq-notifier:
    #  log_level: info
    ## Slack Notifications
    ##
    ## netq-notifier sends notifications to Slack using Incoming Webhooks.
    ## The webhook for your channel can be found or created on Slack at:
    ## Apps -> Custom Integrations -> Incoming Webhooks.
    ## Each webhook has a 'Webhook URL'. Please specify that for webhook.
    ##
    ## enable: true or false
    ## webhook: <webhook link>
    ##
    #slack:
    #  enable: true
    #  webhook: https://cumulusnetworks.slack.com/example/hook
    ## PagerDuty Notifications
    ##
    ## netq-notifier sends notifications to PagerDuty using the Events API v2.
    ## To access the PagerDuty, we need a unique API Access Key which can be created
    ## on your PagerDuty website at:
    ## Configuration -> API Access -> Create New API Key
    ## The Netq PagerDuty Integration needs to be identified by an 'Integration Key'
    ## that can be created/found on your PagerDuty website at:
    ## Configuration -> Services -> Add New Service -> New Integration ->
    ## Select Integration Type as 'Use our API directly: Events API v2'
    ##
    #pagerduty:
    #  enable: false
    #  api_access_key:
    #  api_integration_key:
    ## Agent State Notifications
    ##
    ## Notify when the agent goes Rotten or Fresh.
    ##
    ## enable: true or false
    ## include: list of node names to monitor. E.g. [cumulus-sw1, cumulus-sw2]
    ## exclude: list of node names to ignore. E.g. [cumulus-sw1, cumulus-sw2]
    ##          If 'include' is specified, this field is ignored.
    #agents:
    #  enable: true
    #  exclude: []
    #  include: [leaf01, leaf02, spine01, spine02]
    ## BGP Session Notifications
    ##
    ## Notify when BGP sessions go up or down
    ## enable: true or false
    ## include: list of node names or "nodename neighbor" to monitor
    ## exclude: list of node names or "nodename neighbor" to ignore.
    ##          E.g. [cumulus-sw1, cumulus-sw2 peerlink-3]
    ##          If 'include' is specified, this field is ignored.
    #bgp:
    #  enable: true
    #  exclude: []
    #  include: []
    ## OSPF Session Notifications
    ##
    ## Notify when OSPF sessions go up or down
    ## enable: true or false
    ## include: list of node names or "nodename neighbor" to monitor.
    ##            E.g. [cumulus-sw1, cumulus-sw2 peerlink-3]
    ## exclude: list of node names or "nodename neighbor" to ignore.
    ##          E.g. [cumulus-sw1, cumulus-sw2 peerlink-3]
    ##          If 'include' is specified, this field is ignored.
    #ospf:
    #  enable: true
    #  exclude: []
    #  include: [leaf01, leaf02, spine01, spine02]
    ## CLAG Node Notifications
    ##
    ## Notify when clag goes up or down.
    ## enable: true or false
    ## include: list of node names to monitor. E.g. [cumulus-sw1, cumulus-sw2]
    ## exclude: list of node names to ignore. E.g. [cumulus-sw1, cumulus-sw2]
    ##          If 'include' is specified, this field is ignored.
    #clag:
    #  enable: true
    #  exclude: []
    #  include: []
    ## Sensor Notifications
    ##
    ## Notify when sensors change state
    ## enable: true or false
    ## include: list of node names or "nodename sensor" to monitor
    ## exclude: list of node names or "nodename sensor" to ignore.
    ##          E.g. [cumulus-sw1, cumulus-sw2 temp1]
    ##          If 'include' is specified, this field is ignored.
    #sensors:
    #  enable: true
    #  exclude: []
    #  include: [leaf01, leaf02]
    ## Link Notifications
    ##
    ## Notify when links go up or down
    ## enable: true or false
    ## include: list of node names or "nodename interface" to monitor
    ## exclude: list of node names or "nodename interface" to ignore.
    ##          E.g. [cumulus-sw1, cumulus-sw2 swp1]
    ##          If 'include' is specified, this field is ignored.
    #link:
    #  enable: true
    #  exclude: []
    #  include: [leaf01, leaf02, spine01, spine02]
    ## VLAN notifications
    ##
    ## Notify when VLAN mismatch has occurred
    ## enable: true or false
    ## include: list of node names or "nodename interface" to monitor
    ## exclude: list of node names or "nodename interface" to ignore.
    ##          E.g. [cumulus-sw1, cumulus-sw2 swp1]
    ##          If 'include' is specified, this field is ignored.
    #vlan:
    #  enable: true
    #  exclude: []
    #  include: []
    ## License Notifications
    ##
    ## Notify when Cumulus Linux license is valid or not
    ## enable: true or false
    ## include: list of node names to monitor. E.g. [cumulus-sw1, cumulus-sw2]
    ## exclude: list of node names to ignore. E.g. [cumulus-sw1, cumulus-sw2]
    ##          If 'include' is specified, this field is ignored.
    #license:
    #  enable: true
    #  exclude: []
    #  include: []
    ## MTU notifications
    ##
    ## Notify when MTU mismatch has occurred
    ## enable: true or false
    ## include: list of node names or "nodename interface" to monitor
    ## exclude: list of node names or "nodename interface" to ignore.
    ##          E.g. [cumulus-sw1, cumulus-sw2 swp1]
    ##          If 'include' is specified, this field is ignored.
    #mtu:
    #  enable: true
    #  exclude: []
    #  include: []
    ## LNV notifications
    ##
    ## Notify when LNV error has occurred
    ## enable: true or false
    ## include: list of node names or "nodename interface" to monitor
    ## exclude: list of node names or "nodename interface" to ignore.
    ##          E.g. [cumulus-sw1, cumulus-sw2 swp1]
    ##          If 'include' is specified, this field is ignored.
    #lnv:
    #  enable: true
    #  exclude: []
    #  include: []
    ## VXLAN notifications
    ##
    ## Notify when VXLAN mismatch has occurred
    #vxlan:
    #  enable: true
    #  exclude: []
    #  include: []

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

<script src="js/lunr.js"></script>

<script src="js/lunr-extras.js"></script>

<script src="assets/js/scroll-search.js"></script>
