---
title: DHCP Commands
author: Cumulus Networks
weight: 140
product: Cumulus Linux
type: nojsscroll
---
## nv show service dhcp-relay

Shows the IPv4 DHCP relay configuration on the switch.

### Usage

`nv show service dhcp-relay [options] [<vrf-id> ...]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay
```

## nv show service dhcp-relay \<vrf-id\>

Shows the IPv4 DHCP relay configuration in the specified VRF.

### Usage

`nv show service dhcp-relay <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server`                | Shows the specified DHCP server configuration.|
| `interface`             | Shows DHCP relay configuration information for the interface that handles DHCP relay traffic. |
| `giaddress-interface`   | Shows DHCP relay giaddress configuration information. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay default
```

## nv show service dhcp-relay \<vrf-id\> server \<server-id\>

Shows configuration for the specified IPv4 DHCP server participating in DHCP relay.

### Usage

`nv show service dhcp-relay <vrf-id> server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<server-id>`   | The DHCP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay default server 172.16.1.102
```

## nv show service dhcp-relay \<vrf-id\> interface \<interface-id\>

Shows IPv4 DHCP relay configuration information for the interface that handles DHCP relay traffic.

### Usage

`nv show service dhcp-relay <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` |  The DHCP relay interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay default interface swp1
```

## nv show service dhcp-relay \<vrf-id\> giaddress-interface \<interface-id\>

Shows the IPv4 DHCP relay gateway IP address (giaddress) interface configuration.

### Usage

`nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>`  | The DHCP relay giaddress interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay default giaddress-interface lo
```

## nv show service dhcp-relay6

Shows IPv6 DHVP relay configuration information on the switch.

### Usage

`nv show service dhcp-relay6 [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay6
```

## nv show service dhcp-relay6 \<vrf-id\>

Shows IPv6 DHVP relay configuration information in the specified VRF on the switch.

### Usage

`nv show service dhcp-relay6 <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`  | Shows the IPv6 DHCP relay interfaces. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay6 default
```

## nv show service dhcp-relay6 \<vrf-id\> interface

Shows the IPv6 DHCP relay interface configuration in the specified VRF.

### Usage

`nv show service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `upstream`   | Shows the upstream IPv6 DHCP relay interface configuration. |
| `downstream` | Shows the downstream IPv6 DHCP relay interface configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay6 default interface swp1
```

## nv show service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\>

Shows the upstream IPv6 DHCP relay interface configuration.

### Usage

`nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` | The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay6 default interface upstream swp51
```

## nv show service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\>

AShows the downstream IPv6 DHCP relay interface configuration.

### Usage

`nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` |  The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-relay6 default interface downstream swp1
```

## nv show service dhcp-server

Shows IPv4 DHCP server information.

### Usage

`nv show service dhcp-server [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server
```

## nv show service dhcp-server \<vrf-id\>

Shows IPv4 DHCP server configuration information in the specified VRF.

### Usage

`nv show service dhcp-server <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `interface`             | Shows the interfaces on which IPv4 DPCH clients are attached.|
| `pool`                  | Shows the IPv4 DHCP Pools. |
| `domain-name`           | Shows the IPv4 DHCP domain names. |
| `domain-name-server`    | Shows the IPv4 DHCP domain name servers. |
| `static`                | Shows the IPv4 DHCP clients with fixed IP address assignments. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default
```

## nv show service dhcp-server \<vrf-id\> interface \<interface-id\>

Shows information about the interface on which IPv4 DHCP client is attached.

### Usage

`nv show service dhcp-server <vrf-id> interface <interface-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<interface-id>`  | The IPv4 DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default interface swp1
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\>

Shows information about the IPv4 DHCP pool subnet.

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `domain-name-server`    | Shows information about the IPv4 DHCP domain name server in the pool |
| `domain-name`           | Shows information about the the IPv4 DHCP domain name in the pool. |
| `gateway`               | Shows information about the IPv4 DHCP gateway. |
| `range`                 | Shows the IPv4 DHCP IP address range assignments. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

Shows information about the IPv4 DHCP domain name server in the pool.

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<server-id>` | The DNS server IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name-server 192.168.200.53
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

Shows information about the the IPv4 DHCP domain name in the pool.

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name example.com
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\>

Shows information about the IPv4 DHCP gateway.

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<gateway-id>` |  The gateway IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 gateway 10.1.10.1
```

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\>

Shows the IPv4 DHCP IP address range assignments.

### Usage

`nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The start of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100
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
cumulus@leaf04:mgmt:~$ nv show service dhcp-server default domain-name
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
