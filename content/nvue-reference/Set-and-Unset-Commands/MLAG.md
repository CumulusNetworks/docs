---
title: MLAG
author: Cumulus Networks
weight: 600

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> bond mlag</h>

Provides commands to configure <span class="a-tooltip">[MLAG](## "Multi-chassis Link Aggregation")</span> on a bond interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond mlag enable</h>

Turns MLAG on or off on the bond interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bond mlag enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond mlag id</h>

Configures the MLAG ID on the bond interface. You must specify a unique MLAG ID (`clag-id`) for every dual-connected bond on each peer switch so that switches know which links dual-connect or connect to the same host or switch. The value must be between 1 and 65535 and must be the same on both peer switches. A value of 0 disables MLAG on the bond. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bond mlag id 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag</h>

Provides commands to configure global MLAG settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag backup \<backup-ip\></h>

Configures the IP address of a backup layer 3 interface for the peer link, which the switch uses when the peer link goes down. You must add a backup IP address, which must be different than the peer link IP address. You can use the loopback or management IP address of the switch.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<backup-ip>` |  The IP address of the backup interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag backup 10.10.10.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag backup \<backup-ip\> vrf \<vrf-name\></h>

Configures the VRF for the MLAG backup IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<backup-ip>` |  The IP address of the backup interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag backup 10.10.10.2 vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag debug</h>

Turns MLAG debugging on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag debug on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag enable</h>

Turns MLAG on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag init-delay</h>

Configures the number of seconds `clagd` delays bringing up MLAG bonds and anycast IP addresses. You can set a value between 0 and 9000.

This timer sets to 0 automatically under the following conditions:
- When the peer is not alive and the backup link is not active after a reload timeout.
- When the peer sends a goodbye (through the peer link or the backup link).
- When both MLAG sessions come up at the same time.

The default setting is 180.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag init-delay 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag mac-address</h>

Configures the MLAG system MAC address. NVIDIA provides a reserved range of MAC addresses for MLAG (between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff). Use a MAC address from this range to prevent conflicts with other interfaces in the same bridged network. Do not to use a multicast MAC address. Make sure you specify a different MAC address for each MLAG pair in the network. The default setting is `auto`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag peer-ip</h>

Configures the IP address of the MLAG peer. You can specify an IPv4 address, an IPv6 address or `linklocal`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag peer-ip linklocal
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set mlag priority</h>

Configures the MLAG priority. By default, the switch determines the role by comparing the MAC addresses of the two sides of the peering link; the switch with the lower MAC address assumes the primary role. You can override this by setting the priority option for the peer link. You can set a value between 0 and 65535. The default setting is 32768.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag priority 2084
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan mlag</h>

Provides commands to configure MLAG for VXLAN.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan mlag shared-address</h>

Configures the shared anycast address for MLAG peers.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set mlag vxlan mlag shared-address 10.10.10.2
```
