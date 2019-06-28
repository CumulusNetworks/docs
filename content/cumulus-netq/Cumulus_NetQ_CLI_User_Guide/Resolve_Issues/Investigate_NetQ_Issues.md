---
title: Investigate NetQ Issues
author: Cumulus Networks
weight: 111
aliases:
 - /display/NETQ/Investigate+NetQ+Issues
 - /pages/viewpage.action?pageId=10456384
pageID: 10456384
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
There are several paths you can take to locate and investigate issues
that occur in the NetQ software itself, including viewing configuration
and log files, verifying NetQ Agent health, and verifying NetQ Platform
configuration. If these do not produce a resolution, you can capture a
log to use in discussion with Cumulus Networks support team.

## <span>Browse Configuration and Log Files</span>

To aid in troubleshooting issues with NetQ, there are the following
configuration and log files that can provide insight into the root cause
of the issue:

| File                      | Description                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/etc/netq/netq.yml`      | The NetQ configuration file. This file appears only if you installed either the `netq-apps` package or the NetQ Agent on the system. |
| `/var/log/netqd.log`      | The NetQ daemon log file for the NetQ CLI. This log file appears only if you installed the `netq-apps` package on the system.        |
| `/var/log/netq-agent.log` | The NetQ Agent log file. This log file appears only if you installed the NetQ Agent on the system.                                   |

## <span>Check NetQ Agent Health</span>

Checking the health of the NetQ Agents is a good way to start
troubleshooting NetQ on your network. If any agents are rotten, meaning
three heartbeats in a row were not sent, then you can investigate the
rotten node. In the example below, the NetQ Agent on server01 is rotten,
so you know where to start looking for problems:

    cumulus@switch:$ netq check agents     
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

## <span>Generate a Support File</span>

The `opta-support` command generates an archive of useful information
for troubleshooting issues with NetQ. It is an extension of the
`cl-support` command in Cumulus Linux. It provides information about the
NetQ Platform configuration and runtime statistics as well as output
from the `docker ps` command. The Cumulus Networks support team may
request the output of this command when assisting with any issues that
you could not solve with your own troubleshooting. Run the following
command:

    cumulus@switch:~$ opta-support
