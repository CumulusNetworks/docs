---
title: Configuring High Availability Mode
author: Cumulus Networks
weight: 47
aliases:
 - /display/NETQ121/Configuring+High+Availability+Mode
 - /pages/viewpage.action?pageId=8356542
pageID: 8356542
product: Cumulus NetQ
version: "1.2"
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
old: true
---
NetQ supports high availability - that is, the ability to continue
functioning even in the absence of a single failure of the telemetry
server node. To make the NetQ Telemetry Server highly available (*HA
mode*), you need to run three instances of the telemetry server.
Currently, exactly three instances are supported in HA mode. Of the
three instances, one is considered the *master* and is writeable while
the other two are read-only *replicas*. Each server instance is mapped
to port 6379 on the host. A Redis
*[sentinel](https://redis.io/topics/sentinel)* on each telemetry server
host monitors the health of the database cluster and decides which
database is the current master. If the master becomes unavailable, the
sentinel promotes one of the replicas to become the new master. Each
sentinel runs on port 26379.

HA mode is optional.

To begin using HA mode, install the telemetry server image on three
separate physical hosts to form a database cluster. Note the IP address
of each instance.

## Enabling HA Mode</span>

To configure the HA cluster, perform the following steps. These steps
assume there are three telemetry servers, ts01 (the original one which
was [already
configured](/cumulus-netq-121/Getting-Started-with-NetQ/) as the
telemetry server), ts02 and ts03, which are assigned IP addresses
10.0.0.5, 10.0.0.6 and 10.0.0.7, respectively. The servers are all
assumed to be up and reachable and can communicate with each other.

{{%notice note%}}

When configuring HA mode, you can only specify the IP addresses for the
telemetry servers. You cannot use the DNS names here.

{{%/notice%}}

1.  On each telemetry server, specify the IP address of the master, then
    both replicas. Wait at least 30 seconds between each instance of the
    command.
    
        cumulus@ts01:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.7
    
        cumulus@ts02:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.7
    
        cumulus@ts03:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.7

2.  Replicate NetQ Notifier on the replica telemetry servers, then
    restart the netq-notifier service on the replicas:
    
        cumulus@ts02:~$ sudo systemctl restart netq-notifier.service
    
        cumulus@ts03:~$ sudo systemctl restart netq-notifier.service

3.  Verify that HA mode is configured on the three telemetry servers.
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

4.  Update the agent on each switch and server node to point to the HA
    cluster, and restart the NetQ Agent on each node:
    
        cumulus@switch:~$ netq config add server 10.0.0.5 10.0.0.6 10.0.0.7
        Restarting netqd... Success!
        cumulus@switch:~$ netq config restart agent
        Restarting netq-agent... Success!

## Checking HA Mode Status</span>

To check the status of the database cluster, run the following command
from a telemetry server:

    cumulus@ts01:~$ netq config ts show server

You can also get the detailed output of a specific server in the cluster
by specifying that server's IP address:

    cumulus@ts01:~$ netq config ts show server 10.0.0.7

## Restarting HA Mode Services</span>

You can restart the `netq-appliance` and `netq-gui` services using:

    cumulus@ts01:~$ sudo systemctl restart netq-gui.service
    cumulus@ts01:~$ sudo systemctl restart netq-appliance.service

## Changing the Master Telemetry Server</span>

You can change which telemetry server you want to be the master simply
by changing the order in which you specify them with the `netq config ts
add server` command. You need to run the following command on each
telemetry server, waiting at least 30 seconds in between updating the
configuration on each server.

For example, notice that the telemetry server *ts01* is the master in
the following configuration:

    cumulus@ts01:~$ netq config ts show server
    Server    Role     Master    Replicas            Status    Last Changed
    --------  -------  --------  ------------------  --------  --------------
    10.0.0.5  master   10.0.0.5  10.0.0.6, 10.0.0.7  ok        50s
    10.0.0.6  replica  10.0.0.5  -                   ok        50s
    10.0.0.7  replica  10.0.0.5  -                   ok        50s

To make the first replica the new master, run the following command on
each telemetry server (you don't need to change anything on the switch
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

## Replacing a Replica with a New Server</span>

If you need to replace a telemetry server with a different physical
system, do the following steps.

{{%notice note%}}

Do not try and replace the master server. You can only replace a
replica. If you need to replace the master, make it a replica first, as
described above.

{{%/notice%}}

Consider the following cluster of telemetry servers:

    cumulus@ts01:~$ netq config ts show server
    Server    Role     Master    Replicas            Status    Last Changed
    --------  -------  --------  ------------------  --------  --------------
    10.0.0.5  master   10.0.0.5  10.0.0.6, 10.0.0.7  ok        14m:10s
    10.0.0.6  replica  10.0.0.5  -                   ok        14m:10s
    10.0.0.7  replica  10.0.0.5  -                   ok        14m:10s

10.0.0.5 (ts01) is the master, while 10.0.0.6 (ts02) and 10.0.0.7 (ts03)
are the replicas. You want to replace ts03 with ts04 (10.0.0.8):

1.  Bring up the new telemetry server (ts04) and make sure the
    connectivity is okay.

2.  Bring down the telemetry server you are replacing (ts03):
    
        cumulus@ts03:~$ sudo shutdown

3.  Execute the following NetQ command on every telemetry server to
    create a cluster with the new telemetry server. Wait at least 30
    seconds between each instance of the command.
    
        cumulus@ts01:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.8
    
        cumulus@ts02:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.8
    
        cumulus@ts04:~$ netq config ts add server 10.0.0.5 10.0.0.6 10.0.0.8

4.  Verify the HA status on one of the telemetry servers. The status
    should be the same on all the three telemetry servers indicating
    that ts01 (10.0.0.5) is the master:
    
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

## Resetting the Database Cluster</span>

You can force a reset of the Redis HA cluster using:

    cumulus@netq-ts:~$ netq config ts reset-cluster

## Troubleshooting HA Mode</span>

### Relevant Services and Configuration Files</span>

The following `systemd` services are involved in HA mode:

  - cts-auth.service: The telemetry server-side service that manages the
    configuration.

  - cts-auth.socket: The telemetry server-side authorization shim socket
    for the service console.

  - cts-backup.service: Runs a cron job to back up the Redis database.

  - cts-backup.timer: The timer for the backup service, with a minimum
    interval of 5 minutes.

  - netqd.service: The service for the telemetry server CLI for use
    locally on the server.

  - netq-appliance.service: Starts and stops all telemetry server
    services **except** for the `ts-gui` service.

  - netq-gui.service: Starts and stops telemetry server `ts-gui`
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

  - /var/log/netq-\#\#\#.log

Logging configurations are in:

  - /etc/rsyslog.d

  - /etc/logrotate.d

The following log files are in the `/var/log/cts` directory:

  - cts-backup.log

  - cts-docker-compose.log

  - cts-dockerd.log

  - cts-redis.log

  - cts-sentinel.log

For more information about the log files, see the [Troubleshooting
NetQ](/cumulus-netq-121/Troubleshooting-NetQ) chapter.

### One Replica Must Be Available Always</span>

While HA mode is enabled, if both the replica servers go down, the
master database stops accepting writes. This causes the NetQ agents to
go into a rotten state.

This serves to avoid having multiple masters in a split-brain condition.
Please refer to the section "Example 2: basic setup with three boxes" on
the [Redis Sentinel page](https://redis.io/topics/sentinel) for more
details.

