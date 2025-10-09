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

Upgrades NetQ on NetQ On-premises Appliances or VMs. For detailed instructions, see {{<link title="Upgrade NetQ Appliances and Virtual Machines" text="Upgrade NetQ Appliances and Virtual Machines">}}

### Syntax

```
netq upgrade bundle <text-bundle-url>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Upgrade this appliance or VM with the `NetQ-x.y.z.tgz` package at this location. You must specify the full path |

### Options

None

### Sample Usage

```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.5.0.tgz
```

### Related Commands

None
