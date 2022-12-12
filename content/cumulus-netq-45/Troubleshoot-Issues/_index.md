---
title: Troubleshoot NetQ
author: NVIDIA
weight: 1050
subsection: true
toc: 2
---

This page describes how to generate a support file for the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA support team">}} to help troubleshoot issues with NetQ itself.
## Generate a Support File

The `opta-support` command generates an archive of useful information for troubleshooting issues with NetQ. It provides information about the NetQ Platform configuration and runtime statistics as well as output from the `docker ps` command.

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
## Browse Configuration and Log Files

The following configuration and log files contain information that can help with troubleshooting:

| File | Description |
| ---- | ---- |
| `/etc/netq/netq.yml` | The NetQ configuration file. This file appears only if you installed either the `netq-apps` package or the NetQ Agent on the system. |
| `/var/log/netqd.log` | The NetQ daemon log file for the NetQ CLI. This log file appears only if you installed the `netq-apps` package on the system. |
| `/var/log/netq-agent.log` | The NetQ Agent log file. This log file appears only if you installed the NetQ Agent on the system.                                   |
