---
title: EVPN Commands
author: Cumulus Networks
weight: 150
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> evpn

Shows EVPN control plane configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface bond1 evpn
```

- - -

## nv show interface \<interface-id\> evpn multihoming

Shows the EVPN multihoming interface configuration parameters.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface bond1 evpn multihoming
```

- - -

## nv show interface \<interface-id\> evpn multihoming segment

Shows EVPN multihoming interface segment configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface bond1 evpn multihoming segment
```

- - -

## nv show vrf \<vrf-id\> evpn

Shows EVPN control plane configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn
```

- - -

## nv show vrf \<vrf-id\> evpn vni

Shows all EVPN VNIs in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn vni 
```

- - -

## nv show vrf \<vrf-id\> evpn vni \<vni-id\>

Shows EVPN configuration for a specific VNI in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn vni 
```

- - -

## nv show vrf \<vrf-id\> evpn bgp-info

Shows layer 3 VNI information from BGP.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn bgp-info 
```

- - -

## nv show vrf \<vrf-id\> evpn remote-router-mac

Shows the EVPN remote router MAC addresses in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn remote-router-mac
```

- - -

## nv show vrf \<vrf-id\> evpn remote-router-mac \<mac-address-id\>

Shows information about a specific EVPN remote router MAC address in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<mac-address-id>` |  The MAC address.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn remote-router-mac 50:88:b2:3c:08:f9
```

- - -

## nv show vrf \<vrf-id\> evpn nexthop-vtep

Shows the EVPN next hop VTEP for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn nexthop-vtep
```

- - -

## nv show vrf \<vrf-id\> evpn nexthop-vtep \<nexthop-vtep-id\>

Shows information about a specific EVPN next hop VTEP for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<nexthop-vtep-id>` |  The IP address of the nexthop VTEP.|

### Version History

Introduced in Cumulus Linux 5.?.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn nexthop-vtep 10.10.10.101
```

- - -

## nv show evpn

Shows global EVPN control plane information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn
```

- - -

## nv show evpn route-advertise

Shows EVPN route advertise information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn route-advertise
```

- - -

## nv show evpn dad

Shows EVPN duplicate address detection information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn dad
```

- - -

## nv show evpn dad duplicate-action

Shows the action to take when there is a duplicate address detected.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn dad duplicate-action
```

- - -

## nv show evpn dad duplicate-action freeze

Shows all EVPN duplicate address freeze actions.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn dad duplicate-action freeze
```

- - -

## nv show evpn vni

Shows information about the EVPN VNIs on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| Syntax |  Description   |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni
```

- - -

## nv show evpn vni \<vni-id\>

Shows configuration information about the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| Syntax |  Description   |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10
```

- - -

## nv show evpn vni \<vni-id\> route-advertise

Shows route advertisement information for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| Syntax |  Description   |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 route-advertise
```

- - -

## nv show evpn vni \<vni-id\> route-target

Shows route target information for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| Syntax |  Description   |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 route-target
```

- - -

## nv show evpn vni \<vni-id\> route-target export

Shows export route target information for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 route-target export
```

- - -

## nv show evpn vni \<vni-id\> route-target export \<rt-id\>

Shows configuration information about the a specific export route target for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10  route-target export 65101:10
```

- - -

## nv show evpn vni \<vni-id\> route-target import

Shows import route target configuration for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 route-target import
```

- - -

## nv show evpn vni \<vni-id\> route-target import \<rt-id\>

Shows configuration information about a specific import route target for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 route-target import 65102:10
```

- - -

## nv show evpn vni \<vni-id\> route-target both

Shows both import and export route target information for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 route-target both
```

- - -

## nv show evpn vni \<vni-id\> route-target both \<rt-id\>

Shows information about both the specified import and export route target for the specified EVPN VNI.

### Command Syntax

|  Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<rt-id>` | The route target ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 route-target both 65101:10
```

- - -

## nv show evpn vni \<vni-id\> mac

Shows the MAC address for the specified EVPN VNI.

### Command Syntax

|  Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 mac
```

- - -

## nv show evpn vni \<vni-id\> mac \<mac-address-id\>

Shows configuration information about a specific VNI MAC address.

### Command Syntax

|  Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<mac-address-id>` |  The MAC address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 mac 50:88:b2:3c:08:f9
```

- - -

## nv show evpn vni \<vni-id\> host

Shows the ARP and ND table for the specific VNI.

### Command Syntax

|  Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 host
```

- - -

## nv show evpn vni \<vni-id\> host \<ip-address-id\>

Shows a specific ARP and ND table for the specific VNI.

### Command Syntax

|  Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |
| `<ip-address-id>` |  The IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 host 10.0.1.2
```

- - -

## nv show evpn vni \<vni-id\> bgp-info

Shows BGP configuration information for the specific VNI.

### Command Syntax

|  Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 bgp-info
```

- - -

## nv show evpn multihoming

Shows EVPM multihoming global configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn multihoming
```

- - -

## nv show evpn multihoming ead-evi-route

Shows EVPN multihoming Ethernet Auto-discovery per EVPN instance route information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn multihoming ead-evi-route
```

- - -

## nv show evpn multihoming segment

Shows EVPN multihoming segment information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn multihoming segment
```
