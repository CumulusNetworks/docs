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

Adds a Cumulus Linux image (.bin file) to the lifecycle management repository. Images must match the version, architecture, and ASIC vendor for the switches you want to upgrade.

Obtain the images from the {{<exlink url="https://cumulusnetworks.com/downloads/#product=Cumulus%20Linux" text="Cumulus Downloads">}} page or {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

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

{{<notice tip>}}
The default credentials for Cumulus Linux have changed from cumulus/CumulusLinux! to cumulus/cumulus for releases 4.2 and later. For details, read <a href="https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts/">Cumulus Linux User Accounts</a>.
{{</notice>}}

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

There are two forms of this command; one for Cumulus Linux and the other for NetQ.

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

Obtain the images from the {{<exlink url="https://cumulusnetworks.com/downloads/#product=NetQ" text="Cumulus Downloads">}} page or {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

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
cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-agent_3.3.0-ub18.04u32~1610530013.2e51873_amd64
cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-apps_3.3.0-ub18.04u32~1610530013.2e51873_amd64
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

cumulus@netq-ts:~$ netq lcm 
    discover  :  Perform switch discovery operation
    show      :  Show fabric-wide info about specified object
    upgrade   :  Upgrade NetQ
cumulus@netq-ts:~$ netq lcm discover 
    csv-file  :  Discovery job input as csv file
    ip-range  :  Discovery job input as ip address range
cumulus@netq-ts:~$ netq lcm show 
    cl-images        :  Cumulus Linux Images
    credentials      :  Switch credentials
    default-version  :  add help text
    discovery-job    :  Get status of discovery job
    netq-config      :  Display NetQ config profiles
    netq-images      :  NETQ Agent/CLI Images
    status           :  Get status on CL/NetQ Upgrade
    switches         :  Switches running Cumulus Linux
    upgrade-jobs     :  Get history of all upgrade jobs
cumulus@netq-ts:~$ netq lcm upgrade 
    cl-image    :  Cumulus Linux Image
    name        :  Validation name
    netq-image  :  NetQ Agent/CLI Image
