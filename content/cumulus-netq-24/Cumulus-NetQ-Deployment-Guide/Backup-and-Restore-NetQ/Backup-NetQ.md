---
title: Back Up Your NetQ Data
author: Cumulus Networks
weight: 160
toc: 4
---

NetQ 2.x data is stored in a Cassandra database. A backup is performed by running scripts provided with the software and located in the `/usr/sbin` directory. When a backup is performed, a single tar file is created. The file is stored on a local drive that you specify and is named `netq_master_snapshot_<timestamp>.tar.gz`. Currently, only one backup file is supported, and includes the entire set of data tables. It is replaced each time a new backup is created.

To create a backup:

1. Run the backup script to create a backup file in `/opt/<backup-directory>` being sure to replace the `backup-directory` option with the name of the directory you want to use for the backup file.

   ```
   cumulus@<netq-platform/netq-appliance>:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
   ```

   {{%notice tip%}}
You can abbreviate the `backup` and `localdir` options of this command to `-b` and `-l` to reduce typing. If the backup directory identified does not already exist, the script creates the directory during the backup process.
   {{%/notice%}}

   This is a sample of what you see as the script is running:

   ```
   [Fri 26 Jul 2019 02:35:35 PM UTC] - Received Inputs for backup ...
   [Fri 26 Jul 2019 02:35:36 PM UTC] - Able to find cassandra pod: cassandra-0
   [Fri 26 Jul 2019 02:35:36 PM UTC] - Continuing with the procedure ...
   [Fri 26 Jul 2019 02:35:36 PM UTC] - Removing the stale backup directory from cassandra pod...
   [Fri 26 Jul 2019 02:35:36 PM UTC] - Able to successfully cleanup up /opt/backuprestore from cassandra pod ...
   [Fri 26 Jul 2019 02:35:36 PM UTC] - Copying the backup script to cassandra pod ....
   /opt/backuprestore/createbackup.sh: line 1: cript: command not found
   [Fri 26 Jul 2019 02:35:48 PM UTC] - Able to exeute /opt/backuprestore/createbackup.sh script on cassandra pod
   [Fri 26 Jul 2019 02:35:48 PM UTC] - Creating local directory:/tmp/backuprestore/ ...  
   Directory /tmp/backuprestore/ already exists..cleaning up
   [Fri 26 Jul 2019 02:35:48 PM UTC] - Able to copy backup from cassandra pod  to local directory:/tmp/backuprestore/ ...
   [Fri 26 Jul 2019 02:35:48 PM UTC] - Validate the presence of backup file in directory:/tmp/backuprestore/
   [Fri 26 Jul 2019 02:35:48 PM UTC] - Able to find backup file:netq_master_snapshot_2019-07-26_14_35_37_UTC.tar.gz
   [Fri 26 Jul 2019 02:35:48 PM UTC] - Backup finished successfully!
   ```

2. Verify the backup file has been created.

   ```
   cumulus@<netq-platform/netq-appliance>:~$ cd /opt/<backup-directory>
   cumulus@<netq-platform/netq-appliance>:~/opt/<backup-directory># ls
   netq_master_snapshot_2019-06-04_07_24_50_UTC.tar.gz
   ```
   
To create a scheduled backup, add `./backuprestore.sh --backup --localdir /opt/<backup-directory>` to an existing cron job, or create a new one.
