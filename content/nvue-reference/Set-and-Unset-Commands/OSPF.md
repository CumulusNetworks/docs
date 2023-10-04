---
title: OSPF
author: Cumulus Networks
weight: 630

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> router ospf</h>

Configures OSPF on an interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf area</h>

Configures the OSPF area on the specified OSPF interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf area 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf authentication</h>

Configures OSPF MD5 authentication for the specified interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf authentication enable</h>

Turns OSPF authentication on or off on the specified interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf authentication enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv set interface \<interface-id\> router ospf authentication md5-key \<value\></h>

Configures the MD5 key for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<value>` | The MD5 key. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf authentication md5-key thisisthekey
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf authentication message-digest-key</h>

Configures the message digest key for the specified interface. You can specify a value between 1 and 255. The value must be consistent across all routers on a link.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf authentication message-digest-key 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf bfd</h>

Configures <span style="background-color:#F5F5DC">[BFD](## "Bidirectional Forwarding Detection")</span> on the specified interface. BFD provides low overhead and rapid detection of failures in the paths between two network devices.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf bfd detect-multiplier</h>

Configures the detection time multiplier on the specified OSPF interface. You can specify a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf bfd detect-multiplier 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf bfd enable</h>

Turns BFD on and off on the specified OSPF interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf bfd enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf bfd min-receive-interval</h>

Configures the required minimum interval between received BFD control packets on the specified OSPF interface. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf bfd min-receive-interval 400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf bfd min-transmit-interval</h>

Configures the minimum transmit interval in milliseconds on the specified OSPF interface. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf bfd min-transmit-interval 400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf cost</h>

Configures the cost of this link. You can specify a value between 1 and 65535 or `auto`, which automatically determines the cost based on link speed. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf cost 60
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf enable</h>

Turns OSFP on and off on the specified OSPF interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf mtu-ignore</h>

Configures OSPF to turn MTU value checking in the OSPF DBD packets on or off. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf mtu-ignore off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf network-type</h>

Configures the network type for the OSPF interface: point-to-point or broadcast. The default setting is `broadcast`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf network-type point-to-multipoint
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf passive</h>

Configures the OSPF interface as passive. A passive interface creates a database entry but does not send or receive OSPF hello packets. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf passive on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf priority</h>

Configures the priority in becoming the OSPF Designated Router (DR) on a broadcast interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf priority 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf timers</h>

Configures OSPF timers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf timers dead-interval</h>

Configures the number of seconds to wait without a hello before declaring the neighbor dead. You can specify a value between 1 and 65535, or `minimal`. If you specify `minimal`, you must set the `hello-multiplier`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf timers dead-interval 600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf timers hello-interval</h>

Configures how often in seconds to transmit a hello packet. This setting is only valid if `dead-interval` is not `minimal`. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf timers hello-interval 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf timers hello-multiplier</h>

Configures the multiplier to use if `dead-interval` is `minimal`. You can specify a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf timers hello-multiplier 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf timers retransmit-interval</h>

Configures how often in seconds to retransmit a packet that is not acknowledged. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf timers retransmit-interval 600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router ospf timers transmit-delay</h>

Configures the number of seconds to wait before sending a new LSA. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf timers retransmit-delay 600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf</h>

Configures global OSPF settings on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf enable</h>

Turns OSPF on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf router-id</h>

Configures the OSPF router ID on the switch, which is a 32-bit value and is typically the address of the loopback interface. This command configures the router ID for all VRFs if it is a common one; otherwise, you must set the router ID for every VRF.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf router-id 10.10.10.1.
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers</h>

Configures the OSPF <span style="background-color:#F5F5DC">[LSA](## "Link State Advertisement")</span> timers, <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> timers, and the refresh interval.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers lsa</h>

Configures <span style="background-color:#F5F5DC">[LSA](## "Link State Advertisement")</span> timers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers lsa min-arrival</h>

Configures the minimum interval in seconds during which OSPF can accept the same LSA. You can specify a value between 0 and 600000.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf timers lsa min-arrival 300000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers lsa throttle</h>

Configures the amount of time after which OSPF sends LSAs. You can specify a value between 0 and 5000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf timers lsa throttle 3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers refresh</h>

Configures the refresh interval in seconds to resend LSAs to prevent them from aging out. You can specify a value between 10 and 1800 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf timers refresh 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers spf</h>

Configures OSPF <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> timers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers spf delay</h>

Configures the amount of time to wait before calculating the SPF after receiving the first topology change. You can specify a value between 0 and 600000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf timers spf delay 80
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers spf holdtime</h>

Configures the amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf timers spf holdtime 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ospf timers spf max-holdtime</h>

Configures the maximum amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router ospf timers spf max-holdtime 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf</h>

Configures OSPF in the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\></h>

Configures the OSPF area in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF you want to configure. |
| `<area-id>` | The OSPF area. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router ospf area 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> default-lsa-cost</h>

Configures the default LSA cost. This setting applies only when the OSPF area type is not `normal`. You can specify a value between 0 and 16777215.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` |   The OSPF area. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 default-lsa-cost 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> filter-list</h>

Configures network filtering between OSPF areas.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> filter-list in \<filter-id\></h>

Configures the prefix list to use as an inbound filter for the OSPF area in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF you want to configure. |
| `<area-id>` | The OSPF area. |
| `<filter-id>` | The filter name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 filter-list in MY-OSPF-IN-FILTER
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> filter-list out</h>

Configures the prefix list to use as an outbound filter for the OSPF area in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | The OSPF area. |
| `<filter-id>` | The filter name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 filter-list out MY-OSPF-OUT-FILTER
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> network \<network-id\></h>

Configures prefix filters for an OSPF area in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | The OSPF area. |
| `<network-id>`  | The subnet prefix.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 network 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> range</h>

Configures the OSPF area prefix range settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\></h>

Configures a summary route for all the routes in the specified range in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | The OSPF area. |
| `<range-id>` | The IPv4 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 range 172.16.1.0/24
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\> cost</h>

Configures the metric advertised for the specified address range. You can specify a value between 0 and 16777215, or `auto`. The default value is `auto` (Cumulus Linux derives the operational default value from the components).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | The OSPF area. |
| `<range-id>`  | The IPv4 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 range 172.16.1.0/24 cost 65535
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\> suppress</h>

Configures OSPF to filter out components but not advertise the specified address range. The default setting is `off` (advertise the specified address range).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | The OSPF area. |
| `<range-id>`  | The IPv4 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 range 172.16.1.0/24 suppress on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv set vrf \<vrf-id\> router ospf area \<area-id\> type</h>

Configures the OSPF area type. You can specify `normal`, `stub`, `totally-stub`, `nssa`, or `totally-nssa`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` |   The OSPF area. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf area 0 type stub
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf default-originate</h>

Configures OSPF to advertise the default route to its neighbors, regardless of whether it is in the routing table or not.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf default-originate always</h>

Configures OSPF to advertise a default route to other routers even if there is no default route in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf default-originate always on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf default-originate enable</h>

Turns OSPF default originate on or off. The default value is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf default-originate enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf default-originate metric</h>

Configures the OSPF default originate metric. You can specify a value between 0 and 16777214, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf default-originate metric 16777214
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf default-originate metric-type</h>

Configures the OSPF default originate metric type; 1 or 2.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf default-originate metric-type 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf default-originate route-map

Applies the specified route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf default-originate route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf distance</h>

Configures the administrative distance for OSPF routes. Cumulus Linux uses the administrative distance to choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPF with an administrative distance of 110 and the same route from BGP with an administrative distance of 100, the switch chooses BGP.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf distance external</h>

Configures the external administrative distance for OSPF routes. You can specify a value between 1 and 255, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf distance external 220
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf distance inter-area</h>

Configures the administrative distance for internal OSPF routes. You can specify a value between 1 and 255, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf distance inter-area 150
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf distance intra-area</h>

Configures the administrative distance for internal OSPF routes. You can specify a value between 1 and 255, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf distance intra-area 150
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf enable</h>

Turns OSPF on or off on the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf log</h>

Configures OSPF logging.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf log adjacency-changes</h>

Configures logging for adjacency changes. You can specify `on`, `off`, or `detail`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf log adjacency-changes on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf max-metric</h>

Configures an OSPF maximum metric to notify its neighbors not to use the router as part of the OSPF topology. While the network converges, all traffic forwarded to the max-metric router is still forwarded. After you update the network, the max-metric router no longer receives any traffic and you can configure the max-metric setting.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf max-metric administrative</h>

Turns OSPF maximum metric on or off administratively, for an indefinite period. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf max-metric administrative on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf max-metric on-shutdown</h>

Configures the OSPF maximum metric on shutdown. You can specify a value between 5 and 100, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf max-metric on-shutdown 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf max-metric on-startup</h>

Configures the OSPF maximum metric on startup. You can specify a value between 5 and 86400, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf max-metric on-startup 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute</h>

Configures OSPF route redistribution.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute bgp</h>

Configures OSPF BGP route redistribution.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute bgp enable</h>

Turns OSPF BGP route redistribution on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute bgp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute bgp metric</h>

Configures the metric for OSPF BGP route redistribution. You can specify a value between 0 and 16777214, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute bgp metric 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute bgp metric-type \<type\></h>

Configures the metric type for OSPF BGP route redistribution; 1 or 2.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute bgp metric-type 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute bgp route-map \<route-map-id\></h>

Applies the specified route map for OSPF BGP route redistribution.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<route-map-id>` | The route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute bgp route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute connected</h>

Configures connected route redistribution.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute connected enable</h>

Turns OSPF connected route redistribution on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute connected enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute connected metric</h>

Configures the metric for OSPF connected route redistribution. You can specify a value between 0 and 16777214 or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute connected metric 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute connected metric-type</h>

Configures the metric type for OSPF connected route redistribution; 1 or 2.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute connected metric-type 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute connected route-map \<route-map-id\></h>

Applies the specified route map for OSPF connected route redistribution.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-map-id>` |   The route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute connected route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute kernel</h>

Configures OSPF kernel route redistribution.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute kernel enable</h>

Turns OSPF kernel route redistribution on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute kernel enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute kernel metric</h>

Configures the metric for OSPF kernel route redistribution. You can specify a value between 0 and 16777214, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute kernel metric 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute kernel metric-type</h>

Configures the metric type for OSPF kernel route redistribution; 1 or 2.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute kernel metric-type 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute kernel route-map \<route-map-id\></h>

Applies the specified route map for OSPF kernel route redistribution.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-map-id>` |   The route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute kernel route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute static</h>

Configures OSPF static route redistribution.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute static enable</h>

Turns OSPF static route redistribution on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute static enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute static metric</h>

Configures the metric for OSPF static route redistribution. You can specify a value between 0 and 16777214, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute static metric 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute static metric-type</h>

Configures the metric type for OSPF static route redistribution; 1 or 2.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute static metric-type 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf redistribute static route-map \<route-map\></h>

Applies the specified route map for OSPF static route redistribution.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf redistribute static route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf reference-bandwidth</h>

Configures the auto-cost reference bandwidth. When you set the auto-cost reference bandwidth, Cumulus Linux dynamically calculates the OSPF interface cost to support higher speed links. You can specify a value between 1 and 4294967. The default value is 100000 for 100Gbps link speed.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf reference-bandwidth 9000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf rfc1583-compatible</h>

Configures the OSPF router to be compatible with RFC1583 (OSPFv2).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf rfc1583-compatible off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf router-id</h>

Configures the OSPF router ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf router-id 10.10.10.1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers</h>

Configures OSPF timers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers lsa</h>

Configures OSPF LSA timers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers lsa min-arrival</h>

Configures the minimum interval for accepting the same LSA. You can specify a value between 0 and 600000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf timers lsa min-arrival 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers lsa throttle</h>

Configures the minimum interval in milliseconds between LSA updates in OSPF during times of network instability. You can specify a value between 0 and 5000, or `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf timers lsa throttle 3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers refresh</h>

Configures the interval in seconds to re-send LSAs to keep from aging out. You can specify a value between 10 and 1800, or `auto`. `auto` inherits the global setting. The default is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf timers refresh 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers spf</h>

Configures OSPF SPF timers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers spf delay</h>

Configures the number of milliseconds from the initial event until SPF runs. You can specify a value between 0 and 600000, or `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf timers spf delay 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers spf holdtime</h>

Configures the number of milliseconds between consecutive SPF runs. You can specify a value between 0 and 600000, or `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf timers spf holdtime 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router ospf timers spf max-holdtime</h>

Configures the maximum number of milliseconds between SPFs. You can specify a value between 0 and 600000, or `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router ospf timers spf max-holdtime 3000
```
