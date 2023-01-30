---
title: lcm
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
---
<!-- vale NVIDIA.HeadingTitles = NO -->
<!-- vale off -->
## netq lcm add cl-image
<!-- vale on -->

Adds a Cumulus Linux image (.bin file) to the lifecycle management repository. Images must match the version, architecture, and ASIC vendor for the switches you want to upgrade. For detailed instructions, see {{<link title="Upgrade Cumulus Linux Using LCM">}}.

### Syntax

```
netq lcm add
    cl-image <text-image-path>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | \<text-image-path\> | Add the Cumulus Linux .bin file from this location. You must specify the full path, including the file name. |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm add cl-image /path/to/download/cumulus-linux-4.2.0-mlnx-amd64.bin
```

### Related Commands

- ```netq lcm show cl-images```
- ```netq lcm upgrade cl-image```
- ```netq lcm del cl-image```
- ```netq lcm add netq-image```

- - -

## netq lcm add credentials

Configures the access credentials for all switches that you plan to manage with the NetQ lifecycle management feature. You can define set of credentials. Choose between basic SSH authentication using a username and password or SSH public/private key authentication. You must have sudoer permission to properly configure switches when using the SSH key method.

{{<notice tip>}}
The default credentials for Cumulus Linux have changed from <!-- vale off -->cumulus/CumulusLinux!<!-- vale on --> to cumulus/cumulus for releases 4.2 and later. For details, read <a href="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts/">Cumulus Linux User Accounts</a>.
{{</notice>}}

### Syntax

```
netq lcm add credentials
    username <text-switch-username>
    (password <text-switch-password> | ssh-key <text-ssh-key>)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| credentials | NA | Adds switch credentials for software installation and upgrade management |
| username | \<text-switch-username\> | Specifies the username for the user who can configure switches |
| password | \<text-switch-password\> | Specifies the password associated with the username so that user can configure switches |
| ssh-key | \<text-ssh-key\> | Specifies the *private* key required to configure switches. You must have already installed the *public* key on each switch. |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm add credentials username cumulus password cumulus
```

### Related Commands

- ```netq lcm show credentials```
- ```netq lcm del credentials```

- - -

<!-- vale off -->
## netq lcm add default-version
<!-- vale on -->

Configures or changes the Cumulus Linux or NetQ version to use automatically during an upgrade. This value can be overridden during upgrade as needed, but eases the upgrade process for the majority of switches.

### Syntax

Two forms of this command are available: one for Cumulus Linux and the other for NetQ.

```
netq lcm add default-version
    cl-images <text-cumulus-linux-version>

netq lcm add default-version
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

### Sample Usage

```
cumulus@switch:~$ netq lcm add default-version cl-images 5.3.0

cumulus@switch:~$ netq lcm add default-version netq-images 4.4.0
```

### Related Commands

- ```netq lcm show default-version```

- - -

## netq lcm add netq-image

Adds a NetQ image (.deb package) to the lifecycle management repository. Images must match the version, architecture, and operating system for the switches you want to upgrade. For each version of NetQ, you must add the `netq-agent` and `netq-apps` packages. For more information, see {{<link title="NetQ and Network OS Images">}}.

### Syntax

```
netq lcm add
    netq-image <text-netq-image-path>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | \<text-netq-image-path\> | Add the NetQ Debian package from this location. You need to specify the full path, including the file name. |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-agent_4.0.0-ub18.04u33~1614767175.886b337_amd64.deb
cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-apps_4.0.0-ub18.04u33~1614767175.886b337_amd64.deb
```

### Related Commands

- ```netq lcm show netq-images```
- ```netq lcm upgrade netq-image```
- ```netq lcm del netq-image```
- ```netq lcm add cl-image```

- - -

## netq lcm add role

Assigns or changes a role for one or more switches that defines its placement in a Clos topology and influences the order in which you can upgrade switches.

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
| switches | \<text-switch-hostnames\> | Assign the specified role to the switches with these hostnames. Use a comma-separated list (no spaces) to assign the role to multiple switches at the same time. |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm add role spine switches spine01

cumulus@switch:~$ netq lcm add role leaf switches leaf01,leaf02,leaf03,leaf04
```

### Related Commands

None

- - -
## netq lcm attach credentials

### Syntax

### Required Arguments

### Options

### Sample Usage

### Related Commands

- netq lcm show credentials

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

- ```netq lcm add cl-image```
- ```netq lcm show cl-images```
- ```netq lcm upgrade cl-image```

- - -

## netq lcm del credentials

Removes the access credentials required to upgrade Cumulus Linux or NetQ on switches using the lifecycle management feature. Alternately, use the `netq lcm add credentials` command to change the credentials.

### Syntax

```
netq lcm del credentials
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| credentials | \<text-image-id\> | Remove the access credentials used to upgrade switches |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm del credentials
```

### Related Commands

- ```netq lcm add credentials```
- ```netq lcm show credentials```

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

### Sample Usage

```
cumulus@switch:~$ netq lcm show netq-images json
[
    {
        "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
        "name": "netq-agent_4.0.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
        "netqVersion": "4.0.0",
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

- ```netq lcm add netq-image```
- ```netq lcm show netq-images```
- ```netq lcm upgrade netq-image```

- - -
## netq lcm detach credentials
### Syntax

### Required Arguments

### Options

### Sample Usage

### Related Commands

- netq lcm show credentials

- - -

## netq lcm discover

Searches for switches that do not have NetQ installed based on IP addresses or from a file. After discovery, you can add them to the lifecycle management repository and upgrade Cumulus Linux. Use the `netq lcm show discovery-job` command to view the results of this command.

### Syntax

```
netq lcm discover
    (ip-range <text-ip-range> | csv-file <text-csv-file-path>)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ip-range | \<text-ip-range\> | Search for switches with this IP address or within this address range. Ranges can be contiguous, for example 192.168.0.24-64, or non-contiguous, for example 192.168.0.24-64,128-190,225, but they must reside within a single subnet. You can include a maximum of 50 addresses in an address range. |
| csv-file | \<text-csv-file-path\> | Search for switches in this CSV file containing the IP address, and optionally, the hostname and port for each switch on the network. If the port is blank, NetQ uses switch port 22 by default. They can be in any order you like, but the data must match that order. |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm discover ip-range 10.0.1.12 
NetQ Discovery Started with job id: job_scan_4f3873b0-5526-11eb-97a2-5b3ed2e556db
```

### Related Commands

- ```netq lcm show discovery-job```

- - -
## netq lcm edit credentials
### Syntax

### Required Arguments

### Options

### Sample Usage

### Related Commands

- netq lcm show credentials

- - -
## netq lcm install netq-image

### Syntax

```
netq lcm install netq-image 
    job-name <text-job-name> 
    netq-version <text-netq-version> 
    upgrade-cli [ True | False] 
    hostname <text-switch-hostname> 
    ip <text-switch-ip> 
    cpu_arch <text-cpu-arch> 
    cl_version <text-cumulus-linux-version> 
    [config_profile <text-config-profile>]
```

- - -
## netq lcm show cl-images

Displays all Cumulus Linux images in the lifecycle management repository. 

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
| json | NA | Display the output in JSON format |

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

- ```netq lcm add cl-images```
- ```netq lcm del cl-images```

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
| json | NA | Display the output in JSON format |

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

- ```netq lcm add credentials```
- ```netq lcm del credentials```

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
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq lcm show default-version cl-images 
ID                        Name            CL Version  CPU      ASIC            Last Changed
------------------------- --------------- ----------- -------- --------------- -------------------------
image_b80c410e165ea232cbe cumulus-linux-4 4.2.1       x86_64   VX              Tue Jan 26 22:32:11 2021
b67fd82fea79f05734cd0a32f .2.1-vx-amd64.b
81c148971214bd98b2e0      in
```
### Related Commands

- ```netq lcm add default-version```
- ```netq lcm del default-version```
- ```netq lcm add cl-image```
- ```netq lcm add netq-image```

- - -

## netq lcm show discovery-job

Displays the results of a switch discovery job, including a summary of the job itself and information about any switches discovered, including hostname, IP address, MAC address, CPU, Cumulus Linux and NetQ versions, configuration profile, discovery status, and upgrade status.

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
| json | NA | Display the output in JSON format |

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
fw2               192.168.200.62            44:38:39:00:01:8E  x86_64   4.2.0       4.0.0         []                           WITH_NETQ        NOT_UPGRADING
```

### Related Commands

- ```netq lcm discover```

- - -

## netq lcm show netq-config

Displays the configuration of all NetQ configuration profiles created in the NetQ UI, including the name and identifier, which is the default profile, VRF used, whether you enabled What Just Happened or CPU usage limiting, and logging level.

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
| json | NA | Display the output in JSON format |

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
| NA | \<text-netq-image-id\> | Only display the NetQ image with this identifier |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq lcm show netq-images json
[
    {
        "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
        "name": "netq-agent_4.0.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
        "netqVersion": "4.0.0",
        "clVersion": "cl4u32",
        "cpu": "x86_64",
        "imageType": "NETQ_AGENT",
        "lastChanged": 1609885430638.0
    },
    {
        "id": "image_68db386683c796d86422f2172c103494fef7a820d003de71647315c5d774f834",
        "name": "netq-apps_4.0.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
        "netqVersion": "4.0.0",
        "clVersion": "cl4u32",
        "cpu": "x86_64",
        "imageType": "NETQ_CLI",
        "lastChanged": 1609885434704.0
    }
]
```

### Related Commands

- ```netq lcm add netq-images```
- ```netq lcm del netq-images```

- - -

## netq lcm show status

Displays status of Cumulus Linux or NetQ image upgrade jobs.

### Syntax

Two forms of this command are available: one for Cumulus Linux and one for NetQ. Run `netq lcm show upgrade-jobs` to obtain the job identifier.

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
| json | NA | Display the output in JSON format |

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
### Related Commands

- ```netq lcm show upgrade-jobs```

- - -

## netq lcm show switches

Displays information about switches monitored by NetQ and contained in the lifecycle management repository, including their hostnames, any assigned role, IP and MAC addresses, CPU architecture, Cumulus Linux and NetQ versions, and NetQ configuration profiles. Filter the output by Cumulus Linux or NetQ version running on the switch.

### Syntax

<!-- vale off -->
```
netq lcm show switches
    [cl-version <text-cumulus-linux-version>]
    [netq-version <text-netq-version>]
    [json]
```
<!-- vale on -->

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| switches | NA | Display information about switches known to the lifecycle management feature |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cl-version | \<text-cumulus-linux-version\> | Only display switches running this version of the Cumulus Linux OS |
| netq-version | \<text-netq-version\> | Only display switches running this version of NetQ |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq lcm show switches cl-version 4.2.1
Hostname          Role       IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Last Changed
----------------- ---------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- -------------------------
leaf02                       192.168.200.12            44:38:39:00:01:78  x86_64   4.2.1       4.0.0-cl4u32~ []                           Thu Feb 18 21:33:37 2021
                                                                                               1609391187.7d
                                                                                               f4e1d2
```

### Related Commands

None

- - -

<!-- vale off -->
## netq lcm show upgrade-jobs
<!-- vale on -->

Displays a history of all Cumulus Linux or NetQ upgrade jobs, including the job identifier and name, Cumulus Linux or NetQ version, pre-check status, warnings and errors, and time the job started. The NetQ upgrade jobs also show the overall status.

### Syntax

Two forms of this command are available: one for Cumulus Linux and one for NetQ.

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
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@switch:~$ netq lcm show upgrade-jobs netq-image 
Job ID       Name            NetQ Version  Overall Status   Pre-Check Status Warnings         Errors       Start Time
------------ --------------- ------------- ---------------- ---------------- ---------------- ------------ --------------------------
job_netq_ins Leaf01-02 to Ne 4.0.0         FAILED           COMPLETED        []               []           Thu Jan 28 19:48:10 2021
tall_7152a03 tQ330
a8c63c906631
c3fb340d8f51
e70c3ab508d6
9f3fdf5032ee
bad118cc7
```

### Related Commands

- ```netq lcm show status```
- - -
## netq lcm upgrade cl-image

Upgrades Cumulus Linux on one or more switches in your network

### Syntax

```
netq lcm upgrade 
    [cl-image] 
    job-name <text-job-name> 
    cl-version <text-cumulus-linux-version> 
    netq-version <text-netq-version> 
    hostnames <text-switch-hostnames> 
    [run-restore-on-failure] 
    [run-snapshot-before-after]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| job-name | \<text-job-name\> | Name for the upgrade |
| cl-version | \<text-cumulus-linux-version\> | |
| netq-version | \<text-netq-version\> | |
| hostnames | \<text-switch-hostnames\> | Comma-separated list of the hostname(s) to be upgraded |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cl-image | NA |  |
| run-restore-on-failure | NA | Restore the previous version of Cumulus Linux if the upgrade fails (recommended) |
| run-snapshot-before-after | NA | Generate a network snapshot before and after the upgrade |

### Sample Usage


### Related Commands

- netq lcm show discovery-job

- - -
## netq lcm upgrade netq-image

### Syntax

```
netq lcm upgrade netq-image 
    job-name <text-job-name> 
    [netq-version <text-netq-version>] 
    [upgrade-cli True | upgrade-cli False] 
    hostnames <text-switch-hostnames> 
    [config_profile <text-config-profile>]
 ```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | NA |  |
| job-name | \<text-job-name\> | Name for the upgrade |
| hostnames | \<text-switch-hostnames\> | Comma-separated list of the hostname(s) to be upgraded |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| netq-version | <text-netq-version\> |  |
| upgrade-cli | True, False | Upgrade the NetQ CLI as part of the upgrade (True) |
| config_profile | <text-config-profile\> |  |

### Sample Usage

### Related Commands

- netq lcm show upgrade-jobs netq-image 

- - -