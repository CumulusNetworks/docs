---
title: Troubleshoot NetQ
author: NVIDIA
weight: 1050
subsection: true
toc: 2
---

This page describes how to generate a support file for the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA support team">}} to help troubleshoot issues with NetQ itself.

## Browse Configuration and Log Files

The following configuration and log files contain information that can help with troubleshooting:

| File | Description |
| ---- | ---- |
| `/etc/netq/netq.yml` | The NetQ configuration file. This file appears only if you installed either the `netq-apps` package or the NetQ Agent on the system. |
| `/var/log/netqd.log` | The NetQ daemon log file for the NetQ CLI. This log file appears only if you installed the `netq-apps` package on the system. |
| `/var/log/netq-agent.log` | The NetQ Agent log file. This log file appears only if you installed the NetQ Agent on the system.                                   |

## Check NetQ System Installation Status

The `netq show status verbose` command shows the status of NetQ components after installation. Use this command to validate NetQ system readiness:

```
cumulus@netq:~$ netq show status verbose
NetQ Live State: Active
Installation Status: FINISHED
Version: 4.8.0
Installer Version: 4.8.0
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
