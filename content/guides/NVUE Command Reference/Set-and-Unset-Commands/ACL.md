---
title: ACL
author: Cumulus Networks
weight: 500
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set system acl

Configures Access Control lists (ACLs) on the switch.

- - -

## nv set system acl mode

Configures the ACL mode; atomic or non-atomic.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system acl mode atomic
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip source-port

Configures the IP source port match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip source-port 22
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip dest-port \<ip-port-id\>

Configures the IP destination port match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<ip-port-id>` |  The IP port number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip dest-port 22
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip fragment

Configures IP fragment packet match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip fragment 
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip ecn ip-ect

Configures the ACL to match on the ECT bit. The ECT codepoints negotiate if the connection is ECN capable by setting one of the two bits to 1. Routers also use the ECT bit to indicate that they are experiencing congestion by setting both the ECT codepoints to 1.

By default, ECN rules match a packet with the bit set. You can reverse the match by using an explanation point (!).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip ecn flags ip-ect
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip ecn tcp-cwr

Configures the ACL to match on the CWR bit (Window Reduced). The CWR bit notifies the other endpoint of the connection that it received and reacted to an ECE.

By default, ECN rules match a packet with the bit set. You can reverse the match by using an explanation point (!).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip ecn flags tcp-cwr
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip ecn tcp-ece

Configures the ACL to match on the ECE bit. After an endpoint receives a packet with the CE bit set by a router, it sets the ECE bit in the returning ACK packet to notify the other endpoint that it needs to slow down.

By default, ECN rules match a packet with the bit set. You can reverse the match by using an explanation point (!).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip ecn flags tcp-ece
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip tcp flags

Configures the IP TCP flag you want match in the packet. You can specify: `ack`, `all`, `fin`, `none`, `psh`, `rst`, `syn`, or `urg`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip tcp flags syn
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip tcp mask

Configures the IP TCP mask you want to match in the packet.  You can specify: `ack`, `all`, `fin`, `none`, `psh`, `rst`, `syn`, or `urg`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip tcp mask ack
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip tcp state established

Configures the TCP established state you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip tcp state established
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip source-ip \<ip-address\>

Configures the source IP address you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address-id>` | The source IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip source-ip 10.0.14.2/32
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip dest-ip \<ip-address\>

Configures the destination IP address you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address>` | The destination IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip dest-ip 10.0.15.8/32
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip protocol

Configures the IP protocol you want to match. You can specify `tcp`, `udp`, `ospf`, `pim`, `icmp`, `icmpv6`, or `igmp`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip dscp

Configures the DSCP value you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip dscp af13
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip icmp-type

Configures the IP ICMP type you want to match. You can specify: `dest-unreachable`, `echo-reply`, `echo-request`, `port-unreachable`, or `time-exceeded`. Alternatively, you can specify an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip icmp-type dest-unreachable
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match ip icmpv6-type

Configures the IP ICMPv6 type you want to match. You can specify: `router-solicitation`, `router-advertisement`, `neighbor-solicitation`, or `neighbor-advertisement`. Alternatively, you can specify an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match ip icmpv6-type router-advertisement
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match mac source-mac \<source-mac\>

Configures the source MAC address you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<source-mac>` |  The source MAC address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match mac source-mac any
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match mac source-mac-mask \<source-mac-mask\>

Configure the source MAC address mask you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<source-mac-mask>` |  The source MAC address mask. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match mac source-mac-mask 00:00:00:00:00:12
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match mac dest-mac \<mac-address\>

Configures the destination MAC address you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<mac-address>` |  The destination MAC address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match mac dest-mac any
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match mac dest-mac-mask \<mac\>

Configures the destination MAC address mask you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<mac>` |  The destination MAC address mask. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match mac dest-mac-mask 00:00:00:00:00:12
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match mac protocol

configures the MAC protocol you want to match. You can specify `ANY`, `arp`, `ipv4`, or `ipv6`. Alternatively you can specify a value between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match mac protocol ipv4
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> match mac vlan \<vlan-id\>

Configures the VLAN ID to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<vlan-id>` |  The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 match mac vlan 10
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action permit

Configures a permit action to permit packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action permit
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action deny

Configures a deny action to deny packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action deny
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action log

Configures logging for ACLs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action log
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action log log-prefix \<prefix\>

Configures logging for packets with a specific prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<prefix>`|  The prefix with which you want to log matching packets. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action log log-prefix 10.10.10.1/32
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action set class

Modifies the class value for packet classification.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action set class 3
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action set dscp

Configures the DSCP value to modify in the packet.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action set dscp af12
```

- - -

## nv set acl \<acl-id\> rule\<rule-id\> action set cos

Configures the 802.1p CoS value to modify in the packet.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action set cos 6
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action erspan source-ip

Configures the ERSPAN source IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action erspan source-ip 10.10.10.10
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action erspan dest-ip

Configures the ERSPAN destination IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action erspan dest-ip 10.10.10.3
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action erspan ttl

Configures the ERSPAN Time to Live (TTL). You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action erspan ttl 200
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action police mode

Configures quality of service for traffic on the data plane. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the traffic mode. You can specify `packet`, `kbps`, `mbps` or `gbps`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action police mode mbps
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action police burst

Configures quality of service for traffic on the data plane. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the police burst rate; the number of packets or kilobytes (KB) allowed to arrive sequentially. You can specify a value between 1 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action police burst 1000
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action police rate

Configures quality of service for traffic on the data plane. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the policing rate. You can specify a value between 1 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action police rate 2000
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action police class

Configures quality of service for traffic on the data plane. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the police action class. You can specify an integer between 0 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action police class 5
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> action span \<interface-name\>

Configures the SPAN session.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 action span swp1
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> remark

Configures an ACL rule remark (description) about deny or permit conditions in the rule. You must enclose multiple words in double quotes (").

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 remark "The following line permits TCP packets"
```

- - -

## nv set acl \<acl-id\> rule \<rule-id\> type

Configures the ACL rule type. You can specify `ipv4`, `ipv6` or `mac`.

This command is required when configuring other ACL settings.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set acl EXAMPLE1 rule 10 type ipv4
```

- - -

## nv set interface \<interface-id\> acl \<acl-id\> inbound

Configures the ACL rule to apply in the inbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 inbound
```

- - -

## nv set interface \<interface-id\> acl \<acl-id\> inbound control-plane

Configures the ACL rule to apply to a control plane interface in the inbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 inbound control-plane
```

- - -

## nv set interface \<interface-id\> acl \<acl-id\> outbound

Configures the ACL rule to apply in the outbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 outbound 
```

- - -

## nv set interface \<interface-id\> acl \<acl-id\> outbound control-plane

Configures the ACL rule to apply to a control plane interface in the outbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The name of the ACL. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 acl EXAMPLE1 outbound control-plane
```

- - -
