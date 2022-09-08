---
title: Set Commands
author: Cumulus Networks
weight: 30
product: Cumulus Linux
type: nojsscroll
---
This section describes all the `nv set` commands, together with their attributes and identifiers.

## nv set router

Configures global routing settings for BGP, OSPF, PIM, IGMP, VRR, VRRP, router policies, next hop groups, and adaptive routing.

### Usage

`nv set router [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop-group`| Configures next hop groups.|
| `pbr`| Configures global PBR (Policy-based Routing) settings. |
| `policy`| Configures router policies.|
| `bgp`| Configures global BGP (Border Gateway Protocol) settings.|
| `ospf`| Configures global OSPF (Open Shortest Path First) settings.|
| `pim`| Configures global PIM (Protocol Independent Multicast) settings.|
| `igmp`| Configures global IGMP (Internet Group Management Protocol) settings.|
| `vrrp`| Configures global VRRP (Virtual Router Redundancy) settings.|
| `vrr`:| Configures global VRR (Virtual Router Redundancy Protocol) settings.|
| `adaptive-routing`| Configures adaptive routing settings.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router nexthop-group \<nexthop-group-id\>

Sets the name of the next hop group.

### Usage

`nv set router nexthop-group <nexthop-group-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `via` | Configures the next hop. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1
```

## nv set router nexthop-group \<nexthop-group-id\> via \<via-id\>

Sets the IP addresses of the next hops in the next hop group.

### Usage

`nv set router nexthop-group <nexthop-group-id> via <via-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |
| `<via-id>` | The IP address of the next hop.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|  `interface`| Configures the interface to use for egress. If you do not specify an interface, the switch determines the interface automatically. This attribute is only valid for IPv4 or IPv6 addresses. |
| `vrf` | Configures the VRF to use for egress. If you do not specify the VRF, the switch uses the VRF that the route uses. This attribute is only valid for IPv4 or IPv6 addresses. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1 via 192.168.0.32
```

## nv set router nexthop-group \<nexthop-group-id\> via \<via-id\> interface \<interface-name\>

Sets the interface to use for egress. If you do not specify an interface, the switch determines the interface automatically. This attribute is only valid for IPv4 or IPv6 addresses.

### Usage

`nv set router nexthop-group <nexthop-group-id> via <via-id> interface [options] (auto|<interface-name>)`

### Default Setting

`auto`: The switch determines the interface automatically.

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |
| `<via-id>` | The IP address of the next hop.|
| `<interface-name>` | The interface to use for egress.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1 via 192.168.0.32 interface swp51
```

## nv set router nexthop-group \<nexthop-group-id\> via \<via-id\> vrf \<vrf-name\>

Sets the VRF to use for egress. If you do not specify the VRF, the switch uses the VRF that the route uses. This attribute is only valid for IPv4 or IPv6 addresses.

### Usage

`nv set router nexthop-group <nexthop-group-id> via <via-id> vrf [options] (auto|<vrf-name>)`

### Default Setting

`auto`: The switch uses the VRF that the route uses.

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |
| `<via-id>` | The IP address of the next hop.|
| `<vrf-name>` | The vrf to use for egress.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1 via 192.168.0.32 vrf RED
```

## nv set router pbr

Configures global PBR (Policy-based Routing) settings.

### Usage

`nv set router pbr [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `map`| Configures PBR policies.|
| `enable`| Turns the PBR `on` or `off`. The default is `off`. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router pbr map \<pbr-map-id\>

Configures the name of the PBR route map.

### Usage

`nv set router pbr map <pbr-map-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule`| Configures the PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\>

Configures the PBR route map rule number.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id>` | The PBR rule number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| match     |  Configures the PBR match criteria. |
| action    |  Configures the action to take; permit or deny.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 10
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match

Sets the match criteria you want to use for the PBR map rule.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> match [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id>`    | The PBR rule number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `destination-ip` |  Configures PBR to match a destination IP prefix. |
| `dscp` | Configures PBR to match packets according to the DSCP field in the IP header. The DSCP value can be an integer between 0 and 63 or the DSCP codepoint name.   |
| `ecn`  | Configures PBR to match packets according to the ECN field in the IP header. The ECN value can be an integer between 0 and 3. |
| `source-ip`  |  Configures PBR to match a source IP prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match source-ip \<ipv4-prefix\>|\<ipv6-prefix\>

Sets PBR to match packets according to the source IP prefix.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> match source-ip (<ipv4-prefix>|<ipv6-prefix>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
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

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match destination-ip \<ipv4-prefix\>|\<ipv6-prefix\>

Sets PBR to match packets according to the destination IP prefix.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> match destination-ip (<ipv4-prefix>|<ipv6-prefix>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
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

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match dscp

Sets PBR to match packets according to the DSCP field in the IP header. The DSCP value can be an integer between 0 and 63 or the DSCP codepoint name.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> match dscp [options] 0-63`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 match dscp 10
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match ecn

Sets PBR to match packets according to the ECN field in the IP header. The ECN value can be an integer between 0 and 3.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> match ecn [options] 0-3`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>` |  The PBR rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 match ecn 3
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action

Sets the action you want the PBR map rule to take, such as apply a net hop group or a VRF to a policy.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> action [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id> `  |  The PBR rule number. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop-group` | Configures the route through the nexthop-group. |
| `vrf`     | Configures the route through a VRF. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 action vrf RED
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\>

Configures the next hop group you want to apply to the policy map.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
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

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action vrf \<vrf-name\>

Sets the VRF you want to apply to the policy map. If you do not set a VRF, the rule uses the VRF table set for the interface.

### Usage

`nv set router pbr map <pbr-map-id> rule <rule-id> action vrf [options] <vrf-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
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

## nv set router pbr enable

Enables or disables PBR.

### Usage

`nv set router pbr enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pbr enable on
```

## nv set router policy

Configures a router policy.

### Usage

`nv set router policy [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute  |  Description   |
| ---------  | -------------- |
| `community-list` |  Configures a community list. |
| `as-path-list` | Configures an AS path list. |
| `ext-community-list` | Configures an Extended Community list. |
| `large-community-list` | Configures a Large Community list. |
| `prefix-list` | Configures prefix lists. |
| `route-map` | Configures route maps. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router policy community-list \<list-id\>

Configures the name of the community list you want to use to match BGP community policies.

### Usage

`nv set router policy community-list <list-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | | Configures the community list rule. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list 
```

## nv set router policy community-list \<list-id\> rule \<rule-id\>

Configures the community list rule number.

### Usage

`nv set router policy community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |
| `<rule-id>`  | The community list rule number. |

### Attributes

| Atrribute |  Description   |
| --------- | -------------- |
| `community` | Configures the community expression. |
| `action`    | Configures the action you want to take for a match; permit or deny. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
```

## nv set router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\>

Sets the name of the community you want to match.

### Usage

`nv set router policy community-list <list-id> rule <rule-id> community <community-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The community list name. |
| `<rule-id>` | The community list rule number. |
| `<community-id>` | The community number in AA:NN format or the well-known name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 community 100:100
```

## nv set router policy community-list \<list-id\> rule \<rule-id\> action

Sets the action you want to take when you meet the match criteria; permit or deny.

### Usage

`nv set router policy community-list <list-id> rule <rule-id> action [options] (permit|deny)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |
| `<rule-id>`  | The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
```

## nv set router policy as-path-list \<list-id\>

Sets the name of the AS path access list you want to use to match AS paths.

### Usage

`nv set router policy as-path-list <list-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name.|

### Attributes

| Atrribute |  Description   |
| --------- | -------------- |
| `rule`    |  Configures the AS path list rule. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist
```

## nv set router policy as-path-list \<list-id\> rule \<rule-id\>

Configures the AS Path list rule number.

### Usage

`nv set router policy as-path-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS Path list name. |
| `<rule-id>` |  The prefix list rule number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `action` |  Configures the action you want to take when there is a match, such as permit or deny. |
| `aspath-exp` | Configures the regular expression you want to use to match BGP AS paths. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10
```

## nv set router policy as-path-list \<list-id\> rule \<rule-id\> action

Sets the action you want to take for a match; permit or deny.

### Usage

`nv set router policy as-path-list <list-id> rule <rule-id> action [options] (permit|deny)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS path list name. |
| `<rule-id>` |  The AS path list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10 action permit
```

## nv set router policy as-path-list \<list-id\> rule \<rule-id\> aspath-exp \<bgp-regex\>

Configures the regular expression you want to use to match BGP AS paths.

### Usage

`nv set router policy as-path-list <list-id> rule <rule-id> aspath-exp [options] <bgp-regex>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name. |
| `<rule-id> ` | Th AS path list rule number. |
| `bgp-regex` | The regular expression you want to use to match BGP AS paths.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10 aspath-exp ^100_
```

## nv set router policy ext-community-list \<list-id\>

Sets the name of the Extended Community list you want to use to match BGP communities.

### Usage

`nv set router policy ext-community-list <list-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The extended community list name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures the extended community list rule. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\>

Sets the extended community list rule number.

### Usage

`nv set router policy ext-community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ext-community` | Configures the Extended Community expression. |
| `action `  | Configures the action you want to take when there is a match; permit or deny.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community

Sets the Extended Community name.

### Usage

`nv set router policy ext-community-list <list-id> rule <rule-id> ext-community [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<list-id>` |  The Extended Community list name. |
| `<rule-id>` | The Extended Community list rule number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rt ` | Configures the Route Target Extended Community. |
| `soo ` | Configures the site-of-origin (SoO) Extended Community.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community 64510:2
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt \<ext-community-id\>

Configures the Route Target Extended Community.

### Usage

`nv set router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |
| `<ext-community-id>` | The Extended Community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community rt 64510:1111
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo \<ext-community-id\>

Configures the site-of-origin (SoO) Extended Community to identify routes that originate from a certain site so that you can prevent readvertising that prefix back to the source site.

### Usage

`nv set router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id> ` | The community list name. |
| `<rule-id> ` |  The community list rule number. |
| `<ext-community-id>` | The Extended Community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community soo ????????
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> action

Configures the action to take on a match; permit or deny.

### Usage

`nv set router policy ext-community-list <list-id> rule <rule-id> action [options] (permit|deny)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 action permit
```

## nv set router policy large-community-list \<list-id\>

Configures the name of the Large Community list you want to use to match community based BGP policies.

### Usage

`nv set router policy large-community-list <list-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>  | The community list name |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` |  Configures the Large Community list rule. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist
```

## nv set router policy large-community-list \<list-id\> rule \<rule-id\>

Configures the Large Community list rule number.

### Usage

`nv set router policy large-community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The community list name |
| `<rule-id>`  | The community list rule number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `large-community`  | Configures the large community expression. |
| `action`  |  Configures the action you want to take when there is a match; permit or deny. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10
```

## nv set router policy large-community-list \<list-id\> rule \<rule-id\> large-community \<large-community-id\>

Configures the community names for the large community list.

### Usage

`nv set router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id> ` | The community list rule number. |
| `<large-community-id>` | The community number in AA:BB:CC format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10 large-community ?????
```

## nv set router policy large-community-list <list-id> rule <rule-id> action

### Usage

`nv set router policy large-community-list <list-id> rule <rule-id> action [options] (permit|deny)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id> ` | The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10 action permit
```

## nv set router policy prefix-list \<prefix-list-id\>

Configures the name of the prefix list you want to use to match IPv4 and IPv6 address prefixes.

### Usage

`nv set router policy prefix-list <prefix-list-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures the prefix list rule number. |
| `type` | Configures the prefix list type. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\>

Configures the prefix list rule number.

### Usage

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>`  | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |

### Attributes

| Atrribute |  Description   |
| --------- | -------------- |
| `match` | Configures the prefix list match criteria. |
| `action` | Configures the action you want to take when there is a match; permit or deny. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\>

Configures the prefix match criteria you want to use.

### Usage

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id> ` | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix you want to match.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `max-prefix-len` | Configures the maximum prefix length to match. |
| `min-prefix-len` | Configures the minimum prefix length to match. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> min-prefix-len

Configures the minimum prefix length you want to match.

### Usage

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len [options] 0-128`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 min-prefix-len 30
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> max-prefix-len

Configures the maximum prefix length you want to match. You can specify a value between 0 and 128.

### Usage

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len [options] 0-128`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name.  |
| `<rule-id>` |  The prefix list rule number. |
| `<match-id>` |  The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 max-prefix-len 30
```

## nv set router policy prefix-list \<list-id\> rule \<rule-id\> action

Configures the action to take on a match; permit or deny.

### Usage

`nv set router policy prefix-list <list-id> rule <rule-id> action [options] (permit|deny)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |
| `<rule-id>` |  The prefix list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 action permit
```

## nv set router policy prefix-list \<list-id\> type

Configures the type of prefix list; IPv4 or IPv6.

### Usage

`nv set router policy prefix-list <prefix-list-id> type [options] (ipv4|ipv6)`

### Default Setting

`ipv4`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist type ipv4
```

## nv set router policy route-map \<route-map-id\>

Configures the name of the route map you want to use for policy configuration.

### Usage

`nv set router policy route-map <route-map-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` |  The route map name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures the route map rule. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\>

Configures the route map rule number.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `match` |  Configures the route map match criteria. |
| `set` | Configures the route map set criteria. |
| `action` | Configures the action you want to take when there is a match; permit or deny.   |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match

Configures the match criteria you want to use for the route map rule.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`as-path-list` | Configures the BGP AS path list.|
|`community-list` | Configures the BGP community list.|
|`evpn-route-type` | Configures the EVPN route type.|
|`evpn-vni` | Configures the VNI ID|
|`interface` |  Configures the first hop interface or VRF|
|`ip-nexthop` |  Configures the IP nexthop address.|
|`ip-nexthop-len` | Configures the IP nexthop prefix length.|
|`ip-nexthop-list` | Configures the IP prefix list.|
|`ip-nexthop-type` |Configures the IP nexthop type.|
|`ip-prefix-len`  | Configures the IP address prefix length.|
|`ip-prefix-list` | Configures the IP prefix list.|
|`large-community-list` | Configures the BGP Large Community list. |
|`local-preference` | Configures the local preference for the route. |
|`metric` | Configures the metric for the route. |
|`origin` | Configures the BGP origin. |
|`peer` | Configures the BGP peer. |
|`source-protocol` | Configures the protocol through which the route is learned. |
|`source-vrf` |Configures the source VRF |
|`tag`  |Configures the tag. |
|`type` | Configures the match prefix type. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-list \<instance-name\>

Configures the IP prefix list to use as a match in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>`  |  The route map rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-len

Configures the IP address prefix length you want to match. You can specify a value between 0 and 128.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len [options] 0-128`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-len 128
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-list \<instance-name\>

Configures the IP next hop list you want to use as a match in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-len

Configures the route map to match an IP nexthop prefix length.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len [options] 0-32`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-len 32
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop \<ipv4\>|\<ipv6\>

Configures the route map to match the IP address of a nexthop.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop [options] (<ipv4>|<ipv6>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<ipv4>` or `<ipv6>` | The IPv4 or IPv6 address of the next hop.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop 10.10.101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-type blackhole

Configures the route map to match a null route (blackhole).

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type [options] blackhole`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-type blackhole
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match as-path-list \<instance-name\>

Configures the name of the BGP AS path list you want use in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match as-path-list [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match as-path-list MYLIST
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match community-list \<instance-name\>

Configures the name of the BGP community list you want to use in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match community-list [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match community-list MYLIST
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match large-community-list \<instance-name\>

Configures the name of the BGP Large Community list you want to use in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match large-community-list [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match large-community-list MYLIST
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match metric \<value\>

Configures the route metric (the cost values used by routers to determine the best path to a destination network) you want to use as a match in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match metric [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match metric 1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match interface \<interface-name\>|\<vrf-name\>

Configures the interface you want to use as a match in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match interface (<interface-name>|<vrf-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match interface swp51
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match tag

Configures the BGP tag you want to use as a match in the route map. You can specify a value between 1 and 4294967295.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match tag [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match tag 10
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-protocol

Configures the source protocol you want to use as a match in the route map. The source protocol is the protocol through which the switch learns the route. You can specify `bgp`, `connected`, `kernel`, `ospf`, `spf6`, `sharp` or `static`.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match source-protocol [options] (bgp|connected|kernel|ospf|ospf6|sharp|static)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match source-protocol bgp
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match origin

Configures the BGP origin you want to use as a match in the route map. You can specify `egp`, `igp`, or `incomplete`.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match origin [options] (egp|igp|incomplete)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match origin igp
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match peer

Configures the BGP peer you want to use as a match in the route map. You can specify `local`, the interface, or the IPv4 or IPv6 address.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match peer [options] (local|<interface-name>|<ipv4>|<ipv6>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match peer swp51
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match local-preference

Configures the local preference of the route you want to match in the route map. You can specify a value between 0 and 4294967295.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match local-preference [options] 0-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match local-preference 300
```

## nv set router policy route-map <route-map-id> rule <rule-id> match evpn-route-type

Configures the EVPN route type you want to match in the route map. You can specify type 2 (MAC or IP advertisement routes), type 3 (Inclusive multicast Ethernet tag routes), or type 5 (IP prefix routes).

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match evpn-route-type [options] (macip|imet|ip-prefix)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match evpn-route-type macip
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-vni \<value\>

Configures the VNI ID you want to use a match in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match evpn-vni [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match evpn-vni 10
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-vrf \<vrf-name\>

Configures the source VRF you want to use as a match in the route map.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match source-vrf [options] <vrf-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match source-vrf RED
```

## nv set router policy route-map <route-map-id> rule <rule-id> match type

Configures the the route types you want to use as a match in the route map. You can specify IPv4 or IPv6 routes.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> match type [options] (ipv4|ipv6)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ipv4
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set

Configures the route map rule set.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `as-path-prepend` |  Sets the BGP AS Path you want to prepend for a matched route. |
| `community` |  Sets the BGP Community attribute for a matched route. |
| `large-community` | Sets the BGP Large Community attribute for a matched route. |
| `aggregator-as` | Sets the aggregator AS Number for a matched route. |
| `as-path-exclude` |  Sets the BGP AS Path you want to exclude from a matched route. |
| `atomic-aggregate` |  Sets the BGP atomic aggregate. |
| `community-delete-list` | Sets the Community delete list. |
| `ext-community-bw` |Sets the Extended Community link bandwidth. |
| `ext-community-rt`| Sets the route target Extended Community for a matched route. |
| `ext-community-soo` | Sets the site of the origin Extended Community for a matched route. |
| `ip-nexthop ` | Sets the IP nexthop for a matched route. |
| `ipv6-nexthop-global`| Sets the IPv6 nexthop global address for a matched route. |
| `ipv6-nexthop-local` | sets the IPv6 nexthop local address for a matched route. |
| `ipv6-nexthop-prefer-global` | Sets the global address you prefer to use as the IPV6 next hop for a matched route. |
| `large-community-delete-list` | Sets the Large Community delete list for a matched route. |
| `local-preference` | Sets the local preference for a matched route. |
| `metric ` | Sets the metric value for the destination routing protocol for a matched route. |
| `metric-type` | Sets the metric type for a matched route. |
| `origin` | Sets the BGP origin for a matched route. |
| `source-ip` | Sets the source IP address for a matched route. |
| `tag` | Sets the Tag value for the routing protocol for a matched route. |
| `weight` | Sets the BGP weight for a matched route. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend

Sets the BGP AS Path you want to prepend for a matched route.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `as` | Configures the BGP AS number. |
| `last-as` | Configures the number of times to insert the AS number of the peer. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend as

Sets the BGP AS number to prepend for a matched route.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as 65101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend last-as

Sets the last BGP AS path to prepend for a matched route. You can set a value between 1 and 10.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as last-as 4
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community \<community-id\>

Sets the BGP Community attribute for a matched route.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set community <community-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<community-id>` | The Community number in AA:NN format or the well-known name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set community 100:100
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community \<large-community-id\>

Sets the Large BGP Community for a matched route.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<large-community-id>` | The Large Community number in AA:BB:CC format.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set large-community ????
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\>

Sets the aggregator AS Number for a matched route.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN number.|

### Attributes

| Atrribute |  Description   |
| --------- | -------------- |
| `address` | Configures the set of IPv4 addresses. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address \<ipv4-address-id\>

Sets the originating AS of an aggregated route if there is a match.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN number.|
| `<ipv4-address-id>` |  The IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101 address 10.10.10.01
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-exclude

Configures a set clause in the route map to remove the AS number from the AS Path attribute of the route. You can specify a value between 1 and 4294967295.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-exclude [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-exclude 65101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set atomic-aggregate (on|off)

Configures a set clause in the route map to inform BGP peers that the local router is using a less specific (aggregated) route to a destination. You can specify `on` or `off`.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set atomic-aggregate on
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-rt \<route-distinguisher\>

Sets the route target Extended Community for a matched route.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-rt [options] <route-distinguisher>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
|`<route-distinguisher>` | The route distinguisher. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-rt 64510:1111
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-soo \<route-distinguisher\>

Sets the site-of-origin (SoO) Extended Community for a matched route.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-soo [options] <route-distinguisher>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<route-distinguisher>` |The route distinguisher. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-soo ????
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-bw

Sets the BGP Extended Community for a matched route. You can specify `cumulative` `multipaths` `cumulative-non-transitive`, or `multipaths-non-transitive`.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-bw [options] (cumulative|multipaths|cumulative-non-transitive|multipaths-non-transitive)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-bw multipaths.
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set local-preference

Sets the BGP local preference for a matched route. You can specify a value between 0 and 4294967295.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set local-preference [options] 0-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set local-preference 300
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set weight

Sets the BGP weight value for a matched route. You can specify a value between 0 and 4294967295.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set weight [options] 0-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set weight 300
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric

Configures a set clause in the route map for the metric value for the destination routing protocol. You can set `metric-plus`, `metric-minus`, `rtt`, `rtt-plus`, or `rtt-minus`.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set metric [options] (metric-plus|metric-minus|rtt|rtt-plus|rtt-minus)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set metric metric-minus
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric type

Configures a set clause in the route map for the metric type for routes that match the map. The metric type is used by the the OSPF protocol. You can set OSPF external type 1 metric or OSPF external type 2 metric.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set metric [options] (type-1|type-2)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set metric type type-2
```

## nv set router policy route-map <route-map-id> rule <rule-id> set origin

Configures a set clause in the route map for the BGP origin code for the matched route. You can specify `egp` (the switch learns the origin of the route from an exterior routing protocol with the given autonomous system number) `igp` (the switch learns the the origin of the route from an interior routing protocol), or `incomplete` (the origin of the route is unknown).

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set origin [options] ((egp|igp|incomplete) `

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set origin igp
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set tag

Configures a set clause in the route map for the tag value for the routing protocol.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set metric [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set tag 100
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-global \<ipv6\>

Configures a set clause in the route map for IPv6 next hop global address.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global [options] <ipv6>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-global 2001:db8:0002::0a00:0002
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-local \<ipv6\>

Configures a set clause in the route map for the IPv6 next hop local address.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local [options] <ipv6>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-local 2001:db8:0002::0a00:0002
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-prefer-global

Configures a set clause in the route map to use the global address as the IPv6 next hop.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-prefer-global on
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ip-nexthop

Configures a set clause in the route map for the next hop address for an incoming packet regardless of the explicit route for the packet. You can specify the IP address of the peer, or leave it unchanged.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set ip-nexthop [options] (unchanged|peer-addr)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ip-nexthop peer-addr
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set source-ip

Configures a set clause in the route map for the source IP address. You can specify an IPv4 or IPv6 address.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set source-ip [options] (<ipv4>|<ipv6>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set source-ip 10.1.10.0
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community-delete-list

Configures a set clause in the route map to remove BGP communities from being advertised to other BGP routes.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set community-delete-list [options] (<instance-name>|<integer>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set community-delete-list communitylist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community-delete-list 

Configures a set clause in the route map to remove BGP Large Communities from being advertised to other BGP routes.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list [options] (<instance-name>|<integer>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set large-community-delete-list largecommunitylist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action

Configures the route map rule action; permit or deny.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> action [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `deny`   |  Configures the action of the rule to deny. |
| `permit` |  Configures the action of the rule to permit. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action deny

Configures the route map rule action to deny.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> action deny [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 deny
```

## nv set router policy route-map <route-map-id> rule <rule-id> action permit

Configures the route map rule action to permit.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> action permit [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `exit-policy` | Configures the permit action exit policy. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy

Configures the permit action exit policy.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures jump to specific rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit exit-policy
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy rule \<value\>

Configures the route map to go to specific rule when the matching conditions are met.

### Usage

`nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit exit-policy rule 20
```

## nv set router bgp

Configures BGP global configuration.

### Usage

`nv set router bgp [options] [<attribute> ...`

### Default Setting

`off`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `graceful-restart` | Configures BGP graceful restart globally so that a BGP speaker can signal to its peers that it can preserve its forwarding state and continue data forwarding during a restart. It also enables a BGP speaker to continue to use routes announced by a peer even after the peer has gone down.|
| `convergence-wait` | Configures read-only mode so that you can reduce CPU and network usage when restarting the BGP process.|
| `enable` |  Turns BGP on or off. The default is off.|
| `autonomous-system` |  Configures the ASN to identify the BGP node. This command configures the ASN for all VRFs if a single AS is in use; otherwise, you must set an ASN for every VRF.|
| `graceful-shutdown` |  Configures graceful shutdown, which forces traffic to route around the BGP node and reduces packet loss during planned maintenance of a router or link. |
| `policy-update-timer` | Configures the wait time in seconds before processing updates to policies to ensure that a series of changes are processed together. |
|` router-id`  | Configures the BGP router ID on the switch, which is a 32-bit value and is typically the address of the loopback interface. This command configures a BGP router ID for all VRFs if a common VRF is used; otherwise, you must set a router ID for every VRF. |
| `wait-for-install` | Configures BGP to wait for a response from the RIB indicating that the routes installed in the RIB are also installed in the ASIC before sending updates to peers. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router bgp graceful-restart

Configures BGP graceful restart globally on the switch so that a BGP speaker can signal to its peers that it can preserve its forwarding state and continue data forwarding during a restart. It also enables a BGP speaker to continue to use routes announced by a peer even after the peer has gone down.

### Usage

`nv set router bgp graceful-restart [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `mode` | Configures the role of the router during graceful restart. You can specify `helper-only`, where the router is in helper mode, `full`, where the router is in both helper and restarter mode, or `off`, where BGP graceful restart is off. |
| `path-selection-deferral-time` | Configures the number of seconds a restarting peer defers path-selection when waiting for the EOR (end of RIB) marker from peers. The default is 360 seconds. You can set a value between 0 and 3600.|
| `restart-time` |  Configures the number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. The default is 120 seconds. You can set a value between 1 and 4095. |
| `stale-routes-time` | Configures the number of seconds to hold stale routes for a restarting peer. The default is 360 seconds. You can set a value between 1 and 4095. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router bgp graceful-restart mode (off|helper-only|full)

Configures the role of the router during BGP graceful restart. You can specify `helper-only`, where the router is in helper mode, `full`, where the router is in both helper and restarter mode, or `off`, where BGP graceful restart is off.

### Usage

`nv set router bgp graceful-restart mode [options] (off|helper-only|full)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart mode full
```

## nv set router bgp graceful-restart restart-time

Configures the number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. You can set a value between 1 and 3600.

### Usage

`nv set router bgp graceful-restart restart-time [options] 1-3600`

### Default Setting

120 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp restart-time 400
```

## nv set router bgp graceful-restart path-selection-deferral-time

Configures the number of seconds a restarting peer defers path-selection when waiting for the EOR (end of RIB) marker from peers. You can set a value between 0 and 3600.

### Usage

`nv set router bgp graceful-restart path-selection-deferral-time [options] 0-3600`

### Default Setting

360 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart path-selection-deferral-time 300
```

## nv set router bgp graceful-restart stale-routes-time

Configures the number of seconds to hold stale routes for a restarting peer. You can set a value between 1 and 360.

### Usage

`nv set router bgp graceful-restart stale-routes-time [options] 1-3600`

### Default Setting

360 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart stale-routes-time 400
```

## nv set router bgp convergence-wait

Configures read-only mode so that you can reduce CPU and network usage when restarting the BGP process.

### Usage

`nv set router bgp convergence-wait [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `establish-wait-time` | Configures the maximum time to wait to establish BGP sessions. BGP does not track any peers that do not come up in this time for convergence-wait purposes. A value of 0 means there is no maximum time and BGP tracks peers for convergence time.|
| `time`  | Configures the time to wait for peers to send an EOR (end of RIB) before the switch selects the path, installs and advertises the route. BGP uses the time to wait during startup or when all peerings flap. A value of zero means that there is no wait time. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router bgp convergence-wait time

Configures the time to wait for peers to send an EOR (end of RIB) before the switch selects the path, installs and advertises the route. BGP uses the time to wait during startup or when all peerings flap. You can set a value between 0 and 3600 seconds. A value of zero means that there is no wait time.

### Usage

`nv set router bgp convergence-wait time [options] 0-3600`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp convergence-wait time 300
```

## nv set router bgp convergence-wait establish-wait-time

Configures the maximum time to wait to establish BGP sessions. BGP does not track any peers that do not come up in this time for convergence-wait purposes.  You can set a value between 0 and 600 seconds.  A value of 0 means there is no maximum time and BGP tracks peers for convergence time.

### Usage

`nv set router bgp convergence-wait establish-wait-time [options] 0-3600`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp establish-wait-time time 200
```

## nv set router bgp enable

Turns BGP on or off. The default is off.

### Usage

`nv set router bgp enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp enable on
```

## nv set router bgp autonomous-system

Configures the ASN to identify the BGP node. This command configures the ASN for all VRFs if a single AS is in use; otherwise, you must set an ASN for every VRF.

### Usage

`nv set router bgp autonomous-system [options] (1-4294967295|none|leaf|spine)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp autonomous-system 65101
```

## nv set router bgp router-id

Configures the BGP router ID on the switch, which is a 32-bit value and is typically the address of the loopback interface. This command configures a BGP router ID for all VRFs if a common VRF is used; otherwise, you must set a router ID for every VRF.

### Usage

`nv set router bgp router-id [options] (none|<ipv4>)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp router-id 10.10.10.1
```

## nv set router bgp policy-update-timer

Configures the wait time in seconds before processing updates to policies to ensure that a series of changes process together. You can set a value between o and 600.

### Usage

`nv set router bgp policy-update-timer [options] 0-600`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp policy-update-timer 200
```

## nv set router bgp graceful-shutdown (on|off)

Configures graceful shutdown, which forces traffic to route around the BGP node and reduces packet loss during planned maintenance of a router or link.

### Usage

`nv set router bgp graceful-shutdown [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-shutdown on
```

## nv set router bgp wait-for-install

Configures BGP to wait for a response from the RIB indicating that the routes installed in the RIB are also installed in the ASIC before sending updates to peers.

### Usage

`nv set router bgp wait-for-install [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp wait-for-install on
```

## nv set router ospf

Configures OSPF globally on the switch.

### Usage

`nv set router ospf [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `timers` | Configures OSPF timers. |
| `enable` | Turns OSPF on or off. The default is off. |
| `router-id` | Configures the OSPF router ID. This command configures the router ID for all VRFs if a common one is used; otherwise, you must set the router ID for every VRF. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers

Configures OSPF Link State Advertisement (LSA) and Shortest Path First (SPF) timers, and the refresh interval.

### Usage

`nv set router ospf timers [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| --------- | -------------- |
| `lsa` | Configures LSA timers. |
| `spf` | Configures the SPF timers. |
| `refresh` | Configures the refresh interval in seconds to resend LSAs to prevent them from aging out.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers lsa

Configures LSA timers.

### Usage

`nv set router ospf timers lsa [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `min-arrival` |  Configures the minimum interval during which OSPF can accept the same LSA.|
| `throttle` |  Configures the delay in milliseconds between sending LSAs. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers lsa min-arrival

Configures the minimum interval in seconds during which OSPF can accept the same LSA. You can specify a value between 0 and 600000.

### Usage

`nv set router ospf timers lsa min-arrival [options] 0-600000`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers lsa min-arrival 300000
```

## nv set router ospf timers lsa throttle

Configures the amount of time after which OSPF sends LSAs. You can specify a value between 0 and 5000 milliseconds.

### Usage

`nv set router ospf timers lsa throttle [options] 0-5000`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers lsa throttle 3000
```

## nv set router ospf timers spf

Configures the SPF timers.

### Usage

`nv set router ospf timers spf [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `delay` | Configures the number of milliseconds to wait to do the SPF calculation after receiving the first topology change. |
| `holdtime` | Configures the amount of time to wait between consecutive SPF calculations.| 
| `max-holdtime` | Configures the maximum amount of time to wait between consecutive SPF calculations. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers spf delay

Configures the amount of time to wait to do the SPF calculation after receiving the first topology change. You can specify a value between 0 and 600000 milliseconds.

### Usage

`nv set router ospf timers spf delay [options] 0-600000`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf delay 300000
```

## nv set router ospf timers spf holdtime

Configures the amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

### Usage

`nv set router ospf timers spf holdtime [options] 0-600000`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf holdtime 300000
```

## nv set router ospf timers spf max-holdtime

Configures the maximum amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

### Usage

`nv set router ospf timers spf max-holdtime [options] 0-600000`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf max-holdtime 300000
```

## nv set router ospf timers refresh 10-1800

Configures the refresh interval in seconds to resend LSAs to prevent them from aging out. You can specify a value between 10 and 1800 seconds.

### Usage

`nv set router ospf timers refresh [options] 10-1800`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers refresh 100
```

## nv set router ospf enable

Turns OSPF on or off. 

### Usage

`nv set router ospf enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf enable on
```

## nv set router ospf router-id

Configures the OSPF router ID on the switch, which is a 32-bit value and is typically the address of the loopback interface. This command configures the router ID for all VRFs if a common one is used; otherwise, you must set the router ID for every VRF.

### Usage

`nv set router ospf router-id [options] (none|<ipv4>)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf router-id 10.10.10.1.
```

## nv set router pim

Configures PIM globally on the switch.

### Usage

`nv set router pim [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `timers` | Configures PIM timers. |
| `enable` | Turns PIM feature on or off. |
| `packets` |Configures the number of incoming packets to process from the neighbor. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router pim timers

Configures PIM timers.

### Usage

`nv set router pim timers [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `hello-interval` | Configures the interval in seconds at which the PIM router sends hello messages to discover PIM neighbors and maintain PIM neighbor relationships.  |
| `join-prune-interval` | configures the interval in seconds at which a PIM router sends join and prune messages to its upstream neighbors for a state update. |
| `keep-alive` |  Configures the timeout value for S,G stream, in seconds. |
| `register-suppress` | Configures the number of seconds during which to stop sending register messages to the RP. |
| `rp-keep-alive` | Configures the RP's timeout value, in seconds. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router pim timers hello-interval

Configures the interval in seconds at which the PIM router sends hello messages to discover PIM neighbors and maintain PIM neighbor relationships. You can specify a value between 1 and 180.

### Usage

`nv set router pim timers hello-interval [options] 1-180`

### Default Setting

30 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers hello-interval 60
```

## nv set router pim timers register-suppress

The number of seconds during which to stop sending register messages to the RP. You can specify a value between 5 and 60000 seconds.

### Usage

`nv set router pim timers register-suppress [options] 5-60000`

### Default Setting

60 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers register-suppress 20000
```

## nv set router pim timers join-prune-interval

Configures the interval in seconds at which a PIM router sends join and prune messages to its upstream neighbors for a state update. You can specify a value between 60 and 600 seconds.

### Usage

`nv set router pim timers join-prune-interval [options] 60-600`

### Default Setting

60 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers join-prune-interval 100
```

## nv set router pim timers keep-alive

Configures the timeout value for the S,G stream in seconds. You can specify a value between 31 and 60000.

### Usage

`nv set router pim timers keep-alive [options] 31-60000`

### Default Setting

210 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers keep-alive 10000
```

## nv set router pim timers rp-keep-alive

Configures the timeout value for the RP in seconds. You can specify a value between 31 and 60000.

### Usage

`nv set router pim timers rp-keep-alive [options] 31-60000`

### Default Setting

185 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers rp-keep-alive 10000
```


## nv set router pim enable (on|off)

Turns PIM on or off.

### Usage

`nv set router pim enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim enable on
```

## nv set router pim packets

Configures the number of incoming packets from the neighbor that PIM can process. You can specify a value between 1 and 100.

### Usage

`nv set router pim packets [options] 1-100`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim packets 50
```

## nv set router igmp

Configures IGMP globally on the switch.

### Usage

`nv set router igmp [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns IGMP on or off.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router igmp enable

Turns IGMP on or off.

### Usage

`nv set router igmp enable [options] (on|off)`

### Default Setting

`on`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router igmp enable on
```

## nv set router vrrp

Configures VRRP globally on the switch.

### Usage

`nv set router vrrp [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns VRRP on or off.|
| `advertisement-interval` | Configures the advertisement interval between successive advertisements by the master in a virtual router group. |
| `preempt` | Configures preempt mode, which lets the router take over as master for a virtual router group if it has a higher priority than the current master. |
| `priority` |  Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router vrrp enable

Turns VRRP on or off.

### Usage

`nv set router vrrp enable [options] (on|off)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp enable on
```

## nv set router vrrp priority

Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master.

### Usage

`nv set router vrrp priority [options] 1-2`54`

### Default Setting

100

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp priority 254
```

## nv set router vrrp preempt

Configures the router to take over as master for a virtual router group if it has a higher priority than the current master.

### Usage

`nv set router vrrp preempt [options] (on|off)`

### Default Setting

`on`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp preempt off
```

## nv set router vrrp advertisement-interval

Configures the advertisement interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950.

### Usage

`nv set router vrrp advertisement-interval [options] 10-40950`

### Default Setting

1000 milliseconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp advertisement-interval 2000
```

## nv set router vrr

Configures VRR globally on the switch.

### Usage

`nv set router vrr [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |   Turns VRR on or off. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set router vrr enable

Turns VRR on or off.

### Usage

`nv set router vrr [options]  (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrr enable on
```

## nv set router adaptive-routing

Configures adaptive routing globally on the switch. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

### Usage

`nv set router adaptive-routing [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` | Turns adaptive routing on or off. |

### Version History

Introduced in Cumulus Linux 5.1.0

## nv set router adaptive-routing enable

Turns adaptive routing on or off.

### Usage

`nv set router adaptive-routing [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router adaptive-routing enable on
```

## nv set platform

Configures the switch platform settings.

### Usage

`nv set platform [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `hardware` | Configures the switch hardware components. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware

Configures the hardware components of the switch. 

### Usage

`nv set platform hardware [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `component` | Configures a hardware component on the switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware component \<component-id\>

Configures a hardware component on the switch.

### Usage

`nv set platform hardware component <component-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `linecard` | Configures the properties of a line card. |
| `admin-state` | Configures the admin state of the hardware component. |
| `type` | Configures the conponent type. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware component \<component-id\> linecard

Configures the properties of a line card.

### Usage

`nv set platform hardware component <component-id> linecard [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `provision`  | Configures the provision line card type. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware component \<component-id\> linecard provision

Configures the properties of a line card. You can specify 16x100GE, 4x400GE, 8x200GE, or NONE.

### Usage

`nv set platform hardware component <component-id> linecard provision [options] (16x100GE|4x400GE|8x200GE|NONE)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set platform hardware component device linecard provision 4x400GE 
```

## nv set platform hardware component \<component-id\> type

Configures the conponent type; the switch or a line card.

### Usage

`nv set platform hardware component <component-id> type [options] (switch|linecard)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set platform hardware component device type linecard
```

## nv set platform hardware component \<component-id\> admin-state

Configures the admin state of the hardware component. You can specify enable or disable.

### Usage

`nv set platform hardware component <component-id> admin-state [options] (enable|disable)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set platform hardware component device admin-state enable
```

## nv set bridge

Configures a bridge on the switch.

### Usage

`nv set bridge [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain` |  Configures the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\>

Configures the bridge domain.

### Usage

`nv set bridge domain <domain-id> [options] [<attribute> ...]`

### Default Setting

`br_default`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<domain-id>` |  The name of the bridge domain. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `stp` |   Configures STP globally for all the interfaces on the bridge domain. |
| `multicast` |  Configures multicast on the bridge domain. |
| `vlan` | Configures a set of VLANs in the bridge domain. This is only applicable when the domain type is `vlan-aware`. |
| `encap` | Configures all the interfaces on this bridge domain to use encapsulation by default. |
| `mac-address` |  Configures the bridge domain to override the global MAC address. |
| `type` |  Configures the type of bridge domain. |
| `untagged` |  Configures the interfaces in the bridge domain to be trunk interfaces with a single untagged VLAN by default. Untagged packets on domain ports are in this VLAN. |
| `vlan-vni-offset` |  Configures a VNI offset while automatically mapping VLANs to VNIs.

### Version History

Introduced in Cumulus Linux 5.0.0 

## nv set bridge domain \<domain-id\> stp

Configures STP on the bridge domain.

### Usage

`nv set bridge domain <domain-id> stp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `state` |  Configures the STP state on the bridge domain; down or up.|
| `priority` | Configures the spanning tree priority. The bridge with the lowest priority is the root bridge. You must specify a value between 4096 and 32768. The value must be a multiple of 4096. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> stp priority

Configures the spanning tree priority. The bridge with the lowest priority is the root bridge. The priority must be a number between 0 and 61440, and must be a multiple of 4096.
 
### Usage

`nv set bridge domain <domain-id> stp priority [options] 4096-61440`

### Default Setting

32768

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default stp priority 8192
```

## nv set bridge domain \<domain-id\> multicast

Configures multicast on the bridge domain.

### Usage

`nv set bridge domain <domain-id> multicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `snooping` |  Configures IGMP and MLD snooping.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> multicast snooping

Configures IGMP and MLD snooping to prevent hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments and MLD snooping is for IPv6 environments.

### Usage

`nv set bridge domain <domain-id> multicast snooping [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `querier`|  Configures the IGMP and MLD querier. |
| `enable` | Turns IGMP and MLD snooping on or off. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> multicast snooping querier

Configures the IGMP and MLD querier. Without a multicast router, a single switch in an IP subnet can coordinate multicast traffic flows. This switch is the querier or the designated router. The querier generates query messages to check group membership, and processes membership reports and leave messages.

### Usage

`nv set bridge domain <domain-id> multicast snooping querier [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns the multicast querier on or off.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> multicast snooping querier enable

Turns the multicast querier on or off.

### Usage

`nv set bridge domain <domain-id> multicast snooping querier enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default multicast snooping querier enable on
```

## nv set bridge domain \<domain-id\> multicast snooping enable

Turns IGMP and MLD snooping on or off.

### Usage

`nv set bridge domain <domain-id> multicast snooping enable [options] (on|off)`


### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default multicast snooping enable on
```

## nv set bridge domain \<domain-id\> vlan \<vid\>

Configures the VLAN tag identifier.

### Usage

`nv set bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<domain-id>` |  The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `vni` |  Configures a layer 2 VNI. |
| `ptp` |  Configures PTP on the VLAN (on all the interfaces in this VLAN).|
| `multicast` |  Configures multicast on the VLAN.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10
```

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\>

Maps a VLAN to a VNI.

### Usage

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `flooding`  |  Configures how to handle BUM traffic.|
| `mac-learning` | Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs). You can override this setting with VNI-specific configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10`
```

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding

Configures how to handle BUM traffic.

### Usage

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `head-end-replication` |  Configures replication of BUM traffic where individual copies send to remote destinations.|
| `enable` | Turns flooding on or off for the specified VNI.|
| `multicast-group` | Configures BUM traffic received on the VNI to go to the specified multicast group where receivers who are interested in that group receive the traffic. This usually requires you to use PIM-SM in the network. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication \<hrep-id\>

Configures replication of BUM traffic where individual copies send to remote destinations.

### Usage

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |
| `<hrep-id>`  |  The IPv4 unicast addresses or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
```

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding enable

Turns flooding on or off for the VNI. 

### Usage

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding enable [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 flooding enable on
```

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding multicast-group \<ipv4-multicast\>

Configures BUM traffic to go to the specified multicast group, where receivers who are interested in that group recieve the traffic. This requires PIM-SM to be used in the network.

### Usage

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group [options] <ipv4-multicast>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |
| `<ipv4-multicast>` | The multicast group.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 flooding multicast-group 224.0.0.10
```

## nv set bridge domain \<domain-id\> vlan \<vid> vni \<vni-id\> mac-learning

Turns MAC learning on or off for the VNI.

### Usage

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> mac-learning [options] (on|off|auto)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 mac-learning off
```

## nv set bridge domain \<domain-id\> vlan \<vid\> ptp

Configures Precision Time Protocol (PTP) on the VLAN (all interfaces in this VLAN).

### Usage

`nv set bridge domain <domain-id> vlan <vid> ptp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`   |  Turns PTP on or off. The default is 'off'. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> vlan \<vid\> ptp enable

Turns PTP on or off for the specified VLAN.

### Usage

`nv set bridge domain <domain-id> vlan <vid> ptp enable [options]`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan vlan10 ptp enable on
```

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast

Configures multicast on the VLAN.

### Usage

`nv set bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `snooping`  |  Configures IGMP and MLD snooping on the VLAN. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping

Configures IGMP and MLD snooping on the VLAN.

### Usage

`nv set bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`querier` |  Configures the IGMP and MLD querier on the VLAN. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier

Configures the IGMP and MLD querier on the VLAN. 

### Usage

`nv set bridge domain <domain-id> vlan <vid> multicast snooping querier [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`source-ip`  | Configures the source IP address you want to use to send IGMP MLD queries. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier source-ip \<source-ip\>

Configures the source IP address you want to use to send IGMP MLD queries.

### Usage

`nv set bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip [options] <ipv4>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan vlan10 multicast snooping querier source-ip 10.10.10.1
```

## nv set bridge domain \<domain-id\> type vlan-aware

Configures the bridge domain to be VLAN-aware.

### Usage

`nv set bridge domain <domain-id> type [options] vlan-aware`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default type vlan-aware
```

## nv set bridge domain \<domain-id\> untagged

Configures the bridge domain to 


### Usage

`nv set bridge domain <domain-id> untagged [options] (1-4094|none)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default untagged none
```

## nv set bridge domain \<domain-id\> encap 802.1Q

Configures any interfaces in this bridge domain to use 802.1Q encapsulation by default.

### Usage

`nv set bridge domain <domain-id> encap [options] 802.1Q`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default encap 802.1Q
```

## nv set bridge domain \<domain-id\> mac-address

Configures any interfaces in this bridge domain to use this MAC address.

### Usage

`nv set bridge domain <domain-id> mac-address [options] (auto|<mac>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default mac-address 00:00:00:00:00:10
```

## nv set bridge domain \<domain-id\> vlan-vni-offset

Configures the VNI offset when mapping VLANs to VNIs automatically. You can set a value between 0 and 16773120. For example, if you specify an offset of 10000, the VNI is the VLAN plus 10000.

### Usage

`nv set bridge domain <domain-id> vlan-vni-offset [options] 0-16773120`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan-vni-offset 10000
```

## nv set mlag

Configures global Multi-chassis Link Aggregation (MLAG) properties.

### Usage

`nv set mlag [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `lacp-conflict` |  Configures the MLAG LACP conflict parameters. |
| `backup`  | Configures the IP address of the MLAG backup switch. The backup IP address is any layer 3 backup interface for the peer link, which the switch uses when the peer link goes down. You must add the backup IP address, which must be different than the peer link IP address. |
| `enable` | Turns MLAG on or off. The default is 'off'.|
| `debug` | Turns on MLAG debugging. |
| `init-delay` | Configures the delay, in seconds, after which bonds come up.|
| `mac-address` | Configures the MLAG system MAC address so that the switch overrides the anycast MAC and anycast ID.|
| `peer-ip`  | Configures the IP address of the MLAG peer. |
| `priority` | Configures the MLAG priority. By default, the switch determines the role by comparing the MAC addresses of the two sides of the peering link; the switch with the lower MAC address assumes the primary role. You can override this by setting the priority option for the peer link. |

## nv set mlag lacp-conflict

Configures the MLAG LACP conflict parameters.

### Usage

`nv set mlag lacp-conflict [options]`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag lacp-conflict 
```

## nv set mlag backup \<backup-ip\>

Configures the IP address of the MLAG backup switch. The backup IP address is any layer 3 backup interface for the peer link, which the switch uses when the peer link goes down. You must add the backup IP address, which must be different than the peer link IP address.

### Usage

`nv set mlag backup <backup-ip> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<backup-ip>` |  The IP address of the MLAG backup switch. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `vrf` |  Configures the VRF for the backup IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag backup 10.10.10.2
```

## nv set mlag backup \<backup-ip\> vrf \<vrf-name\>

Configures the VRF for MLAG backup IP address.

### Usage

`nv set mlag backup <backup-ip> vrf [options] <vrf-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<backup-ip>` |  The IP address of the MLAG backup switch.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag backup 10.10.10.2 vrf RED
```

## nv set mlag enable

Turns MLAG on or off.

### Usage

`nv set mlag enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag enable on
```


## nv set mlag mac-address

Configures the MLAG system MAC address. NVIDIA provides a reserved range of MAC addresses for MLAG (between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff). Use a MAC address from this range to prevent conflicts with other interfaces in the same bridged network. Do not to use a multicast MAC address. Make sure you specify a different MAC address for each MLAG pair in the network.

### Usage

`nv set mlag mac-address [options] (auto|<mac>)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
```

## nv set mlag peer-ip

Configures the IP address of the MLAG peer.

### Usage

`nv set mlag peer-ip [options] (linklocal|<ipv4>|<ipv6>)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag peer-ip linklocal
```

## nv set mlag priority

Configures the MLAG priority. By default, the switch determines the role by comparing the MAC addresses of the two sides of the peering link; the switch with the lower MAC address assumes the primary role. You can override this by setting the priority option for the peer link. You can set a vlaue between 0-65535. 

### Usage

`nv set mlag priority [options] 0-65535`

### Default Setting

32768

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag priority 2084
```

## nv set mlag init-delay

Configures the number of seconds `clagd` delays bringing up MLAG bonds and anycast IP addresses. You can set a value between 0 and 9000.

This timer sets to 0 automatically under the following conditions:
- When the peer is not alive and the backup link is not active after a reload timeout.
- When the peer sends a goodbye (through the peer link or the backup link).
- When both MLAG sessions come up at the same time.

### Usage

`nv set mlag init-delay [options] 0-900`

### Default Setting

180

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag init-delay 100
```

## nv set mlag debug

Turns MLAG degugging on or off.

### Usage

`nv set mlag debug [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag debug on
```

## nv set evpn

Enables and disables the EVPN control plane. When enabled, the EVPN service offered is a VLAN-based service and an EVI is created automatically for each extended VLAN.

### Usage

`nv set evpn [options] [<attribute> ...]`

### Default Setting

`off`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`route-advertise` | Configures EVPN route advertising. |
|`dad`  | Configures EVPN duplicate address detection.  |
|`evi` | Configures the EVI. |
|`multihoming`  | Configures EVPN multihoming global configuration parameters. |
|`enable` |  Turns EVPN on or off.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn route-advertise

Configures EVPN route advertising.

### Usage

`nv set evpn route-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `default-gateway` |  Configures the gateway VTEPs to advertise their IP and MAC address. Only turn this setting on in a centralized-routing deployment and only on the centralized gateway router. When set to `on`, the IP addresses of SVIs in all EVIs are announced as type-2 routes with the gateway extended community. The remote layer 2 only VTEPs use ARP suppression and the hosts learn of the gateway's IP to MAC binding. |
| `nexthop-setting` |  Configures the next hop IP and MAC (Router MAC) to use when advertising type-5 routes and “self” type-2 routes (“self” = SVI IP/MAC). Only use this setting in an MLAG configuration.|
| `svi-ip` | Configures the switch to announce the IP addresses of SVIs in all EVIs as type-2 routes. Only enable this option if you reuse SVI IP addresses in the network. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn route-advertise nexthop-setting

Configures how to advertise type-5 routes. Each switch in an MLAG pair advertises type-5 routes with its own system IP address, which creates an additional next hop at the remote VTEPs. In a large multi-tenancy EVPN deployment, where additional resources are a concern, you can disable this feature. Set this command to `shared-ip-mac` if you do not want to advertise type-5 routes with the system IP address. Set this command to `system-ip-mac` to advertise type-5 routes with the system IP address.

### Usage

`nv set evpn route-advertise nexthop-setting [options] (system-ip-mac|shared-ip-mac)`

### Default Setting

`system-ip-mac`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn route-advertise nexthop-setting shared-ip-mac
```

## nv set evpn route-advertise svi-ip

Configures the switch to announce the IP addresses of SVIs in all EVIs as type-2 routes. Only enable this option if you reuse SVI IP addresses in the network.

### Usage

`nv set evpn route-advertise svi-ip [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn route-advertise svi-ip on
```

## nv set evpn route-advertise default-gateway

Configures the gateway VTEPs to advertise their IP and MAC address. Only turn this setting on in a centralized routing deployment and only on the centralized gateway router. When set to `on`, the IP addresses of SVIs in all EVIs are announced as type-2 routes with the gateway extended community. The remote layer 2 only VTEPs use ARP suppression and the hosts learn of the gateway's IP to MAC binding. 

### Usage

`nv set evpn route-advertise default-gateway [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn route-advertise default-gateway on
```

## nv set evpn dad

Configures EVPN duplicate address detection. The VTEP considers a host MAC or IP address to be duplicate if the address moves across the network more than a certain number of times within a certain number of seconds. In addition to legitimate host or VM mobility scenarios, address movement can occur when you configure IP addresses incorrectly on a host or when packet looping occurs in the network due to faulty configuration or behavior.

### Usage

`nv set evpn dad [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`duplicate-action` |    Configures the action to take when the switch flags a MAC address as a possible duplicate. |
|`enable`|  Turns duplicate address detection on or off. |
|`mac-move-threshold` |  Configures the number of MAC moves allowed within a time window before flagging the MAC address as a possible duplicate. |
|`move-window` |   Configures the time window during which the move threshold applies. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn dad duplicate-action

Configures the action to take when the switch flags a MAC address as a possible duplicate.

### Usage

`nv set evpn dad duplicate-action [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `freeze` |   Configures the switch to take no action for further move events for the MAC address. |

## nv set evpn dad duplicate-action freeze

Configures the switch to take no action for further move events for the MAC address.

### Usage

`nv set evpn dad duplicate-action freeze [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `duration` |  Configures the switch to freeze duplicate addresses for a specific period of time or permnently (until the operator intervenes). |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn dad duplicate-action freeze duration

Configures the switch to freeze duplicate addresses for a specific period of time. You can specify a value between 30 and 3600 seconds or `permanent` to freeze duplicate addresses until you run the clear command.

### Usage

`nv set evpn dad duplicate-action freeze duration [options] (30-3600|permanent)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad duplicate-action freeze duration permanent
```

## nv set evpn dad enable (on|off)

Enables and disables duplicate address detection.

### Usage

`nv set evpn dad enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad enable on
```

## nv set evpn dad mac-move-threshold

Configures the number of MAC moves allowed within the detection time specified before the switch flags the MAC address as a possible duplicate. You can specify a value between 2 and 1000.

### Usage

`nv set evpn dad mac-move-threshold [options] 2-1000`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad mac-move-threshold 10
```

## nv set evpn dad move-window

Configures the detection time interval during which the MAC move threshold applies. You can specify a value between 2 and 1800.

### Usage

`nv set evpn dad move-window [options] 2-1800`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad move-window 1200
```

## nv set evpn evi \<evi-id\>

Enables the EVPN control plane so that the EVPN service offered is VLAN-based and an EVI is created automatically for each extended VLAN.

### Usage

`nv set evpn evi <evi-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`route-advertise` |  Configures route advertisement. |
| `route-target` |    Configures route targets. |
| `rd` | Configures the BGP Route Distinguisher to use for EVPN type-5 routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn evi \<evi-id\> route-advertise

Configures route advertisement for an EVPN instance.

### Usage

`nv set evpn evi <evi-id> route-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`default-gateway` |  Turns centralized routing on or off. When you turn centralized routing on, the gateway VTEPs advertise their IP and MAC address. |
|`svi-ip` | Turns the advertise SVI IP and MAC address option on or off for the EVPN instance so you can advertise the SVI IP and MAC address as a type-2 route. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn evi \<evi-id\> route-advertise svi-ip

Turns the advertise SVI IP and MAC address option on or off for the EVPN instance so you can advertise the SVI IP and MAC address as a type-2 route. This eliminates the need for any flooding over VXLAN to reach the IP address from a remote VTEP or rack. You typically turn this setting on if you use unique SVI IP addresses across multiple racks and you want the local SVI IP address to be reachable through remote VTEPs. You can specify `on`, `off`, or `auto`. If you specify `auto`, the EVI inherits from the global configuration. If you turn this setting `on`, the IP addresses of SVIs in all EVIs are announced as type-2 routes. Do not turn this setting `on` if you reuse SVI IP addresses in the network.

### Usage

`nv set evpn evi <evi-id> route-advertise svi-ip [options] (on|off|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn evi 10 route-advertise svi-ip on
```

## nv set evpn evi \<evi-id\> route-advertise default-gateway

Turns centralized routing on or off for the EVI. When you turn centralized routing on, the gateway VTEPs advertise their IP and MAC address.
You can also specify `auto`, where the EVI inherits from the global configuration. Only turn this setting `on` in a centralized-routing deployment and only on the centralized GW router. When you turn this setting `on`, the IP addresses of SVIs in all EVIs announce as type-2 routes with the gateway extended community so that only remote layer 2 VTEPs run ARP suppression and hosts learn of the gateway's IP to MAC binding.

### Usage

`nv set evpn evi <evi-id> route-advertise default-gateway [options] (on|off|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn evi 10 route-advertise default-gateway on
```

## nv set evpn evi \<evi-id\> route-target

Configures route targets for an EVPN instance.

### Usage

`nv set evpn evi <evi-id> route-target [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`export` | Configures the route targets you want to export. |
|`import` | Configures the route targets you want to import. |
|`both` | Configures the route targets you want to both import and export. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn evi \<evi-id\> route-target export \<rt-id\>

Configures the route targets you want to export for the EVPN instance.

### Usage

`nv set evpn evi <evi-id> route-target export <rt-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn evi 10 route-target export 65101:10
```

## nv set evpn evi \<evi-id\> route-target import \<rt-id\>

Configures the route targets you want to import for the EVPN instance.

### Usage

`nv set evpn evi <evi-id> route-target import <rt-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn evi 10 route-target import 65102:10
```

## nv set evpn evi \<evi-id\> route-target both \<rt-id\>

Configures the route targets you want to both import and export for the EVPN instance.

### Usage

`nv set evpn evi <evi-id> route-target both <rt-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn evi 10 route-target both 65101:10
```

## nv set evpn evi <evi-id> rd

Configures the BGP Route Distinguisher to use for EVPN type-5 routes originated from this EVI.

### Usage

`nv set evpn evi <evi-id> rd [options] (auto|<route-distinguisher>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<evi-id>` | The EVPN instance. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn evi 10 rd 10.10.10.1:20
```

## nv set evpn multihoming

Configures EVPN multihoming global configuration parameters.

### Usage

`nv set evpn multihoming [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`ead-evi-route`  | Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-EVI (Ethernet Auto-discovery per EVPN instance) routes. Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements. |
|`segment`  | Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-ES (Ethernet Auto-discovery per Ethernet segment) routes Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.|
|`enable`  | Turns EVPN multihoming on or off. The default is 'off'. |
|`mac-holdtime` |Configures the MAC hold time, which specifies the duration for which a switch maintains SYNC MAC entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the MAC address on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.|
|`neighbor-holdtime` | Configures the neighbor hold times, which pecifies the duration for which a switch maintains SYNC neighbor entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.|
|`startup-delay`  | Configures the duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. The delay can be between 0 and 216000 seconds. The default is 180 seconds.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn multihoming ead-evi-route

Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-EVI (Ethernet Auto-discovery per EVPN instance) routes. 

Note: Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.

### Usage

`nv set evpn multihoming ead-evi-route [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`rx` | Turns EAD-per-EVI at the receiving end on or off.|
|`tx` | Turns EAD-per-EVI route advertisement on or off.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn multihoming ead-evi-route rx

Turns EAD-per-EVI at the receiving end on or off.

### Usage

`nv set evpn multihoming ead-evi-route rx [options] (on|off)`

### Default Setting

`on`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming ead-evi-route rx off
```

## nv set evpn multihoming ead-evi-route tx

Turns EAD-per-EVI route advertisement on or off.

### Usage

`nv set evpn multihoming ead-evi-route tx [options] (on|off)`

### Default Setting

`on`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming ead-evi-route tx off
```

## nv set evpn multihoming segment

Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-ES (Ethernet Auto-discovery per Ethernet segment) routes.

Note: Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.

### Usage

`nv set evpn multihoming segment [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `df-preference` | Configures the designated forwarder preference value for EVPN multihoming. |
| `mac-address` |  Configures the MAC address per ethernet segment for EVPN multihoming. |

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set evpn multihoming segment mac-address \<mac\>

Configures the MAC address per ethernet segment for EVPN multihoming. This setting is required.

### Usage

`nv set evpn multihoming segment mac-address [options] <mac>`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming segment mac-address 00:00:00:00:00:10
```

## nv set evpn multihoming segment df-preference

Configures the designated forwarder preference value for EVPN multihoming. You can specify a value between 1 and 65535.

### Usage

`nv set evpn multihoming segment df-preference [options] 1-65535`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming segment df-preference 50000
```

## nv set evpn multihoming enable (on|off)

Turns EVPN multihoming on or off.

### Usage

`nv set evpn multihoming enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming enable on
```

## nv set evpn multihoming mac-holdtime

Configures the MAC hold time, which specifies the duration for which a switch maintains SYNC MAC entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the MAC address on the local Ethernet segment. You can specify a value between 0 and 86400 seconds.

### Usage

`nv set evpn multihoming mac-holdtime [options] 0-86400`

### Default Setting

1080 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming mac-holdtime 1000
```

## nv set evpn multihoming neighbor-holdtime

Configures the neighbor hold times, which pecifies the duration for which a switch maintains SYNC neighbor entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. You can specify a value between between 0 and 86400 seconds.

### Usage

`nv set evpn multihoming neighbor-holdtime [options] 0-86400`

### Default Setting

1080 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming neighbor-holdtime 600
```

## nv set evpn multihoming startup-delay

Configures the duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. You can specify a value between 0 and 3600 seconds.

### Usage

`nv set evpn multihoming startup-delay [options] 0-3600`

### Default Setting

180 seconds

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming startup-delay 1000
```

## nv set qos

Configures Quality of Service (QOS).

### Usage

`nv set qos [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`roce` |  Configures RDMA over Converged Ethernet lossless (RoCE). |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set qos roce

Configures RDMA over Converged Ethernet lossless (RoCE). 

### Usage

`nv set qos roce [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`enable` |  Turns RDMA over Converged Ethernet on and off. |
|`mode` | Configures the Roce mode: lossy or lossless. |
|`cable-length` | Configures the table length (in meters) for Roce lossless. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set qos roce enable

### Usage

`nv set qos roce enable [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce enable off
```

## nv set qos roce mode

Configures the Roce mode. You can specify `lossy` or `lossless`.

### Usage

`nv set qos roce mode [options] (lossy|lossless)`

### Default Setting

`lossless`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce mode lossy
```

## nv set qos roce cable-length

Configures the cable length (in meters)for Roce lossless. You can specify a value between 1 and 100000.

### Usage

`nv set qos roce cable-length [options] 1-100000`

### Default Setting

100

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set qos roce cable-length 1000
```

## nv set interface \<interface-id\>

Configures an interface.

### Usage

`nv set interface <interface-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`router` | Configures adaptive routing, OSPF, policy-based routing, and PIM for an interface.|
|`bond` | Configures a bond.|
|`bridge` | Configures a bridged interface.|
|`ip` | Configures the IP address for an interface.|
|`lldp` | Configures LLDP on an interface.|
|`link` | Configures the physical interface.|
|`evpn` | Configures EVPN control plane and information for the VRF.|
|`acl` | Configures ACL rules for the interface.|
|`ptp` | Configures PTP settings for the interface.|
|`tunnel`|  The state of the interface|
|`base-interface` | Configures the interface under this interface.|
|`description` | Configures the interface description.|
|`type` | Configures the interface type.|
|`vlan` | Configures the VLAN ID.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router

Configues routing settings on an interface.

### Usage

`nv set interface <interface-id> router [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `pbr`  | Configures PBR on an interface. |
| `ospf` | Configures OSPF on an interface. |
| `pim` |  Configures PIM on an interface. |
| `adaptive-routing` | Configures adaptive routing on an interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pbr

Configures PBR on an interface.

### Usage

`nv set interface <interface-id> router pbr [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `map` |   Configures the PBR map to use on the specified interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pbr map \<pbr-map-id\>

Configures the PBR map to use on the specified interface.

### Usage

`nv set interface <interface-id> router pbr map <pbr-map-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<pbr-map-id>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pbr map1
```

## nv set interface \<interface-id\> router ospf

Configures OSPF on an interface.

### Usage

`nv set interface <interface-id> router ospf [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `timers` |  Configures OSPF timers. |
| `authentication` |  Configures OSPF MD5 authentication on an interface. |
| `bfd` | Configures BFD on an interface. |
| `enable` |  Turns OSPF on and off. |
| `area` |   Configures the area number for enabling OSPF on an interface. |
| `cost`  | Configures the cost of this link.  |
| `mtu-ignore` | Configures OSPF to ignore MTU matching for peering. |
| `network-type` | Configures the network type for the OSPF interface: point-to-point or broadcast. |
| `passive` | Configures the interface as passive. A passive interface creates a database entry but does not send or receive OSPF hello packets. |
| `priority` | Configures the priority in becoming the OSPF Designated Router (DR) on a broadcast interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router ospf timers

Configures OSPF timers.

### Usage

`nv set interface <interface-id> router ospf timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `dead-interval` | Configures the number of seconds to wait without a hello before declaring the neighbor dead. If you specify `minimal`, you must set the `hello-multiplier`.|
| `hello-interval` | Configures how often in seconds to transmit a hello packet. This setting is only valid if `dead-interval` is not `minimal`.|
| `hello-multiplier` | Configures the required multiplier to use if `dead-interval` is `minimal`. |
| `transmit-interval`| Configures how often in seconds to retransmit a packet that is not acknowledged. |
| `transmit-delay` | Configures the number of seconds to wait before sending a new LSA. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router ospf timers dead-interval

Configures the number of seconds to wait without a hello before declaring the neighbor dead. You can specify a value between 1 and 65535, or `minimal`. If you specify `minimal`, you must set the `hello-multiplier`.

### Usage

`nv set interface <interface-id> router ospf timers dead-interval [options] (1-65535|minimal)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers dead-interval 600
```

## nv set interface \<interface-id\> router ospf timers hello-multiplier

Configures the multiplier to use if `dead-interval` is `minimal`. You can specify a value between 1 and 10.

### Usage

`nv set interface <interface-id> router ospf timers hello-multiplier [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers hello-multiplier 6
```

## nv set interface \<interface-id\> router ospf timers hello-interval

Configures how often in seconds to transmit a hello packet. This setting is only valid if `dead-interval` is not `minimal`. You can specify a value between 1 and 65535.

### Usage

`nv set interface <interface-id> router ospf timers hello-interval [options] 1-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers hello-interval 600
```

## nv set interface \<interface-id\> router ospf timers retransmit-interval

Configures how often in seconds to retransmit a packet that is not acknowledged. You can specify a value between 1 and 65535.

### Usage

`nv set interface <interface-id> router ospf timers retransmit-interval [options] 1-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers retransmit-interval 600
```

## nv set interface \<interface-id\> router ospf timers transmit-delay

Configures the number of seconds to wait before sending a new LSA. You can specify a value between 1 and 65535.

### Usage

`nv set interface <interface-id> router ospf timers transmit-delay [options] 1-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers retransmit-delay 600
```

## nv set interface \<interface-id\> router ospf authentication

Configures OSPF MD5 authentication on an interface.

### Usage

`nv set interface <interface-id> router ospf authentication [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns md5 authentication on and off. |
| `md5-key` | Configures the MD5 key. |
| `message-digest-key` |  Configures the message digest key.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router ospf authentication enable

### Usage

`nv set interface <interface-id> router ospf authentication enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf authentication enable on
```

## nv set interface \<interface-id\> router ospf authentication message-digest-key

Configures the message digest key. You can specify a value between 1 and 255. The value must be consistent across all routers on a link.

### Usage

`nv set interface <interface-id> router ospf authentication message-digest-key [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf authentication message-digest-key 1
```

## nv set interface \<interface-id\> router ospf authentication md5-key \<value\>

Configures the MD5 key.

### Usage

`nv set interface <interface-id> router ospf authentication md5-key [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<value>` | The MD5 key. 

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf authentication md5-key thisisthekey
```

## nv set interface \<interface-id\> router ospf bfd

Configures Bidirectional Forwarding Detection (BFD) on an interface. BFD provides low overhead and rapid detection of failures in the paths between two network devices.

### Usage

`nv set interface <interface-id> router ospf bfd [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` | Turns BFD on and off on the OSPF interface.|
| `detect-multiplier` |  Configures the detect multiplier value. |
| `min-receive-interval` | Configures the minimum receive interval in milliseconds. |
| `min-transmit-interval` | Configures the minimum transmit interval in milliseconds. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router ospf bfd enable

Turns BFD on and off on the OSPF interface.

### Usage

`nv set interface <interface-id> router ospf bfd enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd enable on
```

## nv set interface \<interface-id\> router ospf bfd detect-multiplier

Configures the detection time multiplier. You can specify a value between 2 and 255.

### Usage

`nv set interface <interface-id> router ospf bfd detect-multiplier [options] 2-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd detect-multiplier 100
```

## nv set interface \<interface-id\> router ospf bfd min-receive-interval

Configures the required minimum interval between the received BFD control packets. You can specify a value between 50 and 60000.

### Usage

`nv set interface <interface-id> router ospf bfd min-receive-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd min-receive-interval 400
```

## nv set interface \<interface-id\> router ospf bfd min-transmit-interval

Configures the minimum transmit interval in milliseconds. You can specify a value between 50 and 60000.

### Usage

`nv set interface <interface-id> router ospf bfd min-transmit-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd min-transmit-interval 400
```

## nv set interface \<interface-id\> router ospf enable

Turns OSFP on and off on the interface.

### Usage

`nv set interface <interface-id> router ospf enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf enable on
```

## nv set interface \<interface-id\> router ospf area

Configures the OSPF area on the interface.

### Usage

`nv set interface <interface-id> router ospf area [options] (0-4294967295|none|<ipv4>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf area 0
```

## nv set interface \<interface-id\> router ospf cost 

Configures the cost of this link. You can specify a value between 1 and 65535 or `auto`, which automatically determines the cost based on link speed. 

## Usage

`nv set interface <interface-id> router ospf cost [options] (1-65535|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf cost 60
```

## nv set interface \<interface-id\> router ospf mtu-ignore

Configures OSPF to turn MTU value checking in the OSPF DBD packets on or off.

## Usage

`nv set interface <interface-id> router ospf mtu-ignore [options] (on|off)`

### Default Setting

`on`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf mtu-ignore off
```

## nv set interface \<interface-id\> router ospf network-type

Configures the network type for the OSPF interface: point-to-point or broadcast.

## Usage

`nv set interface <interface-id> router ospf network-type [options] (broadcast|non-broadcast|point-to-multipoint|point-to-point)`

### Default Setting

`broadcast`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf network-type point-to-multipoint
```

## nv set interface \<interface-id\> router ospf passive

Configures the interface as passive. A passive interface creates a database entry but does not send or receive OSPF hello packets.

## Usage

`nv set interface <interface-id> router ospf passive [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf passive on
```

## nv set interface \<interface-id\> router ospf priority

Configures the priority in becoming the OSPF Designated Router (DR) on a broadcast interface. 

## Usage

`nv set interface <interface-id> router ospf priority [options] 0-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf priority 5
```

## nv set interface \<interface-id\> router pim

Configures PIM on an interface.

### Usage

`nv set interface <interface-id> router pim [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `timers` | Configures PIM timers on an interface. |
| `bfd` | Configures BFD for the PIM-enabled interface. |
| `address-family` | Configures the address family on the PIM-enabled interface. |
| `enable` | Turns PIM on or off on the interface. |
| `active-active` | Configures active-active for PIM MLAG operation on the interface. |
| `dr-priority` | Configures the designated Router Election priority on the PIM-enabled interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pim timers

Configures PIM timers on an interface.

### Usage

`nv set interface <interface-id> router pim timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `hello-interval` |  Configures the PIM Hello packets periodic interval. If `auto`, the interval is inherited from the VRF. The hold time is 3.5 times the `hello-interval`, the amount of time the neighbor must be in a reachable state. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pim timers hello-interval 

Configures the PIM Hello packets periodic interval. If `auto`, the interval is inherited from the VRF. The hold time is 3.5 times the `hello-interval`, the amount of time the neighbor must be in a reachable state.

### Usage

`nv set interface <interface-id> router pim timers hello-interval [options] (1-180|auto)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface router pim timers hello-interval 100
```

## nv set interface \<interface-id\> router pim bfd

Configures BFD for the PIM enabled interface.

### Usage

`nv set interface <interface-id> router pim bfd [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`  | Turns BFD on or off on the PIM-enabled interface. |
| `detect-multiplier` | Configures the BFD detect multiplier value for a PIM-enabled interface. |
| `min-receive-interval` | Configures the BFD minimum receive interval in milliseconds or a PIM-enabled interface. |
| `min-transmit-interval`| Configures the BFD minimum transmit interval in milliseconds or a PIM-enabled interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pim bfd enable

Turns BFD on or off on the PIM-enabled interface.

### Usage

`nv set interface <interface-id> router pim bfd [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface router pim bfd on
```

## nv set interface \<interface-id\> router pim bfd detect-multiplier

Configures the BFD detect multiplier value for a PIM-enabled interface. You can set a value between 2 and 255.

### Usage

`nv set interface <interface-id> router pim bfd detect-multiplier [options] 2-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim bfd detect-multiplier  10
```

## nv set interface \<interface-id\> router pim bfd min-receive-interval

Configures the BFD minimum receive interval in milliseconds or a PIM-enabled interface. You can set a value between 50 and 60000.

### Usage

`nv set interface <interface-id> router pim bfd min-receive-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim bfd min-receive-interval 300
```

## nv set interface \<interface-id\> router pim bfd min-transmit-interval

Configures the BFD minimum transmit interval in milliseconds or a PIM-enabled interface. You can set a value between 50 and 60000.

### Usage

`nv set interface <interface-id> router pim bfd min-transmit-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim bfd min-transmit-interval 300
```

## nv set interface \<interface-id\> router pim address-family

Configures the address family on the PIM-enabled interface.

### Usage

`nv set interface <interface-id> router pim address-family [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ipv4-unicast` | Configures the IPv4 unicast address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pim address-family ipv4-unicast

Configures the IPv4 unicast address family.

### Usage

`nv set interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `allow-rp` | Configures the interface to ignore the RP check for all upstream neighbors. |
| `multicast-boundary-oil` | Configures multicast boundaries to limit the distribution of multicast traffic and push multicast to a subset of the network. |
| `use-source` | Configures the interface to use the unique source address in the PIM Hello source field. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pim address-family ipv4-unicast allow-rp

Configures the interface to ignore the RP check for all upstream neighbors.

### Usage

`nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp [options] [<attribute> ...]`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`enable` | Turns allow RP on or off on the PIM-enabled interface.|
|`rp-list`  | Configures the prefix list that provides the list of group addresses to accept downstream (*,G) joins and propogate towards the allowed RP.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router pim address-family ipv4-unicast allow-rp enable

Turns allow RP on or off on the PIM-enabled interface.

### Usage

`nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast allow-rp enable on
```

## nv set interface \<interface-id\> router pim address-family ipv4-unicast allow-rp rp-list

Configures the prefix list that provides the list of group addresses to accept downstream (*,G) joins and propogate towards the allowed RP.

### Usage

`nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp rp-list [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<instance-name>` | The name of the prefix list. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast allow-rp rp-list myprefixlist
```

## nv set interface \<interface-id\> router pim address-family ipv4-unicast multicast-boundary-oil

Configures multicast boundaries to limit the distribution of multicast traffic and push multicast to a subset of the network.

### Usage

`nv set interface <interface-id> router pim address-family ipv4-unicast multicast-boundary-oil [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<instance-name>` | The name of the prefix list. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast multicast-boundary-oil MyPrefixList
```

## nv set interface \<interface-id\> router pim address-family ipv4-unicast use-source

Configures the PIM-enabled interface to use the unique source address in the PIM Hello source field.

### Usage

`nv set interface <interface-id> router pim address-family ipv4-unicast use-source [options] (none|<ipv4>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast use-source 10.100.100.100
```

## nv set interface \<interface-id\> router pim enable

Turns PIM on or off on the interface.

### Usage

`nv set interface <interface-id> router pim enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim enable on
```

## nv set interface \<interface-id\> router pim dr-priority

Configures the Designated Router Election priority. You can specify a value between 1 and 4294967295.

### Usage

`nv set interface <interface-id> router pim dr-priority [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 router pim dr-priority 100
```

## nv set interface \<interface-id\> router pim active-active

Turns PIM active-active on or off on the interface.

### Usage

`nv set interface <interface-id> router pim active-active [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim active-active on
```

## nv set interface \<interface-id\> router adaptive-routing

Configures adaptive routing on the PIM-enabled interface.

### Usage

`nv set interface <interface-id> router adaptive-routing [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` | Turns adaptive routing on or off on the PIM-enabled interface. |
| `link-utilization-threshold` |  Configures the link utilization threshold percentage. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> router adaptive-routing enable

Turns adaptive routing on or off on the interface.
### Usage

`nv set interface <interface-id> router adaptive-routing enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router adaptive-routing enable on
```

## nv set interface \<interface-id\> router adaptive-routing link-utilization-threshold

Configures the link utilization threshold percentage. You can set a value between 1 and 100.

### Usage

`nv set interface <interface-id> router adaptive-routing link-utilization-threshold [options] 1-100`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 router adaptive-routing link-utilization-threshold 50
```

## nv set interface \<interface-id\> bond

Configures a bond.

### Usage

`nv set interface <interface-id> bond [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`member` | Configures the bond members. |
| `mlag` | Configures MLAG on the bond interface. |
| `down-delay` |  Configures the bond down delay time. |
| `lacp-bypass` | Turns LACP bypass on or off on the bond interface.  |
| `lacp-rate` | Configures the rate at which the link partner transmits LACP control packets. |
| `mode` | Configures the bond mode: IEEE 802.3ad or Balance-xor.  |
| `up-delay` | Configures the bond up delay.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> bond member \<member-id\>

Configures the bond members.

### Usage

`nv set interface <interface-id> bond member <member-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<member-id>` |The bond member interfaces. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond member swp1-4
```

## nv set interface \<interface-id\> bond mlag

Configures MLAG on the bond interface.

### Usage

`nv set interface <interface-id> bond mlag [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `lacp-conflict` |  Configures MLAG LACP conflict.|
| `enable` | Turns MLAG on or off. |
| `id` |  Configures the MLAG ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> bond mlag lacp-conflict

Configures MLAG LACP conflict on the bond interface.

### Usage

`nv set interface <interface-id> bond mlag lacp-conflict [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond mlag lacp-conflict 
```

## nv set interface \<interface-id\> bond mlag enable 

Turns MLAG on or off on the bond interface.

### Usage

`nv set interface <interface-id> bond mlag enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond mlag enable on
```

## nv set interface \<interface-id\> bond mlag id

Configures the MLAG ID on the bond interface. You must specify a unique MLAG ID (`clag-id`) for every dual-connected bond on each peer switch so that switches know which links dual-connect or connect to the same host or switch. The value must be between 1 and 65535 and must be the same on both peer switches. A value of 0 disables MLAG on the bond.

### Usage

`nv set interface <interface-id> bond mlag id [options] (1-65535|auto)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond mlag id 1
```

## nv set interface \<interface-id\> bond down-delay

Configures the bond down delay time, which is the amount of time to wait before disabling a slave interface after detecting a link failure. You can specify a value between 0 and 65535.

### Usage

`nv set interface <interface-id> bond down-delay [options] 0-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond down-delay 600
```
## nv set interface \<interface-id\> bond lacp-bypass

Turns LACP bypass on or off on the bond interface. When on, LACP bypass on a bond is in 802.3ad mode so that it becomes active and forwards traffic even when there is no LACP partner.

### Usage

`nv set interface <interface-id> bond lacp-bypass [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond lacp-bypass on
```

## nv set interface <interface-id> bond lacp-rate

Configures the rate at which the link partner transmits LACP control packets. You can specify slow or fast.

### Usage

`nv set interface <interface-id> bond lacp-rate [options] (fast|slow)`

### Default Setting

`fast`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond lacp-rate slow
```

## nv set interface <interface-id> bond mode

Configures the bond mode: IEEE 802.3ad (`lacp`) or Balance-xor (`static`). Set Balance-xor mode only if you cannot use LACP; LACP can detect mismatched link attributes between bond members and can even detect misconnections.

### Usage

`nv set interface <interface-id> bond mode [options] (lacp|static)`

### Default Setting

`lacp`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond mode static
```

## nv set interface \<interface-id\> bond up-delay

Configures the bond up delay, which is how much time in milliseconds to wait before enabling a slave after detecting a link recovery. 

### Usage

`nv set interface <interface-id> bond up-delay [options] 0-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond up-delay 6000
```

## nv set interface \<interface-id\> bridge

Configures a bridged interface.

### Usage

`nv set interface <interface-id> bridge [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain`  | Configures the bridge domains on this interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> bridge domain \<domain-id\>

Configures the bridge domains on this interface.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]`

### Default Setting

`br_default`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `stp` | Configures STP for this bridge domain on this interface. |
|`vlan` | Configures the allowed VLANs for this bridge domain on this interface. |
| `access` |  Configures access ports for this bridge domain on this interface. |
| `learning` | Configures source MAC address learning for this bridge domain on this interface. |
| `untagged` | Configures untagged packets ingressing on the interface to go in a specific VLAN. Egress packets are always tagged. If none, then untagged packets will be dropped. If auto, inherit from bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> bridge domain \<domain-id\> stp

Configures STP for this bridge domain on this interface.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> stp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `admin-edge` | Configures PortAdminEdge on the interface on this bridge domain. PortAdminEdge turns the initial edge state of the interface in a bridge on or off. When on, the interface bypasses the listening and learning states and goes straight to forwarding. This is equivalent to the PortFast feature offered by other vendors. |
| `auto-edge`  | Configures PortAutoEdge on the interface on this bridge domain. PortAutoEdge turns the automatic transition to and from the edge state of an interface in a bridge on or off. PortAutoEdge is an enhancement to the standard PortAdminEdge (PortFast) mode.|
| `bpdu-filter` | Configures Bridge Protocol Data Unit (BPDU) filter on the interface on this bridge domain. BPDU filter filters BPDUs in both directions, which disables STP on the interface as no BPDUs transit.|
| `bpdu-guard`| Configures BPDU guard on the interface on this bridge domain. BPDU guard protects the spanning tree topology from an unauthorized device affecting the forwarding path.|
| `network` | Configures bridge assurance on the interface on this bridge domain.|
| `restrrole` | Configures the interface on this bridge domain to take root role.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> bridge domain <domain-id> stp bpdu-filter

Configures Bridge Protocol Data Unit (BPDU) filter on the interface on this bridge domain. BPDU filter filters BPDUs in both directions, which disables STP on the interface as no BPDUs transit.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> stp bpdu-filter [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default stp bpdu-filter on
```

## nv set interface \<interface-id\> bridge domain <domain-id> stp bpdu-guard

Configures BPDU guard on the interface on this bridge domain. BPDU guard protects the spanning tree topology from an unauthorized device affecting the forwarding path.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> stp bpdu-guard [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default stp bpdu-guard on
```

## nv set interface \<interface-id\> bridge domain \<domain-id\> stp admin-edge

Configures PortAdminEdge on the interface on this bridge domain. PortAdminEdge turns the initial edge state of the interface in a bridge on or off. When on, the interface bypasses the listening and learning states and goes straight to forwarding. This is equivalent to the PortFast feature offered by other vendors.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> stp admin-edge [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default stp admin-edge on
```

## nv set interface \<interface-id\> bridge domain \<domain-id\> stp auto-edge

Configures PortAutoEdge on the interface on this bridge domain. PortAutoEdge turns the automatic transition to and from the edge state of an interface in a bridge on or off. PortAutoEdge is an enhancement to the standard PortAdminEdge (PortFast) mode.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> stp auto-edge [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default stp auto-edge on
```

## nv set interface \<interface-id\> bridge domain \<domain-id\> stp network

Configures bridge assurance on the interface on this bridge domain. Bridge assurance detects unidirectional links and puts the port in a discarding state. The port is in a bridge assurance inconsistent state until it receives a BPDU from the peer. You need to configure the port type network on both ends of the link for bridge assurance.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> stp network [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default stp network on
```

## nv set interface <interface-id> bridge domain <domain-id> stp restrrole (on|off)

Configures the interface on this bridge domain to take root role.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> stp restrrole [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default stp restrrole on
```

## nv set interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\>

Configures the allowed VLANs for this bridge domain on this interface. The default value `all` inherits all VLANs from the bridge domain.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> vlan <vid> [options]`

### Default Setting

`all`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |
| `<vid>`  | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10,20
```

## nv set interface \<interface-id\> bridge domain \<domain-id\> learning

Turns source MAC address learning on or off for this bridge domain on this interface.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> learning [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default learning on
```

## nv set interface \<interface-id\> bridge domain \<domain-id\> untagged

Configures untagged packets ingressing on the interface to go in a specific VLAN. Egress packets are always tagged. You can specify a value between 1 and 4094, `none` to drop untagged packets, or `auto` to inherit from the bridge domain.

### Usage

`nv set interface <interface-id> bridge domain <domain-id> untagged [options] (1-4094|none|auto)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default untagged 1
```

## nv set interface \<interface-id\> bridge domain \<domain-id\> access

Configures access ports for this bridge domain on this interface. Access ports ignore all tagged packets. You can specify a value between 1 and 4094 or `auto` to inherit from the bridge domain. 

### Usage

`nv set interface <interface-id> bridge domain <domain-id> access [options] (1-4094|auto)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The bridge domain.  |


### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default access 10
```

## nv set interface \<interface-id\> ip

Configures the IP address for an interface.

### Usage

`nv set interface <interface-id> ip [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address` | Configures an IP address with a prefix for the interface. |
| `vrr`  | Configures Virtual Router Redundancy (VRR) for an interface. |
| `gateway` | Configures the default IPv4 and IPv6 gateways. |
| `ipv4` | Configures IPv4 settings for an interface. |
| `ipv6` | Configures IPv6 settings for an interface. |
| `igmp` | Configures IGMP for an interface.|
| `vrrp` | Configures VRRP for an interface.|
| `neighbor-discovery` | Configures neighbor discovery for an interface. |
| `vrf` | Configures virtual routing and forwarding for an interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip address \<ip-prefix-id\>

Configures an IP address with a route prefix for the interface.

### Usage

`nv set interface <interface-id> ip address <ip-prefix-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip address 10.0.0.1/30
```

## nv set interface \<interface-id\> ip vrr

Configures Virtual Router Redundancy (VRR) for an interface. VRR enables hosts to communicate with any redundant switch without reconfiguration by running dynamic router protocols or router redundancy protocols. Redundant switches respond to ARP requests from hosts. The switches respond in an identical manner, but if one fails, the other redundant switches continue to respond. You use VRR with MLAG.

### Usage

`nv set interface <interface-id> ip vrr [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address` |  Configures the virtual address and prefix. |
| `state` |  Configures the state of the interface. |
| `enable` | Turns VRR on or off on the interface. |
| `mac-address` | Configures anycast MAC override on the interface. |
| `mac-id` | Configures fabric ID override on the interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip vrr address \<ip-prefix-id\>

Configures the virtual address and prefix.

### Usage

`nv set interface <interface-id> ip vrr address <ip-prefix-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-prefix-id>` | IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24 
```

## nv set interface \<interface-id\> ip vrr state

Configures the state of the interface: up or down.

### Usage

`nv set interface <interface-id> ip vrr state [options] (up|down)`

### Default Setting

`down`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr state up 
```

## nv set interface \<interface-id\> ip vrr enable

Turns VRR on or off on the interface.

### Usage

`nv set interface <interface-id> ip vrr enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr enable on 
```

## nv set interface \<interface-id\> ip vrr mac-id

Configures the fabric ID override on the interface.

### Usage

`nv set interface <interface-id> ip vrr mac-id [options] (1-255|none)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr mac-id 1
```

## nv set interface \<interface-id\> ip vrr mac-address

Configures anycast MAC override on the interface.

### Usage

`nv set interface <interface-id> ip vrr mac-address [options] (auto|<mac>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr mac-address 00:00:5E:00:01:00
```

## nv set interface \<interface-id\> ip gateway \<ip-address-id\>

Configures the gateway IP address on the interface.

### Usage

`nv set interface <interface-id> ip gateway <ip-address-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-address-id>` | The IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip gateway 10.10.10.1
```

## nv set interface \<interface-id\> ip ipv4

Configures IPv4 settings for an interface.

### Usage

`nv set interface <interface-id> ip ipv4 [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `forward` |  Turns forwarding on or off. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip ipv4 forward

 Turns forwarding on or off.

### Usage

`nv set interface <interface-id> ip ipv4 forward [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv4 forward on
```

## nv set interface \<interface-id\> ip ipv6

Configures IPv6 settings for an interface.

### Usage

`nv set interface <interface-id> ip ipv6 [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` | Turns IPv6 on or off. |
| `forward` | Turns forwarding on or off. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip ipv6 enable (on|off)

Turns IPv6 on or off.

### Usage

`nv set interface <interface-id> ip ipv6 enable [options] (on|off)`

### Default Setting

`on`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv6 enable off
```

## nv set interface \<interface-id\> ip ipv6 forward (on|off)

Turns forwarding on or off. 

### Usage

`nv set interface <interface-id> ip ipv6 forward [options] (on|off)`

### Default Setting

`on`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv6 forward off
```

## nv set interface \<interface-id\> ip igmp

Configures Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD).

### Usage

`nv set interface <interface-id> ip igmp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`static-group` | Configures IGMP static mutlicast mroutes for the interface. |
|`enable` |  Turns IGMP and MLD on or off for the interface. |
|`last-member-query-interval` | Configures the last member query interval for the interface. |
|`query-interval` | Configures the query interval for the interface. |
|`query-max-response-time` |  Configures the maximum query response time for the interface. |
|`version` | Configures the protocol version for the interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip igmp static-group \<static-group-id\>

Configures IGMP static mutlicast mroutes for the interface.

### Usage

`nv set interface <interface-id> ip igmp static-group <static-group-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<static-group-id>` |  The IGMP static multicast mroute destination. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`source-address` |  Configures the IGMP static multicast mroute source. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip igmp static-group \<static-group-id\> source-address \<ipv4-unicast\>

Configures the IGMP static multicast mroute source for the interface.

### Usage

`nv set interface <interface-id> ip igmp static-group <static-group-id> source-address [options] <ipv4-unicast>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<static-group-id>` |  The IGMP static multicast mroute destination. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp static-group 1 source-address 10.10.10.1
```

## nv set interface \<interface-id\> ip igmp enable

Turns IGMP and MLD on or off for the interface.

### Usage

`nv set interface <interface-id> ip igmp enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp enable on
```

## nv set interface \<interface-id\> ip igmp version

Configures the protocol version for the interface. You can specify either version 2 or 3.

### Usage

`nv set interface <interface-id> ip igmp version [options] (2|3)`

### Default Setting

`2`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp version 3
```

## nv set interface \<interface-id\> ip igmp query-interval

Configures the query interval for the interface. You can specify a value between 1 and 1800 seconds.

### Usage

`nv set interface <interface-id> ip igmp query-interval [options] 1-1800`

### Default Setting

125

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp query-interval 1800
```

## nv set interface \<interface-id\> ip igmp query-max-response-time

Configures the maximum query response time for the interface. You can specify a value between 10 and 250 seconds.

### Usage

`nv set interface <interface-id> ip igmp query-max-response-time [options] 10-250`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp query-max-response-time 100
```

## nv set interface \<interface-id\> ip igmp last-member-query-interval

Configures the last member query interval for the interface. You can specify a value between 1 and 255

### Usage

`nv set interface <interface-id> ip igmp last-member-query-interval [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp last-member-query-interval 200
```

## nv set interface \<interface-id\> ip vrrp

Configures the Virtual Router Redundancy Protocol (VRRP) on the interface.

### Usage

`nv set interface <interface-id> ip vrrp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `virtual-router` |  Configures the group of virtual gateways implemented with VRRP. |
|`enable`   | Turns VRRP on or off for the interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\>

Configures the group of virtual gateways implemented with VRRP.

### Usage

`nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router IDentifier (VRID). |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address` |  Configures a set of virtual addresses for VRRPv3. |
| `advertisement-interval` | Configures the interval between successive advertisements by the master in a virtual router group. |
| `preempt` |  Configures preempt mode, which lets the router take over as master for a virtual router group if it has a higher priority than the current master.|
| `priority`  | Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. |
| `version `  | Configures the VRRP protocol version for the interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\>

Configures a virtual address for VRRPv3.

### Usage

`nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Identifier (VRID). |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> version

Configures the VRRP protocol version for the interface. You can specify a value of 2 or 3.

### Usage

`nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> version [options] (2|3)`

### Default Setting

3

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Identifier (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> priority

Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master.

### Usage

`nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> priority [options] (1-254|auto)`

### Default Setting

100

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Identifier (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 priority 254
```

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> preempt

Configures preempt mode, which lets the router take over as master for a virtual router group if it has a higher priority than the current master.

### Usage

`nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt [options] (on|off|auto)`

### Default Setting

`on`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Identifier (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 preempt off
```

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> advertisement-interval

Configures the interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950 milliseconds.

### Usage

`nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> advertisement-interval [options] (10-40950|auto)`

### Default Setting

1000

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Identifier (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 advertisement-interval 2000
```

## nv set interface \<interface-id\> ip vrrp enable

Turns on VRRP on the interface.

### Usage

`nv set interface <interface-id> ip vrrp enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp enable on
```

### Default Setting

1000

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Identifier (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 advertisement-interval 2000
```

## nv set interface \<interface-id\> ip neighbor-discovery

Configures Neighbor Discovery (ND) for an interface. ND allows different devices on the same link to advertise their existence to their neighbors and to learn about the existence of their neighbors. ND is the IPv6 equivalent of IPv4 ARP for layer 2 address resolution.

### Usage

`nv set interface <interface-id> ip neighbor-discovery [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rdnss` | Configures recursive DNS servers (RDNSS). |
| `prefix` | Configures the IPv6 prefixes you want to include in router advertisements. |
| `dnssl` | Configure DNS search lists (DNSSL). You must specify the domain suffix you want to advertise. |
| `router-advertisement` |  Configures router advertisement for the interface. |
| `home-agent`  | Configures the switch to be a Home Agent.
| `enable` | Turns Neighbor Discovery on or off. The default is 'on'. |
| `mtu` |  Configures the MTU for neighbor discovery messages on an interface. |

### Version History

Introduced in Cumulus Linux 5.1.0

## nv set interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\>

Configures recursive DNS servers (RDNSS). You must specify the IPv6 address of each RDNSS you want to advertise.

### Usage

`nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<ipv6-address-id>` | The IPv6 address. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `lifetime` |  Configures the maximum amount of time you want to use the RDNSS for domain name resolution. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100
```

## nv set interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\> lifetime 

Configures the maximum amount of time you want to use the RDNSS for domain name resolution. You can specify a value between 0 and 4294967295, or specify `infinite` to use the RDNSS for domain name resolution indefinitely. If you set the value to 0, the RDNSS address no longer advertises.

### Usage

`nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime [options] (0-4294967295|infinite)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100 lifetime infinite
```

## nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\>

Configures the IPv6 prefix you want to include in router advertisements.

### Usage

`nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `autoconfig` | Configures automatic configuration to indicate to hosts on the local link that they can use the specified prefix for IPv6 auto configuration.|
| `off-link`  | Configures adverisement to make no statement about prefix on-link or off-link properties. |
| `preferred-lifetime` | Configures the amount of time that addresses generated from a prefix remain preferred. |
| `router-address` | Configures adverisement to indicates to hosts on the local link that the specified prefix contains a complete IP address by setting R flag. |
| `valid-lifetime` | Configures the amount of time that the prefix is valid for on-link determination. |

### Version History

Introduced in Cumulus Linux 5.1.0

## nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> valid-lifetime

Configures the amount of time that the prefix is valid for on-link determination. You can specify a value between 0 and 4294967295.

### Usage

`nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime [options] 0-4294967295`

### Default Setting

2592000

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 valid-lifetime 2000000000
```

## nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> preferred-lifetime

Configures the amount of time that addresses generated from a prefix remain preferred. You can specify a value between 0 and 4294967295.

### Usage

`nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime [options] 0-4294967295`

### Default Setting

604800

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 preferred-lifetime 1000000000
```

## nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> off-link

Configures adverisement to make no statement about prefix on-link or off-link properties.

### Usage

`nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 off-link on
```

## nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> autoconfig

Configures automatic configuration to indicate to hosts on the local link that they can use the specified prefix for IPv6 auto configuration.

### Usage

`nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 autoconfig on
```

## nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> router-address

Configures adverisement to indicates to hosts on the local link that the specified prefix contains a complete IP address by setting R flag.

### Usage

`nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 router-address on
```

## nv set interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\>

Configures the DNS search lists (DNSSL).

### Usage

`nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<domain-name-id>` |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890). |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `lifetime` |  Configure the maximum amount of time in seconds that you want to use the domain suffix for domain name resolution.  |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com
```

## nv set interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\> lifetime

Configures the maximum amount of time you want to use the domain suffix for domain name resolution. You can set a value between 0 and 4294967295 seconds or use the keyword infinte to set the time to never expire. If you set the value to 0, the host does not use the DNSSL.

### Usage

`nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime [options] (0-4294967295|infinite)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<domain-name-id>` |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890). |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com lifetime infinite
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement

Configures Router advertisement for an interface.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`enable` | Turns Router Advertisement on or off. |
|`fast-retransmit`  |  Configures Router Advertisement to allow consecutive RA packets more frequently than every 3 seconds. |
|`hop-limit` | Configures the hop limit value advertised in a Router Advertisement message. |
|`interval` |  Configures the maximum time in milliseconds allowed between sending unsolicited multicast RA from the interface. |
|`interval-option`  | Configures Router Advertiesment to indicate to hosts that the router uses an advertisement interval to send Router Advertisements.|
|`lifetime`  |  Configures the maximum time in seconds that the router can be a default gateway. |
|`managed-config` | Configures Router Advertisement to allow a dynamic host to use a managed protocol, such as DHCPv6, to configure IP addresses automatically (managed configuration). |
| `other-config`    |  Configures Router Advertisement to allow a dynamic host to use a managed protocol to configure additional information through DHCPv6.|
| `reachable-time`  |  Configures the amount of time that an IPv6 node is reachable.|
| `retransmit-time`  |  Configures interval at which neighbor solicitation messages retransmit.|
| `router-preference` | Configures Router Advertisement to allow hosts to use router preference to select the default router.|

### Version History

Introduced in Cumulus Linux 5.1.0

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement enable

Turns Router Advertisement on or off for the interface.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |


### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement enable off
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement interval

Configures the maximum time in milliseconds allowed between sending unsolicited multicast RA from the interface. You can set a value between 70 and 1800000 miliseconds.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement interval [options] 70-1800000`

### Default Setting

600000

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement interval 60000
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement interval-option

Configures the switch to indicate to hosts that the router uses an advertisement interval to send Router Advertisements.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement interval-option [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement interval-option on
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement fast-retransmit (on|off)

Configures the switch to allow consecutive Router Advertisement packets to transmit more frequently than every three seconds (fast retransmit).

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit [options] (on|off)`

### Default Setting

`on`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement fast-retransmit off
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement lifetime


Configures the maximum amount of time that Router Advertisement messages can exist on the route. You can specify a value between 0 and 9000.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime [options] 0-9000`

### Default Setting

1800

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement lifetime 4000
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement reachable-time

Configures the amount of time that an IPv6 node is reachable. You can set a value between 0 and 3600000 milliseconds.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time [options] 0-3600000`

### Default Setting

0

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement reachable-time 3600000
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement retransmit-time

Configures the interval at which neighbor solicitation messages retransmit. You can set a value between 0 and 4294967295 milliseconds.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time [options] 0-4294967295`

### Default Setting

0

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement retransmit-time 4294967295
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement managed-config

Configures the switch to allow a dynamic host to use a managed protocol, such as DHCPv6, to configure IP addresses automatically (managed configuration).

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement managed-config [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement managed-config on
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement other-config

Configures the switch to allow a dynamic host to use a managed protocol to configure additional information through DHCPv6.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement other-config [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement other-config on
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement hop-limit

Configures the hop limit value in the IP header of the outgoing Router Advertisement packet. You can set a value between 0 and 255.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit [options] 0-255`

### Default Setting

64

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement hop-limit 100
```

## nv set interface \<interface-id\> ip neighbor-discovery router-advertisement router-preference

Configures the switch to allow hosts to use router preference to select the default router. You can set a value of high, medium, or low.

### Usage

`nv set interface <interface-id> ip neighbor-discovery router-advertisement router-preference [options] (high|medium|low)`

### Default Setting

`medium`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery router-advertisement router-preference high
```

## nv set interface \<interface-id\> ip neighbor-discovery home-agent

Configures the switch to be a Home Agent.

### Usage

`nv set interface <interface-id> ip neighbor-discovery home-agent [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `lifetime` |  Configures the maximum amount of time you want the router to act as a Home Agent. You can set a value between 0 and 65520 seconds. |
| `preference` |  Configures the Home Agent router preference used to order the addresses returned in the Home Agent address discovery reply. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent 6552
```

## nv set interface \<interface-id\> ip neighbor-discovery home-agent lifetime

Configures the maximum amount of time you want the router to act as a Home Agent. You can set a value between 0 and 65520 seconds. If you set the value to 0, the router is not a Home Agent.

### Usage

`nv set interface <interface-id> ip neighbor-discovery home-agent lifetime [options] 0-65520`

### Default Setting

0

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent lifetime 0
```

## nv set interface \<interface-id\> ip neighbor-discovery home-agent preference

Configures the Home Agent router preference used to order the addresses returned in the Home Agent address discovery reply. You can set a value between 0 and 65535. 0 is the lowest preference.

### Usage

`nv set interface <interface-id> ip neighbor-discovery home-agent preference [options] 0-65535`

### Default Setting

0

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery home-agent preference 0
```

## nv set interface \<interface-id\> ip neighbor-discovery enable

Turns Neighbor Discovery on or off.

### Usage

`nv set interface <interface-id> ip neighbor-discovery enable [options] (on|off)`

### Default Setting

`on`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery enable off
```

## nv set interface \<interface-id\> ip neighbor-discovery mtu

Configures the MTU for Neighbor Discovery messages on an interface. You can set a value between 1 and 65535. 

### Usage

`nv set interface <interface-id> ip neighbor-discovery mtu [options] 1-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip neighbor-discovery mtu 1500
```

## nv set interface \<interface-id\> ip vrf \<vrf-name\>

Configures virtual routing and forwarding on the interface.

### Usage

`nv set interface <interface-id> ip vrf [options] <vrf-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrf RED
```

## nv set interface \<interface-id\> lldp

Configures Link Layer Discovery Protocol (LLDP) for an interface.

### Usage

`nv set interface <interface-id> lldp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `dcbx-ets-config-tlv` |  Configures ETS TLV transmission on the interface.|
| `dcbx-ets-recomm-tlv` |  Configures ETS Recommendation TLV transmission on the interface. |
| `dcbx-pfc-tlv` | Configures PFC TLV transmission on the interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> lldp dcbx-pfc-tlv

Configures PFC TLV transmission on the interface.

### Usage

`nv set interface <interface-id> lldp dcbx-pfc-tlv [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 lldp dcbx-pfc-tlv on
```

## nv set interface \<interface-id\> lldp dcbx-ets-config-tlv

Configures ETS TLV transmission on the interface.

### Usage

`nv set interface <interface-id> lldp dcbx-ets-config-tlv [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 lldp dcbx-ets-config-tlv on
```

## nv set interface \<interface-id\> lldp dcbx-ets-recomm-tlv

Configures ETS Recommendation TLV transmission on the interface.

### Usage

`nv set interface <interface-id> lldp dcbx-ets-recomm-tlv [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 lldp dcbx-ets-recomm-tlv on
```

## nv set interface \<interface-id\> link

Configures the physical interface settings, such as the state, auto-negotiation, breakouts, FEC, MTU, and speed.

### Usage

`nv set interface <interface-id> link [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`state` | Configures the state of the interface; up or down. |
|`dot1x`  | Configures the IEEE 802.1X protocol for the interface. |
|`auto-negotiate` | Configures auto-negotiation for the interface. |
|`breakout` | Configures breakouts for the interface. |
|`duplex` | Configures duplex mode for the interface; full or half. |
|`fec`  |  Configures Forward Error Correction (FEC) for the interface. |
|`mtu`  | Configures the MTU for the interface. |
|`speed` |  Configures the speed for the interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> link state

Configures the state of the interface; up or down.

### Usage

`nv set interface <interface-id> link state [options] (up|down)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link state up
```

## nv set interface \<interface-id\> link dot1x

Configures the IEEE 802.1X protocol for the interface.

### Usage

`nv set interface <interface-id> link dot1x [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `mab` |  Configures bypass MAC authentication. |
| `parking-vlan` | Configures a parking VLAN for unauthorized MAC addresses. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> link dot1x mab

Configures MAC authentication bypass (MAB), which enables bridge ports to allow devices to bypass authentication based on their MAC address. This is useful for devices that do not support PAE, such as printers or phones.

### Usage

`nv set interface <interface-id> link dot1x mab [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link dot1x mab on
```

## nv set interface \<interface-id\> link dot1x parking-vlan

Configures a Parking VLAN. If a non-authorized supplicant tries to communicate with the switch, you can route traffic from that device to a different VLAN and associate that VLAN with one of the switch ports to which the supplicant is attached.

### Usage

`nv set interface <interface-id> link dot1x parking-vlan [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link dot1x parking-vlan on
```

## nv set interface \<interface-id\> link auto-negotiate

Configures auto-negotiation for the interface.

### Usage

`nv set interface <interface-id> link auto-negotiate [options] (on|off)`

### Default Setting

`on`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link auto-negotiate off
```

## nv set interface \<interface-id\> link breakout 

Configures breakout ports for the interface.

### Usage

`nv set interface <interface-id> link breakout [options] (1x|2x20G|2x40G|2x50G|2x100G|2x200G|4x10G|4x25G|4x50G|4x100G|8x50G|disabled|loopback)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link breakout 4x25G
```

## nv set interface \<interface-id\> link duplex 

Configures duplex mode for the interface; full or half.

### Usage

`nv set interface <interface-id> link duplex [options] (half|full)`

### Default Setting

`full`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link duplex half
```

## nv set interface \<interface-id\> link speed

Configures the speed for the interface.

### Usage

`nv set interface <interface-id> link speed [options] (auto|10M|100M|1G|10G|25G|40G|50G|100G|200G|400G)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link speed 10G
```

## nv set interface \<interface-id\> link fec

Configures Forward Error Correction (FEC) for the interface. FEC enables the switch to detect and correct bit errors introduced over the cable between two interfaces. 

### Usage

`nv set interface <interface-id> link fec [options] (auto|baser|off|rs|driver-auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link fec baser
```

## nv set interface \<interface-id\> link mtu

Configures the maximum transmission unit (MTU) for the interface. You can set a value between 552 and 9216.

### Usage

`nv set interface <interface-id> link mtu [options] 552-9216`

### Default Setting

9216

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link mtu 1500
```

## nv set interface \<interface-id\> evpn

Configures the EVPN control plane for the interface.

### Usage

`nv set interface <interface-id> evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `multihoming` |  Configures EVPN multihoming for the interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> evpn multihoming

Configures EVPN multihoming for the interface.

### Usage

`nv set interface <interface-id> evpn multihoming [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `segment`  |  Configures the EVPN multihoming interface segment. |
| `uplink ` |  Turns EVPN multihoming tracking on or off to prevent traffic loss due to NVE connectivity loss.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> evpn multihoming segment

Configures the EVPN multihoming interface segment.

### Usage

`nv set interface <interface-id> evpn multihoming segment [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`enable` | Turns the EVPN multihoming segment on or off.|
|`df-preference`  | Configures a preference on an Ethernet segment for the designated forwarder (DF) election.  |
| `identifier` | Configures the Ethernet segment identifier. This must be unique for each segment and match other bonds in the segment.|
| `local-id`  | Configures the Ethernet segment ID.|
| `mac-address` | Configures the MAC address for this Ethernet segment.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> evpn multihoming segment enable

Turns EVPN multihoming segment on or off.

### Usage

`nv set interface <interface-id> evpn multihoming segment enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 evpn multihoming segment enable on
```

## nv set interface \<interface-id\> evpn multihoming segment local-id

Configures the Ethernet segment ID.  If provided, it will be combined with the global multihoming `mac-address` to create the ethernet segment identifier, which must be unique for each segment and match other bonds in the segment.

### Usage

`nv set interface <interface-id> evpn multihoming segment local-id [options] 1-16777215`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 evpn multihoming segment local-id 1
```

## nv set interface \<interface-id\> evpn multihoming segment identifier \<es-identifier\>

Ethernet segment identifier.  This must be unique for each segment and match other bonds in the segment.

### Usage

`nv set interface <interface-id> evpn multihoming segment identifier [options] <es-identifier>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 evpn multihoming segment identifier 1
```

## nv set interface \<interface-id\> evpn multihoming segment mac-address

Configures the MAC address for this Ethernet segment. You can specify the MAC address or `auto`. If you specify `auto`, the switch uses the global EVPN multihoming MAC address.

### Usage

`nv set interface <interface-id> evpn multihoming segment mac-address [options] (auto|<mac>)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
```

## nv set interface \<interface-id\> evpn multihoming segment df-preference

Configures a preference on an Ethernet segment for the designated forwarder (DF) election. The switch selects a DF for each Ethernet segment. The DF forwards flooded traffic received through the VXLAN overlay to the locally attached Ethernet segment. The EVPN VTEP with the highest DF preference setting becomes the DF.

### Usage

`nv set interface <interface-id> evpn multihoming segment df-preference [options] (1-65535|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
```

## nv set interface \<interface-id\> evpn multihoming uplink

Turns EVPN multihoming tracking on or off. When all uplinks go down, the VTEP loses connectivity to the VXLAN overlay. To prevent traffic loss, Cumulus Linux tracks the operational state of the uplink. When all the uplinks are down, the Ethernet segment bonds on the switch are in a protodown or error-disabled state.

### Usage

`nv set interface <interface-id> evpn multihoming segment uplink [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51-52 evpn multihoming uplink on
```

## nv set interface \<interface-id\> acl \<acl-id\>

Configures the access control list (ACL) rule to apply in the inbound or outbound direction.

### Usage

`nv set interface <interface-id> acl <acl-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<acl-id>` |  The name of the ACL. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound` | Configures the ACL rule to apply in the inbound direction. |
| `outbound` | Configures the ACL rule to apply in the outbound direction. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> acl \<acl-id\> inbound

Configures the ACL rule to apply in the inbound direction.

### Usage

`nv set interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `control-plane`  | Configures the ACL rule to apply to a control plane interface in the inbound direction. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 inbound
```

## nv set interface \<interface-id\> acl \<acl-id\> inbound control-plane

Configures the ACL rule to apply to a control plane interface in the inbound direction.

### Usage

`nv set interface <interface-id> acl <acl-id> inbound control-plane [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 inbound control-plane
```

## nv set interface \<interface-id\> acl \<acl-id\> outbound

Configures the ACL rule to apply in the outbound direction.

### Usage

`nv set interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `control-plane` | Configures the ACL rule to apply to a control plane interface in the inbound direction.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 outbound 
```

## nv set interface \<interface-id\> acl \<acl-id\> outbound control-plane

Configures the ACL rule to apply to a control plane interface in the outbound direction.

### Usage

`nv set interface <interface-id> acl <acl-id> outbound control-plane [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 outbound control-plane
```

## nv set interface \<interface-id\> ptp

Configures PTP on the interface.

### Usage

`nv set interface <interface-id> ptp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`timers`  |  Configures PTP timers on the interface.|
|`enable` | Turns PTP on or off on the interface.|
|`acceptable-master` | Configures the acceptable master table option, which is a security feature that prevents a rogue player from pretending to be the Grandmaster to take over the PTP network.|
|`delay-mechanism` |  Configures the mode in which PTP messages transmit.|
|`forced-master` | Configures PTP interfaces to always be in a master state. This interface ignores any Announce messages it receives.|
|`instance`   |Configures the PTP instance number.|
|`message-mode`| Configures the mode in which PTP delay messages transmit; multicast, unicast, or mixed.|
|`transport` | Configures the transport method for PTP messages.|
|`ttl` |    Configures the maximum number of hops the PTP messages can travel.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ptp timers

Configures timers for PTP messages, such as the average interval between successive Announce messages, the number of announce intervals that have to occur without receiving an Announce message before a timeout occurs, the minimum average time interval allowed between successive Delay Required messages, and the interval between PTP synchronization messages on an interface. 

### Usage

`nv set interface <interface-id> ptp timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `announce-interval`|  Configures the average interval between successive Announce messages.|
| `announce-timeout` | The number of announce intervals that have to occur without receiving an Announce message before a timeout occurs.|
| `delay-req-interval` | The minimum average time interval allowed between successive Delay Required messages.|
| `sync-interval` |  The interval between PTP synchronization messages on an interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> ptp timers announce-interval

Configures the average interval between successive Announce messages. You specify the value as a power of two in seconds.

### Usage

`nv set interface <interface-id> ptp timers announce-interval [options] -3-4`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers announce-interval -1
```

## nv set interface \<interface-id\> ptp timers sync-interval

The interval between PTP synchronization messages on an interface. You specify the value as a power of two in seconds.

### Usage

`nv set interface <interface-id> ptp timers sync-interval [options] -7-1`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers sync-interval -5
```

## nv set interface \<interface-id\> ptp timers delay-req-interval

The minimum average time interval allowed between successive Delay Required messages. You specify the value as a power of two in seconds.

### Usage

`nv set interface <interface-id> ptp timers delay-req-interval [options] -7-6`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers delay-req-interval -5
```

## nv set interface \<interface-id\> ptp timers announce-timeout

The number of announce intervals that have to occur without receiving an Announce message before a timeout occurs. Make sure that this value is longer than the `announce-interval` in your network.

### Usage

`nv set interface <interface-id> ptp timers announce-timeout [options] 2-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers announce-interval 2
```

## nv set interface \<interface-id\> ptp enable

Turns PTP on the interface on or off.

### Usage

`nv set interface <interface-id> ptp enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp enable on
```

## nv set interface \<interface-id\> ptp instance \<value\>

Configures the PTP instance number. 

### Usage

`nv set interface <interface-id> ptp instance [options] <value>`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1
```

## nv set interface \<interface-id\> ptp forced-master (on|off)

Configures PTP interfaces to always be in a master state. This interface ignores any Announce messages it receives.

### Usage

`nv set interface <interface-id> ptp forced-master [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp forced-master on
```

## nv set interface \<interface-id\> ptp acceptable-master (on|off)

Turns the acceptable master table option on or off for the interface. You must configure the clock IDs of known Grandmasters in the acceptable master table before turning on the acceptable master table option. The BMC algorithm checks if the Grandmaster received on the Announce message is in this table before proceeding with the master selection.

### Usage

`nv set interface <interface-id> ptp acceptable-master [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp acceptable-master on
```

## nv set interface \<interface-id\> ptp delay-mechanism end-to-end

Configures the PTP delay mechanism to be end-to-end, where the slave measures the delay between itself and the master. For PTP nodes to synchronize the time of day, each slave has to learn the delay between iteself and the master.

### Usage

`nv set interface <interface-id> ptp delay-mechanism [options] end-to-end`

### Default Setting

`peer-to-peer`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp delay-mechanism end-to-end
```

## nv set interface \<interface-id\> ptp transport 

Configures the transport method for PTP messages. You can encapsulate PTP messages in UDP/IPV4 frames or UDP/IPV6 frames.

### Usage

`nv set interface <interface-id> ptp transport [options] (ipv4|ipv6|802.3)`

### Default Setting

IPv4

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp transport ipv6
```

## nv set interface \<interface-id\> ptp ttl

Configures the maximum number of hops the PTP messages can travel.

### Usage

`nv set interface <interface-id> ptp ttl [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp ttl 20
```

## nv set interface \<interface-id\> ptp message-mode 

Configures the mode in which PTP delay messages transmit; multicast, unicast, or mixed.

### Usage

`nv set interface <interface-id> ptp message-mode [options] (multicast|unicast|mixed)`

### Default Setting

`multicast`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp message-mode mixed
```

## nv set interface \<interface-id\> tunnel

Configures Generic Routing Encapsulation (GRE) tunneling on an interface.

### Usage

`nv set interface <interface-id> tunnel [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `dest-ip` | Configures the destination underlay IP address.|
| `interface` |  Configures the physical underlay interface to use for tunnel packets.|
| `mode`   | Configures the tunnel mode to be GRE.|
| `source-ip` |Configures the source underlay IP address.|
| `ttl` | Configures the maximum number of hops through which the tunneled packets can pass.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set interface \<interface-id\> tunnel source-ip \<ipv4\>

Configures the source underlay IP address.

### Usage

`nv set interface <interface-id> tunnel source-ip [options] <ipv4>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel source-ip 10.10.10.1
```

## nv set interface \<interface-id\> tunnel dest-ip \<ipv4\>

Configures the destination underlay IP address.

### Usage

`nv set interface <interface-id> tunnel dest-ip [options] <ipv4>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel dest-ip 10.10.10.3
```

## nv set interface \<interface-id\> tunnel ttl

Configures the maximum number of hops through which the tunneled packets can pass.

### Usage

`nv set interface <interface-id> tunnel ttl [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel ttl 255
```

## nv set interface \<interface-id\> tunnel mode gre

Configures the tunnel mode to be GRE.

### Usage

`nv set interface <interface-id> tunnel mode [options] gre`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel mode gre
```

## nv set interface \<interface-id\> tunnel interface \<interface-name\>

Configures the physical underlay interface to use for tunnel packets.

### Usage

`nv set interface <interface-id> tunnel interface [options] <interface-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnel interface tunnelR2 
```

## nv set interface \<interface-id\> description \<value\>

Configures a description for the interface. Interface descriptions can have a maximum of 256 characters. Avoid using apostrophes or non-ASCII characters.

### Usage

`nv set interface <interface-id> description [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 description hypervisor_port_1
```

## nv set interface \<interface-id\> type

Configures the interface type; swp, eth, bond, loopback, svi, subinterface, peerlink, or tunnel.

### Usage

`nv set interface <interface-id> type [options] (swp|eth|bond|loopback|svi|sub|peerlink|tunnel)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 type bond
```

## nv set interface \<interface-id\> base-interface (none|<interface-name>)

Configures the base interface under this interface.

### Usage

`nv set interface <interface-id> base-interface [options] (none|<interface-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1.100 base-interface swp1
```

## nv set interface \<interface-id\> vlan

Configures the VLAN ID. You can specify a value between 1 and 4094.

### Usage

`nv set interface <interface-id> vlan [options] 1-4094`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 vlan 10
```

## nv set service

Configures a service, such as DNS, NTP, DHCP relay, PTP, DHCP server, and LLDP.

### Usage

`nv set service [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `dns`  | Configures the Domain Name Server (DNS) service. |
| `syslog`  |  Configures the `syslog` service. |
| `ntp`  | Configures NTP service.|
| `dhcp-relay` | Configures DHCP relay for IPv4. |
| `dhcp-relay6` |  Configures DHCP relay for IPv6.|
| `ptp`  | Configures the PTP service.|
| `dhcp-server` |  Configures DHCP servers for IPv4.|
| `dhcp-server6`|  Configures DHCP servers for IPv6.|
| `lldp` | Configures Link Layer Discovery Protocol (LLDP). |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dns \<vrf-id\>

Configures the Domain Name Server (DNS) service. 

### Usage

`nv set service dns <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `server`   | Configures remote DNS servers.

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dns \<vrf-id\> server \<dns-server-id\>

Configures a remote DNS server.

### Usage

`nv set service dns <vrf-id> server <dns-server-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>`         | The VRF you want to configure. |
| `<dns-server-id>`  | The IPv4 or IPv6 address of the remote DNS server.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dns default server 192.0.2.44
```

## nv set service syslog \<vrf-id\>

Configures the System Logging Protocol (`syslog`) service so that the switch can use a standard message format to communicate with a logging server.

### Usage

`nv set service syslog <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `server`| Configures the remote `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service syslog \<vrf-id\> server \<server-id\>

Configures the remote `syslog` server.

### Usage

`nv set service syslog <vrf-id> server <server-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `port`   | Configures the port number of the remote `syslog server`.|
| `protocol` |  Configures the protocol of the remote `syslog` server (UDP or TCP).|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service syslog \<vrf-id\> server \<server-id\> port

Configures the port number of the remote `syslog` server.

### Usage

`nv set service syslog <vrf-id> server <server-id> port [options] 1-32767`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service syslog default server 192.168.0.254 port 514
```

## nv set service syslog \<vrf-id\> server \<server-id\> protocol (tcp|udp)

Configures the protocol you want to use to transmit syslog data. You can specify wither UDP or TCP.

### Usage

`nv [options] set service syslog <vrf-id> server <server-id> protocol <arg>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |
| `<arg>` |  The protocol you want to use: UDP or TCP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service syslog default server 192.168.0.254 protocol tcp
```

## nv set service ntp \<vrf-id\>

Configures the Network Time Protocol (NTP).

### Usage

`nv set service ntp <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `server` | Configures the remote NTP server. |
| `pool` | Configures the remote NTP Server pool. |
| `listen` | Configures the NTP interface on which to listen.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service ntp \<vrf-id\> server \<server-id\>

Configures the remote NTP server.

### Usage

`nv set service ntp <vrf-id> server <server-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `iburst` |  Configures NTP to send a burst of eight packets instead of the usual one packet when the server is unreachable. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default server 
```

## nv set service ntp \<vrf-id\> server \<server-id\> iburst

Configures NTP to send a burst of eight packets instead of the usual one packet when the server is unreachable. You can specify `on` or `off`.

### Usage

`nv [options] set service ntp <vrf-id> server <server-id> iburst`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default server 192.168.0.254 iburst on
```

## nv set service ntp \<vrf-id\> pool \<server-id\>

Configures the remote NTP server pool.

### Usage

`nv set service ntp <vrf-id> pool <server-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the NTP server. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `iburst` | Configures NTP to send a burst of eight packets instead of the usual one packet when the server is unreachable.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service ntp \<vrf-id\> pool \<server-id\> iburst

Configures NTP to send a burst of eight packets instead of the usual one packet when the server pool is unreachable. You can specify `on` or `off`.

### Usage

`nv [options] set service ntp <vrf-id> pool <server-id> iburst`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The NTP server pool. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default pool 4.cumulusnetworks.pool.ntp.org iburst on
```

## nv set service ntp \<vrf-id\> listen \<interface-name\>

Configures the NTP interface on which to listen.

### Usage

`nv set service ntp <vrf-id> listen [options] <interface-name>`

### Default Setting

`eth0`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-name>` |  The NTP interface on which to listen. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default listen swp10
```

## nv set service dhcp-relay \<vrf-id\>

Configures DHCP relays for IPv4 and IPv6.

### Usage

`nv set service dhcp-relay <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`server` |   Configures the DHCP server. |
|`interface` | Configures the interfaces participating in DHCP relay (facing the server and facing the client). |
|`giaddress-interface` | Configures the gateway IP address on an interface. |
|`source-ip` | Configures the source IP address to use on the relayed packet. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-relay \<vrf-id\> server \<server-id\>

Configures the DHCP server.

### Usage

`nv set service dhcp-relay <vrf-id> server <server-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The DHCP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default server 172.16.1.102
```

## nv set service dhcp-relay \<vrf-id\> interface \<interface-id\>

Configures the interfaces on which to configure DHCP relay.

### Usage

`nv set service dhcp-relay <vrf-id> interface <interface-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` |  The interface on which to configure DHCP relay. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default interface swp51
```

## nv set service dhcp-relay \<vrf-id\> giaddress-interface \<interface-id\>

Configures the gateway IPv4 address on an interface.

### Usage

`nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` | The gateway IPv4 address. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `giaddress-interface` | Configures the gateway IPv4 address on an interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default giaddress-interface lo
```

## nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id> address (auto|<ipv4>)

Configures the IPv4 address on the gateway interface.

### Usage

`nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id> address <ipv4-address> [options] (auto|<ipv4>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` | The gateway IP address. |
| `<ipv4-address>` | The IPv4 address on the gateway interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default giaddress-interface address lo 10.10.10.1
```

## nv set service dhcp-relay \<vrf-id\> source-ip

Configures the source IP address to use on the relayed packet.

### Usage

`nv set service dhcp-relay <vrf-id> source-ip [options] (auto|<ipv4>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default source-ip giaddress
```

## nv set service dhcp-relay6 \<vrf-id\>

Configures DHCP relay for IPv6.

### Usage

`nv set service dhcp-relay6 <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-relay6 \<vrf-id\> interface

Configures the DHCP relay IPv6 interfaces.

### Usage

`nv set service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `upstream`  |  Configures the upstream interface for DHCP relay for IPv6. |
| `downstream` | Configures the downstream interface for DHCP relay for IPv6.  |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\>

Configures the upstream interface for DHCP relay for IPv6.

### Usage

`nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay upstream interface. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address` |  The IPv6 address on the interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\> address \<ipv6\>

Configures the IPv6 address on the DHCP relay upstream interface.

### Usage

`nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address [options] <ipv6>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay6 default interface upstream swp51 address 2001:db8:0002::0a00:0002
```

## nv set service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\>

Configures the DHCP relay downstream interface.

### Usage

`nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay interface |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address`   | Configures the IPv6 address on downstream interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\> address \<ipv6\>

Configures the IPv6 address on downstream interface.

### Usage

`nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address [options] <ipv6>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay downstream interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay6 default interface downstream swp1 address 2001:db8::1
```

## nv set service ptp \<instance-id\>

Configures global Precision Time Protocol (PTP) settings.

### Usage

`nv set service ptp <instance-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `acceptable-master` |  Configures the acceptable master table. |
| `monitor` |  Configures PTP monitor settings. |
| `enable` | Turns PTP on or off. |
| `domain`   |  Configures the domain number of the current syntonization. |
| `ip-dscp`  | Configures the DiffServ code point (DSCP) value for all PTP IPv4 packets originated locally. |
| `priority1`  |  Configures Priority 1 attribute of the local clock to override the clock class and quality selection criteria to select the best master clock.|
| `priority2` |  Configures Priorit 2 attribute of the local clock to identify primary and backup clocks among identical redundant Grandmasters.|
| `two-step` |  Configures two-step clock mode.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service ptp \<instance-id\> acceptable-master \<clock-id\>

Configures the ID of a known Grandmaster clock in the acceptable master table. This setting prevents a rogue player from pretending to be the Grandmaster to take over the PTP network.

### Usage

`nv set service ptp <instance-id> acceptable-master <clock-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<clock-id>` |  The clock ID. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `alt-priority` |   Configures an alternate priority for the Grandmaster clock in the acceptable master table. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06
```

## nv set service ptp \<instance-id\> acceptable-master \<clock-id\> alt-priority \<value\>

 Configures an alternate priority for the acceptable Grandmaster clock in the acceptable master table.

### Usage

`nv set service ptp <instance-id> acceptable-master <clock-id> alt-priority [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<clock-id>` |  The clock ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06 alt-priority 2
```

## nv set service ptp \<instance-id\> monitor

Configures PTP monitor settings.

### Usage

`nv set service ptp <instance-id> monitor [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `max-offset-threshold` | Configures the maximum difference allowed in nanoseconds between the master and slave time. |
| `max-timestamp-entries` | Configures the maximum number of timestamp entries allowed. |
| `max-violation-log-entries` | Configures the maximum number of violation log entries allowed for each set. |
| `max-violation-log-sets` | Configures the maximum number of violation log sets allowed.  |
| `min-offset-threshold` | Configures the minimum difference allowed in nanoseconds between the master and slave time. |
| `path-delay-threshold` | Configures the mean time in nanoseconds that PTP packets take to travel between the master and slave. |
| `violation-log-interval` | Configures the violation log interval in seconds. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service ptp \<instance-id\> monitor min-offset-threshold \<value\>

Sets the minimum difference allowed in nanoseconds between the master and slave time.

### Usage

`nv set service ptp <instance-id> monitor min-offset-threshold [options] <value>`

### Default Setting

-50

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor min-offset-threshold -20
```

## nv set service ptp \<instance-id\> monitor max-offset-threshold \<value\>

Configures the maximum difference allowed in nanoseconds between the master and slave time.

### Usage

`nv set service ptp <instance-id> monitor max-offset-threshold [options] <value>`

### Default Setting

50

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-offset-threshold 30
```

## nv set service ptp \<instance-id\> monitor path-delay-threshold \<value\>

Configures the mean time in nanoseconds that PTP packets take to travel between the master and slave.

### Usage

`nv set service ptp <instance-id> monitor . [options] <value>`

### Default Setting

200

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor path-delay-threshold 300
```

## nv set service ptp \<instance-id\> monitor max-timestamp-entries

Configures the maximum number of timestamp entries allowed. PTP updates the timestamps continuously. You can specify a value between 400 and 1000.

### Usage

`nv set service ptp <instance-id> monitor max-timestamp-entries [options] 400-1000`

### Default Setting

400

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-timestamp-entries 600
```

## nv set service ptp \<instance-id\> monitor max-violation-log-sets

Configures the maximum number of violation log sets allowed. You can specify a value between 8 and 128.

### Usage

`nv set service ptp <instance-id> monitor max-violation-log-sets [options] 8-128`

### Default Setting

8

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-violation-log-sets 20
```

## nv set service ptp \<instance-id\> monitor max-violation-log-entries

Configures the maximum number of violation log entries allowed for each set. You can specify a value between 8 and 128.

### Usage

`nv set service ptp <instance-id> monitor max-violation-log-entries [options] 8-128`

### Default Setting

8

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-violation-log-entries 16
```

## nv set service ptp \<instance-id\> monitor violation-log-interval

Configures the violation log interval in seconds. You can specify a value between 0 and 259200 seconds.

### Usage

`nv set service ptp <instance-id> monitor violation-log-interval [options] 0-259200`

### Default Setting

0

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor violation-log-interval 1000
```

## nv set service ptp \<instance-id\> enable

Turns PTP on or off.

### Usage

`nv set service ptp <instance-id> enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 enable on
```

## nv set service ptp \<instance-id\> two-step

Turns PTP two-step mode on or off.

### Usage

`nv set service ptp <instance-id> two-step [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 two-step on
```

## nv set service ptp \<instance-id\> priority1 \<value\>

Configures PTP priority 1 to override the clock class and quality selection criteria and select the best master clock. You can set a value between 0 and 255.  For the boundary clock, use a number above 128. The lower priority applies first.

### Usage

`nv set service ptp <instance-id> priority1 [options] <value>`

### Default Setting

128

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 priority1 200
```

## nv set service ptp \<instance-id\> priority2 \<value\>

Configures PTP priority 2 to identify primary and backup clocks among identical redundant Grandmasters. You can set a value between 0 and 255.  For the boundary clock, use a number above 128. The lower priority applies first.

### Usage

`nv set service ptp <instance-id> priority2 [options] <value>`

### Default Setting

128

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 priority2 200
```

## nv set service ptp \<instance-id\> domain

Configures the PTP domain, which is a network or a portion of a network within which all the clocks synchronize. Every PTP message contains a domain number. A PTP instance works in only one domain and ignores messages that contain a different domain number.

You can specify multiple PTP clock domains. PTP isolates each domain from other domains so that each domain is a different PTP network. You can specify a number between 0 and 127.



### Usage

`nv set service ptp <instance-id> domain [options] 0-127`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 domain 3
```

## nv set service ptp \<instance-id\> ip-dscp

Configures the DiffServ code point (DSCP) value for all PTP IPv4 packets originated locally. You can set a value between 0 and 63.

### Usage

`nv set service ptp <instance-id> ip-dscp [options] 0-63`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 ip-dscp 22
```

## nv set service dhcp-server \<vrf-id\>

Configures the Dynamic Host Configuration Protocol Server (DHCP server) for IPv4.

### Usage

`nv set service dhcp-server <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `interface` | Configures the DHCP client interface.|
| `pool` |  Configfures the DHCP pool. |
| `domain-name`  |  Configures the DHCP domain name. |
| `domain-name-server` | Configures the DHCP domain name server. |
| `static`  | Configures a DHCP client with a fixed IP address assignment. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server \<vrf-id\> interface \<interface-id\>

Configures the DHCP client interface.

### Usage

`nv set service dhcp-server <vrf-id> interface <interface-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default interface swp1
```

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\>

Configures a DHCP pool.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP pool subnet. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain-name-server` |   Configures the remote DHCP domain name server you want to use in this pool.|
| `domain-name` | Configures the DHCP domain name you want to use in this pool. |
| `gateway` | Configures the DHCP gateway you want to use in this pool. |
| `range`  | Configures the IP Address range you want to use in this pool.|
| `cumulus-provision-url` | Configures a specific URL for the provisioning script. |
| `default-url` | Confifgures the default URL. |
| `lease-time`  | Configures the network address lease time in seconds assigned to DHCP clients.|
| `ping-check` |  Configures the DHCP server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range. |
| `pool-name` |  Configures the pool name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

Configures the remote DHCP domain name server you want to use in this pool.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` |  The remote DHCP domain name server . |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name-server 192.168.200.53 
```

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name you want to use in this pool.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain-name` |  Configures the DHCP domain name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name example.com
```

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\>

Configures the DHCP gateway you want to use in this pool.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<gateway-id>` | The DHCP gateway. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 gateway 10.1.10.1
```

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\>

Configures the start of the IP address range you want to use in this pool.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The start of the IP address range. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `to` |   Configures the end of the IP address range you want to use in this pool. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\> to \<ipv4\>

Configures the end of the IP address range you want to use in this pool.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to [options] <ipv4>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The end of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100 to 10.1.10.199
```

## nv set service dhcp-server  \<vrf-id\> pool \<pool-id\> pool-name \<value\>

Configures the pool name.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> pool-name [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 pool-name storage-servers
```

## nv set service dhcp-server  \<vrf-id\> pool \<pool-id\> lease-time

Configures the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> lease-time [options] 180-31536000`

### Default Setting

600

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 lease-time 200000
```

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> ping-check

Configures the DHCP server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> ping-check [options] (on|off)`

### Default Setting

off

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 ping-check on
```

## nv set service dhcp-server  \<vrf-id\> pool \<pool-id\> default-url \<value\>

Confifgures the default URL for the pool.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> default-url [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 default-url ???
```

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> cumulus-provision-url <value>

Configures a specific URL for the provisioning script.

### Usage

`nv set service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 cumulus-provision-url ???
```

## nv set service dhcp-server \<vrf-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name.

### Usage

`nv set service dhcp-server <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<domain-name-id>` |  The DHCP domain name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain-name` |  Configures the DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server \<vrf-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\>

Configures the Internationalized Domain Name (IDN) you want to use in this pool

### Usage

`nv set service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<domain-name-id>` |  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default domain-name example.com domain-name ?????
```

## nv set service dhcp-server \<vrf-id\> domain-name-server \<server-id\>

Confgures a remote DNS server to use globally.

### Usage

`nv set service dhcp-server <vrf-id> domain-name-server <server-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default domain-name-server 192.168.200.53.
```

## nv set service dhcp-server \<vrf-id\> static \<static-id\>

Configures a static IP address for a resource, such as a server or printer. 

### Usage

`nv set service dhcp-server <vrf-id> static <static-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource to which you want to assign a static IP address. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `cumulus-provision-url` | Cumulus specific URL for provisioning script|
| `ip-address` | IP address |
| `mac-address` | MAC (hardware) address |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server \<vrf-id\> static \<static-id\> mac-address \<mac\>

Configures the MAC address of the resource to which you want to assign a static IP address.

### Usage

`nv set service dhcp-server <vrf-id> static <static-id> mac-address [options] <mac>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1 mac-address 44:38:39:00:01:7e
```

## nv set service dhcp-server \<vrf-id\> static \<static-id\> ip-address \<ipv4\>

Configures the static IP address.

### Usage

`nv set service dhcp-server <vrf-id> static <static-id> ip-address [options] <ipv4>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1 ip-address 10.0.0.2
```

## nv set service dhcp-server \<vrf-id\> static \<static-id\> cumulus-provision-url \<value\>

Configures a URL for a provisioning script.

### Usage

`nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1 cumulus-provision-url http://192.0.2.1/myscript.sh
```

## nv set service dhcp-server6 \<vrf-id\>

Configures the Dynamic Host Configuration Protocol Server (DHCP server) for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `interface`  | Configures the DHCP client interface for IPv6. |
| `pool` | Configfures DHCP IP pools for IPv6.|
| `domain-name`  | Configures DHCP domain names for IPv6.|
| `domain-name-server`|  Configures DHCP domain name servers for IPv6.|
| `static` | Configures DHCP clients with fixed IP address assignments for IPv6.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server6 \<vrf-id\> interface \<interface-id\>

Configures the DHCP client interface for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> interface <interface-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\>

Configfures DHCP IP pools for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`domain-name-server`| Configures the remote DHCP domain name server you want to use in this pool.|
|`domain-name` | Configures the DHCP domain name you want to use in this pool.|
|`range`  |  Configures the IP Address range you want to use in this pool.|
|`cumulus-provision-url` | Configures a specific URL for the provisioning script.|
|`default-url`  | Confifgures the default URL.|
|`lease-time` | Configures the network address lease time in seconds assigned to DHCP clients.|
|`ping-check` | Configures the DHCP server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range.|
|`pool-name` | Configures the pool name.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

Configures the remote DHCP domain name server you want to use in this pool.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<server-id>`  | The DNS server IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 2001:db8::1/128 domain-name-server 2001:4860:4860::8888
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name you want to use in this pool.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<domain-name-id>`|  The DHCP domain name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain-name`| Configures the DHCP domain name.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\>

Configures the Internationalized Domain Name (IDN) you want to use in this pool for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<domain-name-id>`|  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 2001:db8::1/128 domain-name example.com domain-name ?????
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\>

Configures the start of the DHCP pool range for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<range-id>`|  The start of the DHCP pool range. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `to` |  End of the range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 2001:db8::1/128 range ?????
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\> to \<ipv6\>

Configures the end of the DHCP pool range for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to [options] <ipv6>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|
| `<range-id>` | The end of the DHCP pool range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 2001:db8::1/128 range ????? to ????
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> pool-name \<value\>

Configures the DHCP pool name for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> pool-name [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 pool-name storage-servers
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> lease-time

Configures the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time [options] 180-31536000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 lease-time 200000
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> ping-check

Configures the DHCP6 server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> ping-check [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 ping-check on
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> default-url \<value\>

Confifgures the default URL for the IPv6 pool.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 default-url ????
```

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> cumulus-provision-url \<value\>

Configures a specific URL for the provisioning script.

### Usage

`nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 cumulus-provision-url ????
```

## nv set service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name for IPv6.

### Usage

`nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<domain-name-id>`|  The DHCP6 domain name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain-name` | Configures the DHCP6 domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default domain-name example.com
```

## nv set service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\>

Configures the Internationalized Domain Name (IDN) of the IPv6 DHCP server.

### Usage

`nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<domain-name-id>`|  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default domain-name example.com domain-name ????
```

## nv set service dhcp-server6 \<vrf-id\> domain-name-server \<server-id\>

Configures the remote DNS server.

### Usage

`nv set service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default domain-name-server 2001:db8::1/128
```

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\>

Configures a static DHCP6 server for a resource, such as a server or printer.

### Usage

`nv set service dhcp-server6 <vrf-id> static <static-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `cumulus-provision-url` | Configures a specific URL for a provisioning script. |
| `ip-address`   |  Configures the IPv6 address for the static DHCP6 server.  |
| `mac-address` | Configures the MAC (hardware) address for the static DHCP6 server. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\> mac-address \<mac\>

Configures the MAC (hardware) address for the static DHCP6 server.

### Usage

`nv set service dhcp-server6 <vrf-id> static <static-id> mac-address [options] <mac>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default static server1 mac-address 44:38:39:00:01:7e
```

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\> ip-address \<ipv6\>

Configures the IPv6 address for the static DHCP6 server.

### Usage

`nv set service dhcp-server6 <vrf-id> static <static-id> ip-address [options] <ipv6>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default static server1 ip-address 2001:db8::1/128
```

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\> cumulus-provision-url \<value\>

Configures a URL for a provisioning script.

### Usage

`nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url [options] <value>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default static server1 cumulus-provision-url ????
```

## nv set service lldp

Configures Link Layer Discovery Protocol LLDP globally on the switch.

### Usage

`nv set service lldp [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `dot1-tlv` |  Turns dot1 TLV advertisements on or off. |
| `tx-hold-multiplier`  | Configures the amount of time to hold the information before discarding it. The hold time interval is a multiple of the tx-interval. |
| `tx-interval` | Configures the frequency of LLDP updates. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set service lldp tx-interval

Configures the frequency of LLDP updates. You can specify a value between 10 and 300.

### Usage

`nv set service lldp tx-interval [options] 10-300`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp tx-interval 100
```

## nv set service lldp tx-hold-multiplier

Configures the amount of time to hold the information before discarding it. The hold time interval is a multiple of the tx-interval.

### Usage

`nv set service lldp tx-hold-multiplier [options] 1-10`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp tx-hold-multiplier 3
```

## nv set service lldp dot1-tlv

Turns dot1 TLV advertisements on or off.

### Usage

`nv set service lldp dot1-tlv [options] (on|off)`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp dot1-tlv on
```

## nv set system

Configures system-wide settings.

### Usage

`nv set system [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `control-plane` | Configures control plane settings, such as policers and traps.|
| `message` | Configures system pre login and post login messages.|
| `global` |   Configures the global system settings. |
| `port-mirror`  | Configures port mirror settings. |
| `config` | Affects how configuration operations are performed.|
| `hostname`| Configures a static hostname for the system. |
| `timezone` |  Configures the system time zone. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system control-plane

Configures control plane settings to ensure quality of service for traffic on the control plane and rate limit traffic so incoming packets drop if they exceed certain thresholds.

### Usage

`nv set system control-plane [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `trap`  | Configures traps. For example, you can configure the switch to drop all IP packets that are larger in size than the MTU value for the egress layer 3 interface instead of fragmenting packets. |
| `policer`  | Configures quality of service (QoS) policers to rate limit traffic so incoming packets get dropped if they exceed specified thresholds. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system control-plane trap \<trap-id\>

Configures QoS traps. For example, you can configure the switch to drop all IP packets that are larger in size than the MTU value for the egress layer 3 interface instead of fragmenting packets.

### Usage

`nv set system control-plane trap <trap-id> [options] [<attribute> ...]`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<trap-id>` |  The trap ID, such as `l3-mtu-err`. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `state` | Configures the trap state; on or off. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system control-plane trap \<trap-id\> state

Turns the QoS trap on or off.

### Usage

`nv set system control-plane trap <trap-id> state [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<trap-id>` |  The trap ID, such as `l3-mtu-err`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane trap l3-mtu-err state on
```

## nv set system control-plane policer \<policer-id\>

Configures quality of service (QoS) policers to rate limit traffic so incoming packets get dropped if they exceed specified thresholds.

### Usage

`nv set system control-plane policer <policer-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<policer-id>` |  The trap group: arp, bfd, pim-ospf-rip, bgp, clag, icmp-def, dhcp-ptp, igmp, ssh, icmp6-neigh, icmp6-def-mld, lacp, lldp, rpvst, eapol, ip2me, acl-log, nat, stp, l3-local, span-cpu, catch-all, or NONE. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `burst` | Configures the policer burst rate for the trap group, which is the number of packets allowed to arrive sequentially. |
| `rate`  | Configures the forwarding rate for the trap group, which is the maximum rate in kilobytes (KB) or packets. |
| `state` | Turns the policer on or off. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system control-plane policer \<policer-id\> state

Turns the policer on or off.

### Usage

`nv set system control-plane policer <policer-id> state [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<policer-id>` | The trap group: arp, bfd, pim-ospf-rip, bgp, clag, icmp-def, dhcp-ptp, igmp, ssh, icmp6-neigh, icmp6-def-mld, lacp, lldp, rpvst, eapol, ip2me, acl-log, nat, stp, l3-local, span-cpu, catch-all, or NONE.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane policer bfd state on 
```

## nv set system control-plane policer \<policer-id\> burst

Configures the policer burst rate for the trap group. The burst rate is the number of packets allowed to arrive sequentially. You can specify a value between 10 and 10000.

### Usage

`nv set system control-plane policer <policer-id> burst [options] 10-10000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<policer-id>` | The trap group: arp, bfd, pim-ospf-rip, bgp, clag, icmp-def, dhcp-ptp, igmp, ssh, icmp6-neigh, icmp6-def-mld, lacp, lldp, rpvst, eapol, ip2me, acl-log, nat, stp, l3-local, span-cpu, catch-all, or NONE.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane policer bfd burst 100 
```

## nv set system control-plane policer \<policer-id\> rate

Configures the forwarding rate for the trap group. The forwarding rate is the maximum rate in kilobytes (KB) or packets. You can specify a value between 10 and 10000.

### Usage

`nv set system control-plane policer <policer-id> rate [options] 10-10000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<policer-id>` | The trap group: arp, bfd, pim-ospf-rip, bgp, clag, icmp-def, dhcp-ptp, igmp, ssh, icmp6-neigh, icmp6-def-mld, lacp, lldp, rpvst, eapol, ip2me, acl-log, nat, stp, l3-local, span-cpu, catch-all, or NONE. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane policer bfd rate 100
```

## nv set system message

Configures pre-login and post-login system messages.

### Usage

`nv set system message [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `post-login` | Configures a post-login system message of the day. |
| `pre-login`  | Configures a pre-login system message. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system message pre-login \<value\>

Configures a pre-login system message. Use quotes around any message that is more than one word long.

### Usage

`nv set system message pre-login [options] <value>`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system message pre-login "add message here"
```

## nv set system message post-login \<value\>

Configures a post-login system message of the day. Use quotes around any message that is more than one word long.

### Usage

`nv set system message post-login [options] <value>`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system message post-login "add message here"
```

## nv set system global

Configure global system settings, such as the rack MAC address and the first hop router MAC adress.

### Usage

`nv set system global [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `reserved`   |  Configures the reserved routing table and reserved VLAN ranges.|
| `anycast-id`  | Configures the rack MAC address in the range 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff|
| `anycast-mac`| Configures the MAC address shared by the rack.|
| `fabric-id`  |  Configures the first hop router MAC adress in the range 00:00:5E:00:01:01 and 00:00:5E:00:01:ff|
| `fabric-mac` |  Configures the first hop router MAC address. |
| `system-mac` |  Configures the full system MAC address.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system global reserved

Configures the reserved routing table and reserved VLAN ranges.

### Usage

`nv set system global reserved [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `routing-table` |  Configures the reserved routing table ranges. |
| `vlan` |   Configures the reserved VLAN ranges. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system global reserved routing-table

Configures the reserved routing table ranges. 

### Usage

`nv set system global reserved routing-table [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `pbr` |  Configures the reserved routing table ranges for (Policy Based Routing) PBR. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system global reserved routing-table pbr

Configures the reserved routing table ranges for (Policy Based Routing) PBR.

### Usage

`nv set system global reserved routing-table pbr [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `begin`|  Configures the start of the reserved routing table range for PBR. |
| `end`  | Configures the end of the reserved routing table range for PBR. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system global reserved routing-table pbr begin

Configures the start of the reserved routing table range for PBR. You can specify a value between 10000 and 4294966272.

### Usage

`nv set system global reserved routing-table pbr begin [options] 10000-4294966272`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global reserved routing-table pbr begin 20000
```

## nv set system global reserved routing-table pbr end

Configures the end of the reserved routing table range for PBR. You can specify a value between 10000 and 4294966272.

### Usage

`nv set system global reserved routing-table pbr end [options] 10000-4294966272`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global reserved routing-table pbr end 20000
```

## nv set system global reserved vlan

Configures the reserved VLAN ranges.

### Usage

`nv set system global reserved vlan [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `l3-vni-vlan` |  Configures the reserved VLAN range used with a layer 3 VNI. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system global reserved vlan l3-vni-vlan

Configures the reserved VLAN range used with layer 3 VNIs.

### Usage

`nv set system global reserved vlan l3-vni-vlan [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `begin`  | Configures the start of the reserved vlan range for layer 3 VNIs.|
| `end`  |  Configures the end of the reserved vlan range for layer 3 VNIs.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system global reserved vlan l3-vni-vlan begin

Configures the start of the reserved vlan range for layer 3 VNIs. You can specify a value between 1 and 4093.

### Usage

`nv set system global reserved vlan l3-vni-vlan begin [options] 1-4093`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global reserved vlan l3-vni-vlan begin 4093
```

## nv set system global reserved vlan l3-vni-vlan end

Configures the end of the reserved vlan range for layer 3 VNIs.

### Usage

`nv set system global reserved vlan l3-vni-vlan end [options] 2-4093`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global reserved vlan l3-vni-vlan end 4093
```

## nv set system global system-mac

Configures the global system MAC address.

### Usage

`nv set system global system-mac [options] (auto|<mac>)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global system-mac 44:38:39:be:ef:aa
```

## nv set system global anycast-mac (none|<mac>)

Configures the global anycast MAC address, which is unique for each active-active pair. In EVPN symmetric routing configurations with VXLAN active-active (MLAG), all EVPN routes advertise with the anycast MAC address as the router MAC address.

### Usage

`nv set system global anycast-mac [options] (auto|<mac>)`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global anycast-mac 44:38:39:be:ef:aa
```

## nv set system global anycast-id

Configures the anycast MAC ID, from which Cumulus Linux derives the MAC address. You can specify a number between 1 and 65535. Cumulus Linux adds the number to the MAC address 44:38:39:ff:00:00 in hex. For example, if you specify 225, the anycast MAC address is 44:38:39:ff:00:FF.

### Usage

`nv set system global anycast-id [options] (1-65535|none)`

### Default Setting

1

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global anycast-id 225
```

## nv set system global fabric-mac (none|<mac>)

Configures a fabric-wide MAC address to ensure consistency across VRR switches, which is especially useful in an EVPN multi-fabric environment. You can specify a value in the reserved range between 00:00:5E:00:01:00 and 00:00:5E:00:01:FF. Be sure to use an address in this reserved range to prevent MAC address conflicts with other interfaces in the same bridged network.

### Usage

`nv set system global fabric-mac [options] (none|<mac>)`

### Default Setting

00:00:5E:00:01:01

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global fabric-mac 00:00:5E:00:01:FF
```

## nv set system global fabric-id

Configures a fabric ID, from which Cumulus Linux derives the fabric-wide MAC address to ensure consistency across VRR switches. This is especially useful in an EVPN multi-fabric environment. You can specify a number between 1 and 225. Cumulus Linux adds the number to the MAC address 00:00:5E:00:01:00 in hex. For example, if you specify 225, the VRR MAC address is 00:00:5E:00:01:FF.
The default VRR MAC address is 00:00:5E:00:01:01, which the switch derives from a fabric ID setting of 1.

### Usage

`nv set system global fabric-id [options] 1-255`

### Default Setting

1

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system global fabric-id 225
```

## nv set system port-mirror

Configures Switched Port Analyzer (SPAN) and Encapsulated Remote Span (ERSPAN). SPAN enables you to mirror all packets that come in from or go out of an interface (the SPAN source), and copy and transmit the packets out of a local port or CPU (the SPAN destination) for monitoring. ERSPAN enables the mirrored packets to go to a monitoring node located anywhere across the routed network.

### Usage

`nv set system port-mirror [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `session`  |  The port mirror session.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system port-mirror session \<session-id\>

Configures the port mirror session number, which is a number between 0 and 7.

### Usage

`nv set system port-mirror session <session-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number, which is a number between 0 and 7. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `span`  |  Configures Switched Port Analyzer (SPAN). |
| `erspan` | Configures Encapsulated Remote Switched Port Analyzer (ERSPAN). |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system port-mirror session \<session-id\> span

Configures SPAN, which enables you to mirror all packets that come in from or go out of an interface (the SPAN source), and copy and transmit the packets out of a local port or CPU (the SPAN destination) for monitoring.

### Usage

`nv set system port-mirror session <session-id> span [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number, which is a number between 0 and 7. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `source-port` |  Configures the SPAN source port.|
| `destination` |  Configures the SPAN destination port.|
| `truncate`  | Configures truncation to decrease bandwidth by reducing the size of monitored packets.|
| `enable`  | Turn SPAN on or off. |
| `direction` | Configures the direction of traffic through the source port.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system port-mirror session \<session-id\> span source-port \<port-id\>

Configures the port mirror source port (switch ports or bonds only).

### Usage

`nv set system port-mirror session <session-id> span source-port <port-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>`  |  The interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span source-port swp1
```

## nv set system port-mirror session \<session-id\> span destination \<port-id\>

Configures the SPAN destination port.

### Usage

`nv set system port-mirror session <session-id> span destination <port-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>`  |  The interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span destination swp2
```

## nv set system port-mirror session \<session-id\> span truncate

Configures truncation to decrease bandwidth by reducing the size of monitored packets.

### Usage

`nv set system port-mirror session <session-id> span truncate [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns SPAN truncation on or off. |
| `size`   | Truncates the mirrored frames at the specified number of bytes. The truncate size must be between 4 and 4088 bytes and a multiple of 4.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system port-mirror session \<session-id\> span truncate enable

Turns truncation on or off.

### Usage

`nv set system port-mirror session <session-id> span truncate enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span truncate enable on
```

## nv set system port-mirror session \<session-id\> span truncate size

Configures the size in bytes at which to truncate mirrored frames. You can specify a value between 4 and 4088.

### Usage

`nv set system port-mirror session <session-id> span truncate size [options] (4-4088|none)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span truncate size 40
```

## nv set system port-mirror session \<session-id\> span enable

Turns port mirroring on or off.

### Usage

`nv set system port-mirror session <session-id> span enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span enable on
```

## nv set system port-mirror session \<session-id\> span direction

Configures the SPAN direction. You can specify ingress or egress.

### Usage

`nv set system port-mirror session <session-id> span direction [options] (ingress|egress)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span direction ingress
```

## nv set system port-mirror session \<session-id\> erspan

Configures Encapsulated Remote Switched Port Analyzer (ERSPAN).

### Usage

`nv set system port-mirror session <session-id> erspan [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `source-port` |  Configures the ERSPAN source port.|
| `destination` |  Configures the ERSPAN destination.|
| `truncate`  |    Configures truncation to decrease bandwidth by reducing the size of monitored packets. |
| `enable`    |    Turns ERSPAN on or off. |
| `direction`  |   Configures the direction of traffic through the source-port. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system port-mirror session \<session-id\> erspan source-port \<port-id\>

Configures the ERSPAN source port (switch ports or bonds only).

### Usage

`nv set system port-mirror session <session-id> erspan source-port <port-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>`   |  The interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan source-port swp1
```

## nv set system port-mirror session \<session-id\> erspan destination

Configures the ERSPAN destination.

### Usage

`nv set system port-mirror session <session-id> erspan destination [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `source-ip` | The source IP address from where to copy packets. |
| `dest-ip` |  The destination IP address to transmit packets. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system port-mirror session \<session-id\> erspan destination source-ip \<source-ip\>

Configures the source IP address from where to copy packets.

### Usage

`nv set system port-mirror session <session-id> erspan destination source-ip <source-ip> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan destination source-ip 10.10.10.1
```

## nv set system port-mirror session \<session-id\> erspan destination dest-ip \<dest-ip\>

Configures the destination IP address to which you want to transmit packets.

### Usage

`nv set system port-mirror session <session-id> erspan destination dest-ip <dest-ip> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan destination dest-ip 10.10.10.234
```

## nv set system port-mirror session \<session-id\> erspan truncate

Configures truncation to decrease bandwidth by reducing the size of monitored packets.

### Usage

`nv set system port-mirror session <session-id> erspan truncate [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` | Turns truncation on or off.|
| `size` |   Truncates the mirrored frames at the specified number of bytes. The truncate size must be between 4 and 4088 bytes and a multiple of 4.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system port-mirror session <session-id> erspan truncate enable

Turns truncation on or off.

### Usage

`nv set system port-mirror session <session-id> erspan truncate enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan truncate enable on
```

## nv set system port-mirror session \<session-id\> erspan truncate size

Configures the size in bytes at which to truncate mirrored frames. You can specify a value between 4 and 4088.

### Usage

`nv set system port-mirror session <session-id> erspan truncate size [options] (4-4088|none)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan truncate size 4000
```

## nv set system port-mirror session \<session-id\> erspan enable

Turns ERSPAN on or off.

### Usage

`nv set system port-mirror session <session-id> erspan enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan enable on
```

## nv set system port-mirror session \<session-id\> erspan direction

Configures the ERSPAN direction. You can specify ingress or egress.

### Usage

`nv set system port-mirror session <session-id> erspan direction [options] (ingress|egress)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 direction ingress
```

## nv set system config

Sets how you want to perform configuration operations.

### Usage

`nv set system config [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `apply`   | Sets how to apply configurations.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system config apply

Sets how to apply configurations.

### Usage

`nv set system config apply [options] [<attribute> ...]`

### Default Setting

N/A

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ignore` |  Configures NVUE to ignore certain underlying Linux files when applying configuration changes.|
| `overwrite` | Sets which files you can overwrite when you apply configuration changes. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set system config apply ignore \<ignore-id\>

Configures NVUE to ignore certain underlying Linux files when applying configuration changes.

### Usage

`nv set system config apply ignore <ignore-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<ignore-id>` |  The file to ignore |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system config apply ignore /etc/ptp4l.conf
```

## nv set system config apply overwrite

Sets which files you can overwrite when applying configuration changes. You can specify `all` or `controlled`. Specify `all` to overwrite all files. If the file is locally modified, you see a warning and you can stop the apply before the local modifications are overwritten. Specify `controlled"` to overwrite only files that NVUE most recently changed. If the file is locally modified, you see a warning, but the file is not overwritten.

### Usage

`nv set system config apply overwrite [options] (all|controlled)`

### Default Setting

`all`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system config apply overwrite controlled
```

## nv set system hostname \<hostname\>

Configures a static hostname for the switch. The hostname identifies the switch; make sure you configure the hostname to be unique and descriptive.

### Usage

`nv set system hostname [options] <idn-hostname>`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system hostname leaf01
```

## nv set system timezone

Configures the time zone on the switch to be the time zone for your location.

### Usage

`nv set system timezone [options]`

### Default Setting

UTC

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system timezone US/Eastern
```

## nv set vrf \<vrf-id\>

Configures Virtual routing and forwarding (VRF). Multiple instances of a routing table can exist in a virtual router and work simultaneously.

### Usage

`nv set vrf <vrf-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `loopback`  |  Configures the loopback interface associated with this VRF.|
| `evpn`  | Configures Ethernet VPN (EVPN) control plane settings for the VRF.|
| `router` |  Configures router settings for the VRF. |
| `ptp` |   Configures PTP on all interfaces in this VRF.|
| `table` | Configures the routing table number.  between 1001-1255, used by the named VRF. If auto, the default, it will be auto generated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> loopback

Configures the loopback interface associated with this VRF.

### Usage

`nv set vrf <vrf-id> loopback [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ip` |  Configures properties associated with the loopback IP address on this VRF.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> loopback ip

The IP address associated with the loopback interface on this VRF. You can specify more than one IP address.

### Usage

`nv set vrf <vrf-id> loopback ip [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address`  |  Configures the static IPv4 or IPv6 address of the loopback interface on the VRF.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> loopback ip address \<ip-prefix-id\>

Configures the static IPv4 or IPv6 address of the loopback interface on the VRF.

### Usage

`nv set vrf <vrf-id> loopback ip address <ip-prefix-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF you want to configure.|
| `<ip-prefix-id>`  | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default loopback ip address 10.10.10.1/32
```

## nv set vrf \<vrf-id\> evpn

Configures Ethernet VPN (EVPN) control plane settings for the VRF.

### Usage

`nv set vrf <vrf-id> evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `vni`   |  Configures the layer 3 VNI. |
| `enable`  |  Turns EVPN on or off on this VRF. |
| `vlan`  |  Configures the VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> evpn vni \<vni-id\>

Configures the layer 3 VNI.

### Usage

`nv set vrf <vrf-id> evpn vni <vni-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<vni-id>` |  The VXLAN ID. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `prefix-routes-only` |  Configures the associated layer 3 VNI and corresponding route targets with EVPN type-5 routes only, not with EVPN type-2 routes.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default evpn vni 4001
```

## nv set vrf \<vrf-id\> evpn vni \<vni-id\> prefix-routes-only

Configures the associated layer 3 VNI and corresponding route targets with EVPN type-5 routes only, not with EVPN type-2 routes.

### Usage

`nv set vrf <vrf-id> evpn vni <vni-id> prefix-routes-only [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<vni-id>` |  The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default evpn vni 4001 prefix-routes-only on
```

## nv set vrf \<vrf-id\> evpn enable

Turns EVPN on or off for this VRF.

### Usage

`nv set vrf <vrf-id> evpn enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default evpn enable on
```

## nv set vrf \<vrf-id\> evpn vlan

Configures the VLAN ID. You can specify `auto` or a value between 1 and 4094.

### Usage

`nv set vrf <vrf-id> evpn vlan [options] 1-4094|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default evpn vlan 20
```

## nv set vrf \<vrf-id\> router

Configures routing for a VRF.

### Usage

`nv set vrf <vrf-id> router [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rib` |  Configures the routing  table for this VRF.|
| `bgp`  |  Configures BGP in this VRF.|
| `static` |  Configures static routes in this VRF.|
| `pim` | Configures PIM in this VRF.|
| `ospf` |  Configures OSPF in this VRF.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router rib \<afi\>

Configures the routing table for this VRF.

### Usage

`nv set vrf <vrf-id> router rib <afi> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `protocol`  | Configures the import protocols from the Routing Information Base (RIB) to the Forwarding Information Base (FIB). |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\>

Configures the switch to import protocols from where routes are known.

### Usage

`nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<afi>`   |  The route address family. |
| `<import-protocol-id>` |  The import protocol list. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `fib-filter` |  Configures a route map to apply on the routes of the import protocol. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\> fib-filter (none|\<instance-name\>)

Configures a route map to apply on the routes of the import protocol.

### Usage

`nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id> fib-filter [options] (none|<instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
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

## nv set vrf \<vrf-id\> router bgp

Configures BGP on the VRF.

### Usage

`nv set vrf <vrf-id> router bgp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address-family`     | Configures the address family in this VRF.|
| `path-selection`     | Configures BGP path-selection in this VRF. |
| `route-reflection`   | Configures BGP route-reflection in this VRF.|
| `peer-group`         | Configures BGP peers  in this VRF.|
| `route-export`       | Configures IPv4 and IPv6 route export from this VRF. |
| `route-import`       | Configures IPv4 and IPv6 routes import from this VRF |
| `timers`             | Configures timer values for all BGP peers in this VRF. |
| `confederation`      | Configures BGP confederation options in this VRF. |
| `neighbor`           | Configures BGP neighbors (peers) in this VRF. |
| `enable`             | Turns BGP on or off in this VRF. |
| `autonomous-system`  | Configures the ASN for this VRF. If "auto", inherit from the global config. |
| `dynamic-peer-limit` | Configures the maximum number of dynamic neighbors from which you can accept a connection. Applicable only if you configure dynamic- peering subnet ranges.|
| `rd`                 | Configures the BGP Route Distinguisher to use when routes in this VRF have to be exported.|
| `router-id`          | Configures the BGP router ID for this VRF. If "auto", inherit from the global config. This is the default. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family

Configures the address family in this VRF.

### Usage

`nv set vrf <vrf-id> router bgp address-family [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`ipv4-unicast` | Configures the IPv4 unicast address family.|
|`l2vpn-evpn`   | Configures the layer 2 VPN EVPN address family.|
|`ipv6-unicast` | Configures the IPv6 unicast address family.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast

Configures the IPv4 unicast address family.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `redistribute`     | Configures route redistribution. |
| `aggregate-route`  | Configures IPv4 aggregate routes. |
| `network`          | Configures IPv4 static networks. |
| `route-import`     | Configures route import. |
| `multipaths`       | Configures multipaths. |
| `admin-distance`   | Configures admin distances. |
| `route-export`     | Configures route export |
| `rib-filter`       | Configures filtering policies to apply before installing the route into the zebra RIB.|
| `enable`           | Turns BGP address-family ipv4-unicast on or off.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute

Configures route redistribution, which allows a network to use a routing protocol to route traffic dynamically based on the information learned from a different routing protocol or from static routes. Route redistribution helps increase accessibility within networks.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `static`      | Configures route redistribution of IPv4 static routes. |
| `connected`   | Configures route redistribution of IPv4 connected routes. |
| `kernel`      | Configures route redistribution of IPv4 kernel routes. |
| `ospf`        | Configures route redistribution of IPv4 OSPF routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static

Configures route redistribution of IPv4 static routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turns route redistribution of IPv4 static routes on or off.|
| `metric`      | Configures the metric to use for the redistributed route. |
| `route-map`   | Sets the route map to apply to the redistributed route. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static enable

Turns route redistribution of IPv4 static routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute static enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static metric

Configures the metric you want to use for the redistributed route. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route. 

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static metric [options] (0-4294967295|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute static metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static route-map

Sets the route map to apply to the redistributed route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute static route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected

Configures route redistribution of IPv4 connected routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`     | Turns route redistribution of IPv4 connected routes on or off. |
| `metric`     | Configures the metric to use for the redistributed connected route.|
| `route-map`   | Sets the route map to apply to the redistributed connected route.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected enable

Turns route redistribution of IPv4 connected routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected metric

Configures the metric you want to use for the redistributed connected route. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route. 

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected metric [options] (0-4294967295|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected route-map

Sets the route map to apply to the redistributed connected route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel

Configures redistribution of IPv4 kernel routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turns redistribution of IPv4 kernel routes on or off. |
| `metric`      | Configures the metric to use for the redistributed kernel route. |
| `route-map`   | Sets the route map to apply to the redistributed kernelroute.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel enable

Turns redistribution of kernel routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute kernel enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel metric

Configures the metric you want to use for the redistributed kernel route. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route. 

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options] (0-4294967295|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute kernel metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel route-map

Sets the route map to apply to the redistributed route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute kernel route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf

Configures redistribution of IPv4 OSPF routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turns IPv4 OSPF route distribution on or off. |
| `metric`      | Configures the metric to use for the redistributed route. |
| `route-map`   | Sets the route map to apply to the redistributed route.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf enable

Turns redistribution of OSPF routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute ospf enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf metric

Configures the metric you want to use for the redistributed ospf routes. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route. 

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options] (0-4294967295|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute ospf metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf route-map

Sets the route map to apply to the redistributed route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute ospf route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\>

Configures route aggregation to minimize the size of the routing table and save bandwidth. You can aggregate a range of networks in your routing table into a single prefix.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `as-set`                | Turns generation of an AS_SET for the aggregate on or off.|
| `route-map`             | Sets the optional policy to modify attributes.|
| `summary-only`          | Turns on or off suppression of longer prefixes inside the aggregate address before sending updates.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only

Ensures that BGP suppresses longer prefixes inside the aggregate address before sending updates.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 summary-only on
```

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set

Turns generation of an AS_SET for the aggregate on or off. When `on`, BGP creates an aggregate address with a mathematical set of autonomous systems. The AS_SET option summarizes the AS_PATH attributes of all the individual routes to help BGP detect and avoid loops.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 as-set on
```

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> route-map 

Applies a route map to the aggregate route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\>

Configures the prefixes to originate from a BGP node.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-network-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map` |  Applies a route map to the prefixes that originate from a BGP node. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
```

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map

Applies a route map to the prefixes that originate from a BGP node.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-network-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32 route-map HI-PRIO
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import

Configures route leaking, where a destination VRF wants to know the routes of a source VRF. As routes come and go in the source VRF, they dynamically leak to the destination VRF through BGP.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `from-vrf` |   Configures the VRF from which route leaking occurs for this address-family. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf

Configures the VRF from which route leaking occurs for the IPv4 ddress family.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `list`        | Configures the VRF from which to import routes. |
| `enable`      | Turns route leaking on or off.  |
| `route-map`   | Applies a route map to control importing routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\>

Configures the VRF from which to import routes.You can specify multiple VRFs.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<leak-vrf-id>`  | The VRF from which you want to leak routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf list BLUE
```

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf enable (on|off)

Turns route leaking on or off for the IPv4 ddress family.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf route-map \<instance-name\>

Applies a route map to control importing routes. For example, to exclude certain prefixes from the import process, configure the prefixes in a route map.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf route-map BLUEtoRED
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths

Configures the maximum number of equal-cost BGP paths allowed. The BGP multipath option is on by default and the maximum number of paths is 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs. 1 disables the BGP multipath option.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options] [<attribute> ...]`

### Default Setting

64

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `compare-cluster-length` | If on and IBGP paths have a cluster list, their lengths must be equal to be selected as multipaths. |
| `ebgp`  |  Configures the number of equal-cost EBGP paths allowed. |
| `ibgp` | Configures the number of equal-cost IBGP paths allowed. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths ebgp

Configures the number of equal-cost EBGP paths allowed.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp [options] 1-128`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast multipaths ebgp 120
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths ibgp

Configures the number of equal-cost IBGP paths allowed.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp [options] 1-128`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast multipaths ibgp 120
```

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length

Turns on cluster length comparison. When `on` and IBGP paths have a cluster list, their lengths must be equal to be selected as multipaths.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast compare-cluster-length on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance

Configures the BGP administrative distance so that the switch can choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPF with an administrative distance of 110 and the same route from BGP with an administrative distance of 100, the switch chooses BGP.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|  `external`   | Configures the distance to apply to routes from EBGP peers when installed into the RIB.|
|  `internal`   | Configures the distance to apply to routes from IBGP peers when installed into the RIB.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance external

Configures the distance to apply to routes from EBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance external 150
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance internal

Configures the distance to apply to routes from IBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance internal 110
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export

Configures route export settings.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `to-evpn` |   Configures exporting routes from this VRF for this address-family into EVPN as type-5 routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn

Configures prefix-based routing using EVPN type-5 routes. Type-5 routes (or prefix routes) primarily route to destinations outside of the data center fabric. EVPN prefix routes carry the layer 3 VNI and router MAC address and follow the symmetric routing model to route to the destination prefix.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` | Turns prefix-based routing using EVPN type-5 routes on or off.|
| `default-route-origination` | Configures default route origination. |
| `route-map`  | Sets the route map to control the export of routes into EVPN. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn enable

Turns prefix-based routing using EVPN type-5 routes on or off. When `on`, the switch can announce IP prefixes in the BGP RIB as EVPN type-5 routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn route-map

Sets the route map to control the export of routes into EVPN. By default, when announcing IP prefixes in the BGP RIB as EVPN type-5 routes, the switch selects all routes in the BGP RIB to advertise as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn route-map HIGH-PRIO
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination

 Configures originating EVPN default type-5 routes. The default type-5 route originates from a border (exit) leaf and advertises to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod).

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn default-route-origination on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast rib-filter

Applies a route map on route updates from BGP to the Route Information Base (RIB). You can match on prefix, next hop, communities, and so on. You can set the metric and next hop only. Route maps do not affect the BGP internal RIB. Route maps work on multi-paths; however, BGP bases the metric setting on the best path only.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast rib-filter  [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast rib-filter routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast enable

Tuns the BGP IPv4 address family on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv4-unicast enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
```

## nv set vrf \<vrf-id\> router bgp address-family l2vpn-evpn

Configures the L2VPN-EVPN address family.

### Usage

`nv set vrf <vrf-id> router bgp address-family l2vpn-evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

| Attribute |  Description   |
| ---------  | -------------- |
| `enable` |   Turns the L2VPN-EVPN address family on or off for the VRF. |


### Version History

Introduced in Cumulus Linux 5.0.0


## nv set vrf \<vrf-id\> router bgp address-family l2vpn-evpn enable

Tuns the L2VPN-EVPN address family on or off for the VRF.

### Usage

`nv set vrf <vrf-id> router bgp address-family l2vpn-evpn enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast

Configures the IPv6 unicast address family.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aggregate-route`  | Configures IPv6 aggregate routes.|
| `network`          | Configures IPv6 static networks.|
| `route-import`     | Configures route import.|
| `multipaths`       | Configures multipaths|
| `admin-distance`   | Configures the administrative distance for internal and external routes.|
| `route-export`     | Configures route export. |
| `redistribute`     | Configures route redistribution. |
| `rib-filter`       | Applies filtering policies before installing routes into the zebra RIB.|
| `enable`           | Turns the IPv6 unicast address family on or off. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\>

Configures an IPv6 aggregate route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `as-set`                | Turns generation of an AS_SET for the aggregate on or off.|
| `route-map`             | Sets the optional policy to modify attributes.|
| `summary-only`          | Turns on or off suppression of longer prefixes inside the aggregate address before sending updates.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\> summary-only (on|off)

Ensures that BGP suppresses longer IPv6 prefixes inside the aggregate address before sending updates.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> summary-only [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 summary-only on
```

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set

Turns generation of an AS_SET for the aggregate on or off. When `on`, BGP creates an aggregate address with a mathematical set of autonomous systems. The AS_SET option summarizes the AS_PATH attributes of all the individual routes to help BGP detect and avoid loops.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 as-set on
```

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> route-map 

Applies a route map to the aggregate route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast network \<static-network-id\>

Configures an IPv6 static network.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-network-id>`  | The IPv6 address and route prefix in CIDR notation.|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map` | Applies a route map to the prefixes that originate from a BGP node.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import

Configures route leaking, where a destination VRF wants to know the routes of a source VRF. As routes come and go in the source VRF, they dynamically leak to the destination VRF through BGP.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `from-vrf`  |  Configures VRF to VRF route leaking for this address-family.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf

Configures VRF to VRF route leaking for this address-family.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `list`        | Configures the VRF from which to import routes. |
| `enable`      | Turns route leaking on or off.  |
| `route-map`   | Applies a route map to control importing routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list

Configures the VRF from which to import routes. You can specify multiple VRFs.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf list BLUE
```

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf enable

Turns route leaking for IPv6 on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf route-map \<instance-name\>

Applies a route map to control importing routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf route-map BLUEtoRED
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths

Configures the maximum number of equal-cost BGP paths allowed. The BGP multipath option is on by default and the maximum number of paths is 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `compare-cluster-length` | If `on` and IBGP paths have a cluster list, their lengths must be equal to be selected as multipaths. |
| `ebgp`  |  Configures the number of equal-cost EBGP paths allowed. |
| `ibgp` | Configures the number of equal-cost IBGP paths allowed. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths ebgp

Configures the number of equal-cost EBGP paths allowed. You can specify a value between 1 and 128.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp [options] 1-128`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast multipaths ebgp 120
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths ibgp

Configures the number of equal-cost IBGP paths allowed. You can specify a value between 1 and 128.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp [options] 1-128`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast multipaths ibgp 120
```

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length

Turns on cluster length comparison. When `on` and IBGP paths have a cluster list, their lengths must be equal to be selected as multipaths.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast compare-cluster-length on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance

Configures the administrative distance for internal and external routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|  `external`   | Configures the distance to apply to routes from EBGP peers when installed into the RIB.|
|  `internal`   | Configures the distance to apply to routes from IBGP peers when installed into the RIB.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance external

Configures the distance to apply to routes from EBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast admin-distance external 150
```

## nv set vrf \<vrf-id>\ router bgp address-family ipv6-unicast admin-distance internal

Configures the distance to apply to routes from IBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal [options] 1-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast admin-distance internal 110
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export

Configures route export settings for IPv6.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `to-evpn`   |  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn

Configures exporting routes from this VRF for this address-family into EVPN as type-5 routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`     | Turns prefix-based routing using EVPN type-5 routes on or off. |
| `default-route-origination`  | Configures default route origination. |
| `route-map`   | Applies the route map to control the export of routes into EVPN. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn enable

Turns prefix-based routing using EVPN type-5 routes on or off. When `on`, the switch can announce IPv6 prefixes in the BGP RIB as EVPN type-5 routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn route-map

Applies the route map to control the export of routes into EVPN. By default, when announcing IPv6 prefixes in the BGP RIB as EVPN type-5 routes, the switch selects all routes in the BGP RIB to advertise as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn route-map HIGH-PRIO
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination

Configures originating EVPN default type-5 routes. The default type-5 route originates from a border (exit) leaf and advertises to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod).

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn default-route-origination on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute

Configures route redistribution, which allows a network to use a routing protocol to route traffic dynamically based on the information learned from a different routing protocol or from static routes. Route redistribution helps increase accessibility within networks.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `static`      | Configures route redistribution of IPv6 static routes. |
| `connected`   | Configures route redistribution of IPv6 connected routes. |
| `kernel`      | Configures route redistribution of IPv6 kernel routes. |
| `ospf6`       | Configures route redistribution of IPv6 OSPF routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static

Configures route redistribution of IPv6 static routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`       | Turns route redistribution of IPv6 static routes on or off.|
| `metric`       | Configures the metric to use for the redistributed route.|
| `route-map`    | Applies the route map to the redistributed route.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static enable

Turns route redistribution of IPv6 static routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static metric

Configures the metric you want to use for the redistributed route. You can specify auto or a value between 0 and 4294967295. If you specify auto, the switch choses an appropriate value based on the type of route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static metric [options] (0-4294967295|auto)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static route-map

Applies the route map to the redistributed route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected

Configures route redistribution of IPv6 connected routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turns route redistribution of IPv6 connected routes on or off.|
| `metric`      | Configures the metric to use for the redistributed connected route.|
| `route-map`   | Applies a route map to the redistributed connected route.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected enable

Turns route redistribution of IPv6 connected routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected metric

Configures the metric you want to use for the redistributed connected route. You can specify auto or a value between 0 and 4294967295. If you specify auto, the switch choses an appropriate value based on the type of route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected metric [options] (0-4294967295|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected route-map (none|<instance-name>)

Applies a route map to the redistributed connected route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected route-map [options] (none|<instance-name>)`

## Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel

Configures redistribution of IPv4 kernel routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turns redistribution of IPv4 kernel routes on or off.|
| `metric`      | Configures the metric to use for the redistributed kernel route.|
| `route-map`   | Applies a route map to the redistributed kernelroute. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel enable

Turns redistribution of kernel routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel enable[options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel metric

Configures the metric you want to use for the redistributed kernel route. You can specify auto or a value between 0 and 4294967295. If you specify auto, the switch choses an appropriate value based on the type of route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel metric [options] (0-4294967295|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel route-map

Applies a route map to the redistributed route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel route-map [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6

Configures redistribution of IPv6 OSPF routes.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turns IPv6 OSPF route distribution on or off. |
| `metric`      | Configures the metric to use for the redistributed route.|
| `route-map`   | Applies a route map to the redistributed route. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 enable

Turns redistribution of OSPF routes on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf enable on
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 metric (0-4294967295|auto)

Configures the metric you want to use for the redistributed OSPF routes. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 metric [options] (0-4294967295|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf metric 4294967295
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 route-map (none|<instance-name>)

Applies a route map to the redistributed route.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 route-map [options] (none|<instance-name>)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf route-map routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast rib-filter

Applies a route map on route updates from BGP to the Route Information Base (RIB). You can match on prefix, next hop, communities, and so on. You can set the metric and next hop only. Route maps do not affect the BGP internal RIB. Route maps work on multi-paths; however, BGP bases the metric setting on the best path only.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast rib-filter  [options] (none|<instance-name>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast rib-filter routemap1
```

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast enable (on|off)

Tuns the BGP IPv6 address family on or off.

### Usage

`nv set vrf <vrf-id> router bgp address-family ipv6-unicast enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast enable on
```

## nv set vrf \<vrf-id\> router bgp path-selection

Configures BGP best path selection.

### Usage

`nv set vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath`            | Configures BGP aspath path selection. |
| `med`               | BGP med path-selection config, applicable to this BGP instance |
| `multipath`         | BGP multipath path-selection config, applicable to this BGP instance routerid-compare  Path selection based on Router ID comparison. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp path-selection aspath

Configures how BGP selects the best path to an autonomous system (AS).

### Usage

`nv set vrf <vrf-id> router bgp path-selection aspath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `compare-confed`   | Configures BGP to select the AS based on confederations. |
| `compare-lengths`  | Configures BGP to select the AS based on path length. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp path-selection aspath compare-lengths

Configures BGP to select the AS based on path length.

### Usage

`nv set vrf <vrf-id> router bgp path-selection aspath compare-lengths [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection aspath compare-lengths on
```

## nv set vrf \<vrf-id\> router bgp path-selection aspath compare-confed (on|off)

Configures BGP to select the AS based on confederations.

### Usage

`nv set vrf <vrf-id> router bgp path-selection aspath compare-confed [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection aspath compare-confed on
```

## nv set vrf \<vrf-id\> router bgp path-selection med

Configures BGP multi-exit discriminator (MED) path selection.

### Usage

`nv set vrf <vrf-id> router bgp path-selection med [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `compare-always`        | Configures BGP to always compare the MED on routes even when received from different neighbouring autonomous systems.|
| `compare-confed`        | Configures MED for route-selection based on confederations.|
| `compare-deterministic` | Applies route selection in a way that produces deterministic answers locally.|
| `missing-as-max`        | Configures MED missing-as-max. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp path-selection med compare-always

Configures BGP to always compare the MED on routes even when received from different neighbouring autonomous systems. When enabled, BGP compares MEDs for all paths.

### Usage

`nv set vrf <vrf-id> router bgp path-selection med compare-always [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection med compare-always on
```

## nv set vrf \<vrf-id\> router bgp path-selection med compare-deterministic

Applies route selection in a way that produces deterministic answers locally.

### Usage

`nv set vrf <vrf-id> router bgp path-selection med compare-deterministic [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection med compare-deterministic on
```

## nv set vrf \<vrf-id\> router bgp path-selection med compare-confed (on|off)

Configures MED for route-selection based on confederations.

### Usage

`nv set vrf <vrf-id> router bgp path-selection med compare-confed [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection med compare-confed on
```

## nv set vrf \<vrf-id\> router bgp path-selection med missing-as-max (on|off)

Configures MED missing-as-max.

### Usage

`nv set vrf <vrf-id> router bgp path-selection med missing-as-max [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection med missing-as-max on
```

## nv set vrf \<vrf-id\> router bgp path-selection multipath

Configures BGP multipath path selection.

### Usage

`nv set vrf <vrf-id> router bgp path-selection multipath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath-ignore`   | Configures BGP to ignore the AS path when determining multipath routing.|
| `bandwidth`       | Configures multipath route selection based on bandwidth.|
| `generate-asset`  | Configures BGP to generate ??? Requires `aspath-ignore` to be on.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp path-selection multipath aspath-ignore

Configures BGP to ignore the AS path when determining multipath routing.

### Usage

`nv set vrf <vrf-id> router bgp path-selection multipath aspath-ignore [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection multipath aspath-ignore on
```

## nv set vrf \<vrf-id\> router bgp path-selection multipath generate-asset (on|off)

?????

### Usage

`nv set vrf <vrf-id> router bgp path-selection multipath generate-asset [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection multipath generate-asset on
```

## nv set vrf \<vrf-id\> router bgp path-selection multipath bandwidth

Configures multipath route selection based on bandwidth. You can specify `bandwidth`, `all-paths`, `skip-missing`, `default-weight-for-missing`, or `ignore`.

### Usage

`nv set vrf <vrf-id> router bgp path-selection multipath bandwidth [options] (bandwidth|all-paths|skip-missing|default-weight-for-missing|ignore)`

### Default Setting

`ignore`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection multipath bandwidth all-paths
```

## nv set vrf \<vrf-id\> router bgp path-selection routerid-compare (on|off)

Configures BGP to use the router ID to decide the best path when two identical routes are received from two different peers.

### Usage

`nv set vrf <vrf-id> router bgp path-selection routerid-compare [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp path-selection routerid-compare on
```

## nv set vrf \<vrf-id\> router bgp route-reflection

Configures BGP route reflection. When you configure an iBGP speaker as a route reflector, it can send iBGP learned routes to other iBGP peers.

### Usage

`nv set vrf <vrf-id> router bgp route-reflection [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`                  | Turns BGP route reflection on or off. |
| `cluster-id`              | Configures the cluster ID to use during route reflection. This setting is required when route-reflection is on.|
| `outbound-policy`         | Allows outbound peer policy to modify the attributes for reflected routes. Typically, reflected routes have to retain their original attributes.|
| `reflect-between-clients` |  Allows routes to be reflected between clients.  Typically, routes are reflected only between clients and non-clients, with the clients of a route reflector expected to be fully meshed.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp route-reflection enable

Turns BGP route reflection on or off.

### Usage

`nv set vrf <vrf-id> router bgp route-reflection enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp route-reflection enable on
```

## nv set vrf \<vrf-id\> router bgp route-reflection cluster-id

Configures the cluster ID to use during route reflection. This setting is required when route-reflection is on.

### Usage

`nv set vrf <vrf-id> router bgp route-reflection cluster-id [options] (0-4294967295|<ipv4>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp route-reflection cluster-id 10
```

## nv set vrf \<vrf-id\> router bgp route-reflection reflect-between-clients

Allows routes to be reflected between clients. Typically, routes are reflected only between clients and non-clients, with the clients of a route reflector expected to be fully meshed.

### Usage

`nv set vrf <vrf-id> router bgp route-reflection reflect-between-clients [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp route-reflection reflect-between-clients on
```

## nv set vrf \<vrf-id\> router bgp route-reflection outbound-policy (on|off)

Allows an outbound peer policy to modify the attributes for reflected routes. Typically, reflected routes have to retain their original attributes.

### Usage

`nv set vrf <vrf-id> router bgp route-reflection outbound-policy [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp route-reflection outbound-policy on
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\>

Configures BGP peer groups settings.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `bfd`                   | Configures BFD for BGP sessions for the peer group.|
| `ttl-security`          | Configures the TTL security hop count for the peer group.|
| `capabilities`          | Configures advertisement of IPv4 prefixes with IPv6 next hops over global IPv6 peerings.|
| `graceful-restart`      | Configures graceful restart for the peer group.|
| `local-as`              | Configures the local AS for the peer group.|
| `timers`                | Configures timers for the peer group. |
| `address-family`        | Configures address family settings for the peer group.|
| `description`           | Configures a description for the peer group.|
| `enforce-first-as`      | If on, when BGP updates are received from EBGP peers, check that first AS matches peer's AS|
| `multihop-ttl`          | Configures the maximum number of hops allowed for the peer group. When 'auto', the type of peer will determine the appropriate value (255 for iBGP and 1 for eBGP). This is the default.|
| `nexthop-connected-check` | If 'on', it disables the check that a non-multihop EBGP peer should be directly connected and only announce connected next hops|
| `passive-mode`          | Turns passive mode on or off. If on, the peers in the peer group do not initiate the BGP connection but wait for  an incoming connection.|
| `password`              | Configures the password for the peer group.|
| `remote-as`             | Configures the remote ASN for the peer group. If you specify `external`, an EBGP configuration but the actual ASN is immaterial. If specified as 'internal', it means an IBGP configuration.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd

Configures Bidirectional Forwarding Detection (BFD) for BGP sessions for the peer group. When you configure BFD in BGP, PTM registers and de-registers neighbors dynamically.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`             | Turns BFD on or off for the peer group.|
| `detect-multiplier`  | Configures the BFD interval multiplier.|
| `min-rx-interval`    | Configures the minimum interval between received BFD control packets.|
| `min-tx-interval`    | Configures the minimum interval between sending BFD control packets.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd enable

Turns BFD on or off for the BGP peer group.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE bfd enable on
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd detect-multiplier

Configures the BFD interval multiplier. You can specify a value between 2 and 255.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier [options] 2-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE bfd detect-multiplier 4
```

## nv set vrf \<vrf-id\> router bgp peer-group <peer-group-id> bfd min-rx-interval

Configures the minimum interval between received BFD control packets. You can specify a value between 50 and 60000.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE bfd min-rx-interval 400
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd min-tx-interval

Configures the minimum interval between sending BFD control packets. You can specify a value between 50 and 60000.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE bfd min-tx-interval 400
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security

Configures the TTL security hop count for the peer group to prevent attacks against eBGP, such as denial of service (DoS) attacks. By default, BGP messages to eBGP neighbors have an IP time-to-live (TTL) of 1, which requires the peer to be directly connected, otherwise, the packets expire along the way. An attacker can adjust the TTL of packets so that they look like they originate from a directly connected peer. The BGP TTL security hops option inverts the direction in which BGP counts the TTL. Instead of accepting only packets with a TTL of 1, Cumulus Linux accepts BGP messages with a TTL greater than or equal to 255 minus the specified hop count.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`           | Turns BGP TTL security on or off.|
| `hops`             | Configures the number of hops to deduct from a TTL greater than or equal to 255. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security enable

Turns BGP TTL security on or off.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security enable [options] (on|off)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE ttl-security enable on 
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security hops

Configures the number of hops to deduct from a TTL greater than or equal to 255 to prevent attacks against eBGP, such as denial of service (DoS) attacks.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops [options] 1-254`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE ttl-security hops 200 
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities

Configures advertisement of IPv4 prefixes with IPv6 next hops over global IPv6 peerings.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|  `extended-nexthop`  | Turns extended the nexthop capability defined in RFC  5549 on or off.|
|  `source-address`    | Configures the source IP address of the TCP connection, which is often used as the BGP next hop for updates.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities extended-nexthop

Turns the extended next hop capability defined in RFC 5549 on or off. The extended nexthop is advertised to peers in the peer group. If you specify `auto`, extended next hop is `on` for unnumbered peers and `off` otherwise.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities extended-nexthop [options] (on|off|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE capabilities extended-nexthop on 
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities source-address

Configures the source IP address of the TCP connection, which is often used as the BGP next hop for updates.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities source-address [options] (<interface-name>|<ipv4>|<ipv6>)`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE capabilities source-address 10.10.10.1
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart

Configures graceful restart to minimize the negative effects that occur when BGP restarts. This option enables a BGP speaker to signal to its peers that it can preserve its forwarding state and continue data forwarding during a restart. It also enables a BGP speaker to continue to use routes announced by a peer even after the peer has gone down.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `mode`     | Configures the graceful restart mode.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart mode 

Configures the graceful restart mode. If you specify `auto`, the mode is inherited from the global setting. If you specify `off`, graceful restart is not negotiated with the peer group. If you specify `helper-only`, the switch is in a helper role only, where routes originated and advertised from a BGP peer in the peer group are not deleted. If you specify `full`, the switch is in both a helper and restarter role.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart mode [options] (auto|off|helper-only|full)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default bgp peer-group SPINE graceful-restart mode helper-only
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as

Configures the local AS for the peer group.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`enable`    | Turns local AS on or off for the peer group.|
|`asn`        | Configures the ASN you want to use to establish the peering if different from the ASN of the BGP instance. The local AS configured is also attached to incoming and outgoing updates.|
|`prepend`   | Configures BGP to prepend the configured local AS to updates.|
|`replace`    | Configures BGP to either attach only the configured local AS to generated updates or attach the ASN of the BGP instance, then prepend it with the configured local AS. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as enable

 Turns local AS on or off for the peer group.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as enable [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as enable on
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as asn

Configures the ASN you want to use to establish the peering if it is different from the ASN of the BGP instance. The local AS configured is also attached to incoming and outgoing updates.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as asn ????
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as prepend

Configures BGP to prepend the configured local AS to updates.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as prepend [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as enable on
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as replace

Configures BGP to either attach only the configured local AS to generated updates or attach the ASN of the BGP instance, then prepend it with the configured local AS.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as replace [options] (on|off)`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as replace on
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers

Configures BGP timers for the peer group.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `connection-retry`     | Configures the time interval at which the BGP process attempts to connect to a peer after a failure.|
| `hold`                 | Configures the hold timer. If BGP does not receive a keepalive or update message from the peer within the hold time, it declares the peer down and withdraws all routes received by this peer from the local BGP table.|
| `keepalive`            | Configures interval at which BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning.|
| `route-advertisement`  | Configures the time between route advertisements (BGP updates). After making a new best path decision for a prefix, BGP can insert a delay before advertising the new results to a peer. This delay rate limits the amount of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers keepalive

Configures the interval at which BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning. You can specify a value between 1 and 65535. If you speciy `none`, keepalives are not sent. If you specify `auto`, the global value is used.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers keepalive [options] (1-65535|none|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers keepalive 10
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers hold

Configures the hold timer. If BGP does not receive a keepalive or update message from a peer in the peer group within the hold time, it declares the peer down and withdraws all routes received by this peer from the local BGP table. If `none`, keepalives from the peer are not tracked and the peering session does not experience a hold timeout. You can specify a value between 3 and 65535. If you specify `auto`, the global value is used.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers hold [options] (3-65535|none|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers hold 30
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers connection-retry

Configures the time interval at which BGP  attempts to connect to a peer after a failure. You can specify a value between 1 and 65535. If you specify `auto`, the global value is used.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers connection-retry [options] (1-65535|none|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers connection-retry 30
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers route-advertisement (1-600|none|auto)

Configures the time between route advertisements (BGP updates). After making a new best path decision for a prefix, BGP can insert a delay before advertising the new results to a peer. This delay rate limits the amount of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. You can specify a value between 1 and 65535. If you specify `none` route advertisements are delayed and batched. If you specify `auto`, the global value is used.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers route-advertisement [options] (1-600|none|auto)`

### Default Setting

`auto`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers route-advertisement 5
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family

Configures address family settings for the peer group.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ipv4-unicast`     | Configures the IPv4 unicast address family for the peer group. Always on, unless disabled globaly.|
| `ipv6-unicast`     | Configures the IPv6 unicast address family for the peer group.|
| `l2vpn-evpn`       | Configures the l2vpn EVPN address family for the peer group.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast

Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `community-advertise`   | Community advertise for address family.|
| `attribute-mode`        | Attribute mod for address family.|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family|
| `prefix-limits`         | Limits on prefix from the peer for this address-family|
| `default-route-origination`  | Default route origination|
| `policy`                | Policies for ipv4 unicast|
| `conditional-advertise` | Conditional advertise for address family.|
| `enable`                | Turn the feature 'on' or 'off'. The default is 'on'.|
| `add-path-tx`           | Used to enable transmission of additional paths; by default, only the best path is announced to peers|
| `nexthop-setting`       | Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.|
| `route-reflector-client` | Specifies if this peer is a client and we are its route reflector|
| `route-server-client`   | Specifies if this peer is a client and we are its route server|
| `soft-reconfiguration`  | If 'on', it means that received routes from this peer  that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.|
| `weight`                | Weight applied to routes received from peer; this is used in the BGP route selection algorithm|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise

Community advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `extended`         | If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `large`            | If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `regular`          | If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath`           | If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.|
| `med`              | If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.|
| `nexthop`          | If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `allow-my-asn`     | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|
| `private-as`       | If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.|
| `replace-peer-as`  | If on, if the AS_PATH in an outgoing Update contains the  peer's ASN, it is replaced with the local system's ASN|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`           | Turn the feature 'on' or 'off'. The default is 'off'.|
| `occurrences`      | Indicates max number of occurrences of the local system's AS number in the received AS_PATH|
| `origin`           | If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn occurrences

Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound`   | Limits on inbound prefix from the peer for this address-family|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `maximum`            | Limit on number of prefixes of specific address-family that can be received from the peer. By default, there is no limit|
| `reestablish-wait`   | Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing. This would typically be 2-3 seconds.|
| `warning-only`       | If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.|
| `warning-threshold`  | Percentage of the maximum at which a warning syslog is generated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound warning-threshold

Percentage of the maximum at which a warning syslog is generated.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options] 1-100`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound reestablish-wait

Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast default-route-origination

Default route origination

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`   |Turn the feature 'on' or 'off'. The default is 'off'.|
| `policy`   |Optional route-map policy to control the conditions under which the default route is originated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy

Policies for ipv4 unicast

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound`          | Outbound unicast policy|
| `outbound`         | Outbound unicast policy|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`        | Route map to apply to Updates received from this peer|
| `aspath-list`      | AS-Path filter list to apply to Updates received from this peer|
| `prefix-list`      | Prefix list to apply to Updates received from this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound aspath-list none

AS-Path filter list to apply to Updates received from this peer

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`        | Route map to apply to Updates to be sent to this peer|
| `unsuppress-map`   | Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.|
| `aspath-list`      | AS-Path filter list to apply to Updates sent to this peer|
| `prefix-list`      | Prefix list to apply to Updates to be sent to this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound aspath-list none

S-Path filter list to apply to Updates sent to this peer

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`           | Turn the feature 'on' or 'off'. The default is 'off'.|
| `advertise-map`    | route-map contains prefix-list which has list of routes/prefixes to operate on.|
| `exist-map`        | route-map contains the conditional routes/prefixes in prefix-list.|
| `non-exist-map`    | route-map contains the negative conditional routes/prefixes in prefix-list.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise advertise-map \<instance-name\>

route-map contains prefix-list which has list of routes/prefixes to operate on.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise exist-map \<instance-name\>

route-map contains the conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise non-exist-map \<instance-name\>

route-map contains the negative conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast weight

Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight [options] 0-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast

Peer IPv6 unicast address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `policy`                | Policies for ipv4 unicast|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family|
| `prefix-limits`         | Limits on prefix from the peer for this address-family|
| `default-route-origination`  | Default route origination|
| `community-advertise`   | Community advertise for address family.|
| `attribute-mode`         |Attribute mod for address family.|
| `conditional-advertise` |Conditional advertise for address family.|
| `enable`               | Turn the feature 'on' or 'off'. The default is 'off'.|
| `add-path-tx`           | Used to enable transmission of additional paths; by default, only the best path is announced to peers|
| `nexthop-setting`       | Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This  is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes. "force" sets the next hop to ourselves for route  advertisement including for reflected routes.|
| `route-reflector-client`|  Specifies if this peer is a client and we are its route reflector|
| `route-server-client`   | Specifies if this peer is a client and we are its route server|
| `soft-reconfiguration`  | If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.|
| `weight`                | Weight applied to routes received from peer; this is used in the BGP route selection algorithm|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy

Policies for ipv6 unicast

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound`          | Outbound unicast policy|
| `outbound`         | Outbound unicast policy|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`        | Route map to apply to Updates received from this peer|
| `aspath-list`      | AS-Path filter list to apply to Updates received from this peer|
| `prefix-list`      | Prefix list to apply to Updates received from this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound aspath-list none

AS-Path filter list to apply to Updates received from this peer

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| route-map        | Route map to apply to Updates to be sent to this peer
| unsuppress-map   | Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.
| aspath-list      | AS-Path filter list to apply to Updates sent to this peer
| prefix-list      | Prefix list to apply to Updates to be sent to this peer

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound aspath-list none

AS-Path filter list to apply to Updates sent to this peer

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `allow-my-asn`     | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|
| `private-as`       | If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.|
| `replace-peer-as`  | If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`           | Turn the feature 'on' or 'off'. The default is 'off'.|
| `occurrences`      | Indicates max number of occurrences of the local system's AS number in the received AS_PATH|
| `origin`           | If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn occurrences

Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound` |  Limits on inbound prefix from the peer for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `maximum`            | Limit on number of prefixes of specific address-family that can be received from the peer. By default, there is no limit|
| `reestablish-wait`   | Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing. This would typically be 2-3 seconds.|
| `warning-only`       | If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.|
| `warning-threshold`  | Percentage of the maximum at which a warning syslog is generated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound warning-threshold

Percentage of the maximum at which a warning syslog is generated.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options] 1-100`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound reestablish-wait

Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination

Default route origination

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`           | Turn the feature 'on' or 'off'. The default is 'off'.|
| `policy`           | Optional route-map policy to control the conditions under which the default route is originated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise

Community advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `extended`         | If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `large`            | If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `regular`          | If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath`           | If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.|
| `med`              | If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.|
| `nexthop`          | If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`           | Turn the feature 'on' or 'off'. The default is 'off'.|
| `advertise-map`    | route-map contains prefix-list which has list of routes/prefixes to operate on.|
| `exist-map`        | route-map contains the conditional routes/prefixes in prefix-list.|
| `non-exist-map`    | route-map contains the negative conditional routes/prefixes in prefix-list.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise advertise-map \<instance-name\>

route-map contains prefix-list which has list of routes/prefixes to operate on.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise exist-map \<instance-name\>

route-map contains the conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise non-exist-map \<instance-name\>

route-map contains the negative conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast weight

Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight [options] 0-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn

Peer l2vpn EVPN address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]`


### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `attribute-mod`         | Attribute mod for address family.|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family|
| `policy`                | Policies for l2vpn evpn|
| `enable`                | Turn the feature 'on' or 'off'. The default is 'off'.|
| `add-path-tx`           | Used to enable transmission of additional paths; by default, only the best path is announced to peers|
| `nexthop-setting`       | Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes. "force" sets the next hop to ourselves for route  advertisement including for reflected routes.|
| `route-reflector-client`  | Specifies if this peer is a client and we are it route reflector|
| `route-server-client`   | Specifies if this peer is a client and we are its route server|
| `soft-reconfiguration`  | If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod

Attribute mod for address family.

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath`           | If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.|
| `med`              | If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.|
| `nexthop`          | If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `allow-my-asn`     | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|
| `private-as`       | If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.|
| `replace-peer-as`  | If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`           |Turn the feature 'on' or 'off'. The default is 'off'.|
| `occurrences`      |Indicates max number of occurrences of the local system's AS number in the received AS_PATH|
| `origin`           |If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn occurrences

Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy

Policies for l2vpn evpn

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound`          | Inbound l2vpn-evpn policy|
| `outbound`         | Outbound l2vpn-evpn policy|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound

Inbound l2vpn-evpn policy

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`route-map`  | Route map to apply to Updates received from this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound

Outbound l2vpn-evpn policy

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`        | Route map to apply to Updates to be sent to this peer|
| `unsuppress-map`   | Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> password none

Password

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> password [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> description none

neighbor description

### Usage

`nv set vrf <vrf-id> router bgp peer-group <peer-group-id> description [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp route-export

Controls for exporting ipv4 and ipv6 routes from this VRF

### Usage

`nv set vrf <vrf-id> router bgp route-export [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `to-evpn`   | Controls for exporting routes from this VRF into EVPN |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp route-export to-evpn

Controls for exporting routes from this VRF into EVPN

### Usage

`nv set vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-target`  | List the RTs to attach to host or prefix routes when exporting them into EVPN or "auto". If "auto", the RT will be derived. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\>

A route target identifier

### Usage

`nv set vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rt-id>`   | Route targets or "auto"|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp route-import

Controls for importing of ipv4 and ipv6 routes from this VRF

### Usage

`nv set vrf <vrf-id> router bgp route-import [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `from-evpn` |  Controls for importing EVPN type-2 and type-5 routes into this VRF|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp route-import from-evpn

Controls for importing EVPN type-2 and type-5 routes into this VRF

### Usage

`nv set vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-target`  | List the RTs to attach to host or prefix routes when importing them into VRF or "auto". If "auto", the RT will be derived. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\>

A route target identifier

### Usage

`nv set vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rt-id>`   |  Route targets or "auto"|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp timers

timer values for all peers in this VRF

### Usage

`nv set vrf <vrf-id> router bgp timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `conditional-advertise` | Time interval at which bgp table is scanned for condition is met.|
| `connection-retry`      | Time interval at which connection attempts are retried upon a failure.|
| `hold`                  | Hold timer. If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout.|
| `keepalive`             | Keepalive timer. If `none`, keepalives are not sent.|
| `route-advertisement`   | Time between route advertisements (BGP Updates). If not `none`, route advertisements to be delayed and batched.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp timers connection-retry

Time interval at which connection attempts are retried upon a failure.

### Usage

`nv set vrf <vrf-id> router bgp timers connection-retry [options] 1-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp confederation

BGP Confederation options.

### Usage

`nv set vrf <vrf-id> router bgp confederation [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `member-as`   | Confederation ASNs of the peers, maps to BGP confederation peers|
| `id`          | Confederation ASN, maps to BGP confederation id|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp confederation member-as

Set of autonomous numbers

### Usage

`nv set vrf <vrf-id> router bgp confederation member-as [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\>

BGP global configuration.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `bfd`                   | Specifies whether to track BGP peering sessions using this configuration via BFD.|
| `capabilities`          | Capabilities|
| `local-as`              | Local AS feature|
| `graceful-restart`      | BGP Graceful restart per neighbor configuration|
| `ttl-security`          | RFC 5082|
| `address-family`        | Address family specific configuration|
| `timers`                | Peer peer-timerss|
| `description`           | neighbor description|
| `enforce-first-as`      | If on, when BGP updates are received from EBGP peers with this config, check that first AS matches peer's AS|
| `multihop-ttl`          | Maximum hops allowed. When 'auto', the type of peer will determine the appropriate value (255 for iBGP and 1 for eBGP). This is the default.|
| `nexthop-connected-check` | If 'on', it disables the check that a non-multihopmEBGP peer should be directly connected and only announce connected next hops|
| `passive-mode`          | If enabled, do not initiate the BGP connection but wait for incoming connection|
| `password`              | Password|
| `enable`                | Turn the feature 'on' or 'off'. The default is 'on'.|
| `peer-group`            | Optional peer-group to which the peer is attached to inherit the group's configuration.|
| `remote-as`             | ASN for the BGP neighbor(s) using this configuration. If specified as 'external', it means an EBGP configuration but the actual ASN is immaterial. If specified as 'internal', it means an IBGP configuration.|
| `type`                  | The type of peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd

Specifies whether to track BGP peering sessions using this configuration via BFD.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`             | `Turn the feature 'on' or 'off'. The default is 'off'.|
| `detect-multiplier`  | `Detect multiplier|
| `min-rx-interval`    | `Minimum receive interval|
| `min-tx-interval`    | `Minimum transmit interval. The actual value used is the smaller of this or what the peer expects.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd detect-multiplier

Detect multiplier

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier [options] 2-255`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd min-rx-interval

Minimum receive interval

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd min-tx-interval

Minimum transmit interval.  The actual value used is the smaller of this or what the peer expects.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval [options] 50-60000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities

Capabilities

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `extended-nexthop`  | If 'on', the extended-nexthop capability defined in RFC 5549 is advertised to peer(s) with this config. If 'auto', it will be 'on' for unnumbered peers and 'off' otherwise. This is the default.|
| `source-address`    | source IP address of the TCP connection, which is often used as the BGP next hop for Updates|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as

Local AS feature

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `asn`            | ASN to use to establish the peering if different from the ASN of the BGP instance. This configuration finds use during AS renumbering. The local-as configured is also attached to incoming and outgoing updates.|
| `prepend`        | When set to 'off', do not prepend the configured local-as to received updates; otherwise, prepend it.|
| `replace`        | When set to 'on', attach only the configured local-as to generated updates, effectively "replacing" the AS number configured for the BGP instance with the local-as applicable for the peering; otherwise, attach the AS number of the BGP instance and then prepend it with the configured local-as.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as asn

ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart

BGP Graceful restart per neighbor configuration

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `mode`   | If 'auto', inherit from global. This is the default. If set to 'off', GR capability is not negotiated with this peer. If set to 'helper-only', only the Helper role is supported for this peer. This means that the GR capability will be negotiated without any address-families with this peer. If  set to 'full', both the Helper role and the Restarter role are supported with this peer; the GR capability will be negotiated with the enabled address-families for which GR is also supported.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security

RFC 5082

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `hops`           | Number of hops|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security hops

Number of hops

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops [options] 1-254`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family

Address family specific configuration

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ipv4-unicast`   | Peer IPv4 unicast address family. Always on, unless disabled globaly.|
| `ipv6-unicast`   | Peer IPv6 unicast address family.|
| `l2vpn-evpn`     | Peer l2vpn EVPN address family.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast

Peer IPv4 unicast address family.  Always on, unless disabled globally.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `attribute-mod`         | Attribute mod for address family.|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family|
| `policy`                | Policies for ipv4 unicast|
| `prefix-limits`         | Limits on prefix from the peer for this address-family|
| `default-route-origination` | Default route origination|
| `community-advertise`   | Community advertise for address family.|
| `conditional-advertise` | Conditional advertise for address family.|
| `enable`                | Turn the feature 'on' or 'off'. The default is 'on'.|
| `add-path-tx`           | Used to enable transmission of additional paths; by default, only the best path is announced to peers|
| `nexthop-setting`      | Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselvesfor route advertisement, except for reflected routes. "force" sets the next hop to ourselves for route advertisement including for reflected routes.|
| `route-reflector-client` | Specifies if this peer is a client and we are its route reflector|
| `route-server-client`   | Specifies if this peer is a client and we are its route server|
| `soft-reconfiguration`  | If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.|
| `weight`                | Weight applied to routes received from peer; this is  used in the BGP route selection algorithm|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath`         | If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.|
| `med`            | If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.|
| `nexthop`        | If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `allow-my-asn`     | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|
| `private-as`       | If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.|
| `replace-peer-as`  | If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `occurrences`    | Indicates max number of occurrences of the local system's AS number in the received AS_PATH|
| `origin`         | If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn occurrences

Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy

Policies for ipv4 unicast


### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound`        | Outbound unicast policy|
| `outbound`       | Outbound unicast policy|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`      | Route map to apply to Updates received from this peer|
| `aspath-list`    | AS-Path filter list to apply to Updates received from this peer|
| `prefix-list`    | Prefix list to apply to Updates received from this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound aspath-list none

AS-Path filter list to apply to Updates received from this peer

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`      | Route map to apply to Updates to be sent to this peer|
| `unsuppress-map` | Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.|
| `aspath-list` | AS-Path filter list to apply to Updates sent to this peer|
| `prefix-list` | Prefix list to apply to Updates to be sent to this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound aspath-list none

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list [options] none`



  AS-Path filter list to apply to Updates sent to this peer

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]`



  Limits on prefix from the peer for this address-family

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
|`inbound`|  Limits on inbound prefix from the peer for this address- family|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]`



  Limits on inbound prefix from the peer for this address-family

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |           VRF |
| `<neighbor-id>` |      Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `maximum`            | Limit on number of prefixes of specific address-family that can be received from the peer. By default, there is no limit|
| `reestablish-wait`   | Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing. This would typically be 2-3 seconds.|
| `warning-only`       | If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.\
| `warning-threshold`  | Percentage of the maximum at which a warning syslog is generated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound warning-threshold

Percentage of the maximum at which a warning syslog is generated.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options] 1-100`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound reestablish-wait

Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast default-route-origination

Default route origination

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`   | Turn the feature 'on' or 'off'. The default is 'off'.|
| `policy`   | Optional route-map policy to control the conditions under which the default route is originated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast community-advertise

Community advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `extended` | If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `large`    | If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `regular`  | If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise

advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `advertise-map`  | route-map contains prefix-list which has list of routes/prefixes to operate on.|
| `exist-map`      | route-map contains the conditional routes/prefixes in prefix- list.|
| `non-exist-map`  | route-map contains the negative conditional routes/prefixes in prefix-list.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise advertise-map \<instance-name\>

route-map contains prefix-list which has list of routes/prefixes to operate on.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise exist-map \<instance-name\>

route-map contains the conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise non-exist-map \<instance-name\>

route-map contains the negative conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast weight

Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight [options] 0-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast

Peer IPv6 unicast address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `attribute-mod`         | Attribute mod for address family.|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer  for the specified address family|
| `prefix-limits`         | Limits on prefix from the peer for this address-family|
| `default-route-origination` | Default route origination|
| `policy`                | Policies for ipv4 unicast|
| `community-advertise`   | Community advertise for address family.|
| `conditional-advertise` | Conditional advertise for address family.|
| `enable`                | Turn the feature 'on' or 'off'. The default is 'off'.|
| `add-path-tx`           | Used to enable transmission of additional paths; by default, only the best path is announced to peers|
| `nexthop-setting`       | Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes "force" sets the next hop to ourselves for route advertisement including for reflected routes.|
| `route-reflector-client` | Specifies if this peer is a client and we are its route reflector|
| `route-server-client`   | Specifies if this peer is a client and we are its route server soft-reconfiguration  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.|
| `weight`                | Weight applied to routes received from peer; this is used in the BGP route selection algorithm|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath`         | If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.|
| `med`            | If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.|
| `nexthop`        | If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `allow-my-asn`     | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|
| `private-as`       | If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.|
| `replace-peer-as`  | If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `occurrences`    | Indicates max number of occurrences of the local system's AS number in the received AS_PATH|
| `origin`         | If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn occurrences

Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |


### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound`   |Limits on inbound prefix from the peer for this address- family |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `maximum`            | Limit on number of prefixes of specific address-family that can be received from the peer. By default, there is no limit|
| `reestablish-wait`   | Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing. This would typically be 2-3 seconds.|
| `warning-only`       | If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.|
| `warning-threshold`  | Percentage of the maximum at which a warning syslog is generated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound warning-threshold

Percentage of the maximum at which a warning syslog is generated.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options] 1-100`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound reestablish-wait

Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination

Default route origination

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `policy         | Optional route-map policy to control the conditions under which the default route is originated.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy

Policies for ipv6 unicast

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| outbound     |  Outbound unicast policy|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`      | Route map to apply to Updates received from this peer|
| `aspath-list`    | AS-Path filter list to apply to Updates received from this peer|
| `prefix-list`    | Prefix list to apply to Updates received from this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound aspath-list none

AS-Path filter list to apply to Updates received from this peer

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound

Outbound unicast policy

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`       | Route map to apply to Updates to be sent to this peer |
| `unsuppress-map`  | Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.|
| `aspath-list`     | AS-Path filter list to apply to Updates sent to this peer |
| `prefix-list`     | Prefix list to apply to Updates to be sent to this peer |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound aspath-list none

AS-Path filter list to apply to Updates sent to this peer

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise

Community advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `extended`       | If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `large`          | If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.|
| `regular`        | If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `advertise-map`  | route-map contains prefix-list which has list of routes/prefixes to operate on.|
| `exist-map`      | route-map contains the conditional routes/prefixes in prefix-list.|
| `non-exist-map`  | route-map contains the negative conditional routes/prefixes in prefix-list.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise advertise-map \<instance-name\>

route-map contains prefix-list which has list of routes/prefixes to operate on.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise exist-map \<instance-name\>

route-map contains the conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise non-exist-map \<instance-name\>

route-map contains the negative conditional routes/prefixes in prefix-list.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast weight

Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight [options] 0-65535`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn

Peer l2vpn EVPN address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `attribute-mode`        | Attribute mod for address family.|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family|
| `policy`                | Policies for l2vpn evpn|
| `enable`                | Turn the feature 'on' or 'off'. The default is 'off'.|
| `add-path-tx`           | Used to enable transmission of additional paths; by default, only the best path is announced to peers|
| `nexthop-setting`       | Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.|
| `route-reflector-client` | Specifies if this peer is a client and we are its route reflector|
| `route-server-client`   | Specifies if this peer is a client and we are its  route server|
| `soft-reconfiguration`  | If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod

Attribute mod for address family.

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `aspath`         | If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.|
| `med`            | If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.|
| `nexthop`        | If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `allow-my-asn`     | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|
| `private-as`       | If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.|
| `replace-peer-as`  | If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`         | Turn the feature 'on' or 'off'. The default is 'off'.|
| `occurrences`    | Indicates max number of occurrences of the local system's AS number in the received AS_PATH|
| `origin`         | If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn occurrences

Indicates max number of occurrences of the local system's AS number in the received AS_PATH


### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options] 1-10`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy

Policies for l2vpn evpn

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `inbound`        | Inbound l2vpn-evpn policy|
| `outbound`       | Outbound l2vpn-evpn policy|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound

Inbound l2vpn-evpn policy

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`  |Route map to apply to Updates received from this peer|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound

Outbound l2vpn-evpn policy

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `route-map`       | Route map to apply to Updates to be sent to this peer|
| `unsuppress-map`  | Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers

Peer peer-timers

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `connection-retry`     | Time interval at which connection attempts are retried upon a failure. If `auto`, the global value is used.This is the default.|
| `hold`                 | Hold timer. If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout. If `auto`, the global value is used. This is the default.|
| `keepalive`            | Keepalive timer. If `none`, keepalives are not sent. If `auto`, the global value is used. This is the default.|
| `route-advertisement`  | Time between route advertisements (BGP Updates). A non- zero value allows route advertisements to be delayed and batched. If `auto`, the global value is used. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> password none

Password

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> password [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> description none

neighbor description

### Usage

`nv set vrf <vrf-id> router bgp neighbor <neighbor-id> description [options] none`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router bgp dynamic-peer-limit

Maximum number of dynamic neighbors from whom we can accept a connection. Applicable only if 'dynamic-peering' subnet ranges are configured

### Usage

`nv set vrf <vrf-id> router bgp dynamic-peer-limit [options] 1-5000`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router static \<route-id\>

A route

### Usage

`nv set vrf <vrf-id> router static <route-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `distance`        | Paths|
| `via`             | Nexthops|
| `tag`             | Path tag|
| `address-family`  | Route address family|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\>

A path

### Usage

`nv set vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix |
| `<distance-id>` |  A path distance |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `via`       | Nexthops|
| `tag`       | Path tag|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\>

A via

### Usage

`nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix |
| `<distance-id>` |  A path distance |
| `<via-id>`       | IP address, interface, or "blackhole". |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `flag`           | Nexthop flags|
| `interface`      | The interface to use for egress. If not specified, it will automatically be determined. Only valid when the via's type is ipv4-address or ipv6-address.|
| `vrf`            | The VRF to use for egress. If not specified, the route's VRF will be used. Only valid when the via's type is ipv4-address or ipv6-address.|
| `type`           | The type of via|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> flag onlink

Nexthop flags

### Usage

`nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options] onlink`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix |
| `<distance-id>` |  A path distance |
| `<via-id>`       | IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\>

A via

### Usage

`nv set vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix |
| `<via-id>`       | IP address, interface, or "blackhole". |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `flag`        | Nexthop flags|
| `interface`   | The interface to use for egress. If not specified, it will automatically be determined. Only valid when the via's type is ipv4-address or ipv6-address.|
| `vrf`         | The VRF to use for egress. If not specified, the route's VRF will be used. Only valid when the via's type is ipv4-address or ipv6-address.|
| `type`        | The type of via|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> flag onlink

Nexthop flags

### Usage

`nv set vrf <vrf-id> router static <route-id> via <via-id> flag [options] onlink`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix |
| `<via-id>`       | IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router pim

PIM VRF configuration.

### Usage

`nv set vrf <vrf-id> router pim [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `timers`           | Timers|
| `ecmp`             | Choose all available ECMP paths for a particular RPF. If 'off', the first nexthop found will be used. This is the default.|
| `msdp-mesh-group`  | To connect multiple PIM-SM multicast domains using RPs.|
| `address-family`   | Address family specific configuration|
| `enable`           | Turn the feature 'on' or 'off'. The default is 'off'.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim timers

Timers

### Usage

`nv set vrf <vrf-id> router pim timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `keep-alive`     | Timeout value for S,G stream, in seconds|
| `rp-keep-alive`  | RP's timeout value, in seconds|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim ecmp

Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

### Usage

`nv set vrf <vrf-id> router pim ecmp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turn the feature 'on' or 'off'. The default is 'off'.|
| `rebalance`   | Recalculate all multicast streams in the event of path going down. If 'off', only the impacted streams by path going down recalculated. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\>

MSDP mesh-group

### Usage

`nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<msdp-mesh-group-id>`  | MSDP mesh group name |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `member-address`        | Set of member-address|
| `source-address`        | MSDP mesh-group source IP address|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\>

A MSDP mesh member

### Usage

`nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<msdp-mesh-group-id>`  | MSDP mesh group name |
| `<mesh-member-id>`  | MSDP mesh-group member IP address|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> source-address \<ipv4\>

MSDP mesh-group source IP address

### Usage

`nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address [options] <ipv4>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<msdp-mesh-group-id>`  | MSDP mesh group name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router pim address-family

Address family specific configuration

### Usage

`nv set vrf <vrf-id> router pim address-family [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ipv4-unicast`  | IPv4 unicast address family|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv set vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |


### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `spt-switchover`        | Build shortest path tree towards source.|
| `rp`                    | RP address and associated group range.|
| `register-accept-list`  | Prefix-list to specifiy source list to accept register message.|
| `send-v6-secondary`     | Use IPv6 secondary address to transmit PIM Hello  packets. It allows to use IPv6 nexthop in RPF lookup.|
| `ssm-prefix-list`       | Prefix-list to specificy Source Specific Multicast Group range.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover

Build shortest path tree towards source.

### Usage

`nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `action`       | PIM shortest path switchover (SPT) action. |
| `prefix-list`  | Prefix-list to specify multicast group range. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover prefix-list \<instance-name\>

Prefix-list to specify multicast group range.

### Usage

`nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\>

RP

### Usage

`nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rp-id>`  | RP IP address|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `group-range`  |`Set of group range assocaited to RP.|
|`prefix-list`  |`Prefix-list to specify multicast group range.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> group-range \<group-range-id\>

A group range

### Usage

`nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rp-id>`  | RP IP address|
| `<group-range-id>` |  Group range associated to RP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> prefix-list \<instance-name\>

Prefix-list to specify multicast group range.

### Usage

`nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list [options] <instance-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rp-id>`  | RP IP address|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf

OSPF VRF configuration.

### Usage

`nv set vrf <vrf-id> router ospf [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `area`                 | OSPF areas|
| `default-originate`    | Advertise a default route as external lsa|
| `distance`             | Administrative distance for installation into the rib|
| `max-metric`           | Set maximum metric value in router lsa to make stub router|
| `log`                  | Log configuration|
| `redistribute`         | Route redistribute|
| `timers`               | Timers|
| `enable`               | Turn the feature 'on' or 'off'. The default is 'off'.|
| `reference-bandwidth`  | Used to determine link cost/metric value relative to defined reference.|
| `rfc1583-compatible`   | RFC1583 compatible|
| `router-id`            | BGP router-id for this VRF. If "auto", inherit from the global config. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf area \<area-id\>

An OSPF area

### Usage

`nv set vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | Area|

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `filter-list`       | Filters networks between OSPF areas|
| `range`             | Area ranges|
| `network`           | Area networks|
| `default-lsa-cost`  | Default LSA cost. Only applies when type is non-normal.|
| `type`              | The type of area|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf area \<area-id\> filter-list

Filters networks between OSPF areas

### Usage

`nv set vrf <vrf-id> router ospf area <area-id> filter-list [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | Area |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `in`          | prefix-list to use as an inbound filter.|
| `out`         | prefix-list to use as an inbound filter. |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\>

Filters out components of the prefix

### Usage

`nv set vrf <vrf-id> router ospf area <area-id> range <range-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | Area |
| `<range-id>` |  Range |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `cost`       | User specified metric advertised for this summary lsa. If 'auto', operational default value is derived from components. This is the default.|
| `suppress`   | If on, filters out components but does not advertise prefix |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf area \<area-id\> network \<network-id\>

Filters out components of the prefix

### Usage

`nv set vrf <vrf-id> router ospf area <area-id> network <network-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | Area |
| `<network-id>`  | Network|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router ospf area \<area-id\> default-lsa-cost

Default LSA cost.  Only applies when type is non-normal.

### Usage

`nv set vrf <vrf-id> router ospf area <area-id> default-lsa-cost [options] 0-16777215`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` |   Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router ospf default-originate

Advertise a default route as external lsa

### Usage

`nv set vrf <vrf-id> router ospf default-originate [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`       | Turn the feature 'on' or 'off'. The default is 'off'.|
| `metric`       | Metric value for destination routing protocol|
| `metric-type`  | Set OSPF External Type 1/2 metrics|
| `route-map`    | Optional policy to apply to this advertisement|
| `always`       | When 'off', only advertise default route if one exists in the rib. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf default-originate metric-type

Set OSPF External Type 1/2 metrics

### Usage

`nv set vrf <vrf-id> router ospf default-originate metric-type [options] 1-2`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router ospf distance

Administrative distance for installation into the rib

### Usage

`nv set vrf <vrf-id> router ospf distance [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `external`   | External|
|`inter-area` | Inter-area|
|`intra-area`  |Intra-area|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf max-metric

Set maximum metric value in router lsa to make stub router

### Usage

`nv set vrf <vrf-id> router ospf max-metric [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `administrative`  | Administratively applied, for an indefinite period|
| `on-shutdown`     |Advertise stub-router prior to full shutdown of OSPF|
| `on-startup`      | Automatically advertise stub Router-LSA on startup of OSPF|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf log

Log configuration

### Usage

`nv set vrf <vrf-id> router ospf log [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | VRF |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `adjacency-changes` | Log adjacency changes|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf redistribute

Route redistribute

### Usage

`nv set vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `static`      | Route redistribute of static routes|
| `connected`   | Route redistribute of connected routes|
| `kernel`      | Route redistribute of kernel routes|
| `bgp`         | Route redistribute of bgp routes|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf redistribute static

Source route type.

### Usage

`nv set vrf <vrf-id> router ospf redistribute static [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |S

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`       | `Turn the feature 'on' or 'off'. The default is 'off'.|
| `metric`       | `Metric value for destination routing protocol|
| `metric-type`  | `Set OSPF External Type 1/2 metrics|
| `route-map`    | `Optional policy to apply to this advertisement|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf redistribute static metric-type

Set OSPF External Type 1/2 metrics

### Usage

`nv set vrf <vrf-id> router ospf redistribute static metric-type [options] 1-2`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router ospf redistribute connected

Source route type.

### Usage

`nv set vrf <vrf-id> router ospf redistribute connected [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| enable       | Turn the feature 'on' or 'off'. The default is 'off'.|
| metric       | Metric value for destination routing protocol|
| metric-type  | Set OSPF External Type 1/2 metrics|
| route-map    | Optional policy to apply to this advertisement|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf redistribute connected metric-type

Set OSPF External Type 1/2 metrics

### Usage

`nv set vrf <vrf-id> router ospf redistribute connected metric-type [options] 1-2`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router ospf redistribute kernel

Source route type.

### Usage

`nv set vrf <vrf-id> router ospf redistribute kernel [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`      | Turn the feature 'on' or 'off'. The default is 'off'.|
| `metric`      | Metric value for destination routing protocol|
| `metric-type` | Set OSPF External Type 1/2 metrics|
| `route-map`   | Optional policy to apply to this advertisement|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf redistribute kernel metric-type

Set OSPF External Type 1/2 metrics

### Usage

`nv set vrf <vrf-id> router ospf redistribute kernel metric-type [options] 1-2`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router ospf redistribute bgp

Source route type.

### Usage

`nv set vrf <vrf-id> router ospf redistribute bgp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`       | Turn the feature 'on' or 'off'. The default is 'off'.|
| `metric`       | Metric value for destination routing protocol|
| `metric-type`  | Set OSPF External Type 1/2 metrics|
| `route-map`    | Optional policy to apply to this advertisement|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf redistribute bgp metric-type

Set OSPF External Type 1/2 metrics

### Usage

`nv set vrf <vrf-id> router ospf redistribute bgp metric-type [options] 1-2`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> router ospf timers

Timers

### Usage

`nv set vrf <vrf-id> router ospf timers [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| lsa      |   LSA timers |
| spf      |   SPF timers |
| refresh     defines interval (sec) to re-send lsas to keep from aging out. If 'auto', inherited from global. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf timers lsa

LSA timers

### Usage

`nv set vrf <vrf-id> router ospf timers lsa [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `min-arrival` | Minimum delay in receiving new version of a LSA. If 'auto', inherited from global. This is the default.|
| `throttle`  | Delay (msec) between sending LSAs. If 'auto', inherited from  global. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf timers spf

SPF timers

### Usage

`nv set vrf <vrf-id> router ospf timers spf [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `delay` | Delay (msec) from first change received till SPF calculation. If 'auto', inherited from global. This is the default.|
| `holdtime` | Initial hold time (msec) between consecutive SPF calculations. If 'auto', inherited from global. This is the default.|
| `max-holdtime`|  Maximum hold time (msec) between consecutive SPF calculations. If 'auto', inherited from global. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> router ospf reference-bandwidth

Used to determine link cost/metric value relative to defined reference

### Usage

`nv set vrf <vrf-id> router ospf reference-bandwidth [options] 1-4294967`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set vrf \<vrf-id\> ptp

VRF PTP configuration.  Inherited by interfaces in this VRF.

### Usage

`nv set vrf <vrf-id> ptp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable`    | Turn the feature 'on' or 'off'. The default is 'on'.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set vrf \<vrf-id\> table auto

The routing table number, between 1001-1255, used by the named VRF. If auto, the default, it will be auto generated.

### Usage

`nv set vrf <vrf-id> table [options] auto`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set nve

Network Virtualization configuration and operational info

### Usage

`nv set nve [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `vxlan` | Global VxLAN configuration and operational properties.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set nve vxlan

VxLAN

### Usage

`nv set nve vxlan [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `mlag`             | VxLAN specific MLAG address|
| `source`           | Source address|
| `flooding`         | Configuration to specify how BUM traffic in the overlay is handled. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.|
| `enable`           | Turn the feature 'on' or 'off'. The default is 'off'.|
| `arp-nd-suppress`  | Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs).|
| `mac-learning`     | Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.|
| `mtu`              | interface mtu|
| `port`             | UDP port for VXLAN frames|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set nve vxlan mlag

VxLAN specfic MLAG configuration

### Usage

`nv set nve vxlan mlag [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `shared-address` |  shared anycast address for MLAG peers |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set nve vxlan source

Source address

### Usage

`nv set nve vxlan source [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `address`   |  IP addresses of this node's VTEP or 'auto'. If 'auto', use the primary IP loopback (not 127.0.0.1). This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set nve vxlan flooding

Handling of BUM traffic

### Usage

`nv set nve vxlan flooding [options] [<attribute> ...]`

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `head-end-replication`  | BUM traffic is replicated and individual copies sent to remote destinations.|
| `enable`                | Turn the feature 'on' or 'off'. The default is 'off'.|
| `multicast-group`       | BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set nve vxlan flooding head-end-replication \<hrep-id\>

Set of IPv4 unicast addresses or "evpn".

### Usage

`nv set nve vxlan flooding head-end-replication <hrep-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<hrep-id>` |   IPv4 unicast addresses or "evpn" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set nve vxlan flooding multicast-group \<ipv4-multicast\>

BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.

### Usage

`nv set nve vxlan flooding multicast-group [options] <ipv4-multicast>`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set nve vxlan port

UDP port for VXLAN frames

### Usage

`nv set nve vxlan port [options] 1024-65535`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set nve vxlan mtu

interface mtu

### Usage

`nv set nve vxlan mtu [options] 552-9216`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\>

An ACL is used for matching packets and take actions

### Usage

`nv set acl <acl-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule`       | acl rule |
| `type`       | acl type |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\>

ACL Matching criteria and action rule

### Usage

`nv set acl <acl-id> rule <rule-id> [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `match`    |   ACL match criteria |
| `action`    |  ACL action |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> match

An ACL match

### Usage

`nv set acl <acl-id> rule <rule-id> match [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `ip`    | IPv4 and IPv6 match |
| `mac`   | MAC match |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> match ip

An ACL IPv4/IPv6 match

### Usage

`nv set acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `source-port`  | source port |
| `dest-port`    | destination port |
| `fragment`     | Fragment packets |
| `ecn`          | ECN protocol packet match |
| `tcp`          | TCP protocol packet match |
| `dest-ip`      | Destination IP address |
| `dscp`         | DSCP |
| `icmp-type`    | ICMP message type |
| `icmpv6-type`  | ICMPv6 message type |
| `protocol`     | IP protocol |
| `source-ip`    | Source IP address |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> match ip source-port \<ip-port-id\>

L4 port

### Usage

`nv set acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |
| `<ip-port-id>` |  IP port ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> match ip dest-port \<ip-port-id\>

 L4 port

### Usage

`nv set acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |
| `<ip-port-id>` |  IP port ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> match ip fragment

State details

### Usage

`nv set acl <acl-id> rule <rule-id> match ip fragment [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> match ip ecn

ECN

### Usage

`nv set acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `flags`    |   ECN protocol flags |
| `ip-ect`    |  IP ECT |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> match ip ecn ip-ect

IP ECT

### Usage

`nv set acl <acl-id> rule <rule-id> match ip ecn ip-ect [options] 0-3`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> match ip tcp

L4 port

### Usage

`nv set acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `flags`       | TCP protocol flags |
| `mask`        | TCP protocol flag mask |
| `state`       | TCP state |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> match ip tcp state established

TCP state

### Usage

`nv set acl <acl-id> rule <rule-id> match ip tcp state [options] established`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> match mac

An ACL MAC match

### Usage

`nv set acl <acl-id> rule <rule-id> match mac [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `dest-mac`        | Destination MAC address|
| `dest-mac-mask`   | Destination MAC address mask|
| `protocol`        | MAC protocol|
| `Source-mac`      | Source MAC address|
| `source-mac-mask` | Source MAC address mask|
| `vlan`            | VLAN ID|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> match mac source-mac-mask \<mac\>

Source MAC address mask

### Usage

`nv set acl <acl-id> rule <rule-id> match mac source-mac-mask [options] <mac>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> match mac dest-mac-mask \<mac\>

Destination MAC address mask

### Usage

`nv set acl <acl-id> rule <rule-id> match mac dest-mac-mask [options] <mac>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> match mac vlan

VLAN ID

### Usage

`nv set acl <acl-id> rule <rule-id> match mac vlan [options] 1-4094`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action

ACL rule action

### Usage

`nv set acl <acl-id> rule <rule-id> action [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `permit`      | Permit action |
| `deny`        | Deny action |
| `log`         | Provides ACL logging facility |
| `set`         | Modify the packet with appropriate values |
| `erspan`      | ERSPAN session |
| `police`      | policing of packets/bytes |
| `span`        | SPAN session |

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> action permit

Permit packets

### Usage

`nv set acl <acl-id> rule <rule-id> action permit [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action deny

deny packets

### Usage

`nv set acl <acl-id> rule <rule-id> action deny [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action log

log packets

### Usage

`nv set acl <acl-id> rule <rule-id> action log [options]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action set

Set action for packets

### Usage

`nv set acl <acl-id> rule <rule-id> action set [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `class`       | Sets the class value for classification of the packet|
| `cos`         | Set the CoS value|
| `dscp`        | Sets/Modifies the DSCP value in the packet|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> action set class

Sets the class value for classification of the packet

### Usage

`nv set acl <acl-id> rule <rule-id> action set class [options] 0-7`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule\<rule-id\> action set cos

Set the CoS value

### Usage

`nv set acl <acl-id> rule <rule-id> action set cos [options] 0-7`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action erspan

ERSPAN session

### Usage

`nv set acl <acl-id> rule <rule-id> action erspan [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `dest-ip`     | Destination IP address|
| `source-ip`   | Source IP address|
| `ttl`         | Time to Live|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> action erspan ttl

Time to Live

### Usage

`nv set acl <acl-id> rule <rule-id> action erspan ttl [options] 1-2`55`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action police

### Usage

`nv set acl <acl-id> rule <rule-id> action police [options] [<attribute> ...]`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `burst` | Policing burst value |
| `mode` | Policing mode |
| `rate` | Policing rate value|

### Version History

Introduced in Cumulus Linux 5.0.0

## nv set acl \<acl-id\> rule \<rule-id\> action police burst

Policing burst value

### Usage

`nv set acl <acl-id> rule <rule-id> action police burst [options] 1-2`147483647`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |  ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action police rate

Policing rate value

### Usage

`nv set acl <acl-id> rule <rule-id> action police rate [options] 1-2`147483647`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |    ACL ID |
| `<rule-id>` |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

## nv set acl \<acl-id\> rule \<rule-id\> action span \<interface-name\>

SPAN session

### Usage

`nv set acl <acl-id> rule <rule-id> action span [options] <interface-name>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   ACL ID |
| `<rule-id>` |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```
