---
title: DHCP Snooping
author: Cumulus Networks
weight: 154

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop</h>

Shows the DHCP snooping table for IPv4.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop
DHCP Snooping Table 
====================== 
VLAN  Port  IP        MAC                      Lease     State   Bridge 
----  ----  ------    -----------------        -----     -----   ------ 
10    swp3  10.0.0.4  00:02:00:00:00:04        7200      ACK     br_default
      swp6  10.0.0.6  00:02:00:00:00:06        7200      ACK     br_default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop vlan</h>

Shows the IPv4 DHCP snooping trust ports table.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan
DHCP Snooping Vlan Trust Ports Table
=======================================
    Port 
    -----
    bond1

DHCP Snooping Vlan Bind Table
================================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop vlan \<vid\></h>

Shows the IPv4 DHCP snooping trust ports table for a specific VLAN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan 10
DHCP Snooping Vlan Trust Ports Table
=======================================
    Port 
    -----
    bond1

DHCP Snooping Vlan Bind Table
================================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop vlan \<vid\> trust</h>

Shows the trusted ports for a VLAN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan 10 trust
Port 
-----
bond1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop vlan \<vid\> trust \<interface-id\></h>

Shows information in the IPv4 DHCP snooping table for a specific trusted port.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan 10 trust swp6
DHCP Snooping Table 
====================== 
IP    : 20.0.0.1 
Mac   : 00:02:00:00:00:04 
Lease : 7200    
State : ACK  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop vlan \<vid\> bind</h>

Shows IPv4 DHCP bind port information.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan 10 bind
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop vlan \<vid\> bind \<interface-id\></h>

Shows IPv4 DHCP bind information for a specific port.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan 10 bind swp6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop6</h>

Shows the DHCP snooping table for IPv6.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop6 vlan</h>

Shows the IPv6 DHCP snooping table for all VLANs

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop6 vlan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop6 vlan \<vid\></h>

Shows the IPv6 DHCP snooping table for a specific VLAN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop6 vlan 10
DHCP Snooping Vlan Trust Ports Table
=======================================
    Port 
    -----
    bond1

DHCP Snooping Vlan Bind Table
================================
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop6 vlan \<vid\> trust</h>

Shows information in the IPv6 DHCP snooping table for trusted ports.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop6 vlan 10 trust
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop6 vlan \<vid\> trust \<interface-id\></h>

Shows information in the IPv6 DHCP snooping table for a specific trusted port.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop6 vlan 10 trust swp6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop6 vlan \<vid\> bind</h>

Shows IPv6 DHCP bind information.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop6 vlan 10 bind
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> dhcp-snoop6 vlan \<vid\> bind \<interface-id\></h>

Shows IPv6 DHCP bind information for a specific port.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop6 vlan 10 bind swp6
```
