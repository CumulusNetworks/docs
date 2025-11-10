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

## <h>nv set interface \<interface-id\> ipv4 dhcp-client set-hostname</h>

Enables and disables the DHCPv4 client to update system hostname from the DHCP server. You can specify `enabled` or `disabled`. The default value is `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set interface swp5 ipv4 dhcp-client set-hostname enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv6 dhcp-client set-hostname</h>

Enables and disables the DHCPv6 client to update system hostname from the DHCP server. You can specify `enabled` or `disabled`. The default value is `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set interface swp5 ipv6 dhcp-client set-hostname enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> domain-name \<domain-name-id\></h>

Configures the Dynamic Host Configuration Protocol Server (DHCP server) domain name.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 domain-name`.
{{%/notice%}}

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

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 domain-name-server`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 interface <interface-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> provision-url`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> provision-url`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name-server <domain-name-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> gateway <gateway-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> lease-time`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> ping-check`.
{{%/notice%}}

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

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> pool-name \<pool-id\></h>

Configures the pool name.

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

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

## <h>nv set service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-start\> to \<range-end\></h>

Configures the end of the IP address range you want to use in this DHCP server pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> range <range-start> to <range-end>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP pool subnet. |
| `<range-start>` |  The start of the IP address range. |
| `<range-end>` |  The end of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100 to 10.1.10.199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server \<vrf-id\> static \<static-id\></h>

Configures a static IP address for a resource, such as a server or printer.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 static-host <static-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 static-host <static-id> provision-url`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 static-host <static-id> agent-remoteid-circuitid`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 static-host <static-id> ifname <interface-name>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 static-host <static-id> ip-address <ip-address>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v4 static-host <static-id> mac-address <mac-address>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6`.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\></h>

Configures the DHCP domain name for IPv6.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 domain-name <domain-name-id>`.
{{%/notice%}}

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

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 domain-name-server <domain-name-server-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 interface <interface-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id>`.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> cumulus-provision-url \<url\></h>

Configures a specific URL for the provisioning script.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> provision-url`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> default-url <url>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> domain-name <domain-name-id>`.
{{%/notice%}}

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

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<domain-name-id>`|  The zname. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name example.com domain-name myidn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\></h>

Configures the remote DHCP domain name server you want to use in this pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> domain-name-server <domain-name-server-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> lease-time`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> ping-check`.
{{%/notice%}}

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

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

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

## <h>nv set service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-start\> to \<range-end\></h>

Configures the end of the DHCP pool range for IPv6.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> range <range-start> to <range-end>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<pool-id>` |  The DHCP6 pool subnet.|
| `<range-start>` | The start of the DHCP pool range. |
| `<range-end>` | The end of the DHCP pool range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 range 2002:a01:a64:: to 2002:a01:ac7::
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-server6 \<vrf-id\> static \<static-id\></h>

Configures a static DHCP6 server for a resource, such as a server or printer.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 static-host <static-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 static-host <static-id> provision-url`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 static-host <static-id> ifname <interface-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 static-host <static-id> ip-address <ip-address-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set vrf <vrf-id> dhcp-server-v6 static-host <static-id> mac-address <mac-address-id>`.
{{%/notice%}}

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 interface \<interface-id\></h>

Configures the DHCP client interface.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> interface <interface-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\></h>

Configures a DHCP pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> domain-name \<domain-name-id\></h>

Configures the DHCP domain name you want to use in this pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> domain-name-server \<domain-name-server-id\></h>

Configures the DHCP domain name server you want to use in this pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP pool subnet. |
| `<domain-name-server-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 domain-name-server 10.0.0.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> gateway \<gateway-id\></h>

Configures the DHCP gateway you want to use in this pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP pool subnet. |
| `<gateway-id>` | The DHCP gateway. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 gateway 10.1.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> lease-time</h>

Configures the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000. The default setting is 600.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id> lease-time`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 lease-time 200000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> ping-check</h>

Configures the DHCP server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id> ping-check`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 ping-check enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> range \<range-id\></h>

Configures the start of the IP address range you want to use in this DHCP server pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The start of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 range 10.1.10.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> range \<range-id\> to \<ipv4\></h>

Configures the end of the IP address range you want to use in this DHCP server pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to <ipv4>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP pool subnet. |
| `<range-id>` |  The end of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 subnet 10.1.10.0/24 range 10.1.10.100 to 10.1.10.199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 static-host \<static-id\></h>

Configures a static IP address for a resource, such as a server or printer.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> static <static-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource to which you want to assign a static IP address. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 static-host server1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 static-host \<static-id\> provision-url \<value\></h>

Configures a URL for a provisioning script.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url <value>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 static-host server1 provision-url http://192.0.2.1/myscript.sh
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 static-host \<static-id\> agent-remoteid-circuitid \<value\></h>

Configures the host identifier for the agent circuit ID.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> static <static-id> host-id-circuit-id <value>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<value>` |  The host identifier for the agent circuit ID. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 static-host server1 agent-remoteid-circuitid 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 static-host \<static-id\> ifname \<interface-name\></h>

Configures the interface name for the DHCP static assignment (IPv4 only) to use instead of the MAC address.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> static <static-id> ifname <interface-name>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<interface-name>` |  The interface name (such as swp1). |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 static-host server1 ifname swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 static-host \<static-id\> ip-address \<ipv4\></h>

Configures the static IP address for the resource.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> static <static-id> ip-address <ipv4>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 static-host server1 ip-address 10.0.0.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v4 static-host \<static-id\> mac-address \<mac-address\></h>

Configures the MAC address of the resource to which you want to assign a static IP address.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server <vrf-id> static <static-id> mac-address <mac-address>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<static-id>` | The name of the resource. |
| `<mac-address>` | The MAC address. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v4 static-host server1 mac-address 44:38:39:00:01:7e
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6</h>

Configures the Dynamic Host Configuration Protocol Server (DHCP server) for IPv6.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id>`.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 domain-name \<domain-name-id\></h>

Configures the DHCP domain name for IPv6.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<domain-name-id>`|  The DHCP6 domain name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 domain-name-server \<server-id\></h>

Configures the remote DNS server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> domain-name-server <domain-name-server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The DNS server. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 domain-name-server 2001:db8::
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 interface \<interface-id\></h>

Configures the DHCP client interface for IPv6.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> interface <interface-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 subnet \<subnet-id\> provision-url \<url\></h>

Configures a specific URL for the provisioning script.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url <url>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<subnet-id>` |  The DHCP6 pool subnet.|
| `<url>` |  The providioning script URL.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 subnet 2001:db8::1/128 provision-url https://www.nvidia.com/provision
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 subnet \<subnet-id\> default-url \<url\></h>

Configures the default URL for the IPv6 pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url <url>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<subnet-id>` |  The DHCP6 pool subnet.|
| `<url>` |  The default URL.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 subnet 2001:db8::1/128 default-url https://www.nvidia.com/
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 subnet \<subnet-id\> domain-name \<domain-name-id\></h>

Configures the DHCP domain name you want to use in this pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` | The DHCP6 pool subnet. |
| `<domain-name-id>`|  The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 subnet 2001:db8::1/128 domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 subnet \<subnet-id\> domain-name-server \<server-id\></h>

Configures the remote DHCP domain name server you want to use in this pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <domain-name-server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` | The DHCP6 pool subnet. |
| `<server-id>`  | The DNS server IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 subnet 2001:db8::1/128 domain-name-server 2001:4860:4860::8888
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 subnet \<subnet-id\> lease-time</h>

Configures the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<subnet-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 subnet 2001:db8::1/128 lease-time 200000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 subnet \<subnet-id\> ping-check</h>

Configures the DHCP6 server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> pool <pool-id> ping-check`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<subnet-id>` |  The DHCP6 pool subnet.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 subnet 2001:db8::1/128 ping-check enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 subnet \<subnet-id\> range \<range-start\> to \<range-end\></h>

Configures the end of the DHCP pool range for IPv6.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-start> to <range-end>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<subnet-id>` |  The DHCP6 pool subnet.|
| `<range-start>` | The start of the DHCP pool range. |
| `<range-end>` | The end of the DHCP pool range. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 subnet 2001:db8::1/128 range 2002:a01:a64:: to 2002:a01:ac7::
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 static-host \<static-id\></h>

Configures a static DHCP6 server for a resource, such as a server or printer.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> static <static-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 static-host server1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 static-host \<static-id\> provision-url \<value\></h>

Configures a URL for a provisioning script.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 static-host server1 provision-url https://www.nvidia.com/provision
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 static-host \<static-id\> ifname \<interface-id\></h>

Configures the interface for the static DHCP6 server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> static <static-id> ifname <interface-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<interface-id>` |  The interface ID. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 static-host server1 ifname swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 static-host \<static-id\> ip-address \<ip-address-id\></h>

Configures the IPv6 address for the static DHCP6 server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> static <static-id> ip-address <ip-address-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<ip-address-id>` |  The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 static-host server1 ip-address 2001:db8::
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> dhcp-server-v6 static-host \<static-id\> mac-address \<mac-address\></h>

Configures the MAC (hardware) address for the static DHCP6 server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dhcp-server6 <vrf-id> static <static-id> mac-address <mac-address-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-id>` |  The name of the resource. |
| `<mac-address>` |  The MAC address. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default dhcp-server-v6 static-host server1 mac-address 44:38:39:00:01:7e
```
