---
title: upgrade
author: Cumulus Networks
weight: 1107
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq upgrade

Upgrades NetQ on NetQ on-premises appliances or VMs. For detailed instructions, see {{<link title="Upgrade NetQ Virtual Machines" text="Upgrade NetQ Virtual Machines">}}

### Syntax

```
netq upgrade bundle <text-bundle-url>
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
    [cluster-vip <text-cluster-vip>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Upgrade this appliance or VM with the `NetQ-x.y.z.tgz` package at this location. You must specify the full path |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |
| cluster-vip| \<text-cluster-vip\>| Upgrade cluster deployments, specifying the virtual IP address from the same subnet used for your master and worker nodes.|

### Sample Usage

```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.10.1.tgz
```

### Related Commands

None
