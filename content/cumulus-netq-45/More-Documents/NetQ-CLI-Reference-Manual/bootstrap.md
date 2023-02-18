---
title: bootstrap
author: NVIDIA
weight: 1101
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq bootstrap

Load the installation program onto the network switches and hosts in either a single server or server cluster arrangement. This command is the same for any deployment model.

### Syntax

```
netq bootstrap master
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    tarball <text-tarball-name>
    [pod-ip-range <text-pod-ip-range>]
    [ignore-errors]

netq bootstrap worker
    tarball <text-tarball-name>
    master-ip <text-master-ip>
    [password <text-password>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| master | NA | Load the installation program onto the single NetQ server or master server in a cluster |
| interface | \<text-opta-ifname\> | Name of the interface on the NetQ appliance or VM where the server listens for NetQ Agents |
| ip-addr | \<text-ip-addr\> | IP address of the interface on the NetQ appliance or VM where the server listens for NetQ Agents |
| worker | NA | Load the installation program onto worker nodes in a NetQ server cluster |
| tarball | \<text-tarball-name\> | Full path of the installation file, for example, */mnt/installables/netq-bootstrap-4.0.0.tgz* |
| master-ip | \<text-master-ip\> | IP address for the master server in a NetQ server cluster |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| pod-ip-range | \<text-pod-ip-range\> | Change the IP address range to this range for Flannel container environments when you have a conflict. NetQ overrides the default Flannel address range (10.1.0.0/16) with 10.244.0.0/16. |
| password | \<text-password\> | Passphrase for access to the worker node |
| ignore-errors| NA | Ignore errors caused by Kubernetes pre-flight checks |

### Sample Usage

Bootstrap single server or master server in a server cluster:

```
cumulus@switch:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-4.0.0.tgz
```

Bootstrap worker node in server cluster:

```
cumulus@switch:~$ netq bootstrap worker tarball /mnt/installables/netq-bootstrap-4.0.0.tgz  master-ip 192.168.10.20
```

### Related Commands

- ```netq bootstrap reset```
- ```netq bootstrap master upgrade```

- - -

## netq bootstrap master upgrade

Loads master node with a new NetQ installer in an existing server cluster deployment.

{{%notice note%}}

This command applies only when upgrading from NetQ 3.1.1 and earlier.

{{%/notice%}}

### Syntax

```
netq bootstrap master upgrade
    <text-tarball-name>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-tarball-name\> | Full path of the installation file, for example, */mnt/installables/netq-bootstrap-4.0.0.tgz*  |

### Options

None

### Sample Usage

Basic bootstrap:

```
cumulus@switch:~$ netq bootstrap master upgrade mnt/installables/netq-bootstrap-4.0.0.tgz
```

### Related Commands

- ```netq bootstrap```
- ```netq bootstrap reset```

- - -

<!--Refresh NetQ installation artifacts
## netq bootstrap refresh

### Syntax

```
netq bootstrap refresh 
    <text-tarball-name> 
    [ecr-access-key <text-ecr-access-key> ecr-secret-key <text-ecr-secret-key>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-tarball-name\> | Full path of the installation file, for example, */mnt/installables/netq-bootstrap-4.0.0.tgz*  |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ecr-access-key | \<text-ecr-access-key\> | AWS access key ID |
| ecr-secret-key| \<text-ecr-secret-key\>| AWS secret key ID |

### Sample Usage

### Related Commands
- netq bootstrap reset

- - -

-->
## netq bootstrap reset

Reset the node to prepare it for loading the installation program. In on-premises deployments with database on site, you can choose whether to save the current data or discard it (default) during the reset process. NetQ saves all data by default in remotely hosted database deployments.

### Syntax

```
netq bootstrap reset
    [keep-db | purge-db]
    [purge-images]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| keep-db | NA | Save existing data before resetting the node. Only applies to deployments with local databases. |
| purge-db | NA | Discard existing data when resetting the node. Only applies to deployments with local databases. |
| purge-images | NA | Discard Docker images when resetting the node. Only applies to deployments with local databases. |

### Sample Usage

Prepare node for bootstrapping and discard data:

```
cumulus@switch:~$ netq bootstrap reset
```

Prepare node for bootstrapping while keeping existing data:

```
cumulus@switch:~$ netq bootstrap reset keep-db
```

### Related Commands

- ```netq bootstrap```
- ```netq bootstrap master upgrade```



