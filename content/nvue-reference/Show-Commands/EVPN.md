---
title: EVPN
author: Cumulus Networks
weight: 170
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show evpn</h>

Shows global EVPN control plane information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info</h>

Shows access VLAN information.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan</h>

Shows all EVPN access VLANs.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan \<vlan-id\></h>

Shows EVPN access VLAN information for the specified VLAN.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan \<vlan-id\> member-interface</h>

Shows EVPN access VLAN member interface information.

### Command Syntax

| Syntax | Description |
| ---------  | -------------- |
| `<vlan-id>` | The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan 10 member-interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad</h>

Shows EVPN duplicate address detection information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn dad
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad duplicate-action</h>

Shows the action to take when there is a duplicate address detected.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn dad duplicate-action
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad duplicate-action freeze</h>

Shows all EVPN duplicate address freeze actions.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn dad duplicate-action freeze
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg</h>

Shows EVPN nexthop groups.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg vtep-ip</h>

Shows EVPN nexthop group information for all VTEPs.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg vtep-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg vtep-ip \<vtep-id\></h>

Shows EVPN nexthop group information for the specified VTEP.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg vtep-ip 10.10.10.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming</h>

Shows EVPM multihoming global configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info</h>

Shows EVPN multihoming BGP information.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi</h>

Shows EVPN multihoming BGP information for all ESIs.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\></h>

Shows EVPN multihoming BGP information for the specified ESI.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> remote-vtep</h>

Shows EVPN multihoming BGP information for the specified ESI for all VTEPs.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> remote-vtep \<ipv4-address-id\></h>

Shows EVPN multihoming BGP information for the specified ESI for a specific VTEP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |
| `<ipv4-address-id>` | The IPv4 address of the VTEP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep 10.10.10.101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> fragments</h>

Shows EVPN multihoming BGP remote VTEP fragment information for a specific ESI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 fragments
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi \<esi-id\> fragments \<fragment-id\></h>

Shows specific EVPN multihoming BGP remote VTEP fragment information for a specific ESI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<esi-id>` | The ESI identifier. |
| `<fragment-id>` | The route-distinguisher. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02 fragments 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming ead-evi-route</h>

Shows EVPN multihoming Ethernet Auto-discovery per EVPN instance route information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming ead-evi-route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming esi</h>

Shows EVPN multihoming Ethernet segment ID information.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi
```

## <h>nv show evpn multihoming esi \<esi-id\></h>

Shows information about the specified EVPN multihoming Ethernet segment ID.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi 03:44:38:39:be:ef:aa:00:00:02
```

## <h>nv show evpn multihoming esi \<esi-id\> remote-vtep</h>

Shows information about the specified EVPN multihoming Ethernet segment ID for remote VTEPs.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming esi \<esi-id\> remote-vtep \<ipv4-address-id\></h>

Shows information about a specific EVPN multihoming Ethernet segment ID for the specified remote VTEP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<esi-id>` | The ESI identifier. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep 10.10.10.101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming segment</h>

Shows EVPN multihoming segment information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming segment
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn route-advertise</h>

Shows EVPN route advertise information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show evpn route-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni</h>

Shows information about the EVPN VNIs on the switch.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\></h>

Shows configuration information about the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> bgp-info</h>

Shows BGP configuration information for the specific VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 bgp-info
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> host</h>

Shows the ARP and ND table for the specific VNI.

### Command Syntax

|  Syntax |  Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 host
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> host \<ip-address-id\></h>

Shows a specific ARP and ND table for the specific VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<ip-address-id>` |  The IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 host 10.0.1.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> mac</h>

Shows the MAC address for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 mac
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> mac \<mac-address-id\></h>

Shows configuration information about a specific VNI MAC address.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<mac-address-id>` | The MAC address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 mac 50:88:b2:3c:08:f9
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming</h>

Shows multihoming Ethernet configuration for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi</h>

Shows BGP information for the multihoming Ethernet segments for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming bgp-info esi
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi \<es-id\></h>

Shows BGP information for a specific multihoming Ethernet segment for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming bgp-info esi 03:44:38:39:be:ef:aa:00:00:02
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi \<esi-id\> remote-vtep</h>

Shows BGP information for a specific multihoming Ethernet segment for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming bgp-info esi \<esi-id\> remote-vtep \<ipv4-address-id\></h>

Shows BGP information for a specific multihoming Ethernet segment for the specified VNI on a specific remote VTEP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |
| `<ipv4-address-id>` | The IPv4 address of the remote VTEP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming esi 03:44:38:39:be:ef:aa:00:00:02 remote-vtep 10.10.10.101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming esi</h>

Shows the EVPN multihoming ESIs for the specified VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming esi
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming esi \<es-id\></h>

Shows information for a specific multihoming Ethernet segment for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<es-id>` | The Ethernet segment ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming esi 03:44:38:39:be:ef:aa:00:00:02
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-advertise</h>

Shows route advertisement information for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-advertise`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target</h>

Shows route target information for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target both</h>

Shows both import and export route target information for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target both`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target both
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target both \<rt-id\></h>

Shows information about both the specified import and export route target for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target both <rt-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target both 65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target export</h>

Shows export route target information for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target export`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target export
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target export \<rt-id\></h>

Shows configuration information about the a specific export route target for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target export <rt-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10  route-target export 65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target import</h>

Shows import route target configuration for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target import`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target import
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target import \<rt-id\></h>

Shows configuration information about a specific import route target for the specified EVPN VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv show evpn evi <vni-id> route-target import <rt-id>`
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` | The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 route-target import 65102:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> evpn</h>

Shows EVPN control plane configuration for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond1 evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> evpn multihoming</h>

Shows the EVPN multihoming interface configuration parameters.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond1 evpn multihoming
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> evpn multihoming segment</h>

Shows EVPN multihoming interface segment configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface bond1 evpn multihoming segment
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn</h>

Shows EVPN control plane configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn bgp-info</h>

Shows layer 3 VNI information from BGP.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn bgp-info 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn nexthop-vtep</h>

Shows the EVPN next hop VTEP for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn nexthop-vtep
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn nexthop-vtep \<nexthop-vtep-id\></h>

Shows information about a specific EVPN next hop VTEP in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<nexthop-vtep-id>` | The IP address of the nexthop VTEP.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn nexthop-vtep 10.10.10.101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn remote-router-mac</h>

Shows the EVPN remote router MAC addresses in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn remote-router-mac
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn remote-router-mac \<mac-address-id\></h>

Shows information about a specific EVPN remote router MAC address in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<mac-address-id>` | The MAC address.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn remote-router-mac 50:88:b2:3c:08:f9
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn vni</h>

Shows all EVPN VNIs in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn vni 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn vni \<vni-id\></h>

Shows EVPN configuration for a specific VNI in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn vni 
```
