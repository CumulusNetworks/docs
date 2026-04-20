---
title: upgrade
author: Cumulus Networks
weight: 1107
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq upgrade bundle

Upgrades NetQ on NetQ on-premises servers or VMs. For detailed instructions, see {{<link title="Upgrade NetQ Virtual Machines" text="Upgrade NetQ Virtual Machines">}}

### Syntax

```
netq upgrade bundle <text-bundle-url>
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
    [cluster-vip <text-cluster-vip>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Upgrade this server or VM with the `NetQ-x.y.z.tgz` package at this location. You must specify the full path |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |
| cluster-vip| \<text-cluster-vip\>| Upgrade cluster deployments, specifying the virtual IP address from the same subnet used for your master and worker nodes.|

### Sample Usage

```
nvidia@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-5.2.0.tgz
```

### Related Commands

None

- - -

## netq upgrade cluster bundle

Upgrades NetQ on NetQ on-premises servers or VMs in combined NVLink + Ethernet mode. For detailed instructions, see {{<link title="Upgrade NetQ Virtual Machines" text="Upgrade NetQ Virtual Machines">}}

### Syntax

```
netq upgrade cluster bundle <text-bundle-url> 
    <text-cluster-config> 
    [ignore-pre-checks] 
    [restore <text-backup-file>] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Upgrade this server or VM with the `NetQ-x.y.z.tgz` package at this location. You must specify the full path. |
| NA | \<text-cluster-config\> | Specify the full path to your cluster's JSON configuration file.|

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ignore-pre-checks | NA | Skips pre-checks (not recommended)|
| restore | \<text-backup-file\> | Specify the path where the backup .tar file resides |

### Sample Usage

```
nvidia@<hostname>:~$ netq upgrade cluster bundle /mnt/installables/NetQ-5.2.0.tgz /tmp/combined-cluster-config.json
```

### Related Commands

None

- - -

## netq upgrade nvl bundle

Upgrades NetQ on NetQ on-premises servers or VMs for NVLink-only deployments. For detailed instructions, see {{<link title="Upgrade NetQ Virtual Machines" text="Upgrade NetQ Virtual Machines">}}

### Syntax

```
netq upgrade nvl bundle <text-bundle-url> 
    kong-rw-password <text-kong-rw-password> 
    kong-ro-password <text-kong-ro-password> 
    <text-cluster-config> 
    [ignore-pre-checks] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Upgrade this server or VM with the `NetQ-x.y.z.tgz` package at this location. You must specify the full path. |
| kong-rw-password | \<text-kong-rw-password\> | Specify the Kong read-write password |
| kong-ro-password | \<text-kong-ro-password\> | Specify the Kong read-only password ( |
| NA | \<text-cluster-config\> | Specify the full path to your cluster's JSON configuration file.|

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ignore-pre-checks | NA | Skips pre-checks (not recommended)|

### Sample Usage

```
nvidia@<hostname>:~$ netq upgrade nvl bundle /mnt/installables/NetQ-5.2.0.tgz kong-rw-password <rw-password> kong-ro-password <ro-password> /home/nvidia/nvl-cluster-config.json
```

### Related Commands

None