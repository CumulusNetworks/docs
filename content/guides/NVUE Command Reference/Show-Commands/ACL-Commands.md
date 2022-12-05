---
title: ACL Commands
author: Cumulus Networks
weight: 110
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> acl \<acl-id\>

An ACL is used for matching packets and take actions

### Usage

`nv show interface <interface-id> acl <acl-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` |     ACL ID|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | ACL applied for inbound direction |
| `outbound` | ACL applied for outbound direction |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> inbound

inbound direction

### Usage

`nv show interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `control-plane`   | ACL applied for control plane |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> inbound control-plane

State details

### Usage

`nv show interface <interface-id> acl <acl-id> inbound control-plane [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> outbound

State details

### Usage

`nv show interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `control-plane` | |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> acl \<acl-id\> outbound control-plane

State details

### Usage

`nv show interface <interface-id> acl <acl-id> outbound control-plane [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<acl-id>` | ACL ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
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

ACL rules

### Usage

`nv show acl [options] [<acl-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <acl-id> |  ACL ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\>

An ACL is used for matching packets and take actions

### Usage

`nv show acl <acl-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>`  |  ACL ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rule` |  acl rule |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\>

ACL Matching criteria and action rule

### Usage

`nv show acl <acl-id> rule <rule-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `match`   | ACL match criteria |
| `action`  | ACL action |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match

An ACL match

### Usage

`nv show acl <acl-id> rule <rule-id> match [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ip` |   IPv4 and IPv6 match |
| `mac` |  MAC match |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip

An ACL IPv4/IPv6 match

### Usage

`nv show acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-port`| source port |
| `dest-port`  | destination port |
| `fragment`   | Fragment packets |
| `ecn`        | ECN protocol packet match |
| `tcp`        | TCP protocol packet match |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip source-port \<ip-port-id\>

### Usage

`nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |
| `<ip-port-id>` |  IP port ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port \<ip-port-id\>

L4 port

### Usage

`nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |
| `<ip-port-id>` | IP port ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip fragment

State details

### Usage

`nv show acl <acl-id> rule <rule-id> match ip fragment [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn

ECN

### Usage

`nv show acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flags`  |  ECN protocol flags |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn flags

ECN flags

### Usage

`nv show acl <acl-id> rule <rule-id> match ip ecn flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp

L4 port

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flags`  | TCP protocol flags |
| `mask`   | TCP protocol flag mask |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp flags

TCP flags

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp flags [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp mask

TCP flags

### Usage

`nv show acl <acl-id> rule <rule-id> match ip tcp mask [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> match mac

An ACL MAC match

### Usage

`nv show acl <acl-id> rule <rule-id> match mac [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action

ACL rule action

### Usage

`nv show acl <acl-id> rule <rule-id> action [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `permit`  | Permit action |
| `deny`    | Deny action |
| `log`     | Provides ACL logging facility |
| `set`     | Modify the packet with appropriate values |
| `erspan`  | ERSPAN session |
| `police`  | policing of packets/bytes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action permit

Permit packets

### Usage

`nv show acl <acl-id> rule <rule-id> action permit [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action deny

deny packets

### Usage

`nv show acl <acl-id> rule <rule-id> action deny [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action log

log packets

### Usage

`nv show acl <acl-id> rule <rule-id> action log [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action set

Set action for packets

### Usage

`nv show acl <acl-id> rule <rule-id> action set [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action erspan

ERSPAN session

### Usage

`nv show acl <acl-id> rule <rule-id> action erspan [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>` | ACL ID |
| `<rule-id>`  |   ACL rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show acl \<acl-id\> rule \<rule-id\> action police

Policing of matched packets/bytes

### Usage

`nv show acl <acl-id> rule <rule-id> action police [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<acl-id>`  |  ACL ID |
  
  <rule-id>             ACL rule number

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
