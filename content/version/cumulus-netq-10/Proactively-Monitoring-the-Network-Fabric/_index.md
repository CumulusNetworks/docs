---
title: Proactively Monitoring the Network Fabric
author: Cumulus Networks
weight: 17
aliases:
 - /display/NETQ10/Proactively+Monitoring+the+Network+Fabric
 - /pages/viewpage.action?pageId=6488207
pageID: 6488207
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
---
NetQ continually and algorithmically checks for these symptoms and sends
real-time alerts via *NetQ Notifier* to notify users that a network
state deviation has occurred. When alerted, you can determine precisely
where the fault occurred so you can remediate quickly.

## NetQ Notifier</span>

The NetQ Notifier's role within the NetQ suite of applications is to
deliver alerts to users through mediums such as Slack and syslog,
informing users of network events.

{{% imgOld 0 %}}

Notifications can be provided for the following network events:

  - BGP session failures

  - Host sensor failures

  - License failures

  - Link up/down

  - LNV failures

  - MLAG node failures

  - MTU mismatches

  - NetQ Agent failures

  - OSPF session failures

  - VLAN mismatches

  - VXLAN failures

When a notification arrives, what should you do next? Typically, you
could run `netq check` commands; see [Performing Network
Diagnostics](/version/cumulus-netq-10/Performing-Network-Diagnostics)
for more information. For a thorough example, read about troubleshooting
[MLAG node
failures](/version/cumulus-netq-10/Proactively-Monitoring-the-Network-Fabric/MLAG-Troubleshooting-with-NetQ).

### Log Message Format</span>

Messages have the following structure:

    <level> <type>: <message>

For example:

    INFO: AGENTS: All nodes are up.

Enumerated lists are appended to the next line:

    WARNING: VLAN: 3 mismatch(es) are found. They are: server01 torbond1, server02 torbond1, server03 torbond1

### Supported Third-party Applications</span>

The following applications are supported by NetQ for notifications:

  - PagerDuty: NetQ Notifier sends notifications to PagerDuty as
    PagerDuty events.
    
    {{% imgOld 1 %}}

  - rsyslog: Using `rsyslog`, NetQ Notifier sends alerts and events to
    the `/var/log/docker/netq/notifier_1/netq-notifier.log` file by
    default, but notifications can also be sent to ELK/Logstash or
    Splunk.
    
    {{% imgOld 2 %}}

  - Slack: NetQ Notifier sends notifications to Slack as incoming
    webhooks for a Slack channel you configure. For example:
    
    {{% imgOld 3 %}}

### Early Access Support</span>

Early access features include NetQ Notifier integration with:

  - ELK

  - Splunk

In addition, you can export NetQ Notifier data to the following
applications:

  - ELK/Logstash

  - PagerDuty

  - Slack

  - Splunk

  - syslog

NetQ integrates with ELK and Splunk using `rsyslog`, a standard
mechanism to capture log files in Linux. Both ELK and Splunk provide
plugins to handle `rsyslog` inputs.

To configure PagerDuty, Slack or `syslog`, you need to edit the NetQ
configuration file `/etc/netq/netq.yml`.

### Exporting to ELK</span>

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

    root@ts_host:~# vi /etc/logstash/conf.d/notifier_logstash.conf
     
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

### Exporting to Splunk</span>

To export NetQ Notifier data to Splunk, on the host running the NetQ
Telemetry Server and NetQ Notifier, configure the notifier to send the
logs to Splunk. In the following example, Splunk is on a host with the
IP address 192.168.50.30, using port 51414:

    # rsyslog - splunk configuration 
    sed -i ‘/$netq_notifier_log/a if $programname == “netq-notifier” then @@192.168.50.30:51415’ /etc/rsyslog.d\
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

    cumulus@leaf01:~$ netq check vlan 
    Checked Nodes: 25, Checked Links: 775, Failed Nodes: 3, Failed Links: 6
    Vlan and/or PVID mismatch found on following links
    Node      Interface    Vlans              Peer     Peer Interface    Peer Vlans         Error
    --------  -----------  -----------------  -------  ----------------  -----------------  -----------------
    server01  torbond1     103-106,1000-1005  leaf02   hostbond2         101-106,1000-1005  VLAN set Mismatch
    server01  torbond1     103-106,1000-1005  leaf01   hostbond2         101-106,1000-1005  VLAN set Mismatch
    server02  torbond1     102-106,1000-1005  leaf02   hostbond3         101-106,1000-1005  VLAN set Mismatch
    server02  torbond1     102-106,1000-1005  leaf01   hostbond3         101-106,1000-1005  VLAN set Mismatch
    server03  torbond1     102-106,1000-1005  leaf04   hostbond2         101-106,1000-1005  VLAN set Mismatch
    server03  torbond1     102-106,1000-1005  leaf03   hostbond2         101-106,1000-1005  VLAN set Mismatch

## Extending NetQ with Custom Services Using curl</span>

You can extend NetQ to monitor parameters beyond what it monitors by
default. For example, you can create a service that runs a series of
pings to a known host or between two known hosts to ensure that
connectivity is valid. Or you can create a service that curls a URL and
sends the output to `/dev/null`. This method works with the [NetQ time
machine](Performing-Network-Diagnostics.html#src-6488212_PerformingNetworkDiagnostics-time_machine)
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
    
        cumulus@leaf01: netq agent restart

4.  You can verify the command is running by checking the
    `/var/run/netq-agent-running.json` file:
    
        cumulus@leaf01: sudo cat /var/run/netq-agent-running.json
        cumulus@leaf01:mgmt-vrf:~$ cat /var/run/netq-agent-running.json 
        {"commands": [{"callback": null, "service": "web", "command": "/usr/bin/curl https://cumulusnetworks.com/ -o /dev/null", "period": 60, "key": "webping"},  #this is the output
         
        {"service": "smond", "always": false, "period": 30, "callback": {}, "command": "/usr/sbin/smonctl -j", "key": "smonctl-json"}, {"service": "zebra", "always": false, "period": 60, "callback": null, "command": ["/usr/bin/vtysh", "-c", "show running-config"], "key": "config-quagga"}, {"service": "clagd", "always": false, "period": 15, "callback": {}, "command": "/usr/bin/clagctl -j", "key": "clagctl-json"}, {"service": "bgpd", "always": false, "period": 15, "callback": {}, "command": ["/usr/bin/vtysh", "-c", "show ip bgp vrf all neighbors json"], "key": "bgp-neighbors"}, {"service": "misc", "always": false, "period": 30, "callback": {}, "command": "/usr/sbin/switchd -lic", "key": "cl-license"}, {"service": "misc", "always": false, "period": 60, "callback": null, "command": "/bin/cat /etc/network/interfaces", "key": "config-interfaces"}, {"service": "misc", "always": false, "period": 60, "callback": null, "command": "/bin/cat /etc/ntp.conf", "key": "config-ntp"}, {"service": "lldpd", "always": false, "period": 30, "callback": {}, "command": "/usr/sbin/lldpctl -f json", "key": "lldp-neighbor-json"}, {"service": "mstpd", "always": false, "period": 15, "callback": {}, "command": "/sbin/mstpctl showall json", "key": "mstpctl-bridge-json"}], "backend": {"server": "192.168.0.254", "vrf": "mgmt", "port": 6379}}
        cumulus@leaf01:mgmt-vrf:~$  

5.  And you can see the service is running on the host when you run netq
    show services:
    
        cumulus@leaf01: netq show services web

## Exporting NetQ Data</span>

Data from the NetQ Telemetry Server can be exported in a number of ways.
First, you can use the `json` option to output check and show commands
to JSON format for parsing in other applications.

For example, you can check the state of BGP on your network with `netq
check bgp`:

    cumulus@leaf01:~$ netq check bgp
    Total Nodes: 25, Failed Nodes: 2, Total Sessions: 228 , Failed Sessions: 2, 
    Node        Neighbor    Peer ID     Reason    Time
    ----------  ----------  ----------  --------  -------
    exit01      swp6.2      spine01     Idle      15h ago
    spine01     swp3.2      exit01      Idle      15h ago

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

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

<script src="js/lunr.js"></script>

<script src="js/lunr-extras.js"></script>

<script src="assets/js/scroll-search.js"></script>
