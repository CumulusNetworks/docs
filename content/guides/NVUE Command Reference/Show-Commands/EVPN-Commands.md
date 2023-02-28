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

Shows information about the VNIs on the switch.

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

Shows information about the specified VNI.

### Command Syntax

 Syntax |  Description   |
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

 Syntax |  Description   |
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

 Syntax |  Description   |
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

Shows information for the specified export route target for the specified EVPN VNI.

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

Shows import route target information for the specified EVPN VNI.

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

Shows information about the specified import route target for the specified EVPN VNI.

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
