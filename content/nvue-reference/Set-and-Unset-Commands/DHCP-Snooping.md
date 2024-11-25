---
title: DHCP Snooping
author: Cumulus Networks
weight: 544

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> dhcp-snoop vlan \<vid\></h>

Enables DHCP snooping for IPv4 on a VLAN under a bridge.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default dhcp-snoop vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> dhcp-snoop vlan \<vid\> trust \<interface-id\></h>

Configures a trusted interface for IPv4. Cumulus Linux allows DHCP offers from only trusted interfaces to prevent malicious DHCP servers from assigning IPv4 addresses inside the network. The interface must be a member of the bridge you specify.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |
| `<interface-id>` | The trusted interface ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default dhcp-snoop vlan 10 trust swp3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> dhcp-snoop6 vlan \<vid\></h>

Enables DHCP snooping for IPv6 on a VLAN under a bridge.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default dhcp-snoop6 vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> dhcp-snoop6 vlan \<vid\> trust \<interface-id\></h>

Configures a trusted interface for IPv6. Cumulus Linux allows DHCP offers from only trusted interfaces to prevent malicious DHCP servers from assigning IPv6 addresses inside the network. The interface must be a member of the bridge you specify.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<domain-id>` | The bridge name. |
| `<vlan-id>` | The VLAN name. |
| `<interface-id>` | The trusted interface ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default dhcp-snoop6 vlan 10 trust swp3
```
