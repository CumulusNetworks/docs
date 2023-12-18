---
title: NAT
author: Cumulus Networks
weight: 215

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat</h>

Shows NAT destination rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip</h>

Shows NAT destination translate IP address rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip \<ip-address\> to \<ip-address\></h>

Shows NAT destination translate IP address range rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-ip 172.30.58.0 to 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port</h>

Shows the NAT destination translate port rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port <port-id></h>

Shows the NAT destination translate rule for a specific port.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<port-id>` | The port number. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-port 6000
```
