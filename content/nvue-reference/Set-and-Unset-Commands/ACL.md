---
title: ACL
author: Cumulus Networks
weight: 505

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system acl</h>

Configures Access Control lists (ACLs) on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system acl mode</h>

Configures the ACL mode; atomic or non-atomic. The default setting is atomic mode.

Atomic mode limits the number of ACL rules that you can configure. To increase the number of configurable ACL rules, configure the switch to operate in nonatomic mode, which offers better scaling because all TCAM resources actively impact traffic. With atomic updates, half of the hardware resources are on standby and do not actively impact traffic.

Incremental nonatomic updates are table based, so they do not interrupt network traffic when you install new rules.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system acl mode non-atomic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action</h>

Configures the ACL action.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action deny</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action erspan dest-ip</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action erspan dest-ip 10.10.10.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action erspan source-ip</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action erspan source-ip 10.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action erspan ttl</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action erspan ttl 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action log</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action log level</h>

Configures the log level for the specified ACL rule. You can set a value between 0 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action log level 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action log rate</h>

Configures the number of logs per minute you want to generate for the specified ACL rule. You can set a value between 1 and 50000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action log rate 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action log log-prefix \<prefix\></h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action log log-prefix 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action permit</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action recent</h>

Configures the ACL rule to be the most recent.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action recent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action set class</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action set class 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule\<rule-id\> action set cos</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action set cos 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action set dscp</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action set dscp af12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action police burst</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action police burst 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action police class</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action police class 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action police mode</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action police mode mbps
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action police rate</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action police rate 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action source-nat translate-ip</h>

Configures a NAT action rule to translate a source IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_3 rule 1 action source-nat translate-ip 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action source-nat translate-ip \<range-id\> to \<ipv4\></h>

Configures a dynamic NAT action rule to translate a source IP address range to a public address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_1 rule 1 action source-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action source-nat translate-mac \<mac\></h>

Configures MAC address translation to translate a source MAC address to a public address. MAC address translation is equivalent to static NAT but operates at layer 2 on Ethernet frames.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl MACL1 rule 1 action source-nat translate-mac 99:de:fc:32:11:01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action source-nat translate-port</h>

Configures a NAT action rule to translate a source IP port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_2 rule 1 action source-nat translate-port 1024-1200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action span \<interface-name\></h>

Configures the SPAN session for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<interface-name>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action span swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip connection-state</h>

Configures the connection state (control-plane only) you want to match. You can set the value to `established`, `related`, `new`, or `invalid`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip connection-state related
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip dest-ip \<ip-address-id\></h>

Configures the destination IP address you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address-id>` | The destination IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip dest-ip 10.0.15.8/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip dscp</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip dscp af13
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip ecn ip-ect</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip ecn ip-ect
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip ecn tcp-cwr</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip ecn tcp-cwr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip ecn flags tcp-ece</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip ecn flags tcp-ece
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip fragment</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip fragment 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip hashlimit name</h>

Configures the hashlimit name you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit name NAME
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip hashlimit rate-above</h>

Configures how much above the hashlimit rate you want to match. You can specify an `<integer>/second` `<integer>/min`, or `<integer>/hour`. The maximum rate is 1000000 per second.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit rate-above 1000/min
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip hashlimit burst</h>

Configures the hashlimit burst rate you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit burst 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip hashlimit source-mask</h>

Configures the hashlimit source mask you want to match; the source mask used to mask the source IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit source-mask 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip hashlimit destination-mask</h>

Configures the hashlimit destination mask you want to match; the destination mask used to mask the source IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit destination-mask 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip hashlimit expire</h>

Configures the hashlimit expire time (in milliseconds) you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit expire 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip hashlimit mode</h>

Configures the hashlimit mode you want to match. You can specify `src-ip` or `dst-ip`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit mode dst-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip icmp-type</h>

Configures the IP ICMP type you want to match. You can specify: `dest-unreachable`, `echo-reply`, `echo-request`, `port-unreachable`, `time-exceeded`, or an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip icmp-type dest-unreachable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip icmpv6-type</h>

Configures the IP ICMPv6 type you want to match. You can specify: `router-solicitation`, `router-advertisement`, `neighbor-solicitation`, `neighbor-advertisement`, or an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip icmpv6-type router-advertisement
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip protocol</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip recent-list action</h>

Configures the recent list action you want to match. You can specify `set` or `update`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list action update
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip recent-list hit-count</h>

Configures the recent list hit count you want to match. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list hit-count 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip recent-list name</h>

Configures the recent list name you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list name list1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip recent-list update-interval</h>

Configures the recent list update interval you want to match. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list update-interval 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip source-ip \<ip-address\></h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip source-ip 10.0.14.2/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip source-port</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip source-port 22
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip tcp</h>

Configures the IP TCP properties you want match.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip tcp all-mss-except</h>

Configures the switch to match all TCP maximum segment size (MSS) values except for the specified value.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp all-mss-except 536
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip tcp flags</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp flags syn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip tcp mask</h>

Configures the IP TCP mask you want to match in the packet. You can specify: `ack`, `all`, `fin`, `none`, `psh`, `rst`, `syn`, or `urg`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp mask ack
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip tcp mss</h>

Configures the specified TCP maximum segment size (MSS) value you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp mss 536
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match ip tcp state established</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp state established
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match mac dest-mac \<mac-address\></h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match mac dest-mac any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match mac dest-mac-mask \<mac\></h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match mac dest-mac-mask 00:00:00:00:00:12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match mac protocol</h>

Configures the MAC protocol you want to match. You can specify `ANY`, `arp`, `ipv4`, or `ipv6`, or a value between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match mac protocol ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match mac source-mac \<source-mac\></h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match mac source-mac any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match mac source-mac-mask \<source-mac-mask\></h>

Configures the source MAC address mask you want to match.

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match mac source-mac-mask 00:00:00:00:00:12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> match mac vlan \<vlan-id\></h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match mac vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> remark</h>

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
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 remark "The following line permits TCP packets"
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> type</h>

Configures the ACL rule type. You can specify `ipv4`, `ipv6` or `mac`.

You must run this command when configuring other ACL settings.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 type ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> type mac</h>

Configures the ACL type to MAC address for MAC address translation.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl MACL1 type mac
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> acl \<acl-id\> inbound</h>

Configures the ACL rule to apply in the inbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The ACL name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> acl \<acl-id\> inbound control-plane</h>

Configures the ACL rule to apply to a control plane interface in the inbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The ACL name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound control-plane
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> acl \<acl-id\> outbound</h>

Configures the ACL rule to apply in the outbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The ACL name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 outbound 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> acl \<acl-id\> outbound control-plane</h>

Configures the ACL rule to apply to a control plane interface in the outbound direction.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
| `<acl-id>` |   The ACL name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 outbound control-plane
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane acl \<acl-id\></h>

Configures a control plane ACL to apply a single rule for all packets forwarded to the CPU regardless of the source interface or destination interface on the switch. Control plane ACLs allow you to regulate traffic forwarded to applications on the switch with more granularity than traps and to configure ACLs to block SSH from specific addresses or subnets.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane acl \<acl-id\> inbound control-plane</h>

Configures an inbound control plane ACL.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system control-plane acl ACL1 inbound control-plane
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane acl \<acl-id\> outbound control-plane</h>

Configures an outbound control plane ACL.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system control-plane acl ACL1 outbound control-plane
```
