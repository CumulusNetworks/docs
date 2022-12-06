---
title: ACL Commands
author: Cumulus Networks
weight: 110
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> acl \<acl-id\>

Shows information about Access Control Lists (ACLs) on the switch. You use ACLs to match packets and take actions.

### Usage

`nv show interface <interface-id> acl <acl-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Shows information about the ACL applied for inbound traffic. |
| `outbound` | Shows information about the ACL applied for outbound traffic. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 acl
```

## nv show interface \<interface-id\> acl \<acl-id\> inbound

Shows information about the ACL applied for inbound traffic.

### Usage

`nv show interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `control-plane`   | Shows information about the ACL applied to the control plane for inbound traffic. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 acl EXAMPLE1 inbound
```

## nv show interface \<interface-id\> acl \<acl-id\> inbound control-plane

Shows information about the ACL applied for the control plane.

### Usage

`nv show interface <interface-id> acl <acl-id> inbound control-plane [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 acl EXAMPLE1 inbound control-plane
```

## nv show interface \<interface-id\> acl \<acl-id\> outbound

Shows information about the ACL applied for outbound traffic.

### Usage

`nv show interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `control-plane` |  Shows information about the ACL applied to the control plane for outbound traffic. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 acl EXAMPLE1 outbound
```

## nv show interface \<interface-id\> acl \<acl-id\> outbound control-plane

Shows information about the ACL applied to the control plane for outbound traffic.

### Usage

`nv show interface <interface-id> acl <acl-id> outbound control-plane [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 acl EXAMPLE1 outbound control-plane
```

## nv show system acl

### Usage

`nv show system acl [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl

Shows the configured ACL rules on the switch.

### Usage

`nv show acl [options] [<acl-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl
```

## nv show acl \<acl-id\>

Shows the specified ACL rule.

### Usage

`nv show acl <acl-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` |  Shows configuration information about the ACL with the specified rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1
```

## nv show acl \<acl-id\> rule \<rule-id\>

Shows configuration information about the ACL with the specified rule number.

### Usage

`nv show acl <acl-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `match`   | Shows the ACL match criteria.|
| `action`  | Shows the ACL action. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10
```

## nv show acl \<acl-id\> rule \<rule-id\> match

Shows the ACL match criteria for the specified ACL rule.

### Usage

`nv show acl <acl-id> rule <rule-id> match [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ip` |   Shows an IPv4 or IPv6 match. |
| `mac` |  Shows a MAC match. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip

Shows an IPv4 or IPv6 match for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-port`| Shows source port matches. |
| `dest-port`  | Shows destination port matches. |
| `fragment`   | Shows ip fragment packets. |
| `ecn`        | Shows ECN protocol packet matches |
| `tcp`        | Shows TCP protocol packet matches. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip source-port \<ip-port-id\>

Shows source port matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<ip-port-id>` | The IP port number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip source-port ssh
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port \<ip-port-id\>

Shows destination port matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<ip-port-id>` |  The IP port number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip dest-port http
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip fragment

Shows ip fragment packet matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip fragment [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip fragment
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn

Shows ECN matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flags`  |  Shows the ECN protocol flags. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip ecn
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn flags

Shows the ECN protocol flag matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip ecn flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip ecn flags
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp

Shows TCP matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flags`  | Shows TCP protocol flag matches. |
| `mask`   | Shows TCP protocol flag mask matches. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip tcp
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp flags

Shows TCP flag matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip tcp flags
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp mask

Shows TCP protocol flag mask matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp mask [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip tcp mask
```

## nv show acl \<acl-id\> rule \<rule-id\> match mac

Shows MAC address matches for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> match mac [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 match mac
```

## nv show acl \<acl-id\> rule \<rule-id\> action

Shows the action for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> action [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `permit`  | Shows a permit action. |
| `deny`    | Shows a deny action. |
| `log`     | Shows ACL logging. |
| `set`     | Shows a set action. |
| `erspan`  | Shows an ERSPAN session. |
| `police`  | Shows policing of packets and bytes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 action
```

## nv show acl \<acl-id\> rule \<rule-id\> action permit

Shows a permit action for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> action permit [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 action permit
```

## nv show acl \<acl-id\> rule \<rule-id\> action deny

Shows a deny action for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> action deny [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 action deny
```

## nv show acl \<acl-id\> rule \<rule-id\> action log

Shows logs for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> action log [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 action log
```

## nv show acl \<acl-id\> rule \<rule-id\> action set

Shows the set action for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> action set [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 action set
```

## nv show acl \<acl-id\> rule \<rule-id\> action erspan

Shows the ERSPAN session for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> action erspan [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 action erspan
```

## nv show acl \<acl-id\> rule \<rule-id\> action police

Shows policing of matched packets and bytes for the ACL rule specified.

### Usage

`nv show acl <acl-id> rule <rule-id> action police [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show acl EXAMPLE1 rule 10 action police
```
