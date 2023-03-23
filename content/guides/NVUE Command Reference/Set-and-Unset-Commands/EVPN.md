---
title: EVPN
author: Cumulus Networks
weight: 560
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set evpn

Configures the EVPN control plane.

## nv set evpn dad

Configures EVPN duplicate address detection. The VTEP considers a host MAC or IP address to be duplicate if the address moves across the network more than a certain number of times within a certain number of seconds. In addition to legitimate host or VM mobility scenarios, address movement can occur when you configure IP addresses incorrectly on a host or when packet looping occurs in the network due to faulty configuration or behavior.

- - -

## nv set evpn dad duplicate-action

Configures the action to take when the switch flags a MAC address as a possible duplicate.

- - -

## nv set evpn dad enable

Enables and disables duplicate address detection. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad enable on
```

- - -

## nv set evpn dad duplicate-action freeze

Configures the switch to take no action for further move events for the MAC address.

- - -

## nv set evpn dad duplicate-action freeze duration

Configures the switch to freeze duplicate addresses for a specific period of time. You can specify a value between 30 and 3600 seconds or `permanent` to freeze duplicate addresses until you run the clear command.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad duplicate-action freeze duration permanent
```

- - -

## nv set evpn dad mac-move-threshold

Configures the number of MAC moves allowed within the detection time specified before the switch flags the MAC address as a possible duplicate. You can specify a value between 2 and 1000.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad mac-move-threshold 10
```

- - -

## nv set evpn dad move-window

Configures the detection time interval during which the MAC move threshold applies. You can specify a value between 2 and 1800.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn dad move-window 1200
```

- - -

## nv set evpn enable

Enables and disables the EVPN control plane. When enabled, the EVPN service offered is a VLAN-based service and an EVI is created automatically for each extended VLAN. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn enable on
```

- - -

## nv set evpn route-advertise

Configures EVPN route advertising.

- - -

## nv set evpn route-advertise default-gateway

Configures the gateway VTEPs to advertise their IP and MAC address. Only turn this setting on in a centralized routing deployment and only on the centralized gateway router. When set to `on`, the IP addresses of SVIs in all EVIs are announced as type-2 routes with the gateway extended community. The remote layer 2 only VTEPs use ARP suppression and the hosts learn of the gateway's IP to MAC binding. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn route-advertise default-gateway on
```

- - -

## nv set evpn route-advertise nexthop-setting

Configures how to advertise type-5 routes. Each switch in an MLAG pair advertises type-5 routes with its own system IP address, which creates an additional next hop at the remote VTEPs. In a large multi-tenancy EVPN deployment, where additional resources are a concern, you can disable this feature. Set this command to `shared-ip-mac` if you do not want to advertise type-5 routes with the system IP address. Set this command to `system-ip-mac` to advertise type-5 routes with the system IP address. The default setting is `system-ip-mac`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn route-advertise nexthop-setting shared-ip-mac
```

- - -

## nv set evpn route-advertise svi-ip

Configures the switch to announce the IP addresses of SVIs in all EVIs as type-2 routes. Only enable this option if you reuse SVI IP addresses in the network. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn route-advertise svi-ip on
```

- - -

## nv set evpn multihoming

Configures global EVPN multihoming configuration settings.

- - -

## nv set evpn multihoming ead-evi-route

Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-EVI (Ethernet Auto-discovery per EVPN instance) routes.

{{%notice note%}}
Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.
{{%/notice%}}

- - -

## nv set evpn multihoming ead-evi-route rx

Turns EAD-per-EVI at the receiving end on or off. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming ead-evi-route rx off
```

- - -

## nv set evpn multihoming ead-evi-route tx

Turns EAD-per-EVI route advertisement on or off. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming ead-evi-route tx off
```

- - -

## nv set evpn multihoming enable

Turns EVPN multihoming on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming enable on
```

- - -

## nv set evpn multihoming segment

Configures the switch to advertise type-1/EAD (Ethernet Auto-discovery) routes as EAD-per-ES (Ethernet Auto-discovery per Ethernet segment) routes.

{{%notice note%}}
Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.
{{%/notice%}}

- - -

## nv set evpn multihoming segment df-preference

Configures the designated forwarder preference value for EVPN multihoming. You can specify a value between 1 and 65535.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming segment df-preference 50000
```

- - -

## nv set evpn multihoming segment mac-address \<mac-address\>

Configures the MAC address per Ethernet segment for EVPN multihoming. This setting is required.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming segment mac-address 00:00:00:00:00:10
```

- - -

## nv set evpn multihoming mac-holdtime

Configures the MAC hold time, which specifies the duration for which a switch maintains SYNC MAC entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the MAC address on the local Ethernet segment. You can specify a value between 0 and 86400 seconds.

The default setting is 1080 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming mac-holdtime 1000
```

- - -

## nv set evpn multihoming neighbor-holdtime

Configures the neighbor hold times, which specifies the duration for which a switch maintains SYNC neighbor entries after the switch deletes the EVPN type-2 route of the Ethernet segment peer. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. You can specify a value between between 0 and 86400 seconds.

The default setting is 1080 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming neighbor-holdtime 600
```

- - -

## nv set evpn multihoming startup-delay

Configures the duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. You can specify a value between 0 and 3600 seconds.

The default setting is 180 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn multihoming startup-delay 1000
```

- - -

## nv set evpn vni

Enables the EVPN control plane so that the EVPN service offered is VLAN-based and an EVI is created automatically for each extended VLAN.

- - -

## nv set evpn vni \<vni-id\> route-target

Configures route targets for the specified VNI.

- - -

## nv set evpn vni \<vni-id\> route-target both \<rt-id\>

Configures the route targets you want to both import and export for the specified VNI.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn vni 10 route-target both 65101:10
```

- - -

## nv set evpn vni \<vni-id\> route-target export \<rt-id\>

Configures the route targets you want to export for the specified VNI.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn vni 10 route-target export 65101:10
```

- - -

## nv set evpn vni \<vni-id\> route-target import \<rt-id\>

Configures the route targets you want to import for the specified VNI.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn vni 10 route-target import 65102:10
```

- - -

## nv set evpn vni \<vni-id\> rd

Configures the BGP Route Distinguisher to use for EVPN type-5 routes originated from this VNI.

### Command Syntax

| Command |  Description   |
| ---------  | -------------- |
| `<vni-id>` | The VNI ID. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set evpn vni 10 rd 10.10.10.1:20
```

- - -
