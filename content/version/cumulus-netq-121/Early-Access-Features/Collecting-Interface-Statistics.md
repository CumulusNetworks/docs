---
title: Collecting Interface Statistics
author: Cumulus Networks
weight: 79
aliases:
 - /display/NETQ121/Collecting-Interface-Statistics
 - /pages/viewpage.action?pageId=8356589
pageID: 8356589
product: Cumulus NetQ
version: 1.2.1
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
The NetQ Agent collects interface counters from `/proc/net/dev` and
pushes them to the NetQ Telemetry Server, where they are stored in a
container running an
[InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/)
database. Only counters for physical interfaces are collected; NetQ does
not collect counters for non-physical interfaces like bonds, bridges and
VXLANs.

The NetQ Agent uses the `netq-stats-pushd` service to collect counters
and push them to the database on the telemetry server. The service
collects counters every 15 seconds.

The counters that are collected include:

  - rx\_bytes, rx\_drop, rx\_errs, rx\_frame, rx\_multicast, rx\_packets

  - tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs, tx\_packets

{{%notice warning%}}

**Early Access Feature**

Collecting counters is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus NetQ 1.2.

{{%/notice%}}

## <span>Configuring Counter Collection</span>

The InfluxDB database is installed in its own container by default on
the telemetry server. The `netq-stats-pushd` service is also installed,
but must be enabled. You also need to enable counter collection on every
node for which you want to gather statistics.

To enable and start the `netq-stats-pushd` service on the telemetry
server, run:

    cumulus@ts:~$ sudo systemctl enable netq-stats-pushd.service
    cumulus@ts:~$ sudo systemctl start netq-stats-pushd.service

To check the status of the service, use systemd:

    cumulus@ts:~$ sudo systemctl status netq-stats-pushd.service 
    ● netq-stats-pushd.service - NetQ Stats Storage daemon
       Loaded: loaded (/lib/systemd/system/netq-stats-pushd.service; enabled)
       Active: active (running) since Mon 2017-11-27 00:51:09 UTC; 6s ago
     Main PID: 30550 (netq-stats-push)

On every node you want to monitor, enable counter collection, then
restart the NetQ Agent:

    cumulus@ts:~$ netq config add stats
    cumulus@ts:~$ netq config restart agent

Once the agent is restarted, the `netq-stats-pushd` service starts
collecting interface statistics and pushes them to the database on the
telemetry server.

## <span>Troubelshooting</span>

The primary log files for the telemetry server are:

  - /var/log/cts/cts-influxdb.log

  - /var/log/netq-stats-pushd.log

On each node, check the NetQ Agent log file: `/var/log/netq-agent.log`.

## <span>Disabling Counter Collection</span>

To disable counter collection on a node, run the following commands:

    cumulus@switch:~$ netq config del stats
    cumulus@switch:~$ netq config restart agent

Disabling this feature does not purge the data already collected from
the database.

Once all nodes have stopped pushing statistics, you can stop and disable
the `netq-stats-pushd` service on the telemetry server:

    cumulus@ts:~$ sudo systemctl stop netq-stats-pushd.service
    cumulus@ts:~$ sudo systemctl disable netq-stats-pushd.service

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
