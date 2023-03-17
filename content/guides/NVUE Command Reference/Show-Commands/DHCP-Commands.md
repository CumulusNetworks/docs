---
title: DHCP Commands
author: Cumulus Networks
weight: 150
product: Cumulus Linux
type: nojsscroll
---
## nv show service dhcp-relay

Shows the IPv4 DHCP relay configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay
```

- - -

## nv show service dhcp-relay \<vrf-id\>

Shows the IPv4 DHCP relay configuration in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay default
```

- - -

- - -

## nv show service dhcp-relay \<vrf-id\> giaddress-interface \<interface-id\>

Shows the IPv4 DHCP relay gateway IP address (giaddress) interface configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>`  | The DHCP relay giaddress interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay default giaddress-interface lo
```

## nv show service dhcp-relay \<vrf-id\> interface \<interface-id\>

Shows IPv4 DHCP relay configuration information for the interface that handles DHCP relay traffic.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` |  The DHCP relay interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay default interface swp1
```

- - -

## nv show service dhcp-relay \<vrf-id\> server \<server-id\>

Shows configuration for the specified IPv4 DHCP server participating in DHCP relay.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<server-id>`   | The DHCP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay default server 172.16.1.102
```

- - -

## nv show service dhcp-relay6

Shows IPv6 DHVP relay configuration information on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay6
```

- - -

## nv show service dhcp-relay6 \<vrf-id\>

Shows IPv6 DHVP relay configuration information in the specified VRF on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay6 default
```

- - -

## nv show service dhcp-relay6 \<vrf-id\> interface

Shows the IPv6 DHCP relay interface configuration in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay6 default interface swp1
```

- - -

## nv show service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\>

Shows the downstream IPv6 DHCP relay interface configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` |  The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay6 default interface downstream swp1
```

- - -

## nv show service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\>

Shows the upstream IPv6 DHCP relay interface configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` | The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-relay6 default interface upstream swp51
```

- - -

## nv show service dhcp-server

Shows IPv4 DHCP server information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server
```

- - -

## nv show service dhcp-server \<vrf-id\>

Shows IPv4 DHCP server configuration information in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default
```

- - -

## nv show service dhcp-server \<vrf-id\> domain-name

Shows the DNS attributes provided by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default domain-name
```

- - -

## nv show service dhcp-server \<vrf-id\> domain-name \<domain-name-id\>

Shows information about a specific DNS attribute provided by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<domain-name-id>` | The IPv4 DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default domain-name my-domain
```

- - -

## nv show service dhcp-server \<vrf-id\> domain-name-server

Shows DNS configuration provided by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default domain-name-server
```

- - -

## nv show service dhcp-server \<vrf-id\> domain-name-server \<server-id\>

Shows specific DNS server configuration provided by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<server-id>` |  The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default domain-name-server 192.168.200.53
```

- - -

## nv show service dhcp-server \<vrf-id\> interface

Shows a list of interfaces on which IPv4 DHCP client is attached.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default interface
```
- - -

## nv show service dhcp-server \<vrf-id\> interface \<interface-id\>

Shows information about a specific interface on which IPv4 DHCP client is attached.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<interface-id>`  | The IPv4 DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default interface swp1
```

- - -

## nv show service dhcp-server \<vrf-id\> pool

Shows a list of the IPv4 DHCP pool subnets and the applied configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\>

Shows information about a specific IPv4 DHCP pool subnet.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name

Shows the IPv4 DHCP domain names in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

Shows information about the IPv4 DHCP domain name in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name example.com
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server

Shows a list of the IPv4 DHCP domain name servers in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name-server
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

Shows information about the IPv4 DHCP domain name server in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<server-id>` | The DNS server IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name-server 192.168.200.53
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> gateway

Shows the IPv4 DHCP gateways in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 gateway
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\>

Shows information about a specific IPv4 DHCP gateway.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<gateway-id>` |  The gateway IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 gateway 10.1.10.1
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> range

Shows the IPv4 DHCP IP address range assignments.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 range
```

- - -

## nv show service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\>

Shows information about a specific IPv4 DHCP IP address range assignment.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The start of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100
```

- - -

## nv show service dhcp-server \<vrf-id\> static

Shows configuration for static hosts served by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default static
```

- - -

## nv show service dhcp-server \<vrf-id\> static \<static-id\>

Shows configuration for a specific static host served by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<static-id>` | The IDN host name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server default static server1
```

- - -

## nv show service dhcp-server6

Shows IPv6 DHCP server information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6
```

- - -

## nv show service dhcp-server6 \<vrf-id\>

Shows IPv6 DHCP server configuration information in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default
```

- - -

## nv show service dhcp-server6 \<vrf-id\> domain-name

Shows the DNS attributes provided by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default domain-name
```

- - -

## nv show service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\>

Shows information about a specific DNS attribute provided by the DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default domain-name example.com
```

- - -

## nv show service dhcp-server6 \<vrf-id\> domain-name-server

Shows the IPv6 domain name servers.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default domain-name-server
```

- - -

## nv show service dhcp-server6 \<vrf-id\> domain-name-server \<server-id\>

Shows information about a specific IPv6 domain name server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<server-id>` |  The IPv6 address of the DNS server.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default domain-name-server 0:0:0:0:0:ffff:c0a8:c835
```

- - -

## nv show service dhcp-server6 \<vrf-id\> interface

Shows the interfaces on which IPv6 DHCP client is attached.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default interface
```

- - -

## nv show service dhcp-server6 \<vrf-id\> interface \<interface-id\>

Shows information about a specific interface on which IPv6 DHCP client is attached.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default interface swp1
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool

Shows the configured IPv6 DHCP pool subnets.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\>

Shows information about a specific IPv6 DHCP pool subnet.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default storage-servers
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name

Shows information about the IPv6 DHCP domain names in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default storage-servers domain-name
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

Shows information about a specific IPv6 DHCP domain name in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default storage-servers domain-name example.com
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server

Shows information about the IPv6 DHCP domain name servers in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default storage-servers domain-name-server
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

Shows information about a specific IPv6 DHCP domain name server in the pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |
| `<server-id>` |  The DNS server.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default storage-servers domain-name-server 0:0:0:0:0:ffff:c0a8:c835
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> range>

Shows the IPv6 DHCP IP address range assignments.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default storage-servers range
```

- - -

## nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\>

Shows information about a specific IPv6 DHCP IP address range assignment.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |
| `<range-id>` |  The start of the IPv6 address range.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default storage-servers range 0:0:0:0:0:ffff:0a01:0a64
```

- - -

## nv show service dhcp-server6 \<vrf-id\> static

Shows configuration for static hosts served by the IPv6 DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default static
```

## nv show service dhcp-server6 \<vrf-id\> static \<static-id\>

Shows configuration for a specific static host served by the IPv6 DHCP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name. | 
| `<static-id>` | The IDN host name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server6 default static server1
```

- - -
