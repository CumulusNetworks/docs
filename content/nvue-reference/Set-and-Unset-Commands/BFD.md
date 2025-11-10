---
title: BFD
author: Cumulus Networks
weight: 517

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf bfd profile \<profile-name\></h>

Configures the BFD profile to use for an OSPF interface.

When you enable BFD on an OSPF interface, a neighbor registers with BFD when two-way adjacency starts and de-registers when adjacency goes down. The BFD configuration is per interface and any IPv4 neighbors discovered on that interface inherit the configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set interface swp1 router ospf bfd profile BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim bfd profile \<profile-name\></h>

Configures the BFD profile to use for a PIM interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set interface swp1 router pim bfd profile BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd state</h>

Enables and disables BFD globally on the switch.

BFD provides low overhead and rapid detection of failures in the paths between two network devices. It provides a unified mechanism for link detection over all media and protocol layers. Use BFD to detect failures for IPv4 and IPv6 single or multihop paths between any two network devices, including unidirectional path failure detection.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd profile \<profile-name\></h>

Configures the BFD profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd profile BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd profile \<profile-name\> detect-multiplier</h>

Configures the detection time multiplier to determine packet loss. The detection timeout is calculated based on multiplying the detection multiplier with the greater value between the local switch’s receive interval and the peer’s transmit interval. The default value is 3.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd profile BFD1 detect-multiplier 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd profile \<profile-name\> min-rx-interval</h>

Configures the minimum interval between the received BFD control packets. You can set a value between 10 and 4294967 milliseconds. The default value is 300.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd profile BFD1 min-rx-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd profile \<profile-name\> min-tx-interval</h>

Configures the minimum interval for transmitting BFD control packets. You can set a value between 10 and 4294967 milliseconds. The default value is 300.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd profile BFD1 min-tx-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd profile \<profile-name\> shutdown</h>

Configures the BFD shutdown, which enables or disables the peer. When the peer is disabled, the switch sends an administrative down message to the remote peer. The default value is disabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd profile BFD1 shutdown enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd profile \<profile-name\> passive-mode</h>

Configures passive mode, which marks the session as passive. A passive session does not attempt to start the connection and waits for control packets from the peer before it begins replying. Passive mode is useful when you have a router that acts as the central node of a star network and you want to avoid sending BFD control packets you don’t need to. You can set passive mode to `enabled` or `disabled`. The default is `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd profile BFD1 passive-mode enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bfd profile \<profile-name\> minimum-ttl</h>

Configures the minimum expected TTL for an incoming BFD control packet (for multi hop sessions only). This feature tightens the packet validation requirements to avoid receiving BFD control packets from other sessions. You can set a value between 1 and 254. The default value is 254 (only expect one hop between this system and the peer).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `\<profile-name\>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set router bfd profile BFD1 minimum-ttl 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd profile \<profile-name\></h>

Configures BFD for a peer group using the specified BFD profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>` |  The peer group name. |
| `<profile-name>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group fabric bfd profile BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd profile \<profile-name\></h>

Configures BFD for a neighbor using the specified BFD profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<neighbor-id>` |  The VRF name. |
| `<profile-name>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 bfd profile BFD1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<ipv4-prefix\> distance \<integer\> via \<ipv4\> bfd profile \<profile-name\></h>

Associates static routes with BFD to monitor static route reachability. Depending on status of the BFD session, the switch either adds or removes static routes from the Routing Information Base (RIB).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<ipv4-prefix>` |  The IPv4 prefix. |
| `<integer>` |  The IPv4 prefix. |
| `<ipv4>` |  The IPv4 prefix. |
| `<profile-name>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd profile BFD2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<ipv4-prefix\> distance \<integer\> via \<ipv4\> bfd multi-hop</h>

Configures BFD for multihop next-hop tracking through static routes. You can specify `enabled` or `disabled`. BFD operates in single hop mode by default.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<ipv4-prefix>` |  The IPv4 prefix. |
| `<integer>` |  The IPv4 prefix. |
| `<ipv4>` |  The IPv4 prefix. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd multi-hop enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<ipv4-prefix\> distance \<integer\> via \<ipv4\> bfd source</h>

Configures the BFD source for static routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<ipv4-prefix>` |  The IPv4 prefix. |
| `<integer>` |  The IPv4 prefix. |
| `<ipv4>` |  The IPv4 prefix. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd source 10.10.10.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<ipv4-prefix\> via \<ipv4\> bfd profile \<profile-name\></h>

Associates static routes with BFD to monitor static route reachability. Depending on status of the BFD session, the switch either adds or removes static routes from the Routing Information Base (RIB).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<ipv4-prefix>` |  The IPv4 prefix. |
| `<ipv4>` |  The IPv4 prefix. |
| `<profile-name>` |  The profile name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 bfd profile BFD1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<ipv4-prefix\> via \<ipv4\> bfd multi-hop</h>

Configures BFD for multihop next-hop tracking through static routes. You can specify `enabled` or `disabled`. BFD operates in single hop mode by default.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<ipv4-prefix>` |  The IPv4 prefix. |
| `<ipv4>` |  The IPv4 prefix. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 bfd multi-hop enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<ipv4-prefix\> via \<ipv4\> bfd source</h>

Configures the BFD source for static routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<ipv4-prefix>` |  The IPv4 prefix. |
| `<ipv4>` |  The IPv4 prefix. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd source 10.10.10.3
```
