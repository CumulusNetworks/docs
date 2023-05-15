---
title: RIB
author: Cumulus Networks
weight: 700

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set vrf \<vrf-id\> router rib

Provides commands to configure the routing table for the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\>

Provides commands to configure the switch to import protocols from where routes are known.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\> fib-filter</h>

Configures a route map to apply on the routes of the import protocol.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family. |
| `<import-protocol-id>` |  The import protocol list. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set vrf default router rib ipv4 protocol bgp fib-filter routemap1
```
