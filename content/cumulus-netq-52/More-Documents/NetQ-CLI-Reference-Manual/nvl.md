---
title: nvl
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
<!-- vale NVIDIA.HeadingTitles = NO -->
## netq nvl cluster backup
<!-- vale on -->

Creates a backup file of the NVLink cluster including TLS certificates, cert-manager configurations, and MongoDB data. The file created from this command is timestamped and can be restored using the `netq nvl cluster restore` command. The options allow you to customize the parameters of the backup file.

### Syntax

```
netq nvl cluster backup 
    [backup-path <text-backup-path>] 
    [cm-op-ns <text-cm-op-ns>] 
    [cm-target-ns <text-cm-target-ns>] 
    [mongo-db-name <text-mongo-db-name>] 
    [mongo-collections <text-mongo-collections>] 
    [mongo-k8s-ns <text-mongo-k8s-ns>] 
    [mongo-statefulset <text-mongo-statefulset>] 
    [mongo-container <text-mongo-container>] 
    [mongo-replicaset <text-mongo-replicaset>]
```

### Required Arguments

None


### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| backup-path | \<text-backup-path\> | Specify a path to the directory where the backup file is stored |
| cm-op-ns | \<text-cm-op-ns\> | Cert-manager operational namespace. If unspecified, the default is `infra`. |
| cm-target-ns | \<text-cm-target-ns\> | Target namespaces for certificates If unspecified, the defaults are `infra`, `kafka`, and `nmx`. |
| mongo-db-name | \<text-mongo-db-name\> | Name of the MongoDB database. If unspecified, the default is `EntityDB`. |
| mongo-collections | \<text-mongo-collections\> | Name of the MongoDB collections. If unspecified, the defaults are `nmx-services`, `domains`, and `switch_profiles`. |
| mongo-k8s-ns | \<text-mongo-k8s-ns\> | MongoDB Kubernetes namespace. If unspecified, the default is `infra`. |
| mongo-statefulset | \<text-mongo-statefulset\> | MongoDB StatefulSet name. If unspecified, the default is `mongodb`. |
| mongo-container | \<text-mongo-container\> | MongoDB container name. If unspecified, the default is `mongodb`. |
| mongo-replicaset | \<text-mongo-replicaset\> | Name of the MongoDB replica set. If unspecified, the default is `rs0`. |


### Related Commands

- `netq nvl cluster restore`

- - -

## netq nvl cluster restore

Restores an NVLink cluster that was backed up using the `netq nvl cluster backup` command.


### Syntax

```
 netq nvl cluster restore <text-backup-path> 
    [drop-mongo-collections] 
    [cm-op-ns <text-cm-op-ns>] 
    [mongo-k8s-ns <text-mongo-k8s-ns>] 
    [mongo-statefulset <text-mongo-statefulset>] 
    [mongo-container <text-mongo-container>] 
    [mongo-replicaset <text-mongo-replicaset>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-backup-path\> | Path to the timestamped backup directory (for example, `/opt/backups/nvl-backup_20241201143022`) |
| cm-op-ns | \<text-cm-op-ns\> | Cert-manager operational namespace. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| drop-mongo-collections | NA | Removes any pre-existing MongoDB collections (recommended) |
| mongo-k8s-ns | \<text-mongo-k8s-ns\> | MongoDB Kubernetes namespace |
| mongo-statefulset | \<text-mongo-statefulset\> | MongoDB StatefulSet name |
| mongo-container | \<text-mongo-container\> | MongoDB container name |
| mongo-replicaset | \<text-mongo-replicaset\> | Name of the MongoDB replica set |

### Related Commands

- `netq nvl cluster restore`

