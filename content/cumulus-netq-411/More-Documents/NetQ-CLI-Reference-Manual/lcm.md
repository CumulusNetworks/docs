---
title: lcm
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
<!-- vale NVIDIA.HeadingTitles = NO -->
<!-- vale off -->
## netq lcm add cl-image
<!-- vale on -->

Adds a Cumulus Linux image (.bin file) to the lifecycle management repository. Images must match the version, architecture, and ASIC vendor for the switches you want to upgrade. For detailed instructions, see {{<link title="Upgrade Cumulus Linux">}}.

### Syntax

```
netq lcm add cl-image <text-cl-image-path>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | \<text-cl-image-path\> | Add the Cumulus Linux .bin file from this location. You must specify the full path, including the file name. |

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

Configures the access credentials for all switches that you plan to manage with the NetQ lifecycle management feature. You can choose between basic authentication using a username and password or SSH public/private key authentication. You must have sudoer permission to configure switches when using the SSH key method.

To obtain the access profile's name, run `netq lcm show credentials`.

{{<notice tip>}}
The default credentials for Cumulus Linux have changed from <!-- vale off -->cumulus/CumulusLinux!<!-- vale on --> to cumulus/cumulus for releases 4.2 and later. For details, read <a href="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts/">Cumulus Linux User Accounts</a>.
{{</notice>}}

### Syntax

```
netq lcm add credentials
    profile_name <text-switch-profile-name>
    username <text-switch-username>
    (password <text-switch-password> | ssh-key <text-ssh-key>)
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| profile_name | \<text-switch-profile-name\> | Specifies the access profile's name |
| username | \<text-switch-username\> | Specifies the username for the user who can configure switches |
| password | \<text-switch-password\> | Specifies the password associated with the username so that user can configure switches |
| ssh-key | \<text-ssh-key\> | Specifies the *private* key required to configure switches. You must have already installed the *public* key on each switch. |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm add credentials profile_name n-2000 username cumulus password cumulus
```

### Related Commands

- `netq lcm attach credentials`
- `netq lcm show credentials`
- `netq lcm del credentials`

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
cumulus@switch:~$ netq lcm add default-version cl-images 5.9.1

cumulus@switch:~$ netq lcm add default-version netq-images 4.10.1
```

### Related Commands

- ```netq lcm show default-version```

- - -

## netq lcm add netq-config

Creates a NetQ agent configuration profile.

### Syntax

```
netq lcm add netq-config 
    config-profile-name <text-config-profile> 
    access-key <text-access-key> 
    secret-key <text-secret-key> 
    [cpu-limit <text-cpu-limit>] 
    [log-level error | log-level warn | log-level info | log-level debug] 
    [vrf default | vrf mgmt | vrf <text-config-vrf>] 
    [wjh enable | wjh disable]
    [inband-interface <text-interface-name>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| config-profile-name | \<text-config-profile\> | Specify the name for the configuration profile |
| access-key | \<text-access-key\> | NetQ access key |
| secret-key | \<text-secret-key\> | NetQ secret key |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cpu-limit | \<text-cpu-limit\> | Specify the percentage of CPU resources on a switch that the NetQ Agent cannot exceed |
| log-level | error, warn, info, debug | Specify the logging level |
| vrf | default, mgmt, \<text-config-vrf\>  | Set the VRF to default, management, or specify a custom VRF |
| wjh | enable, disable | Enable or disable What Just Happened events |
| inband-interface | <text-interface-name\>  | Creates an agent configuration profile for in-band deployments |

### Sample Usage

The following example creates a configuration called 'test-set-all.' The agent is configured not to consume more than 60% of CPU resources, the logging level is set to error, the VRF is set to management, and WJH events are enabled.

```
cumulus@switch:~$ netq lcm add netq-config config-profile-name test-set-all access-key KEY secret-key SKEY cpu-limit 60 log-level error vrf mgmt wjh enable
NetQ config profile test-set-all successfully added
 
cumulus@switch:~$ netq lcm show netq-config
ID                        Name            Default Profile                VRF             WJH       CPU Limit Log Level Last Changed
------------------------- --------------- ------------------------------ --------------- --------- --------- --------- -------------------------
config_profile_d349823e2a test-set-all    No                             mgmt            Enable    60%       error     Thu Apr 20 08:38:37 2023
ae91a083ed7874d5a3c4fd09b
1e99963bda91efccecfc5421a
faa8
config_profile_3289efda36 NetQ default co Yes                            mgmt            Disable   Disable   info      Mon Apr 17 06:21:35 2023
db4065d56f91ebbd34a523b45 nfig
944fbfd10c5d75f9134d42023
eb2b
```

### Related Commands

- `netq lcm show netq-config`
- `netq lcm del netq-config`

- - -
## netq lcm add netq-image

Adds a NetQ image (.deb package) to the lifecycle management repository. Images must match the version, architecture, and operating system for the switches you want to upgrade. For each version of NetQ, you must add the `netq-agent` and `netq-apps` packages. For more information, see {{<link title="NetQ and Network OS Images">}}.

### Syntax

```
netq lcm add netq-image <text-netq-image-path>
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
<!-- NVlink command
## netq lcm add nvos-image

### Syntax

```
 netq lcm add nvos-image <text-nvos-image-path> 
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| nvos-image | \<text-nvos-image-path\> |  |

- - -
-->
## netq lcm add role

Assigns or changes a role for one or more switches that defines its placement in a Clos topology and influences the order in which you can upgrade switches.

### Syntax

```
netq lcm add role (superspine | spine | leaf | exit)
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
## netq lcm add ztp-script

Adds a ZTP script to your NetQ VM to provision switches running Cumulus Linux. The output of this command provides the URL to use in the DHCP server option 239 configuration to instruct switches to retrieve the script.

### Syntax

```
netq lcm add ztp-script <text-ztp-script-path>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ztp-script | <text-ztp-script-path\>  | File path specifying the location of the ZTP script |
### Options

None

### Sample Usage

```
cumulus@netq-server:~$ netq lcm add ztp-script /home/cumulus/ztp.sh
ZTP script ztp.sh uploaded successfully and can be downloaded from http://10.10.10.10/lcm/asset/ztp.sh
cumulus@netq-server:~$ 
```

### Related Commands

- `netq lcm del ztp-script`
- `netq lcm show ztp-scripts`
- - -
## netq lcm attach credentials

Assigns an {{<link title="Credentials and Profiles" text="access profile">}} to one or more switches. For step-by-step instructions, see {{<link title="Switch Management#assign-a-profile-to-a-switch" text="Switch Management">}}.

To display the `profile_id`, run `netq lcm show credentials`.

To display `hostnames`, run `netq lcm show switches`.

### Syntax

```
netq lcm attach credentials 
    profile_id <text-switch-profile-id> 
    hostnames <text-switch-hostnames>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| profile_id | <text-switch-profile-id\> | Attach the access profile with this ID to the switch |
| hostnames | <text-switch-hostnames\>  | Assign the access profile to this hostname |

### Options

None
### Sample Usage

```
cumulus@switch:~$ netq lcm attach credentials profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289 hostnames tor-1,tor-2
Attached profile to switch(es).
```
### Related Commands

- `netq lcm add credentials`
- `netq lcm detach credentials`
- `netq lcm show credentials`
- `netq lcm show switches`

- - -

## netq lcm del cl-image

Removes a selected Cumulus Linux image (.bin) from the NetQ lifecycle management repository. Obtain the image identifier using the `netq lcm show cl-image` command with the `json` option.

### Syntax

```
netq lcm del cl-image <text-cl-image-id>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-image | \<text-cl-image-id\> | Remove the Cumulus Linux image with this identifier |

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

Deletes the access credentials required to upgrade Cumulus Linux or NetQ on switches using lifecycle management. Run `netq show credentials` to obtain the profile ID. Refer to {{<link title="Credentials and Profiles/#delete-access-profiles" text="delete access profiles">}} for step-by-step examples.

### Syntax

```
netq lcm del credentials 
    profile_ids <text-credential-profile-ids>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| credentials | NA | Remove the access credentials used to upgrade switches |
| profile_ids | <text-credential-profile-ids\> | Remove the profile assigned this ID |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm del credentials profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289
```

### Related Commands

- `netq lcm add credentials`
- `netq lcm detach credentials`
- `netq lcm show credentials`

- - -

<!-- need to verify below command against 4.7 command line diff-->
## netq lcm del netq-config

Deletes a NetQ configuration profile. You can obtain the configuration profile ID with `netq lcm show netq-config`.

### Syntax

```
netq lcm del netq-config config-profile-id <text-config-profile-id>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| config-profile-id | \<text-config-profile-id\> | Remove the NetQ configuration profile with this identifier |

### Options

None

### Sample Usage

To obtain the configuration profile ID, run `netq lcm show netq-config`:

``` 
cumulus@switch:~$ netq lcm show netq-config
ID                        Name            Default Profile                VRF             WJH       CPU Limit Log Level Last Changed
------------------------- --------------- ------------------------------ --------------- --------- --------- --------- -------------------------
config_profile_d349823e2a test-set-all    No                             mgmt            Enable    60%       error     Thu Apr 20 08:38:37 2023
ae91a083ed7874d5a3c4fd09b
1e99963bda91efccecfc5421a
faa8
config_profile_3289efda36 NetQ default co Yes                            mgmt            Disable   Disable   info      Mon Apr 17 06:21:35 2023
db4065d56f91ebbd34a523b45 nfig
944fbfd10c5d75f9134d42023
eb2b
```

After obtaining the profile ID, run the delete command:

```
cumulus@switch:~$ netq lcm del netq-config config-profile-id config_profile_d349823e2aae91a083ed7874d5a3c4fd09b1e99963bda91efccecfc5421afaa8
NetQ config profile ID config_profile_d349823e2aae91a083ed7874d5a3c4fd09b1e99963bda91efccecfc5421afaa8 successfully deleted
```

You can verify that the configuration profile was deleted with `netq lcm show netq-config`:

```
cumulus@switch:~$ netq lcm show netq-config
ID                        Name            Default Profile                VRF             WJH       CPU Limit Log Level Last Changed
------------------------- --------------- ------------------------------ --------------- --------- --------- --------- -------------------------
config_profile_3289efda36 NetQ default co Yes                            mgmt            Disable   Disable   info      Mon Apr 17 06:21:35 2023
db4065d56f91ebbd34a523b45 nfig
944fbfd10c5d75f9134d42023
eb2b
```

### Related Commands

- `netq lcm add netq-config`
- `netq lcm show netq-config`

- - -

## netq lcm del netq-image

Removes a selected NetQ image (.deb) from the NetQ lifecycle management repository. Obtain the image identifier using the `netq lcm show netq-image` command with the `json` option. Note to completely remove a version, you must delete both the `netq-agent` and `netq-apps` images.

### Syntax

```
netq lcm del netq-image <text-netq-image-id>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| netq-image | \<text-netq-image-id\> | Remove the NetQ image with this identifier |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm show netq-image json
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
<!--NVLink command
## netq lcm del nvos image

### Syntax

```
netq lcm del nvos-image <text-nvos-image-id>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| nvis-image | \<text-nvos-image-id\> | Remove the NVOS image with this identifier |

### Options

None

### Sample Usage

### Related Commands

- - -
-->
## netq lcm del ztp-script

Deletes a ZTP script from your NetQ server. Use the `netq lcm show ztp-scripts` command to view a list of all ZTP scripts along with their script identification numbers.

### Syntax

```
netq lcm del ztp-script <text-ztp-script-id>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ztp-script | <text-ztp-script-id\> | Delete ZTP script with this script ID |
### Options

None


### Sample Usage

```
cumulus@netq-server:~$ netq lcm show ztp-scripts json
[
    {
        "scriptId": "file_e96b2807bdb2c77c89334d03952097dd2224a25df68a6e91d6ab19fc9c265974",
        "scriptName": "ztp1.sh",
        "generatedDownloadUrl": http://10.10.10.10/lcm/asset/ztp.sh
    }
]

cumulus@netq-server:~$ netq lcm del ztp-script file_e96b2807bdb2c77c89334d03952097dd2224a25df68a6e91d6ab19fc9c265974
ZTP script ztp1.sh successfully deleted 
```
### Related Commands

- `netq lcm add ztp-script`
- `netq lcm show ztp-scripts`
- - -
## netq lcm detach credentials

Detaches an access profile from a switch and restores the default profile. Obtain the hostname by running `netq lcm show switches`.

### Syntax

```
netq lcm detach credentials 
    hostname <text-switch-hostname>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| hostname | <text-switch-hostname\>  | Detach access credentials from the switch with this hostname |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm detach credentials hostname spine-1
Detached profile from switch.
```

### Related Commands

- `netq lcm attach credentials`
- `netq lcm del credentials`
- `netq lcm show credentials`
- `netq lcm show switches`

- - -

## netq lcm discover

Searches for switches that do not have NetQ installed based on IP addresses or from a file. After discovery, you can add them to the lifecycle management repository and upgrade Cumulus Linux. To obtain the profile ID, run `netq lcm show credentials`. Use the `netq lcm show discovery-job` command to view the results of this command.

### Syntax

```
netq lcm discover
    (ip-range <text-ip-range> | csv-file <text-csv-file-path>)
    profile_id <text-credential-profile-id>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ip-range | \<text-ip-range\> | Search for switches with this IP address or within this address range. Ranges can be contiguous, for example 192.168.0.24-64, or non-contiguous, for example 192.168.0.24-64,128-190,225, but they must reside within a single subnet. You can include a maximum of 50 addresses in an address range. |
| csv-file | \<text-csv-file-path\> | Search for switches in this CSV file containing the IP address, and optionally, the hostname and port for each switch on the network. If the port is blank, NetQ uses switch port 22 by default. They can be in any order you like, but the data must match that order. |
| profile_id | <text-credential-profile-id\> | Search for switches attached to this access profile |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq lcm discover ip-range 192.168.0.24-64 profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289
NetQ Discovery Started with job id: job_scan_4f3873b0-5526-11eb-97a2-5b3ed2e556db
```

### Related Commands

- ```netq lcm show discovery-job```

- - -
## netq lcm edit credentials

Modifies an access profile's name, authentication type, username, or password. See {{<link title="Credentials and Profiles">}} for more information about access profiles.

Before editing an access profile, run `netq lcm show credentials` to obtain the profile's ID.
### Syntax

```
netq lcm edit credentials 
    profile_id <text-switch-profile-id> 
    [profile_name <text-switch-profile-name>] 
    [auth-type <text-switch-auth-type>] 
    [username <text-switch-username>] 
    [password <text-switch-password> | ssh-key <text-ssh-key>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| profile_id | <text-credential-profile-id\> | Edit the profile assigned this ID |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| profile_name | \<text-switch-profile-name\> | Changes the access profile's name |
| auth-type | \<text-switch-auth-type\> | Changes the authentication method (basic or SSH) |
| username | \<text-switch-username\> | Changes the username for the user who can configure switches |
| password | \<text-switch-password\> | Changes the password associated with the username so that the user can configure switches |
| ssh-key | \<text-ssh-key\> | Changes the *private* key required to configure switches. You must have already installed the *public* key on each switch. |

### Sample Usage

To obtain the profile ID, run `netq lcm show credentials`:

```
cumulus@switch:~$ netq lcm show credentials
Profile ID           Profile Name             Type             SSH Key        Username         Password         Number of switches                   Last Changed
-------------------- ------------------------ ---------------- -------------- ---------------- ---------------- ------------------------------------ -------------------------
credential_profile_3 n-1000                   BASIC                           admin            **************   3                                    Fri Feb  3 21:49:10 2023
eddab251bddea9653df7
cd1be0fc123c5d7a42f8
18b68134e42858e54a9c
289
```
To change the name of the profile (in this example from n-1000 to n-2000) run:

```
cumulus@switch:~$ netq lcm edit credentials profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289 profile_name n-2000
Credential profile modified.
```

Run `netq lcm show credentials` to verify the edit:

```
netq lcm show credentials
Profile ID           Profile Name             Type             SSH Key        Username         Password         Number of switches                   Last Changed
-------------------- ------------------------ ---------------- -------------- ---------------- ---------------- ------------------------------------ -------------------------
credential_profile_3 n-2000                   BASIC                           admin            **************   3                                    Tue Feb  7 16:57:46 2023
eddab251bddea9653df7
cd1be0fc123c5d7a42f8
18b68134e42858e54a9c
289
```
### Related Commands

- `netq lcm show credentials`

- - -
## netq lcm install netq-image

Installs NetQ on switches.

### Syntax

```
netq lcm install netq-image 
    job-name <text-job-name> 
    netq-version <text-netq-version> 
    upgrade-cli [True | False] 
    ips <text-ip-range> 
    cpu_arch <text-cpu-arch> 
    cl_version <text-cumulus-linux-version>
    profile_id <text-credential-profile-id> 
    [config_profile <text-config-profile>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| job-name | \<text-job-name\> | Name for the installation |
| netq-version | \<text-netq-version\> | Install this NetQ version in x.z.y format |
| upgrade-cli | True, False | Upgrade the NetQ CLI as part of the installation (True) or not (False) |
| ips | <text-ip-range\> | Install NetQ on switches within this address range. Ranges can be contiguous, for example 192.168.0.24-64, or non-contiguous, for example 192.168.0.24-64,128-190,225, but they must reside within a single subnet. You can include a maximum of 50 addresses in an address range. |
| cpu_arch | <text-cpu-arch\> | CPU architecture for the switch|
| cl-version | \<text-cumulus-linux-version\> | Install this CL version in x.y.z format |
| profile_id | <text-credential-profile-id\> | Access profile attached to the switches |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| config_profile | <text-config-profile\> | Configuration file applied after the installation |

### Sample Usage

```
netq lcm install netq-image job-name install55 netq-version 4.9.0 upgrade-cli True ips 192.168.0.24-64 cpu_arch x86_64 cl_version 5.8.0 profile_id credential_profile_3eddab251bddea9653df7cd1be0fc12
```
### Related Commands

- `netq lcm discover`
- - -
<!-- NVLink command
## netq lcm restart nvos

### Syntax

```
netq lcm restart nvos 
    job-name <text-job-name> 
    ips <text-switch-ips> 
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| job-name | \<text-job-name\> | Name for the upgrade |
| ips | <text-switch-ips\> | |

### Options

None

### Sample Usage

### Related Commands

- netq lcm upgrade nvos
- - -
-->
## netq lcm show cl-images

Displays all Cumulus Linux images in the lifecycle management repository. 

### Syntax

```
netq lcm show cl-images
    [<text-cl-image-id>]
    [json]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| cl-images | NA | Display all Cumulus Linux images in the lifecycle management repository |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-cl-image-id\> | Only display Cumulus Linux image with this identifier |
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

- ```netq lcm add cl-image```
- ```netq lcm del cl-image```

- - -

## netq lcm show credentials

Displays access profiles, their associated credentials, and the number of switches assigned to each access profile.

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
Profile ID           Profile Name             Type             SSH Key        Username         Password         Number of switches                   Last Changed
-------------------- ------------------------ ---------------- -------------- ---------------- ---------------- ------------------------------------ -------------------------
credential_profile_d Netq-Default             BASIC                           cumulus          **************   11                                   Fri Feb  3 18:20:33 2023
9e875bd2e6784617b304
c20090ce28ff2bb46a4b
9bf23cda98f1bdf91128
5c9
credential_profile_3 Nvl4-Default             BASIC                           admin            **************   1                                    Fri Feb  3 19:18:26 2023
5a2eead7344fb91218bc
dec29b12c66ebef0d806
659b20e8805e4ff629bc
23e
credential_profile_3 n-1000                   BASIC                           admin            **************   3                                    Fri Feb  3 21:49:10 2023
eddab251bddea9653df7
cd1be0fc123c5d7a42f8
18b68134e42858e54a9c
289
```

### Related Commands

- `netq lcm add credentials`
- `netq lcm attach credentials`
- `netq lcm del credentials`

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
netq lcm show discovery-job
    [json]
```

### Required Arguments

None
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

- `netq lcm discover`

- - -

## netq lcm show netq-config

Displays the configuration of all NetQ configuration profiles, including the name and identifier, the default profile, VRF, What Just Happened status, CPU usage limit, and logging level.

### Syntax

```
netq lcm show netq-config
    [json]
```

### Required Arguments

None

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

- `netq lcm add netq-config`
- `netq lcm del netq-config`

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

- `netq lcm add netq-image`
- `netq lcm del netq-image`

- - -
<!--NVLink command
## netq lcm show nvos-images

Displays all NVOS images in the lifecycle management repository.

### Syntax

```
netq lcm show nvos-images
    [<text-nvos-image-id>]
    [json]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| nvos-images | NA | Display all NVOS images in the lifecycle management repository |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-nvos-image-id\> | Only display the NVOS image with this identifier |
| json | NA | Display the output in JSON format |

- - -
-->
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

Displays information about switches monitored by NetQ and contained in the lifecycle management repository, including their hostnames, any assigned role, IP and MAC addresses, CPU architecture, Cumulus Linux and NetQ versions, and NetQ configuration and access profiles. Filter the output by Cumulus Linux or NetQ version running on the switch.

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
| switches | NA | Display information about switches known to lifecycle management |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| cl-version | \<text-cumulus-linux-version\> | Only display switches running this version of the Cumulus Linux OS |
| netq-version | \<text-netq-version\> | Only display switches running this version of NetQ |
| json | NA | Display the output in JSON format |

### Sample Usage

Display switches running Cumulus Linux 5.5.0:

```
cumulus@switch:~$ netq lcm show switches cl-version 5.5.0
Hostname          Role       IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Credential Profile                   Last Changed
----------------- ---------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- ------------------------------------ -------------------------
noc-se                       192.168.0.15              00:01:00:00:12:00  x86_64   5.5.0       4.8.0-cl4u46~ []                           Netq-Default                         Fri Feb  3 20:50:40 2023
                                                                                               1713945871.12
                                                                                               7fb0c1b
spine-1                      192.168.0.15              00:01:00:00:13:00  x86_64   5.5.0       4.8.0-cl4u46~ []                           n-2000                               Fri Feb  3 22:28:25 2023
                                                                                               1713945871.12
                                                                                               7fb0c1b
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
## netq lcm show ztp-scripts

Displays a list of ZTP scripts along with their script identification numbers and the URL where they can be downloaded.

### Syntax

```
netq lcm show ztp-scripts [<text-ztp-script-id>]
    [json]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ztp-scripts | <text-ztp-script-id\> | Only display ZTP script with this script ID |
| json | NA | Display the output in JSON format |

### Sample Usage

```
cumulus@netq-server:~$ netq lcm show ztp-scripts json
[
    {
        "scriptId": "file_e96b2807bdb2c77c89334d03952097dd2224a25df68a6e91d6ab19fc9c265974",
        "scriptName": "ztp1.sh",
        "generatedDownloadUrl": http://10.10.10.10/lcm/asset/ztp.sh
    }
]
```
### Related Commands

- `netq lcm add ztp-script`
- `netq lcm del ztp-script`
- - -
## netq lcm upgrade cl-image

Upgrades Cumulus Linux on one or more switches in your network.

### Syntax

```
netq lcm upgrade cl-image 
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
| cl-version | \<text-cumulus-linux-version\> | Upgrade to this CL version in x.y.z format |
| netq-version | \<text-netq-version\> | Upgrade to this NetQ version in x.z.y format |
| hostnames | \<text-switch-hostnames\> | Comma-separated list of the hostname(s) to be upgraded |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| run-restore-on-failure | NA | Restore the previous version of Cumulus Linux if the upgrade fails (recommended) |
| run-snapshot-before-after | NA | Generate a network snapshot before and after the upgrade |

### Sample Usage

```
cumulus@switch:~$ netq lcm upgrade cl-image job-name upgrade-cl430 cl-version 4.3.0 netq-version 4.6.0 hostnames spine01,spine02
```

### Related Commands

- `netq lcm show discovery-job`

- - -
## netq lcm upgrade netq-image

Upgrades NetQ Agents on one or more switches in your network.

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
| job-name | \<text-job-name\> | User-defined name for the upgrade |
| hostnames | \<text-switch-hostnames\> | Comma-separated list of the hostname(s) to be upgraded |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| netq-version | <text-netq-version\> |  Upgrade to this NetQ version in x.y.z format |
| upgrade-cli | True, False | Upgrade the NetQ CLI as part of the upgrade (True) |
| config_profile | <text-config-profile\> | Configuration file applied after the upgrade |

### Sample Usage

```
cumulus@switch:~$ netq lcm upgrade netq-image job-name upgrade-cl530-nq450 netq-version 4.6.0 hostnames spine01,spine02
```

### Related Commands

- `netq lcm show upgrade-jobs netq-image`


<!--NVLink command
## netq lcm upgrade nvos-image

### Syntax

```
netq lcm upgrade nvos-image 
    job-name <text-job-name> 
    nvos-version <text-nvos-version> 
    ips <text-switch-ips> 
    [restart_after_upgrade]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| nvos-image | NA |  |
| job-name | \<text-job-name\> | Name for the upgrade |
| nvos-version | <text-netq-version\> | |
| ips | <text-switch-ips\> | |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| restart_after_upgrade | NA |  |

### Sample Usage

### Related Commands

- netq lcm restart nvos

-->