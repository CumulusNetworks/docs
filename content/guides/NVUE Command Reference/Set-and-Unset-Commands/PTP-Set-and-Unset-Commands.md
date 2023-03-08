---
title: PTP Set and Unset Commands
author: Cumulus Networks
weight: 670
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> ptp

Provides PTP configuration commands for the interface.

- - -

## nv set interface \<interface-id\> ptp timers

Provides PTP configuration commands to set timers for PTP messages. The commands include the average interval between successive Announce messages, the number of announce intervals that have to occur without receiving an Announce message before a timeout occurs, the minimum average time interval allowed between successive Delay Required messages, and the interval between PTP synchronization messages on an interface.

- - -

## nv set interface \<interface-id\> ptp timers announce-interval

Configures the average interval between successive Announce messages. You specify the value as a power of two in seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers announce-interval -1
```

- - -

## nv set interface \<interface-id\> ptp timers sync-interval

The interval between PTP synchronization messages on an interface. You specify the value as a power of two in seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers sync-interval -5
```

- - -

## nv set interface \<interface-id\> ptp timers delay-req-interval

The minimum average time interval allowed between successive Delay Required messages. You specify the value as a power of two in seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers delay-req-interval -5
```

- - -

## nv set interface \<interface-id\> ptp timers announce-timeout

The number of announce intervals that have to occur without receiving an Announce message before a timeout occurs. Make sure that this value is longer than the `announce-interval` in your network.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp timers announce-interval 2
```

- - -

## nv set interface \<interface-id\> ptp enable

Turns PTP on the interface on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp enable on
```

- - -

## nv set interface \<interface-id\> ptp instance \<value\>

Configures the PTP instance number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1
```

- - -

## nv set interface \<interface-id\> ptp forced-master

Configures PTP interfaces to always be in a master state. This interface ignores any Announce messages it receives.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp forced-master on
```

- - -

## nv set interface \<interface-id\> ptp acceptable-master

Turns the acceptable master table option on or off for the interface. You must configure the clock IDs of known Grandmasters in the acceptable master table before turning on the acceptable master table option. The BMC algorithm checks if the Grandmaster received on the Announce message is in this table before proceeding with the master selection.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp acceptable-master on
```

- - -

## nv set interface \<interface-id\> ptp delay-mechanism end-to-end

Configures the PTP delay mechanism to be end-to-end, where the slave measures the delay between itself and the master. For PTP nodes to synchronize the time of day, each slave has to learn the delay between iteself and the master.

The default setting is `peer-to-peer`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp delay-mechanism end-to-end
```

- - -

## nv set interface \<interface-id\> ptp transport

Configures the transport method for PTP messages. You can encapsulate PTP messages in UDP/IPV4 frames or UDP/IPV6 frames.

The default setting is IPv4.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp transport ipv6
```

- - -

## nv set interface \<interface-id\> ptp ttl

Configures the maximum number of hops the PTP messages can travel.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp ttl 20
```

- - -

## nv set interface \<interface-id\> ptp mixed-multicast-unicast

Configures the mode in which PTP delay messages transmit; mixed (multicast and unicast) or multicast only. Specify `on` for mixed mode or `off` for multicast mode.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp mixed-multicast-unicast on
```

- - -

## nv set interface \<interface-id\> ptp unicast-service-mode

Configures the PTP interface on the switch to be a unicast client or a unicast server. Unicast mode reduces the amount of bandwidth consumed.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp unicast-service-mode server
```

- - -

## nv set interface \<interface-id\> ptp unicast-request-duration

Configures the unicast request duration; the service time in seconds requested during discovery.

The default setting is `300`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp unicast-request-duration 500
```

- - -

## nv set interface \<interface-id\> ptp unicast-master-table-id

Configures the unicast table ID; a unique ID that identifies the unicast master table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ptp unicast-master-table-id 1
```

- - -

## nv set service ptp \<instance-id\>

Provides commands to configure global Precision Time Protocol (PTP) settings.

- - -

## nv set service ptp \<instance-id\> acceptable-master \<clock-id\>

Configures the ID of a known Grandmaster clock in the acceptable master table. This setting prevents a rogue player from pretending to be the Grandmaster to take over the PTP network.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<clock-id>` |  The clock ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06
```

- - -

## nv set service ptp \<instance-id\> acceptable-master \<clock-id\> alt-priority \<value\>

Configures an alternate priority for the acceptable Grandmaster clock in the acceptable master table.
 
### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<clock-id>` |  The clock ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06 alt-priority 2
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\>

Configures a custom PTP profile.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> profile-type

Configures the profile type; ieee-1588 or itu-g-8275-1. PTP profiles are a standardized set of configurations and rules intended to meet the requirements of a specific application. Profiles define required, allowed, and restricted PTP options, network restrictions, and performance requirements.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 profile-type itu-g-8275-1
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> priority1

Configures the Priority 1 attribute of the local clock for the custom profile. Priority 1 overrides the clock class and quality selection criteria to select the best master clock.

The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 priority1 100
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> priority2

Configures the Priority 2 attribute of the local clock for the custom profile. Priority 2 identifies primary and backup clocks among identical redundant Grandmasters. You can specify a value between 0 and 255.

The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 priority2 100
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> local-priority

Configures the local priority attribute of the local clock for the custom profile. You can specify a value between 0 and 255.

The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 local-priority 100
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> domain

Configures the PTP domain for the custom profile. PTP domains allow different independent timing systems to be present in the same network without confusing each other. A PTP domain is a network or a portion of a network within which all the clocks synchronize. Every PTP message contains a domain number. A PTP instance works in only one domain and ignores messages that contain a different domain number.You can specify a value between 0 and 127.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 domain 28
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> delay-mechanism end-to-end

Configures the method of calculating the delay within the network to end-to-end. For PTP nodes to synchronize the time of day, each slave has to learn the delay between iteself and the master.

The default setting is `peer-to-peer`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 delay-mechanism end-to-end 
```

## nv set service ptp \<instance-id\> profile \<profile-id\> transport

Configures the transport mode for PTP messages. You can specify `ipv4`, `ipv6`, or `802.3`.

The default setting is `ipv4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 transport ipv6
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> announce-interval

Configures the interval at which PTP sends announce messages to the master. This is the mean time interval between successive Announce messages,  specified as a power of two in seconds. You can specify a value between -7 and 7.

The default setting is `-3`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 announce-interval 5
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> sync-interval

Configures how often PTP synchronizes with the master. This is the mean sync interval for multicast messages, specified as a power of two in seconds.You can specify a value between -7 and 7.

The default setting is `-4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 sync-interval 5
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> delay-req-interval

Configures the minimum average time interval allowed between successive Delay Required messages, specified as a power of two in seconds. You can specify a value between -7 and 7.

The default setting is `-4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 delay-req-interval 5
```

- - -

## nv set service ptp \<instance-id\> profile \<profile-id\> announce-timeout

Configures the number of announce intervals that have to pass without receipt of an Announce message before the timeout event occurs. You can specify a value between 2 and 255.

The default setting is `2`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 profile CUSTOM1 announce-timeout 5
```

- - -

## nv set service ptp \<instance-id\> monitor

Provides commands to configure PTP monitor settings.

- - -

## nv set service ptp \<instance-id\> monitor min-offset-threshold \<value\>

Sets the minimum difference allowed in nanoseconds between the master and slave time. You can set a value between -1000000000 and 0 nanoseconds.

The default setting is -50.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor min-offset-threshold -20
```

- - -

## nv set service ptp \<instance-id\> monitor max-offset-threshold \<value\>

Configures the maximum difference allowed in nanoseconds between the master and slave time. You can set a value between 0 and 1000000000 nanoseconds.

The default setting is 50.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-offset-threshold 30
```

- - -

## nv set service ptp \<instance-id\> monitor path-delay-threshold \<value\>

Configures the mean time in nanoseconds that PTP packets take to travel between the master and slave. You can set a value between 0 and 1000000000 nanoseconds.

The default setting is 200.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor path-delay-threshold 300
```

- - -

## nv set service ptp \<instance-id\> monitor max-timestamp-entries

Configures the maximum number of timestamp entries allowed. PTP updates the timestamps continuously. You can specify a value between 100 and 400.

The default setting is 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-timestamp-entries 300
```

- - -

## nv set service ptp \<instance-id\> monitor max-violation-log-sets

Configures the maximum number of violation log sets allowed. You can specify a value between 2 and 4.

The default setting is 4.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-violation-log-sets 3
```

- - -

## nv set service ptp \<instance-id\> monitor max-violation-log-entries

Configures the maximum number of violation log entries allowed for each set. You can specify a value between 2 and 8.

The default setting is 8.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor max-violation-log-entries 6
```

- - -

## nv set service ptp \<instance-id\> monitor violation-log-interval

Configures the violation log interval in seconds. You can specify a value between 0 and 60 seconds.

The default setting is 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 monitor violation-log-interval 1000
```

- - -

## nv set service ptp \<instance-id\> enable

Turns PTP on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 enable on
```

- - -

## nv set service ptp \<instance-id\> priority1 \<value\>

Configures PTP priority 1 to override the clock class and quality selection criteria and select the best master clock. You can set a value between 0 and 255.  For the boundary clock, use a number above 128. The lower priority applies first.

The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 priority1 200
```

- - -

## nv set service ptp \<instance-id\> priority2 \<value\>

Configures PTP priority 2 to identify primary and backup clocks among identical redundant Grandmasters. You can set a value between 0 and 255.  For the boundary clock, use a number above 128. The lower priority applies first.

The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 priority2 200
```

- - -

## nv set service ptp \<instance-id\> domain

Configures the PTP domain, which is a network or a portion of a network within which all the clocks synchronize. Every PTP message contains a domain number. A PTP instance works in only one domain and ignores messages that contain a different domain number.

You can specify multiple PTP clock domains. PTP isolates each domain from other domains so that each domain is a different PTP network. You can specify a number between 0 and 127.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 domain 3
```

- - -

## nv set service ptp \<instance-id\> ip-dscp

Configures the DiffServ code point (DSCP) value for all PTP IPv4 packets originated locally. You can set a value between 0 and 63.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ptp 1 ip-dscp 22
```
