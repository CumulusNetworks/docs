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

## <h>nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\></h>

Provides commands to configure the switch to import protocols from where routes are known.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use `nv set vrf <vrf> router rib <address-family> fib-filter protocol  <protocol-id> route-map <route-map-id>` instead.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\> fib-filter \<route-map\></h>

Configures a route map to apply on the routes of the import protocol.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use `nv set vrf <vrf> router rib <address-family> fib-filter route-map <route-map-id>` instead.
{{%/notice%}}

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv set vrf \<vrf\> router rib \<afi\> fib-filter protocol \<protocol-id\> route-map \<route-map\></h>

Configures the protocol you want to import from the RIB to the FIB.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family. |
| `<protocol-id>` |  The import protocol list. |
| `<route-map>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set vrf default router rib ipv4 fib-filter protocol bgp route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv set vrf \<vrf\> router rib \<afi\> fib-filter route-map \<route-map\></h>

Configures a route map to apply on the routes of the import protocol.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family. |
| `<route-map>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set vrf default router rib ipv4 fib-filter route-map routemap1
```
