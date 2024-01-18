---
title: decommission
author: NVIDIA
weight: 1103
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq decommission

Decommissions a switch or host *currently* running the NetQ Agent. This removes information about the switch or host from the NetQ database. Before decommissioning a switch, you should stop and disable the NetQ Agent.

You might need to decommission a switch when you:

<!-- vale off -->
- Change the hostname of the switch or host
- Move the switch or host from one data center to another
- Return the switch or host
<!-- vale on -->

### Syntax

```
netq decommission <hostname-to-decommission>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<hostname-to-decommission\> | Decommission the switch with this hostname |

### Options

None

### Sample Usage

```
cumulus@switch:~$ sudo systemctl stop netq-agent
cumulus@switch:~$ sudo systemctl disable netq-agent

cumulus@switch:~$ netq decommission leaf28
Successfully decommissioned node leaf28
```

### Related Commands

None

