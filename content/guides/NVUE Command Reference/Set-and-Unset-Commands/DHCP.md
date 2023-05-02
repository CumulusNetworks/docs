---
title: DHCP
author: Cumulus Networks
weight: 540
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set service dhcp-relay \<vrf-id\>

Configures DHCP relays for IPv4 and IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set service dhcp-relay \<vrf-id\> gateway-interface \<interface-id\>

Configures the gateway IPv4 address on an interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id>`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` | The gateway interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default gateway-interface lo
```

- - -

## nv set service dhcp-relay \<vrf-id\> giaddress-interface \<interface-id\> address

Configures the IPv4 address on the gateway interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` | The gateway IP address. |
| `<ipv4-address>` | The IPv4 address on the gateway interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default giaddress-interface address lo 10.10.10.1
```

- - -

## nv set service dhcp-relay \<vrf-id\> interface \<interface-id\>

Configures the interfaces on which to configure DHCP relay.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` |  The interface on which to configure DHCP relay. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default interface swp51
```

- - -

## nv set service dhcp-relay \<vrf-id\> server \<server-id\>

Configures the DHCP server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The IPv4 address of the DHCP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default server 172.16.1.102
```

- - -

## nv set service dhcp-relay \<vrf-id\> source-ip

Configures the source IP address to use on the relayed packet.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay default source-ip giaddress
```

- - -

## nv set service dhcp-relay6 \<vrf-id\>

Configures DHCP relay for IPv6 on a specific VRF.

- - -

## nv set service dhcp-relay6 \<vrf-id\> interface

Configures the DHCP relay IPv6 interfaces.

- - -

## nv set service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\>

Configures the DHCP relay downstream interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay6 default interface downstream swp1
```

- - -

## nv set service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\> link-address \<ipv6\>

Configures the IPv6 address on DHCP relay downstream interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, the command is `nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address <ipv6>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay downstream interface. |
|`<ipv6>` |  The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay6 default interface downstream swp1 address 2001:db8::1
```

- - -

## nv set service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\>

Configures the upstream interface for DHCP relay for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay upstream interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

## Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay6 default interface upstream swp51
```

- - -

## nv set service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\> server-address \<ipv6\>

Configures the IPv6 address on the DHCP relay upstream interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, the command is `nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address <ipv6>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay interface. |
|`<ipv6>` |  The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-relay6 default interface upstream swp51 server-address 2001:db8:0002::0a00:0002
```

- - -

## nv set service dhcp-server

Configures the Dynamic Host Configuration Protocol Server (DHCP server) for IPv4.

- - -

## nv set service dhcp-server \<vrf-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<domain-name-id>` |  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default domain-name example.com
```

- - -

## nv set service dhcp-server \<vrf-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\>

Configures the Internationalized Domain Name (IDN) you want to use in this pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<domain-name-id>` |  The DHCP domain name. |
| `<idn-hostname>` |  The IDN. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default domain-name example.com domain-name myIDN
```

- - -

## nv set service dhcp-server \<vrf-id\> domain-name-server \<server-id\>

Confgures a remote DNS server to use globally.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default domain-name-server 192.168.200.53.
```

- - -

## nv set service dhcp-server \<vrf-id\> interface \<interface-id\>

Configures the DHCP client interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default interface swp1
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\>

Configures a DHCP pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> cumulus-provision-url \<value\>

Configures a specific URL for the provisioning script.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 cumulus-provision-url https://www.nvidia.com/provision
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> default-url \<value\>

Confifgures the default URL for the DHCP server pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 default-url https://www.nvidia.com/
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name you want to use in this pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name example.com
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

Configures the remote DHCP domain name server you want to use in this pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP pool subnet. |
| `<server-id>` |  The remote DHCP domain name server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name-server 192.168.200.53 
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\>

Configures the DHCP gateway you want to use in this pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<gateway-id>` | The DHCP gateway. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 gateway 10.1.10.1
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> lease-time

Configures the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000. The default setting is 600.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 lease-time 200000
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> ping-check

Configures the DHCP server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 ping-check on
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> pool-name \<value\>

Configures the pool name.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<value>` |  The DHCP pool name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 pool-name storage-servers
```

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\>

Configures the start of the IP address range you want to use in this DHCP server pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The start of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\> to \<ipv4\>

Configures the end of the IP address range you want to use in this DHCP server pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The end of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100 to 10.1.10.199
```

- - -

## nv set service dhcp-server \<vrf-id\> static \<static-id\>

Configures a static IP address for a resource, such as a server or printer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource to which you want to assign a static IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1
```

- - -

## nv set service dhcp-server \<vrf-id\> static \<static-id\> cumulus-provision-url \<value\>

Configures a URL for a provisioning script.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1 cumulus-provision-url http://192.0.2.1/myscript.sh
```

- - -

## nv set service dhcp-server \<vrf-id\> static \<static-id\> host-id-circuit-id \<value\>

Configures the host identifier for the agent circuit ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<value>` |  The host identifier for the agent circuit ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1 host-id-circuit-id 1
```

- - -

## nv set service dhcp-server \<vrf-id\> static \<static-id\> ip-address \<ipv4\>

Configures the static IP address for the resource.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1 ip-address 10.0.0.2
```

- - -

## nv set service dhcp-server \<vrf-id\> static \<static-id\> mac-address \<mac-address\>

Configures the MAC address of the resource to which you want to assign a static IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource. |
| `<mac-address>` | The MAC address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server default static server1 mac-address 44:38:39:00:01:7e
```

- - -

## nv set service dhcp-server6

Configures the Dynamic Host Configuration Protocol Server (DHCP server) for IPv6.

- - -

## nv set service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<domain-name-id>`|  The DHCP6 domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default domain-name example.com
```

- - -

## nv set service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\>

Configures the Internationalized Domain Name (IDN) of the IPv6 DHCP server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<domain-name-id>`|  The DHCP domain name. |
| `<idn-hostname>`|  The IDN. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default domain-name example.com domain-name 
```

- - -

## nv set service dhcp-server6 \<vrf-id\> domain-name-server \<server-id\>

Configures the remote DNS server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default domain-name-server 2001:db8::1/128
```

- - -

## nv set service dhcp-server6 \<vrf-id\> interface \<interface-id\>

Configures the DHCP client interface for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default interface swp1
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\>

Configures DHCP IP pools for IPv6.

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> cumulus-provision-url \<url\>

Configures a specific URL for the provisioning script.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|
| `<url>` |  The providioning script URL.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 cumulus-provision-url https://www.nvidia.com/provision
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> default-url \<url\>

Confifgures the default URL for the IPv6 pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|
| `<url>` |  The default URL.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 default-url https://www.nvidia.com/
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\>

Configures the DHCP domain name you want to use in this pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<domain-name-id>`|  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name example.com
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\>

Configures the Internationalized Domain Name (IDN) you want to use in this pool for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<domain-name-id>`|  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name example.com domain-name myidn
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\>

Configures the remote DHCP domain name server you want to use in this pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<server-id>`  | The DNS server IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name-server 2001:4860:4860::8888
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> lease-time

Configures the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 lease-time 200000
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> ping-check

Configures the DHCP6 server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 ping-check on
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> pool-name \<value\>

Configures the DHCP pool name for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|
| `<pool-name>` |  The DHCP6 pool name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 pool-name storage-servers
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\>

Configures the start of the DHCP pool range for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<range-id>`|  The start of the DHCP pool range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 range 2002:a01:a64::
```

- - -

## nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\> to \<ipv6\>

Configures the end of the DHCP pool range for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|
| `<range-id>` | The end of the DHCP pool range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 range 2002:a01:a64:: to 2002:a01:ac7::
```

- - -

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\>

Configures a static DHCP6 server for a resource, such as a server or printer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\> cumulus-provision-url \<value\>

Configures a URL for a provisioning script.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default static server1 cumulus-provision-url https://www.nvidia.com/provision
```

- - -

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\> ip-address \<ipv6\>

Configures the IPv6 address for the static DHCP6 server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<ip-address>` |  The IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default static server1 ip-address 2001:db8::1/128
```

- - -

## nv set service dhcp-server6 \<vrf-id\> static \<static-id\> mac-address \<mac-address\>

Configures the MAC (hardware) address for the static DHCP6 server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<mac-address>` |  The MAC address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dhcp-server6 default static server1 mac-address 44:38:39:00:01:7e
```

- - -
