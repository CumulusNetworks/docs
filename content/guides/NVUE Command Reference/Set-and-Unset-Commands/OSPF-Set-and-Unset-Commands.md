---
title: OSPF Set and Unset Commands
author: Cumulus Networks
weight: 620
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set router ospf

Configures global OSPF settings on the switch.

- - -

## nv set router ospf timers

Configures OSPF Link State Advertisement (LSA) and Shortest Path First (SPF) timers, and the refresh interval.

- - -

## nv set router ospf timers lsa

Configures LSA timers.

- - -

## nv set router ospf timers lsa min-arrival

Configures the minimum interval in seconds during which OSPF can accept the same LSA. You can specify a value between 0 and 600000.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers lsa min-arrival 300000
```

- - -

## nv set router ospf timers lsa throttle

Configures the amount of time after which OSPF sends LSAs. You can specify a value between 0 and 5000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers lsa throttle 3000
```

- - -

## nv set router ospf timers spf

Configures the SPF timers.

- - -

## nv set router ospf timers spf delay

Configures the amount of time to wait to do the SPF calculation after receiving the first topology change. You can specify a value between 0 and 600000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf delay 300000
```

- - -

## nv set router ospf timers spf holdtime

Configures the amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf holdtime 300000
```

- - -

## nv set router ospf timers spf max-holdtime

Configures the maximum amount of time to wait between consecutive SPF calculations. You can specify a value between 0 and 600000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers spf max-holdtime 300000
```

- - -

## nv set router ospf timers refresh 10-1800

Configures the refresh interval in seconds to resend LSAs to prevent them from aging out. You can specify a value between 10 and 1800 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf timers refresh 100
```

- - -

## nv set router ospf enable

Turns OSPF on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf enable on
```

- - -

## nv set router ospf router-id

Configures the OSPF router ID on the switch, which is a 32-bit value and is typically the address of the loopback interface. This command configures the router ID for all VRFs if a common one is used; otherwise, you must set the router ID for every VRF.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ospf router-id 10.10.10.1.
```

- - -

# nv set interface \<interface-id\> router ospf

Configures OSPF on an interface.

- - -

## nv set interface \<interface-id\> router ospf timers

Configures OSPF timers.

- - -

## nv set interface \<interface-id\> router ospf timers dead-interval

Configures the number of seconds to wait without a hello before declaring the neighbor dead. You can specify a value between 1 and 65535, or `minimal`. If you specify `minimal`, you must set the `hello-multiplier`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers dead-interval 600
```

- - -

## nv set interface \<interface-id\> router ospf timers hello-multiplier

Configures the multiplier to use if `dead-interval` is `minimal`. You can specify a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers hello-multiplier 6
```

- - -

## nv set interface \<interface-id\> router ospf timers hello-interval

Configures how often in seconds to transmit a hello packet. This setting is only valid if `dead-interval` is not `minimal`. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers hello-interval 600
```

- - -

## nv set interface \<interface-id\> router ospf timers retransmit-interval

Configures how often in seconds to retransmit a packet that is not acknowledged. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers retransmit-interval 600
```

- - -

## nv set interface \<interface-id\> router ospf timers transmit-delay

Configures the number of seconds to wait before sending a new LSA. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf timers retransmit-delay 600
```

- - -

## nv set interface \<interface-id\> router ospf authentication

Configures OSPF MD5 authentication on an interface.

- - -

## nv set interface \<interface-id\> router ospf authentication enable

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf authentication enable on
```

- - -

## nv set interface \<interface-id\> router ospf authentication message-digest-key

Configures the message digest key. You can specify a value between 1 and 255. The value must be consistent across all routers on a link.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf authentication message-digest-key 1
```

- - -

## nv set interface \<interface-id\> router ospf authentication md5-key \<value\>

Configures the MD5 key.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<value>` | The MD5 key. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf authentication md5-key thisisthekey
```

- - -

## nv set interface \<interface-id\> router ospf bfd

Configures Bidirectional Forwarding Detection (BFD) on an interface. BFD provides low overhead and rapid detection of failures in the paths between two network devices.

- - -

## nv set interface \<interface-id\> router ospf bfd enable

Turns BFD on and off on the OSPF interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd enable on
```

- - -

## nv set interface \<interface-id\> router ospf bfd detect-multiplier

Configures the detection time multiplier. You can specify a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd detect-multiplier 100
```

- - -

## nv set interface \<interface-id\> router ospf bfd min-receive-interval

Configures the required minimum interval between the received BFD control packets. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd min-receive-interval 400
```

- - -

## nv set interface \<interface-id\> router ospf bfd min-transmit-interval

Configures the minimum transmit interval in milliseconds. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf bfd min-transmit-interval 400
```

- - -

## nv set interface \<interface-id\> router ospf enable

Turns OSFP on and off on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf enable on
```

- - -

## nv set interface \<interface-id\> router ospf area

Configures the OSPF area on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf area 0
```

- - -

## nv set interface \<interface-id\> router ospf cost

Configures the cost of this link. You can specify a value between 1 and 65535 or `auto`, which automatically determines the cost based on link speed. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf cost 60
```

- - -

## nv set interface \<interface-id\> router ospf mtu-ignore

Configures OSPF to turn MTU value checking in the OSPF DBD packets on or off.

The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf mtu-ignore off
```

- - -

## nv set interface \<interface-id\> router ospf network-type

Configures the network type for the OSPF interface: point-to-point or broadcast. The default setting is `broadcast`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf network-type point-to-multipoint
```

- - -

## nv set interface \<interface-id\> router ospf passive

Configures the interface as passive. A passive interface creates a database entry but does not send or receive OSPF hello packets. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf passive on
```

- - -

## nv set interface \<interface-id\> router ospf priority

Configures the priority in becoming the OSPF Designated Router (DR) on a broadcast interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router ospf priority 5
```

- - -

## nv set vrf \<vrf-id\> router ospf

Configures OSPF in the specified VRF.

- - -

## nv set vrf \<vrf-id\> router ospf area \<area-id\>

Configures the OSPF area in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | Area|

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf area \<area-id\> filter-list

Configures network filtering between OSPF areas.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | Area |
 
### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\>

- - -

## nv set vrf \<vrf-id\> router ospf area \<area-id\> network \<network-id\>

Filters out components of the prefix

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` | Area |
| `<network-id>`  | Network|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router ospf area 0 network ???
```

- - -

## nv set vrf \<vrf-id\> router ospf area \<area-id\> default-lsa-cost

Configures the default LSA cost. Only applies when type is non-normal.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<area-id>` |   Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router ospf area 0 default-lsa-cost
```

- - -

## nv set vrf \<vrf-id\> router ospf default-originate

Advertise a default route as external lsa

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf default-originate metric-type

Set OSPF External Type 1/2 metrics

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router ospf distance

Administrative distance for installation into the rib

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router ospf max-metric

Set maximum metric value in router lsa to make stub router

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf log

Log configuration

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf redistribute

Route redistribute

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf redistribute static

Source route type.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |S

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf redistribute static metric-type

Set OSPF External Type 1/2 metrics

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router ospf redistribute connected

Source route type.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf redistribute connected metric-type

Set OSPF External Type 1/2 metrics

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router ospf redistribute kernel

Source route type.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf redistribute kernel metric-type

Set OSPF External Type 1/2 metrics

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router ospf redistribute bgp

Source route type.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf redistribute bgp metric-type

Set OSPF External Type 1/2 metrics

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router ospf timers

Timers

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf timers lsa

LSA timers

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf timers spf

SPF timers

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router ospf reference-bandwidth

Used to determine link cost/metric value relative to defined reference

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -
