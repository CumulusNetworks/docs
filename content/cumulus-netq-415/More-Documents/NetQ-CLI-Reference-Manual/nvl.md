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
<!-- vale off -->
## netq nvl cluster backup
<!-- vale on -->

Creates a backup file of the NVLink cluster including TLS certificates, cert-manager configurations, and MongoDB data. The file created from this command is timestamped and can be restored using the `netq nvl cluster restore` command.

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
| backup-path | \<text-backup-path\> | Directory path where backup will be stored |
| cm-op-ns | \<text-cm-op-ns\> | Cert-manager operational namespace (default: infra) |
| cm-target-ns | \<text-cm-target-ns\> | Target namespaces for certificates (default: infra,kafka,nmx) |
| mongo-db-name | \<text-mongo-db-name\> | MongoDB database name to backup (default: EntityDB) |
| mongo-collections | \<text-mongo-collections\> | MongoDB collections to backup (default: nmx-services,domains,switch_profiles) |
| mongo-k8s-ns | \<text-mongo-k8s-ns\> | MongoDB Kubernetes namespace (default: infra) |
| mongo-statefulset | \<text-mongo-statefulset\> | MongoDB StatefulSet name (default: mongodb) |
| mongo-container | \<text-mongo-container\> | MongoDB container name (default: mongodb) |
| mongo-replicaset | \<text-mongo-replicaset\> | MongoDB replica set name (default: rs0) |


### Sample Usage


### Related Commands


- - -

## netq nvl cluster restore

Restores NVL cluster from a previously created backup, including certificates, cert-manager configurations, and MongoDB data. This command ensures complete cluster recovery with proper certificate chain validation.


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

### Options

| Option | Value | Description |
| ---- | ---- | ---- |

### Sample Usage



### Related Commands

- `netq nvl cluster restore`
- - -

<!-- vale off -->
## netq nvl bootstrap reset
<!-- vale on -->
Resets the NVL bootstrap configuration to factory defaults. This command clears custom configurations and can be used for troubleshooting or preparing for fresh installations.



### Syntax

```
netq nvl bootstrap reset [config <text-config-path>]
```


### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |


### Options

None

### Sample Usage



### Related Commands

