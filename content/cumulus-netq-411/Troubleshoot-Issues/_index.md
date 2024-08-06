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
cumulus@netq:~$ netq show status verbose
NetQ Live State: Active
Installation Status: FINISHED
Version: 4.11.0
Installer Version: 4.11.0
Installation Type: Standalone
Activation Key: EhVuZXRxLWasdW50LWdhdGV3YXkYsagDIixkWUNmVmhVV2dWelVUOVF3bXozSk8vb2lSNGFCaE1FR2FVU2dHK1k3RzJVPQ==
Master SSH Public Key: c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCfdsaHpjKzcwNmJiNVROOExRRXdLL3l5RVNLSHRhUE5sZS9FRjN0cTNzaHh1NmRtMkZpYmg3WWxKUE9lZTd5bnVlV2huaTZxZ0xxV3ZMYkpLMGdkc3RQcGdzNUlqanNMR3RzRTFpaEdNa3RZNlJYenQxLzh4Z3pVRXp3WTBWZDB4aWJrdDF3RGQwSjhnbExlbVk1RDM4VUdBVFVkMWQwcndLQ3gxZEhRdEM5L1UzZUs5cHFlOVdBYmE0ZHdiUFlaazZXLzM0ZmFsdFJxaG8rNUJia0pkTkFnWHdkZGZ5RXA1Vjc3Z2I1TUU3Q1BxOXp2Q1lXZW84cGtXVS9Wc0gxWklNWnhsa2crYlZ4MDRWUnN4ZnNIVVJHVmZvckNLMHRJL0FrQnd1N2FtUGxObW9ERHg2cHNHaU1EQkM0WHdud1lmSlNleUpmdTUvaDFKQ2NuRXpOVnVWRjUgcm9vdEBhbmlscmVzdG9yZQ==
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
<!--
## Troubleshoot Installation and Upgrade

Before you attempt a NetQ installation or upgrade, verify that your system meets the {{<link title="Install the NetQ System" text="minimum VM requirements">}} for your deployment type. 

{{%notice note%}}
If an upgrade or installation process stalls or fails, run the `netq bootstrap reset` command to stop the process, followed by the `netq install` command to re-attempt the installation or upgrade. 
{{%/notice%}}
## Known Installation and Upgrade Issues

{{<tabs "TabID113" >}}

{{<tab "Upgrade Issues">}}

| Error | Setup | Solution |
| ---- | ---- | ---- |
| Cannot upgrade a non-bootstrapped NetQ server. Please reset the cluster and re-install.| | Only a server that has been bootstrapped and has a valid `/etc/app-release` file can be upgraded.<br> 1. Run the `netq bootstrap reset` command. <br> 2. Run the `netq install` command. |
| Unable to get response from admin app. | | Re-run the `netq upgrade bundle <tarball>` command. If the retry fails with same error, reset the server and run the `install` command:<br> 1. Run the `netq bootstrap reset` command <br> 2. Run the `netq install` command. |
| Unable to get response from kubernetes api server. |  | Re-run the `netq upgrade bundle <tarball>` command. If the retry fails with same error, reset the server and run the `install` command:<br> 1. Run the `netq bootstrap reset` command <br> 2. Run the `netq install` command. |
| Cluster vip is an invalid parameter for standalone upgrade. | Single server | Remove the `cluster-vip` option from the `netq upgrade bundle` command. |
| Please provide cluster-vip option and run command. | HA server cluster | Include the `cluster-vip` option in the `netq upgrade bundle` command. | 
| Could not find admin app pod, please re-run the command. | | Re-run the `netq upgrade bundle <tarball>` command. |
| Could not upgrade server, unable to restore got exception: {} | On-premises |  The backup/restore option is only applicable for on-premises deployments which use {{<link title="Install a Custom Signed Certificate" text="self-signed certificates">}}.| 
{{</tab>}}

{{<tab "Installation Issues" >}}

| Error | Setup | Solution |
| ---- | ---- | ---- |
| NetQ is operational with version: {}. Run the bootstrap reset before re-installing NetQ. | | 1. Run the `netq bootstrap reset` command. <br> 2. Run the `netq install` command. |
| The Default interface was not found | | You must have a default route configured in your routing table, and the associated network interface must correspond to this default route.
| No default route found. Please set the default route via interface {} and re-run the installation. | | See above. | 
| Default route set via a different interface {}. Please set the default route via interface {} and re-run the installation.| | See above. |
| Minimum of {} GB RAM required but {} GB RAM detected.| | Increase VM resources according to your {{<link title="Install the NetQ System" text="deployment model requirements">}}.|
| Minimum of {} CPU cores required but {} detected.| | Increase VM resources according to your {{<link title="Install the NetQ System" text="deployment model requirements">}}.|
| Please free up disk as {} is {}% utilised. Recommended to keep under 70%. | | Delete previous software tarballs in the `/mnt/installables/` directory to regain space. If you cannot decrease disk usage to under 70%, contact the NVIDIA support team. |
| Did not find the vmw_pvscsi driver enabled on this NetQ VM. Please re-install the NetQ VM on ESXi server. | VMware | The NetQ VM must have the `vmw_pvscsi` driver enabled. |
| Error: Bootstrapped IP does not belong to any local IPs | | The IP address used for bootstrapping should be from the local network. |
| ERROR: IP address mismatch. Bootstrapped with: {} kube_Config: {} Admin_kube_config: {}| | The bootstrap IP address must match the kube config and admin kube config IP addresses. |
| ERROR: Clock not synchronised. Please check timedatectl. | | The system clock must be synchronized. Verify synchronization using the `timedatectl` command. |
| {} does not have sse4.2 capabilities. Check lscpu. | | The CPU model used for the installation must support SSE4.2. |
| NTP is installed. Please uninstall NTP as it will conflict with chrony installation.| | Uninstall NTP and any other NTP services, such as ntpd or SNTP.|
| Netqd service is not running | | Verify that the `netqd` service is up and running prior to installation. |
| Found identical ip for {} and {}/ Please provide different ip for cluster vip/workers. | Cluster | The cluster virtual IP address (VIP) and worker node IP addresses must be unique. |
| Please provide worker nodes IPV6 addresses in order to have IPV6 support. | Cluster | IPv6 addresses must be provided for worker nodes if IPv6 support is required. |
| Master node is not initialised. Run “net install cluster master-init” on master node before NetQ Install/upgrade command. | Cluster | Initialize the master node with the `netq install cluster master-init` command.|
| Worker node Ip {} is not reachable| Cluster | Make sure worker nodes are reachable in your network. |
| Worker node {} is not initialised. Please initialise worker node and re-run the command.| Cluster | After initializing the cluster on the master node, initialize each worker nodes with the `netq install cluster worker-init` command. |
| Cluster VIP is not valid IP address | Cluster | Provide a valid cluster IP address. |
| All cluster addresses must belong to the same subnet. Master node net mask = {} | Cluster |  Make sure all cluster IP addresses---the master, worker and virtual IP---belong to the same subnet.|
| Virtual IP {} is already used | Cluster | Provide a unique virtual IP address. |
| Package {} with version {} must be installed. | | Make sure `netq-apps` version is the same as the tarball version. |
| Master node is already bootstrapped | | Run the `netq bootstrap reset` command, followed by the `netq install` command to re-attempt the installation. |
{{</tab>}}

{{</tabs>}}
-->
## Installation and Upgrade Hook Scripts

NVIDIA might provide hook scripts to patch issues encountered during a NetQ installation or upgrade. When you run the `netq install` or `netq upgrade` command, NetQ checks for specific hook script filenames in the `/usr/bin` directory. The expected filenames for NetQ 4.11.0 are:

- Pre-install script: `/usr/bin/pre_install_4.11.0.sh`
- Post-install script: `/usr/bin/post_install_4.11.0.sh`
- Pre-upgrade script: `/usr/bin/pre_upgrade_4.11.0.sh`
- Post-upgrade script: `/usr/bin/post_upgrade_4.11.0.sh`

After placing the script in the `/usr/bin` directory, set executable permissions with the `chmod +x /usr/bin/<filename>` command:

```
cumulus@netq-server:~$ chmod +x /usr/bin/pre_install_4.11.0.sh
```

After copying the script to the expected path and setting it to executable, the script will run during the next installation or upgrade attempt.
## Verify Connectivity between Agents and Appliances

The `sudo opta-info.py` command displays the status of and connectivity between agents and appliances. This command is typically used when debugging NetQ.

{{<tabs "TabID73" >}}

{{<tab "Cloud Appliance">}}

In the output below, the Opta Health Status column displays a healthy status, which indicates that the appliance is functioning properly. The Opta-Gateway Channel Status column displays the connectivity status between the appliance and cloud endpoint. The Agent ID column displays the switches connected to the appliance.

```
cumulus@netq-appliance:~$ sudo opta-info.py
[sudo] password for cumulus:
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

{{<tab "On-premises Appliance" >}}

```
cumulus@sm-telem-06:~$ sudo opta-info.py
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
cumulus@server:~$ sudo opta-support
Please send /var/support/opta_support_server_2021119_165552.txz to Nvidia support.
```
To export network validation check data in addition to OPTA health data to the support bundle, the {{<link title="Install NetQ CLI#configure-netq-cli-using-the-cli" text="NetQ CLI must be activated with AuthKeys">}}. If the CLI access key is not activated, the command output displays a notification and data collection excludes `netq show` output:

```
cumulus@server:~$ sudo opta-support
Access key is not found. Please check the access key entered or generate a fresh access_key,secret_key pair and add it to the CLI configuration
Proceeding with opta-support generation without netq show outputs
Please send /var/support/opta_support_server_20211122_22259.txz to Nvidia support.
```
## Generate a Support File on Switches and Hosts

The `netq-support` command generates information for troubleshooting NetQ issues on a host or switch. Similar to collecting a support bundle on the NetQ system, the NVIDIA support team might request this output to gather more information about switch and host status. 

When you run the `netq-support` command on a switch running Cumulus Linux, a {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Understanding-the-cl-support-Output-File/" text="cl-support file">}} will also be created and bundled within the NetQ support archive:

```
cumulus@switch:mgmt:~$ sudo netq-support
Collecting cl-support...
Collecting netq-support...
Please send /var/support/netq_support_switch_20221220_16188.txz to Nvidia support.
