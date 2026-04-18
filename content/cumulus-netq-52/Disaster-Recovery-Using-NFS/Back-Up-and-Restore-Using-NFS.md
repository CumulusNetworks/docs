---
title: Back Up and Restore Using NFS
author: NVIDIA
weight: 500
toc: 2
---

The backup and restore process preserves data related to Cassandra, MongoDB, and lifecycle management. OTLP and search data are not preserved.


## Prerequisites
- The hostnames of all nodes in the target (new) cluster must match the corresponding node hostnames in the source (old) cluster.
- The NFS server must be accessible from all nodes in the new cluster. {{<link title="Set Up the NFS Server" text="Set up an NFS server">}} before performing the steps on this page.
- You must execute the backup and restore script from the cluster's master node.
- Retrieve the `backup-restore-nfs.sh` script: <!--need to check this 5.1--><p style="text-indent: 40px; margin: 0;">a. Log in to the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.</p><p style="text-indent: 40px; margin: 0;">b. Select <b>NVIDIA Licensing Portal</b>.</p><p style="text-indent: 40px; margin: 0;">c. Select <b>Software Downloads</b> from the menu.</p><p style="text-indent: 40px; margin: 0;">d. In the search field, enter <b>NetQ</b>.</p><p style="text-indent: 40px; margin: 0;">e. Locate the latest <i>NetQ Upgrade Backup Restore</i> file and select <b>Download</b>.</p><p style="text-indent: 40px; margin: 0;">f. If prompted, read the license agreement and proceed with the download.</p>

## Back Up and Restore NetQ Data

1. Back up the existing cluster. Run the following command on the master node of your NetQ cluster. Replace `NFS_SERVER_IP` with the IP address of the NFS server. Replace `NFS_SERVER_PATH` with the path configured in the `/etc/exports` file on the NFS server. Your NetQ data will be copied to and from this path. 

```
sudo NFS_SERVER_IP=10.104.229.103 NFS_SERVER_PATH=/data/backup bash backup-restore-nfs.sh --backup
```
If the backup process fails at any point, you can try re-running this command.

2. Run the following command on your master node to initialize the cluster. Copy the output of the command to use on your worker nodes. If you're backing up a standalone, single server deployment, you do not need to run the `netq install cluster worker-init` command:

```
nvidia@<hostname>:~$ netq install cluster master-init
    Please run the following command on all worker nodes:
    netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVM3dQN9MWTU1a
```
3. Run the `netq install cluster worker-init <ssh-key>` command on each of your worker nodes. For standalone deployments, skip this step.

4. Restore the data on the new cluster. Copy the `backup-restore-nfs.sh` script to the master node.

5. Create a node mapping file that maps the node hostnames to their respective IP addresses. Format each line as `<node-name> <ip-address>`. Lines that start with `#` are ignored. To retrieve the node names from your cluster, run the `kubectl get nodes -o wide` command. The values in the `NAME` column are equivalent to the `node-name` values.

{{<expand "Example nodes.txt file for 3-node cluster">}}

```
master-node 10.104.229.161
onprem-worker1 10.104.229.236
onprem-worker2 10.104.229.158
```
{{</expand>}}

{{<expand "Example nodes.txt file for 6-node cluster">}}

```
scale-master 192.168.10.11
scale-worker1 192.168.10.12
scale-worker2 192.168.10.13
scale-worker3 192.168.10.14
scale-worker4 192.168.10.15
scale-worker5 192.168.10.16
```
{{</expand>}}


6. Run the following command to restore your data. NetQ automatically selects the latest backup available on the NFS server and restores the data to the same nodes as in the original cluster.
```
sudo NFS_SERVER_IP=10.104.229.103 \
NFS_SERVER_PATH=/data/backup6 \
NODE_MAP_FILE=/home/nvidia/scripts/nodes.txt \
bash backup-restore-nfs.sh --restore
```

7. After the restoration process completes, you can install NetQ using the installation command (`netq install`) associated with your {{<link title="Install the NetQ System" text="deployment model">}}. Do not use the `restore` option when running this command: the `restore` option is used exclusively for the {{<link title="Back Up and Restore NetQ" text="general backup and restore">}} process.

## Additional Backup and Restore Options

Perform a backup using a custom NFS mount point:

```
sudo NFS_SERVER_IP=192.168.1.100 NFS_SERVER_PATH=/export/netq-backup \
NFS_MOUNT_DIR=/mnt/nfs-backup \
./backup-restore-nfs.sh --backup
```

Perform a backup using a log file:

```
sudo NFS_SERVER_IP=192.168.1.100 NFS_SERVER_PATH=/export/netq-backup \
LOGFILE=/var/log/my-backup.log \
./backup-restore-nfs.sh --backup
```

Create a new backup directory. By default, the script reuses the latest backup directory. To create a new backup directory for each run, set `BACKUP_REUSE_LATEST` to `0`:

```
sudo NFS_SERVER_IP=192.168.1.100 NFS_SERVER_PATH=/export/netq-backup \
BACKUP_REUSE_LATEST=0 \
./backup-restore-nfs.sh --backup
```

Refresh metadata while continuing to use the existing data directory:

```
sudo NFS_SERVER_IP=192.168.1.100 NFS_SERVER_PATH=/export/netq-backup \
SKIP_METADATA_WHEN_REUSE=0 \
./backup-restore-nfs.sh --backup
```

## Troubleshooting

If the backup process fails at any point, re-run the backup command from step 1 on this page. If that fails, you can try adjusting the variables. The following table reflects a comprehensive list of variables you can specify during this process: 

| Variable                      | Default                          | Description                      |
|------------------------------|----------------------------------|----------------------------------|
| `NFS_SERVER_IP`              | Required                         | NFS server IP                    |
| `NFS_SERVER_PATH`            | Required                         | Export path                      |
| `NFS_MOUNT_DIR`              | `/mnt/nfs-share`                 | Local mount directory            |
| `KUBECONFIG`                 | `/etc/kubernetes/admin.conf`     | Kubernetes config                |
| `LOGFILE`                    | `/var/log/vm-backuprestore.log`  | Log file                         |
| `STATE_FILE`                 | `/tmp/netq-stop-state.txt`       | Stores replica counts            |
| `BACKUP_REUSE_LATEST`        | 1                              | Reuse latest backup directory    |
| `SKIP_METADATA_WHEN_REUSE`   | 1                              | Skip metadata when reusing       |
| `RSYNC_MAX_CONCURRENT`       | 3                              | Max concurrent rsync             |
| `RSYNC_BW_LIMIT`             | none                           | Rsync bandwidth limit            |
| `CASSANDRA_RSYNC_BW_LIMIT`   | none                           | Cassandra rsync limit            |
| `CASSANDRA_RSYNC_MAX_CONCURRENT` | 1                          | Cassandra concurrent jobs        |
| `RSYNC_NICE`                 | 19                             | Lower CPU priority               |
| `NODE_MAP_FILE`              | none                           | Node map file                    |
| `NODE_MAP_JSON`              | none                           | JSON node map                    |


The following example performs a backup with bandwidth limits to reduce CPU spikes and network load. The `RSYNC_BW_LIMIT` and `CASSANDRA_RSYNC_BW_LIMIT` variables reflect the general `rsync` and Cassandra replica `rsync` values, respectively, and are expressed in KB/s.

```
sudo NFS_SERVER_IP=192.168.1.100 NFS_SERVER_PATH=/export/netq-backup \
RSYNC_BW_LIMIT=10240 \
CASSANDRA_RSYNC_BW_LIMIT=5120 \
./backup-restore-nfs.sh --backup
```

- You can monitor `rsync` activity using the `ps aux | grep rsync` command.
- You can check the size of the backup directory using the `du -sh /mnt/nfs-share/hybrid-backup-*/node-data/*` command
- Log files are stored in the `/var/log/vm-backuprestore.log` directory by default.