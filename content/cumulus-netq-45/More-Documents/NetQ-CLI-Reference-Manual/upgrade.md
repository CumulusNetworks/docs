---
title: upgrade
author: Cumulus Networks
weight: 1107
toc: 3
right_toc_levels: 1
pdfhidden: true
---

## netq upgrade

Upgrades NetQ on NetQ On-premises Appliances or VMs.

Obtain the software upgrade bundle from the {{<exlink url="https://cumulusnetworks.com/downloads/#product=NetQ" text="Cumulus Downloads">}} page or {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

### Syntax

```
netq upgrade bundle <text-bundle-url>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Upgrade this appliance or VM with the `NetQ-x.y.z.tgz` package at this location; you must specify the full path |

### Options

None

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.0.0.tgz
```

### Related Commands

None
