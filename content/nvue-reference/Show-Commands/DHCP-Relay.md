---
title: DHCP Relay
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

## <h>nv show service dhcp-relay \<vrf-id\> agent remote-id \<remote-id\></h>

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

Shows if circuit ID is ON for DHCP Agent Information Option 82.

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
