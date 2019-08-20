---
title: Investigate NetQ Issues
author: Cumulus Networks
weight: 129
aliases:
 - /display/NETQ141/Investigate+NetQ+Issues
 - /pages/viewpage.action?pageId=10453531
pageID: 10453531
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
There are several tacks you can take to locate and investigate issues
that occur in the NeQ software itself, including viewing configuration
and log files, verifying NetQ Agent health, and verifying Telemetry
Server configuration. If these do not produce a resolution, you can
capture a log to use in discussion with Cumulus Networks support team.

## Browse Configuration and Log Files

To aid in troubleshooting issues with NetQ, there are several
configuration and log files on the **telemetry server** that can provide
insight into the root cause of the issue:

| File                                  | Description                                                                                                                                                                                                                                                                                                 |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/etc/netq/netq.yml`                  | The NetQ Telemetry Server configuration file.                                                                                                                                                                                                                                                               |
| `/var/log/cts/cts-backup.log`         | Database service backup log file.                                                                                                                                                                                                                                                                           |
| `/var/log/cts/cts-redis.log`          | The Redis log file.                                                                                                                                                                                                                                                                                         |
| `/var/log/cts/cts-sentinel.log`       | The Redis sentinel log file.                                                                                                                                                                                                                                                                                |
| `/var/log/cts/cts-dockerd.log`        | The Docker daemon log file.                                                                                                                                                                                                                                                                                 |
| `/var/log/cts/cts-docker-compose.log` | The backup log file.                                                                                                                                                                                                                                                                                        |
| `/var/log/netqd.log`                  | The NetQ daemon log file for the NetQ CLI.                                                                                                                                                                                                                                                                  |
| `/var/log/netq-notifier.log`          | The NetQ Notifier log file.                                                                                                                                                                                                                                                                                 |
| `/etc/cts/netq/netq.yml`              | The configuration file for NetQ running in the web-browser.                                                                                                                                                                                                                                                 |
| `/etc/cts/run/redis/redis_6379.conf`  | The runtime configuration file for the REDIS database.                                                                                                                                                                                                                                                      |
| `/etc/cts/run/redis/snt1.conf`        | The runtime configuration file for REDIS Sentinels.                                                                                                                                                                                                                                                         |
| `/etc/cts/redis/redis.conf`           | Contains the base REDIS configuration, which is inherited by and overriden by the `/etc/cts/run/redis/redis_6379.conf` file.                                                                                                                                                                                |
| `/etc/cts/environment`                | The configuration file for environment variables that configure and control NetQ Telemetry Server services. This file contains the `REDIS_MEMORY_PCT` environment variable. Setting this variable to a value between 10-90 allocates that much of the VM's total memory to REDIS. The default value is 60%. |

A **node** running the NetQ Agent has the following configuration and
log files:

| File                                         | Description                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------- |
| `/etc/netq/netq.yml`                         | The NetQ configuration file.                                                 |
| `/var/log/netq-agent.log`                    | The NetQ Agent log file.                                                     |
| `/etc/netq/config.d/netq-agent-commands.yml` | Contains key-value command pairs and relevant custom configuration settings. |
| `/run/netq-agent-running.json`               | Contains the full command list that will be pushed when the agent starts.    |

## Check NetQ Agent Health

Checking the health of the NetQ agents is a good way to start
troubleshooting NetQ on your network. If any agents are rotten, meaning
three heartbeats in a row were not sent, then you can investigate the
rotten node. In the example below, the NetQ Agent on server01 is rotten,
so you know where to start looking for problems:

```
cumulus@switch:~$ netq check agents     
Checked nodes: 12, Rotten nodes: 1

cumulus@switch:~$ netq show agents
Node      Status    Sys Uptime    Agent Uptime
--------  --------  ------------  --------------
exit01    Fresh     8h ago        4h ago
exit02    Fresh     8h ago        4h ago
leaf01    Fresh     8h ago        4h ago
leaf02    Fresh     8h ago        4h ago
leaf03    Fresh     8h ago        4h ago
leaf04    Fresh     8h ago        4h ago
server01  Rotten    4h ago        4h ago
server02  Fresh     4h ago        4h ago
server03  Fresh     4h ago        4h ago
server04  Fresh     4h ago        4h ago
spine01   Fresh     8h ago        4h ago
spine02   Fresh     8h ago        4h ago
```

## Verify Telemetry Server Configuration on a Node

If you get an error when your run the `netq config add server` command
on a node, it is usually due to one of two reasons:

  - The hostname or IP address for the telemetry server was input
    incorrectly when you ran `netq config add server`. Check what you
    input and try again.
  - The Telemetry Server is not responding. Try pinging the IP address
    you entered and see if the ping works.

## Generate a Support File

The `cts-support` command generates an archive of useful information for
troubleshooting issues with NetQ. It is an extension of the `cl-support`
command in Cumulus Linux. It provides information about the telemetry
server configuration and runtime statistics as well as output from the
`docker ps` command. The Cumulus Networks support team may request the
output of this command when assisting with any issues that you could not
solve with your own troubleshooting. Run the following command on the
Telemetry Server:

    cumulus@ts:~$ cts-support

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
