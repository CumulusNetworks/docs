---
title: Back Up and Restore NetQ
author: NVIDIA
weight: 520
toc: 3
---

The following sections describe how to back up and restore your NetQ data and VMs for on-premises deployments. Cloud deployments are backed up automatically. The data restoration workflow upgrades your deployment to NetQ 4.13. 

{{<notice note>}}
- You must run backup and restore scripts with sudo privileges.<br>
- When you upgrade to NetQ 4.13, any pre-existing PTP data will be lost.
{{</notice>}}

## Back Up Your NetQ Data

1. Retrieve the `vm-backuprestore.sh` script:

<p style="text-indent: 40px">a. Log in to the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.<br></p>
<p style="text-indent: 40px">b. Select <b>NVIDIA Licensing Portal</b>.</p>
<p style="text-indent: 40px">c. Select <b>Software Downloads</b> from the menu.</p>
<p style="text-indent: 40px">d. In the search field, enter <b>NetQ</b>.</p>
<p style="text-indent: 40px">e. Locate the latest <i>NetQ Upgrade Backup Restore</i> file and select <b>Download</b>.</p>
<p style="text-indent: 40px">f. If prompted, read the license agreement and proceed with the download.<br></p>

2. Copy the `vm-backuprestore.sh` script to your NetQ server in standalone deployments, or to each node in cluster deployments:

```
username@hostname:~$ scp ./vm-backuprestore.sh cumulus@10.10.10.10:/home/cumulus/
cumulus@10.10.10.10's password:
vm-backuprestore.sh                                                                                        
```

Then copy the `vm-backuprestore.sh` script to the `/sbin/` directory on your NetQ servers:

```
cumulus@netq-server:~$ sudo cp ./vmbackuprestore.sh /sbin/
```

3. Log in to your NetQ server and set the script to executable. Do this for each node in your deployment:

```
cumulus@netq-appliance:/home/cumulus# chmod +x /usr/sbin/vm-backuprestore.sh
```

4. On your NetQ server (or the master node in cluster deployments), run the `/usr/sbin/vm-backuprestore.sh --backup` command. This command backs up each node in your deployment and combines the data into a single .tar file. Take note of the config key in the output of this command. You will enter it when you restore your data:  

```
cumulus@netq-appliance:~$ sudo /usr/sbin/vm-backuprestore.sh --backup
[sudo] password for cumulus:
Fri Jan 17 05:44:13 2025 - Please find detailed logs at: /var/log/vm-backuprestore.log
Stopping pods...
Fri Jan 17 05:44:13 2025 - Stopping pods in namespace default
Fri Jan 17 05:44:19 2025 - Scaling all pods to replica 0
Fri Jan 17 05:44:38 2025 - Waiting for all pods to go down in namespace: default
Fri Jan 17 05:45:39 2025 - Stopping pods in namespace ingress-nginx
Fri Jan 17 05:45:43 2025 - Scaling all pods to replica 0
Fri Jan 17 05:45:57 2025 - Waiting for all pods to go down in namespace: ingress-nginx
Fri Jan 17 05:45:57 2025 - Stopping pods in namespace monitoring
Fri Jan 17 05:46:01 2025 - Scaling all pods to replica 0
Fri Jan 17 05:46:14 2025 - Waiting for all pods to go down in namespace: monitoring
Fri Jan 17 05:46:14 2025 - All pods are down
Fetching master and worker IPs...
Running backup on all nodes...
Running backup on master node (10.188.46.221)...
Fri Jan 17 05:46:14 2025 - Starting backup of data, the backup might take time based on the size of the data
Fri Jan 17 05:46:15 2025 - Creating backup tar /opt/backuprestore/backup-netq-cluster-onprem-4.12.0-2025-01-17_05_46_15_UTC-a1ad8571-2184-42e2-b9a3-0fe7be8e1043.tar
Backup is successful
Running backup on worker node (10.188.46.193)...
Fri Jan 17 05:46:19 2025 - Please find detailed logs at: /var/log/vm-backuprestore.log
Fri Jan 17 05:46:19 2025 - Starting backup of data, the backup might take time based on the size of the data
Fri Jan 17 05:46:19 2025 - Creating backup tar /opt/backuprestore/backup-netq-cluster-onprem-4.12.0-2025-01-17_05_46_19_UTC-0309b675-2359-48e9-83d8-cfeac9585ba2.tar
Backup is successful
Running backup on worker node (10.188.44.55)...
Fri Jan 17 05:46:44 2025 - Please find detailed logs at: /var/log/vm-backuprestore.log
Fri Jan 17 05:46:44 2025 - Starting backup of data, the backup might take time based on the size of the data
Fri Jan 17 05:46:45 2025 - Creating backup tar /opt/backuprestore/backup-netq-cluster-onprem-4.12.0-2025-01-17_05_46_45_UTC-ecb3b55a-f660-42ee-8dc6-c16b22b6584e.tar
Backup is successful
Combining tars from all nodes...
Adding the latest master tar...
Fetching the latest tar from worker node (10.188.46.193)...
Fetching the latest tar from worker node (10.188.44.55)...
Creating combined tar at /opt/backuprestore/combined_backup_20250117054718.tar...
Cleaning up temporary files...
Combined tar created at /opt/backuprestore/combined_backup_20250117054718.tar
The config key is EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIixWMnkyRVRwbkxVVXBTVDFsSXUzM3NzRlNkMFE5S0Y3OFlVRVdBWUU5K244PQ==, alternately the config key is available in file /tmp/config-key
Starting pods on master node...
Fri Jan 17 05:48:25 2025 - Scaling all pods to replica 1
Fri Jan 17 05:50:01 2025 - Waiting for all pods to come up
Fri Jan 17 05:58:14 2025 - All pods are up
```

## Restore Your NetQ Data

Restore your data with the backup file you created in the preceding steps. The `restore` option copies the data from the backup file to the database, decompresses it, verifies the restoration, and starts all necessary services. 

Run the installation command on your NetQ server (or on the master node in cluster deployments), referencing the path where the backup file resides and including the `config-key` created during the backup process.

{{<tabs "96">}}

{{<tab "Single Server">}}

```
cumulus@netq-appliance:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-4.13.0-SNAPSHOT-feature-k8-ub-storage-upgrade.tgz config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIix1NHgwU3NhWlV5NzZXZVpiK2FFazRmQ3dkM2hzTk9IMWtDRlNjM0FHdVIwPQ== restore /home/cumulus/backup-netq-standalone-onprem-4.12.0-2024-12-11_19_50_12_UTC.tar
```
{{</tab>}}

{{<tab "Cluster" >}}

```
cumulus@netq-appliance:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-4.13.0-SNAPSHOT-feature-k8-ub-storage-upgrade.tgz config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIiwzNWJVL2NkZmtnekRqZ21yUUdZTHFFa0wvMVZSNHlLd3JaYlpuWE1VS21JPQ== workers 10.188.44.219 10.188.45.164 cluster-vip 10.188.45.169 restore /home/cumulus/combined_backup_20241211111316.tar
```

{{</tab>}}

{{<tab "Scale Cluster">}}

1. Add the `config-key` parameter to the JSON template you used during the {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster" text="scale cluster installation">}}. Edit the file with values for each attribute.

```
cumulus@netq-server:~$ vim /tmp/cluster-install-config.json 
{
        "version": "v2.0",
        "config-key": "<INPUT>",
        "interface": "<INPUT>",
        "cluster-vip": "<INPUT>",
        "master-ip": "<INPUT>",
        "is-ipv6": false,
        "ha-nodes":
                {
                        "ip": "<INPUT>"
                },
                {
                        "ip": "<INPUT>"
                }
}
```

2. Run the following command on your master node, using the JSON configuration file from the previous step. Include the restore option referencing the path where the backup file resides:

```
cumulus@<hostname>:~$ netq install cluster bundle /mnt/installables/NetQ-4.13.0.tgz /tmp/cluster-install-config.json restore /home/cumulus/combined_backup_20241211111316.tar
```
{{</tab>}}

{{</tabs>}}

{{<notice note>}}
If you restore NetQ data to a server with an IP address that is different from the one used to back up the data, you must {{<link title="Install NetQ Agents/#configure-netq-agents-using-a-configuration-file" text="reconfigure the agents">}} on each switch as a final step.
{{</notice>}}