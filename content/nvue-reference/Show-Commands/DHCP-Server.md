---
title: DHCP Server
author: Cumulus Networks
weight: 152

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server</h>

Shows IPv4 DHCP server information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server
         Summary           
-------  ------------------
default  interface:    swp1
         pool: 10.1.10.0/24
         static:    server1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\></h>

Shows IPv4 DHCP server configuration information in the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default
          operational   applied     
--------  ------------  ------------
[interface]  swp1          swp1        
[pool]       10.1.10.0/24  10.1.10.0/24
[static]     server1       server1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> domain-name</h>

Shows the DNS attributes provided by the DHCP server in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default domain-name
             domain-name
--------     -----------
mydomain.com

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> domain-name \<domain-name-id\></h>

Shows information about a specific DNS attribute provided by the DHCP server in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<domain-name-id>` | The IPv4 DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default domain-name mydomain.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> domain-name-server</h>

Shows DNS configuration provided by the DHCP server in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default domain-name-server

--------------
192.168.200.53
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> domain-name-server \<server-id\></h>

Shows specific DNS server configuration provided by the DHCP server in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<server-id>` | The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default domain-name-server 192.168.200.53
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> interface</h>

Shows a list of interfaces on which the IPv4 DHCP client attaches.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 interface`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default interface

----
swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> interface \<interface-id\></h>

Shows information about a specific interface on which the IPv4 DHCP client attaches.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 interface <interface-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<interface-id>` | The IPv4 DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool</h>

Shows a list of the IPv4 DHCP pool subnets and the applied configuration.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool
              cumulus-provision-url  default-url  lease-time  ping-check  pool-name  Summary                           
------------  ---------------------  -----------  ----------  ----------  ---------  ----------------------------------
10.1.10.0/24                                      200000                             domain-name:           example.com
                                                                                     domain-name-server: 192.168.200.53
                                                                                     gateway:                 10.1.10.1
                                                                                     range:                 10.1.10.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\></h>

Shows information about a specific IPv4 DHCP pool subnet.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24
                       operational     applied        
---------------------  --------------  ---------------
cumulus-provision-url                                 
default-url                                           
lease-time             200000          200000         
ping-check                             on             
pool-name                              storage-servers
[domain-name]          example.com     example.com    
[domain-name-server]   192.168.200.53  192.168.200.53 
[gateway]              10.1.10.1       10.1.10.1      
[range]                10.1.10.100     10.1.10.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name</h>

Shows the IPv4 DHCP domain names in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name
             domain-name
-----------  -----------
example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\></h>

Shows information about a specific IPv4 DHCP domain name in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name <domain-name-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server</h>

Shows a list of the IPv4 DHCP domain name servers in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name-server`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name-server

--------------
192.168.200.53
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\></h>

Shows information about a specific IPv4 DHCP domain name server in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name-server <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |
| `<server-id>` | The DNS server IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 domain-name-server 192.168.200.53
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> gateway</h>

Shows the IPv4 DHCP gateways in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> gateway`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 gateway
         
---------
10.1.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> gateway \<gateway-id\></h>

Shows information about a specific IPv4 DHCP gateway in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> gateway <gateway-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |
| `<gateway-id>` | The gateway IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 gateway 10.1.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> range</h>

Shows the IPv4 DHCP IP address range assignments.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> range`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 range
             to         
-----------  -----------
10.1.10.100  10.1.10.199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> pool \<pool-id\> range \<range-id\></h>

Shows information about a specific IPv4 DHCP IP address range assignment.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> range <range-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP pool subnet. |
| `<range-id>` | The start of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100
    operational  applied    
--  -----------  -----------
to  10.1.10.199  10.1.10.199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> static</h>

Shows configuration for static hosts served by the DHCP server.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 static`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default static
         cumulus-provision-url  host-id-circuit-id  ip-address  MAC address      
-------  ---------------------  ------------------  ----------  -----------------
server1                                             10.0.0.2    44:38:39:00:01:7e
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> static \<static-id\></h>

Shows configuration for a specific static host served by the DHCP server.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show vrf <vrf-id> dhcp-server-v4 static <static-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<static-id>` | The IDN host name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server default static server1
             operational        applied          
-----------  -----------------  -----------------
ip-address   10.0.0.2           10.0.0.2         
mac-address  44:38:39:00:01:7e  44:38:39:00:01:7e
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6</h>

Shows IPv6 DHCP server information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\></h>

Shows IPv6 DHCP server configuration information in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> domain-name</h>

Shows the DNS attributes provided by the IPv6 DHCP server.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default domain-name
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> domain-name \<domain-name-id\></h>

Shows information about a specific DNS attribute provided by the IPv6 DHCP server.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> domain-name-server</h>

Shows the IPv6 domain name servers.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default domain-name-server
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> domain-name-server \<server-id\></h>

Shows information about a specific IPv6 domain name server.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<server-id>` | The IPv6 address of the DNS server.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default domain-name-server 0:0:0:0:0:ffff:c0a8:c835
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> interface</h>

Shows the interfaces on which the IPv6 DHCP client attaches.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> interface \<interface-id\></h>

Shows information about a specific interface on which the IPv6 DHCP client attaches.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<interface-id>` | The DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool</h>

Shows the configured IPv6 DHCP pool subnets.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\></h>

Shows information about a specific IPv6 DHCP pool subnet.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default storage-servers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name</h>

Shows information about the IPv6 DHCP domain names in the specified pool.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.  |
| `<pool-id>` |   The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default storage-servers domain-name
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name \<domain-name-id\></h>

Shows information about a specific IPv6 DHCP domain name in the specified pool.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` |   The DHCP6 pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default storage-servers domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server</h>

Shows information about the IPv6 DHCP domain name servers in the specified pool.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default storage-servers domain-name-server
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> domain-name-server \<server-id\></h>

Shows information about a specific IPv6 DHCP domain name server in the specified pool.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<server-id>` | The DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default storage-servers domain-name-server 0:0:0:0:0:ffff:c0a8:c835
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> range></h>

Shows the IPv6 DHCP IP address range assignments.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP6 pool subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default storage-servers range
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> pool \<pool-id\> range \<range-id\></h>

Shows information about a specific IPv6 DHCP IP address range assignment.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<pool-id>` | The DHCP6 pool subnet. |
| `<range-id>` | The start of the IPv6 address range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default storage-servers range 0:0:0:0:0:ffff:0a01:0a64
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> static</h>

Shows configuration for static hosts served by the IPv6 DHCP server.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default static
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server6 \<vrf-id\> static \<static-id\></h>

Shows configuration for a specific static host served by the IPv6 DHCP server.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<static-id>` | The IDN hostname. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-server6 default static server1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4</h>

Shows IPv4 DHCP server configuration information in the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show vrf <vrf-id> dhcp-server-v4`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4
               applied     
-------------  ------------
[subnet]       10.1.10.0/24
[static-host]  server1     
[static-host]  server2     
[static-host]  server3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-server \<vrf-id\> interface</h>

Shows a list of interfaces on which the IPv4 DHCP client attaches.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> interface`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 interface
----
swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 interface \<interface-id\></h>

Shows information about a specific interface on which the IPv4 DHCP client attaches.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> interface <interface-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<interface-id>` | The IPv4 DHCP client interface. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet</h>

Shows a list of the IPv4 DHCP pool subnets and the applied configuration.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 subnet
              cumulus-provision-url  default-url  lease-time  ping-check  pool-name  Summary                           
------------  ---------------------  -----------  ----------  ----------  ---------  ----------------------------------
10.1.10.0/24                                      200000                             domain-name:           example.com
                                                                                     domain-name-server: 192.168.200.53
                                                                                     gateway:                 10.1.10.1
                                                                                     range:                 10.1.10.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\></h>

Shows information about a specific IPv4 DHCP pool subnet.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 subnet 10.1.10.0/24
                       operational     applied        
---------------------  --------------  ---------------
cumulus-provision-url                                 
default-url                                           
lease-time             200000          200000         
ping-check                             on             
pool-name                              storage-servers
[domain-name]          example.com     example.com    
[domain-name-server]   192.168.200.53  192.168.200.53 
[gateway]              10.1.10.1       10.1.10.1      
[range]                10.1.10.100     10.1.10.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-4 subnet \<subnet-id\> domain-name</h>

Shows the IPv4 DHCP domain names in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 subnet 10.1.10.0/24 domain-name
             domain-name
-----------  -----------
example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> domain-name \<domain-name-id\></h>

Shows information about a specific IPv4 DHCP domain name in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |
| `<domain-name-id>` | The DHCP domain name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show dhcp-server-v4 vrf default subnet 10.1.10.0/24 domain-name example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> domain-name-server</h>

Shows a list of the IPv4 DHCP domain name servers in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server`.

{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-4 subnet 10.1.10.0/24 domain-name-server
--------------
192.168.200.53
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show dhcp-server-v4 vrf \<vrf-id\> subnet \<subnet-id\> domain-name-server \<server-id\></h>

Shows information about a specific IPv4 DHCP domain name server in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |
| `<server-id>` | The DNS server IP address.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-4 subnet 10.1.10.0/24 domain-name-server 192.168.200.53
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> gateway</h>

Shows the IPv4 DHCP gateways in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id> gateway`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-4 subnet 10.1.10.0/24 gateway
---------
10.1.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> gateway \<gateway-id\></h>

Shows information about a specific IPv4 DHCP gateway in the specified pool.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |
| `<gateway-id>` | The gateway IP address. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-4 subnet 10.1.10.0/24 gateway 10.1.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> range</h>

Shows the IPv4 DHCP IP address range assignments.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id> range`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 subnet 10.1.10.0/24 range
             to         
-----------  -----------
10.1.10.100  10.1.10.199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 subnet \<subnet-id\> range \<range-id\></h>

Shows information about a specific IPv4 DHCP IP address range assignment.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<subnet-id>` | The DHCP pool subnet. |
| `<range-id>` | The start of the IP address range. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 subnet 10.1.10.0/24 range 10.1.10.100
    operational  applied    
--  -----------  -----------
to  10.1.10.199  10.1.10.199
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 static</h>

Shows configuration for static hosts served by the DHCP server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> static`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 static
         cumulus-provision-url  host-id-circuit-id  ip-address  MAC address      
-------  ---------------------  ------------------  ----------  -----------------
server1                                             10.0.0.2    44:38:39:00:01:7e
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> dhcp-server-v4 static \<static-id\></h>

Shows configuration for a specific static host served by the DHCP server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dhcp-server <vrf-id> static <static-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<static-id>` | The IDN host name.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default dhcp-server-v4 static server1
             operational        applied          
-----------  -----------------  -----------------
ip-address   10.0.0.2           10.0.0.2         
mac-address  44:38:39:00:01:7e  44:38:39:00:01:7e
```
