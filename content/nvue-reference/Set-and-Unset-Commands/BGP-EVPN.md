---
title: BGP EVPN
author: Cumulus Networks
weight: 524

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family l2vpn-evpn state</h>

Enables or disables the EVPN address family for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family l2vpn-evpn state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn add-path-tx</h>

Configures BGP to advertise more than just the best path for an EVPN prefix to the BGP neighbor. You can specify `all-paths` to advertise all known paths to the neighbor or `best-per-as` to advertise only the best path learned from each AS. The default setting is disabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn add-path-tx all-paths
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn state</h>

Configures BGP to allow a received AS path to contain the ASN of the local system. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath allow-my-asn state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn occurrences</h>

Configures the maximum number of times the AS number of the local system can be in the received AS path.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath allow-my-asn occurrences 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn origin</h>

Configures BGP to allow a received AS path to contain the ASN of the local system only if it is the originating AS.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath allow-my-asn origin on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod aspath</h>

Configures BGP to follow normal BGP procedures when generating the `AS_PATH` attribute for the neighbor for EVPN. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn attribute-mod aspath enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod med</h>

Configures BGP to follow normal BGP procedures when generating the `MED` attribute for the specified neighbor for EVPN. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change the `MED` when sending an update to the neighbor.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn attribute-mod med enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod nexthop</h>

Configures BGP to follow normal BGP procedures when generating the `NEXT_HOP` attribute for the specified neighbor for EVPN. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change `NEXT_HOP` when sending an update to the neighbor.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn attribute-mod nexthop enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn state</h>

Enables and disables the EVPN address family for the specified neighbor. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`  | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn nexthop-setting</h>

Configures the BGP next hop value of advertised EVPN routes for the BGP neighbor. You can specify `auto` to follow regular BGP next hop determination rules, `self` to set the next hop to itself for route advertisement excluding reflected routes, or `force` to set the next hop to itself for route advertisement including reflected routes. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`  | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn nexthop-setting force
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound route-map</h>

Configures the route map to use for inbound EVPN policies.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`  | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy inbound route-map myroutemap
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound route-map</h>

Provides the route map to use for outbound EVPN policies.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`  | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound route-map myroutemap
```
HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound unsuppress-map</h>

Configures the route map you want to use to unsuppress EVPN routes selectively when advertising to this neighbor; these are routes that have been suppressed due to aggregation configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`  | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound unsuppress-map none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn prefix-limits inbound maximum</h>

Configures the maximum number of inbound prefixes allowed from the BGP neighbor for EVPN. You can set a value between 0 and 4294967295 or `none`.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn prefix-limits inbound maximum 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn prefix-limits inbound reestablish-wait</h>

Configures the time in seconds to wait before reestablishing the BGP session with a neighbor. The default value is `auto`, which uses standard BGP timers and processing (typically between 2 and 3 seconds). You can set a value between 1 and 65535.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn prefix-limits inbound reestablish-wait 60
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn prefix-limits inbound warning-only</h>

Configures the switch to generate a warning syslog message only when the number of BGP prefixes from the neighbor exceeds a percentage of the maximum limit but does not bring down the BGP session. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn prefix-limits inbound warning-only enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn prefix-limits warning-threshold</h>

Configures when to generate a warning syslog message and bring down the BGP session (if `warning-only` is set to off) when the number of BGP prefixes from the neighbor exceeds a percentage of the maximum limit. For example, if the maximum prefix limit is 3 and the warning threshold is 60, the switch generates a warning message when the number of BGP prefixes from the BGP neighbor is more than 60 percent of 20 (12 prefixes). You can set a value between 0 and 100.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn prefix-limits inbound warning-threshold 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn route-reflector-client</h>

Configures the BGP node as a route reflector for the BGP neighbor for EVPN. The default setting is off`.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn route-reflector-client on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn soft-reconfiguration</h>

Turns on soft configuration so that received EVPN routes from the neighbor that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP updates. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn soft-reconfiguration enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn add-path-tx</h>

Configures BGP to advertise more than just the best path for an EVPN prefix. You can specify `all-paths` to advertise all known paths to the peers in the peer group or `best-per-as` to advertise only the best path learned from each AS. The default setting is off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn add-path-tx best-per-as
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn enable</h>

Configures BGP to allow a received AS path to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn aspath allow-my-asn enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn occurrences</h>

Indicates the maximum number of times you can receive the ASN of the local system in the received `AS_PATH`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath allow-my-asn occurrences 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn origin</h>

Configures BGP to allow a received AS path to contain the ASN of the local system only if it is the originating AS.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath allow-my-asn origi on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath private-as </h>

Configures what action to take with private ASNs. You can specify `none` to take no action, `remove`, to remove any private ASNs in the update to the peers in the peer group, or `replace` to replace any private ASNs in the update to the peers with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn aspath private-as  replace
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath replace-peer-as </h>

Configures BGP to replace the AS path in an outgoing update that contains the ASN of the peers in the peer group with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn aspath replace-peer-as on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod aspath</h>

Configures BGP to follow normal EVPN BGP procedures when generating the `AS_PATH` attribute for the peer group in the specified VRF. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn attribute-mod aspath enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod med</h>

Configures BGP to follow normal BGP procedures when generating the `MED` attribute for the specified peer group. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change the `MED` when sending an update to the peer group.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn attribute-mod med enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod nexthop</h>

Configures BGP to follow normal BGP procedures when generating the `NEXT_HOP` attribute for the specified peer group. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change `NEXT_HOP` when sending an update to the peer group.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn attribute-mod nexthop enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn state</h>

Enables and disables EVPN for the BGP peer group. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn nexthop-setting</h>

Configures the BGP next hop value of advertised EVPN routes for the peers in the peer group. You can specify `auto` to follow regular BGP next hop determination rules, `self` to set the next hop to itself for route advertisement excluding reflected routes, or `force` to set the next hop to itself for route advertisement including reflected routes. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn nexthop-setting self
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound route-map</h>

Configures the EVPN route map you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn policy inbound route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound route-map</h>

Configures the EVPN route map you want to apply to updates sent to the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn policy outbound route-map routemap2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound unsuppress-map</h>

Configures the route map you want to use to unsuppress EVPN routes selectively when advertising to the peers in the peer group; these are routes that have been suppressed due to aggregation configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn policy outbound unsuppress-map map3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn prefix-limits inbound maximum</h>

Configures the maximum number of inbound prefixes allowed from the BGP peers in the peer group for EVPN. You can set a value between 0 and 4294967295 or `none`.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn prefix-limits inbound maximum 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn prefix-limits inbound reestablish-wait</h>

Configures the time in seconds to wait before reestablishing the BGP session with the peers in the peer group. The default value is `auto`, which uses standard BGP timers and processing (typically between 2 and 3 seconds). You can set a value between 1 and 65535.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn prefix-limits inbound reestablish-wait 60
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn prefix-limits inbound warning-only</h>

Configures the switch to generate a warning syslog message only when the number of BGP prefixes from the peers in the peer group exceeds a percentage of the maximum limit but does not bring down the BGP session. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn prefix-limits inbound warning-only enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn prefix-limits warning-threshold</h>

Configures when to generate a warning syslog message and bring down the BGP session (if `warning-only` is set to off) when the number of BGP prefixes from the peers in the peer group exceeds a percentage of the maximum limit. For example, if the maximum prefix limit is 3 and the warning threshold is 60, the switch generates a warning message when the number of BGP prefixes from the BGP peers is more than 60 percent of 20 (12 prefixes). You can set a value between 0 and 100.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn prefix-limits inbound warning-threshold 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn route-reflector-client</h>

Configures the BGP node as a route reflector for the BGP peers in the peer group for EVPN. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn route-reflector-client enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn soft-reconfiguration</h>

Turns on soft configuration so that received EVPN routes from the peers in the peer group that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP updates. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn soft-reconfiguration enabled
```
