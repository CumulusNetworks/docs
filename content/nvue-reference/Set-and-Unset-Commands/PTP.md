---
title: PTP
author: Cumulus Networks
weight: 680

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> ptp

Provides PTP interface configuration commands.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp acceptable-master</h>

Turns the acceptable master table option on or off for the interface. You must configure the clock IDs of known Grandmasters in the acceptable master table before turning on the acceptable master table option. The BMC algorithm checks if the Grandmaster received on the Announce message is in this table before proceeding with the master selection. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp acceptable-master on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp delay-mechanism end-to-end</h>

Configures the PTP delay mechanism to be end-to-end, where the slave measures the delay between itself and the master. For PTP nodes to synchronize the time of day, each slave has to learn the delay between itself and the master. The default setting is `peer-to-peer`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp delay-mechanism end-to-end
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp enable</h>

Turns PTP on the specified PTP interface on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp forced-master</h>

Configures PTP interfaces to always be in a master state. The interfaces ignore any Announce messages they receive. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp forced-master on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp instance \<value\></h>

Configures the PTP instance number for the specified PTP interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp mixed-multicast-unicast</h>

Configures the mode in which PTP delay messages transmit for the specified PTP interface; mixed (multicast and unicast) or multicast only. Specify `on` for mixed mode or `off` for multicast mode. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp mixed-multicast-unicast on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp shaper</h>

Configures PTP shaping on the NVIDIA Spectrum 1 switch for PTP-enabled ports with speeds lower than 100G to improve performance.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp shaper enable</h>

Turns a pre-defined traffic shaping profile on or off on the specified interface to improve performance. This command is available for the NVIDIA Spectrum 1 switch only for PTP-enabled ports with speeds lower than 100G. For example, if you see that the PTP timing offset varies widely and is does not stabilize, enable PTP shaping on all PTP enabled ports to reduce the bandwidth on the ports slightly and improve timing stabilization.

- Switches with Spectrum-2 and later do not support PTP shaping.
- Bonds do not support PTP shaping.
- You cannot configure QoS traffic shaping and PTP traffic shaping on the same ports.
- You must configure a strict priority for PTP traffic; for example:

   ```
   cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 0-5,7 mode dwrr
   cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 0-5,7 bw-percent 12
   cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 6 mode strict
   ```

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp shaper enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp timers</h>

Provides PTP configuration commands to set timers for PTP messages for the specified PTP interface. The commands include the average interval between successive Announce messages, the number of announce intervals that have to occur without receiving an Announce message before a timeout occurs, the minimum average time interval allowed between successive Delay Required messages, and the interval between PTP synchronization messages on an interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp timers announce-interval</h>

Configures the average interval between successive Announce messages for the specified PTP interface. You specify the value as a power of two in seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp timers announce-interval -1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp timers announce-timeout</h>

The number of announce intervals that have to occur without receiving an Announce message before a timeout occurs. Make sure that this value is longer than the `announce-interval` in your network.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp timers announce-interval 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp timers delay-req-interval</h>

The minimum average time interval allowed between successive Delay Required messages for the specified PTP interface. You specify the value as a power of two in seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp timers delay-req-interval -5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp timers sync-interval</h>

The interval between PTP synchronization messages on the specified PTP interface. You specify the value as a power of two in seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp timers sync-interval -5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp transport</h>

Configures the transport method for PTP messages for the specified PTP interface. You can encapsulate PTP messages in UDP IPV4 frames or UDP IPV6 frames. The default setting is IPv4.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp transport ipv6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp ttl</h>

Configures the maximum number of hops the PTP messages can travel for the specified PTP interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp ttl 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp unicast-master-table-id</h>

Configures the unicast table ID for the specified PTP interface, which is a unique ID that identifies the unicast master table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp unicast-master-table-id 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp unicast-request-duration</h>

Configures the unicast request duration for the specified PTP interface, which is the service time in seconds requested during discovery. The default setting is `300`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp unicast-request-duration 500
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ptp unicast-service-mode</h>

Configures the specified PTP interface to be a unicast client or a unicast server. Unicast mode reduces the amount of bandwidth consumed.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ptp unicast-service-mode server
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\></h>

Provides commands to configure global Precision Time Protocol (PTP) settings. The NVUE PTP commands require an instance number for management purposes.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> acceptable-master \<clock-id\></h>

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
cumulus@switch:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> acceptable-master \<clock-id\> alt-priority \<value\></h>

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
cumulus@switch:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06 alt-priority 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> current-profile</h>

Configures the current PTP profile. PTP profiles are a standardized set of configurations and rules intended to meet the requirements of a specific application. Profiles define required, allowed, and restricted PTP options, network restrictions, and performance requirements.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 current-profile default-itu-8275-1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> domain</h>

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
cumulus@switch:~$ nv set service ptp 1 domain 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> enable</h>

Turns PTP on or off globally. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 enable on
```

HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> force-version</h>

Configures the PTP minor version. Cumulus Linux uses a `linuxptp` package that is PTP v2.1 compliant, and sets the major PTP version to 2 and the minor PTP version to 1 by default in the configuration. If your PTP configuration does not work correctly when the minor version is set, you can change the minor version to 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 force-version 2.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> ip-dscp</h>

Configures the <span class="a-tooltip">[DSCP](## "DiffServ code point")</span> value for all PTP IPv4 packets originated locally. You can set a value between 0 and 63.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 ip-dscp 22
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor</h>

Provides commands to configure PTP monitor settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor max-offset-threshold</h>

Configures the maximum difference allowed in nanoseconds between the master and slave time. You can set a value between 0 and 1000000000 nanoseconds. The default setting is 50.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 monitor max-offset-threshold 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor max-timestamp-entries</h>

Configures the maximum number of timestamp entries allowed. PTP updates the timestamps continuously. You can specify a value between 100 and 400. The default setting is 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 monitor max-timestamp-entries 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor max-violation-log-entries</h>

Configures the maximum number of violation log entries allowed for each log set. You can specify a value between 2 and 8. The default setting is 8.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 monitor max-violation-log-entries 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor max-violation-log-sets</h>

Configures the maximum number of violation log sets allowed. You can specify a value between 2 and 4. The default setting is 4.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 monitor max-violation-log-sets 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor min-offset-threshold</h>

Sets the minimum difference allowed in nanoseconds between the master and slave time. You can set a value between -1000000000 and 0 nanoseconds. The default setting is -50.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 monitor min-offset-threshold -20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor path-delay-threshold</h>

Configures the mean time in nanoseconds that PTP packets take to travel between the master and slave. You can set a value between 0 and 1000000000 nanoseconds. The default setting is 200.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 monitor path-delay-threshold 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> monitor violation-log-interval</h>

Configures the violation log interval in seconds. You can specify a value between 0 and 60 seconds. The default setting is 0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 monitor violation-log-interval 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> priority1</h>

Configures PTP priority 1 to override the clock class and quality selection criteria and select the best master clock. You can set a value between 0 and 255. For the boundary clock, use a number above 128. The lower priority applies first. The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 priority1 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> priority2</h>

Configures PTP priority 2 to identify primary and backup clocks among identical redundant Grandmasters. You can set a value between 0 and 255. For the boundary clock, use a number above 128. The lower priority applies first. The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 priority2 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\></h>

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
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> announce-interval</h>

Configures the interval at which PTP sends announce messages to the master for the custom profile. This is the mean time interval between successive Announce messages, specified as a power of two in seconds. You can specify a value between -7 and 7. The default setting is `-3`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 announce-interval 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> announce-timeout</h>

Configures the number of announce intervals that have to pass without receipt of an Announce message before the timeout event occurs for the custom profile. You can specify a value between 2 and 255. The default setting is `2`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 announce-timeout 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> delay-mechanism end-to-end</h>

Configures the method of calculating the delay within the network to end-to-end for the custom profile. For PTP nodes to synchronize the time of day, each slave has to learn the delay between itself and the master. The default setting is `peer-to-peer`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 delay-mechanism end-to-end 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> delay-req-interval</h>

Configures the minimum average time interval allowed between successive Delay Required messages, specified as a power of two in seconds, for the custom profile. You can specify a value between -7 and 7. The default setting is `-4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 delay-req-interval 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> domain</h>

Configures the PTP domain for the custom profile. PTP domains allow different independent timing systems to be present in the same network without confusing each other. A PTP domain is a network or a portion of a network within which all the clocks synchronize. Every PTP message contains a domain number. A PTP instance works in only one domain and ignores messages that contain a different domain number. You can specify a value between 0 and 127.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 domain 28
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> local-priority</h>

Configures the local priority attribute of the local clock for the custom profile. You can specify a value between 0 and 255. The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 local-priority 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> priority1</h>

Configures the Priority 1 attribute of the local clock for the custom profile. Priority 1 overrides the clock class and quality selection criteria to select the best master clock. The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 priority1 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> priority2</h>

Configures the Priority 2 attribute of the local clock for the custom profile. Priority 2 identifies primary and backup clocks among identical redundant Grandmasters. You can specify a value between 0 and 255. The default setting is 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 priority2 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> profile-type</h>

Configures the profile type for the custom profile; ieee-1588 or itu-g-8275-1. PTP profiles are a standardized set of configurations and rules intended to meet the requirements of a specific application. Profiles define required, allowed, and restricted PTP options, network restrictions, and performance requirements.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 profile-type itu-g-8275-1
```
<!--
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> servo noise-transfer</h>

Enables Noise Transfer Servo to smooth the jitter and wander noise from the Master clock.

{{%notice note%}}
- To use Noise Transfer Servo, you need to enable SyncE on the switch and on PTP interfaces.
- Cumulus Linux supports Noise Transfer Servo on Spectrum ASICs that support SyncE.
- NVIDIA recommends you do not change the default Noise Transfer Servo configuration parameters.
- NVIDIA recommends you use Noise Transfer Servo with PTP Telecom profiles. If you use other profiles or choose not to use a profile, make sure to set the sync interval to -3 or better.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 servo noise-transfer
```
-->
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> sync-interval</h>

Configures how often PTP synchronizes with the master for the custom profile. This is the mean sync interval for multicast messages, specified as a power of two in seconds. You can specify a value between -7 and 7. The default setting is `-4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 sync-interval 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> transport</h>

Configures the transport mode for PTP messages for the custom profile. You can specify `ipv4`, `ipv6`, or `802.3`. The default setting is `ipv4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 transport ipv6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> profile \<profile-id\> two-step</h>

Configures clock correction mode for a custom profile. Specify `off` to use one-step mode or `on` to use two-step mode. The default value is `on`.

In one-step mode, PTP time stamps the packet as it egresses the port and there is no need for a follow-up packet.
In two-step mode, PTP notes the time when the packet egresses the port and sends it in a separate follow-up message.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<profile-id>` |  The custom profile name. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 two-step off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> two-step</h>

Configures clock correction mode if no profile is set. Specify `off` to use one-step mode or `on` to use two-step mode. The default value is `on`.

In one-step mode, PTP time stamps the packet as it egresses the port and there is no need for a follow-up packet.
In two-step mode, PTP notes the time when the packet egresses the port and sends it in a separate follow-up message.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 two-step off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> unicast-master \<table-id\></h>

Configures the PTP unicast master table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<table-id>` |  The unicast master table ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 unicast-master 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> unicast-master \<table-id\> address</h>

Configures the IP addresses of the PTP master clocks for unicast requests. You can specify an IPv4, IPv6, or MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<table-id>` |  The PTPT unicast master table ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 unicast-master 1 address 10.10.1.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> unicast-master \<table-id\> peer-address</h>

Configures the IP address of the external peer from which to accept unicast requests. You can specify an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<table-id>` |  The PTP unicast master table ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 unicast-master 1 peer-address 10.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ptp \<instance-id\> unicast-master \<table-id\> query-interval</h>

Configures how often to query for unicast sessions with each of the master clocks listed in the unicast master table. You can set a value between -3 and 4.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<instance-id>` |  The PTP instance number used for management purposes. |
| `<table-id>` |  The PTP unicast master table ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ptp 1 unicast-master 1 query-interval 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> ptp</h>

Configures PTP in the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> ptp enable</h>

Turns PTP on or off in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED ptp enable on
```
