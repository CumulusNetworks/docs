---
title: Troubleshooting NetQ
author: Cumulus Networks
weight: 31
aliases:
 - /display/NETQ10/Troubleshooting+NetQ
 - /pages/viewpage.action?pageId=6488225
pageID: 6488225
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
---
To aid in troubleshooting issues with NetQ, there are several
configuration and log files on the telemetry server that can provide
insight into the root cause of the issue:

| File                                                | Description                                   |
| --------------------------------------------------- | --------------------------------------------- |
| `/appliance/cfg/netq/netq.yml`                      | The NetQ Telemetry Server configuration file. |
| `/var/log/docker/netq/cli_1/netqd.log`              | The NetQ daemon log file for the NetQ CLI.    |
| `/var/log/docker/netq/notifier_1/netq-notifier.log` | The NetQ Notifier log file.                   |

A node running the NetQ Agent has the following configuration and log
files:

| File                                         | Description                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------- |
| `/etc/netq/netq.yml`                         | The NetQ configuration file.                                                 |
| `/var/log/netq-agent.log`                    | The NetQ Agent log file.                                                     |
| `/var/log/netqd.log`                         | The NetQ daemon log file.                                                    |
| `/etc/netq/config.d/netq-agent-commands.yml` | Contains key-value command pairs and relevant custom configuration settings. |
| `/run/netq-agent-running.json`               | Contains the full command list that will be pushed when the agent starts.    |

## Checking Agent Health</span>

Checking the health of the NetQ agents is a good way to start
troubleshooting NetQ on your network. If any agents are rotten, meaning
three heartbeats in a row were not sent, then you can investigate the
rotten node. In the example below, the NetQ Agent on server01 is rotten,
so you know where to start looking for problems:

<div class="confbox panel">

<div class="panel-content">

    netq@446c0319c06a:/$ netq check agents     
    Checked nodes: 12,    
         
    Rotten nodes: 1    
    netq@446c0319c06a:/$ netq show agents 
    Node      Status    Sys Uptime    Agent Uptime
    --------  --------  ------------  --------------
    exit01        
    Fresh    
         8h ago        4h ago
    exit02        
    Fresh    
         8h ago        4h ago
    leaf01        
    Fresh    
         8h ago        4h ago
    leaf02        
    Fresh    
         8h ago        4h ago
    leaf03        
    Fresh    
         8h ago        4h ago
    leaf04        
    Fresh    
         8h ago        4h ago
    server01      
    Rotten    
        4h ago        4h ago
    server02      
    Fresh    
         4h ago        4h ago
    server03      
    Fresh    
         4h ago        4h ago
    server04      
    Fresh    
         4h ago        4h ago
    spine01       
    Fresh    
         8h ago        4h ago
    spine02       
    Fresh    
         8h ago        4h ago

</div>

</div>

## Error Configuring the Telemetry Server on a Node</span>

If you get an error when your run the `netq add server` command on a
node, it's usually due to one of two reasons:

  - The hostname or IP address for the telemetry server was input
    incorrectly when you ran `netq add server`. Check what you input and
    try again.

  - The telemetry server isn't responding. Try pinging the IP address
    you entered and see if the ping works.

## netq-support</span>

The `netq-support` command generates an archive of useful information
for troubleshooting issues with NetQ. The Cumulus Networks support team
may request the output of this command when assisting with any issues
that you could not solve with your own troubleshooting:

    cumulus@switch:~$ netq-support

{{%notice note%}}

The `netq-support` script generates a file called `cl-support`.

{{%/notice%}}
