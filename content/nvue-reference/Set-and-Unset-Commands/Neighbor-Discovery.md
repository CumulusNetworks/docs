---
title: Neighbor Discovery
author: Cumulus Networks
weight: 610

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> ip neighbor-discovery</h>

Configures <span style="background-color:#F5F5DC">[ND](## "Neighbor Discovery")</span> for an interface. ND allows different devices on the same link to advertise their existence to their neighbors and to learn about the existence of their neighbors. ND is the IPv6 equivalent of IPv4 ARP for layer 2 address resolution.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\></h>

Configures the DNS search lists (DNSSL).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<domain-name-id>` |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890). |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\> lifetime</h>

Configures the maximum amount of time you want to use the domain suffix for domain name resolution. You can set a value between 0 and 4294967295 seconds or use the keyword `infinte` to set the time to never expire. If you set the value to 0, the host does not use the DNSSL.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<domain-name-id>` |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890). |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com lifetime infinite
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery enable</h>

Turns ND on or off. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery enable off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery home-agent</h>

Configures the switch to be a Home Agent.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery home-agent enable</h>

Turns the Home Agent on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery home-agent enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery home-agent lifetime</h>

Configures the maximum amount of time you want the router to act as a Home Agent. You can set a value between 0 and 65520 seconds. If you set the value to 0, the router is not a Home Agent. The default setting is 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery home-agent lifetime 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery home-agent preference</h>

Configures the Home Agent router preference used to order the addresses returned in the Home Agent address discovery reply. You can set a value between 0 and 65535. 0 is the lowest preference. The default setting is 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery home-agent preference 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery mtu</h>

Configures the MTU for ND messages on an interface. You can set a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery mtu 1500
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery prefix</h>

Configures the IPv6 prefix you want to include in router advertisements.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> autoconfig</h>

Configures automatic configuration to indicate to hosts on the local link that they can use the specified prefix for IPv6 auto configuration. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 autoconfig on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> off-link</h>

Configures advertisement to make no statement about prefix on-link or off-link properties. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 off-link on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> preferred-lifetime</h>

Configures the amount of time that addresses generated from a prefix remain preferred. You can specify a value between 0 and 4294967295. The default setting is 604800.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 preferred-lifetime 1000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> router-address</h>

Configures advertisement to indicate to hosts on the local link that the specified prefix contains a complete IP address by setting R flag.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 router-address on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\> valid-lifetime</h>

Configures the amount of time that the prefix is valid for on-link determination. You can specify a value between 0 and 4294967295. The default setting is 2592000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32 valid-lifetime 2000000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\></h>

Configures recursive DNS servers (RDNSS). You must specify the IPv6 address of each RDNSS you want to advertise.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\> lifetime</h>

Configures the maximum amount of time you want to use the RDNSS for domain name resolution. You can specify a value between 0 and 4294967295, or specify `infinite` to use the RDNSS for domain name resolution indefinitely. If you set the value to 0, the RDNSS address no longer advertises.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
|`<ipv6-address-id>` | The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100 lifetime infinite
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement</h>

Configures router advertisement for an interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement enable</h>

Turns router advertisement on or off for the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement enable off
```

{{%notice note%}}
In Cumulus Linux 5.5 and later, the NVUE command to enable router advertisment for an interface is `nv set interface swp1 ip neighbor-discovery router-advertisement enable on`.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement fast-retransmit</h>

Configures the specified interface to allow consecutive router advertisement packets to transmit more frequently than every three seconds (fast retransmit). The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement fast-retransmit off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement hop-limit</h>

Configures the hop limit value in the IP header of the outgoing router advertisement packet. You can set a value between 0 and 255. The default setting is 64.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement hop-limit 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement interval</h>

Configures the maximum time in milliseconds allowed between sending unsolicited multicast RA from the interface. You can set a value between 70 and 1800000 milliseconds. The default setting is 600000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement interval 60000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement interval-option</h>

Configures the specified interface to indicate to hosts that the router uses an advertisement interval to send router advertisements. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement interval-option on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement lifetime</h>

Configures the maximum amount of time that router advertisement messages can exist on the route. You can specify a value between 0 and 9000. The default setting is 1800.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement lifetime 4000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement managed-config</h>

Configures the specified interface to allow a dynamic host to use a managed protocol, such as DHCPv6, to configure IP addresses automatically (managed configuration). The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement managed-config on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement other-config</h>

Configures the specified interface to allow a dynamic host to use a managed protocol to configure additional information through DHCPv6. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement other-config on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement reachable-time</h>

Configures the amount of time that an IPv6 node is reachable. You can set a value between 0 and 3600000 milliseconds. The default setting is 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement reachable-time 3600000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement retransmit-time</h>

Configures the interval at which neighbor solicitation messages retransmit. You can set a value between 0 and 4294967295 milliseconds. The default setting is 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement retransmit-time 4294967295
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip neighbor-discovery router-advertisement router-preference</h>

Configures the specified interface to allow hosts to use router preference to select the default router. You can set a value of high, medium, or low. The default setting is `medium`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip neighbor-discovery router-advertisement router-preference high
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global nd base-reachable-time</h>

Configures how long a neighbor cache entry is valid. The entry is considered valid for at least the value between the base reachable time divided by two and three times the base reachable time divided by two. You can specify a value between 30 and 2147483 seconds. The default value is auto; NVUE derives the value for auto from the `/etc/sysctl.d/neigh.conf` file.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system global nd base-reachable-time 50
```
