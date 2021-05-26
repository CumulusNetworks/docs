---
title: L through R Commands
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
---

This topic includes all commands that begin with `netq l*`, `netq m*`, `netq n*`, `netq o*`, `netq p*`, `netq q*`, and `netq r*`.

## netq lcm add cl-image

Adds a Cumulus Linux image (.bin file) to the lifecycle management repository. Images must match the version, architecture, and ASIC vendor for the switches you want to upgrade.

Obtain the images from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

### Syntax

```
netq lcm add
    cl-image <text-image-path>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | \<text-image-path\> | Add the Cumulus Linux .bin file from this location. The full path is required, including the file name. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Changed `image` keyword to `cl-image` |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm add cl-image /path/to/download/cumulus-linux-4.2.0-mlnx-amd64.bin
```

### Related Commands

- netq lcm show cl-images
- netq lcm upgrade cl-image
- netq lcm del cl-image
- netq lcm add netq-image

- - -

## netq lcm add credentials

Configures the access credentials for all switches that you plan to manage with the NetQ lifecycle management feature. One set of credentials can be defined. Choose between basic SSH authentication using a username and password or SSH public/private key authentication. You must have sudoer permission to properly configure switches when using the SSH Key method.

{{%notice tip%}}
The default credentials for Cumulus Linux have changed from <!-- vale off -->cumulus/CumulusLinux!<!-- vale on --> to cumulus/cumulus for releases 4.2 and later. For details, read [Cumulus Linux User Accounts]({{<ref "/cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts" >}}).
{{%/notice%}}

### Syntax

```
netq lcm add
    credentials
    username <text-switch-username>
    (password <text-switch-password> | ssh-key <text-ssh-key>)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| credentials | NA | Adds switch credentials for software installation and upgrade management |
| username | \<text-switch-username\> | Specifies the username that is allowed to configure switches |
| password | \<text-switch-password\> | Specifies the password associated with the username that is required to configure switches |
| ssh-key | \<text-ssh-key\> | Specifies the *private* key required to configure switches. The *public* key must already be installed on each switch. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Made `username` a required argument |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm add credentials username cumulus password cumulus
```

### Related Commands

- netq lcm show credentials
- netq lcm del credentials

- - -

## netq lcm add default-version

Configures or changes the Cumulus Linux or NetQ version to use automatically during an upgrade. This value can be overridden during upgrade as needed, but eases the upgrade process for the majority of switches.

### Syntax

Two forms of this command are available; one for Cumulus Linux and the other for NetQ.

```
netq lcm add 
    default-version
    cl-images <text-cumulus-linux-version>

netq lcm add
    default-version
    netq-images <text-netq-version>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| default-version | NA | Specify the default Cumulus Linux or NetQ version for switch upgrades |
| cl-images | \<text-cumulus-linux-version\> | Configure the default Cumulus Linux upgrade image to be this version |
| netq-images | \<text-netq-version\> | Configure the default NetQ upgrade image to be this version |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm add default-version cl-images 4.2.0

cumulus@switch:~$ netq lcm add default-version netq-images 3.3.0
```

### Related Commands

- netq lcm show default-version

- - -

## netq lcm add netq-image

Adds a NetQ image (.deb package) to the lifecycle management repository. Images must match the version, architecture, and operating system for the switches you want to upgrade. For each version of NetQ, you must add the `netq-agent` and `netq-apps` packages.

Obtain the images from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

### Syntax

```
netq lcm add
    netq-image <text-netq-image-path>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | \<text-netq-image-path\> | Add the NetQ Debian package from this location. The full path is required, including the file name. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Changed value of `netq-image` keyword from \<text-image-name\> to \<text-netq-image-name\> |
| 3.1.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-agent_3.3.1-ub18.04u33~1614767175.886b337_amd64.deb
cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-apps_3.3.1-ub18.04u33~1614767175.886b337_amd64.deb
```

### Related Commands

- netq lcm show netq-images
- netq lcm upgrade netq-image
- netq lcm del netq-image
- netq lcm add cl-image

- - -

## netq lcm add role

Assigns or changes a role for one or more switches that defines its placement in a Clos topology and influences the order in which switches are upgraded.

### Syntax

```
netq lcm add
    role (superspine | spine | leaf | exit)
    switches <text-switch-hostnames>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| role | superspine, spine, leaf, exit | Assign this role to the specified switches |
| switches | \<text-switch-hostnames\> | Assign the specified role to the switches with these hostnames. Use a comma-separated list (no spaces) to assign the role to multiple switches at once. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm add role spine switches spine01

cumulus@switch:~$ netq lcm add role leaf switches leaf01,leaf02,leaf03,leaf04
```

### Related Commands

None

- - -

## netq lcm del cl-image

Removes a selected Cumulus Linux image (.bin) from the NetQ lifecycle management repository. Obtain the image identifier using the `netq lcm show cl-image` command with the `json` option.

### Syntax

```
netq lcm del
    cl-image <text-image-id>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | \<text-image-id\> | Remove the Cumulus Linux image with this identifier |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Renamed `image` option to `cl-image` |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show cl-images json
[
    {
        "id": "image_cc97be3955042ca41857c4d0fe95296bcea3e372b437a535a4ad23ca300d52c3",
        "name": "cumulus-linux-4.2.0-vx-amd64-1594775435.dirtyzc24426ca.bin",
        "clVersion": "4.2.0",
        "cpu": "x86_64",
        "asic": "VX",
        "lastChanged": 1609884659654.0
    },
...
cumulus@switch:~$ netq lcm del cl-image image_cc97be3955042ca41857c4d0fe95296bcea3e372b437a535a4ad23ca300d52c3
```

### Related Commands

- netq lcm add cl-image
- netq lcm show cl-images
- netq lcm upgrade cl-image

- - -

## netq lcm del credentials

Removes the access credentials required to upgrade Cumulus Linux or NetQ on switches using the lifecycle management feature. Alternately, use the `netq lcm add credentials` command to change the credentials.

### Syntax

```
netq lcm del
    credentials
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| credentials | \<text-image-id\> | Remove the access credentials used to upgrade switches |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm del credentials
```

### Related Commands

- netq lcm add credentials
- netq lcm show credentials

- - -

## netq lcm del netq-image

Removes a selected NetQ image (.deb) from the NetQ lifecycle management repository. Obtain the image identifier using the `netq lcm show netq-image` command with the `json` option. Note to completely remove a version, you must delete both the `netq-agent` and `netq-apps` images.

### Syntax

```
netq lcm del
    netq-image <text-image-id>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | \<text-image-id\> | Remove the NetQ image with this identifier |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Renamed `image` option to `netq-image` |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show netq-images json
[
    {
        "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
        "name": "netq-agent_3.3.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
        "netqVersion": "3.3.0",
        "clVersion": "cl4u32",
        "cpu": "x86_64",
        "imageType": "NETQ_AGENT",
        "lastChanged": 1609885430638.0
    },
...

cumulus@switch:~$ netq lcm del netq-image image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001

cumulus@switch:~$ netq lcm del netq-image image_68db386683c796d86422f2172c103494fef7a820d003de71647315c5d774f834
```

### Related Commands

- netq lcm add netq-image
- netq lcm show netq-images
- netq lcm upgrade netq-image

- - -

## netq lcm discover

Searches for switches that do not have NetQ installed based on IP addresses or from a file. Once found you can add them to the lifecycle management repository and upgrade Cumulus Linux. Use the `netq lcm show discovery-job` command to view the results of this command.

### Syntax

```
netq lcm discover
    (ip-range <text-ip-range> | csv-file <text-csv-file-path>)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ip-range | \<text-ip-range\> | Search for switches with this IP address or within this address range. Ranges can be contiguous, for example 192.168.0.24-64, or non-contiguous, for example 192.168.0.24-64,128-190,225, but they must be contained within a single subnet. A maximum of 50 addresses can be included in an address range. |
| csv-file | \<text-csv-file-path\> | Search for switches in this CSV file containing the IP address, and optionally, the hostname and port for each switch on the network. If the port is blank, NetQ uses switch port 22 by default. They can be in any order you like, but the data must match that order. |

### Options

None

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm discover ip-range 10.0.1.12 
NetQ Discovery Started with job id: job_scan_4f3873b0-5526-11eb-97a2-5b3ed2e556db
```

### Related Commands

- netq lcm show discovery-job

- - -

## netq lcm show cl-images

Displays all Cumulus Linux images in the lifecycle management repository. 

{{<notice tip>}}
The <code>json</code> option is useful when you are looking to capture the image identifier because it is not broken into pieces within a table column.
{{</notice>}}

### Syntax

```
netq lcm show cl-images
    [<text-image-id>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-images | NA | Display all Cumulus Linux images in the lifecycle management repository |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-image-id\> | Only display Cumulus Linux image with this identifier |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Renamed `images` argument to `cl-images` |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show cl-images
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

```
cumulus@switch:~$ netq lcm show cl-images json
[
    {
        "id": "image_cc97be3955042ca41857c4d0fe95296bcea3e372b437a535a4ad23ca300d52c3",
        "name": "cumulus-linux-4.2.0-vx-amd64-1594775435.dirtyzc24426ca.bin",
        "clVersion": "4.2.0",
        "cpu": "x86_64",
        "asic": "VX",
        "lastChanged": 1609884659654.0
    },
    {
        "id": "image_b80c410e165ea232cbeb67fd82fea79f05734cd0a32f81c148971214bd98b2e0",
        "name": "cumulus-linux-4.2.1-vx-amd64.bin",
        "clVersion": "4.2.1",
        "cpu": "x86_64",
        "asic": "VX",
        "lastChanged": 1611161189714.0
    }
]
```

### Related Commands

- netq lcm add cl-images
- netq lcm del cl-images

- - -

## netq lcm show credentials

Displays the switch access credentials method and values currently configured.

### Syntax

```
netq lcm show credentials
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| credentials | NA | Display current switch access credentials configuration |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show credentials 
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
BASIC                           cumulus          **************   Wed Jan 27 19:24:03 2021
```

```
cumulus@switch:~$ netq lcm show credentials
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
SSH              <your-SSH-key>                                   Tue Apr 28 19:08:52 2020
```

### Related Commands

- netq lcm add credentials
- netq lcm del credentials

- - -

## netq lcm show default-version

Displays the default Cumulus Linux or NetQ version specified for upgrades.

### Syntax

Two forms of this command are available depending on whether you want to view the default version for Cumulus Linux or for NetQ.

```
netq lcm show default-version 
    cl-images
    [json]

netq lcm show default-version
    netq-images
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-images | NA | Display configuration of Cumulus Linux default upgrade version |
| netq-images | NA | Display configuration of NetQ default upgrade version |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show default-version cl-images 
ID                        Name            CL Version  CPU      ASIC            Last Changed
------------------------- --------------- ----------- -------- --------------- -------------------------
image_b80c410e165ea232cbe cumulus-linux-4 4.2.1       x86_64   VX              Tue Jan 26 22:32:11 2021
b67fd82fea79f05734cd0a32f .2.1-vx-amd64.b
81c148971214bd98b2e0      in
```

```
cumulus@switch:~$ netq lcm show default-version netq-images
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

### Related Commands

- netq lcm add default-version
- netq lcm del default-version
- netq lcm add cl-image
- netq lcm add netq-image

- - -

## netq lcm show discovery-job

Displays the results of a switch discovery job, including a summary of the job itself and information about any switches discovered, including hostname, IP address, MAC address, CPU, Cumulus Linux and NetQ versions, configuration profile, discovery status and upgrade status.

### Syntax

```
netq lcm show
    discovery-job <text-discovery-job-id>
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| discovery-job | \<text-discovery-job-id\> | Display results of discovery job with this identifier |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm discover ip-range 192.168.200.62
NetQ Discovery Started with job id: job_scan_c1d5e060-720e-11eb-9e30-f75bf78d6bf1

cumulus@switch:~$ netq lcm show discovery-job job_scan_c1d5e060-720e-11eb-9e30-f75bf78d6bf1
Scan COMPLETED

Summary
-------
Start Time: 2021-02-18 17:29:18.640000
End Time: 1970-01-01 00:00:00.000000
Total IPs: 1
Completed IPs: 1
Discovered without NetQ: 0
Discovered with NetQ: 1
Incorrect Credentials: 0
OS Not Supported: 0
Not Discovered: 0


Hostname          IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Discovery Status Upgrade Status
----------------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- ---------------- --------------
fw2               192.168.200.62            44:38:39:00:01:8E  x86_64   4.2.0       3.3.0         []                           WITH_NETQ        NOT_UPGRADING
```

### Related Commands

- netq lcm discover

- - -

## netq lcm show netq-config

Displays the configuration of all NetQ configuration profiles created in the NetQ UI, including the name and identifier, which is the default profile, VRF used, whether What Just Happened or CPU usage limiting is enabled, and logging level.

### Syntax

```
netq lcm show netq-config
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-config | NA | Display results of discovery job with this identifier |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show netq-config 
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

### Related Commands

None

- - -

## netq lcm show netq-images

Displays all NetQ images in the lifecycle management repository.

{{<notice tip>}}
The <code>json</code> option is useful when you are looking to capture the image identifier because it is not broken into pieces within a table column.
{{</notice>}}

### Syntax

```
netq lcm show netq-images
    [<text-netq-image-id>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-images | NA | Display all NetQ images in the lifecycle management repository |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-netq-image-id\> | Only display  the NetQ image with this identifier |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Renamed `images` argument to `netq-images` |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show netq-images 
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

```
cumulus@switch:~$ netq lcm show netq-images json
[
    {
        "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
        "name": "netq-agent_3.3.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
        "netqVersion": "3.3.0",
        "clVersion": "cl4u32",
        "cpu": "x86_64",
        "imageType": "NETQ_AGENT",
        "lastChanged": 1609885430638.0
    },
    {
        "id": "image_68db386683c796d86422f2172c103494fef7a820d003de71647315c5d774f834",
        "name": "netq-apps_3.3.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
        "netqVersion": "3.3.0",
        "clVersion": "cl4u32",
        "cpu": "x86_64",
        "imageType": "NETQ_CLI",
        "lastChanged": 1609885434704.0
    }
]
```

### Related Commands

- netq lcm add netq-images
- netq lcm del netq-images

- - -

## netq lcm show status

Displays status of Cumulus Linux or NetQ image upgrade jobs.

### Syntax

Two forms of this command are available; one to display Cumulus Linux job status and one to display NetQ job status. Use the `netq lcm show upgrade-jobs` to obtain the job identifier.

```
netq lcm show status
    cl-image <text-lcm-job-id>
    [json]

netq lcm show status
    netq-image <text-netq-upgrade-job-id>
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | \<text-lcm-job-id\> | Display the status of the Cumulus Linux upgrade job with this identifier |
| netq-image | \<text-netq-upgrade-job-id\> | Display the status of the NetQ upgrade job with this identifier |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Added ability to view NetQ job status with the change of the `images` argument to `cl-images` and `netq-images` |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show upgrade-jobs cl-image json
[
    {
        "jobId": "job_cl_upgrade_a96e0beb59a16b085a7d2b3b5ffd6e5971870aa2903c6df86f26fa908ded2e21",
        "name": "test",
        "clVersion": "4.2.1",
        "pre-checkStatus": "COMPLETED",
        "warnings": "",
        "errors": "",
        "startTime": 1611170981846.0
    },
    {
        "jobId": "job_cl_upgrade_9c5e3b4b76f490e6531c34faf52907bda46648701b3f7c0289b96c5d76af53eb",
        "name": "UpgradeJustOne",
        "clVersion": "4.2.1",
        "pre-checkStatus": "COMPLETED",
        "warnings": "",
        "errors": "",
        "startTime": 1613595515152.0
    }
]
cumulus@switch:~$ netq lcm show status cl-image job_cl_upgrade_a96e0beb59a16b085a7d2b3b5ffd6e5971870aa2903c6df86f26fa908ded2e21
Hostname    CL Version    Backup Status    Backup Start Time         Restore Status      Restore Start Time    Upgrade Status      Upgrade Start Time
----------  ------------  ---------------  ------------------------  ------------------  --------------------  ------------------  --------------------
leaf01      4.2.0         FAILED           Wed Jan 20 19:30:12 2021  SKIPPED_ON_FAILURE  N/A                   SKIPPED_ON_FAILURE  N/A
```

```
cumulus@switch:~$ netq lcm show upgrade-jobs netq-image json
[
    {
        "jobId": "job_netq_install_7152a03a8c63c906631c3fb340d8f51e70c3ab508d69f3fdf5032eebad118cc7",
        "name": "Leaf01-02 to NetQ330",
        "netqVersion": "3.3.0",
        "overallStatus": "FAILED",
        "pre-checkStatus": "COMPLETED",
        "warnings": [],
        "errors": [],
        "startTime": 1611863290557.0
    }
]

cumulus@switch:~$ netq lcm show status netq-image job_netq_install_7152a03a8c63c906631c3fb340d8f51e70c3ab508d69f3fdf5032eebad118cc7
NetQ Upgrade FAILED

Upgrade Summary
---------------
Start Time: 2021-01-28 19:48:10.557000
End Time: 2021-01-28 19:48:17.972000
Upgrade CLI: True
NetQ Version: 3.3.0
Pre Check Status COMPLETED
Precheck Task switch_precheck COMPLETED
	Warnings: []
	Errors: []
Precheck Task version_precheck COMPLETED
	Warnings: []
	Errors: []
Precheck Task config_precheck COMPLETED
	Warnings: []
	Errors: []


Hostname          CL Version  NetQ Version  Prev NetQ Ver Config Profile               Status           Warnings         Errors       Start Time
                                            sion
----------------- ----------- ------------- ------------- ---------------------------- ---------------- ---------------- ------------ --------------------------
leaf01            4.2.1       3.3.0         3.2.1         ['NetQ default config']      FAILED           []               ["Unreachabl Thu Jan 28 19:48:10 2021
                                                                                                                         e at Invalid
                                                                                                                         /incorrect u
                                                                                                                         sername/pass
                                                                                                                         word. Skippi
                                                                                                                         ng remaining
                                                                                                                         10 retries t
                                                                                                                         o prevent ac
                                                                                                                         count lockou
                                                                                                                         t: Warning:
                                                                                                                         Permanently
                                                                                                                         added '192.1
                                                                                                                         68.200.11' (
                                                                                                                         ECDSA) to th
                                                                                                                         e list of kn
                                                                                                                         own hosts.\r
                                                                                                                         \nPermission
                                                                                                                         denied,
                                                                                                                         please try a
                                                                                                                         gain."]
leaf02            4.2.1       3.3.0         3.2.1         ['NetQ default config']      FAILED           []               ["Unreachabl Thu Jan 28 19:48:10 2021
                                                                                                                         e at Invalid
                                                                                                                         /incorrect u
                                                                                                                         sername/pass
                                                                                                                         word. Skippi
                                                                                                                         ng remaining
                                                                                                                         10 retries t
                                                                                                                         o prevent ac
                                                                                                                         count lockou
                                                                                                                         t: Warning:
                                                                                                                         Permanently
                                                                                                                         added '192.1
                                                                                                                         68.200.12' (
                                                                                                                         ECDSA) to th
                                                                                                                         e list of kn
                                                                                                                         own hosts.\r
                                                                                                                         \nPermission
                                                                                                                         denied,
                                                                                                                         please try a
                                                                                                                         gain."]
```

### Related Commands

- netq lcm show upgrade-jobs

- - -

## netq lcm show switches

Displays information about switches monitored by NetQ and contained in the lifecycle management repository, including their hostnames, any assigned role, IP and MAC addresses, CPU architecture, Cumulus Linux and NetQ versions, and NetQ configuration profiles. Filter the output by Cumulus Linux or NetQ version running on the switch.

### Syntax

```
netq lcm show switches
    [cl-version <text-cumulus-linux-version>]
    [netq-version <text-netq-version>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| switches | NA | Display information about switches known to the lifecycle management feature |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cl-version | \<text-cumulus-linux-version\> | Only display switches running this version of the Cumulus Linux OS |
| netq-version | \<text-netq-version\> | Only display switches running this version of NetQ |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Renamed the `version` option to `cl-version` and added `netq-version` option to enable filtering by NetQ version |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show switches
Hostname          Role       IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Last Changed
----------------- ---------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- -------------------------
fw2                          192.168.200.62            44:38:39:00:01:8E  x86_64   4.2.0       3.3.0-cl4u32~ []                           Thu Jan 21 16:56:01 2021
                                                                                               1610528867.2e
                                                                                               518733
border02                     192.168.200.64            44:38:39:00:01:7C  x86_64   4.2.0       3.3.0-cl4u32~ []                           Thu Feb 18 16:42:52 2021
                                                                                               1610528867.2e
                                                                                               518733
leaf03                       192.168.200.13            44:38:39:00:01:84  x86_64   4.2.0       3.3.0-cl4u32~ []                           Thu Feb 18 16:42:28 2021
                                                                                               1610528867.2e
                                                                                               518733
spine03                      192.168.200.23            44:38:39:00:01:70  x86_64   4.2.0       3.3.0-cl4u32~ []                           Wed Jan 20 16:41:50 2021
                                                                                               1610528867.2e
                                                                                               518733
...
```

```
cumulus@switch:~$ netq lcm show switches cl-version 4.2.1
Hostname          Role       IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Last Changed
----------------- ---------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- -------------------------
leaf02                       192.168.200.12            44:38:39:00:01:78  x86_64   4.2.1       3.3.0-cl4u32~ []                           Thu Feb 18 21:33:37 2021
                                                                                               1609391187.7d
                                                                                               f4e1d2
```

### Related Commands

None

- - -

## netq lcm show upgrade-jobs

Displays a history of all Cumulus Linux or NetQ upgrade jobs, including the job identifier and name, Cumulus Linux or NetQ version, pre-check status, warnings and errors, and start the job started. The NetQ upgrade jobs also show the overall status.

### Syntax

Two forms of this command are available; one for Cumulus Linux and one for NetQ.

```
netq lcm show upgrade-jobs
    cl-image
    [json]

netq lcm show upgrade-jobs
    netq-image
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| upgrade-jobs | NA | Display upgrade job history |
| cl-image | NA | Display upgrade job history for Cumulus Linux |
| netq-image | NA | Display upgrade job history for NetQ |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| json | NA | Display the output in JSON file format instead of default on-screen text format |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.3.0 | Added the `cl-image` and `netq-image` options to enable display of Cumulus Linux or NetQ upgrade job history |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@switch:~$ netq lcm show upgrade-jobs cl-image 
Job ID       Name            CL Version  Pre-Check Status Warnings         Errors       Start Time
------------ --------------- ----------- ---------------- ---------------- ------------ --------------------------
job_cl_upgra test            4.2.1       COMPLETED                                      Wed Jan 20 19:29:41 2021
de_a96e0beb5
9a16b085a7d2
b3b5ffd6e597
1870aa2903c6
df86f26fa908
ded2e21
job_cl_upgra UpgradeJustOne  4.2.1       COMPLETED                                      Wed Feb 17 20:58:35 2021
de_9c5e3b4b7
6f490e6531c3
4faf52907bda
46648701b3f7
c0289b96c5d7
6af53eb

cumulus@switch:~$ netq lcm show upgrade-jobs cl-image json
[
    {
        "jobId": "job_cl_upgrade_a96e0beb59a16b085a7d2b3b5ffd6e5971870aa2903c6df86f26fa908ded2e21",
        "name": "test",
        "clVersion": "4.2.1",
        "pre-checkStatus": "COMPLETED",
        "warnings": "",
        "errors": "",
        "startTime": 1611170981846.0
    },
    {
        "jobId": "job_cl_upgrade_9c5e3b4b76f490e6531c34faf52907bda46648701b3f7c0289b96c5d76af53eb",
        "name": "UpgradeJustOne",
        "clVersion": "4.2.1",
        "pre-checkStatus": "COMPLETED",
        "warnings": "",
        "errors": "",
        "startTime": 1613595515152.0
    }
]
```

```
cumulus@switch:~$ netq lcm show upgrade-jobs netq-image 
Job ID       Name            NetQ Version  Overall Status   Pre-Check Status Warnings         Errors       Start Time
------------ --------------- ------------- ---------------- ---------------- ---------------- ------------ --------------------------
job_netq_ins Leaf01-02 to Ne 3.3.0         FAILED           COMPLETED        []               []           Thu Jan 28 19:48:10 2021
tall_7152a03 tQ330
a8c63c906631
c3fb340d8f51
e70c3ab508d6
9f3fdf5032ee
bad118cc7

cumulus@switch:~$ netq lcm show upgrade-jobs netq-image json
[
    {
        "jobId": "job_netq_install_7152a03a8c63c906631c3fb340d8f51e70c3ab508d69f3fdf5032eebad118cc7",
        "name": "Leaf01-02 to NetQ330",
        "netqVersion": "3.3.0",
        "overallStatus": "FAILED",
        "pre-checkStatus": "COMPLETED",
        "warnings": [],
        "errors": [],
        "startTime": 1611863290557.0
    }
]
```

### Related Commands

- netq lcm show status

- - -
