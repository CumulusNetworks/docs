---
title: EVPN Commands
author: Cumulus Networks
weight: 150
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> evpn

EVPN control plane config and info for VRF

### Usage

`nv show interface <interface-id> evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|  `multihoming`    | Multihoming interface configuration parameters|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> evpn multihoming

Multihoming interface configuration parameters

### Usage

`nv show interface <interface-id> evpn multihoming [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `segment`   |  Multihoming interface segment|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> evpn multihoming segment

Multihoming interface segment

### Usage

`nv show interface <interface-id> evpn multihoming segment [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> evpn

EVPN control plane config and info for VRF

### Usage

`nv show vrf <vrf-id> evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `vni`|  L3 VNI |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> evpn vni \<vni-id\>

 VNI

### Usage

`nv show vrf <vrf-id> evpn vni <vni-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<vni-id>` |  VxLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn

Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Usage

`nv show evpn [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-advertise`  | Route advertising |
| `dad`              | Advertise |
| `evi`              | EVI |
| `multihoming`      | Multihoming global configuration parameters |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn route-advertise

### Usage

`nv show evpn route-advertise [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad

Duplicate address detection

### Usage

`nv show evpn dad [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `duplicate-action`  | Action to take when a MAC is flagged as a possible duplicate. If 'warning-only', generates a log message. If 'freeze', further move events for the MAC will not be acted upon. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad duplicate-action

Handling of BUM traffic

### Usage

`nv show evpn dad duplicate-action [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `freeze`  |  Further move events for the MAC will not be acted upon. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn dad duplicate-action freeze

Advertise

### Usage

`nv show evpn dad duplicate-action freeze [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi

EVIs

### Usage

`nv show evpn evi [options] [<evi-id> ...]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\>

Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Usage

`nv show evpn evi <evi-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-advertise` | Route advertise |
| `route-target`    | Route targets |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-advertise

Route advertise

### Usage

`nv show evpn evi <evi-id> route-advertise [options]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target

EVPN control plane config and info for VRF

### Usage

`nv show evpn evi <evi-id> route-target [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| `<evi-id>`    |  VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `export` |  Route targets to export |
| `import` |  Route targets to import |
| `both`   |  Route targets to import and export |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target export

Set of route target identifiers

### Usage

`nv show evpn evi <evi-id> route-target export [options] [<rt-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target export \<rt-id\>

A route target identifier

### Usage

`nv show evpn evi <evi-id> route-target export <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target import

Set of route target identifiers

### Usage

`nv show evpn evi <evi-id> route-target import [options] [<rt-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target import \<rt-id\>

A route target identifier

### Usage

`nv show evpn evi <evi-id> route-target import <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target both

Set of route target identifiers

### Usage

`nv show evpn evi <evi-id> route-target both [options] [<rt-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |   VRF |
| `<rt-id>` |    Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn evi \<evi-id\> route-target both \<rt-id\>

A route target identifier

### Usage

`nv show evpn evi <evi-id> route-target both <rt-id> [options]`

### Identifiers

|  Identifier |  Description   |
| --------- | -------------- |
| `<evi-id>` |  VRF |
| `<rt-id>` |Route target ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming

Multihoming global configuration parameters

### Usage

`nv show evpn multihoming [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ead-evi-route`  | Ethernet Auto-discovery per EVPN instance routes |
| `segment`        | Multihoming interface segment |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming ead-evi-route

### Usage

`nv show evpn multihoming ead-evi-route [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show evpn multihoming segment

Multihoming interface segment

### Usage

`nv show evpn multihoming segment [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
