---
title: ND Commands
author: Cumulus Networks
weight: 175
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ip neighbor-discovery

Neighbor discovery configuration for an interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\>

A recursive DNS server

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ipv6-address-id>`  |   IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\>

A IPv6 prefix

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ipv6-address-id>`  |   IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\>

A DNS search list

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-name-id>`   |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890).|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor-discovery router-advertisement

Router advertisement configuration for an interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor-discovery home-agent

Indicates to neighbors that this router acts as a Home Agent and includes a Home Agent Option. Not defined by default

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
