---
title: RIB Set and Unset Commands
author: Cumulus Networks
weight: 800
product: Cumulus Linux
type: nojsscroll
---
## nv set vrf \<vrf-id\> router rib \<afi\>

Provides commands to configure the routing table for the specified VRF.

- - -

## nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\>

Provides commands to configure the switch to import protocols from where routes are known.

- - -

## nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\> fib-filter (none|\<instance-name\>)

Configures a route map to apply on the routes of the import protocol.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family. |
| `<import-protocol-id>` |  The import protocol list. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router rib ipv4 protocol bgp fib-filter routemap1
```

- - -
