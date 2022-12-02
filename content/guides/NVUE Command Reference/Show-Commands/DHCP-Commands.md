---
title: DHCP Commands
author: Cumulus Networks
weight: 130
product: Cumulus Linux
type: nojsscroll
---
## nv show service dhcp-relay

DHCP-relays

### Usage

`nv show service dhcp-relay [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\>

DHCP relay

### Usage

`nv show service dhcp-relay <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server`                | DHCP servers |
| `interface`             | Set of interfaces on which to handle DHCP relay traffic |
| `giaddress-interface`   | Configures DHCP relay giaddress on the interfaes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\> server \<server-id\>

A DHCP server

### Usage

`nv show service dhcp-relay <vrf-id> server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>`   | DHCP server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\> interface \<interface-id\>

### Usage

`nv show service dhcp-relay <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` |  DHCP relay interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay \<vrf-id\> giaddress-interface \<interface-id\>

### Usage

`nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>`  | DHCP relay giaddress interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6

### Usage

`nv show service dhcp-relay6 [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\>

### Usage

`nv show service dhcp-relay6 <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`  | DHCP relay interfaces |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\> interface

DHCP relay interfaces

### Usage

`nv show service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `upstream`   | Configures DHCP relay on the interfaes. |
| `downstream` | Configures DHCP relay on the interfaes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\>

An interface on which DPCH relay is configured.

### Usage

`nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` |  DHCP relay interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\>

An interface on which DPCH relay is configured.

### Usage

`nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` |  DHCP relay interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```




## nv show service dhcp-server

DHCP-servers

### Usage

`nv show service dhcp-server [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\>

Dynamic Host Configuration Protocol Server

### Usage

`nv show service dhcp-server <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`             | Assign DHCP options to clients directly attached to these interfaes. |
| `pool`                  | DHCP Pools |
| `domain-name`           | DHCP domain names |
| `domain-name-server`    | DHCP domain name servers |
| `static`                | DHCP clients with fixed IP address assignments |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> interface \<interface-id\>

An interface on which DPCH clients are attached.

### Usage

`nv show service dhcp-server <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>`  | DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\>

DHCP Pool

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP pool subnet. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `domain-name-server`    | DHCP domain name servers |
| `domain-name`           | DHCP domain names |
| `gateway`               | DHCP gateway |
| `range`                 | IP Address range assignments |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<pool-id>` |  DHCP pool subnet. |
| `<server-id>` | DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` | DHCP pool subnet. |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\>

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]`



  A remote DNS server

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` | DHCP pool subnet. |
| `<gateway-id>` |  Gateway |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\>

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options]`



  DHCP Pool range

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` | DHCP pool subnet. |
| `<range-id>` |   DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server <vrf-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server <vrf-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |  DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server \<vrf-id\> static \<static-id\>

static entry

### Usage

`nv show service dhcp-server <vrf-id> static <static-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-id>` | static mapping name|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6

DHCP-servers6

### Usage

`nv show service dhcp-server6 [options] [<vrf-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\>

Dynamic Host Configuration Protocol IPv6 Server

### Usage

`nv show service dhcp-server6 <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`             | Assign DHCP options to clients directly attached to these interfaes.|
| `pool`                  | DHCP IP Pools |
| `domain-name`           | DHCP domain names |
| `domain-name-server`    | DHCP domain name servers |
| `static`                | DHCP clients with fixed IP address assignments |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> interface \<interface-id\>

### Usage

`nv show service dhcp-server6 <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<interface-id>` | DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\>

DHCP Pool

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |   DHCP6 pool subnet. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  domain-name-server    DHCP domain name servers

  domain-name           DHCP domain names

  range                 IP Address range assignments

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP6 pool subnet. |
| `<server-id>` |   DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP6 pool subnet. |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\>

DHCP Pool range

### Usage

`nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<pool-id>` |  DHCP6 pool subnet. |
| `<range-id>` |  DHCP client interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\>

TBD

### Usage

`nv show service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<domain-name-id>` | DHCP domain name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> domain-name-server \<server-id\>

A remote DNS server

### Usage

`nv show service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |  DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service dhcp-server6 \<vrf-id\> static \<static-id\>

static entry

### Usage

`nv show service dhcp-server6 <vrf-id> static <static-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-id>` |  static mapping name|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
