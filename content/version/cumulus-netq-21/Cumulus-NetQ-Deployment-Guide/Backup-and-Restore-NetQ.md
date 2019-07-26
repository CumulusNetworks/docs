---
title: Backup and Restore NetQ
author: Cumulus Networks
weight: 75
aliases:
 - /display/NETQ21/Backup+and+Restore+NetQ
 - /pages/viewpage.action?pageId=12320799
pageID: 12320799
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq-21
siteSlug: cumulus-netq-21
---
It is recommended that you back up your NetQ data according to your
company policy. This topic describes how to backup and also restore your
NetQ data.

Backup and restore can be performed as needed or it can be scheduled
through a cron job. NetQ 2.x data is stored in a Cassandra database.
Only one backup file is supported, and can be restored as needed. The
backup can be created from one running cluster and restored to another
cluster. The backup snapshot file is stored on a local drive.

 Any pre-reqs? Stop any services?

 Any recommendations on when to backup,
where to save the file, or other tips?

 Does this save agent data?

 Same steps for NetQ Appliance and NetQ
Cloud Appliance?

## Create a Backup File

To create a backup manually:

1.  Create a new subdirectory for the backup file in the `/opt`
    directory. For example: `netq`-`backup`.

2.  Navigate to the new directory.

3.  Run the backup script.

        cumulus@<netq-platform/netq-appliance>:~/opt/netq-backup# ./backuprestore.sh --backup --localdir /opt/netq-backup

    {{%notice tip%}}

    You can simplify this command to `./backuprestore.sh -b -l
    /opt/netq-backup` to reduce typing.

    {{%/notice%}}

4.  Verify the backup file has been created.

        cumulus@<netq-platform/netq-appliance>:~/opt/netq-backup# ls
        netq_master_snapshot_2019-06-04_07_24_50_UTC.tar.gz

To create a scheduled backup, add `./backuprestore.sh --backup
--localdir /opt/<backup-directory>` to an existing cron job or create a
new one.

## Restore NetQ from Your Backup File

To restore NetQ on the same Cassandra pod as the backup file:

1.  Navigate to your backup directory. For example, netq-backup.

2.  Run the restore script.

        cumulus@<netq-platform/netq-appliance>:~/opt/netq-backup# ./backuprestore.sh --restore --localdir /opt/netq-backup

    {{%notice tip%}}

    You can simplify this command to `./backuprestore.sh -r -l
    /opt/netq-backup` to reduce typing.

    {{%/notice%}}

3.   Install the backup file....   
     use instruction from upgrading
    procedure?

To restore NetQ on a different Cassandra pod on another server:

1.  Copy the backup file from the local backup directory to the backup
    directory on the target server.

2.  Navigate to the backup directory on the target server.

3.  Run the restore script.

        cumulus@<netq-platform/netq-appliance>:~/opt/netq-backup# ./backuprestore.sh --restore --localdir /opt/netq-backup

4.   Install the [backup file](/version/cumulus-netq-21/Cumulus-NetQ-Deployment-Guide/Backup-and-Restore-NetQ/)...
