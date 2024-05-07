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

Shows the destination NAT rule settings.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl acl_2 rule 1 action dest-nat
                  operational  applied 
----------------  -----------  --------
[translate-ip]                 10.0.0.1
[translate-port]                      
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip</h>

Shows information about the destination NAT translate IP address rule or rule range for dynamic NAT.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port</h>

Shows information about the destination NAT translate port rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port \<port-id\></h>

Shows information about the destination NAT translate rule for the specified port or range of ports.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<port-id>` | The port number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-port 6000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action source-nat</h>

Shows the source NAT rule settings.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl acl_3 rule 1 action source-nat
                  operational  applied     
----------------  -----------  ------------
[translate-ip]                 172.30.58.80
[translate-port]               6000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action source-nat translate-ip</h>

Shows information about the source NAT translate IP address rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action source-nat translate-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action source-nat translate-ip \<ip-address\></h>

Shows information about the source NAT translate rule for the specified IP address or IP address range.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<ip-address>` | The IP address.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action source-nat translate-ip 172.30.58.80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action source-nat translate-port</h>

Shows information about the source NAT translate port rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action source-nat translate-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action source-nat translate-port \<translate-port-id\></h>

Shows information about the source NAT translate rule for the specified port or port range.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<translate-port-id>` | The port ID or the port range. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action source-nat translate-port 1024-1200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system nat</h>

Shows the current NAT configuration settings on the switch.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$  nv show system nat
                      operational  applied  pending
--------------------  -----------  -------  -------
age-poll-interval                  5        5      
translate-table-size               1024     1024   
rule-table-size                    64       64     
mode                               dynamic  dynamic
```
