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
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_2 rule 1 action dest-nat translate-ip 10.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip \<ip-address\> to \<ip-address\></h>

Configures a dynamic NAT rule to translate a destination IP address range.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address> to <ip-address>` |  The IP address range. |

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
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl MACL2 rule 1 action dest-nat translate-mac 99:de:fc:32:11:01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port \<port-id\></h>

Configures a NAT action rule to translate a destination port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<port-id>` |  The port number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_4 rule 1 action dest-nat translate-port 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action source-nat translate-ip \<ip-address\></h>

Configures a NAT action rule to translate a source IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address>` |  The IP address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_1 rule 1 action source-nat translate-ip 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action source-nat translate-ip \<ip-address\> to \<ip-address\></h>

Configures a NAT action rule to translate a source IP address range.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<ip-address> to <ip-address>` |  The IP address range. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_1 rule 1 action source-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action source-nat translate-port \<port-id\></h>

Configures a NAT action rule to translate a source port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<port-id>` |  The port number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl acl_3 rule 1 action source-nat translate-port 6000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set acl \<acl-id\> rule \<rule-id\> action source-nat translate-mac \<mac-address\></h>

Configures a NAT action rule to translate a source MAC address to a public address. MAC address translation is equivalent to static NAT but operates at layer 2 on Ethernet frames.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<acl-id>` |   The ACL name. |
| `<rule-id>` |  The ACL rule number. |
| `<mac-address>` |  The MAC address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set acl MACL1 rule 1 action source-nat translate-mac 99:de:fc:32:11:01  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system nat age-poll-interval</h>

Configures the period of inactivity (in minutes) before Cumulus Linux releases a NAT entry from the translation table. You can set a value between 1 and 1440. The default value is 5.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system nat age-poll-interval 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system nat mode dynamic</h>

Enables and disables dynamic NAT mode. Dynamic NAT maps private IP addresses and ports to a public IP address and port range or a public IP address range and port range. Cumulus Linux assigns IP addresses from a pool of addresses dynamically. When the switch releases entries after a period of inactivity, it maps new incoming connections dynamically to the freed up addresses and ports.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system nat mode dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system nat rule-table-size</h>

Configures the maximum number of rules allowed. You can set a value between 64 and 1024. The default value is 64.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system nat rule-table-size 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system nat translate-table-size</h>

Configures the maximum number of dynamic `snat` and `dnat` entries in the translation table. You can set a value between 1024 and 8192. The default value is 1024.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$  nv set system nat translate-table-size 2048
```
