---
title: EVPN
author: Cumulus Networks
weight: 560

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set evpn</h>

Configures the EVPN control plane.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn dad</h>

Configures EVPN duplicate address detection. The VTEP considers a host MAC or IP address to be duplicate if the address moves across the network more than a certain number of times within a certain number of seconds. In addition to legitimate host or VM mobility scenarios, address movement can occur when you configure IP addresses incorrectly on a host or when packet looping occurs in the network due to faulty configuration or behavior.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn dad duplicate-action</h>

Configures the action to take when the switch flags a MAC address as a possible duplicate.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn dad duplicate-action freeze</h>

Configures the switch to take no action for further move events for the MAC address.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn dad duplicate-action freeze duration</h>

Configures the switch to freeze duplicate addresses for a specific period of time. You can specify a value between 30 and 3600 seconds or `permanent` to freeze duplicate addresses until you run the clear command.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn dad duplicate-action freeze duration permanent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn dad enable</h>

Enables and disables duplicate address detection. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn dad enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn dad mac-move-threshold</h>

Configures the number of MAC moves allowed within the detection time specified before the switch flags the MAC address as a possible duplicate. You can specify a value between 2 and 1000.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn dad mac-move-threshold 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn dad move-window</h>

Configures the detection time interval during which the MAC move threshold applies. You can specify a value between 2 and 1800.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn dad move-window 1200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn enable</h>

Enables and disables the EVPN control plane. When enabled, the EVPN service offered is a VLAN-based service and Cumulus Linux creates an EVI automatically for each extended VLAN. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn mac-vrf-soo</h>

Configures a site ID. When you use EVPN with MLAG, EVPN might install local MAC addresses or neighbor entries as remote entries. To prevent EVPN from taking ownership of local MAC addresses or neighbor entries from MLAG, you can associate all local layer 2 VNIs with a unique site ID, which represents an MLAG pair.

When you configure a site ID, Cumulus Linux:
- Adds a Site-of-Origin extended community encoded with the local site ID to EVPN routes that originate from local layer 2 VNIs. Cumulus Linux adds the Site-of-Origin extended community when creating the route.
- Filters all received EVPN routes with a `Site-of-Origin` extended community that matches the local site ID. Cumulus Linux filters the routes when importing the routes from the global table to the layer 2 VNI or layer 3 VNI table.

The site ID is in the format `<IPv4 address>:<2-byte Value>`, where the IPv4 address is the anycast IP address (a virtual IP address for VXLAN data-path termination) and the 2-byte value is an integer between 0 and 65535. For example: 10.0.1.12:10

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set evpn mac-vrf-soo 10.0.1.12:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming</h>

Configures global EVPN multihoming configuration settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming ead-evi-route</h>

Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-EVI (Ethernet Auto-discovery per EVPN instance) routes.

{{%notice note%}}
Some third-party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming ead-evi-route rx</h>

Turns EAD-per-EVI at the receiving end on or off. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming ead-evi-route rx off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming ead-evi-route tx</h>

Turns EAD-per-EVI route advertisement on or off. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming ead-evi-route tx off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming enable</h>

Turns EVPN multihoming on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming mac-holdtime</h>

Configures the MAC hold time, which specifies the duration for which a switch maintains SYNC MAC entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the MAC address on the local Ethernet segment. You can specify a value between 0 and 86400 seconds. The default setting is 1080 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming mac-holdtime 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming neighbor-holdtime</h>

Configures the neighbor hold times, which specifies the duration for which a switch maintains SYNC neighbor entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. You can specify a value between 0 and 86400 seconds. The default setting is 1080 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming neighbor-holdtime 600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming segment</h>

Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-ES (Ethernet Auto-discovery per Ethernet segment) routes.

{{%notice note%}}
Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming segment df-preference</h>

Configures the designated forwarder preference value for EVPN multihoming. You can specify a value between 1 and 65535.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming segment df-preference 50000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming segment mac-address \<mac-address\></h>

Configures the MAC address per Ethernet segment for EVPN multihoming. This setting is required.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming segment mac-address 00:00:00:00:00:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn multihoming startup-delay</h>

Configures the duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. You can specify a value between 0 and 3600 seconds. The default setting is 180 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn multihoming startup-delay 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn route-advertise</h>

Configures EVPN route advertising.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn route-advertise default-gateway</h>

Configures the gateway VTEPs to advertise their IP and MAC address. Only turn this setting on in a centralized routing deployment and only on the centralized gateway router. When set to `on`, the IP addresses of SVIs in all EVIs announce as type-2 routes with the gateway extended community. The remote layer 2 only VTEPs use ARP suppression and the hosts learn of the gateway's IP to MAC binding. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn route-advertise default-gateway on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn route-advertise nexthop-setting</h>

Configures how to advertise type-5 routes. Each switch in an MLAG pair advertises type-5 routes with its own system IP address, which creates an additional next hop at the remote VTEPs. In a large multi-tenancy EVPN deployment, where additional resources are a concern, you can disable this feature. Set this command to `shared-ip-mac` if you do not want to advertise type-5 routes with the system IP address. Set this command to `system-ip-mac` to advertise type-5 routes with the system IP address. The default setting is `system-ip-mac`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn route-advertise nexthop-setting shared-ip-mac
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn route-advertise svi-ip</h>

Configures the switch to announce the IP addresses of SVIs in all EVIs as type-2 routes. Only enable this option if you reuse SVI IP addresses in the network. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn route-advertise svi-ip on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn vni</h>

Enables the EVPN control plane so that the EVPN service offered is VLAN-based and Cumulus Linux creates an EVI automatically for each extended VLAN.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv set evpn evi,`
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn vni \<vni-id\> rd</h>

Configures the BGP Route Distinguisher to use for EVPN type-5 routes originated from this VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv set evpn evi <vni-id> rd`
{{%/notice%}}

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set evpn vni 10 rd 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn vni \<vni-id\> route-target</h>

Configures route targets for the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv set evpn evi <vni-id> route-target`
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn vni \<vni-id\> route-target both \<rt-id\></h>

Configures the route targets you want to both import and export for the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv set evpn evi <vni-id> route-target both <rt-id>`
{{%/notice%}}

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn vni 10 route-target both 65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn vni \<vni-id\> route-target export \<rt-id\></h>

Configures the layer 2 <span class="a-tooltip">[RTs](## "route targets")</span> you want to export for the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv set evpn evi <vni-id> route-target export <rt-id>`
{{%/notice%}}

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn vni 10 route-target export 65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set evpn vni \<vni-id\> route-target import \<rt-id\></h>

Configures the layer 2 <span class="a-tooltip">[RTs](## "route targets")</span> you want to import for the specified VNI.

{{%notice note%}}
In Cumulus Linux 5.3 and earlier, this command is `nv set evpn evi <vni-id> route-target import <rt-id>`
{{%/notice%}}

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set evpn vni 10 route-target import 65102:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> evpn</h>

Configures the EVPN control plane on the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> evpn enable</h>

Turns the EVPN control plane on or off in the specified VRF.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED evpn enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> evpn vlan</h>

Configures the VLAN for the EVPN instance in the specified VRF. You can specify a value between 1 and 4094, or `auto`.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |
| `<vlan-id>` | The VLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED evpn vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> evpn vni \<vni-id\></h>

Configures the layer 3 VNI for the EVPN instance in the specified VRF. You can specify a value between 1 and 16777214, or `auto`.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |
| `<vni-id>` | The layer 3 VNI ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED evpn vni 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> evpn prefix-routes-only</h>

Configures the switch to advertise IP prefix routes (type 5 routes) only in the specified VRF. You can specify `on` or `off`.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED evpn prefix-routes-only on
```
