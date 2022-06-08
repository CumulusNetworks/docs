---
title: Set Commands
author: Cumulus Networks
weight: 30
product: Cumulus Linux
type: nojs
---
This section describes all the `nv set` commands, together with their attributes and identifiers.

## nv set router

Configures global routing settings for BGP, OSPF, PIM, IGMP, VRR, VRRP, router policies, next hop groups, and adaptive routing.

**Usage**

  `nv set router [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

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

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router nexthop-group \<nexthop-group-id\>

Sets the name of the next hop group.

**Usage**

`nv set router nexthop-group <nexthop-group-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |

**Attributes**

| Attribute |  Description   |
| --------- | -------------- |
| `via` | Configures the next hop. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1
```

## nv set router nexthop-group \<nexthop-group-id\> via \<via-id\>

Sets the IP addresses of the next hops in the next hop group.

**Usage**

`nv set router nexthop-group <nexthop-group-id> via <via-id> [options] [<attribute> ...]`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |
| `<via-id>` | The IP address of the next hop.|

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
|  `interface`| Configures the interface to use for egress. If you do not specify an interface, the switch determines the interface automatically. This attribute is only valid for IPv4 or IPv6 addresses. |
| `vrf` | Configures the VRF to use for egress. If you do not specify the VRF, the switch uses the VRF that the route uses. This attribute is only valid for IPv4 or IPv6 addresses. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1 via 192.168.0.32
```

## nv set router nexthop-group \<nexthop-group-id\> via \<via-id\> interface \<interface-name\>

Sets the interface to use for egress. If you do not specify an interface, the switch determines the interface automatically. This attribute is only valid for IPv4 or IPv6 addresses.

**Usage**

`nv set router nexthop-group <nexthop-group-id> via <via-id> interface [options] (auto|<interface-name>)`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |
| `<via-id>` | The IP address of the next hop.|
| `<interface-name>` | The interface to use for egress.|

**Default Setting**

`auto`: The switch determines the interface automatically.

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1 via 192.168.0.32 interface swp51
```

## nv set router nexthop-group \<nexthop-group-id\> via \<via-id\> vrf \<vrf-name\>

Sets the VRF to use for egress. If you do not specify the VRF, the switch uses the VRF that the route uses. This attribute is only valid for IPv4 or IPv6 addresses.

**Usage**

`nv set router nexthop-group <nexthop-group-id> via <via-id> vrf [options] (auto|<vrf-name>)`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<nexthop-group-id>` | The next hop group name. |
| `<via-id>` | The IP address of the next hop.|
| `<vrf-name>` | The vrf to use for egress.|

**Default Setting**

`auto`: The switch uses the VRF that the route uses.

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router nexthop-group group1 via 192.168.0.32 vrf RED
```

## nv set router pbr

Configures global PBR (Policy-based Routing) settings.

**Usage**

`nv set router pbr [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `map`| Configures PBR policies.|
| `enable`| Turns the PBR `on` or `off`. The default is `off`. |

## nv set router pbr map \<pbr-map-id\>

Configures the name of the PBR route map.

**Usage**

`nv set router pbr map <pbr-map-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule`| Configures the PBR rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\>

Configures the PBR route map rule number.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id>` | The PBR rule number. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| match     |  Configures the PBR match criteria. |
| action    |  Configures the action to take; permit or deny.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 10
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match

Sets the match criteria you want to use for the PBR map rule.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> match [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id>`    | The PBR rule number. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `destination-ip` |  Configures PBR to match a destination IP prefix. |
| `dscp` | Configures PBR to match packets according to the DSCP field in the IP header. The DSCP value can be an integer between 0 and 63 or the DSCP codepoint name.   |
| `ecn`  | Configures PBR to match packets according to the ECN field in the IP header. The ECN value can be an integer between 0 and 3. |
| `source-ip`  |  Configures PBR to match a source IP prefix. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match source-ip \<ipv4-prefix\>|\<ipv6-prefix\>

Sets PBR to match packets according to the source IP prefix.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> match source-ip (<ipv4-prefix>|<ipv6-prefix>)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |
| `<ipv4-prefix>` or `<ipv6-prefix>` | The source IPv4 or IPv6 prefix. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 10 match source-ip 10.1.4.1/24 
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match destination-ip \<ipv4-prefix\>|\<ipv6-prefix\>

Sets PBR to match packets according to the destination IP prefix.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> match destination-ip (<ipv4-prefix>|<ipv6-prefix>)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |
| `<ipv4-prefix>` or `<ipv6-prefix>` | The destination IPv4 or IPv6 prefix. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 10 match destination-ip 10.1.2.0/24
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match dscp

Sets PBR to match packets according to the DSCP field in the IP header. The DSCP value can be an integer between 0 and 63 or the DSCP codepoint name.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> match dscp [options] 0-63`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>`   | The PBR rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 match dscp 10
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> match ecn

Sets PBR to match packets according to the ECN field in the IP header. The ECN value can be an integer between 0 and 3.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> match ecn [options] 0-3`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` |  The PBR route map name. |
| `<rule-id>` |  The PBR rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 match ecn 3
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action

Sets the action you want the PBR map rule to take, such as apply a net hop group or a VRF to a policy.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> action [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>` | The PBR route map name. |
| `<rule-id> `  |  The PBR rule number. |

**Attributes**

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop-group` | Configures the route through the nexthop-group. |
| `vrf`     | Configures the route through a VRF. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 action vrf RED
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\>

Configures the next hop group you want to apply to the policy map.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id> [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>`  |  The PBR route map name. |
| `<rule-id>`     |  The PBR rule number. |
| `<nexthop-group-id>`  | The next hop group name. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 action nexthop-group group1
```

## nv set router pbr map \<pbr-map-id\> rule \<rule-id\> action vrf \<vrf-name\>

Sets the VRF you want to apply to the policy map. If you do not set a VRF, the rule uses the VRF table set for the interface.

**Usage**

`nv set router pbr map <pbr-map-id> rule <rule-id> action vrf [options] <vrf-name>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<pbr-map-id>`  |  The PBR route map name. |
| `<rule-id>`     |  The PBR rule number. |
| `<vrf-name>`    |  The VRF you want to apply to the policy map. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr map map1 rule 1 action vrf RED
```

## nv set router pbr enable

Enables or disables PBR.

**Usage**

`nv set router pbr enable [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pbr enable on
```

## nv set router policy

Configures a router policy.

**Usage**

`nv set router policy [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute  |  Description   |
| ---------  | -------------- |
| `community-list` |  Configures a community list. |
| `as-path-list` | Configures an AS path list. |
| `ext-community-list` | Configures an Extended Community list. |
| `large-community-list` | Configures a Large Community list. |
| `prefix-list` | Configures prefix lists. |
| `route-map` | Configures route maps. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router policy community-list \<list-id\>

Configures the name of the community list you want to use to match BGP community policies.

**Usage**

`nv set router policy community-list <list-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | | Configures the community list rule. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list 
```

## nv set router policy community-list \<list-id\> rule \<rule-id\>

Configures the community list rule number.

**Usage**

`nv set router policy community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |
| `<rule-id>`  | The community list rule number. |

**Attributes**

| Atrribute |  Description   |
| --------- | -------------- |
| `community` | Configures the community expression. |
| `action`    | Configures the action you want to take for a match; permit or deny. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
```
## nv set router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\>

Sets the name of the community you want to match.

**Usage**

`nv set router policy community-list <list-id> rule <rule-id> community <community-id> [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The community list name. |
| `<rule-id>` | The community list rule number. |
| `<community-id>` | The community number in AA:NN format or the well-known name. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 community 100:100
```

## nv set router policy community-list \<list-id\> rule \<rule-id\> action

Sets the action you want to take when you meet the match criteria; permit or deny.

**Usage**

`nv set router policy community-list <list-id> rule <rule-id> action [options] (permit|deny)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |
| `<rule-id>`  | The community list rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
```

## nv set router policy as-path-list \<list-id\>

Sets the name of the AS path access list you want to use to match AS paths.

**Usage**

`nv set router policy as-path-list <list-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name.|

**Attributes**

| Atrribute |  Description   |
| --------- | -------------- |
| `rule`    |  Configures the AS path list rule. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist
```

## nv set router policy as-path-list \<list-id\> rule \<rule-id\>

Configures the AS Path list rule number.

**Usage**

`nv set router policy as-path-list <list-id> rule <rule-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS Path list name. |
| `<rule-id>` |  The prefix list rule number. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `action` |  Configures the action you want to take when there is a match, such as permit or deny. |
| `aspath-exp` | Configures the regular expression you want to use to match BGP AS paths. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10
```

## nv set router policy as-path-list \<list-id\> rule \<rule-id\> action

Sets the action you want to take for a match; permit or deny.

**Usage**

`nv set router policy as-path-list <list-id> rule <rule-id> action [options] (permit|deny)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS path list name. |
| `<rule-id>` |  The AS path list rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10 action permit
```

## nv set router policy as-path-list \<list-id\> rule \<rule-id\> aspath-exp \<bgp-regex\>

Configures the regular expression you want to use to match BGP AS paths.

**Usage**

`nv set router policy as-path-list <list-id> rule <rule-id> aspath-exp [options] <bgp-regex>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name. |
| `<rule-id> ` | Th AS path list rule number. |
| `bgp-regex` | The regular expression you want to use to match BGP AS paths.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy as-path-list mylist rule 10 aspath-exp ^100_
```

## nv set router policy ext-community-list \<list-id\>

Sets the name of the Extended Community list you want to use to match BGP communities.

**Usage**

`nv set router policy ext-community-list <list-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The extended community list name. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures the extended community list rule. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\>

Sets the extended community list rule number.

**Usage**

`nv set router policy ext-community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `ext-community` | Configures the Extended Community expression. |
| `action `  | Configures the action you want to take when there is a match; permit or deny.

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community

Sets the Extended Community name.

**Usage**

`nv set router policy ext-community-list <list-id> rule <rule-id> ext-community [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<list-id>` |  The Extended Community list name. |
| `<rule-id>` | The Extended Community list rule number. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rt ` | Configures the Route Target Extended Community. |
| `soo ` | Configures the site-of-origin (SoO) Extended Community.  |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community 64510:2
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt \<ext-community-id\>

Configures the Route Target Extended Community.

**Usage**

`nv set router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id> [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |
| `<ext-community-id>` | The Extended Community number in AA:NN or IP:NN format. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community rt 64510:1111
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo \<ext-community-id\>

Configures the site-of-origin (SoO) Extended Community to identify routes that originate from a certain site so that you can prevent readvertising that prefix back to the source site.

**Usage**

`nv set router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id> [options]`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id> ` | The community list name. |
| `<rule-id> ` |  The community list rule number. |
| `<ext-community-id>` | The Extended Community number in AA:NN or IP:NN format. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 ext-community soo ????????
```

## nv set router policy ext-community-list \<list-id\> rule \<rule-id\> action

Configures the action to take on a match; permit or deny.

**Usage**

`nv set router policy ext-community-list <list-id> rule <rule-id> action [options] (permit|deny)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The community list rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy ext-community-list mylist rule 10 action permit
```

## nv set router policy large-community-list \<list-id\>

Configures the name of the Large Community list you want to use to match community based BGP policies.

**Usage**

`nv set router policy large-community-list <list-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>  | The community list name |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` |  Configures the Large Community list rule. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist
```

## nv set router policy large-community-list \<list-id\> rule \<rule-id\>

Configures the Large Community list rule number.

**Usage**

`nv set router policy large-community-list <list-id> rule <rule-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` | The community list name |
| `<rule-id>`  | The community list rule number. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `large-community`  | Configures the large community expression. |
| `action`  |  Configures the action you want to take when there is a match; permit or deny. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10
```

## nv set router policy large-community-list \<list-id\> rule \<rule-id\> large-community \<large-community-id\>

Configures the community names for the large community list.

**Usage**

`nv set router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id> [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id> ` | The community list rule number. |
| `<large-community-id>` | The community number in AA:BB:CC format. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10 large-community ?????
```

## nv set router policy large-community-list <list-id> rule <rule-id> action

**Usage**

`nv set router policy large-community-list <list-id> rule <rule-id> action [options] (permit|deny)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id> ` | The community list rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy large-community-list mylist rule 10 action permit
```

## nv set router policy prefix-list \<prefix-list-id\>

Configures the name of the prefix list you want to use to match IPv4 and IPv6 address prefixes.

**Usage**

`nv set router policy prefix-list <prefix-list-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures the prefix list rule number. |
| `type` | Configures the prefix list type. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\>

Configures the prefix list rule number.

**Usage**

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>`  | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |

**Attributes**

| Atrribute |  Description   |
| --------- | -------------- |
| `match` | Configures the prefix list match criteria. |
| `action` | Configures the action you want to take when there is a match; permit or deny. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\>

Configures the prefix match criteria you want to use.

**Usage**

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id> ` | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix you want to match.|

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `max-prefix-len` | Configures the maximum prefix length to match. |
| `min-prefix-len` | Configures the minimum prefix length to match. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> min-prefix-len

Configures the minimum prefix length you want to match.

**Usage**

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len [options] 0-128`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 min-prefix-len 30
```

## nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> max-prefix-len

Configures the maximum prefix length you want to match. You can specify a value between 0 and 128.

**Usage**

`nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len [options] 0-128`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name.  |
| `<rule-id>` |  The prefix list rule number. |
| `<match-id>` |  The IPv4 or IPv6 prefix. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 max-prefix-len 30
```

## nv set router policy prefix-list \<list-id\> rule \<rule-id\> action

Configures the action to take on a match; permit or deny.

**Usage**

`nv set router policy prefix-list <list-id> rule <rule-id> action [options] (permit|deny)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |
| `<rule-id>` |  The prefix list rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist rule 10 action permit
```

## nv set router policy prefix-list \<list-id\> type

Configures the type of prefix list; IPv4 or IPv6.

**Usage**

`nv set router policy prefix-list <prefix-list-id> type [options] (ipv4|ipv6)`

**Default Setting**

`ipv4`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy prefix-list mylist type ipv4
```

## nv set router policy route-map \<route-map-id\>

Configures the name of the route map you want to use for policy configuration.

**Usage**

`nv set router policy route-map <route-map-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` |  The route map name. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures the route map rule. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\>

Configures the route map rule number.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `match` |  Configures the route map match criteria. |
| `set` | Configures the route map set criteria. |
| `action` | Configures the action you want to take when there is a match; permit or deny.   |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match

Configures the match criteria you want to use for the route map rule.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number. |

**Attributes**

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

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-list \<instance-name\>

Configures the IP prefix list to use as a match in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list [options] <instance-name>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>`  |  The route map rule number. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-len

Configures the IP address prefix length you want to match. You can specify a value between 0 and 128.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len [options] 0-128`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-len 128
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-list \<instance-name\>

Configures the IP next hop list you want to use as a match in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list [options] <instance-name>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-len

Configures the route map to match an IP nexthop prefix length.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len [options] 0-32`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-len 32
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop \<ipv4\>|\<ipv6\>

Configures the route map to match the IP address of a nexthop.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop [options] (<ipv4>|<ipv6>)`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<ipv4>` or `<ipv6>` | The IPv4 or IPv6 address of the next hop.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop 10.10.101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-type blackhole

Configures the route map to match a null route (blackhole).

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type [options] blackhole`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-type blackhole
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match as-path-list \<instance-name\>

Configures the name of the BGP AS path list you want use in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match as-path-list [options] <instance-name>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match as-path-list MYLIST
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match community-list \<instance-name\>

Configures the name of the BGP community list you want to use in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match community-list [options] <instance-name>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match community-list MYLIST
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match large-community-list \<instance-name\>

Configures the name of the BGP Large Community list you want to use in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match large-community-list [options] <instance-name>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match large-community-list MYLIST
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match metric \<value\>

Configures the route metric (the cost values used by routers to determine the best path to a destination network) you want to use as a match in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match metric [options] <value>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match metric 1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match interface \<interface-name\>|\<vrf-name\>

Configures the interface you want to use as a match in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match interface (<interface-name>|<vrf-name>)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match interface swp51
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match tag

Configures the BGP tag you want to use as a match in the route map. You can specify a value between 1 and 4294967295.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match tag [options] 1-4294967295`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match tag 10
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-protocol

Configures the source protocol you want to use as a match in the route map. The source protocol is the protocol through which the switch learns the route. You can specify `bgp`, `connected`, `kernel`, `ospf`, `spf6`, `sharp` or `static`.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match source-protocol [options] (bgp|connected|kernel|ospf|ospf6|sharp|static)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match source-protocol bgp
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match origin

Configures the BGP origin you want to use as a match in the route map. You can specify `egp`, `igp`, or `incomplete`.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match origin [options] (egp|igp|incomplete)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match origin igp
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match peer

Configures the BGP peer you want to use as a match in the route map. You can specify `local`, the interface, or the IPv4 or IPv6 address.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match peer [options] (local|<interface-name>|<ipv4>|<ipv6>)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match peer swp51
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match local-preference

Configures the local preference of the route you want to match in the route map. You can specify a value between 0 and 4294967295.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match local-preference [options] 0-4294967295`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match local-preference 300
```

## nv set router policy route-map <route-map-id> rule <rule-id> match evpn-route-type

Configures the EVPN route type you want to match in the route map. You can specify type 2 (MAC or IP advertisement routes), type 3 (Inclusive multicast Ethernet tag routes), or type 5 (IP prefix routes).

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match evpn-route-type [options] (macip|imet|ip-prefix)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match evpn-route-type macip
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-vni \<value\>

Configures the VNI ID you want to use a match in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match evpn-vni [options] <value>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match evpn-vni 10
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-vrf \<vrf-name\>

Configures the source VRF you want to use as a match in the route map.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match source-vrf [options] <vrf-name>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match source-vrf RED
```

## nv set router policy route-map <route-map-id> rule <rule-id> match type

Configures the the route types you want to use as a match in the route map. You can specify IPv4 or IPv6 routes.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> match type [options] (ipv4|ipv6)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 match ipv4
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set

Configures the route map rule set.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Attributes**

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

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend

Sets the BGP AS Path you want to prepend for a matched route.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `as` | Configures the BGP AS number. |
| `last-as` | Configures the number of times to insert the AS number of the peer. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend as

Sets the BGP AS number to prepend for a matched route.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as [options] 1-4294967295`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as 65101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend last-as

Sets the last BGP AS path to prepend for a matched route. You can set a value between 1 and 10.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as [options] 1-10`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as last-as 4
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community \<community-id\>

Sets the BGP Community attribute for a matched route.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set community <community-id> [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<community-id>` | The Community number in AA:NN format or the well-known name.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set community 100:100
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community \<large-community-id\>

Sets the Large BGP Community for a matched route.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id> [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<large-community-id>` | The Large Community number in AA:BB:CC format.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set large-community ????
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\>

Sets the aggregator AS Number for a matched route.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN number.|

**Attributes**

| Atrribute |  Description   |
| --------- | -------------- |
| `address` | Configures the set of IPv4 addresses. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address \<ipv4-address-id\>

Sets the originating AS of an aggregated route if there is a match.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id> [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN number.|
| `<ipv4-address-id>` |  The IPv4 address. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101 address 10.10.10.01
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-exclude

Configures a set clause in the route map to remove the AS number from the AS Path attribute of the route. You can specify a value between 1 and 4294967295.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set as-path-exclude [options] 1-4294967295`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set as-path-exclude 65101
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set atomic-aggregate (on|off)

Configures a set clause in the route map to inform BGP peers that the local router is using a less specific (aggregated) route to a destination. You can specify `on` or `off`.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate [options] (on|off)`

**Default Setting**

`off`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set atomic-aggregate on
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-rt \<route-distinguisher\>

Sets the route target Extended Community for a matched route.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-rt [options] <route-distinguisher>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
|`<route-distinguisher>` | The route distinguisher. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-rt 64510:1111
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-soo \<route-distinguisher\>

Sets the site-of-origin (SoO) Extended Community for a matched route.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-soo [options] <route-distinguisher>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<route-distinguisher>` |The route distinguisher. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-soo ????
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-bw

Sets the BGP Extended Community for a matched route. You can specify `cumulative` `multipaths` `cumulative-non-transitive`, or `multipaths-non-transitive`.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-bw [options] (cumulative|multipaths|cumulative-non-transitive|multipaths-non-transitive)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ext-community-bw multipaths.
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set local-preference

Sets the BGP local preference for a matched route. You can specify a value between 0 and 4294967295.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set local-preference [options] 0-4294967295`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set local-preference 300
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set weight

Sets the BGP weight value for a matched route. You can specify a value between 0 and 4294967295.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set weight [options] 0-4294967295`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set weight 300
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric

Configures a set clause in the route map for the metric value for the destination routing protocol. You can set `metric-plus`, `metric-minus`, `rtt`, `rtt-plus`, or `rtt-minus`.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set metric [options] (metric-plus|metric-minus|rtt|rtt-plus|rtt-minus)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set metric metric-minus
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric type

Configures a set clause in the route map for the metric type for routes that match the map. The metric type is used by the the OSPF protocol. You can set OSPF external type 1 metric or OSPF external type 2 metric.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set metric [options] (type-1|type-2)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set metric type type-2
```

## nv set router policy route-map <route-map-id> rule <rule-id> set origin

Configures a set clause in the route map for the BGP origin code for the matched route. You can specify `egp` (the switch learns the origin of the route from an exterior routing protocol with the given autonomous system number) `igp` (the switch learns the the origin of the route from an interior routing protocol), or `incomplete` (the origin of the route is unknown).

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set origin [options] ((egp|igp|incomplete) `

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set origin igp
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set tag

Configures a set clause in the route map for the tag value for the routing protocol.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set metric [options] 1-4294967295`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set tag 100
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-global \<ipv6\>

Configures a set clause in the route map for IPv6 next hop global address.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global [options] <ipv6>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-global 2001:db8:0002::0a00:0002
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-local \<ipv6\>

Configures a set clause in the route map for the IPv6 next hop local address.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local [options] <ipv6>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-local 2001:db8:0002::0a00:0002
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-prefer-global

Configures a set clause in the route map to use the global address as the IPv6 next hop.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global [options] (on|off)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-prefer-global on
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ip-nexthop

Configures a set clause in the route map for the next hop address for an incoming packet regardless of the explicit route for the packet. You can specify the IP address of the peer, or leave it unchanged.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set ip-nexthop [options] (unchanged|peer-addr)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set ip-nexthop peer-addr
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set source-ip

Configures a set clause in the route map for the source IP address. You can specify an IPv4 or IPv6 address.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set source-ip [options] (<ipv4>|<ipv6>)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set source-ip 10.1.10.0
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community-delete-list

Configures a set clause in the route map to remove BGP communities from being advertised to other BGP routes.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set community-delete-list [options] (<instance-name>|<integer>)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set community-delete-list communitylist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community-delete-list 

Configures a set clause in the route map to remove BGP Large Communities from being advertised to other BGP routes.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list [options] (<instance-name>|<integer>)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 set large-community-delete-list largecommunitylist1
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action

Configures the route map rule action; permit or deny.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> action [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `deny`   |  Configures the action of the rule to deny. |
| `permit` |  Configures the action of the rule to permit. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action deny

Configures the route map rule action to deny.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> action deny [options]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 deny
```

## nv set router policy route-map <route-map-id> rule <rule-id> action permit

Configures the route map rule action to permit.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> action permit [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `exit-policy` | Configures the permit action exit policy. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy

Configures the permit action exit policy.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `rule` | Configures jump to specific rule |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit exit-policy
```

## nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy rule \<value\>

Configures the route map to go to specific rule when the matching conditions are met.

**Usage**

`nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule [options] <value>`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router policy route-map MAP1 rule 10 permit exit-policy rule 20
```

## nv set router bgp

Configures BGP global configuration.

**Usage**

`nv set router bgp [options] [<attribute> ...`

**Default Setting**

`off`

**Attributes**

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

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router bgp graceful-restart

Configures BGP graceful restart globally on the switch so that a BGP speaker can signal to its peers that it can preserve its forwarding state and continue data forwarding during a restart. It also enables a BGP speaker to continue to use routes announced by a peer even after the peer has gone down.

**Usage**

`nv set router bgp graceful-restart [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `mode` | Configures the role of the router during graceful restart. You can specify `helper-only`, where the router is in helper mode, `full`, where the router is in both helper and restarter mode, or `off`, where BGP graceful restart is off. |
| `path-selection-deferral-time` | Configures the number of seconds a restarting peer defers path-selection when waiting for the EOR (end of RIB) marker from peers. The default is 360 seconds. You can set a value between 0 and 3600.|
| `restart-time` |  Configures the number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. The default is 120 seconds. You can set a value between 1 and 4095. |
| `stale-routes-time` | Configures the number of seconds to hold stale routes for a restarting peer. The default is 360 seconds. You can set a value between 1 and 4095. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router bgp graceful-restart mode (off|helper-only|full)

Configures the role of the router during BGP graceful restart. You can specify `helper-only`, where the router is in helper mode, `full`, where the router is in both helper and restarter mode, or `off`, where BGP graceful restart is off.

**Usage**

`nv set router bgp graceful-restart mode [options] (off|helper-only|full)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart mode full
```

## nv set router bgp graceful-restart restart-time

Configures the number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. You can set a value between 1 and 4095.

**Usage**

`nv set router bgp graceful-restart restart-time [options] 1-3600`

**Default Setting**

120 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp restart-time 400
```

## nv set router bgp graceful-restart path-selection-deferral-time

Configures the number of seconds a restarting peer defers path-selection when waiting for the EOR (end of RIB) marker from peers. You can set a value between 0 and 3600.

**Usage**

`nv set router bgp graceful-restart path-selection-deferral-time [options] 0-3600`

**Default Setting**

360 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart path-selection-deferral-time 300
```

## nv set router bgp graceful-restart stale-routes-time

Configures the number of seconds to hold stale routes for a restarting peer. You can set a value between 1 and 4095.

**Usage**

`nv set router bgp graceful-restart stale-routes-time [options] 1-3600`

**Default Setting**

360 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart stale-routes-time 400
```

## nv set router bgp convergence-wait

Configures read-only mode so that you can reduce CPU and network usage when restarting the BGP process.

**Usage**

`nv set router bgp convergence-wait [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `establish-wait-time` | Configures the maximum time to wait to establish BGP sessions. BGP does not track any peers that do not come up in this time for convergence-wait purposes. A value of 0 means there is no maximum time and BGP tracks peers for convergence time.|
| `time`  | Configures the time to wait for peers to send an EOR (end of RIB) before the switch selects the path, installs and advertises the route. BGP uses the time to wait during startup or when all peerings flap. A value of zero means that there is no wait time. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router bgp convergence-wait time

Configures the time to wait for peers to send an EOR (end of RIB) before the switch selects the path, installs and advertises the route. BGP uses the time to wait during startup or when all peerings flap. You can set a value between 0 and 3600 seconds. A value of zero means that there is no wait time.

**Usage**

`nv set router bgp convergence-wait time [options] 0-3600`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp convergence-wait time 300
```

## nv set router bgp convergence-wait establish-wait-time

Configures the maximum time to wait to establish BGP sessions. BGP does not track any peers that do not come up in this time for convergence-wait purposes.  You can set a value between 0 and 600 seconds.  A value of 0 means there is no maximum time and BGP tracks peers for convergence time.

**Usage**

`nv set router bgp convergence-wait establish-wait-time [options] 0-3600`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp establish-wait-time time 200
```

## nv set router bgp enable

Turns BGP on or off. The default is off.

**Usage**

`nv set router bgp enable [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp enable on
```

## nv set router bgp autonomous-system

Configures the ASN to identify the BGP node. This command configures the ASN for all VRFs if a single AS is in use; otherwise, you must set an ASN for every VRF.

**Usage**

`nv set router bgp autonomous-system [options] (1-4294967295|none|leaf|spine)`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp autonomous-system 65101
```

## nv set router bgp router-id

Configures the BGP router ID on the switch, which is a 32-bit value and is typically the address of the loopback interface. This command configures a BGP router ID for all VRFs if a common VRF is used; otherwise, you must set a router ID for every VRF.

**Usage**

`nv set router bgp router-id [options] (none|<ipv4>)`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp router-id 10.10.10.1
```

## nv set router bgp policy-update-timer

Configures the wait time in seconds before processing updates to policies to ensure that a series of changes process together. You can set a value between o and 600.

**Usage**

`nv set router bgp policy-update-timer [options] 0-600`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp policy-update-timer 200
```

## nv set router bgp graceful-shutdown (on|off)

Configures graceful shutdown, which forces traffic to route around the BGP node and reduces packet loss during planned maintenance of a router or link.

**Usage**

`nv set router bgp graceful-shutdown [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-shutdown on
```

## nv set router bgp wait-for-install

Configures BGP to wait for a response from the RIB indicating that the routes installed in the RIB are also installed in the ASIC before sending updates to peers.

**Usage**

`nv set router bgp wait-for-install [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router bgp wait-for-install on
```

## nv set router ospf

Configures OSPF globally on the switch.

**Usage**

`nv set router ospf [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `timers` | Configures OSPF timers. |
| `enable` | Turns OSPF on or off. The default is off. |
| `router-id` | Configures the OSPF router ID. This command configures the router ID for all VRFs if a common one is used; otherwise, you must set the router ID for every VRF. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers

Configures OSPF Link State Advertisement (LSA) and Shortest Path First (SPF) timers, and the refresh interval.

**Usage**

`nv set router ospf timers [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| --------- | -------------- |
| `lsa` | Configures LSA timers. |
| `spf` | Configures the SPF timers. |
| `refresh` | Configures the refresh interval in seconds to resend LSAs to prevent them from aging out.|

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers lsa

Configures LSA timers.

**Usage**

`nv set router ospf timers lsa [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `min-arrival` |  Configures the minimum interval during which OSPF can accept the same LSA.|
| `throttle` |  Configures the delay in milliseconds between sending LSAs. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers lsa min-arrival

Configures the minimum interval in seconds during which OSPF can accept the same LSA. You can specify a value between 0 and 600000.

**Usage**

`nv set router ospf timers lsa min-arrival [options] 0-600000`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers lsa min-arrival 300000
```

## nv set router ospf timers lsa throttle

Configures the amount of time after which OSPF sends LSAs. You can specify a value between 0 and 5000 milliseconds.

**Usage**

`nv set router ospf timers lsa throttle [options] 0-5000`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers lsa throttle 3000
```

## nv set router ospf timers spf

Configures the SPF timers.

**Usage**

`nv set router ospf timers spf [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `delay` | Configures the number of milliseconds to wait to do the SPF calculation after receiving the first topology change. |
| `holdtime` | Configures the amount of time to wait between consecutive SPF calculations.| 
| `max-holdtime` | Configures the maximum amount of time to wait between consecutive SPF calculations. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router ospf timers spf delay

Configures the amount of time to wait to do the SPF calculation after receiving the first topology change. You can specify a value between 0 and 600000 milliseconds.

**Usage**

`nv set router ospf timers spf delay [options] 0-600000`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf delay 300000
```

## nv set router ospf timers spf holdtime

Configures the amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

**Usage**

`nv set router ospf timers spf holdtime [options] 0-600000`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf holdtime 300000
```

## nv set router ospf timers spf max-holdtime

Configures the maximum amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

**Usage**

`nv set router ospf timers spf max-holdtime [options] 0-600000`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf max-holdtime 300000
```

## nv set router ospf timers refresh 10-1800

Configures the refresh interval in seconds to resend LSAs to prevent them from aging out. You can specify a value between 10 and 1800 seconds.

**Usage**

`nv set router ospf timers refresh [options] 10-1800`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers refresh 100
```

## nv set router ospf enable

Turns OSPF on or off. 

**Usage**

`nv set router ospf enable [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf enable on
```

## nv set router ospf router-id

Configures the OSPF router ID on the switch, which is a 32-bit value and is typically the address of the loopback interface. This command configures the router ID for all VRFs if a common one is used; otherwise, you must set the router ID for every VRF.

**Usage**

`nv set router ospf router-id [options] (none|<ipv4>)`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router ospf router-id 10.10.10.1.
```

## nv set router pim

Configures PIM globally on the switch.

**Usage**

`nv set router pim [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `timers` | Configures PIM timers. |
| `enable` | Turns PIM feature on or off. |
| `packets` |Configures the number of incoming packets to process from the neighbor. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router pim timers

Configures PIM timers.

**Usage**

`nv set router pim timers [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `hello-interval` | Configures the interval in seconds at which the PIM router sends hello messages to discover PIM neighbors and maintain PIM neighbor relationships.  |
| `join-prune-interval` | The interval in seconds at which a PIM router sends join and prune messages to its upstream neighbors for a state update. |
| `keep-alive` |  Timeout value for S,G stream, in seconds. |
| `register-suppress` | The number of seconds during which to stop sending register messages to the RP. |
| `rp-keep-alive` | RP's timeout value, in seconds |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router pim timers hello-interval

Configures the interval in seconds at which the PIM router sends hello messages to discover PIM neighbors and maintain PIM neighbor relationships. You can specify a value between 1 and 180. The default setting is 30 seconds. 

**Usage**

`nv set router pim timers hello-interval [options] 1-180`

**Default Setting**

30 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pim timers hello-interval 60
```

## nv set router pim timers register-suppress

The number of seconds during which to stop sending register messages to the RP. You can specify a value between 5 and 60000 seconds.

**Usage**

`nv set router pim timers register-suppress [options] 5-60000`

**Default Setting**

60 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pim timers register-suppress 20000
```

## nv set router pim timers join-prune-interval

The interval in seconds at which a PIM router sends join and prune messages to its upstream neighbors for a state update. You can specify a value between 60 and 600 seconds.

**Usage**

`nv set router pim timers join-prune-interval [options] 60-600`

**Default Setting**

60 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pim timers join-prune-interval 100
```

## nv set router pim timers keep-alive

Configures the timeout value for the S,G stream in seconds. You can specify a value between 31 and 60000.

**Usage**

`nv set router pim timers keep-alive [options] 31-60000`

**Default Setting**

210 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pim timers keep-alive 10000
```

## nv set router pim timers rp-keep-alive

Configures the timeout value for the RP in seconds. You can specify a value between 31 and 60000.

**Usage**

`nv set router pim timers rp-keep-alive [options] 31-60000`

**Default Setting**

185 seconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pim timers rp-keep-alive 10000
```


## nv set router pim enable (on|off)

Turns PIM on or off.

**Usage**

`nv set router pim enable [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pim enable on
```

## nv set router pim packets

Configures the number of incoming packets from the neighbor that PIM can process. You can specify a value between 1 and 100.

**Usage**

`nv set router pim packets [options] 1-100`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router pim packets 50
```

## nv set router igmp

Configures IGMP globally on the switch.

**Usage**

`nv set router igmp [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns IGMP on or off.|

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router igmp enable

Turns IGMP on or off.

**Usage**

`nv set router igmp enable [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router igmp enable on
```

## nv set router vrrp

Configures VRRP globally on the switch.

**Usage**

`nv set router vrrp [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns VRRP on or off.|
| `advertisement-interval` | Configures the advertisement interval between successive advertisements by the master in a virtual router group. |
| `preempt` | Configures preempt mode, which lets the router take over as master for a virtual router group if it has a higher priority than the current master. |
| `priority` |  Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router vrrp enable

Turns VRRP on or off.

**Usage**

`nv set router vrrp enable [options] (on|off)`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router vrrp enable on
```

## nv set router vrrp priority

Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master.

**Usage**

`nv set router vrrp priority [options] 1-254`

**Default Setting**

100

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router vrrp priority 254
```

## nv set router vrrp preempt

Configures preempt mode, which lets the router take over as master for a virtual router group if it has a higher priority than the current master.

**Usage**

`nv set router vrrp preempt [options] (on|off)`

**Default Setting**

`on`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router vrrp preempt off
```

## nv set router vrrp advertisement-interval

Configures the advertisement interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950.

**Usage**

`nv set router vrrp advertisement-interval [options] 10-40950`

**Default Setting**

1000 milliseconds

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router vrrp advertisement-interval 2000
```

## nv set router vrr

Configures VRR globally on the switch.

**Usage**

`nv set router vrr [options] [<attribute> ...]`

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |   Turns VRR on or off. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set router vrr enable

Turns VRR on or off.

**Usage**

`nv set router vrr [options]  (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router vrr enable on
```

## nv set router adaptive-routing

Configures adaptive routing globally on the switch. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

**Usage**

`nv set router adaptive-routing [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` | Turns adaptive routing on or off. |

**Version History**

Introduced in Cumulus Linux 5.1.0

## nv set router adaptive-routing enable

Turns adaptive routing on or off.

**Usage**

`nv set router adaptive-routing [options] (on|off)`

**Default Setting**

`off`

**Version History**

Introduced in Cumulus Linux 5.1.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set router adaptive-routing enable on
```

## nv set platform

Configures the switch platform settings.

**Usage**

`nv set platform [options] [<attribute> ...]`

**Default Setting**

`off`

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `hardware` | Configures the switch hardware components. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware

Configures the hardware components of the switch. 

**Usage**

`nv set platform hardware [options] [<attribute> ...]`

**Default Setting**

N/A

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `component` | Configures a hardware component on the switch. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware component \<component-id\>

Configures a hardware component on the switch.

**Usage**

`nv set platform hardware component <component-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `linecard` | Configures the properties of a line card. |
| `admin-state` | Configures the admin state of the hardware component. |
| `type` | Configures the conponent type. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware component \<component-id\> linecard

Configures the properties of a line card.

**Usage**

`nv set platform hardware component <component-id> linecard [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `provision`  | Configures the provision line card type. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set platform hardware component \<component-id\> linecard provision

Configures the properties of a line card. You can specify 16x100GE, 4x400GE, 8x200GE, or NONE.

**Usage**

`nv set platform hardware component <component-id> linecard provision [options] (16x100GE|4x400GE|8x200GE|NONE)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set platform hardware component device linecard provision 4x400GE 
```

## nv set platform hardware component \<component-id\> type

Configures the conponent type; the switch or a line card.

**Usage**

`nv set platform hardware component <component-id> type [options] (switch|linecard)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set platform hardware component device type linecard
```

## nv set platform hardware component \<component-id\> admin-state

Configures the admin state of the hardware component. You can specify enable or disable.

**Usage**

`nv set platform hardware component <component-id> admin-state [options] (enable|disable)`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<component-id>` | The hardware component you want to configure.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set platform hardware component device admin-state enable
```

## nv set bridge

Configures a bridge on the switch.

**Usage**

`nv set bridge [options] [<attribute> ...]`

**Default Setting**

`br_default`

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain` |  Configures the bridge domain. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\>

Configures the bridge domain.

**Usage**

`nv set bridge domain <domain-id> [options] [<attribute> ...]`

**Default Setting**

`br_default`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
| `<domain-id>` |  The name of the bridge domain. |

**Attributes**

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

**Version History**

Introduced in Cumulus Linux 5.0.0 

## nv set bridge domain \<domain-id\> stp


**Usage**

`nv set bridge domain <domain-id> stp [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `state` |  Configures the STP state on the bridge domain; down or up.|
| `priority` | Configures the spanning tree priority. The bridge with the lowest priority is the root bridge. You must specify a value between 4096 and 32768. The value must be a multiple of 4096. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> stp priority

Configures the spanning tree priority. The bridge with the lowest priority is the root bridge. The priority must be a number between 0 and 61440, and must be a multiple of 4096.
 
**Usage**

`nv set bridge domain <domain-id> stp priority [options] 4096-61440`

**Default Setting**

32768

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default stp priority 8192
```

## nv set bridge domain \<domain-id\> multicast

Configures multicast on the bridge domain.

**Usage**

`nv set bridge domain <domain-id> multicast [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `snooping` |  Configures IGMP and MLD snooping.|

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> multicast snooping

Configures IGMP and MLD snooping to prevent hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments and MLD snooping is for IPv6 environments.

**Usage**

`nv set bridge domain <domain-id> multicast snooping [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `querier`|  Configures the IGMP and MLD querier. |
| `enable` | Turns IGMP and MLD snooping on or off. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain \<domain-id\> multicast snooping querier

Configures the IGMP and MLD querier. Without a multicast router, a single switch in an IP subnet can coordinate multicast traffic flows. This switch is the querier or the designated router. The querier generates query messages to check group membership, and processes membership reports and leave messages.

**Usage**

`nv set bridge domain <domain-id> multicast snooping querier [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `enable` |  Turns the multicast querier on or off.|

**Version History**

Introduced in Cumulus Linux 5.0.0


## nv set bridge domain \<domain-id\> multicast snooping querier enable

Turns the multicast querier on or off.

**Usage**

`nv set bridge domain <domain-id> multicast snooping querier enable [options] (on|off)`

**Default Setting**

`off`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default multicast snooping querier enable on
```

## nv set bridge domain \<domain-id\> multicast snooping enable

Turns IGMP and MLD snooping on or off.

**Usage**

`nv set bridge domain <domain-id> multicast snooping enable [options] (on|off)`


**Default Setting**

`off`

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default multicast snooping enable on
```

## nv set bridge domain \<domain-id\> vlan \<vid\>

Configures the VLAN tag identifier.

**Usage**

`nv set bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |
| `<vid>`   |  The VLAN identifier.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `vni` |  Configures a layer 2 VNI. |
| `ptp` |  Configures the VLAN PTP configuration. This is inherited by the interfaces in this VLAN.|
| `multicast` |  Configures multicast on the VLAN.|

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10
```

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\>

Maps a VLAN to a VNI.

**Usage**

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `flooding`  |  Configures how to handle BUM traffic.|
| `mac-learning` | Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs). You can override this setting with VNI-specific configuration. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
nv set bridge domain br_default vlan 10 vni 10
```

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding

Configures how to handle BUM traffic.

**Usage**

`nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]`

**Default Setting**

N/A

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |
| `head-end-replication` |  Configures replication of BUM traffic where individual copies send to remote destinations.|
| `enable` | Turns flooding on or off, or sets flooding to auto.|
| `multicast-group` | Configures BUM traffic to go to the specified multicast group where receivers who are interested in that group receive the traffic. This usually requires you to use PIM-SM in the network. |

**Version History**

Introduced in Cumulus Linux 5.0.0

## nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>

**Usage**

  nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]



  Set of IPv4 unicast addresses or "evpn".

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID
  <hrep-id>    IPv4 unicast addresses or "evpn"

## nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group <ipv4-multicast>

**Usage**

  nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group [options] <ipv4-multicast>



  BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID

## nv set bridge domain <domain-id> vlan <vid> ptp

**Usage**

  nv set bridge domain <domain-id> vlan <vid> ptp [options] [<attribute> ...]



  VLAN PTP configuration.  Inherited by interfaces in this VLAN.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain
  <vid>        VLAN ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

## nv set bridge domain <domain-id> vlan <vid> multicast

**Usage**

  nv set bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]



  Configure multicast on the vlan

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain
  <vid>        VLAN ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  snooping     IGMP/MLD snooping configuration

## nv set bridge domain <domain-id> vlan <vid> multicast snooping

**Usage**

  nv set bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]



  IGMP/MLD snooping configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain
  <vid>        VLAN ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  querier      IGMP/MLD querier configuration

## nv set bridge domain <domain-id> vlan <vid> multicast snooping querier

**Usage**

  nv set bridge domain <domain-id> vlan <vid> multicast snooping querier [options] [<attribute> ...]



  IGMP/MLD querier configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain
  <vid>        VLAN ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  source-ip    Source IP to use when sending IGMP/MLD queries.

## nv set bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip <ipv4>

**Usage**

  nv set bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip [options] <ipv4>



  Source IP to use when sending IGMP/MLD queries.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain
  <vid>        VLAN ID

## nv set bridge domain <domain-id> type vlan-aware

**Usage**

  nv set bridge domain <domain-id> type [options] vlan-aware



  Type of bridge domain.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain

## nv set bridge domain <domain-id> encap 802.1Q

**Usage**

  nv set bridge domain <domain-id> encap [options] 802.1Q



  Interfaces added to this domain will, by default, use this encapsulation.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain

## nv set bridge domain <domain-id> vlan-vni-offset 0-16773120

**Usage**

  nv set bridge domain <domain-id> vlan-vni-offset [options] 0-16773120



  A VNI offset while (automatically) mapping VLANs to VNIs

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <domain-id>  Domain

## nv set mlag

**Usage**

  nv set mlag [options] [<attribute> ...]



  Global Multi-chassis Link Aggregation properties

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  lacp-conflict  Configure the mlag lacp-conflict parameters

  backup         Set of MLAG backups

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  debug          Enable MLAG debugging

  init-delay     The delay, in seconds, before bonds are brought up.

  mac-address    Override anycast-mac and anycast-id

  peer-ip        Peer Ip Address

  priority       Mlag Priority

## nv set mlag lacp-conflict

**Usage**

  nv set mlag lacp-conflict [options]



  Configure the mlag lacp-conflict parameters

## nv set mlag backup <backup-ip>

**Usage**

  nv set mlag backup <backup-ip> [options] [<attribute> ...]



  alternative ip address or interface for peer to reach us

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <backup-ip>  Backup IP of MLAG peer

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  vrf          The backup IP's VRF.

## nv set mlag backup <backup-ip> vrf <vrf-name>

**Usage**

  nv set mlag backup <backup-ip> vrf [options] <vrf-name>



  The backup IP's VRF.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <backup-ip>  Backup IP of MLAG peer

## nv set mlag priority 0-65535

**Usage**

  nv set mlag priority [options] 0-65535



  Mlag Priority

## nv set mlag init-delay 0-900

**Usage**

  nv set mlag init-delay [options] 0-900



  The delay, in seconds, before bonds are brought up.

## nv set evpn

**Usage**

  nv set evpn [options] [<attribute> ...]



  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-advertise  Route advertising

  dad              Advertise

  evi              EVI

  multihoming      Multihoming global configuration parameters

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

## nv set evpn route-advertise

**Usage**

  nv set evpn route-advertise [options] [<attribute> ...]



  Route dvertising

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  default-gateway  This configuration should be turned 'on' only in a centralized-routing deployment and only on the centralized GW router(s). If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes with the gateway extended community. The purpose is for remote L2-only VTEPs to do  ARP suppression and for hosts to learn of the gateway's IP to MAC binding.

  nexthop-setting  Specifies the next hop IP and MAC (Router MAC) to use in the advertisement of type-5 routes and “self” type-2 routes (“self” = SVI IP/MAC). Relevant only in an MLAG configuration.

  svi-ip           If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes. This configuration should not be enabled if SVI IPs are reused in the network.

## nv set evpn dad

**Usage**

  nv set evpn dad [options] [<attribute> ...]



  Duplicate address detection

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  duplicate-action    Action to take when a MAC is flagged as a possible duplicate. If 'warning-only', generates a log message. If 'freeze', further move events for the MAC will not be acted upon.

  enable              Turn the feature 'on' or 'off'. The default is 'off'.

  mac-move-threshold  Number of MAC moves within a time window before the MAC is flagged as a possible duplicate.

  move-window         Time window during which the move threshold applies

## nv set evpn dad duplicate-action

**Usage**

  nv set evpn dad duplicate-action [options] [<attribute> ...]



  Handling of BUM traffic

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  freeze      Further move events for the MAC will not be acted upon.

## nv set evpn dad duplicate-action freeze

**Usage**

  nv set evpn dad duplicate-action freeze [options] [<attribute> ...]



  Advertise

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  duration    Freeze the MAC for the specified duration or, if 'permanent'

              until the operator intervenes.

## nv set evpn dad mac-move-threshold 2-1000

**Usage**

  nv set evpn dad mac-move-threshold [options] 2-1000



  Number of MAC moves within a time window before the MAC is flagged as a possible duplicate.

## nv set evpn dad move-window 2-1800

**Usage**

  nv set evpn dad move-window [options] 2-1800



  Time window during which the move threshold applies

## nv set evpn evi <evi-id>

**Usage**

  nv set evpn evi <evi-id> [options] [<attribute> ...]



  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <evi-id>         VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-advertise  Route advertise

  route-target     Route targets

  rd               BGP Route Distinguisher to use for EVPN type-5 routes

                   originated for this VRF.

## nv set evpn evi <evi-id> route-advertise

**Usage**

  nv set evpn evi <evi-id> route-advertise [options] [<attribute> ...]



  Route advertise

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <evi-id>         VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  default-gateway  If 'auto', inherit from global config. This is the default. This configuration should be turned 'on' only in a centralized-routing deployment and only on the centralized GW router(s). If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes with the gateway extended community. The purpose is for remote L2-only VTEPs to do ARP suppression and for hosts to learn of the gateway's IP to MAC binding.

  svi-ip           If 'auto', inherit from global config. This is the default. If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes. This configuration should not be enabled if SVI IPs are reused in the network.

## nv set evpn evi <evi-id> route-target

**Usage**

  nv set evpn evi <evi-id> route-target [options] [<attribute> ...]



  EVPN control plane config and info for VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <evi-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  export      Route targets to export

  import      Route targets to import

  both        Route targets to import and export

## nv set evpn evi <evi-id> route-target export <rt-id>

**Usage**

  nv set evpn evi <evi-id> route-target export <rt-id> [options]



  A route target identifier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <evi-id>    VRF
  <rt-id>     Route target ID

## nv set evpn evi <evi-id> route-target import <rt-id>

**Usage**

  nv set evpn evi <evi-id> route-target import <rt-id> [options]



  A route target identifier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <evi-id>    VRF
  <rt-id>     Route target ID

## nv set evpn evi <evi-id> route-target both <rt-id>

**Usage**

  nv set evpn evi <evi-id> route-target both <rt-id> [options]



  A route target identifier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <evi-id>    VRF
  <rt-id>     Route target ID

## nv set evpn multihoming

**Usage**

  nv set evpn multihoming [options] [<attribute> ...]



  Multihoming global configuration parameters

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ead-evi-route      Ethernet Auto-discovery per EVPN instance routes

  segment            Multihoming interface segment

  enable             Turn the feature 'on' or 'off'. The default is 'off'.

  mac-holdtime       During this interval, the switch attempts to independently establish reachability of the MAC on the local ethernet segment. If 'none', there is no holdtime.

  neighbor-holdtime  During this interval, the switch attempts to independently establish reachability of the host on the local ethernet segment.

  startup-delay      The duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or  process restart.

## nv set evpn multihoming ead-evi-route

**Usage**

  nv set evpn multihoming ead-evi-route [options] [<attribute> ...]



  Ethernet Auto-discovery per EVPN instance routes

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  rx          Disable EAD-per-EVI at receiving end.

  tx          Suppress advertisement of EAD-per-EVI routes.

## nv set evpn multihoming segment

**Usage**

  nv set evpn multihoming segment [options] [<attribute> ...]



  Multihoming interface segment

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  df-preference  Designated forwarder preference value.

  mac-address    MAC address per ethernet segment. Required.

## nv set evpn multihoming segment mac-address <mac>

**Usage**

  nv set evpn multihoming segment mac-address [options] <mac>



  MAC address per ethernet segment.  Required.

## nv set evpn multihoming segment df-preference 1-65535

**Usage**

  nv set evpn multihoming segment df-preference [options] 1-65535



  Designated forwarder preference value.

## nv set evpn multihoming mac-holdtime 0-86400

**Usage**

  nv set evpn multihoming mac-holdtime [options] 0-86400



  During this interval, the switch attempts to independently establish reachability of the MAC on the local ethernet segment. If 'none', there is no holdtime.

## nv set evpn multihoming neighbor-holdtime 0-86400

**Usage**

  nv set evpn multihoming neighbor-holdtime [options] 0-86400



  During this interval, the switch attempts to independently establish reachability of the host on the local ethernet segment.

## nv set evpn multihoming startup-delay 0-3600

**Usage**

  nv set evpn multihoming startup-delay [options] 0-3600



  The duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart.

## nv set qos

**Usage**

  nv set qos [options] [<attribute> ...]



  QOS

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  roce        Properties associated with the RDMA over Converged Ethernet (RoCE) feature.

## nv set qos roce

**Usage**

  nv set qos roce [options] [<attribute> ...]



  Properties associated with the RDMA over Converged Ethernet (RoCE) feature.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable        Turn the feature 'on' or 'off'. The default is 'off'.

  mode          Roce Mode

  cable-length  Cable Length(in meters) for Roce Lossless Config

## nv set qos roce cable-length 1-100000

**Usage**

  nv set qos roce cable-length [options] 1-100000



  Cable Length(in meters) for Roce Lossless Config

## nv set interface <interface-id>

**Usage**

  nv set interface <interface-id> [options] [<attribute> ...]



  An interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  router          interface router

  bond            The state of the interface

  bridge          attributed related to a bridged interface

  ip              IP configuration for an interface

  lldp            LLDP on for an interface

  link            An physical interface

  evpn            EVPN control plane config and info for VRF

  acl             Interface ACL rules

  ptp             Interface Specific PTP configuration.

  tunnel          The state of the interface

  base-interface  The interface under this interface

  description     Details about the interface

  type            The type of interface

  vlan            VLAN ID

## nv set interface <interface-id> router

**Usage**

  nv set interface <interface-id> router [options] [<attribute> ...]



  interface router

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>    Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  pbr               PBR interface configuration.

  ospf              OSPF interface configuration.

  pim               PIM interface configuration.

  adaptive-routing  Adaptive routing interface configuration.

## nv set interface <interface-id> router pbr

**Usage**

  nv set interface <interface-id> router pbr [options] [<attribute> ...]



  PBR interface configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  map             PBR map to use on this interface

## nv set interface <interface-id> router pbr map <pbr-map-id>

**Usage**

  nv set interface <interface-id> router pbr map <pbr-map-id> [options]



  Interface Pbr map

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <pbr-map-id>    Route Map ID

## nv set interface <interface-id> router ospf

**Usage**

  nv set interface <interface-id> router ospf [options] [<attribute> ...]



  OSPF interface configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  timers          Timers configuration

  authentication  md5 authentication configuration

  bfd             BFD configuration

  enable          Turn the feature 'on' or 'off'. The default is 'off'.

  area            Area number for enabling ospf on this interface.

  cost            The cost of this link the router lsa. If `auto`, determine

                  the cost based on link speed. This is the default.

  mtu-ignore      Do not test mtu matching for peering.

  network-type    Network type.

  passive         Stops the creation of peers on this interface

  priority        Eligibility of this router to become DR on multi-access network

## nv set interface <interface-id> router ospf timers

**Usage**

  nv set interface <interface-id> router ospf timers [options] [<attribute> ...]



  Timers configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>       Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  dead-interval        Length of time, in seconds, without a hello before  declaring the neighbor dead. If `minimal`, `hello-multiplier` must be set.

  hello-interval       How often to transmit a hello packet, in seconds. Only valid if `dead-interval` is not `minimal`.

  hello-multiplier     Required and only valid if `dead-interval` is `minimal`.

  retransmit-interval  How often to retransmit a packet not acknowledged, in seconds

  transmit-delay       Delay before sending a new lsa, in seconds

## nv set interface <interface-id> router ospf timers hello-multiplier 1-10

**Usage**

  nv set interface <interface-id> router ospf timers hello-multiplier [options] 1-10



  Required and only valid if `dead-interval` is `minimal`.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf timers hello-interval 1-65535

**Usage**

  nv set interface <interface-id> router ospf timers hello-interval [options] 1-65535



  How often to transmit a hello packet, in seconds.  Only valid if `dead-interval` is not `minimal`.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf timers retransmit-interval 1-65535

**Usage**

  nv set interface <interface-id> router ospf timers retransmit-interval [options] 1-65535



  How often to retransmit a packet not acknowledged, in seconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf timers transmit-delay 1-65535

**Usage**

  nv set interface <interface-id> router ospf timers transmit-delay [options] 1-65535



  Delay before sending a new lsa, in seconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf authentication

**Usage**

  nv set interface <interface-id> router ospf authentication [options] [<attribute> ...]



  md5 authentication configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>      Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable              Turn the feature 'on' or 'off'. The default is 'off'.

  md5-key             md5 key

  message-digest-key  Message digest key

## nv set interface <interface-id> router ospf authentication message-digest-key 1-255

**Usage**

  nv set interface <interface-id> router ospf authentication message-digest-key [options] 1-255



  Message digest key

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf authentication md5-key <value>

**Usage**

  nv set interface <interface-id> router ospf authentication md5-key [options] <value>



  md5 key

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf bfd

**Usage**

  nv set interface <interface-id> router ospf bfd [options] [<attribute> ...]



  BFD configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>        Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  detect-multiplier     Detect multiplier value

  min-receive-interval  Minimum receive interval in milliseconds

  min-transmit-interval  Minimum transmit interval in milliseconds

## nv set interface <interface-id> router ospf bfd detect-multiplier 2-255

**Usage**

  nv set interface <interface-id> router ospf bfd detect-multiplier [options] 2-255



  Detect multiplier value

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf bfd min-receive-interval 50-60000

**Usage**

  nv set interface <interface-id> router ospf bfd min-receive-interval [options] 50-60000



  Minimum receive interval in milliseconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf bfd min-transmit-interval 50-60000

**Usage**

  nv set interface <interface-id> router ospf bfd min-transmit-interval [options] 50-60000



  Minimum transmit interval in milliseconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router ospf priority 0-255

**Usage**

  nv set interface <interface-id> router ospf priority [options] 0-255



  Eligibility of this router to become DR on multi-access network

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router pim

**Usage**

  nv set interface <interface-id> router pim [options] [<attribute> ...]



  PIM interface configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  timers          Timers

  bfd             BFD configuration

  address-family  Address family specific configuration

  enable          Turn the feature 'on' or 'off'. The default is 'off'.

  active-active   Enable/disable active-active for PIM MLAG operation on the

                  interface.

  dr-priority     Designated Router Election priority.

## nv set interface <interface-id> router pim timers

**Usage**

  nv set interface <interface-id> router pim timers [options] [<attribute> ...]



  Timers

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  hello-interval  PIM Hello packets periodic interval. If "auto", inherit from the VRF. This is the default. Holdtime is 3.5 times the hello-interval, the amount of time neighbor must kept in reachable state.

## nv set interface <interface-id> router pim bfd

**Usage**

  nv set interface <interface-id> router pim bfd [options] [<attribute> ...]



  BFD configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>        Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  detect-multiplier     Detect multiplier value

  min-receive-interval  Minimum receive interval in milliseconds

  min-transmit-interval Minimum transmit interval in milliseconds

## nv set interface <interface-id> router pim bfd detect-multiplier 2-255

**Usage**

  nv set interface <interface-id> router pim bfd detect-multiplier [options] 2-255



  Detect multiplier value

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router pim bfd min-receive-interval 50-60000

**Usage**

  nv set interface <interface-id> router pim bfd min-receive-interval [options] 50-60000



  Minimum receive interval in milliseconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router pim bfd min-transmit-interval 50-60000

**Usage**

  nv set interface <interface-id> router pim bfd min-transmit-interval [options] 50-60000



  Minimum transmit interval in milliseconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router pim address-family

**Usage**

  nv set interface <interface-id> router pim address-family [options] [<attribute> ...]



  Address family specific configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ipv4-unicast    IPv4 unicast address family

## nv set interface <interface-id> router pim address-family ipv4-unicast

**Usage**

  nv set interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]



  IPv4 unicast address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>        Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  allow-rp              Allow RP feature, which allows RP address to be accepts for the received

  multicast-boundary-oil  PIM join/prunes are accepted or dropped based upon the prefix-list filter apply on outgoing filter list on  the specified interface.

  use-source            Use unique source address in PIM Hello source field.

## nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp

**Usage**

  nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp [options] [<attribute> ...]



  Allow RP feature, which allows RP address to be accepts for the received

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable          Turn the feature 'on' or 'off'. The default is 'off'.

  rp-list         The prefix-list provides the list of group addresses to

                  accept downstream (*,G) joins and propogate towards the

                  allowed-rp.

## nv set interface <interface-id> router pim dr-priority 1-4294967295

**Usage**

  nv set interface <interface-id> router pim dr-priority [options] 1-4294967295



  Designated Router Election priority.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> router adaptive-routing

**Usage**

  nv set interface <interface-id> router adaptive-routing [options] [<attribute> ...]



  Adaptive routing interface configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>        Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  link-utilization-threshold  Link utilization threshold percentage

## nv set interface <interface-id> router adaptive-routing link-utilization-threshold 1-100

**Usage**

  nv set interface <interface-id> router adaptive-routing link-utilization-threshold [options] 1-100



  Link utilization threshold percentage

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> bond

**Usage**

  nv set interface <interface-id> bond [options] [<attribute> ...]



  The state of the interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  member          Set of bond members

  mlag            MLAG configuration on the bond interface

  down-delay      bond down delay

  lacp-bypass     lacp bypass

  lacp-rate       lacp rate

  mode            bond mode

  up-delay        bond up delay

## nv set interface <interface-id> bond member <member-id>

**Usage**

  nv set interface <interface-id> bond member <member-id> [options]



  A bond member

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <member-id>     Bond memer interface

## nv set interface <interface-id> bond mlag

**Usage**

  nv set interface <interface-id> bond mlag [options] [<attribute> ...]



  MLAG configuration on the bond interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  lacp-conflict   Configure the mlag lacp-conflict parameters

  enable          Turn the feature 'on' or 'off'. The default is 'off'.

  id              MLAG id

## nv set interface <interface-id> bond mlag lacp-conflict

**Usage**

  nv set interface <interface-id> bond mlag lacp-conflict [options]



  Configure the mlag lacp-conflict parameters

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> bond down-delay 0-65535

**Usage**

  nv set interface <interface-id> bond down-delay [options] 0-65535



  bond down delay

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> bond up-delay 0-65535

**Usage**

  nv set interface <interface-id> bond up-delay [options] 0-65535



  bond up delay

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> bridge

**Usage**

  nv set interface <interface-id> bridge [options] [<attribute> ...]



  attributed related to a bridged interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  domain          Bridge domains on this interface

## nv set interface <interface-id> bridge domain <domain-id>

**Usage**

  nv set interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]



  Bridge domain on this interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <domain-id>     Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  stp             attributed related to a stpd interface

  vlan            Set of allowed vlans for this bridge domain on this interface. If "all", inherit all vlans from the bridge domain, if appropriate. This is the default.

  access          Untagged packets ingressing on this interface will be put in this vlan. Tagged packets will be dropped. Egress packets will be untagged. If auto, inherit from bridge domain.

  learning        source mac address learning for this bridge domain on this interface

  untagged        Untagged packets ingressing on the interface will be put in this vlan. Egress packets are always tagged. If none, then untagged packets will be dropped. If auto, inherit from bridge domain.

## nv set interface <interface-id> bridge domain <domain-id> stp

**Usage**

  nv set interface <interface-id> bridge domain <domain-id> stp [options] [<attribute> ...]



  attributed related to a stpd interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <domain-id>     Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  admin-edge      Edge state of the port

  auto-edge       Auto transition to/from edge state of the port

  bpdu-filter     BPDU filter on a port

  bpdu-guard      Bridge Protocol Data Unit guard

  network         Bridge assurance capability for a port

  restrrole       enable/disable port ability to take root role of the port (need better name)

## nv set interface <interface-id> bridge domain <domain-id> vlan <vid>

**Usage**

  nv set interface <interface-id> bridge domain <domain-id> vlan <vid> [options]



  A VLAN tag identifier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <domain-id>     Domain
  <vid>           VLAN ID, or all

## nv set interface <interface-id> ip

**Usage**

  nv set interface <interface-id> ip [options] [<attribute> ...]



  IP configuration for an interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>      Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  address             ipv4 and ipv6 address

  vrr                 Configuration for VRR

  gateway             default ipv4 and ipv6 gateways

  ipv4                IPv4 configuration for an interface

  ipv6                IPv6 configuration for an interface

  igmp                Configuration for IGMP

  vrrp                Configuration for VRRP

  neighbor-discovery  Neighbor discovery configuration for an interface

  vrf                 Virtual routing and forwarding

## nv set interface <interface-id> ip address <ip-prefix-id>

**Usage**

  nv set interface <interface-id> ip address <ip-prefix-id> [options]



  An IP address with prefix

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip vrr

**Usage**

  nv set interface <interface-id> ip vrr [options] [<attribute> ...]



  Configuration for VRR

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  address         Virtual addresses with prefixes

  state           The state of the interface

  enable          Turn the feature 'on' or 'off'. The default is 'off'.

  mac-address     Override anycast-mac

  mac-id          Override fabric-id

## nv set interface <interface-id> ip vrr address <ip-prefix-id>

**Usage**

  nv set interface <interface-id> ip vrr address <ip-prefix-id> [options]



  An IP address with prefix

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip gateway <ip-address-id>

**Usage**

  nv set interface <interface-id> ip gateway <ip-address-id> [options]



  An IP address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>   Interface
  <ip-address-id>  IPv4 or IPv6 address

## nv set interface <interface-id> ip ipv4

**Usage**

  nv set interface <interface-id> ip ipv4 [options] [<attribute> ...]



  IPv4 configuration for an interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  forward         Enable or disable forwarding.

## nv set interface <interface-id> ip ipv6

**Usage**

  nv set interface <interface-id> ip ipv6 [options] [<attribute> ...]



  IPv6 configuration for an interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable          Turn the feature 'on' or 'off'. The default is 'on'.

  forward         Enable or disable forwarding.

## nv set interface <interface-id> ip igmp

**Usage**

  nv set interface <interface-id> ip igmp [options] [<attribute> ...]



  Configuration for IGMP

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>        Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  static-group          IGMP static mutlicast mroutes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  last-member-query-interval Last member query interval.

  query-interval        Query interval, in seconds.

  query-max-response-time  Max query response time, in seconds.

  version               Protocol version

## nv set interface <interface-id> ip igmp static-group <static-group-id>

**Usage**

  nv set interface <interface-id> ip igmp static-group <static-group-id> [options] [<attribute> ...]



  IGMP static multicast mroute

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>     Interface
  <static-group-id>  IGMP static multicast mroute destination

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  source-address     IGMP static multicast mroute source.

## nv set interface <interface-id> ip igmp static-group <static-group-id> source-address <ipv4-unicast>

**Usage**

  nv set interface <interface-id> ip igmp static-group <static-group-id> source-address [options] <ipv4-unicast>



  IGMP static multicast mroute source.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>     Interface
  <static-group-id>  IGMP static multicast mroute destination

## nv set interface <interface-id> ip igmp query-interval 1-1800

**Usage**

  nv set interface <interface-id> ip igmp query-interval [options] 1-1800



  Query interval, in seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip igmp query-max-response-time 10-250


**Usage**

  nv set interface <interface-id> ip igmp query-max-response-time [options] 10-250



  Max query response time, in seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip igmp last-member-query-interval 1-255

**Usage**

  nv set interface <interface-id> ip igmp last-member-query-interval [options] 1-255



  Last member query interval.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip vrrp

**Usage**

  nv set interface <interface-id> ip vrrp [options] [<attribute> ...]



  Configuration for VRRP

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  virtual-router  Group of virtual gateways implemented with VRRP

  enable          Turn the feature 'on' or 'off'. The default is 'off'.

## nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id>

**Usage**

  nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]



  A virtual gateway implemented with VRRP

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>        Interface
  <virtual-router-id>   Virtual Router IDentifier (VRID)

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  address               A set of virtual addresses for VRRPv3

  advertisement-interval Sets the interval between successive VRRP advertisements -- RFC 5798 defines this as a 12-bit value expressed as 0.1 seconds, with default 1000 milliseconds, i.e., 1 second. Represented in units of milliseconds

  preempt               When set to true, enables preemption by a higher priority backup router of a lower priority master router

  priority              Specifies the sending VRRP interface's priority foe the virtual router. Higher values equal higher priority

  version               Protocol version

## nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>

**Usage**

  nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]



  An IP address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>       Interface
  <virtual-router-id>  Virtual Router IDentifier (VRID)
  <ip-address-id>      IPv4 or IPv6 address

## nv set interface <interface-id> ip neighbor-discovery

**Usage**

  nv set interface <interface-id> ip neighbor-discovery [options] [<attribute> ...]



  Neighbor discovery configuration for an interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>        Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  rdnss                 Recursive DNS server addresses to be advertised using

                        type 25 option RFC8016

  prefix                IPv6 prefix configuration

  dnssl                 Advertise DNS search list using type 31 option RFC8106

  router-advertisement  Router advertisement

  home-agent            Home agent configuration

  enable                Turn the feature 'on' or 'off'. The default is 'on'.

  mtu                   MTU option for neighbor discovery messages

## nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>

**Usage**

  nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> [options] [<attribute> ...]



  A recursive DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>     Interface
  <ipv6-address-id>  IPv6 address

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  lifetime           Maximum time in seconds for which the server may be used for domain name resolution

## nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>

**Usage**

  nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> [options] [<attribute> ...]



  A IPv6 prefix

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>      Interface
  <ipv6-prefix-id>    IPv6 address and route prefix in CIDR notation

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  autoconfig          Indicates to hosts on the local link that the specified  prefix can be used for v6 autoconfiguration

  off-link            Indicates that adverisement makes no statement about on-link or off-link properties of the prefix

  preferred-lifetime  Time in seconds that addresses generated from a prefix remain preferred

  router-address      Indicates to hosts on the local link that the specified prefix contains a complete IP address by setting R flag

  valid-lifetime      Time in seconds the prefix is valid for on-link determination

## nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime 0-4294967295

**Usage**

  nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime [options] 0-4294967295



  Time in seconds the prefix is valid for on-link determination

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime 0-4294967295

**Usage**

  nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime [options] 0-4294967295



  Time in seconds that addresses generated from a prefix remain preferred

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>

**Usage**

  nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> [options] [<attribute> ...]



  A DNS search list

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>    Interface
  <domain-name-id>  The domain portion of a hostname (RFC 1123) or an
                    internationalized hostname (RFC 5890).

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  lifetime          Maximum time in seconds for which the domain suffix may be used for domain name resolution

## nv set interface <interface-id> ip neighbor-discovery router-advertisement

**Usage**

  nv set interface <interface-id> ip neighbor-discovery router-advertisement [options] [<attribute> ...]



  Router advertisement configuration for an interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>     Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable             Turn the feature 'on' or 'off'. The default is 'on'.

  fast-retransmit    Allow consecutive RA packets more frequently than every 3  seconds

  hop-limit          Value in hop count field in IP header of the outgoing router advertisement packet

  interval           Maximum time in milliseconds allowed between sending unsolicited multicast RA from the interface

  interval-option    Indicates hosts that the router will use advertisement interval to send router advertisements

  lifetime           Maximum time in seconds that the router can be treated as default gateway

  managed-config     Knob to allow dynamic host to use managed (stateful) protocol for address autoconfiguration in addition to any addresses autoconfigured using stateless address autoconfig

  other-config       Knob to allow dynamic host to use managed (stateful) protocol for autoconfiguration information other than  addresses

  reachable-time     Time in milliseconds that a IPv6 node is considered reachable

  retransmit-time    Time in milliseconds between retransmission of neighbor solicitation messages

  router-preference  Hosts use router preference in selection of the default router

## nv set interface <interface-id> ip neighbor-discovery router-advertisement interval 70-1800000

**Usage**

  nv set interface <interface-id> ip neighbor-discovery router-advertisement interval [options] 70-1800000



  Maximum time in milliseconds allowed between sending unsolicited multicast RA from the interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime 0-9000

**Usage**

  nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime [options] 0-9000



  Maximum time in seconds that the router can be treated as default gateway

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time 0-3600000

**Usage**

  nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time [options] 0-3600000



  Time in milliseconds that a IPv6 node is considered reachable

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time 0-4294967295


**Usage**

  nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time [options] 0-4294967295



  Time in milliseconds between retransmission of neighbor solicitation messages

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit 0-255

**Usage**

  nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit [options] 0-255



  Value in hop count field in IP header of the outgoing router advertisement packet

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery home-agent

**Usage**

  nv set interface <interface-id> ip neighbor-discovery home-agent [options] [<attribute> ...]



  Indicates to neighbors that this router acts as a Home Agent and includes a Home Agent Option. Not defined by default

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  lifetime        Lifetime of a home agent in seconds

  preference      Home agent's preference value that is used to order the  addresses returned in the home agent address discovery reply.

## nv set interface <interface-id> ip neighbor-discovery home-agent lifetime 0-65520

**Usage**

  nv set interface <interface-id> ip neighbor-discovery home-agent lifetime [options] 0-65520



  Lifetime of a home agent in seconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery home-agent preference 0-65535

**Usage**

  nv set interface <interface-id> ip neighbor-discovery home-agent preference [options] 0-65535



  Home agent's preference value that is used to order the addresses returned in the home agent address discovery reply.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery mtu 1-65535

**Usage**

  nv set interface <interface-id> ip neighbor-discovery mtu [options] 1-65535



  MTU option for neighbor discovery messages

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ip vrf <vrf-name>

**Usage**

  nv set interface <interface-id> ip vrf [options] <vrf-name>



  Virtual routing and forwarding

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> lldp

**Usage**

  nv set interface <interface-id> lldp [options] [<attribute> ...]



  LLDP on for an interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>       Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  dcbx-ets-config-tlv  DCBX ETS config TLV flag

  dcbx-ets-recomm-tlv  DCBX ETS recommendation TLV flag

  dcbx-pfc-tlv         DCBX PFC TLV flag

## nv set interface <interface-id> link

**Usage**

  nv set interface <interface-id> link [options] [<attribute> ...]



  An physical interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  state           The state of the interface

  dot1x           An physical interface

  auto-negotiate  Link speed and characteristic auto negotiation

  breakout        sub-divide or disable ports (only valid on plug interfaces)

  duplex          Link duplex

  fec             Link forward error correction mechanism

  mtu             interface mtu

  speed           Link speed

## nv set interface <interface-id> link dot1x

**Usage**

  nv set interface <interface-id> link dot1x [options] [<attribute> ...]



  An physical interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  mab             bypass MAC authentication

  parking-vlan    VLAN for unauthorized MAC addresses

## nv set interface <interface-id> link mtu 552-9216

**Usage**

  nv set interface <interface-id> link mtu [options] 552-9216



  interface mtu

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> evpn

**Usage**

  nv set interface <interface-id> evpn [options] [<attribute> ...]



  EVPN control plane config and info for VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  multihoming     Multihoming interface configuration parameters

## nv set interface <interface-id> evpn multihoming

**Usage**

  nv set interface <interface-id> evpn multihoming [options] [<attribute> ...]



  Multihoming interface configuration parameters

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  segment         Multihoming interface segment

  uplink          Enable evpn multihoming tracking to prevent traffic loss due to NVE connectivity loss, uplink's operational state is tracked when enabled.

## nv set interface <interface-id> evpn multihoming segment

**Usage**

  nv set interface <interface-id> evpn multihoming segment [options] [<attribute> ...]



  Multihoming interface segment

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  enable          Turn the feature 'on' or 'off'. The default is 'off'.

  df-preference   Designated forwarder preference value for this ethernet segment. If 'auto', the global evpn multihoming preference will be used. This is the default.

  identifier      Ethernet segment identifier. This must be unique for each segment and match other bonds in the segment.

  local-id        Ethernet segment local-id. If provided, it will be combined with the global multihoming `mac-address` to create the ethernet segment identifier, which must be unique for each segment and match other bonds in the segment.

  mac-address     MAC address for this ethernet segment. If 'auto', the global evpn multihoming mac-address will be used. This is the default.

## nv set interface <interface-id> evpn multihoming segment local-id 1-16777215

**Usage**

  nv set interface <interface-id> evpn multihoming segment local-id [options] 1-16777215



  Ethernet segment local-id.  If provided, it will be combined with the global multihoming `mac-address` to create the ethernet segment identifier, which must be unique for each segment and match other bonds in the segment.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> evpn multihoming segment identifier <es-identifier>

**Usage**

  nv set interface <interface-id> evpn multihoming segment identifier [options] <es-identifier>



  Ethernet segment identifier.  This must be unique for each segment and match other bonds in the segment.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> acl <acl-id>

**Usage**

  nv set interface <interface-id> acl <acl-id> [options] [<attribute> ...]



  An ACL is used for matching packets and take actions

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <acl-id>        ACL ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound         ACL applied for inbound direction

  outbound        ACL applied for outbound direction

## nv set interface <interface-id> acl <acl-id> inbound

**Usage**

  nv set interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]



  inbound direction

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <acl-id>        ACL ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  control-plane   ACL applied for control plane

## nv set interface <interface-id> acl <acl-id> inbound control-plane

**Usage**

  nv set interface <interface-id> acl <acl-id> inbound control-plane [options]



  State details

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <acl-id>        ACL ID

## nv set interface <interface-id> acl <acl-id> outbound

**Usage**

  nv set interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]



  State details

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <acl-id>        ACL ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  control-plane

## nv set interface <interface-id> acl <acl-id> outbound control-plane

**Usage**

  nv set interface <interface-id> acl <acl-id> outbound control-plane [options]



  State details

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface
  <acl-id>        ACL ID

## nv set interface <interface-id> ptp

**Usage**

  nv set interface <interface-id> ptp [options] [<attribute> ...]



  Interface Specific PTP configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>     Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  timers             Interface PTP timerss

  enable             Turn the feature 'on' or 'off'. The default is 'off'.

  acceptable-master  Determines if acceptable master check is enabled for this interface.

  delay-mechanism    Mode in which PTP message is transmitted.

  forced-master      Configures PTP interfaces to forced master state.

  instance           PTP instance number.

  message-mode       Mode in which PTP delay message is transmitted.

  transport          Transport method for the PTP messages.

  ttl                Maximum number of hops the PTP messages can make before it gets dropped.

## nv set interface <interface-id> ptp timers

**Usage**

  nv set interface <interface-id> ptp timers [options] [<attribute> ...]



  Interface PTP timerss

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>      Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  announce-interval   Mean time interval between successive Announce messages. It's specified as a power of two in seconds.

  announce-timeout    The number of announceIntervals that have to pass without receipt of an Announce message before the  occurrence of the timeout event

  delay-req-interval  The minimum permitted mean time interval between successive Delay Req messages. It's specified as a power of two in seconds.

  sync-interval       The mean SyncInterval for multicast messages. It's specified as a power of two in seconds.

## nv set interface <interface-id> ptp timers announce-interval -3-4

**Usage**

  nv set interface <interface-id> ptp timers announce-interval [options] -3-4



  Mean time interval between successive Announce messages.  It's specified as a power of two in seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ptp timers sync-interval -7-1

**Usage**

  nv set interface <interface-id> ptp timers sync-interval [options] -7-1



  The mean SyncInterval for multicast messages.  It's specified as a power of two in seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ptp timers delay-req-interval -7-6

**Usage**

  nv set interface <interface-id> ptp timers delay-req-interval [options] -7-6



  The minimum permitted mean time interval between successive Delay Req messages.  It's specified as a power of two in seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ptp timers announce-timeout 2-10

**Usage**

  nv set interface <interface-id> ptp timers announce-timeout [options] 2-10



  The number of announceIntervals that have to pass without receipt of an Announce message before the occurrence of the timeout event

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ptp instance <value>

**Usage**

  nv set interface <interface-id> ptp instance [options] <value>



  PTP instance number.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ptp delay-mechanism end-to-end

**Usage**

  nv set interface <interface-id> ptp delay-mechanism [options] end-to-end



  Mode in which PTP message is transmitted.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> ptp ttl 1-255

**Usage**

  nv set interface <interface-id> ptp ttl [options] 1-255



  Maximum number of hops the PTP messages can make before it gets dropped.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> tunnel

**Usage**

  nv set interface <interface-id> tunnel [options] [<attribute> ...]



  The state of the interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  dest-ip         Destination underlay IP address

  interface       Physical underlay interface to used for Tunnel packets

  mode            tunnel mode

  source-ip       Source underlay IP address

  ttl             time to live

## nv set interface <interface-id> tunnel source-ip <ipv4>

**Usage**

  nv set interface <interface-id> tunnel source-ip [options] <ipv4>



  Source underlay IP address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> tunnel dest-ip <ipv4>

**Usage**

  nv set interface <interface-id> tunnel dest-ip [options] <ipv4>



  Destination underlay IP address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> tunnel ttl 1-255

**Usage**

  nv set interface <interface-id> tunnel ttl [options] 1-255



  time to live

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> tunnel mode gre

**Usage**

  nv set interface <interface-id> tunnel mode [options] gre



  tunnel mode

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> tunnel interface <interface-name>

**Usage**

  nv set interface <interface-id> tunnel interface [options] <interface-name>



  Physical underlay interface to used for Tunnel packets

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> description <value>

**Usage**

  nv set interface <interface-id> description [options] <value>



  Details about the interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set interface <interface-id> vlan 1-4094

**Usage**

  nv set interface <interface-id> vlan [options] 1-4094



  VLAN ID

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <interface-id>  Interface

## nv set service

**Usage**

  nv set service [options] [<attribute> ...]



  A service

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  dns           collection of DNS

  syslog        collection of syslog

  ntp           NTPs

  dhcp-relay    DHCP-relays

  dhcp-relay6   DHCP-relays

  ptp           Collection of PTP instances

  dhcp-server   DHCP-servers

  dhcp-server6  DHCP-servers6

  lldp          Global LLDP

## nv set service dns <vrf-id>

**Usage**

  nv set service dns <vrf-id> [options] [<attribute> ...]



  Domain Name Service

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  server      Remote DNS servers

## nv set service dns <vrf-id> server <dns-server-id>

**Usage**

  nv set service dns <vrf-id> server <dns-server-id> [options]



  A remote DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <dns-server-id>  IPv4 or IPv6 address of a DNS server

## nv set service syslog <vrf-id>

**Usage**

  nv set service syslog <vrf-id> [options] [<attribute> ...]



  Domain Name Service

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  server      Remote DNS servers

## nv set service syslog <vrf-id> server <server-id>

**Usage**

  nv set service syslog <vrf-id> server <server-id> [options] [<attribute> ...]



  A remote DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of a syslog server

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  port         Port number of the remote syslog server

  protocol     Protocol, udp or tcp, of the remote syslog server

## nv set service syslog <vrf-id> server <server-id> port 1-32767

**Usage**

  nv set service syslog <vrf-id> server <server-id> port [options] 1-32767



  Port number of the remote syslog server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of a syslog server

## nv set service ntp <vrf-id>

**Usage**

  nv set service ntp <vrf-id> [options] [<attribute> ...]



  Network Time Protocol

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  server      Remote NTP Servers

  pool        Remote NTP Servers

  listen      NTP interface to listen on.

## nv set service ntp <vrf-id> server <server-id>

**Usage**

  nv set service ntp <vrf-id> server <server-id> [options] [<attribute> ...]



  A remote NTP Server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  iburst       When the server is unreachable, send a burst of eight packets instead of the usual one.

## nv set service ntp <vrf-id> pool <server-id>

**Usage**

  nv set service ntp <vrf-id> pool <server-id> [options] [<attribute> ...]



  A remote NTP Server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  iburst       When the server is unreachable, send a burst of eight packets instead of the usual one.

## nv set service ntp <vrf-id> listen <interface-name>

**Usage**

  nv set service ntp <vrf-id> listen [options] <interface-name>



  NTP interface to listen on.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set service dhcp-relay <vrf-id>

**Usage**

  nv set service dhcp-relay <vrf-id> [options] [<attribute> ...]



  DHCP relay

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>             VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  server               DHCP servers

  interface            Set of interfaces on which to handle DHCP relay traffic

  giaddress-interface  Configures DHCP relay giaddress on the interfaes.

  source-ip            Source IP to use on the relayed packet. If "giaddr", it will be taken from giaddress. Otherwise, if "auto", it will be taken from an L3 interface on this switch using normal routing methods. This is the default.

## nv set service dhcp-relay <vrf-id> server <server-id>

**Usage**

  nv set service dhcp-relay <vrf-id> server <server-id> [options]



  A DHCP server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <server-id>  DHCP server

## nv set service dhcp-relay <vrf-id> interface <interface-id>

**Usage**

  nv set service dhcp-relay <vrf-id> interface <interface-id> [options]



  An interface on which DHCP relay is configured.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id>

**Usage**

  nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options] [<attribute> ...]



  An interface on which DHCP relay giaddress is configured.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP relay giaddress interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  address         ipv4 address on giaddress interface

## nv set service dhcp-relay6 <vrf-id>

**Usage**

  nv set service dhcp-relay6 <vrf-id> [options] [<attribute> ...]



  DHCP relay

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  interface   DHCP relay interfaces

## nv set service dhcp-relay6 <vrf-id> interface

**Usage**

  nv set service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]



  DHCP relay interfaces

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  upstream    Configures DHCP relay on the interfaes.

  downstream  Configures DHCP relay on the interfaes.

## nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id>

**Usage**

  nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options] [<attribute> ...]



  An interface on which DPCH relay is configured.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  address         ipv6 address on interface

## nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address <ipv6>

**Usage**

  nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address [options] <ipv6>



  ipv6 address on interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id>

**Usage**

  nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options] [<attribute> ...]



  An interface on which DPCH relay is configured.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  address         ipv6 address on interface

## nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address <ipv6>

**Usage**

  nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address [options] <ipv6>



  ipv6 address on interface

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv set service ptp <instance-id>

**Usage**

  nv set service ptp <instance-id> [options] [<attribute> ...]



  Global PTP configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>      PTP instance number. It is used for management purpose.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  acceptable-master  Collection of acceptable masters

  monitor            PTP monitor configuration

  enable             Turn the feature 'on' or 'off'. The default is 'off'.

  domain             Domain number of the current syntonization

  ip-dscp            Sets the Diffserv code point for all PTP packets

                     originated locally.

  priority1          Priority1 attribute of the local clock

  priority2          Priority2 attribute of the local clock

  two-step           Determines if the Clock is a 2 step clock

## nv set service ptp <instance-id> acceptable-master <clock-id>

**Usage**

  nv set service ptp <instance-id> acceptable-master <clock-id> [options] [<attribute> ...]



  List of clocks that the local clock can accept as master clock

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.
  <clock-id>     Clock ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  alt-priority   Alternate priority

## nv set service ptp <instance-id> acceptable-master <clock-id> alt-priority <value>


**Usage**

  nv set service ptp <instance-id> acceptable-master <clock-id> alt-priority [options] <value>



  Alternate priority

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.
  <clock-id>     Clock ID

## nv set service ptp <instance-id> monitor

**Usage**

  nv set service ptp <instance-id> monitor [options] [<attribute> ...]



  PTP monitor configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>         PTP instance number. It is used for management purpose.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  max-offset-threshold  Maximum offset threshold in nano seconds

  max-timestamp-entries Maximum timestamp entries allowed

  max-violation-log-entries  Maximum violation log entries per set

  max-violation-log-sets Maximum violation logs sets allowed

  min-offset-threshold  Minimum offset threshold in nano seconds

  path-delay-threshold  Path delay threshold in nano seconds

  violation-log-interval violation log intervals in seconds

## nv set service ptp <instance-id> monitor min-offset-threshold <value>

**Usage**

  nv set service ptp <instance-id> monitor min-offset-threshold [options] <value>



  Minimum offset threshold in nano seconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-offset-threshold <value>

**Usage**

  nv set service ptp <instance-id> monitor max-offset-threshold [options] <value>



  Maximum offset threshold in nano seconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor path-delay-threshold <value>

**Usage**

  nv set service ptp <instance-id> monitor path-delay-threshold [options] <value>



  Path delay threshold in nano seconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-timestamp-entries 400-1000

**Usage**

  nv set service ptp <instance-id> monitor max-timestamp-entries [options] 400-1000



  Maximum timestamp entries allowed

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-violation-log-sets 8-128

**Usage**

  nv set service ptp <instance-id> monitor max-violation-log-sets [options] 8-128



  Maximum violation logs sets allowed

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-violation-log-entries 8-128

**Usage**

  nv set service ptp <instance-id> monitor max-violation-log-entries [options] 8-128



  Maximum violation log entries per set

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor violation-log-interval 0-259200

**Usage**

  nv set service ptp <instance-id> monitor violation-log-interval [options] 0-259200



  violation log intervals in seconds

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> priority1 <value>

**Usage**

  nv set service ptp <instance-id> priority1 [options] <value>



  Priority1 attribute of the local clock

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> priority2 <value>

**Usage**

  nv set service ptp <instance-id> priority2 [options] <value>



  Priority2 attribute of the local clock

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> domain 0-127

**Usage**

  nv set service ptp <instance-id> domain [options] 0-127



  Domain number of the current syntonization

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> ip-dscp 0-63

**Usage**

  nv set service ptp <instance-id> ip-dscp [options] 0-63



  Sets the Diffserv code point for all PTP packets originated locally.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service dhcp-server <vrf-id>

**Usage**

  nv set service dhcp-server <vrf-id> [options] [<attribute> ...]



  Dynamic Host Configuration Protocol Server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>            VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  interface           Assign DHCP options to clients directly attached to

                      these interfaes.

  pool                DHCP Pools

  domain-name         DHCP domain names

  domain-name-server  DHCP domain name servers

  static              DHCP clients with fixed IP address assignments

## nv set service dhcp-server <vrf-id> interface <interface-id>

**Usage**

  nv set service dhcp-server <vrf-id> interface <interface-id> [options]



  An interface on which DPCH clients are attached.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP client interface

## nv set service dhcp-server <vrf-id> pool <pool-id>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]



  DHCP Pool

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <pool-id>             DHCP pool subnet.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  domain-name-server    DHCP domain name servers

  domain-name           DHCP domain names

  gateway               DHCP gateway

  range                 IP Address range assignments

  cumulus-provision-url  Cumulus specific URL for provisioning script

  default-url           TBD

  lease-time            Network address lease time in seconds assigned to DHCP clients.

  ping-check            TBD

  pool-name             Name

## nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]



  A remote DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <pool-id>    DHCP pool subnet.
  <server-id>  DNS server

## nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <pool-id>         DHCP pool subnet.
  <domain-name-id>  DHCP domain name

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  domain-name       DHCP domain name

## nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name <idn-hostname>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>



  DHCP domain name

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <pool-id>         DHCP pool subnet.
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]



  A remote DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>      VRF
  <pool-id>     DHCP pool subnet.
  <gateway-id>  Gateway

## nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]



  DHCP Pool range

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  <range-id>  DHCP client interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  to          End of the range.

## nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to <ipv4>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to [options] <ipv4>



  End of the range.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  <range-id>  DHCP client interface

## nv set service dhcp-server <vrf-id> pool <pool-id> pool-name <value>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> pool-name [options] <value>



  Name

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.

## nv set service dhcp-server <vrf-id> pool <pool-id> lease-time 180-31536000

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> lease-time [options] 180-31536000



  Network address lease time in seconds assigned to DHCP clients.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.

## nv set service dhcp-server <vrf-id> pool <pool-id> default-url <value>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> default-url [options] <value>



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.

## nv set service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url <value>

**Usage**

  nv set service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url [options] <value>



  Cumulus specific URL for provisioning script

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.

## nv set service dhcp-server <vrf-id> domain-name <domain-name-id>

**Usage**

  nv set service dhcp-server <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  domain-name       DHCP domain name

## nv set service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name <idn-hostname>

**Usage**

  nv set service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>



  DHCP domain name

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server <vrf-id> domain-name-server <server-id>

**Usage**

  nv set service dhcp-server <vrf-id> domain-name-server <server-id> [options]



  A remote DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <server-id>  DNS server

## nv set service dhcp-server <vrf-id> static <static-id>

**Usage**

  nv set service dhcp-server <vrf-id> static <static-id> [options] [<attribute> ...]



  static entry

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <static-id>           static mapping nane

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  cumulus-provision-url Cumulus specific URL for provisioning script

  ip-address            IP address

  mac-address           MAC (hardware) address

## nv set service dhcp-server <vrf-id> static <static-id> mac-address <mac>

**Usage**

  nv set service dhcp-server <vrf-id> static <static-id> mac-address [options] <mac>



  MAC (hardware) address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv set service dhcp-server <vrf-id> static <static-id> ip-address <ipv4>


**Usage**

  nv set service dhcp-server <vrf-id> static <static-id> ip-address [options] <ipv4>



  IP address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url <value>

**Usage**

  nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url [options] <value>



  Cumulus specific URL for provisioning script

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv set service dhcp-server6 <vrf-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> [options] [<attribute> ...]



  Dynamic Host Configuration Protocol IPv6 Server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>            VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  interface           Assign DHCP options to clients directly attached to

                      these interfaes.

  pool                DHCP IP Pools

  domain-name         DHCP domain names

  domain-name-server  DHCP domain name servers

  static              DHCP clients with fixed IP address assignments

## nv set service dhcp-server6 <vrf-id> interface <interface-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> interface <interface-id> [options]



  An interface on which DPCH clients are attached.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <interface-id>  DHCP client interface

## nv set service dhcp-server6 <vrf-id> pool <pool-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]



  DHCP Pool

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <pool-id>             DHCP6 pool subnet.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  domain-name-server    DHCP domain name servers

  domain-name           DHCP domain names

  range                 IP Address range assignments

  cumulus-provision-url  Cumulus specific URL for provisioning script

  default-url           TBD

  lease-time            Network address lease time in seconds assigned to DHCP clients.

  ping-check            TBD

  pool-name             Name

## nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]



  A remote DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <pool-id>    DHCP6 pool subnet.
  <server-id>  DNS server

## nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <pool-id>         DHCP6 pool subnet.
  <domain-name-id>  DHCP domain name

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  domain-name       DHCP domain name

## nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name <idn-hostname>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>



  DHCP domain name

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <pool-id>         DHCP6 pool subnet.
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]



  DHCP Pool range

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  <range-id>  DHCP client interface

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  to          End of the range.

## nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to <ipv6>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to [options] <ipv6>



  End of the range.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  <range-id>  DHCP client interface

## nv set service dhcp-server6 <vrf-id> pool <pool-id> pool-name <value>


**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> pool-name [options] <value>



  Name

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.

## nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time 180-31536000


**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time [options] 180-31536000



  Network address lease time in seconds assigned to DHCP clients.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.

## nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url <value>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url [options] <value>



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.

## nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url <value>

**Usage**

  nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url [options] <value>



  Cumulus specific URL for provisioning script

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.

## nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  domain-name       DHCP domain name

## nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name <idn-hostname>

**Usage**

  nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>



  DHCP domain name

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server6 <vrf-id> domain-name-server <server-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]



  A remote DNS server

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <server-id>  DNS server

## nv set service dhcp-server6 <vrf-id> static <static-id>

**Usage**

  nv set service dhcp-server6 <vrf-id> static <static-id> [options] [<attribute> ...]



  static entry

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <static-id>           static mapping nane

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  cumulus-provision-url  Cumulus specific URL for provisioning script

  ip-address            IP address

  mac-address           MAC (hardware) address

## nv set service dhcp-server6 <vrf-id> static <static-id> mac-address <mac>

**Usage**

  nv set service dhcp-server6 <vrf-id> static <static-id> mac-address [options] <mac>



  MAC (hardware) address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv set service dhcp-server6 <vrf-id> static <static-id> ip-address <ipv6>

**Usage**

  nv set service dhcp-server6 <vrf-id> static <static-id> ip-address [options] <ipv6>



  IP address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url <value>

**Usage**

  nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url [options] <value>



  Cumulus specific URL for provisioning script

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv set service lldp

**Usage**

  nv set service lldp [options] [<attribute> ...]



  Global LLDP

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  dot1-tlv            Enable dot1 TLV advertisements on enabled ports

  tx-hold-multiplier  < TTL of transmitted packets is calculated by multiplying the tx-interval by the given factor

  tx-interval         change transmit delay

## nv set service lldp tx-interval 10-300

**Usage**

  nv set service lldp tx-interval [options] 10-300



  change transmit delay

## nv set service lldp tx-hold-multiplier 1-10

**Usage**

  nv set service lldp tx-hold-multiplier [options] 1-10



  < TTL of transmitted packets is calculated by multiplying the tx-interval by the given factor

## nv set system

**Usage**

  nv set system [options] [<attribute> ...]



  Top-level node which contains system-wide properties.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  control-plane  Control Plane specific configurations

  message        System pre-login and post-login messages

  global         global system configuration

  port-mirror    Port mirror

  config         Affect how config operations are performed.

  hostname       Static hostname for the switch

  timezone       system time zone

## nv set system control-plane

**Usage**

  nv set system control-plane [options] [<attribute> ...]



  Control Plane specific configurations

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  trap        Traps

  policer     Policers

## nv set system control-plane trap <trap-id>

**Usage**

  nv set system control-plane trap <trap-id> [options] [<attribute> ...]



  Trap

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <trap-id>   TRAP ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  state       trap state

## nv set system control-plane policer <policer-id>

**Usage**

  nv set system control-plane policer <policer-id> [options] [<attribute> ...]



  Policer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <policer-id>  Policer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  burst         policer burst value

  rate          policer rate value

  state         policer state

## nv set system control-plane policer <policer-id> burst 10-10000

**Usage**

  nv set system control-plane policer <policer-id> burst [options] 10-10000



  policer burst value

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <policer-id>  Policer ID

## nv set system control-plane policer <policer-id> rate 10-10000

**Usage**

  nv set system control-plane policer <policer-id> rate [options] 10-10000



  policer rate value

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <policer-id>  Policer ID

## nv set system message

**Usage**

  nv set system message [options] [<attribute> ...]



  System pre-login and post-login messages

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  post-login  configure post-login message of the day

  pre-login   configure pre-login banner

## nv set system message pre-login <value>

**Usage**

  nv set system message pre-login [options] <value>



  configure pre-login banner

## nv set system message post-login <value>

**Usage**

  nv set system message post-login [options] <value>



  configure post-login message of the day

## nv set system global

**Usage**

  nv set system global [options] [<attribute> ...]



  global system configuration

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  reserved     reserved ranges

  anycast-id   An integer (1-65535) to select rack MAC address in range 44:38:39:ff:00:00 to 44:38:39:ff:ff:ff

  anycast-mac  MAC address shared by the rack.

  fabric-id    An integer (1-255) to select first hop router MAC adress in range 00:00:5E:00:01:01 to 00:00:5E:00:01:ff

  fabric-mac   First hop router MAC address

  system-mac   full MAC address.

## nv set system global reserved

**Usage**

  nv set system global reserved [options] [<attribute> ...]



  reserved ranges

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  routing-table  reserved routing table ranges

  vlan           reserved vlan ranges

## nv set system global reserved routing-table

**Usage**

  nv set system global reserved routing-table [options] [<attribute> ...]



  reserved routing table ranges

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  pbr         reserved routing table ranges for PBR

## nv set system global reserved routing-table pbr

**Usage**

  nv set system global reserved routing-table pbr [options] [<attribute> ...]



  reserved routing table ranges for PBR

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  begin       Beginning of reserved routing table range for PBR

  end         End of reserved routing table range for PBR

## nv set system global reserved routing-table pbr begin 10000-4294966272

**Usage**

  nv set system global reserved routing-table pbr begin [options] 10000-4294966272



  Beginning of reserved routing table range for PBR

## nv set system global reserved routing-table pbr end 10000-4294966272

**Usage**

  nv set system global reserved routing-table pbr end [options] 10000-4294966272



  End of reserved routing table range for PBR

## nv set system global reserved vlan

**Usage**

  nv set system global reserved vlan [options] [<attribute> ...]



  reserved vlan ranges

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  l3-vni-vlan  Reserved vlans to be used with l3vni

## nv set system global reserved vlan l3-vni-vlan

**Usage**

  nv set system global reserved vlan l3-vni-vlan [options] [<attribute> ...]



  Reserved vlans to be used with l3vni

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  begin       Beginning of reserved vlan range for L3 VNI

  end         End of reserved vlan range for L3 VNI

## nv set system global reserved vlan l3-vni-vlan begin 1-4093

**Usage**

  nv set system global reserved vlan l3-vni-vlan begin [options] 1-4093



  Beginning of reserved vlan range for L3 VNI

## nv set system global reserved vlan l3-vni-vlan end 2-4093

**Usage**

  nv set system global reserved vlan l3-vni-vlan end [options] 2-4093



  End of reserved vlan range for L3 VNI

## nv set system global fabric-id 1-255

**Usage**

  nv set system global fabric-id [options] 1-255



  An integer (1-255) to select first hop router MAC adress in range 00:00:5E:00:01:01 to 00:00:5E:00:01:ff

## nv set system port-mirror

**Usage**

  nv set system port-mirror [options] [<attribute> ...]



  Port mirror

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  session     sessions


## nv set system port-mirror session <session-id>

**Usage**

  nv set system port-mirror session <session-id> [options] [<attribute> ...]



  port mirror session number

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  span          Switched Port Analyzer

  erspan        Encapsulated Remote Switched Port Analyzer.

## nv set system port-mirror session <session-id> span

**Usage**

  nv set system port-mirror session <session-id> span [options] [<attribute> ...]



  Switched Port Analyzer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  source-port   Set of source ports.

  destination   The SPAN destination port.

  truncate      TBD

  enable        Turn the feature 'on' or 'off'. The default is 'off'.

  direction     The direction of traffic through source-port to mirror.

## nv set system port-mirror session <session-id> span source-port <port-id>

**Usage**

  nv set system port-mirror session <session-id> span source-port <port-id> [options]



  A port-mirror source port (swps or bonds only)

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

  <port-id>     Port interface

## nv set system port-mirror session <session-id> span destination <port-id>

**Usage**

  nv set system port-mirror session <session-id> span destination <port-id> [options]



  The SPAN destination port.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

  <port-id>     Port interface

## nv set system port-mirror session <session-id> span truncate

**Usage**

  nv set system port-mirror session <session-id> span truncate [options] [<attribute> ...]



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable        Turn the feature 'on' or 'off'. The default is 'off'.

  size          Truncates the mirrored frames at specified number of bytes. Truncate size must be between 4 and 4088 bytes and a multiple of 4

## nv set system port-mirror session <session-id> erspan

**Usage**

  nv set system port-mirror session <session-id> erspan [options] [<attribute> ...]



  Encapsulated Remote Switched Port Analyzer.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  source-port   Set of source ports.

  destination   erspan destination

  truncate      TBD

  enable        Turn the feature 'on' or 'off'. The default is 'off'.

  direction     The direction of traffic through source-port to mirror.

## nv set system port-mirror session <session-id> erspan source-port <port-id>

**Usage**

  nv set system port-mirror session <session-id> erspan source-port <port-id> [options]



  A port-mirror source port (swps or bonds only)

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

  <port-id>     Port interface

## nv set system port-mirror session <session-id> erspan destination

**Usage**

  nv set system port-mirror session <session-id> erspan destination [options] [<attribute> ...]



  erspan destination

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  source-ip     TBD

  dest-ip       TBD

## nv set system port-mirror session <session-id> erspan destination source-ip <source-ip>

**Usage**

  nv set system port-mirror session <session-id> erspan destination source-ip <source-ip> [options]



  An IPv4 address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

## nv set system port-mirror session <session-id> erspan destination dest-ip <dest-ip>

**Usage**

  nv set system port-mirror session <session-id> erspan destination dest-ip <dest-ip> [options]



  An IPv4 address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

## nv set system port-mirror session <session-id> erspan truncate

**Usage**

  nv set system port-mirror session <session-id> erspan truncate [options] [<attribute> ...]



  TBD

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <session-id>  port mirror session number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  enable        Turn the feature 'on' or 'off'. The default is 'off'.

  size          Truncates the mirrored frames at specified number of bytes. Truncate size must be between 4 and 4088 bytes and a multiple of 4

## nv set system config

**Usage**

  nv set system config [options] [<attribute> ...]



  Affect how config operations are performed.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  apply       Affect how config apply operations are performed.

## nv set system config apply

**Usage**

  nv set system config apply [options] [<attribute> ...]



  Affect how config apply operations are performed.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ignore      Set of files to ignore during config apply operations.

  overwrite   Determine which files can be overwritten during an apply. When "all", then all files can be overwritten. If the file was locally modified, then a warning will be issued and the client will have an opportunity to abort the apply before the local modifications are overwritten. This is the default. When "controlled", then only files that were most recently written by CUE can be overwritten. If the file was locally modified, a warning will be issued, but the file will not be overwritten.

## nv set system config apply ignore <ignore-id>

**Usage**

  nv set system config apply ignore <ignore-id> [options]



  File to ignore during config apply operations.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <ignore-id>  Ignored file

## nv set system hostname <idn-hostname>

**Usage**

  nv set system hostname [options] <idn-hostname>



  Static hostname for the switch

## nv set vrf <vrf-id>

**Usage**

  nv set vrf <vrf-id> [options] [<attribute> ...]



  A VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  loopback    The loopback IP interface associated with this VRF.

  evpn        EVPN control plane config and info for VRF

  router      A VRF

  ptp         VRF PTP configuration. Inherited by interfaces in this VRF.

  table       The routing table number, between 1001-1255, used by the named VRF. If auto, the default, it will be auto generated.

## nv set vrf <vrf-id> loopback

**Usage**

  nv set vrf <vrf-id> loopback [options] [<attribute> ...]



  The loopback IP interface associated with this VRF.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ip          Properties associated with the loopback IP address on this VRF.

## nv set vrf <vrf-id> loopback ip

**Usage**

  nv set vrf <vrf-id> loopback ip [options] [<attribute> ...]



  IP addresses associated with the VRF's loopback interface.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  address     static IPv4 or IPv6 address

## nv set vrf <vrf-id> loopback ip address <ip-prefix-id>

**Usage**

  nv set vrf <vrf-id> loopback ip address <ip-prefix-id> [options]



  An IP address with prefix

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF

  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv set vrf <vrf-id> evpn

**Usage**

  nv set vrf <vrf-id> evpn [options] [<attribute> ...]



  EVPN control plane config and info for VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  vni         L3 VNI

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  vlan        VLAN ID

## nv set vrf <vrf-id> evpn vni <vni-id>

**Usage**

  nv set vrf <vrf-id> evpn vni <vni-id> [options] [<attribute> ...]



  VNI

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>            VRF

  <vni-id>            VxLAN ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  prefix-routes-only  Associated L3 VNI and corresponding route targets only with EVPN type-5 routes, not with EVPN type-2 routes.

## nv set vrf <vrf-id> router

**Usage**

  nv set vrf <vrf-id> router [options] [<attribute> ...]



  A VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  rib         RIB Routes

  bgp         BGP VRF configuration.

  static      Routes

  pim         PIM VRF configuration.

  ospf        OSPF VRF configuration.

## nv set vrf <vrf-id> router rib <afi>

**Usage**

  nv set vrf <vrf-id> router rib <afi> [options] [<attribute> ...]



  Vrf aware Routing-table per address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

  <afi>       Route address family.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  protocol    Import protocols from RIB to FIB

## nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id>

**Usage**

  nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id> [options] [<attribute> ...]



  Import Protocols from where routes are known

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

  <afi>                 Route address family.

  <import-protocol-id>  Import protocol list.

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  fib-filter            Route map to apply on the import prootcol's routes.

## nv set vrf <vrf-id> router bgp

**Usage**

  nv set vrf <vrf-id> router bgp [options] [<attribute> ...]



  BGP VRF configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>            VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  address-family      Address family specific configuration

  path-selection      BGP path-selection configuration.

  route-reflection    BGP route-reflection configuration.

  peer-group          Peers

  route-export        Controls for exporting ipv4 and ipv6 routes from this VRF

  route-import        Controls for importing of ipv4 and ipv6 routes from this VRF

  timers              timer values for all peers in this VRF

  confederation       BGP Confederation options.

  neighbor            Peers

  enable              Turn the feature 'on' or 'off'. The default is 'off'.

  autonomous-system   ASN for this VRF. If "auto", inherit from the global config. This is the default.

  dynamic-peer-limit  Maximum number of dynamic neighbors from whom we can accept a connection. Applicable only if 'dynamic- peering' subnet ranges are configured

  rd                  BGP Route Distinguisher to use when this VRF routes have to be exported.

  router-id           BGP router-id for this VRF. If "auto", inherit from the global config. This is the default.

## nv set vrf <vrf-id> router bgp address-family

**Usage**

  nv set vrf <vrf-id> router bgp address-family [options] [<attribute> ...]



  Address family specific configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>      VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ipv4-unicast  IPv4 unicast address family

  l2vpn-evpn    BGP VRF configuration. L2VPN EVPN address family

  ipv6-unicast  IPv6 unicast address family

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]



  IPv4 unicast address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  redistribute     Route redistribute

  aggregate-route  IPv4 aggregate routes

  network          IPv4 static networks.

  route-import     Route import

  multipaths       Multipaths

  admin-distance   Admin distances.

  route-export     Route export

  rib-filter       Specifies filtering policies to apply prior to route install into the zebra RIB

  enable           Turn the feature 'on' or 'off'. The default is 'on'.

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]



  Route redistribute

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  static      Route redistribution of ipv4 static routes

  connected   Route redistribution of ipv4 connected routes

  kernel      Route redistribution of ipv4 kernel routes

  ospf        Route redistribution of ipv4 ospf routes

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route. This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route. This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]



  An IPv4 aggregate route

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  as-set                If 'on', an AS_SET is generated for the aggregate.

  route-map             Optional policy to modify attributes

  summary-only          If 'on', suppress more-specific routes.

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options] [<attribute> ...]



  An IPv4 static network.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>             VRF
  <static-network-id>  IPv4 address and route prefix in CIDR notation

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map            Optional policy to modify attributes

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]



  Route import

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  from-vrf    Controls for VRF to VRF route leaking for this address-family

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]



  Controls for VRF to VRF route leaking for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  list        List of VRFs the routes can be imported from

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  route-map   Route-map to control the import of routes into EVPN

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]



  A VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  
  <leak-vrf-id>  VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map [options] <instance-name>



  Route-map to control the import of routes into EVPN

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options] [<attribute> ...]



  Multipaths

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  compare-cluster-length If on, if IBGP paths have a CLUSTER_LIST, their lengths must be equal to be selected as multipaths

  ebgp                  EBGP multipath

  ibgp                  IBGP multipath

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp 1-128

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp [options] 1-128



  EBGP multipath

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp 1-128

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp [options] 1-128



  IBGP multipath

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options] [<attribute> ...]



  Admin distances.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  external    Distance to apply to routes from EBGP peers when installed into the RIB

  internal    Distance to apply to routes from IBGP peers when installed into the RIB

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external 1-255

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external [options] 1-255



  Distance to apply to routes from EBGP peers when installed into the RIB

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal 1-255

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal [options] 1-255



  Distance to apply to routes from IBGP peers when installed into the RIB

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]



  Route export

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  to-evpn     Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options] [<attribute> ...]



  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  default-route-origination Default route origination

  route-map             Route-map to control the export of routes into EVPN

## nv set vrf <vrf-id> router bgp address-family l2vpn-evpn

**Usage**

  nv set vrf <vrf-id> router bgp address-family l2vpn-evpn [options] [<attribute> ...]



  BGP VRF configuration. L2VPN EVPN address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]



  IPv6 unicast address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aggregate-route  IPv6 aggregate routes

  network          IPv6 static networks.

  route-import     Route import

  multipaths       Multipaths

  admin-distance   Admin distances.

  route-export     Route export

  redistribute     Route redistribute

  rib-filter       Specifies filtering policies to apply prior to route install into the zebra RIB

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]



  An IPv6 aggregate route

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  as-set                If 'on', an AS_SET is generated for the aggregate.

  route-map             Optional policy to modify attributes

  summary-only          If 'on', suppress more-specific routes.

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options] [<attribute> ...]



  An IPv6 static network.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>             VRF
  <static-network-id>  IPv6 address and route prefix in CIDR notation

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map            Optional policy to modify attributes

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]



  Route import

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  from-vrf    Controls for VRF to VRF route leaking for this address-family

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]



  Controls for VRF to VRF route leaking for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  list        List of VRFs the routes can be imported from

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  route-map   Route-map to control the import of routes into EVPN

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]



  Set of VRFs

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map [options] <instance-name>



  Route-map to control the import of routes into EVPN

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options] [<attribute> ...]



  Multipaths

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  compare-cluster-length If on, if IBGP paths have a CLUSTER_LIST, their lengths must be equal to be selected as multipaths

  ebgp                  EBGP multipath

  ibgp                  IBGP multipath

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp 1-128

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp [options] 1-128



  EBGP multipath

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp 1-128

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp [options] 1-128



  IBGP multipath

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options] [<attribute> ...]



  Admin distances.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  external    Distance to apply to routes from EBGP peers when installed into the RIB

  internal    Distance to apply to routes from IBGP peers when installed into the RIB

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external 1-255

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external [options] 1-255



  Distance to apply to routes from EBGP peers when installed into the RIB

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal 1-255

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal [options] 1-255



  Distance to apply to routes from IBGP peers when installed into the RIB

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]



  Route export

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  to-evpn     Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options] [<attribute> ...]



  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  default-route-origination  Default route origination

  route-map             Route-map to control the export of routes into EVPN

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]



  Route redistribute

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  static      Route redistribution of ipv4 static routes

  connected   Route redistribution of ipv4 connected routes

  kernel      Route redistribution of ipv4 kernel routes

  ospf6       Route redistribution of ipv6 ospf routes

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route. This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route. This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route. This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6

**Usage**

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  metric      Metric to use for the redistributed route. If "auto", an appropriate value will be chosen based on the type of route. This is the default.

  route-map   Route map to apply to the redistributed route.

## nv set vrf <vrf-id> router bgp path-selection

**Usage**

  nv set vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]



  BGP path-selection configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath            BGP aspath path-selection config, applicable to this BGP instance

  med               BGP med path-selection config, applicable to this BGP instance

  multipath         BGP multipath path-selection config, applicable to this BGP instance routerid-compare  Path selection based on Router ID comparison.

## nv set vrf <vrf-id> router bgp path-selection aspath

**Usage**

  nv set vrf <vrf-id> router bgp path-selection aspath [options] [<attribute> ...]



  BGP aspath path-selection config, applicable to this BGP instance

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  compare-confed   Select AS based on confederations.

  compare-lengths  Select AS based on path length.

## nv set vrf <vrf-id> router bgp path-selection med

**Usage**

  nv set vrf <vrf-id> router bgp path-selection med [options] [<attribute> ...]



  BGP med path-selection config, applicable to this BGP instance

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  compare-always        Always compare the MED on routes, even when they were received from different neighbouring ASes.

  compare-confed        MED configuration for route-selection based on confederations.

  compare-deterministic Carry out route-selection in a way that produces deterministic answers locally.

  missing-as-max        missing-as-max

## nv set vrf <vrf-id> router bgp path-selection multipath

**Usage**

  nv set vrf <vrf-id> router bgp path-selection multipath [options] [<attribute> ...]



  BGP multipath path-selection config, applicable to this BGP instance

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath-ignore   Ignore AS path when determining multipath routing.

  bandwidth       Perform multipath route selection based on bandwidth.

  generate-asset  Requires aspath-ignore to be on

## nv set vrf <vrf-id> router bgp route-reflection

**Usage**

  nv set vrf <vrf-id> router bgp route-reflection [options] [<attribute> ...]



  BGP route-reflection configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  cluster-id            Cluster ID used during route reflection. Required when route-reflection is enabled.

  outbound-policy       Allows outbound peer policy to modify the attributes  for reflected routes. Normally, reflected routes have to retain their original attributes.

  reflect-between-clients  Allows routes to be reflected between clients.  Normally, routes are reflected only between clients and non-clients, with the clients of a route reflector expected to be fully meshed.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id>

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]



  BGP global configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <peer-group-id>       Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  bfd                   Specifies whether to track BGP peering sessions using this configuration via BFD.

  ttl-security          RFC 5082

  capabilities          Capabilities

  graceful-restart      Graceful restart

  local-as              Local AS feature

  timers                Peer peer-timerss

  address-family        Address family specific configuration

  description           neighbor description

  enforce-first-as      If on, when BGP updates are received from EBGP peers  with this config, check that first AS matches peer's AS

  multihop-ttl          Maximum hops allowed. When 'auto', the type of peer will determine the appropriate value (255 for iBGP and 1 for eBGP). This is the default.

  nexthop-connected-check  If 'on', it disables the check that a non-multihop EBGP peer should be directly connected and only announce connected next hops

  passive-mode          If enabled, do not initiate the BGP connection but wait for incoming connection

  password              Password

  remote-as             ASN for the BGP neighbor(s) using this configuration. If specified as 'external', it means an EBGP  configuration but the actual ASN is immaterial. If specified as 'internal', it means an IBGP configuration.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options] [<attribute> ...]



  Specifies whether to track BGP peering sessions using this configuration via BFD.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>           VRF
  <peer-group-id>    Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable             Turn the feature 'on' or 'off'. The default is 'off'.

  detect-multiplier  Detect multiplier

  min-rx-interval    Minimum receive interval

  min-tx-interval    Minimum transmit interval. The actual value used is the smaller of this or what the peer expects.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier 2-255

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier [options] 2-255



  Detect multiplier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval 50-60000

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval [options] 50-60000



  Minimum receive interval

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval 50-60000

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval [options] 50-60000



  Minimum transmit interval.  The actual value used is the smaller of this or what the peer expects.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options] [<attribute> ...]



  RFC 5082

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  hops             Number of hops

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops 1-254

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops [options] 1-254



  Number of hops

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options] [<attribute> ...]



  Capabilities

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <peer-group-id>   Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  extended-nexthop  If 'on', the extended-nexthop capability defined in RFC  5549 is advertised to peer(s) with this config. If 'auto', it will be 'on' for unnumbered peers and 'off' otherwise. This is the default.

  source-address    source IP address of the TCP connection, which is often  used as the BGP next hop for Updates

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options] [<attribute> ...]



  BGP Graceful restart per neighbor configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  mode             If 'auto', inherit from global. This is the default. If set to 'off', GR capability is not negotiated with this peer. If set to 'helper-only', only the Helper role is supported for this peer. This means that the GR capability will be negotiated without any address-families with this peer. If set to 'full', both the Helper role and the Restarter role are supported with this peer; the GR capability will be negotiated with the enabled address-families for which GR is also supported.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options] [<attribute> ...]



  Local AS feature

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  asn              ASN to use to establish the peering if different from the ASN of the BGP instance. This configuration finds use during AS renumbering. The local-as configured is also attached to incoming and outgoing updates.

  prepend          When set to 'off', do not prepend the configured local-as to received updates; otherwise, prepend it.

  replace          When set to 'on', attach only the configured local-as to generated updates, effectively "replacing" the AS number configured for the BGP instance with the local-as applicable for the peering; otherwise, attach the AS number of the BGP instance and then prepend it with the configured local-as.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn 1-4294967295

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn [options] 1-4294967295



  ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options] [<attribute> ...]



  Peer peer-timerss

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>             VRF
  <peer-group-id>      Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  connection-retry     Time interval at which connection attempts are retried upon a failure. If `auto`, the global value is used. This is the default.

  hold                 Hold timer. If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout. If `auto`, the global value is used. This is the default.

  keepalive            Keepalive timer. If `none`, keepalives are not sent. If `auto`, the global value is used. This is the default.

  route-advertisement  Time between route advertisements (BGP Updates). A non-zero value allows route advertisements to be delayed and batched. If `auto`, the global value is used. This is the default.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]



  Address family specific configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ipv4-unicast     Peer IPv4 unicast address family. Always on, unless disabled globaly.

  ipv6-unicast     Peer IPv6 unicast address family.

  l2vpn-evpn       Peer l2vpn EVPN address family.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]



  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <peer-group-id>       Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  community-advertise   Community advertise for address family.

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  prefix-limits         Limits on prefix from the peer for this address-family

  default-route-origination Default route origination

  policy                Policies for ipv4 unicast

  conditional-advertise Conditional advertise for address family.

  enable                Turn the feature 'on' or 'off'. The default is 'on'.

  add-path-tx           Used to enable transmission of additional paths; by default, only the best path is announced to peers

  nexthop-setting       Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

  route-reflector-client Specifies if this peer is a client and we are its route reflector

  route-server-client   Specifies if this peer is a client and we are its route server

  soft-reconfiguration  If 'on', it means that received routes from this peer  that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

  weight                Weight applied to routes received from peer; this is used in the BGP route selection algorithm

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise\

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]



  Community advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  extended         If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

  large            If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

  regular          If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]



  Attribute mod for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath           If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

  med              If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

  nexthop          If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

  private-as       If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the  peer's ASN, it is replaced with the local system's ASN

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  occurrences      Indicates max number of occurrences of the local system's AS number in the received AS_PATH

  origin           If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences 1-10

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options] 1-10



  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound          Limits on inbound prefix from the peer for this address-family

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]



  Limits on inbound prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>           VRF
  <peer-group-id>    Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  maximum            Limit on number of prefixes of specific address-family that can be received from the peer. By default, there is no limit

  reestablish-wait   Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing. This would typically be 2-3 seconds.

  warning-only       If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.

  warning-threshold  Percentage of the maximum at which a warning syslog is generated.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold 1-100

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options] 1-100



  Percentage of the maximum at which a warning syslog is generated.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295



  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]



  Default route origination

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  policy           Optional route-map policy to control the conditions under which the default route is originated.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]



  Policies for ipv4 unicast

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound          Outbound unicast policy

  outbound         Outbound unicast policy

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map        Route map to apply to Updates received from this peer

  aspath-list      AS-Path filter list to apply to Updates received from this peer

  prefix-list      Prefix list to apply to Updates received from this peer

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list [options] none



  AS-Path filter list to apply to Updates received from this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map        Route map to apply to Updates to be sent to this peer

  unsuppress-map   Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

  aspath-list      AS-Path filter list to apply to Updates sent to this peer

  prefix-list      Prefix list to apply to Updates to be sent to this peer

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list [options] none



  AS-Path filter list to apply to Updates sent to this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]



  Conditional advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  advertise-map    route-map contains prefix-list which has list of

                   routes/prefixes to operate on.

  exist-map        route-map contains the conditional routes/prefixes in

                   prefix-list.

  non-exist-map    route-map contains the negative conditional routes/prefixes

                   in prefix-list.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map [options] <instance-name>



  route-map contains prefix-list which has list of routes/prefixes to operate on.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map [options] <instance-name>



  route-map contains the conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map [options] <instance-name>



  route-map contains the negative conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight 0-65535

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight [options] 0-65535



  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]



  Peer IPv6 unicast address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <peer-group-id>       Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  policy                Policies for ipv4 unicast

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  prefix-limits         Limits on prefix from the peer for this address-family

  default-route-origination  Default route origination

  community-advertise   Community advertise for address family.

  attribute-mod         Attribute mod for address family.

  conditional-advertise Conditional advertise for address family.

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  add-path-tx           Used to enable transmission of additional paths; by default, only the best path is announced to peers

  nexthop-setting       Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This  is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes. "force" sets the next hop to ourselves for route  advertisement including for reflected routes.

  route-reflector-client Specifies if this peer is a client and we are its route reflector

  route-server-client   Specifies if this peer is a client and we are its route server

  soft-reconfiguration  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

  weight                Weight applied to routes received from peer; this is used in the BGP route selection algorithm

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy


**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]



  Policies for ipv6 unicast

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound          Outbound unicast policy

  outbound         Outbound unicast policy

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map        Route map to apply to Updates received from this peer

  aspath-list      AS-Path filter list to apply to Updates received from this

                   peer

  prefix-list      Prefix list to apply to Updates received from this peer

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list [options] none



  AS-Path filter list to apply to Updates received from this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map        Route map to apply to Updates to be sent to this peer

  unsuppress-map   Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

  aspath-list      AS-Path filter list to apply to Updates sent to this peer

  prefix-list      Prefix list to apply to Updates to be sent to this peer

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list [options] none



  AS-Path filter list to apply to Updates sent to this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

  private-as       If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  occurrences      Indicates max number of occurrences of the local system's AS number in the received AS_PATH

  origin           If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences 1-10

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options] 1-10



  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound          Limits on inbound prefix from the peer for this address-family

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]



  Limits on inbound prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>           VRF
  <peer-group-id>    Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  maximum            Limit on number of prefixes of specific address-family that can be received from the peer. By default, there is no limit

  reestablish-wait   Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing. This would typically be 2-3 seconds.

  warning-only       If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.

  warning-threshold  Percentage of the maximum at which a warning syslog is generated.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold 1-100

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options] 1-100



  Percentage of the maximum at which a warning syslog is generated.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295



  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]



  Default route origination

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  policy           Optional route-map policy to control the conditions under which the default route is originated.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]



  Community advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  extended         If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

  large            If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

  regular          If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]



  Attribute mod for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath           If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

  med              If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

  nexthop          If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise


**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]



  Conditional advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  advertise-map    route-map contains prefix-list which has list of routes/prefixes to operate on.

  exist-map        route-map contains the conditional routes/prefixes in prefix-list.

  non-exist-map    route-map contains the negative conditional routes/prefixes in prefix-list.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map [options] <instance-name>



  route-map contains prefix-list which has list of routes/prefixes to operate on.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map <instance-name>


**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map [options] <instance-name>



  route-map contains the conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map <instance-name>


**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map [options] <instance-name>



  route-map contains the negative conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight 0-65535

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight [options] 0-65535



  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]



  Peer l2vpn EVPN address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <peer-group-id>       Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for l2vpn evpn

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  add-path-tx           Used to enable transmission of additional paths; by default, only the best path is announced to peers

  nexthop-setting       Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes. "force" sets the next hop to ourselves for route  advertisement including for reflected routes.

  route-reflector-client Specifies if this peer is a client and we are it route reflector

  route-server-client   Specifies if this peer is a client and we are its route server

  soft-reconfiguration  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]



  Attribute mod for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath           If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

  med              If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

  nexthop          If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

  private-as       If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  occurrences      Indicates max number of occurrences of the local system's AS number in the received AS_PATH

  origin           If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences 1-10

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options] 1-10



  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]



  Policies for l2vpn evpn

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound          Inbound l2vpn-evpn policy

  outbound         Outbound l2vpn-evpn policy

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]



  Inbound l2vpn-evpn policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map        Route map to apply to Updates received from this peer

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]



  Outbound l2vpn-evpn policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map        Route map to apply to Updates to be sent to this peer

  unsuppress-map   Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> password none


**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> password [options] none



  Password

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> description none

**Usage**

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> description [options] none



  neighbor description

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp route-export

**Usage**

  nv set vrf <vrf-id> router bgp route-export [options] [<attribute> ...]



  Controls for exporting ipv4 and ipv6 routes from this VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  to-evpn     Controls for exporting routes from this VRF into EVPN

## nv set vrf <vrf-id> router bgp route-export to-evpn

**Usage**

  nv set vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]



  Controls for exporting routes from this VRF into EVPN

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>      VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-target  List the RTs to attach to host or prefix routes when exporting them into EVPN or "auto". If "auto", the RT will be derived. This is the default.

## nv set vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>

**Usage**

  nv set vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]



  A route target identifier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <rt-id>     Route targets or "auto"

## nv set vrf <vrf-id> router bgp route-import

**Usage**

  nv set vrf <vrf-id> router bgp route-import [options] [<attribute> ...]



  Controls for importing of ipv4 and ipv6 routes from this VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  from-evpn   Controls for importing EVPN type-2 and type-5 routes into this VRF

## nv set vrf <vrf-id> router bgp route-import from-evpn

**Usage**

  nv set vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]



  Controls for importing EVPN type-2 and type-5 routes into this VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>      VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-target  List the RTs to attach to host or prefix routes when importing them into VRF or "auto". If "auto", the RT will be derived. This is the default.\

## nv set vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>

**Usage**

  nv set vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]



  A route target identifier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <rt-id>     Route targets or "auto"

## nv set vrf <vrf-id> router bgp timers


**Usage**

  nv set vrf <vrf-id> router bgp timers [options] [<attribute> ...]



  timer values for all peers in this VRF

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  conditional-advertise Time interval at which bgp table is scanned for condition is met.

  connection-retry      Time interval at which connection attempts are retried upon a failure.

  hold                  Hold timer. If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout.

  keepalive             Keepalive timer. If `none`, keepalives are not sent.

  route-advertisement   Time between route advertisements (BGP Updates). If not `none`, route advertisements to be delayed and batched.



## nv set vrf <vrf-id> router bgp timers connection-retry 1-65535

**Usage**

  nv set vrf <vrf-id> router bgp timers connection-retry [options] 1-65535



  Time interval at which connection attempts are retried upon a failure.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp confederation


**Usage**

  nv set vrf <vrf-id> router bgp confederation [options] [<attribute> ...]



  BGP Confederation options.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  member-as   Confederation ASNs of the peers, maps to BGP confederation peers

  id          Confederation ASN, maps to BGP confederation id

## nv set vrf <vrf-id> router bgp confederation member-as

**Usage**

  nv set vrf <vrf-id> router bgp confederation member-as [options]



  Set of autonomous numbers

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id>

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]



  BGP global configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  bfd                   Specifies whether to track BGP peering sessions using this configuration via BFD.

  capabilities          Capabilities

  local-as              Local AS feature

  graceful-restart      BGP Graceful restart per neighbor configuration

  ttl-security          RFC 5082

  address-family        Address family specific configuration

  timers                Peer peer-timerss

  description           neighbor description

  enforce-first-as      If on, when BGP updates are received from EBGP peers with this config, check that first AS matches peer's AS

  multihop-ttl          Maximum hops allowed. When 'auto', the type of peer will determine the appropriate value (255 for iBGP and 1 for eBGP). This is the default.

  nexthop-connected-check If 'on', it disables the check that a non-multihopmEBGP peer should be directly connected and only announce connected next hops

  passive-mode          If enabled, do not initiate the BGP connection but wait for incoming connection

  password              Password

  enable                Turn the feature 'on' or 'off'. The default is 'on'.

  peer-group            Optional peer-group to which the peer is attached to inherit the group's configuration.

  remote-as             ASN for the BGP neighbor(s) using this configuration. If specified as 'external', it means an EBGP configuration but the actual ASN is immaterial. If specified as 'internal', it means an IBGP configuration.

  type                  The type of peer

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options] [<attribute> ...]



  Specifies whether to track BGP peering sessions using this configuration via BFD.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>           VRF
  <neighbor-id>      Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable             Turn the feature 'on' or 'off'. The default is 'off'.

  detect-multiplier  Detect multiplier

  min-rx-interval    Minimum receive interval

  min-tx-interval    Minimum transmit interval. The actual value used is the smaller of this or what the peer expects.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier 2-255

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier [options] 2-255



  Detect multiplier

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval 50-60000

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval [options] 50-60000



  Minimum receive interval

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval 50-60000

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval [options] 50-60000



  Minimum transmit interval.  The actual value used is the smaller of this or what the peer expects.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options] [<attribute> ...]



  Capabilities

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <neighbor-id>     Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  extended-nexthop  If 'on', the extended-nexthop capability defined in RFC 5549 is advertised to peer(s) with this config. If 'auto', it will be 'on' for unnumbered peers and 'off' otherwise. This is the default.

  source-address    source IP address of the TCP connection, which is often used as the BGP next hop for Updates

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options] [<attribute> ...]



  Local AS feature

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  asn            ASN to use to establish the peering if different from the ASN of the BGP instance. This configuration finds use during AS renumbering. The local-as configured is also attached to incoming and outgoing updates.

  prepend        When set to 'off', do not prepend the configured local-as to received updates; otherwise, prepend it.

  replace        When set to 'on', attach only the configured local-as to generated updates, effectively "replacing" the AS number configured for the BGP instance with the local-as applicable for the peering; otherwise, attach the AS number of the BGP instance and then prepend it with the configured local-as.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn 1-4294967295

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn [options] 1-4294967295



  ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options] [<attribute> ...]



  BGP Graceful restart per neighbor configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  mode           If 'auto', inherit from global. This is the default. If set

                 to 'off', GR capability is not negotiated with this peer. If

                 set to 'helper-only', only the Helper role is supported for

                 this peer. This means that the GR capability will be

                 negotiated without any address-families with this peer. If

                 set to 'full', both the Helper role and the Restarter role

                 are supported with this peer; the GR capability will be

                 negotiated with the enabled address-families for which GR is

                 also supported.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options] [<attribute> ...]



  RFC 5082

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  hops           Number of hops

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops 1-254

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops [options] 1-254



  Number of hops

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]



  Address family specific configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ipv4-unicast   Peer IPv4 unicast address family. Always on, unless disabled globaly.

  ipv6-unicast   Peer IPv6 unicast address family.

  l2vpn-evpn     Peer l2vpn EVPN address family.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]



  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for ipv4 unicast

  prefix-limits         Limits on prefix from the peer for this address-family

  default-route-origination  Default route origination

  community-advertise   Community advertise for address family.

  conditional-advertise Conditional advertise for address family.

  enable                Turn the feature 'on' or 'off'. The default is 'on'.

  add-path-tx           Used to enable transmission of additional paths; by default, only the best path is announced to peers

  nexthop-setting       Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselvesfor route advertisement, except for reflected routes. "force" sets the next hop to ourselves for route advertisement including for reflected routes.

  route-reflector-client Specifies if this peer is a client and we are its route reflector

  route-server-client   Specifies if this peer is a client and we are its route server

  soft-reconfiguration  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

  weight                Weight applied to routes received from peer; this is  used in the BGP route selection algorithm

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]



  Attribute mod for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath         If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

  med            If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

  nexthop        If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <neighbor-id>    Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

  private-as       If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  occurrences    Indicates max number of occurrences of the local system's AS number in the received AS_PATH

  origin         If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences 1-10

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options] 1-10



  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]



  Policies for ipv4 unicast

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound        Outbound unicast policy

  outbound       Outbound unicast policy

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map      Route map to apply to Updates received from this peer

  aspath-list    AS-Path filter list to apply to Updates received from this peer

  prefix-list    Prefix list to apply to Updates received from this peer

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list [options] none



  AS-Path filter list to apply to Updates received from this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <neighbor-id>   Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map       Route map to apply to Updates to be sent to this peer

  unsuppress-map  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

  aspath-list     AS-Path filter list to apply to Updates sent to this peer

  prefix-list     Prefix list to apply to Updates to be sent to this peer

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list [options] none



  AS-Path filter list to apply to Updates sent to this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound        Limits on inbound prefix from the peer for this address- family

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]



  Limits on inbound prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>           VRF
  <neighbor-id>      Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  maximum            Limit on number of prefixes of specific address-family that can be received from the peer. By default, there is no limit

  reestablish-wait   Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing. This would typically be 2-3 seconds.

  warning-only       If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.

  warning-threshold  Percentage of the maximum at which a warning syslog is generated.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold 1-100

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options] 1-100



  Percentage of the maximum at which a warning syslog is generated.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295



  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]



  Default route origination

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  policy         Optional route-map policy to control the conditions under which the default route is originated.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]



  Community advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  extended       If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

  large          If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

  regular        If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]



  Conditional advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  advertise-map  route-map contains prefix-list which has list of routes/prefixes to operate on.

  exist-map      route-map contains the conditional routes/prefixes in prefix- list.

  non-exist-map  route-map contains the negative conditional routes/prefixes in prefix-list.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map [options] <instance-name>



  route-map contains prefix-list which has list of routes/prefixes to operate on.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map [options] <instance-name>



  route-map contains the conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map [options] <instance-name>



  route-map contains the negative conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight 0-65535

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight [options] 0-65535



  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]



  Peer IPv6 unicast address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer  for the specified address family

  prefix-limits         Limits on prefix from the peer for this address-family

  default-route-origination Default route origination

  policy                Policies for ipv4 unicast

  community-advertise   Community advertise for address family.

  conditional-advertise Conditional advertise for address family.

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  add-path-tx           Used to enable transmission of additional paths; by default, only the best path is announced to peers

  nexthop-setting       Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes "force" sets the next hop to ourselves for route advertisement including for reflected routes.

  route-reflector-client  Specifies if this peer is a client and we are its route reflector

  route-server-client   Specifies if this peer is a client and we are its route server soft-reconfiguration  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

  weight                Weight applied to routes received from peer; this is used in the BGP route selection algorithm

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]



  Attribute mod for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath         If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

  med            If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

  nexthop        If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <neighbor-id>    Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

  private-as       If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  occurrences    Indicates max number of occurrences of the local system's AS number in the received AS_PATH

  origin         If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences 1-10

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options] 1-10



  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]



  Limits on prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound        Limits on inbound prefix from the peer for this address- family

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]



  Limits on inbound prefix from the peer for this address-family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>           VRF
  <neighbor-id>      Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  maximum            Limit on number of prefixes of specific address-family

                     that can be received from the peer. By default, there is

                     no limit

  reestablish-wait   Specifes the time in seconds to wait before establishing

                     the BGP session again with the peer. Defaults to 'auto',

                     which will use standard BGP timers and processing. This

                     would typically be 2-3 seconds.

  warning-only       If 'on', it means to only generate a warning syslog if

                     the number of received prefixes exceeds the limit, do not

                     bring down the BGP session.

  warning-threshold  Percentage of the maximum at which a warning syslog is

                     generated.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold 1-100

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options] 1-100



  Percentage of the maximum at which a warning syslog is generated.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295



  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]



  Default route origination

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  policy         Optional route-map policy to control the conditions under which the default route is originated.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]



  Policies for ipv6 unicast

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound        Outbound unicast policy

  outbound       Outbound unicast policy

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map      Route map to apply to Updates received from this peer

  aspath-list    AS-Path filter list to apply to Updates received from this peer

  prefix-list    Prefix list to apply to Updates received from this peer

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list [options] none



  AS-Path filter list to apply to Updates received from this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]



  Outbound unicast policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <neighbor-id>   Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map       Route map to apply to Updates to be sent to this peer

  unsuppress-map  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

  aspath-list     AS-Path filter list to apply to Updates sent to this peer

  prefix-list     Prefix list to apply to Updates to be sent to this peer

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list none

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list [options] none



  AS-Path filter list to apply to Updates sent to this peer

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]



  Community advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  extended       If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

  large          If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

  regular        If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise


**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]



  Conditional advertise for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  advertise-map  route-map contains prefix-list which has list of routes/prefixes to operate on.

  exist-map      route-map contains the conditional routes/prefixes in prefix-list.

  non-exist-map  route-map contains the negative conditional routes/prefixes in prefix-list.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map [options] <instance-name>



  route-map contains prefix-list which has list of routes/prefixes to operate on.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map [options] <instance-name>



  route-map contains the conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map <instance-name>

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map [options] <instance-name>



  route-map contains the negative conditional routes/prefixes in prefix-list.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight 0-65535

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight [options] 0-65535



  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]



  Peer l2vpn EVPN address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  attribute-mod         Attribute mod for address family.

  aspath                Options for handling AS_PATH for prefixes from/to peer for the specified address family

  policy                Policies for l2vpn evpn

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  add-path-tx           Used to enable transmission of additional paths; by default, only the best path is announced to peers

  nexthop-setting       Control nexthop value of advertised routes. "auto" follows regular BGP next-hop determination rules. This is the default. "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

  route-reflector-client Specifies if this peer is a client and we are its route reflector

  route-server-client   Specifies if this peer is a client and we are its  route server

  soft-reconfiguration  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]



  Attribute mod for address family.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  aspath         If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

  med            If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

  nexthop        If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]



  Options for handling AS_PATH for prefixes from/to peer for the specified address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF
  <neighbor-id>    Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

  private-as       If 'none', no specific action is taken. This is the default. If set to 'remove', any private ASNs in the Update to the peer are removed. If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]



  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable         Turn the feature 'on' or 'off'. The default is 'off'.

  occurrences    Indicates max number of occurrences of the local system's AS number in the received AS_PATH

  origin         If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences 1-10

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options] 1-10



  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]



  Policies for l2vpn evpn

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  inbound        Inbound l2vpn-evpn policy

  outbound       Outbound l2vpn-evpn policy

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]



  Inbound l2vpn-evpn policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map      Route map to apply to Updates received from this peer

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]



  Outbound l2vpn-evpn policy

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <neighbor-id>   Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  route-map       Route map to apply to Updates to be sent to this peer

  unsuppress-map  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options] [<attribute> ...]



  Peer peer-timerss

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>             VRF
  <neighbor-id>        Peer ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  connection-retry     Time interval at which connection attempts are retried upon a failure. If `auto`, the global value is used.This is the default.

  hold                 Hold timer. If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout. If `auto`, the global value is used. This is the default.

  keepalive            Keepalive timer. If `none`, keepalives are not sent. If `auto`, the global value is used. This is the default.

  route-advertisement  Time between route advertisements (BGP Updates). A non- zero value allows route advertisements to be delayed and batched. If `auto`, the global value is used. This is the default.

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> password none

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> password [options] none



  Password

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> description none

**Usage**

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> description [options] none



  neighbor description

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp dynamic-peer-limit 1-5000

**Usage**

  nv set vrf <vrf-id> router bgp dynamic-peer-limit [options] 1-5000



  Maximum number of dynamic neighbors from whom we can accept a connection. Applicable only if 'dynamic-peering' subnet ranges are configured

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router static <route-id>

**Usage**

  nv set vrf <vrf-id> router static <route-id> [options] [<attribute> ...]



  A route

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF
  <route-id>      IP prefix

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  distance        Paths

  via             Nexthops

  tag             Path tag

  address-family  Route address family

## nv set vrf <vrf-id> router static <route-id> distance <distance-id>

**Usage**

  nv set vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]



  A path

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  via            Nexthops

  tag            Path tag

## nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>

**Usage**

  nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]



  A via

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  flag           Nexthop flags

  interface      The interface to use for egress. If not specified, it will

                 automatically be determined. Only valid when the via's type

                 is ipv4-address or ipv6-address.

  vrf            The VRF to use for egress. If not specified, the route's VRF

                 will be used. Only valid when the via's type is ipv4-address

                 or ipv6-address.

  type           The type of via

## nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag onlink

**Usage**

  nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options] onlink



  Nexthop flags

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".

## nv set vrf <vrf-id> router static <route-id> via <via-id>

**Usage**

  nv set vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]



  A via

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  flag        Nexthop flags

  interface   The interface to use for egress. If not specified, it will automatically be determined. Only valid when the via's type is ipv4-address or ipv6-address.

  vrf         The VRF to use for egress. If not specified, the route's VRF will be used. Only valid when the via's type is ipv4-address or ipv6-address.

  type        The type of via

## nv set vrf <vrf-id> router static <route-id> via <via-id> flag onlink

**Usage**

  nv set vrf <vrf-id> router static <route-id> via <via-id> flag [options] onlink



  Nexthop flags

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".

## nv set vrf <vrf-id> router pim

**Usage**

  nv set vrf <vrf-id> router pim [options] [<attribute> ...]



  PIM VRF configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>         VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  timers           Timers

  ecmp             Choose all available ECMP paths for a particular RPF. If 'off', the first nexthop found will be used. This is the default.

  msdp-mesh-group  To connect multiple PIM-SM multicast domains using RPs.

  address-family   Address family specific configuration

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

## nv set vrf <vrf-id> router pim timers

**Usage**

  nv set vrf <vrf-id> router pim timers [options] [<attribute> ...]



  Timers

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>       VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  keep-alive     Timeout value for S,G stream, in seconds

  rp-keep-alive  RP's timeout value, in seconds

## nv set vrf <vrf-id> router pim ecmp

**Usage**

  nv set vrf <vrf-id> router pim ecmp [options] [<attribute> ...]



  Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

  rebalance   Recalculate all multicast streams in the event of path going down. If 'off', only the impacted streams by path going down recalculated. This is the default.

## nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>

**Usage**

  nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]



  MSDP mesh-group

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  member-address        Set of member-address

  source-address        MSDP mesh-group source IP address

## nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>

**Usage**

  nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]



  A MSDP mesh member

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name
  <mesh-member-id>      MSDP mesh-group member IP address

## nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address <ipv4>

**Usage**

  nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address [options] <ipv4>



  MSDP mesh-group source IP address

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name

## nv set vrf <vrf-id> router pim address-family

**Usage**

  nv set vrf <vrf-id> router pim address-family [options] [<attribute> ...]



  Address family specific configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>      VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ipv4-unicast  IPv4 unicast address family

## nv set vrf <vrf-id> router pim address-family ipv4-unicast

**Usage**

  nv set vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]



  IPv4 unicast address family

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>              VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  spt-switchover        Build shortest path tree towards source.

  rp                    RP address and associated group range.

  register-accept-list  Prefix-list to specifiy source list to accept register message.

  send-v6-secondary     Use IPv6 secondary address to transmit PIM Hello  packets. It allows to use IPv6 nexthop in RPF lookup.

  ssm-prefix-list       Prefix-list to specificy Source Specific Multicast Group range.

## nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover

**Usage**

  nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options] [<attribute> ...]



  Build shortest path tree towards source.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  action       PIM shortest path switchover (SPT) action.

  prefix-list  Prefix-list to specify multicast group range.

## nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list <instance-name>

**Usage**

  nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list [options] <instance-name>



  Prefix-list to specify multicast group range.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>

**Usage**

  nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]



  RP

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF
  <rp-id>      RP IP address

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  group-range  Set of group range assocaited to RP.

  prefix-list  Prefix-list to specify multicast group range.

## nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>

**Usage**

  nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]



  A group range

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <rp-id>           RP IP address
  <group-range-id>  Group range associated to RP.

## nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list <instance-name>

**Usage**

  nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list [options] <instance-name>



  Prefix-list to specify multicast group range.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <rp-id>     RP IP address

## nv set vrf <vrf-id> router ospf

**Usage**

  nv set vrf <vrf-id> router ospf [options] [<attribute> ...]



  OSPF VRF configuration.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>             VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  area                 OSPF areas

  default-originate    Advertise a default route as external lsa

  distance             Administrative distance for installation into the rib

  max-metric           Set maximum metric value in router lsa to make stub router

  log                  Log configuration

  redistribute         Route redistribute

  timers               Timers

  enable               Turn the feature 'on' or 'off'. The default is 'off'.

  reference-bandwidth  Used to determine link cost/metric value relative to defined reference.

  rfc1583-compatible   RFC1583 compatible

  router-id            BGP router-id for this VRF. If "auto", inherit from the global config. This is the default.

## nv set vrf <vrf-id> router ospf area <area-id>

**Usage**

  nv set vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]



  An OSPF area

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>          VRF
  <area-id>         Area

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  filter-list       Filters networks between OSPF areas

  range             Area ranges

  network           Area networks

  default-lsa-cost  Default LSA cost. Only applies when type is non-normal.

  type              The type of area

## nv set vrf <vrf-id> router ospf area <area-id> filter-list

**Usage**

  nv set vrf <vrf-id> router ospf area <area-id> filter-list [options] [<attribute> ...]



  Filters networks between OSPF areas

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <area-id>   Area

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  in          prefix-list to use as an inbound filter.

  out         prefix-list to use as an inbound filter.

## nv set vrf <vrf-id> router ospf area <area-id> range <range-id>

**Usage**

  nv set vrf <vrf-id> router ospf area <area-id> range <range-id> [options] [<attribute> ...]



  Filters out components of the prefix

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <area-id>   Area
  <range-id>  Range

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  cost        User specified metric advertised for this summary lsa. If 'auto', operational default value is derived from components. This is the default.

  suppress    If on, filters out components but does not advertise prefix

## nv set vrf <vrf-id> router ospf area <area-id> network <network-id>

**Usage**

  nv set vrf <vrf-id> router ospf area <area-id> network <network-id> [options]



  Filters out components of the prefix

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>      VRF
  <area-id>     Area
  <network-id>  Network

## nv set vrf <vrf-id> router ospf area <area-id> default-lsa-cost 0-16777215

**Usage**

  nv set vrf <vrf-id> router ospf area <area-id> default-lsa-cost [options] 0-16777215



  Default LSA cost.  Only applies when type is non-normal.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF
  <area-id>   Area

## nv set vrf <vrf-id> router ospf default-originate

**Usage**

  nv set vrf <vrf-id> router ospf default-originate [options] [<attribute> ...]



  Advertise a default route as external lsa

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

  metric       Metric value for destination routing protocol

  metric-type  Set OSPF External Type 1/2 metrics

  route-map    Optional policy to apply to this advertisement

  always       When 'off', only advertise default route if one exists in the rib. This is the default.

## nv set vrf <vrf-id> router ospf default-originate metric-type 1-2

**Usage**

  nv set vrf <vrf-id> router ospf default-originate metric-type [options] 1-2



  Set OSPF External Type 1/2 metrics

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router ospf distance

**Usage**

  nv set vrf <vrf-id> router ospf distance [options] [<attribute> ...]



  Administrative distance for installation into the rib

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  external    External

  inter-area  Inter-area

  intra-area  Intra-area

## nv set vrf <vrf-id> router ospf max-metric

**Usage**

  nv set vrf <vrf-id> router ospf max-metric [options] [<attribute> ...]



  Set maximum metric value in router lsa to make stub router

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>        VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  administrative  Administratively applied, for an indefinite period

  on-shutdown     Advertise stub-router prior to full shutdown of OSPF

  on-startup      Automatically advertise stub Router-LSA on startup of OSPF

## nv set vrf <vrf-id> router ospf log

**Usage**

  nv set vrf <vrf-id> router ospf log [options] [<attribute> ...]



  Log configuration

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>           VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  adjacency-changes  Log adjacency changes

## nv set vrf <vrf-id> router ospf redistribute

**Usage**

  nv set vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]



  Route redistribute

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  static      Route redistribute of static routes

  connected   Route redistribute of connected routes

  kernel      Route redistribute of kernel routes

  bgp         Route redistribute of bgp routes

## nv set vrf <vrf-id> router ospf redistribute static

**Usage**

  nv set vrf <vrf-id> router ospf redistribute static [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

  metric       Metric value for destination routing protocol

  metric-type  Set OSPF External Type 1/2 metrics

  route-map    Optional policy to apply to this advertisement

## nv set vrf <vrf-id> router ospf redistribute static metric-type 1-2

**Usage**

  nv set vrf <vrf-id> router ospf redistribute static metric-type [options] 1-2



  Set OSPF External Type 1/2 metrics

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router ospf redistribute connected

**Usage**

  nv set vrf <vrf-id> router ospf redistribute connected [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

  metric       Metric value for destination routing protocol

  metric-type  Set OSPF External Type 1/2 metrics

  route-map    Optional policy to apply to this advertisement

## nv set vrf <vrf-id> router ospf redistribute connected metric-type 1-2

**Usage**

  nv set vrf <vrf-id> router ospf redistribute connected metric-type [options] 1-2



  Set OSPF External Type 1/2 metrics

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router ospf redistribute kernel

**Usage**

  nv set vrf <vrf-id> router ospf redistribute kernel [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

  metric       Metric value for destination routing protocol

  metric-type  Set OSPF External Type 1/2 metrics

  route-map    Optional policy to apply to this advertisement

## nv set vrf <vrf-id> router ospf redistribute kernel metric-type 1-2

**Usage**

  nv set vrf <vrf-id> router ospf redistribute kernel metric-type [options] 1-2



  Set OSPF External Type 1/2 metrics

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router ospf redistribute bgp

**Usage**

  nv set vrf <vrf-id> router ospf redistribute bgp [options] [<attribute> ...]



  Source route type.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

  metric       Metric value for destination routing protocol

  metric-type  Set OSPF External Type 1/2 metrics

  route-map    Optional policy to apply to this advertisement

## nv set vrf <vrf-id> router ospf redistribute bgp metric-type 1-2

**Usage**

  nv set vrf <vrf-id> router ospf redistribute bgp metric-type [options] 1-2



  Set OSPF External Type 1/2 metrics

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> router ospf timers

**Usage**

  nv set vrf <vrf-id> router ospf timers [options] [<attribute> ...]



  Timers

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  lsa         LSA timers

  spf         SPF timers

  refresh     defines interval (sec) to re-send lsas to keep from aging out. If 'auto', inherited from global. This is the default.

## nv set vrf <vrf-id> router ospf timers lsa


**Usage**

  nv set vrf <vrf-id> router ospf timers lsa [options] [<attribute> ...]



  LSA timers

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>     VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  min-arrival  Minimum delay in receiving new version of a LSA. If 'auto', inherited from global. This is the default.

  throttle     Delay (msec) between sending LSAs. If 'auto', inherited from  global. This is the default.

## nv set vrf <vrf-id> router ospf timers spf

**Usage**

  nv set vrf <vrf-id> router ospf timers spf [options] [<attribute> ...]



  SPF timers

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>      VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  delay         Delay (msec) from first change received till SPF calculation. If 'auto', inherited from global. This is the default.

  holdtime      Initial hold time (msec) between consecutive SPF calculations. If 'auto', inherited from global. This is the default.

  max-holdtime  Maximum hold time (msec) between consecutive SPF calculations. If 'auto', inherited from global. This is the default.

## nv set vrf <vrf-id> router ospf reference-bandwidth 1-4294967

**Usage**

  nv set vrf <vrf-id> router ospf reference-bandwidth [options] 1-4294967



  Used to determine link cost/metric value relative to defined reference.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set vrf <vrf-id> ptp

**Usage**

  nv set vrf <vrf-id> ptp [options] [<attribute> ...]



  VRF PTP configuration.  Inherited by interfaces in this VRF.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  enable      Turn the feature 'on' or 'off'. The default is 'on'.

## nv set vrf <vrf-id> table auto

**Usage**

  nv set vrf <vrf-id> table [options] auto



  The routing table number, between 1001-1255, used by the named VRF. If auto, the default, it will be auto generated.

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <vrf-id>    VRF

## nv set nve

**Usage**

  nv set nve [options] [<attribute> ...]



  Network Virtualization configuration and operational info

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  vxlan       Global VxLAN configuration and operational properties.

## nv set nve vxlan

**Usage**

  nv set nve vxlan [options] [<attribute> ...]



  VxLAN

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  mlag             VxLAN specific MLAG address

  source           Source address

  flooding         Configuration to specify how BUM traffic in the overlay is handled. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.

  enable           Turn the feature 'on' or 'off'. The default is 'off'.

  arp-nd-suppress  Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs).

  mac-learning     Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.

  mtu              interface mtu

  port             UDP port for VXLAN frames

## nv set nve vxlan mlag

**Usage**

  nv set nve vxlan mlag [options] [<attribute> ...]



  VxLAN specfic MLAG configuration

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  shared-address  shared anycast address for MLAG peers

## nv set nve vxlan source

**Usage**

  nv set nve vxlan source [options] [<attribute> ...]



  Source address

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  address     IP addresses of this node's VTEP or 'auto'. If 'auto', use the primary IP loopback (not 127.0.0.1). This is the default.

## nv set nve vxlan flooding

**Usage**

  nv set nve vxlan flooding [options] [<attribute> ...]



  Handling of BUM traffic

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  head-end-replication  BUM traffic is replicated and individual copies sent to remote destinations.

  enable                Turn the feature 'on' or 'off'. The default is 'off'.

  multicast-group       BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.

## nv set nve vxlan flooding head-end-replication <hrep-id>

**Usage**

  nv set nve vxlan flooding head-end-replication <hrep-id> [options]



  Set of IPv4 unicast addresses or "evpn".

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <hrep-id>   IPv4 unicast addresses or "evpn"

## nv set nve vxlan flooding multicast-group <ipv4-multicast>

**Usage**

  nv set nve vxlan flooding multicast-group [options] <ipv4-multicast>



  BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.

## nv set nve vxlan port 1024-65535

**Usage**

  nv set nve vxlan port [options] 1024-65535



  UDP port for VXLAN frames

## nv set nve vxlan mtu 552-9216

**Usage**

  nv set nve vxlan mtu [options] 552-9216



  interface mtu

## nv set acl <acl-id>

**Usage**

  nv set acl <acl-id> [options] [<attribute> ...]



  An ACL is used for matching packets and take actions

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  rule        acl rule

  type        acl type

## nv set acl <acl-id> rule <rule-id>

**Usage**

  nv set acl <acl-id> rule <rule-id> [options] [<attribute> ...]



  ACL Matching criteria and action rule

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  match       ACL match criteria

  action      ACL action

## nv set acl <acl-id> rule <rule-id> match

**Usage**

  nv set acl <acl-id> rule <rule-id> match [options] [<attribute> ...]



  An ACL match

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  ip          IPv4 and IPv6 match

  mac         MAC match

## nv set acl <acl-id> rule <rule-id> match ip

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]



  An ACL IPv4/IPv6 match

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>     ACL ID
  <rule-id>    ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  source-port  source port

  dest-port    destination port

  fragment     Fragment packets

  ecn          ECN protocol packet match

  tcp          TCP protocol packet match

  dest-ip      Destination IP address

  dscp         DSCP

  icmp-type    ICMP message type

  icmpv6-type  ICMPv6 message type

  protocol     IP protocol

  source-ip    Source IP address

## nv set acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]



  L4 port

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>      ACL ID
  <rule-id>     ACL rule number
  <ip-port-id>  IP port ID

## nv set acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]



  L4 port

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>      ACL ID
  <rule-id>     ACL rule number
  <ip-port-id>  IP port ID

## nv set acl <acl-id> rule <rule-id> match ip fragment

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip fragment [options]



  State details

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> match ip ecn

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]



  ECN

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  flags       ECN protocol flags

  ip-ect      IP ECT

## nv set acl <acl-id> rule <rule-id> match ip ecn ip-ect 0-3

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip ecn ip-ect [options] 0-3



  IP ECT

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> match ip tcp

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]



  L4 port

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  flags       TCP protocol flags

  mask        TCP protocol flag mask

  state       TCP state

## nv set acl <acl-id> rule <rule-id> match ip tcp state established

**Usage**

  nv set acl <acl-id> rule <rule-id> match ip tcp state [options] established



  TCP state

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> match mac

**Usage**

  nv set acl <acl-id> rule <rule-id> match mac [options] [<attribute> ...]



  An ACL MAC match

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>         ACL ID
  <rule-id>        ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  dest-mac         Destination MAC address

  dest-mac-mask    Destination MAC address mask

  protocol         MAC protocol

  source-mac       Source MAC address

  source-mac-mask  Source MAC address mask

  vlan             VLAN ID

## nv set acl <acl-id> rule <rule-id> match mac source-mac-mask <mac>


**Usage**

  nv set acl <acl-id> rule <rule-id> match mac source-mac-mask [options] <mac>



  Source MAC address mask

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> match mac dest-mac-mask <mac>

**Usage**

  nv set acl <acl-id> rule <rule-id> match mac dest-mac-mask [options] <mac>



  Destination MAC address mask

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> match mac vlan 1-4094

**Usage**

  nv set acl <acl-id> rule <rule-id> match mac vlan [options] 1-4094



  VLAN ID

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action

**Usage**

  nv set acl <acl-id> rule <rule-id> action [options] [<attribute> ...]



  ACL rule action

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |


  permit      Permit action

  deny        Deny action

  log         Provides ACL logging facility

  set         Modify the packet with appropriate values

  erspan      ERSPAN session

  police      policing of packets/bytes

  span        SPAN session

## nv set acl <acl-id> rule <rule-id> action permit

**Usage**

  nv set acl <acl-id> rule <rule-id> action permit [options]



  Permit packets

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action deny


**Usage**

  nv set acl <acl-id> rule <rule-id> action deny [options]



  deny packets

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action log

**Usage**

  nv set acl <acl-id> rule <rule-id> action log [options]



  log packets

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action set

**Usage**

  nv set acl <acl-id> rule <rule-id> action set [options] [<attribute> ...]



  Set action for packets

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  class       Sets the class value for classification of the packet

  cos         Set the CoS value

  dscp        Sets/Modifies the DSCP value in the packet

## nv set acl <acl-id> rule <rule-id> action set class 0-7

**Usage**

  nv set acl <acl-id> rule <rule-id> action set class [options] 0-7



  Sets the class value for classification of the packet

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action set cos 0-7

**Usage**

  nv set acl <acl-id> rule <rule-id> action set cos [options] 0-7



  Set the CoS value

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action erspan


**Usage**

  nv set acl <acl-id> rule <rule-id> action erspan [options] [<attribute> ...]



  ERSPAN session

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  dest-ip     Destination IP address

  source-ip   Source IP address

  ttl         Time to Live

## nv set acl <acl-id> rule <rule-id> action erspan ttl 1-255

**Usage**

  nv set acl <acl-id> rule <rule-id> action erspan ttl [options] 1-255



  Time to Live

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action police

**Usage**

  nv set acl <acl-id> rule <rule-id> action police [options] [<attribute> ...]



  Policing of matched packets/bytes

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

**Attributes**

| Atrribute |  Description   |
| ---------  | -------------- |

  burst       Policing burst value

  mode        Policing mode

  rate        Policing rate value

## nv set acl <acl-id> rule <rule-id> action police burst 1-2147483647


**Usage**

  nv set acl <acl-id> rule <rule-id> action police burst [options] 1-2147483647



  Policing burst value

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action police rate 1-2147483647

**Usage**

  nv set acl <acl-id> rule <rule-id> action police rate [options] 1-2147483647



  Policing rate value

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv set acl <acl-id> rule <rule-id> action span <interface-name>

**Usage**

  nv set acl <acl-id> rule <rule-id> action span [options] <interface-name>



  SPAN session

**Identifiers**

| Identifier |  Description   |
| ---------  | -------------- |

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
