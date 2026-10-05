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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\> fib-filter \<route-map\></h>

Configures a route map to apply on the routes of the import protocol.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use `nv set vrf <vrf-id> router rib <address-family> fib-filter route-map <route-map-id>` instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family: `ipv4` or `ipv6`. |
| `<import-protocol-id>` |  The import protocol list. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set vrf default router rib ipv4 protocol bgp fib-filter routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv set vrf \<vrf-id\> router rib \<afi\> fib-filter protocol \<protocol-id\> route-map \<route-map\></h>

Configures the protocol you want to import from the RIB to the FIB.

{{%notice note%}}
Cumulus Linux 5.19 removes `connected`, `kernel`, and `table` as valid values for `<protocol-id>`. If your configuration filters RIB-to-FIB routes from one of these three protocols, `nv config apply` rejects it after you upgrade.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family: `ipv4` or `ipv6`. |
| `<protocol-id>` |  The import protocol list: `bgp`, `ospf`, `static`, `rip`, `sharp`, `isis`, `ospf6`, or `ripng`. In Cumulus Linux 5.18 and earlier, `connected`, `kernel`, and `table` are also valid. |
| `<route-map>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.11.0

Cumulus Linux 5.19.0 removes `connected`, `kernel`, and `table` from `<protocol-id>`.

### Example

```
cumulus@switch:~$ nv set vrf default router rib ipv4 fib-filter protocol bgp route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv set vrf \<vrf-id\> router rib \<afi\> fib-filter route-map \<route-map\></h>

Configures a route map to apply on the routes of the import protocol.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family: `ipv4` or `ipv6`. |
| `<route-map>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set vrf default router rib ipv4 fib-filter route-map routemap1
```
