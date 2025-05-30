---
title: DHCP Server
author: Cumulus Networks
weight: 542

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> domain-name \<domain-name-id\></h>

Configures the Dynamic Host Configuration Protocol Server (DHCP server) domain name.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<domain-name-id>` |  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server default domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\></h>

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
cumulus@switch:~$ nv set service dhcp-server default domain-name example.com domain-name myIDN
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> domain-name-server \<server-id\></h>

Configures a remote DNS server to use globally.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server default domain-name-server 192.168.200.53
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> interface \<interface-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server default interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\></h>

Configures a DHCP pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> cumulus-provision-url \<value\></h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 cumulus-provision-url https://www.nvidia.com/provision
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> default-url \<value\></h>

Configures the default URL for the DHCP server pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 default-url https://www.nvidia.com/
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name-server 192.168.200.53 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 gateway 10.1.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> lease-time</h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 lease-time 200000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> ping-check</h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 ping-check on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> pool-name \<value\></h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 pool-name storage-servers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\></h>

Configures the start of the IP address range you want to use in this DHCP server pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The start of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\> to \<ipv4\></h>

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
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100 to 10.1.10.199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server default static server1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\> cumulus-provision-url \<value\></h>

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
cumulus@switch:~$ nv set service dhcp-server default static server1 cumulus-provision-url http://192.0.2.1/myscript.sh
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\> host-id-circuit-id \<value\></h>

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
cumulus@switch:~$ nv set service dhcp-server default static server1 host-id-circuit-id 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\> ifname \<interface-name\></h>

Configures the interface name for the DHCP static assignment (IPv4 only) to use instead of the MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<interface-name>` |  The interface name (such as swp1). |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server default static server1 ifname swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\> ip-address \<ipv4\></h>

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
cumulus@switch:~$ nv set service dhcp-server default static server1 ip-address 10.0.0.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\> mac-address \<mac-address\></h>

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
cumulus@switch:~$ nv set service dhcp-server default static server1 mac-address 44:38:39:00:01:7e
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6</h>

Configures the Dynamic Host Configuration Protocol Server (DHCP server) for IPv6.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default domain-name example.com domain-name 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> domain-name-server \<server-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default domain-name-server 2001:db8::
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> interface \<interface-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\></h>

Configures DHCP IP pools for IPv6.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> cumulus-provision-url \<url\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 cumulus-provision-url https://www.nvidia.com/provision
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> default-url \<url\></h>

Configures the default URL for the IPv6 pool.

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 default-url https://www.nvidia.com/
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\> domain-name \<idn-hostname\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name example.com domain-name myidn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name-server 2001:4860:4860::8888
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> lease-time</h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 lease-time 200000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> ping-check</h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 ping-check on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> pool-name \<value\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 pool-name storage-servers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\> to \<ipv6\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 range 2002:a01:a64:: to 2002:a01:ac7::
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> static \<static-id\></h>

Configures a static DHCP6 server for a resource, such as a server or printer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> static \<static-id\> cumulus-provision-url \<value\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default static server1 cumulus-provision-url https://www.nvidia.com/provision
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\> ifname \<interface-id\></h>

Configures the interface for the static DHCP6 server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<interface-id>` |  The interface ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server6 default static server1 ifname swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> static \<static-id\> ip-address \<ip-address-id\></h>

Configures the IPv6 address for the static DHCP6 server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<ip-address-id>` |  The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server6 default static server1 ip-address 2001:db8::
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> static \<static-id\> mac-address \<mac-address\></h>

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
cumulus@switch:~$ nv set service dhcp-server6 default static server1 mac-address 44:38:39:00:01:7e
```
