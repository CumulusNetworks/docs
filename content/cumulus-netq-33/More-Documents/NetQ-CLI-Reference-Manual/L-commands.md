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

## netq lcm

    add      :  Add netq tca configuration
    del       :  Delete netq tca configuration
    discover  :  Perform switch discovery operation
    show      :  Show fabric-wide info about specified object
    upgrade   :  Upgrade NetQ

    netq lcm del netq-image <text-image-id>
    netq lcm discover (ip-range <text-ip-range> | csv-file <text-csv-file-path>)
    netq lcm show cl-images [<text-image-id>] [json]
    netq lcm show credentials [json]
    netq lcm show default-version cl-images [json]
    netq lcm show default-version netq-images [json]
    netq lcm show discovery-job <text-discovery-job-id> [json]
    netq lcm show netq-config [json]
    netq lcm show netq-images [<text-netq-image-id>] [json]
    netq lcm show status cl-image <text-lcm-job-id> [json]
    netq lcm show status netq-image <text-netq-upgrade-job-id> [json]
    netq lcm show switches [cl-version <text-cumulus-linux-version>] [netq-version <text-netq-version>] [json]
    netq lcm show upgrade-jobs cl-image [json]
    netq lcm show upgrade-jobs netq-image [json]
    netq lcm upgrade [cl-image] name <text-job-name> cl-version <text-cumulus-linux-version> netq-version <text-netq-version> hostnames <text-switch-hostnames> [run-restore-on-failure] [run-before-after]
    netq lcm upgrade netq-image name <text-job-name> [netq-version <text-netq-version>] [upgrade-cli True | upgrade-cli False] hostnames <text-switch-hostnames> [config_profile <text-config-profile>]

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
| 3.1.0 | Introduced |

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
| 3.0.0 | Introduced |

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
| 3.3.0 | Introduced |

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
| 3.3.0 | Introduced |

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
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm add role leaf switches leaf01,leaf02
```

- - -

## netq lcm del cl-image

{{<link url="Image-Management/#remove-images-from-local-repository" text="Deletes">}} a Cumulus Linux image from the LCM repository.

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
| 3.3.0 | Added ability to specify a Cumulus Linux or NetQ image |
| 3.0.0 | Introduced |

### Sample Usage

```
cumulus@netq-ts:~$ netq lcm del cl-image image_c6e812f0081fb03b9b8625a3c0af14eb82c35d79997db4627c54c76c973ce1ce
```

- - -

## netq lcm del credentials



### Syntax

```
netq lcm del credentials
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
|  |  |  |

### Options

None

<!-- ### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
|  | Introduced | -->

### Sample Usage

```
cumulus@netq-ts:~$ 
```

- - -

## netq lcm



### Syntax

```
netq 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
|  |  |  |

### Options

None

<!-- ### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
|  | Introduced | -->

### Sample Usage

```
cumulus@netq-ts:~$ 
```

- - -

## netq lcm



### Syntax

```
netq 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
|  |  |  |

### Options

None

<!-- ### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
|  | Introduced | -->

### Sample Usage

```
cumulus@netq-ts:~$ 
```

- - -

## netq lcm



### Syntax

```
netq 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
|  |  |  |

### Options

None

<!-- ### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
|  | Introduced | -->

### Sample Usage

```
cumulus@netq-ts:~$ 
```

- - -

## netq lcm



### Syntax

```
netq 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
|  |  |  |

### Options

None

<!-- ### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
|  | Introduced | -->

### Sample Usage

```
cumulus@netq-ts:~$ 
```

- - -


