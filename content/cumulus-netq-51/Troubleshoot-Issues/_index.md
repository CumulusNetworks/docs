---
title: Troubleshoot NetQ
author: NVIDIA
weight: 1050
subsection: true
toc: 2
---

This page describes how to troubleshoot issues with NetQ itself. If you need additional assistance, contact the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA support team">}} with the support file you created using the steps outlined on this page.

## Browse Configuration and Log Files

The following configuration and log files contain information that can help with troubleshooting:

| File | Description |
| ---- | ---- |
| `/etc/netq/netq.yml` | The NetQ configuration file. This file appears only if you installed either the `netq-apps` package or the NetQ Agent on the system. |
| `/var/log/netqd.log` | The NetQ daemon log file for the NetQ CLI. This log file appears only if you installed the `netq-apps` package on the system. |
| `/var/log/netq-agent.log` | The NetQ Agent log file. This log file appears only if you installed the NetQ Agent on the system. |

## Check NetQ System Installation Status

The `netq show status verbose` command shows the status of NetQ components after installation. Use this command to validate NetQ system readiness.

{{< expand "netq show status verbose" >}}


```
nvidia@netq:~$ netq show status verbose
NetQ Live State: Active
Installation Status: FINISHED
Version: 5.1.0
Installer Version: 5.1.0
Installation Type: Standalone
Activation Key: EhVuZXRxLWasdW50LWdhdGV3YXkYsagDIixkWUNmVmhVV2dWelVUOVF3bXozSk8vb2lSNGFCaE1FR2FVU2dHK1k3RzJVPQ==
Master SSH Public Key: c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCfdIVVJHVmZvckNLMHRJL0FrQnd1N2FtUGxObW9ERHg2cHNHaU1EQkM0WHdud1lmSlNleUpmdTUvaDFKQ2NuRXpOVnVWRjUgcm9vdEBhbmlscmVzdG9yZQ==
Is Cloud: False
Kubernetes Cluster Nodes Status:
IP Address     Hostname       Role    NodeStatus
-------------  -------------  ------  ------------
10.188.46.243  10.188.46.243  Role    Ready
Task                                                                Status
------------------------------------------------------------------  --------
Prepared for download and extraction                                FINISHED
Completed setting up python virtual environment                     FINISHED
Checked connectivity from master node                               FINISHED
Installed Kubernetes control plane services                         FINISHED
Installed Calico CNI                                                FINISHED
Installed K8 Certificates                                           FINISHED
Updated etc host file with master node IP address                   FINISHED
Stored master node hostname                                         FINISHED
Generated and copied master node configuration                      FINISHED
Updated cluster information                                         FINISHED
Plugged in release bundle                                           FINISHED
Downloaded, installed, and started node service                     FINISHED
Downloaded, installed, and started port service                     FINISHED
Patched Kubernetes infrastructure                                   FINISHED
Removed unsupported conditions from master node                     FINISHED
Installed NetQ Custom Resource Definitions                          FINISHED
Installed Master Operator                                           FINISHED
Updated Master Custom Resources                                     FINISHED
Updated NetQ cluster manager custom resource                        FINISHED
Installed Cassandra                                                 FINISHED
Created new database                                                FINISHED
Updated Master Custom Resources                                     FINISHED
Updated Kafka Custom Resources                                      FINISHED
Read Config Key ConfigMap                                           FINISHED
Backed up ConfigKey                                                 FINISHED
Read ConfigKey                                                      FINISHED
Created Keys                                                        FINISHED
Verified installer version                                          FINISHED
...
```
{{< /expand >}}

## Troubleshoot NetQ Installation and Upgrade Issues

Before you attempt a NetQ installation or upgrade, verify that your system meets the {{<link title="Install the NetQ System" text="minimum VM requirements">}} for your deployment type. 

{{%notice note%}}
If an upgrade or installation process stalls or fails, run the {{<link title="bootstrap" text="netq bootstrap reset">}} command to stop the process, followed by the {{<link title="install" text="netq install">}} command to re-attempt the installation or upgrade. 
{{%/notice%}}

{{<tabs "TabID113" >}}

{{<tab "Upgrade Issues">}}

| Error Message | Deployment Type | Solution |
| ---- | ---- | ---- |
| Error: Tar size is exceeding the minimum disk required to run NetQ.| 5.0.0 single server or HA scale cluster |  Reduce the size of  the backup file, delete old backup files, or update the filesystem trimming logic. Refer to {{<link title="Troubleshoot NetQ/#resolve-disk-capacity-issues" text="Resolve Disk Capacity Issues">}}. |
| Cannot upgrade a non-bootstrapped NetQ server. Please reset the cluster and re-install.| | Only a server that has been bootstrapped and has a valid `/etc/app-release` file can be upgraded.<br> 1. Run the `netq bootstrap reset` command. <br> 2. Run the {{<link title="install" text="netq install">}} command according to your deployment type. |
| Unable to get response from admin app. | | Re-run the {{<link title="upgrade" text="netq upgrade bundle <text-bundle-url>">}} command. If the retry fails with same error, reset the server and run the `install` command:<br> 1. Run the `netq bootstrap reset` command. <br> 2. Run the {{<link title="install" text="netq install">}} command according to your deployment type. |
| Unable to get response from kubernetes api server. |  | Re-run the {{<link title="upgrade" text="netq upgrade bundle <text-bundle-url>">}} command. If the retry fails with same error, reset the server and run the `install` command:<br> 1. Run the `netq bootstrap reset` command <br> 2. Run the {{<link title="install" text="netq install">}} command according to your deployment type. |
| Cluster vip is an invalid parameter for standalone upgrade. | Single server | Remove the `cluster-vip` option from the {{<link title="upgrade" text="netq upgrade bundle">}} command. |
| Please provide cluster-vip option and run command. | HA cluster | Include the `cluster-vip` option in the {{<link title="upgrade" text="netq upgrade bundle">}} command. | 
| Could not find admin app pod, please re-run the command. | | Re-run the {{<link title="upgrade" text="netq upgrade bundle <text-bundle-url>">}} command. |
| Could not upgrade server, unable to restore got exception: {} | On-premises |  The backup/restore option is only applicable for on-premises deployments which use {{<link title="Install a Custom Signed Certificate" text="self-signed certificates">}}.| 
{{</tab>}}

{{<tab "Installation Issues" >}}

| Error Message | Deployment Type | Solution |
| ---- | ---- | ---- |
| NetQ is operational with version: {}. Run the bootstrap reset before re-installing NetQ. | | NetQ has previously been installed. To install a new version:<br>1. Run the {{<link title="bootstrap" text="netq bootstrap reset">}} command. <br> 2. Run the {{<link title="install" text="netq install">}} command. |
| The Default interface was not found | | You must have a default route configured in your routing table, and the associated network interface must correspond to this default route.
| No default route found. Please set the default route via interface {} and re-run the installation. | | You must have a default route configured in your routing table, and the associated network interface must correspond to this default route. | 
| Default route set via a different interface {}. Please set the default route via interface {} and re-run the installation.| | You must have a default route configured in your routing table, and the associated network interface must correspond to this default route. |
| Minimum of {} GB RAM required but {} GB RAM detected.| | Increase VM resources according to your {{<link title="Install the NetQ System" text="deployment model requirements">}}.|
| Minimum of {} CPU cores required but {} detected.| | Increase VM resources according to your {{<link title="Install the NetQ System" text="deployment model requirements">}}.|
| Please free up disk as {} is {}% utilised. Recommended to keep under 70%. | | Delete previous software tarballs in the `/mnt/installables/` directory to regain space. If you cannot decrease disk usage to under 70%, contact the NVIDIA support team. |
| Did not find the `vmw_pvscsi` driver enabled on this NetQ VM. Please re-install the NetQ VM on ESXi server. | VMware | The NetQ VM must have the `vmw_pvscsi` driver enabled. |
| Error: Bootstrapped IP does not belong to any local IPs | | The IP address used for bootstrapping should be from the local network. |
| ERROR: IP address mismatch. Bootstrapped with: {} kube_Config: {} Admin_kube_config: {}| | The bootstrap IP address must match the kube config and admin kube config IP addresses. |
| ERROR: Clock not synchronised. Please check `timedatectl`. | | The system clock must be synchronized. Verify synchronization using the `timedatectl` command. |
| {} does not have sse4.2 capabilities. Check lscpu. | | The CPU model used for the installation must support SSE4.2. |
| NTP is installed. Please uninstall NTP as it will conflict with chrony installation.| | Uninstall NTP and any other NTP services, such as `ntpd` or SNTP.|
| Netqd service is not running | | Verify that the `netqd` service is up and running prior to installation. |
| Found identical ip for {} and {}/ Please provide different ip for cluster vip/workers. | HA cluster | The cluster virtual IP address (VIP) and worker node IP addresses must be unique. |
| Please provide worker nodes IPV6 addresses in order to have IPV6 support. | HA cluster | Provide IPv6 addresses for each worker node. |
| Master node is not initialised. Run “net install cluster master-init” on master node before NetQ Install/upgrade command. | HA cluster | Initialize the master node with the `netq install cluster master-init` command.|
| Worker node Ip {} is not reachable| HA cluster | Make sure worker nodes are reachable in your network. |
| Worker node {} is not initialised. Please initialise worker node and re-run the command.| HA cluster | After initializing the cluster on the master node, initialize each worker node with the `netq install cluster worker-init` command. |
| Cluster VIP is not valid IP address | HA cluster | Provide a valid cluster IP address. |
| All cluster addresses must belong to the same subnet. Master node net mask = {} | HA cluster |  Make sure all cluster IP addresses---the master, worker, and virtual IP---belong to the same subnet.|
| Virtual IP {} is already used | HA cluster | Provide a unique virtual IP address. |
| Package {} with version {} must be installed. | | Make sure the `netq-apps` version is the same as the tarball version. |
| Master node is already bootstrapped | | Run the {{<link title="bootstrap" text="netq bootstrap rest">}} command, followed by the {{<link title="install" text="netq install">}} command to re-attempt the installation. |
{{</tab>}}

{{</tabs>}}

### Resolve Disk Capacity Issues

When you perform a backup, you may encounter the following error: `Error: Tar size exceeds the minimum disk space required to run NetQ.` This error indicates that the backup operation will fail because the size of the backup file will cause NetQ to cross the 80% disk threshold limit.

Three resolution options are available, listed in order of recommendation. Try each option sequentially if the previous option does not resolve the issue.

{{< expand "Option 1: Reduce the size of the backup file" >}}

Compress the backup file by adding the compression flag to the backup command. The compression process increases the amount of time it takes to create the backup file, but the size of the file is significantly reduced.

1. Run the following command on your NetQ server (or the master node in cluster deployments):
```
nvidia@netq-server:~$ sudo /usr/sbin/vm-backuprestore.sh --backup --use_compression
```
2. Monitor the backup process. After the backup is complete, verify the backup file was created in the `/opt/backuprestore/` directory.

{{< /expand >}}

{{< expand "Option 2: Remove old backup files to free up disk space" >}}

The following steps remove backup files from the backup directory to free up disk space. Make sure that the files are not required for retention policies or compliance before performing these steps.

1. Run the `df -h /` command to check how much disk space is available.

2. Navigate to the backup directory on your NetQ server:
```
nvidia@netq-server:~$ cd /opt/backuprestore
```
3. List all backup files with their respective sizes using the `ls -lh` command.

4. Remove the old backup files. Specify the name of the backup .tar file in the command:
```
nvidia@netq-server:~$ sudo rm -f /opt/backuprestore/backup-netq-<old-date>.tar
```
5. After the file is removed, verify that sufficient disk space is available:
```
nvidia@netq-server:~$ df -h /
```
6. Retry the backup procedure. You can optionally include the compression flag in the backup command:
```
nvidia@netq-server:~$ sudo /usr/sbin/vm-backuprestore.sh --backup --use_compression
```

{{< /expand >}}

{{< expand "Option 3: Reclaim unused disk space by enabling filesystem trim" >}}

The following steps apply exclusively to NetQ version 5.0.0.

1. Create the configuration YAML file for the Longhorn filesystem trim recurring job:
```
sudo vi /tmp/longhorn-trim-recurringjob.yaml
```

2. Add the following content to the file:

```
apiVersion: longhorn.io/v1beta2
kind: RecurringJob
metadata:
  name: filesystem-trim-job
  namespace: longhorn-system
spec:
  # Run every hour at minute 0
  cron: "0 * * * *"
  task: filesystem-trim
  concurrency: 1
  retain: 0
```
3. Apply the recurring job to Kubernetes:
```
kubectl apply -f /tmp/longhorn-trim-recurringjob.yaml
```
4. Verify that the recurring job was created successfully:
```
kubectl get recurringjobs -n longhorn-system
```
5. The trim job runs every hour. After it runs, check the available disk space with the `df -h /` command.

6. If there is sufficient disk space, retry the backup procedure.
{{< /expand >}}

## Installation and Upgrade Hook Scripts

NVIDIA might provide hook scripts to patch issues encountered during a NetQ installation or upgrade. When you run the `netq install` or `netq upgrade` command, NetQ checks for specific hook script filenames in the `/usr/bin` directory. The expected filenames for NetQ 5.1.0 are:

- Pre-install script: `/usr/bin/pre_install_5.1.0.sh`
- Post-install script: `/usr/bin/post_install_5.1.0.sh`
- Pre-upgrade script: `/usr/bin/pre_upgrade_5.1.0.sh`
- Post-upgrade script: `/usr/bin/post_upgrade_5.1.0.sh`

After placing the script in the `/usr/bin` directory, set executable permissions with the `chmod +x /usr/bin/<filename>` command:

```
nvidia@netq-server:~$ sudo chmod +x /usr/bin/pre_install_5.1.0.sh
```

After copying the script to the expected path and setting it to executable, the script will run during the next installation or upgrade attempt.
## Verify Connectivity between Agents and Servers

The `sudo opta-info.py` command displays the status of and connectivity between agents and servers. This command is typically used when debugging NetQ.

{{<tabs "TabID73" >}}

{{<tab "Cloud Server">}}

In the output below, the Opta Health Status column displays a healthy status, which indicates that the server is functioning properly. The Opta-Gateway Channel Status column displays the connectivity status between the server and cloud endpoint. The Agent ID column displays the switches connected to the server.

```
nvidia@netq-server:~$ sudo opta-info.py
[sudo] password for nvidia:
Service IP:  10.102.57.27

Opta Health Status    Opta-Gateway Channel Status
--------------------  -----------------------------
Healthy               READY

Agent ID        Remote Address    Status      Messages Exchanged  Time Since Last Communicated
----------      ----------------  --------  --------------------  ------------------------------
switch1         /20.1.1.10:46420  UP                         906  2023-02-14 00:32:43.920000
netq-appliance  /20.1.1.10:44717  UP                        1234  2023-02-14 00:32:31.757000
```

{{</tab>}}

{{<tab "On-premises Server" >}}

```
nvidia@sm-telem-06:~$ sudo opta-info.py
Service IP:  10.97.49.106

Agent ID                                   Remote Address         Status      Messages Exchanged  Time Since Last Communicated
-----------------------------------------  ---------------------  --------  --------------------  ------------------------------
netq-lcm-executor-deploy-65c984fc7c-x97bl  /10.244.207.135:52314  UP                        1340  2023-02-13 19:31:37.311000
sm-telem-06                                /10.188.47.228:2414    UP                        1449  2023-02-14 06:42:12.215000
mlx-2010a1-14                              /10.188.47.228:12888   UP                          15  2023-02-14 06:42:27.003000
```

{{</tab>}}

{{</tabs>}}
## Generate a Support File on the NetQ System

The `opta-support` command generates information for troubleshooting issues with NetQ. It provides information about the NetQ Platform configuration and runtime statistics as well as output from the `docker ps` command.

```
nvidia@server:~$ sudo opta-support
Generating opta-support archive. Process takes few minutes to complete...
Please send /var/support/opta_support_server_2021119_165552.txz to Nvidia support.
```
To export network validation check data in addition to OPTA health data to the support bundle, the {{<link title="Install NetQ CLI#configure-the-netq-cli" text="NetQ CLI must be activated with AuthKeys">}}. If the CLI access key is not activated, the command output displays a notification and data collection excludes `netq show` output:

```
nvidia@server:~$ sudo opta-support
Access key is not found. Please check the access key entered or generate a fresh access_key,secret_key pair and add it to the CLI configuration
Proceeding with opta-support generation without netq show outputs
Please send /var/support/opta_support_server_20211122_22259.txz to Nvidia support.
```
## Generate a Support File on Switches and Hosts

The `netq-support` command generates information for troubleshooting NetQ issues on a host or switch. Similar to collecting a support bundle on the NetQ system, the NVIDIA support team might request this output to gather more information about switch and host status. 

When you run the `netq-support` command on a switch running Cumulus Linux, a {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Understanding-the-cl-support-Output-File/" text="cl-support file">}} will also be created and bundled within the NetQ support archive:

```
nvidia@switch:mgmt:~$ sudo netq-support
Collecting cl-support...
Collecting netq-support...
Please send /var/support/netq_support_switch_20221220_16188.txz to Nvidia support.
```

## Restart NetQ After a Power Failure

In the event of a major power outage or hardware failure, NetQ might not load properly when you power back on your server. First identify this issue by performing the following steps:

1. Check whether Cassandra pods are in a `CrashloopbackOff` state or are restarting frequently:

```
kubectl get pods -n netq-infra -l app.kubernetes.io/name=cassandra -o wide
```

Example output showing a crashing pod:

```
NAME                     READY   STATUS             RESTARTS        AGE   IP               NODE       NOMINATED NODE   READINESS GATES
netq-dc1-default-sts-0   0/2     CrashLoopBackOff   36 (50s ago)    3h52m 10.244.133.233   worker-2   <none>           <none>
netq-dc1-default-sts-1   2/2     Running            0               21h   10.244.219.127   master     <none>           <none>
netq-dc1-default-sts-2   2/2     Running            0               21h   10.244.226.111   worker-1   <none>           <none>
```

2. The log message from the crashing pods will return a `CommitLogReadException` exception:

```
kubectl logs -n netq-infra netq-dc1-default-sts-0 -c cassandra -p
```

Example error output:

```
org.apache.cassandra.db.commitlog.CommitLogReadHandler$CommitLogReadException: Could not read commit log descriptor in file /opt/cassandra/data/commitlog/CommitLog-7-1735662812573.log
at org.apache.cassandra.db.commitlog.CommitLogReader.readCommitLogSegment(CommitLogReader.java:195)
at org.apache.cassandra.db.commitlog.CommitLogReader.readCommitLogSegment(CommitLogReader.java:146)
at org.apache.cassandra.db.commitlog.CommitLogReplayer.replayFiles(CommitLogReplayer.java:157)
at org.apache.cassandra.db.commitlog.CommitLog.recoverFiles(CommitLog.java:221)
at org.apache.cassandra.db.commitlog.CommitLog.recoverSegmentsOnDisk(CommitLog.java:202)
at org.apache.cassandra.service.CassandraDaemon.setup(CassandraDaemon.java:360)
at org.apache.cassandra.service.CassandraDaemon.activate(CassandraDaemon.java:765)
at org.apache.cassandra.service.CassandraDaemon.main(CassandraDaemon.java:889)
```

To fix the issue, delete the corrupted commit log file from the Cassandra pod. The following example deletes the corrupted file from pod `netq-dc1-default-sts-0`:

1. Execute into the Cassandra container inside the failing pod:

```
kubectl exec -it -n netq-infra netq-dc1-default-sts-0 -c cassandra -- /bin/bash
```

2. Change directories to the `commitlog` directory:

```
cd /opt/cassandra/data/commitlog
```

3. List the commit log files to identify the corrupted file (referenced in the error message):

```
ls -la
```

4. Remove the corrupted commit log file:

```
rm CommitLog-7-1735662812573.log
```

5. Exit the pod with the `exit` command.

6. Delete the failing Cassandra pod. This allows Cassandra to recreate it:

```
kubectl get pods -n netq-infra -l app.kubernetes.io/name=cassandra
```

```
NAME                     READY   STATUS             RESTARTS        AGE
netq-dc1-default-sts-0   0/2     CrashLoopBackOff   37 (4m50s ago)  4h3m
netq-dc1-default-sts-1   2/2     Running            0               21h
netq-dc1-default-sts-2   2/2     Running            0               21h
```

```
kubectl delete pod -n netq-infra netq-dc1-default-sts-0
```

```
pod "netq-dc1-default-sts-0" deleted
```

7. Repeat these steps for all pods that are in a `CrashLoopBackOff` state. Verify that all faulty pods are recovered using the following command:

```
kubectl get pods -n netq-infra -l app.kubernetes.io/name=cassandra
```

```
NAME                     READY   STATUS    RESTARTS   AGE
netq-dc1-default-sts-0   2/2     Running   0          2s
netq-dc1-default-sts-1   2/2     Running   0          21h
netq-dc1-default-sts-2   2/2     Running   0          21h
```

If the problem persists, check whether the power outage caused node disk pressure, a condition where a node's available disk space becomes critically low. To recover from this state, perform a manual cleanup of the container images by checking which pods are taking up the most space. Then run `docker system prune -a` or `crictl rmi --prune` (depending on container runtime) to remove all unused images, containers, and networks.