---
title: Back Up and Restore NetQ
author: NVIDIA
weight: 520
toc: 3
---

The following sections describe how to back up and restore your NetQ data and VMs.

{{<notice note>}}
These procedures only apply to on-premises deployments. Cloud deployments are backed up automatically.
{{</notice>}}
{{<notice note>}}
You must run backup and restore scripts with sudo privileges.
{{</notice>}}

## Back Up Your NetQ Data

NetQ stores its data in a Cassandra database. You perform backups by running scripts provided with the software and located in the `/usr/sbin` directory. When you run a backup, the script creates a single `tar` file in the `/opt/backuprestore/` directory. 

To create a backup, refer to the following steps for your NetQ version.
### Back Up NetQ 4.4.1 or Earlier

1. Retrieve the `vm-backuprestore.sh` script:

<p style="text-indent: 40px">a. On the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}, log in to your account.<br></p>
<p style="text-indent: 40px">b. Select <b>NVIDIA Licensing Portal</b>.<br></p>
<p style="text-indent: 40px">c. Select <b>Software Downloads</b> from the menu.<br></p>
<p style="text-indent: 40px">d. Click <b>Product Family</b> and select <b>NetQ</b>.<br></p>
<p style="text-indent: 40px">e. Locate the NetQ Upgrade Backup Restore file and select <b>Download</b>.<br></p>
<p style="text-indent: 40px">f. If prompted, read the license agreement and proceed with the download.<br></p>

2. Copy the `vm-backuprestore.sh` script to your NetQ server:

```
username@hostname:~$ scp ./vm-backuprestore.sh cumulus@10.10.10.10:/home/cumulus/
cumulus@10.10.10.10's password:
vm-backuprestore.sh                                                                                       100%   15KB  54.0KB/s   00:00 
```

3. Log in to your NetQ server and set the script to executable:

```
cumulus@netq-appliance:/home/cumulus# chmod +x /usr/sbin/vm-backuprestore.sh
```

4. In the directory you copied the `vm-backuprestore.sh` script, run:

```
cumulus@netq-appliance:~$ sudo ./vm-backuprestore.sh --backup
[sudo] password for cumulus:
Mon Feb  6 12:37:18 2023 - Please find detailed logs at: /var/log/vm-backuprestore.log
Mon Feb  6 12:37:18 2023 - Starting backup of data, the backup might take time based on the size of the data
Mon Feb  6 12:37:19 2023 - Scaling static pods to replica 0
Mon Feb  6 12:37:19 2023 - Scaling all pods to replica 0
Mon Feb  6 12:37:28 2023 - Scaling all daemonsets to replica 0
Mon Feb  6 12:37:29 2023 - Waiting for all pods to go down
Mon Feb  6 12:37:29 2023 - All pods are down
Mon Feb  6 12:37:29 2023 - Creating backup tar /opt/backuprestore/backup-netq-standalone-onprem-4.4.0-2023-02-06_12_37_29_UTC.tar
Backup is successful, please scp it to the master node the below command:
      sudo scp /opt/backuprestore/backup-netq-standalone-onprem-4.4.0-2023-02-06_12_37_29_UTC.tar cumulus@<ip_addr>:/home/cumulus
 
  Restore the backup file using the below command:
      ./vm-backuprestore.sh --restore --backupfile /opt/backuprestore/backup-netq-standalone-onprem-4.4.0-2023-02-06_12_37_29_UTC.tar
cumulus@netq-appliance:~$
```

5. Verify the backup file creation was successful:

   ```
   cumulus@netq-appliance:~$ cd /opt/backuprestore/
   cumulus@netq-appliance:~/opt/backuprestore$ ls
   backup-netq-standalone-onprem-4.4.0-2023-02-06_12_37_29_UTC.tar
   ```

### Back Up NetQ 4.5.0 or Later

1. Run the backup script `/usr/sbin/vm-backuprestore.sh`:

```
cumulus@netq-appliance:~$ sudo /usr/sbin/vm-backuprestore.sh --backup
```

2. Verify the backup file creation was successful:

   ```
   cumulus@netq-appliance:~$ cd /opt/backuprestore/
   cumulus@netq-appliance:~/opt/backuprestore$ ls
   ```


## Restore Your NetQ Data

Restore NetQ data with the backup file you created in the steps above. The restore option of the backup script copies the data from the backup file to the database, decompresses it, verifies the restoration, and starts all necessary services. You should not see any data loss as a result of a restore operation.

Run the restore script, referencing the directory where the backup file resides.

{{<notice note>}}
If you restore NetQ data to a server with an IP address that is different from the one used to back up the data, you must {{<link title="Install NetQ Agents/#configure-netq-agents-using-a-configuration-file" text="reconfigure the agents">}} on each switch as a final step.
{{</notice>}}

```
cumulus@netq-appliance:~$ sudo vm-backuprestore.sh --restore --backupfile /home/cumulus/backup-netq-standalone-onprem-4.4.0-2023-02-06_12_37_29_UTC.tar
Mon Feb  6 12:39:57 2023 - Please find detailed logs at: /var/log/vm-backuprestore.log
Mon Feb  6 12:39:57 2023 - Starting restore of data
Mon Feb  6 12:39:57 2023 - Extracting release file from backup tar
Mon Feb  6 12:39:57 2023 - Cleaning the system
Mon Feb  6 12:39:57 2023 - Restoring data from tarball /home/cumulus/backup-netq-standalone-onprem-4.4.0-2023-02-06_12_37_29_UTC.tar
Data restored successfully
  Please follow the below instructions to bootstrap the cluster
  The config key restored is EhVuZXRxLWVuZHBvaW50LWdhdGVfYXkYsagDIix2OUJhMUpyekMwSHBBaitUdTVDaTRvbVJDR3F6Qlo4VHhZRytjUUhLZGJRPQ==, alternately the config key is available in file /tmp/config-key
 
  Pass the config key while bootstrapping:
  Example(standalone): netq install standalone full interface eth0 bundle /mnt/installables/NetQ-4.8.0.tgz config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIix2OUJhMUpyekMwSHBbaitUdTVDaTRvbVJDR3F6Qlo4VHhZRytjUUhLZGJRPQ==
  Example(cluster):    netq install cluster full interface eth0 bundle /mnt/installables/NetQ-4.8.0.tgz config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIix2OUJhMUpyekMwSHBbaitUdTVDaTRvbVJDR3F6Qlo4VHhZRytjUUhLZGJRPQ==
  Alternately you can setup config-key post bootstrap in case you missed to pass it during bootstrap
  Example(standalone): netq install standalone activate-job config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIix2OUJhMUpyekMwSHBbaitUdTVDaTRvbVJDR3F6Qlo4VHhZRytjUUhLZGJRPQ==
  Example(cluster):    netq install cluster activate-job config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIix2OUJhMUpyekMwSHBbaitUdTVDaTRvbVJDR3F6Qlo4VHhZRytjUUhLZGJRPQ==
  In case the IP of the restore machine is different from the backup machine, please reconfigure the agents using: https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-44/Installation-Management/Install-NetQ/Install-NetQ-Agents/#configure-netq-agents-using-a-configuration-file
cumulus@netq-appliance:~$
```