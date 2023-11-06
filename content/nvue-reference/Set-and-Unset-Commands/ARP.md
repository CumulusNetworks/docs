---
title: ARP
author: Cumulus Networks
weight: 517

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system global arp base-reachable-time</h>

Configures how long a neighbor cache entry is valid. The entry is considered valid for at least the value between the base reachable time divided by two and three times the base reachable time divided by two. You can specify a value between 30 and 2147483 seconds. The default value is auto; NVUE derives the value for auto from the `/etc/sysctl.d/neigh.conf` file.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system global arp base-reachable-time 50
```
