---
title: NAT
author: Cumulus Networks
weight: 605

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip</h>

Configures a NAT action rule to translate a destination IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<acl-id\>` |   The ACL name. |
| `\<rule-id\>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_2 rule 1 action dest-nat translate-ip 10.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip \<range-id\> to \<ipv4\></h>

Configures a dynamic NAT rule to translate a destination IP address range.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<acl-id\>` |   The ACL name. |
| `\<rule-id\>` |  The ACL rule number. |
| `\<range-id\>` |  The IP address range. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_4 rule 1 action dest-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action dest-nat translate-mac</h>

Configures MAC address translation to translate a destination MAC address to a public address. MAC address translation is equivalent to static NAT but operates at layer 2 on Ethernet frames.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<acl-id\>` |   The ACL name. |
| `\<rule-id\>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl MACL2 rule 1 action dest-nat translate-mac 99:de:fc:32:11:01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port</h>

Configures a NAT action rule to translate a destination port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<acl-id\>` |   The ACL name. |
| `\<rule-id\>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_4 rule 1 action dest-nat translate-port 5000
```
