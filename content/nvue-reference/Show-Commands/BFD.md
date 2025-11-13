---
title: BFD
author: Cumulus Networks
weight: 127

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router ospf bfd </h>

Shows the BFD configuration profile associated with the OSPF interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface swp1 router ospf bfd
         operational  applied
-------  -----------  -------
profile               BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pim bfd </h>

Shows the BFD configuration profile associated with the PIM interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The PIM interface. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 router pim bfd
         operational  applied
-------  -----------  -------
profile               BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router bfd profile \<profile-name\></h>

Shows BFD configuration profile details.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show router bfd profile BFD1
                   applied 
-----------------  -------- 
detect-multiplier  10 
min-rx-interval    100 
min-tx-interval    100 
shutdown           enabled 
passive-mode       enabled 
minimum-ttl        1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bfd peers</h>

Shows BFD peer information for the VRF.

You can use the following command options:
- `--view brief` shows summarized information.
- `--view standard` shows detailed information
- `--view counters` shows counters, such as the control packet input and output, the echo packet input and output, and if the session is up or down.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router bfd peers --view brief
MHop - Multihop, Local - Local, Peer - Peer, Interface - Interface, State - 
State, Passive - Passive Mode, Time - Up/Down Time, Type - Config Type 
LocalId     MHop   Local       Peer        Interface  State  Passive  Time        Type 
----------  -----  ----------  ----------  ---------  -----  -------  ----------  ------- 
20162981    True   6.0.0.24    6.0.0.26               up     False    1:00:08:20  dynamic 
1002134429  True   6000::24    6000::26               up     False    1:00:08:20  dynamic 
1987835266  False  fe80::a288  fe80::9e05  p0_if.100  up     False    1:00:08:20  dynamic 
2124581159  False  fe80::a288  fe80::9e05  p0_if.101  up     False    1:00:08:20  dynamic 
2323511220  True   6000::24    6000::23               up     False    1:00:08:20  dynamic 
4089962224  True   6.0.0.24    6.0.0.23               up     False    0:19:07:20  dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bfd peers \<local-id\></h>

Shows BFD peer information for the specified vrf and session.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |
| `<local-ID>` | The session ID (integer). |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router bfd peers 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd</h>

Shows the BFD configuration profile associated with a BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>` | The neighbor ID. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 bfd
         operational  applied
-------  -----------  -------
profile               BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group\> bfd</h>

Shows the BFD configuration profile associated with a BGP peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group underlay bfd
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router static \<ipv4-address\> via \<ipv4-address\> bfd</h>

Shows the BFD configuration profile associated static routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | ------------- |
| `<vrf-id>` | The VRF ID. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router static 10.10.10.101/32 via 10.0.1.0 bfd
         operational  applied
-------  -----------  -------
profile               BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router static \<ipv4-address\> distance \<integer\> via <ipv4-address\> bfd</h>

Shows the BFD configuration profile associated with static routes for the specified number of next hops.

### Command Syntax

| Syntax |  Description   |
| ---------  | ------------- |
| `<vrf-id>` | The VRF ID. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd
         operational  applied
-------  -----------  -------
profile               BFD1
```
