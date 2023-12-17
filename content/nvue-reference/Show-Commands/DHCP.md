---
title: DHCP
author: Cumulus Networks
weight: 150

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay</h>

Shows the IPv4 DHCP relay configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay
           source-ip  Summary
---------  ---------  -----------------------
+ default  auto       gateway-interface: lo
  default             interface:        swp51
  default             interface:        swp52
  default             interface:        vlan10
  default             server:    172.16.1.102
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\></h>

Shows the IPv4 DHCP relay configuration in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default
                     operational    applied      
-------------------  -------------  -------------
source-ip            auto           auto         
[gateway-interface]  swp2           swp2         
[interface]          peerlink.4094  peerlink.4094
[interface]          swp51          swp51        
[interface]          swp52          swp52        
[interface]          vlan10         vlan10       
[server]             172.16.1.102   172.16.1.102
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\> agent

Shows DHCP Agent Information Option 82 configuration settings.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default agent
                    applied          
------------------  -----------------
[remote-id]         44:38:39:BE:EF:AA
use-pif-circuit-id                   
  enable            on               
enable              on  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\> agent remote-id

Shows the remote IDs configured for DHCP Agent Information Option 82.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default agent remote-id
                    applied          
------------------  -----------------
[remote-id]         44:38:39:BE:EF:AA
use-pif-circuit-id                   
  enable            on               
enable              on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\> agent remote-id \<remote-id\>

Shows information about the specified remote ID configured for DHCP Agent Information Option 82.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<remote-id>` |  The remote name.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default agent remote-id 44:38:39:BE:EF:AA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\> agent use-pif-circuit-id

Shows if circuit ID is enabled for DHCP Agent Information Option 82.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default agent use-pif-circuit-id
        applied
------  -------
enable  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\> gateway-interface \<interface-id\></h>

Shows the IPv4 DHCP relay gateway IP address interface configuration.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>`  | The DHCP relay gateway address interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default gateway-interface swp2
         operational  applied 
-------  -----------  --------
address  10.0.0.4     10.0.0.4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\> interface \<interface-id\></h>

Shows IPv4 DHCP relay configuration information for the interface that handles DHCP relay traffic.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` |  The DHCP relay interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay \<vrf-id\> server \<server-id\></h>

Shows configuration information for the specified IPv4 DHCP server participating in DHCP relay.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<server-id>`   | The DHCP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay default server 172.16.1.102
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay6</h>

Shows IPv6 DHVP relay configuration information on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay6
         Summary                            
-------  -----------------------------------
default  interface.downstream: peerlink.4094
         interface.downstream:        vlan10
         interface.upstream:           swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay6 \<vrf-id\></h>

Shows IPv6 DHVP relay configuration information in the specified VRF on the switch.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay6 default
                operational    applied      
--------------  -------------  -------------
interface                                   
  [downstream]  peerlink.4094  peerlink.4094
  [downstream]  vlan10         vlan10       
  [upstream]    swp51          swp51        
  [upstream]    swp52          swp52 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay6 \<vrf-id\> interface</h>

Shows the IPv6 DHCP relay interface configuration in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay6 default interface
              operational    applied      
------------  -------------  -------------
[downstream]  peerlink.4094  peerlink.4094
[downstream]  vlan10         vlan10       
[upstream]    swp51          swp51        
[upstream]    swp52          swp52
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\></h>

Shows the downstream IPv6 DHCP relay interface configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` |  The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay6 default interface downstream vlan10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\></h>

Shows the upstream IPv6 DHCP relay interface configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<interface-id>` | The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dhcp-relay6 default interface upstream swp51
                operational      applied        
--------------  ---------------  ---------------
server-address  2001:db8:100::2  2001:db8:100::2
```

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

Shows a list of interfaces on which the IPv4 DHCP client is attached.

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

Shows information about a specific interface on which the IPv4 DHCP client is attached.

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

Shows the interfaces on which the IPv6 DHCP client is attached.

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

Shows information about a specific interface on which the IPv6 DHCP client is attached.

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
