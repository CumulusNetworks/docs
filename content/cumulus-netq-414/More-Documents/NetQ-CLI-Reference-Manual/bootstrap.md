---
title: bootstrap
author: NVIDIA
weight: 1101
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
## netq bootstrap reset

Reset the node to prepare it for loading the installation program. In on-premises deployments, you can choose whether to save the current data or discard it during the reset process. NetQ saves all data by default in remotely hosted database deployments.

In a cluster deployment, you must run this command on each node in the cluster. Refer to the {{<link title="Install the NetQ System" text="installation page for your deployment model">}} for step-by-step instructions.

### Syntax

```
netq bootstrap reset
    [keep-db | purge-db]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| keep-db | NA | Save existing data before resetting the node. Only applies to deployments with local databases. |
| purge-db | NA | Discard existing data when resetting the node. Only applies to deployments with local databases. |

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

- `netq config reset premise`

<!--not exposed to customers
## netq bootstrap worker

### Syntax

```
netq bootstrap worker 
    tarball <text-tarball-name> 
    ip-addr <text-ip-addr> 
    master-ip <text-master-ip> 
    cluster-vip <text-cluster-vip> 
    [password <text-password>] 
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| tarball | \<text-tarball-name\> | Full path of the installation file, for example, */mnt/installables/netq-bootstrap-4.9.0.tgz*  |
| ip-addr | \<text-ip-addr\> | IP address used for your NetQ server |
| master-ip | \<text-master-ip\> | IP address used for your master node |
| cluster-vip | \<text-cluster-vip\> | Virtual IP address from the same subnet used for your master and worker nodes. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| password | \<text-password\> | Admin password |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |

## Related Commands

None
-->