---
title: Restore Your NetQ Data
author: Cumulus Networks
weight: 170
toc: 4
---

You can restore NetQ data using the backup file you created in {{<link title="Back Up Your NetQ Data">}}. You can restore your instance to the same NetQ Platform or NetQ Appliance or to a new platform or appliance. You do not need to stop the server where the backup file resides to perform the restoration, but logins to the NetQ UI will fail during the restoration process.The restore option of the backup script, copies the data from the backup file to the database, decompresses it, verifies the restoration, and starts all necessary services. You should not see any data loss as a result of a restore operation.

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
