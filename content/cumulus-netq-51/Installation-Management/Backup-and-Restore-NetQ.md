---
title: Back Up and Restore NetQ
author: NVIDIA
weight: 520
toc: 3
---

The following sections describe how to back up and restore your NetQ data and VMs for on-premises deployments.

{{%notice note%}}
- You must run backup and restore scripts with sudo privileges.
- NetQ does not retain custom-signed certificates during the backup and restore process. If your deployment uses a custom-signed certificate, you must {{<link title="Install a Custom Signed Certificate" text="reconfigure the certificate">}} after you restore it on a new NetQ VM.
- The backup and restore process does not retain several configurations necessary for the Grafana integration, including switch TLS certificates, authentication tokens (vm-tokens), OpenTelemetry configurations, and external time-series database configurations. After reinstalling NetQ, you must {{<link title="Integrate NetQ with Grafana" text="reconfigure these components">}}. Grafana will not display data from previous NetQ versions.
{{%/notice%}}

## Back Up Your NetQ Data

Follow the process below for your deployment type to back up your NetQ data.

{{<tabs "TabID19" >}}
{{<tab "Ethernet-only and Combined (Ethernet + NVLink)" >}}

{{%notice note%}}
If your NetQ deployment uses combined Ethernet and NVLink mode, only your Ethernet data can be backed up and restored. NVLink data is excluded from the backup and restoration process.
{{%/notice%}}

1. Retrieve the `vm-backuprestore.sh` script:

<p style="text-indent: 40px">a. Log in to the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.<br></p>
<p style="text-indent: 40px">b. Select <b>NVIDIA Licensing Portal</b>.</p>
<p style="text-indent: 40px">c. Select <b>Software Downloads</b> from the menu.</p>
<p style="text-indent: 40px">d. In the search field, enter <b>NetQ</b>.</p>
<p style="text-indent: 40px">e. Locate the latest <i>NetQ Upgrade Backup Restore</i> file and select <b>Download</b>.</p>
<p style="text-indent: 40px">f. If prompted, read the license agreement and proceed with the download.<br></p>

2. Copy the `vm-backuprestore.sh` script to your NetQ server in standalone deployments, or to the master node in cluster deployments:

```
username@hostname:~$ scp ./vm-backuprestore.sh nvidia@10.10.10.10:/home/nvidia/
nvidia@10.10.10.10's password:
vm-backuprestore.sh                                                                                        
```

Then copy the `vm-backuprestore.sh` script to the `/usr/sbin/` directory on your NetQ servers:

```
nvidia@netq-server:~$ sudo cp ./vm-backuprestore.sh /usr/sbin/
```

3. Log in to your NetQ server (or the master node in cluster deployments) and set the script to executable.

```
nvidia@netq-server:/home/nvidia# sudo chmod +x /usr/sbin/vm-backuprestore.sh
```

4. On your NetQ server (or the master node in cluster deployments), run the `/usr/sbin/vm-backuprestore.sh --backup` command. This command backs up each node in your deployment and combines the data into a single .tar file. Take note of the config key in the output of this command. You will enter it when you restore your data:  

```
nvidia@netq-server:~$ sudo /usr/sbin/vm-backuprestore.sh --backup
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
Fri Jan 17 05:46:15 2025 - Creating backup tar /opt/backuprestore/backup-netq-cluster-onprem.tar
Backup is successful
Running backup on worker node (10.188.46.193)...
Fri Jan 17 05:46:19 2025 - Please find detailed logs at: /var/log/vm-backuprestore.log
Fri Jan 17 05:46:19 2025 - Starting backup of data, the backup might take time based on the size of the data
Fri Jan 17 05:46:19 2025 - Creating backup tar /opt/backuprestore/backup-netq-cluster-onprem.tar
Backup is successful
Running backup on worker node (10.188.44.55)...
Fri Jan 17 05:46:44 2025 - Please find detailed logs at: /var/log/vm-backuprestore.log
Fri Jan 17 05:46:44 2025 - Starting backup of data, the backup might take time based on the size of the data
Fri Jan 17 05:46:45 2025 - Creating backup tar /opt/backuprestore/backup-netq-cluster-onprem.tar
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

5. Copy the newly created tarball from the server and restore the data on your _new_ VM.

```
nvidia@netq-server:~$ sudo scp /opt/backuprestore/combined_backup_20250117054718.tar username:password@<destination>
```

{{</tab>}}
{{<tab "NVLink-only" >}}

These steps apply exclusively to {{<link title="Install NetQ for NVLink" text="NetQ NVLink">}} three-node cluster deployments.

1. Run the {{<link title="nvl/#netq-nvl-cluster-backup" text="netq nvl cluster backup">}} command on your cluster's master node, specifying the path to the directory where the backup file is stored. Make sure that the path ends with `backup`:

```
nvidia@<hostname>:~$ netq nvl cluster backup backup-path /home/nvidia/backup
2025-06-17 06:30:52,717 - INFO - Parsed arguments: Namespace(action='backup', backup_path='nvlink_cluster_backup', drop_mongo_collections=False, cm_op_ns='infra', cm_target_ns=['infra', 'kafka', 'nmx'], mongo_db_name=None, mongo_collections=None, mongo_k8s_ns='infra', mongo_statefulset='mongodb', mongo_container='mongodb', mongo_replicaset='rs0')
2025-06-17 06:30:52,717 - INFO - Action: Full Backup selected.
2025-06-17 06:30:52,717 - INFO - --- Starting NVLINK Cluster Full Backup to: nvlink_cluster_backup_20250617063052 ---
...
2025-06-17 06:30:55,159 - INFO - Full backup completed to: nvlink_cluster_backup_20250617063052
```
2. Run `netq bootstrap rest purge-db` on your cluster's master node.

3. Copy the newly-created file to the `/tmp/data-infra/` directory:

```
cp -r /home/nvidia/nvlink_cluster_backup_20250617063052 /tmp/data-infra
```


{{</tab >}}
{{</tabs>}}

## Restore Your NetQ Data

{{<tabs "TabID129" >}}
{{<tab "Ethernet-only and Combined (Ethernet + NVLink)"  >}}

To restore your NetQ data, perform a {{<link title="Install the NetQ System" text="new NetQ VM installation">}} and follow the steps to restore your NetQ data when you run the `netq install` command. You will use the `restore` option, referencing the path where the backup file resides.

{{</tab>}}
{{<tab "NVLink-only" >}}

1. Run the installation command on your master node and specify the following within the command itself: 

- The tarball of the latest NetQ release. This command upgrades NetQ to the release specified in the command.
- The passwords for the read-write user (`rw-password`) and the read-only user (`ro-password`)
- The `/home/nvidia/nvl-cluster-config.json` backup file

```
nvidia@<hostname>:~$ netq install nvl bundle /mnt/installables/NetQ-5.1.0.tgz kong-rw-password <rw-password> kong-ro-password <ro-password> /home/nvidia/nvl-cluster-config.json
```

2. Restore your data by running the {{<link title="nvl/#netq-nvl-cluster-restore" text="netq nvl cluster restore">}} command with the `drop-mongo-collections` option. This option prevents NetQ from re-installing duplicate data entries.

```
nvidia@<hostname>:~$ netq nvl cluster restore /tmp/data-infra/nvlink_cluster_backup_20250617063052/ drop-mongo-collections
```
If this step fails for any reason, run `netq nvl bootstrap reset` and then try again.

{{</tab >}}
{{</tabs>}}