---
title: Back Up and Restore NetQ
author: Cumulus Networks
weight: 150
toc: 3
---

It is recommended that you back up your NetQ data according to your company policy. Typically this includes after key configuration changes and on a scheduled basis.

These topics describe how to backup and also restore your NetQ data for NetQ On-premises Appliance and VMs.

{{<notice note>}}
These procedures <em>do not</em> apply to your NetQ Cloud Appliance or VM. Data backup is handled automatically with the NetQ cloud service.
{{</notice>}}

## Back Up Your NetQ Data

NetQ data is stored in a Cassandra database. A backup is performed by running scripts provided with the software and located in the `/usr/sbin` directory. When a backup is performed, a single tar file is created. The file is stored on a local drive that you specify and is named `netq_master_snapshot_<timestamp>.tar.gz`. Currently, only one backup file is supported, and includes the entire set of data tables. It is replaced each time a new backup is created.

{{<notice note>}}
If the rollback option is selected during the lifecycle management upgrade process (the default behavior), a backup is created automatically.
{{</notice>}}

To manually create a backup:

1. If you are backing up data from NetQ 2.4.0 or earlier, or you upgraded from NetQ 2.4.0 to 2.4.1, obtain an updated backuprestore script. If you installed NetQ 2.4.1 as a fresh install, you can skip this step. Replace \<version\> in these commands with *2.4.1* or later release version.

   ```
   cumulus@switch:~$ tar -xvzf  /mnt/installables/NetQ-<version>.tgz  -C /tmp/ ./netq-deploy-<version>.tgz

   cumulus@switch:~$ tar -xvzf /tmp/netq-deploy-<version>.tgz   -C /usr/sbin/ --strip-components 1 --wildcards backuprestore/*.sh
   ```

2. Run the backup script to create a backup file in `/opt/<backup-directory>` being sure to replace the `backup-directory` option with the name of the directory you want to use for the backup file.

   ```
   cumulus@switch:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
   ```

   {{<notice tip>}}
You can abbreviate the <code>backup</code> and <code>localdir</code> options of this command to <code>-b</code> and <code>-l</code> to reduce typing. If the backup directory identified does not already exist, the script creates the directory during the backup process.
   {{</notice>}}

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

3. Verify the backup file has been created.

   ```
   cumulus@switch:~$ cd /opt/<backup-directory>
   cumulus@switch:~/opt/<backup-directory># ls
   netq_master_snapshot_2019-06-04_07_24_50_UTC.tar.gz
   ```

To create a scheduled backup, add `./backuprestore.sh --backup --localdir /opt/<backup-directory>` to an existing cron job, or create a new one.

## Restore Your NetQ Data

You can restore NetQ data using the backup file you created above in {{<link title="#Back Up Your NetQ Data">}}. You can restore your instance to the same NetQ Platform or NetQ Appliance or to a new platform or appliance. You do not need to stop the server where the backup file resides to perform the restoration, but logins to the NetQ UI will fail during the restoration process.The restore option of the backup script, copies the data from the backup file to the database, decompresses it, verifies the restoration, and starts all necessary services. You should not see any data loss as a result of a restore operation.

To restore NetQ on the same hardware where the backup file resides:

1. If you are restoring data from NetQ 2.4.0 or earlier, or you upgraded from NetQ 2.4.0 to 2.4.1, obtain an updated backuprestore script. If you installed NetQ 2.4.1 as a fresh install, you can skip this step. Replace \<version\> in these commands with *2.4.1* or later release version.

   ```
   cumulus@switch:~$ tar -xvzf  /mnt/installables/NetQ-<version>.tgz  -C /tmp/ ./netq-deploy-<version>.tgz

   cumulus@switch:~$ tar -xvzf /tmp/netq-deploy-<version>.tgz   -C /usr/sbin/ --strip-components 1 --wildcards backuprestore/*.sh
   ```

2. Run the restore script being sure to replace the `backup-directory` option with the name of the directory where the backup file resides.

   ```
   cumulus@switch:~$ ./backuprestore.sh --restore --localdir /opt/<backup-directory>
   ```

   {{<notice tip>}}
   You can abbreviate the <code>restore</code> and <code>localdir</code> options of this command to <code>-r</code> and <code>-l</code> to reduce typing.
   {{</notice>}}

   This is a sample of what you see while the script is running:

   ```
   [Fri 26 Jul 2019 02:37:49 PM UTC] - Received Inputs for restore ...

   WARNING: Restore procedure wipes out the existing contents of Database.
     Once the Database is restored you loose the old data and cannot be recovered.
   "Do you like to continue with Database restore:[Y(yes)/N(no)]. (Default:N)"
   ```

      You must answer the above question to continue the restoration. After entering **Y** or **yes**, the output continues as follows:
      
      ```
      [Fri 26 Jul 2019 02:37:50 PM UTC] - Able to find cassandra pod: cassandra-0
      [Fri 26 Jul 2019 02:37:50 PM UTC] - Continuing with the procedure ...
      [Fri 26 Jul 2019 02:37:50 PM UTC] - Backup local directory:/tmp/backuprestore/ exists....
      [Fri 26 Jul 2019 02:37:50 PM UTC] - Removing any stale restore directories ...
      Copying the file for restore to cassandra pod ....
      [Fri 26 Jul 2019 02:37:50 PM UTC] - Able to copy the local directory contents to cassandra pod in /tmp/backuprestore/.
      [Fri 26 Jul 2019 02:37:50 PM UTC] - copying the script to cassandra pod in dir:/tmp/backuprestore/....
      Executing the Script for restoring the backup ...
      /tmp/backuprestore//createbackup.sh: line 1: cript: command not found
      [Fri 26 Jul 2019 02:40:12 PM UTC] - Able to exeute /tmp/backuprestore//createbackup.sh script on cassandra pod
      [Fri 26 Jul 2019 02:40:12 PM UTC] - Restore finished successfully!
      ```

To restore NetQ on new hardware:

1. Copy the backup file from `/opt/<backup-directory>` on the older hardware to the backup directory on the new hardware.

2. Run the restore script on the new hardware, being sure to replace the `backup-directory` option with the name of the directory where the backup file resides.

   ```
   cumulus@switch:~$ ./backuprestore.sh --restore --localdir /opt/<backup-directory>
   ```

