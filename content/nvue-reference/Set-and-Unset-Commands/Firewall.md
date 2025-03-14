---
title: Firewall
author: Cumulus Networks
weight: 565

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action deny</h>

Configures a deny action for the firewall DoS rule to deny packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action deny
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action dest-nat translate-ip \<range-id\></h>

Configures an IP address destination <span class="a-tooltip">[NAT](## "Network Address Translation")</span> for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<range-id>` |  The IPv4 range; for example, `<ip-address> to <ip-address>`|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action dest-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action dest-nat translate-port \<port-id\></h>

Configures a port destination <span class="a-tooltip">[NAT](## "Network Address Translation")</span> firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<port-id>` |  The port ID or port range.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action dest-nat translate-port 22
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action erspan dest-ip</h>

Configures the ERSPAN destination IP address for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action erspan dest-ip 10.10.10.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action erspan source-ip</h>

Configures the ERSPAN source IP address for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action erspan dest-ip 10.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action erspan ttl</h>

Configures the ERSPAN Time to Live (TTL) for the firewall DoS rule. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action erspan ttl 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action log level</h>

Configures the log level for the firewall DoS rule. You can specify a value between 1 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action log level 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action log log-prefix \<prefix\></h>

Configures logging for packets with a specific prefix for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<prefix>` |  The prefix with which you want to log matching packets. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action log log-prefix 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action log rate</h>

Configures the number of logs per minute you want to generate for the firewall DoS rule. You can set a value between 1 and 50000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action log rate 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action permit </h>

Configures a permit action to permit packets for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action police burst</h>

Configures quality of service for traffic for the firewall DoS rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the police burst rate; the number of packets or kilobytes (KB) allowed to arrive sequentially. You can specify a value between 1 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action police burst 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action police class</h>

Configures quality of service for traffic for the firewall DoS rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the police action class. You can specify an integer between 0 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action police class 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action police mode</h>

Configures quality of service for traffic for the firewall DoS rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the traffic mode. You can specify packet, kbps, mbps or gbps.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action police mode mbps
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action police rate</h>

Configures quality of service for traffic for the firewall DoS rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the policing rate. You can specify a value between 1 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action police rate 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action recent</h>

Configures the firewall DoS rule to be the most recent.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action recent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action set class</h>

Modifies the class value for packet classification for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action set class 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action set cos</h>

Configures the 802.1p CoS value to modify in the packet for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action set cos 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action set dscp</h>

Configures the DSCP value to modify in the packet for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action set dscp af12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action source-nat translate-ip \<range-id\></h>

Configures a dynamic NAT action DoS rule to translate a source IP address range to a public address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<range-id>` |  The IP address range; for example, `<ip-address> to <ip-address>`. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action source-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action source-nat translate-port \<port-id\></h>

Configures a NAT action DoS rule to translate a source IP port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<port-id>` |  The port number or range of ports (separated with a `-`). |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action source-nat translate-port 1024-1200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> action span \<interface-id\></h>

Configures the SPAN session for the specified interface for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 action span swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip connection-state </h>

Configures the connection state you want to match for the firewall DoS rule. You can set the value to `established`, `related`, `new`, or `invalid`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip connection-state related
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip dest-ip \<ip-address-id\></h>

Configures the destination IP address you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address-id>` |  The destination IP address. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip dest-ip 10.0.15.8/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip dscp</h>

Configures the DSCP value you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip dscp af13
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip ecn flags tcp-cwr</h>

Configures the firewall DoS rule to match on the TCP Congestion Window Reduced Flag.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip ecn flags tcp-cwr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip ecn flags tcp-ece</h>

Configures the firewall DoS rule to match on the TCP ECN Echo Flag.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip ecn flags tcp-ece
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip ecn ip-ect</h>

Configures the firewall DoS rule to match on the ECT bit. The ECT codepoints negotiate if the connection is ECN capable by setting one of the two bits to 1. Routers also use the ECT bit to indicate that they are experiencing congestion by setting both the ECT codepoints to 1.

By default, ECN rules match a packet with the bit set. You can reverse the match by using an explanation point (!).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip ecn ip-ect
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip fragment</h>

Configures IP fragment packet match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip fragment
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip hashlimit burst</h>

Configures the hashlimit burst rate you want to match for the firewall DoS rule. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip hashlimit burst 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip hashlimit destination-mask</h>

Configures the hashlimit destination mask you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip hashlimit destination-mask 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip hashlimit expire</h>

Configures the hashlimit expire time (in milliseconds) you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip hashlimit expire 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip hashlimit mode</h>

Configures the hashlimit mode you want to match for the firewall DoS rule. You can specify `src-ip` or `dst-ip`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip hashlimit mode dst-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip hashlimit name</h>

Configures the hashlimit name you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip hashlimit name SSH
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip hashlimit rate-above</h>

Configures how much above the hashlimit rate you want to match for the firewall DoS rule. You can specify an `<integer>/second`, `<integer>/min`, or `<integer>/hour`. The maximum rate is `1000000/second`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip hashlimit rate-above 1000/min
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip hashlimit source-mask</h>

Configures the hashlimit source mask you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip hashlimit source-mask 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip icmp-type</h>

Configures the IP ICMP type you want to match for the firewall DoS rule. You can specify: dest-unreachable, echo-reply, echo-request, port-unreachable, time-exceeded, or an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip icmp-type dest-unreachable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip icmpv6-type</h>

Configures the IP ICMPv6 type you want to match for the firewall DoS rule. You can specify `router-solicitation`, `router-advertisement`, `neighbor-solicitation`, `neighbor-advertisement`, or an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip icmpv6-type router-solicitation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip protocol</h>

Configures the IP protocol you want to match for the firewall DoS rule. You can specify `tcp`, `udp`, `ospf`, `pim`, `icmp`, `icmpv6`, or `igmp`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip protocol tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip recent-list action</h>

Configures the IP recent list action you want to match for the firewall DoS rule. You can specify `set` or `update`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip recent-list action update
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip recent-list hit-count</h>

Configures the IP recent list hit count you want to match for the firewall DoS rule. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip recent-list hit-count 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip recent-list name</h>

Configures the IP recent list name you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip recent-list name list1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip recent-list update-interval</h>

Configures the IP recent list update interval you want to match for the firewall DoS rule. You can specify a value between 1 and 4294967295

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip recent-list update-interval 1000 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip source-ip</h>

Configures the source IP address you want to match for the firewall DoS rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip source-ip 10.0.14.2/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip tcp all-mss-except</h>

Configures the firewall DoS rule to match all TCP maximum segment size (MSS) values except for the specified value.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip tcp all-mss-except 536
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip tcp flags</h>

Configures the IP TCP flag you want match in the packet for the firewall DoS rule. You can specify `ack`, `all`, `fin`, `none`, `psh`, `rst`, `syn`, or `urg`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip tcp flags syn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip tcp mask</h>

Configures the IP TCP mask you want match in the packet for the firewall DoS rule. You can specify `ack`, `all`, `fin`, `none`, `psh`, `rst`, `syn`, or `urg`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip tcp mask ack
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip tcp mss</h>

Configures the TCP maximum segment size (MSS) you want match in the packet for the firewall DoS rule. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip tcp mss 536
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip tcp state established</h>

Configures the firewall DoS rule to match on the TCP established state.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip tcp state established 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip ttl</h>

Configures the firewall DoS rule to match on the IP TTL.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip ttl 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip udp dest-port</h>

Configures the firewall DoS rule to match on the specified IP UDP destination port. You can specify `ANY`,`bootps`, `http`, `ntp`, `telnet`, `bfd`, `clag`, `https`, `pop3`, `tftp`, `bfd-echo`, `dhcp-client`, `imap2`, `smtp`, `bfd-multihop`, `dhcp-server`, `ldap`, `snmp`, `bgp`, `domain`, `ldaps`, `snmp-trap`, `bootpc`, `ftp`, `msdp`, or `ssh`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip udp dest-port https
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match ip udp source-port</h>

Configures the firewall DoS rule to match on the specified IP UDP source port. You can specify `ANY`,`bootps`, `http`, `ntp`, `telnet`, `bfd`, `clag`, `https`, `pop3`, `tftp`, `bfd-echo`, `dhcp-client`, `imap2`, `smtp`, `bfd-multihop`, `dhcp-server`, `ldap`, `snmp`, `bgp`, `domain`, `ldaps`, `snmp-trap`, `bootpc`, `ftp`, `msdp`, or `ssh`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match ip udp source-port https
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match mac dest-mac</h>

Configures the firewall DoS rule to match on the specified destination MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match mac dest-mac any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match mac dest-mac-mask</h>

Configures the firewall DoS rule to match on the specified destination MAC address mask.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match mac dest-mac-mask 00:00:00:00:00:12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match mac protocol</h>

Configures the firewall DoS rule to match on the specified destination MAC protocol. You can specify `ANY`, `arp`, `ipv4`, `ipv6`, or a value between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match mac protocol arp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match mac source-mac</h>

Configures the firewall DoS rule to match on the specified source MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match mac source-mac any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match mac source-mac-mask</h>

Configures the firewall DoS rule to match on the specified source MAC address mask.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match mac source-mac-mask any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> match vlan</h>

Configures the firewall DoS rule to match on the specified VLAN ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 match vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-dos rule \<rule-id\> remark</h>

Configures a remark (description) about deny or permit conditions in the firewall DoS rule. You must enclose multiple words in double quotes (").

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-dos rule 10 remark "The following line permits TCP packets"
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action deny</h>

Configures a deny action for the firewall whitelist rule to deny packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action deny
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action dest-nat translate-ip \<range-id\></h>

Configures an IP address destination <span class="a-tooltip">[NAT](## "Network Address Translation")</span> for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<range-id>` |  The IPv4 range; for example, `<ip-address> to <ip-address>`|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action dest-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action dest-nat translate-port \<port-id\></h>

Configures a port destination <span class="a-tooltip">[NAT](## "Network Address Translation")</span> for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<port-id>` |  The port ID or port range.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action dest-nat translate-port 22
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action erspan dest-ip</h>

Configures the ERSPAN destination IP address for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action erspan dest-ip 10.10.10.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action erspan source-ip</h>

Configures the ERSPAN source IP address for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action erspan source-ip 10.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action erspan ttl</h>

Configures the ERSPAN Time to Live (TTL) for the firewall whitelist rule. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action erspan ttl 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action log</h>

Configures logging for the firewall whitelist rule.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action log level</h>

Configures the log level for the firewall whitelist rule. You can specify a value between 1 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action log level 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action log log-prefix \<prefix\></h>

Configures logging for packets with a specific prefix for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<prefix>` |  The prefix with which you want to log matching packets. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action log log-prefix 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action log rate</h>

Configures the number of logs per minute you want to generate for the firewall whitelist rule. You can set a value between 1 and 50000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action log rate 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action permit </h>

Configures a permit action to permit packets for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action police burst</h>

Configures quality of service for traffic for the firewall whitelist rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the police burst rate; the number of packets or kilobytes (KB) allowed to arrive sequentially. You can specify a value between 1 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action police burst 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action police class</h>

Configures quality of service for traffic for the firewall whitelist rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the police action class. You can specify an integer between 0 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action police class 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action police mode</h>

Configures quality of service for traffic for the firewall whitelist rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the traffic mode. You can specify `packet`, `kbps`, `mbps`, or `gbps`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action police mode mbps
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action police rate</h>

Configures quality of service for traffic for the firewall whitelist rule. Using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds. This command configures the policing rate. You can specify a value between 1 and 2147483647.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action police rate 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action recent</h>

Configures the firewall whitelist rule to be the most recent.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action recent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action set class</h>

Modifies the class value for packet classification for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action set class 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action set cos</h>

Configures the 802.1p CoS value to modify in the packet for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action set cos 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action set dscp</h>

Configures the DSCP value to modify in the packet for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action set dscp af12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action source-nat translate-ip \<range-id\></h>

Configures a dynamic NAT action whitelist rule to translate a source IP address range to a public address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<range-id>` |  The IP address range; for example, `<ip-address> to <ip-address>`. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action source-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action source-nat translate-port \<port-id\></h>

Configures a NAT action whitelist rule to translate a source IP port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<port-id>` |  The port number or range of ports (separated with a `-`). |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action source-nat translate-port 1024-1200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> action span \<interface-id\></h>

Configures the SPAN session for the specified interface for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<interface-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 action span swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip connection-state </h>

Configures the connection state you want to match for the firewall whitelist rule. You can set the value to `established`, `related`, `new`, or `invalid`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip connection-state related
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip dest-ip \<ip-address-id\></h>

Configures the destination IP address you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address-id>` |  The destination IP address. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip dest-ip 10.0.15.8/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip dscp</h>

Configures the DSCP value you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip dscp af13
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip ecn flags tcp-cwr</h>

Configures the firewall whitelist rule to match on the TCP Congestion Window Reduced Flag.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip ecn flags tcp-cwr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip ecn flags tcp-ece</h>

Configures the firewall whitelist rule to match on the TCP ECN Echo Flag.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip ecn flags tcp-ece
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip ecn ip-ect</h>

Configures the firewall whitelist rule to match on the ECT bit. The ECT codepoints negotiate if the connection is ECN capable by setting one of the two bits to 1. Routers also use the ECT bit to indicate that they are experiencing congestion by setting both the ECT codepoints to 1.

By default, ECN rules match a packet with the bit set. You can reverse the match by using an explanation point (!).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip ecn ip-ect
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip fragment</h>

Configures IP fragment packet match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip fragment
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip hashlimit burst</h>

Configures the hashlimit burst rate you want to match for the firewall whitelist rule. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip hashlimit burst 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip hashlimit destination-mask</h>

Configures the hashlimit destination mask you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip hashlimit destination-mask 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip hashlimit expire</h>

Configures the hashlimit expire time (in milliseconds) you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip hashlimit expire 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip hashlimit mode</h>

Configures the hashlimit mode you want to match for the firewall whitelist rule. You can specify `src-ip` or `dst-ip`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip hashlimit mode dst-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip hashlimit name</h>

Configures the hashlimit name you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip hashlimit name SSH
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip hashlimit rate-above</h>

Configures how much above the hashlimit rate you want to match for the firewall whitelist rule. You can specify an `<integer>/second`, `<integer>/min`, or `<integer>/hour`. The maximum rate is `1000000/second`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip hashlimit rate-above 1000/min
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip hashlimit source-mask</h>

Configures the hashlimit source mask you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip hashlimit source-mask 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip icmp-type</h>

Configures the IP ICMP type you want to match for the firewall whitelist rule. You can specify: dest-unreachable, echo-reply, echo-request, port-unreachable, time-exceeded, or an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip icmp-type dest-unreachable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip icmpv6-type</h>

Configures the IP ICMPv6 type you want to match for the firewall whitelist rule. You can specify `router-solicitation`, `router-advertisement`, `neighbor-solicitation`, `neighbor-advertisement`, or an integer between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip icmpv6-type router-solicitation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip protocol</h>

Configures the IP protocol you want to match for the firewall whitelist rule. You can specify `tcp`, `udp`, `ospf`, `pim`, `icmp`, `icmpv6`, or `igmp`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip protocol tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip recent-list action</h>

Configures the IP recent list action you want to match for the firewall whitelist rule. You can specify `set` or `update`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip recent-list action update
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip recent-list hit-count</h>

Configures the IP recent list hit count you want to match for the firewall whitelist rule. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip recent-list hit-count 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip recent-list name</h>

Configures the IP recent list name you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip recent-list name list1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip recent-list update-interval</h>

Configures the IP recent list update interval you want to match for the firewall whitelist rule. You can specify a value between 1 and 4294967295

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip recent-list update-interval 1000 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip source-ip</h>

Configures the source IP address you want to match for the firewall whitelist rule.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip source-ip 10.0.14.2/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip tcp all-mss-except</h>

Configures the firewall whitelist rule to match all TCP maximum segment size (MSS) values except for the specified value.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip tcp all-mss-except 536
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip tcp flags</h>

Configures the IP TCP flag you want match in the packet for the firewall whitelist rule. You can specify `ack`, `all`, `fin`, `none`, `psh`, `rst`, `syn`, or `urg`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip tcp flags syn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip tcp mask</h>

Configures the IP TCP mask you want match in the packet for the firewall whitelist rule. You can specify `ack`, `all`, `fin`, `none`, `psh`, `rst`, `syn`, or `urg`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip tcp mask ack
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip tcp mss</h>

Configures the TCP maximum segment size (MSS) you want match in the packet for the firewall whitelist rule. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip tcp mss 536
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip tcp state established</h>

Configures the firewall whitelist rule to match on the TCP established state. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip tcp state established 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip ttl</h>

Configures the firewall whitelist rule to match on the IP TTL. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip ttl 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip udp dest-port</h>

Configures the firewall whitelist rule to match on the specified IP UDP destination port. You can specify `ANY`,`bootps`, `http`, `ntp`, `telnet`, `bfd`, `clag`, `https`, `pop3`, `tftp`, `bfd-echo`, `dhcp-client`, `imap2`, `smtp`, `bfd-multihop`, `dhcp-server`, `ldap`, `snmp`, `bgp`, `domain`, `ldaps`, `snmp-trap`, `bootpc`, `ftp`, `msdp`, or `ssh`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip udp dest-port https
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match ip udp source-port</h>

Configures the firewall whitelist rule to match on the specified IP UDP source port. You can specify `ANY`,`bootps`, `http`, `ntp`, `telnet`, `bfd`, `clag`, `https`, `pop3`, `tftp`, `bfd-echo`, `dhcp-client`, `imap2`, `smtp`, `bfd-multihop`, `dhcp-server`, `ldap`, `snmp`, `bgp`, `domain`, `ldaps`, `snmp-trap`, `bootpc`, `ftp`, `msdp`, or `ssh`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match ip udp source-port https
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match mac dest-mac</h>

Configures the firewall whitelist rule to match on the specified destination MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match mac dest-mac any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match mac dest-mac-mask</h>

Configures the firewall whitelist rule to match on the specified destination MAC address mask.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match mac dest-mac-mask 00:00:00:00:00:12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match mac protocol</h>

Configures the firewall whitelist rule to match on the specified destination MAC protocol. You can specify `ANY`, `arp`, `ipv4`, `ipv6`, or a value between 0 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |
| ---------  | -------------- |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match mac protocol arp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match mac source-mac</h>

Configures the firewall whitelist rule to match on the specified source MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match mac source-mac any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match mac source-mac-mask</h>

Configures the firewall whitelist rule to match on the specified source MAC address mask.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match mac source-mac-mask any
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> match vlan</h>

Configures the firewall whitelist rule to match on the specified VLAN ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 match vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl acl-default-whitelist rule \<rule-id\> remark</h>

Configures a remark (description) about deny or permit conditions in the firewall whitelist rule. You must enclose multiple words in double quotes (").

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 10 remark "The following line permits TCP packets"
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane acl acl-default-dos inbound</h>

Enables or disables the Cumulus Linux default Dos firewall rules that protect the switch control plane and CPU from DOS attacks. Cumulus Linux provides firewall DoS rules to:
- Allow only internal traffic to the loopback interfaces.
- Accept already established connections and outbound traffic.
- Set the - allow option to color the packets from a specific interface. Used when different policies - need to be applied for different eth interfaces.
- Drop packets if the first TCP segment is not SYN.
- Drop fragmented IP packets.
- Drop Christmas tree packets; packets with all TCP flags set.
- Drop NULL packets.
- Drop invalid packets.
- Drop strange MSS values.
- Provide brute-force protection.
- Drop packets with routing Header Type 0.
- Drop packets with a hop limit greater than 1.
- Limit excessive TCP reset packets.
- Protect against SYN flood.
- Rate limit new TCP connections for each IP address.
- Log all remaining packets, then drop them.

In Cumulus Linux 5.8 and earlier, the set of default firewall rules are more open; Cumulus Linux accepts packets from all addresses and protocols. Cumulus Linux 5.9 and later provides a set of default firewall rules that allows only specific addresses and ports, and drops packets that are disallowed.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv unset system control-plane acl acl-default-dos inbound 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane acl acl-default-whitelist inbound</h>

Enables or disables the Cumulus Linux default whitelist firewall rules that specify the services or application ports enabled on the switch. Cumulus Linux provides firewall whitelist rules to enable TCP ports and UDP ports.

In Cumulus Linux 5.8 and earlier, the set of default firewall rules are more open; Cumulus Linux accepts packets from all addresses and protocols. Cumulus Linux 5.9 and later provides a set of default firewall rules that allows only specific addresses and ports, and drops packets that are disallowed.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv unset system control-plane acl acl-default-whitelist inbound
```
