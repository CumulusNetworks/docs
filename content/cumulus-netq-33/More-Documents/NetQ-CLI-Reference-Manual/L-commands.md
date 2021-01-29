---
title: L through R Commands
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---

This topic includes all commands that begin with `netq l*`, `netq m*`, `netq n*`, `netq o*`, `netq p*`, `netq q*`, and `netq r*`.

## netq lcm add cl-image

{{<link title="Manage Cumulus Linux and NetQ Images#upload-images" text="Uploads">}} a Cumulus Linux disk image to the LCM repository.

### Syntax

```
netq lcm add cl-image <text-image-path> 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | &lt;text-image-path> | Path to the NetQ image. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm add cl-image /path/to/download/cumulus-linux-4.2.0-mlx-amd64.bin
```

- - -

## netq lcm add credentials

Creates {{<link url="Manage-Switch-Credentials" text="switch access credentials">}} for the specified user.

### Syntax

```
netq lcm add credentials username <text-switch-username> (password <text-switch-password> | ssh-key <text-ssh-key>)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| username | &lt;text-switch-username> | The user's account name. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| password | &lt;text-switch-password> | The password for the user's account. |
| ssh-key | &lt;text-ssh-key> | The public SSH key for the user. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm add credentials username testuser password testpassword 
```

- - -

## netq lcm add default-version

Configures a Cumulus Linux disk image as the {{<link title="Manage Cumulus Linux and NetQ Images/#specify-a-default-upgrade-version" text="default image">}}.

### Syntax

```
netq lcm add default-version cl-images <text-cumulus-linux-version>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-images | &lt;text-cumulus-linux-version> | The version of Cumulus Linux to use as the default. Must be formatted as *X.X.X*. |
| netq-images | &lt;text-netq-version> | The version of NetQ to specify as the default. Must be formatted as *X.X.X*. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm add default-version cl-images 4.3.0 
```

- - -

## netq lcm add netq-image

{{<link title="Manage Cumulus Linux and NetQ Images#upload-images" text="Uploads">}} a NetQ disk image to the LCM repository.

### Syntax

```
netq lcm add netq-image <text-netq-image-path>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | &lt;text-netq-image-path>  | Path to the NetQ image. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm add netq-image /path/to/netq-agent-3.3.0_cl4u32_hash_amd64.deb
```

- - -

## netq lcm add role

Adds a {{<link title="Manage Switch Inventory and Roles/#role-management" text="role">}} to one or more switches.

### Syntax

```
netq add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| switches | &lt;text-switch-hostnames> | A comma-separated list of switches on the network. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| role | superspine, spine, leaf, exit | The switch role. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm add role leaf switches leaf01,leaf02
```

- - -

## netq lcm del cl-image

{{<link title="Manage Cumulus Linux and NetQ Images/#remove-images-from-local-repository" text="Deletes">}} a Cumulus Linux image from the LCM repository.

### Syntax

```
netq lcm del cl-image <text-image-id>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | &lt;text-image-id> | The Cumulus Linux image ID. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Added ability to specify a Cumulus Linux image. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm del cl-image image_c6e812f0081fb03b9b8625a3c0af14eb82c35d79997db4627c54c76c973ce1ce
```

- - -

## netq lcm del credentials

{{<link url="Manage-Switch-Credentials/#remove-switch-credentials" text="Removes">}} the access credentials for switches using the NetQ CLI.

### Syntax

```
netq lcm del credentials
```

### Required Arguments

None

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm del credentials
```

- - -

## netq lcm del netq-image

{{<link title="Manage Cumulus Linux and NetQ Images/#remove-images-from-local-repository" text="Deletes">}} a NetQ image from the LCM repository.

### Syntax

```
netq lcm del netq-image <text-image-id>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | &lt;text-image-id> | The NetQ image ID to delete. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Added ability to specify a NetQ image. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm del netq-image image_68db386683c796d86422f2172c103494fef7a820d003de71647315c5d774f834
```

- - -

## netq lcm discover

Creates a {{<link title="Upgrade Cumulus Linux Using LCM/#upgrade-cumulus-linux-on-switches-without-netq-agent-installed" text="discovery job">}} to locate Cumulus Linux switches on the network.

### Syntax

```
netq lcm discover (ip-range | <text-ip-range> | csv-file <text-csv-file-path>)
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ip-range | &lt;text-ip-range> | A range of IP addresses where your switches are located in the network. |
| csv-file | &lt;text-csv-file-path> | The path to a CSV file containing the IP address, and optionally, the hostname and port for each switch on the network. If the port is blank, NetQ uses switch port 22 by default. They can be in any order you like, but the data must match that order. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@switch:~$ netq lcm discover ip-range 10.0.1.12-14
NetQ Discovery Started with job id: job_scan_006b73a0-60d3-11eb-9e30-f75bf78d6bf1
```

- - -

## netq lcm show cl-images

Displays a summary of the Cumulus Linux images uploaded to the LCM repo on the NetQ appliance or VM.

### Syntax

```
netq lcm show cl-images [<text-image-id>] [json] 
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| &lt;text-image-id> | &lt;text-image-id> | The ID for a specific Cumulus Linux image. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Changed the option to display Cumulus Linux images only. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show cl-images
ID                        Name            CL Version  CPU      ASIC            Last Changed
------------------------- --------------- ----------- -------- --------------- -------------------------
image_cc97be3955042ca4185 cumulus-linux-4 4.2.0       x86_64   VX              Tue Jan  5 22:10:59 2021
7c4d0fe95296bcea3e372b437 .2.0-vx-amd64-1
a535a4ad23ca300d52c3      594775435.dirty
                          zc24426ca.bin
image_b80c410e165ea232cbe cumulus-linux-4 4.2.1       x86_64   VX              Wed Jan 20 16:46:29 2021
b67fd82fea79f05734cd0a32f .2.1-vx-amd64.b
81c148971214bd98b2e0      in
```

- - -

## netq lcm show credentials

Displays the type of {{<link title="Manage Switch Credentials/#view-switch-credentials" text="credentials">}} being used to access switches in the NetQ UI. You can view the details of the credentials using the NetQ CLI.

### Syntax

```
netq lcm show credentials [json] 
```

### Required Arguments

None

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show credentials
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
BASIC                           test             **************   Wed Jan 27 19:08:01 2021
```

- - -

## netq lcm show default-version cl-images

Shows which version of Cumulus Linux has been configured {{<link title="Manage Cumulus Linux and NetQ Images/#specify-a-default-upgrade-version" text="as the default">}}.

### Syntax

```
netq lcm show default-version cl-images [json] 
```

### Required Arguments

None

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show default-version cl-images 
ID                        Name            CL Version  CPU      ASIC            Last Changed
------------------------- --------------- ----------- -------- --------------- -------------------------
image_b80c410e165ea232cbe cumulus-linux-4 4.2.1       x86_64   VX              Wed Jan 20 16:46:29 2021
b67fd82fea79f05734cd0a32f .2.1-vx-amd64.b
81c148971214bd98b2e0      in
```

- - -

## netq lcm show default-version netq-images

Shows which version of NetQ has been configured {{<link title="Manage Cumulus Linux and NetQ Images/#specify-a-default-upgrade-version" text="as the default">}}.

### Syntax

```
netq lcm show default-version netq-images [json] 
```

### Required Arguments

None

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show default-version netq-images 
ID                        Name            NetQ Version  CL Version  CPU      Image Type           Last Changed
------------------------- --------------- ------------- ----------- -------- -------------------- -------------------------
image_d23a9e006641c675ed9 netq-agent_3.3. 3.3.0         cl4u32      x86_64   NETQ_AGENT           Tue Jan  5 22:23:50 2021
e152948a9d1589404e8b83958 0-cl4u32_160939
d53eb0ce7698512e7001      1187.7df4e1d2_a
                          md64.deb
image_68db386683c796d8642 netq-apps_3.3.0 3.3.0         cl4u32      x86_64   NETQ_CLI             Tue Jan  5 22:23:54 2021
2f2172c103494fef7a820d003 -cl4u32_1609391
de71647315c5d774f834      187.7df4e1d2_am
                          d64.deb
```

- - -

## netq lcm show discovery-job

Shows the Cumulus Linux switches on the network located by a {{<link title="Upgrade Cumulus Linux Using LCM/#upgrade-cumulus-linux-on-switches-without-netq-agent-installed" text="discovery job">}}.

### Syntax

```
netq lcm show discovery-job <text-discovery-job-id> [json] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| discovery-job | &lt;text-discovery-job-id> | The ID of the discovery job. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@switch:~$ netq lcm show discovery-job job_scan_921f0a40-5440-11eb-97a2-5b3ed2e556db
Scan COMPLETED

Summary
-------
Start Time: 2021-01-11 19:09:47.441000
End Time: 2021-01-11 19:09:59.890000
Total IPs: 1
Completed IPs: 1
Discovered without NetQ: 0
Discovered with NetQ: 0
Incorrect Credentials: 0
OS Not Supported: 0
Not Discovered: 1


Hostname          IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Discovery Status Upgrade Status
----------------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- ---------------- --------------
N/A               10.0.1.12                 N/A                N/A      N/A         N/A           []                           NOT_FOUND        NOT_UPGRADING
```

- - -

## netq lcm show netq-config

Shows existing NetQ {{<link title="Manage Switch Configurations/#manage-netq-configuration-profiles" text="configuration profiles">}}.

### Syntax

```
netq lcm show netq-config [json] 
```

### Required Arguments

None

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show netq-config
ID                        Name            Default Profile                VRF             WJH       CPU Limit Log Level Last Changed
------------------------- --------------- ------------------------------ --------------- --------- --------- --------- -------------------------
config_profile_3289efda36 NetQ default co Yes                            mgmt            Disable   Disable   info      Tue Jan  5 05:25:31 2021
db4065d56f91ebbd34a523b45 nfig
944fbfd10c5d75f9134d42023
eb2b
config_profile_233c151302 CPU limit 75%   No                             mgmt            Disable   75%       info      Mon Jan 11 19:11:35 2021
eb8ee77d6c27fe2eaca51a9bf
2dfcbfd77d11ff0af92b807de
a0dd
```

- - -

## netq lcm show netq-images

Shows a summary of the NetQ images uploaded to the LCM repo on the NetQ appliance or VM.

### Syntax

```
netq lcm show netq-images [<text-netq-image-id>] [json] 
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| &lt;text-netq-image-id> | &lt;text-netq-image-id> | The ID for a specific NetQ image. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Changed the option to display NetQ images only. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show netq-images 
ID                        Name            NetQ Version  CL Version  CPU      Image Type           Last Changed
------------------------- --------------- ------------- ----------- -------- -------------------- -------------------------
image_d23a9e006641c675ed9 netq-agent_3.3. 3.3.0         cl4u32      x86_64   NETQ_AGENT           Tue Jan  5 22:23:50 2021
e152948a9d1589404e8b83958 0-cl4u32_160939
d53eb0ce7698512e7001      1187.7df4e1d2_a
                          md64.deb
image_68db386683c796d8642 netq-apps_3.3.0 3.3.0         cl4u32      x86_64   NETQ_CLI             Tue Jan  5 22:23:54 2021
2f2172c103494fef7a820d003 -cl4u32_1609391
de71647315c5d774f834      187.7df4e1d2_am
                          d64.deb
```

- - -

## netq lcm show status cl-image

Shows the status of a Cumulus Linux upgrade job.

### Syntax

```
netq lcm show status cl-image <text-lcm-job-id> [json] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | &lt;text-lcm-job-id> | The Cumulus Linux upgrade job ID. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Changed the option to display Cumulus Linux images only. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show status cl-image job_cl_upgrade_a96e0beb59a16b085a7d2b3b5ffd6e5971870aa2903c6df86f26fa908ded2e21
Hostname    CL Version    Backup Status    Backup Start Time         Restore Status      Restore Start Time    Upgrade Status      Upgrade Start Time
----------  ------------  ---------------  ------------------------  ------------------  --------------------  ------------------  --------------------
leaf01      4.2.0         FAILED           Wed Jan 20 19:30:12 2021  SKIPPED_ON_FAILURE  N/A                   SKIPPED_ON_FAILURE  N/A
```

- - -

## netq lcm show status netq-image

Shows the status of a NetQ upgrade job.

### Syntax

```
netq lcm show status netq-image <text-netq-upgrade-job-id> [json] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | &lt;text-netq-upgrade-job-id> | The NetQ upgrade job ID. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Changed the option to display NetQ images only. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ 
```

- - -

## netq lcm show switches

Displays a list of {{<link title="Manage Switch Inventory and Roles" text="all switches">}} known to lifecycle management (LCM).

### Syntax

```
netq lcm show switches [cl-version <text-cumulus-linux-version>] [netq-version <text-netq-version>] [json] 
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cl-version | &lt;text-cumulus-linux-version> | Filter results only for this version of Cumulus Linux. |
| netq-version | &lt;text-netq-version> | Filter results only for this version of NetQ. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show switches 
Hostname          Role       IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Last Changed
----------------- ---------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- -------------------------
fw2                          192.168.200.62            44:38:39:00:01:8E  x86_64   4.2.0       3.3.0-cl4u32~ []                           Thu Jan 21 16:56:01 2021
                                                                                               1610528867.2e
                                                                                               518733
border02          exit       192.168.200.64            44:38:39:00:01:7C  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 27 19:47:39 2021
                                                                                               1610528867.2e
                                                                                               518733
leaf03            leaf       192.168.200.13            44:38:39:00:01:84  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 27 19:49:05 2021
                                                                                               1610528867.2e
                                                                                               518733
spine03           spine      192.168.200.23            44:38:39:00:01:70  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 20 16:41:50 2021
                                                                                               1610528867.2e
                                                                                               518733
leaf01            leaf       192.168.200.11            44:38:39:00:01:7A  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 27 19:46:48 2021
                                                                                               1610528867.2e
                                                                                               518733
fw1                          192.168.200.61            44:38:39:00:01:8C  x86_64   4.2.0       3.3.0-cl4u32~ []                           Thu Jan 21 16:56:09 2021
                                                                                               1610528867.2e
                                                                                               518733
leaf02            leaf       192.168.200.12            44:38:39:00:01:78  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 27 20:11:53 2021
                                                                                               1610528867.2e
                                                                                               518733
leaf04            leaf       192.168.200.14            44:38:39:00:01:8A  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 27 19:48:37 2021
                                                                                               1610528867.2e
                                                                                               518733
spine02           spine      192.168.200.22            44:38:39:00:01:92  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 20 16:41:49 2021
                                                                                               1610528867.2e
                                                                                               518733
spine01           spine      192.168.200.21            44:38:39:00:01:82  x86_64   4.2.0       3.3.0-cl4u32~ []                           Thu Jan 21 17:06:49 2021
                                                                                               1610528867.2e
                                                                                               518733
spine04           spine      192.168.200.24            44:38:39:00:01:6C  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 20 16:41:49 2021
                                                                                               1610528867.2e
                                                                                               518733
border01          exit       192.168.200.63            44:38:39:00:01:74  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 27 19:47:23 2021
                                                                                               1610528867.2e
                                                                                               518733
```

- - -

## netq lcm show upgrade-jobs cl-image

Displays all the Cumulus Linux LCM upgrade jobs.

### Syntax

```
netq lcm show upgrade-jobs cl-image [json] 
```

### Required Arguments

None

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Added ability to specify Cumulus Linux upgrade jobs only. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show upgrade-jobs cl-image
Job ID       Name            CL Version  Pre-Check Status Warnings         Errors       Start Time
------------ --------------- ----------- ---------------- ---------------- ------------ --------------------------
job_cl_upgra test            4.2.1       COMPLETED                                      Wed Jan 20 19:29:41 2021
de_a96e0beb5
9a16b085a7d2
b3b5ffd6e597
1870aa2903c6
df86f26fa908
ded2e21
```

- - -

## netq lcm show upgrade-jobs netq-image

Displays all the NetQ LCM upgrade jobs.

### Syntax

```
netq lcm show upgrade-jobs netq-image [json] 
```

### Required Arguments

None

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Added ability to specify NetQ upgrade jobs only. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm show upgrade-jobs netq-image
```

- - -

## netq lcm upgrade

Upgrades Cumulus Linux and NetQ using LCM.

### Syntax

```
netq lcm upgrade [cl-image] name <text-job-name> cl-version <text-cumulus-linux-version> netq-version <text-netq-version> hostnames <text-switch-hostnames> [run-restore-on-failure] [run-before-after] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| name | &lt;text-job-name> | Name of the upgrade job. You should keep the name 22 characters or shorter so it displays in the UI correctly. |
| cl-version | &lt;text-cumulus-linux-version> | The version of Cumulus Linux image used for the upgrade. |
| netq-version | &lt;text-netq-version> | The version of NetQ image used for the upgrade. |
| hostnames | &lt;text-switch-hostnames> | A comma-separated list of switches to upgrade. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cl-image | none | The Cumulus Linux image name. |
| run-restore-on-failure | none | Enables LCM to restore the previous version of Cumulus Linux or NetQ if the upgrade job fails. |
| run-before-after | none | Runs LCM before and after the upgrade. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Added ability to specify a Cumulus Linux disk image. |
| 3.0.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm upgrade name upgrade-430 cl-version 4.3.0 netq-version 3.3.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-restore-on-failure
```

- - -

## netq lcm upgrade netq-image

Upgrades the NetQ agent and, optionally, the CLI, using LCM.

### Syntax

```
netq lcm upgrade netq-image name <text-job-name> [netq-version <text-netq-version>] [upgrade-cli True | upgrade-cli False] hostnames <text-switch-hostnames> [config_profile <text-config-profile>] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| name | &lt;text-job-name> | Name of the upgrade job. You should keep the name 22 characters or shorter so it displays in the UI correctly. |
| hostnames | &lt;text-switch-hostnames> | A comma-separated list of hosts and switches to upgrade. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| netq-version | &lt;text-netq-version> | The version of NetQ image used for the upgrade. |
| upgrade-cli | True/False | When true, the upgrade job also upgrades the NetQ CLI. |
| config_profile | &lt;text-config-profile> | The name of the configuration profile to load on the upgraded hosts. |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced. |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm upgrade netq-image name NQ330upgrade netq-version 3.3.0 upgrade-cli True hostnames leaf01,leaf02,spine01,spine02
```
