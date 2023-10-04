---
title: bootstrap
author: NVIDIA
weight: 1101
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
## netq bootstrap refresh

### Syntax

```
netq bootstrap refresh 
    <text-tarball-name> 
    [ecr-access-key <text-ecr-access-key> ecr-secret-key <text-ecr-secret-key>]
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
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
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |

<!--
### Sample Usage

-->

### Related Commands

None

- - -
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

None



