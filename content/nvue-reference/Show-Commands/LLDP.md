---
title: LLDP
author: Cumulus Networks
weight: 200

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> lldp</h>

Shows <span style="background-color:#F5F5DC">[LLDP](## "Link Layer Discovery Protocol")</span> statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 lldp
                    operational  applied  pending
-------------------  -----------  -------  -------
dcbx-ets-config-tlv  off                          
dcbx-ets-recomm-tlv  off                          
dcbx-pfc-tlv         off                          
[neighbor]           server01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> lldp neighbor</h>

Shows information about all the LLDP neighbors for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp51 lldp neighbor
Neighbor  Remote IP     Model  SW Version  Remote Port
--------  ------------  -----  ----------  -----------
spine01   10.10.10.101                     swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> lldp neighbor \<neighbor-id\></h>

Shows statistics for a specific LLDP neighbor for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp51 lldp neighbor spine01
                           operational                                                    applied  pending
-------------------------  ------------------------------------------------------------…  -------  -------
age                        323055                                                                         
bridge                                                                                                    
  [vlan]                                                                                                  
chassis                                                                                                   
  chassis-id               44:38:39:22:01:82                                                              
  management-address-ipv4  10.10.10.101                                                                   
  management-address-ipv6  fe80::4638:39ff:fe22:182                                                       
  system-description       Cumulus Linux version 5.5.0 running on QEMU Standard PC                        
                           (i440FX + PIIX, 1996)                                                          
  system-name              spine01                                                                        
lldp-med                                                                                                  
  device-type              Network Connectivity Device                                                    
port                                                                                                      
  description              swp1                                                                           
  name                     swp1                                                                           
  ttl                      120                                                                            
  type                     ifname                                                                         
  pmd-autoneg                                                                                             
    [advertised]                                                                                          
    mau-oper-type          1000BaseTFD - Four-pair Category 5 UTP, full duplex mode
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge</h>

Shows bridge information for the specified LLDP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp51 lldp neighbor spine01 bridge
       operational  applied  pending
------  -----------  -------  -------
[vlan]
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge vlan</h>

Shows the VLANs for the specified LLDP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 lldp neighbor leaf02 bridge vlan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge vlan \<vid\></h>

Shows information about a specific VLAN for the specified LLDP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name.|
| `<neighbor-id>` |  The LLDP neighbor name. |
| `<vid>` | The VLAN name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 lldp neighbor leaf02 bridge vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service lldp</h>

Shows global LLDP configuration, such as the LLDP mode, and LLDP timers and if 802.1 TLV transmission is on or off. By default, 802.1 TLV transmission is off and the switch sends all LLDP frames without 802.1 TLVs.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service lldp
                        operational  applied  pending
----------------------  -----------  -------  -------
dot1-tlv                off          off      off    
lldp-med-inventory-tlv  off          off      off    
mode                    default      default  default
tx-hold-multiplier      4            4        4      
tx-interval             30           30       30
```
