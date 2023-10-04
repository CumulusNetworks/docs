---
title: PBR
author: Cumulus Networks
weight: 640

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> router pbr</h>

Configures PBR on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>`  |  The interface you want to configure.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pbr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pbr map \<pbr-map-id\></h>

Applies a PBR policy on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>`  |  The interface you want to configure.  |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pbr map MAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr</h>

Configures global PBR (Policy-based Routing) settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr enable</h>

Enables or disables PBR. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\></h>

Configures the name of the PBR route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\></h>

Configures the PBR route map rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action</h>

Sets the action you want the PBR map rule to take, such as apply a next hop group or a VRF to a policy.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id> `  |  The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10 action vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\></h>

Configures the next hop group you want to apply to the policy map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>`  |  The PBR route map name. |
| `<rule-id>`     |  The PBR rule number. |
| `<nexthop-group-id>`  | The nexthop group name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10 action nexthop-group group1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action vrf \<vrf-name\></h>

Sets the VRF you want to apply to the policy map. If you do not set a VRF, the rule uses the VRF table set for the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>`  |  The PBR route map name. |
| `<rule-id>`     |  The PBR rule number. |
| `<vrf-name>`    |  The VRF you want to apply to the policy map. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10 action vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match</h>

Sets the match criteria you want to use for the PBR map rule.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match destination-ip \<ip-address\></h>

Sets PBR to match packets according to the destination IP prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |
| `<ip-address>` | The destination IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10 match destination-ip 10.1.2.0/24
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match dscp</h>

Sets PBR to match packets according to the DSCP field in the IP header. The DSCP value can be an integer between 0 and 63 or the DSCP codepoint name.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10 match dscp 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match ecn</h>

Sets PBR to match packets according to the ECN field in the IP header. The ECN value can be an integer between 0 and 3.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>` |  The PBR rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10 match ecn 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match source-ip \<ipv4-prefix\>|\<ipv6-prefix\></h>

Sets PBR to match packets according to the source IP prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |
| `<ipv4-prefix>` or `<ipv6-prefix>` | The source IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pbr map map1 rule 10 match source-ip 10.1.4.1/24 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved routing-table pbr</h>

Configures the reserved routing table ranges for PBR.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved routing-table pbr begin</h>

Configures the starting reserved routing table range for PBR. You can specify a value between 10000 and 4294966272.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system global reserved routing-table pbr begin 140000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved routing-table pbr end</h>

Configures the end of the reserved routing table range for PBR. You can specify a value between 10000 and 4294966272.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system global reserved routing-table pbr end 150000
```
