---
title: EVPN Commands
author: Cumulus Networks
weight: 150
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> evpn

EVPN control plane config and info for VRF

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> evpn multihoming

Multihoming interface configuration parameters

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> evpn multihoming segment

Multihoming interface segment

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> evpn

EVPN control plane config and info for VRF

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> evpn vni \<vni-id\>

 VNI

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<vni-id>` |  VxLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn

Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn route-advertise

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn dad

Duplicate address detection

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn dad duplicate-action

Handling of BUM traffic

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn dad duplicate-action freeze

Advertise

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi

EVIs

### Command Syntax

| Syntax |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\>

Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Command Syntax

| Syntax |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-advertise

Route advertise

### Command Syntax

| Syntax |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-target

EVPN control plane config and info for VRF

### Command Syntax

| Syntax |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-target export

Set of route target identifiers

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-target export \<rt-id\>

A route target identifier

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-target import

Set of route target identifiers

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-target import \<rt-id\>

A route target identifier

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-target both

Set of route target identifiers

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn evi \<evi-id\> route-target both \<rt-id\>

A route target identifier

### Command Syntax

|  Syntax |  Description   |
| --------- | -------------- |
| `<evi-id>` |  VRF |
| `<rt-id>` |Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn multihoming

Multihoming global configuration parameters

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn multihoming ead-evi-route

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show evpn multihoming segment

Multihoming interface segment

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
