---
title: Restoring from Backups with NetQ
author: Cumulus Networks
weight: 31
aliases:
 - /display/NETQ121/Restoring+from+Backups+with+NetQ
 - /pages/viewpage.action?pageId=8356584
pageID: 8356584
product: Cumulus NetQ
version: "1.2"
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
NetQ automatically takes snapshots of the NetQ Telemetry Server at five
minute intervals. These snapshots can be used to restore to a previous
configuration, or to diagnose existing issues with the configuration.
For information regarding how long snapshot data is stored, refer to the
[How Far Back in Time Can You Travel](/version/cumulus-netq-121/Performing-Network-Diagnostics/#how-far-back-in-time-can-you-travel)
section.

{{%notice note%}}

There are no configuration steps required for setting up backups. NetQ
snapshots occur automatically.

{{%/notice%}}

## Backup Locations</span>

Backup snapshots can be found in two file locations on the NetQ
Telemetry Server:

  - `/var/log/backup`: The latest, or master, snapshot.

  - `/var/backup`: Directory of previous snapshots.

## Use Cases</span>

There are several use-cases in which restoring from a snapshot may be
warranted. These include:

  - Upgrading the physical server to increase available resources.

  - Migrating from one physical server to another.

  - A NetQ Telemetry Server crash.

## Restoring from a Snapshot</span>

The following steps outline the process for restoring the NetQ Telemetry
Server from a snapshot:

1.  Extract the GZip snapshot you wish to restore into a file called
    `appendonly.aof`. The example command below uses the master
    snapshot:
    
        root@cumulus:~# gzip -d < /var/backup/appendonly.aof_master_2017-06-06_054601.gz > appendonly.aof
    
    The snapshot filename has several parts:
    
      - `appendonly.aof`: The base file name.
    
      - `_master_`: Defines this file as the current master snapshot.
    
      - `2017-06-06_054601`: The date and time the snapshot was taken.

2.  Shutdown the NetQ stack:
    
        root@cumulus:~# sudo systemctl stop netq-appliance

3.  Copy the extracted `appendonly.aof` file into the data directory:
    
        root@cumulus:~# cp appendonly.aof /var/data/redis/master/appendonly.aof

4.  Remove the `dump.rmb` file from the master directory, if the file is
    present:
    
        root@cumulus:~# rm -f /var/data/redis/master/dump.rdb

5.  Use the `grep` command to confirm the Redis configuration is still
    set correctly:
    
        root@cumulus:~# grep appendonly /etc/cts/redis/*conf
        /etc/cts/redis/redis.conf:appendonly yes
        /etc/cts/redis/redis.conf:appendfilename "appendonly.aof"
        root@cumulus:~# grep 'save ""' /etc/cts/redis/*conf
        /etc/cts/redis/redis.conf:save ""

6.  Restart the NetQ Stack:
    
        root@cumulus:~# sudo systemctl start netq-appliance

