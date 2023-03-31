---
title: PBR
author: Cumulus Networks
weight: 640
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> router pbr

Configures PBR on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>`  |  The interface you want to configure.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pbr
```

- - -

## nv set interface \<interface-id\> router pbr map \<pbr-map-id\>

Applies a PBR policy on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>`  |  The interface you want to configure.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pbr map MAP1
```

- - -

## nv set router pbr

Configures global PBR (Policy-based Routing) settings.

- - -

## nv set router pbr enable

Enables or disables PBR. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr enable on
```

- - -

## nv set router pbr map \<pbr-map-id\>

Configures the name of the PBR route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\>

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
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 10
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action

Sets the action you want the PBR map rule to take, such as apply a net hop group or a VRF to a policy.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id> `  |  The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 action vrf RED
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\>

Configures the next hop group you want to apply to the policy map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>`  |  The PBR route map name. |
| `<rule-id>`     |  The PBR rule number. |
| `<nexthop-group-id>`  | The next hop group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 action nexthop-group group1
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action vrf \<vrf-name\>

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
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 action vrf RED
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match

Sets the match criteria you want to use for the PBR map rule.

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match destination-ip \<ipv4-prefix\>|\<ipv6-prefix\>

Sets PBR to match packets according to the destination IP prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |
| `<ipv4-prefix>` or `<ipv6-prefix>` | The destination IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 10 match destination-ip 10.1.2.0/24
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match dscp

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
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 match dscp 10
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match ecn

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
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 match ecn 3
```

- - -

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match source-ip \<ipv4-prefix\>|\<ipv6-prefix\>

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
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 10 match source-ip 10.1.4.1/24 
```

- - -

## nv set system global reserved routing-table pbr

Configures the reserved routing table ranges for PBR.

- - -

## nv set system global reserved routing-table pbr begin

Configures the starting reserved routing table range for PBR. You can specify a value between 10000 and 4294966272.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global reserved routing-table pbr begin 140000
```

- - -

## nv set system global reserved routing-table pbr end

Configures the end of the reserved routing table range for PBR. You can specify a value between 10000 and 4294966272.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global reserved routing-table pbr end 150000
```

- - -
