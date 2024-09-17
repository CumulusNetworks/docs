---
title: System Forwarding
author: Cumulus Networks
weight: 770

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system forwarding</h>

Configures switch forwarding.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash</h>

Configures custom hashing to specify what to include in the hash calculation during load balancing between multiple next hops of a layer 3 route (ECMP hashing).

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash destination-ip</h>

Turns ECMP hashing on the destination IP field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash destination-ip on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash destination-port</h>

Turns ECMP hashing on the destination port field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash destination-port on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash gtp-teid</h>

Turns ECMP hashing on the GTP TEID field on or off. The default setting is `off`.

GTP TEID-based ECMP hashing is only applicable if the outer header egressing the port is GTP encapsulated and if the ingress packet is either a GTP-U packet or a VXLAN encapsulated GTP-U packet.

{{%notice note%}}
- Cumulus Linux supports GTP Hashing on NVIDIA Spectrum-2 and later.
- GTP-C packets are not part of GTP hashing.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash gtp-teid on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash ingress-interface</h>

Turns ECMP hashing on the ingress interface on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash ingress-interface on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash inner-ip-protocol</h>

Turns ECMP hashing on the inner IP protocol field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash inner-ip-protocol on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash inner-destination-ip</h>

Turns ECMP hashing on the inner destination IP address field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash inner-destination-ip on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash inner-destination-port</h>

Turns ECMP hashing on the inner destination port field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash inner-destination-port on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash inner-ipv6-label</h>

Turns ECMP hashing on the inner IPv6 label field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash inner-ipv6-label on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash inner-source-ip</h>

Turns ECMP hashing on the inner source IP address field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash inner-ip-protocol on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash inner-source-port</h>

Turns ECMP hashing on the inner source port field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash inner-source-port on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash ipv6-label</h>

Turns ECMP hashing on the IPv6 label field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash ipv6-label on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash ip-protocol</h>

Turns ECMP hashing on the IP protocol field on or off. For IP traffic, the switch uses IP header source and destination fields in the hash calculation. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash ip-protocol on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash source-ip</h>

Turns ECMP hashing on the source IP field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash source-ip on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-hash source-port</h>

Turns ECMP hashing on the source port field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-hash source-port on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding hash-seed</h>

Configures a unique hash seed for each switch to prevent hash polarization, a type of network congestion that occurs when multiple data flows try to reach a switch using the same switch ports.

You can set a hash seed value between 0 and 4294967295. If you do not specify a value, `switchd` creates a randomly generated seed.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding hash-seed 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-weight-normalisation max-hw-weight</h>

Configures the maximum number of hardware entries for weighted ECMP. You can specify a value between 8 and 4096. The default value is 32.

The NVIDIA Spectrum switch supports weight programming for ECMP by repeating each individual path, which consumes resources. To reduce hardware utilization of ECMP resources, you can enable weight normalization.

{{%notice note%}}
In Cumulus Linux 5.9 and earlier, the minimum number of hardware entries for weighted ECMP that you can specify is 10 and the maximum number is 255.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-weight-normalisation max-hw-weight 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding ecmp-weight-normalisation mode</h>

Enables (`enabled`) and disables (`disabled`) ECMP weight normalization.

The NVIDIA Spectrum switch supports weight programming for ECMP by repeating each individual path, which consumes resources. To reduce hardware utilization of ECMP resources, you can enable weight normalization.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system forwarding ecmp-weight-normalisation mode enabled on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding host-route-preference</h>

Configures the forwarding host route preference: `route`, `neighbour`, or `route-and-neighbour`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding host-route-preference neighbour
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash</h>

Configures custom hashing to load balance between multiple interfaces that are members of the same bond.

The switch distributes egress traffic through a bond to a slave based on a packet hash calculation, providing load balancing over the slaves; the switch distributes conversation flows over all available slaves to load balance the total traffic. Traffic for a single conversation flow always hashes to the same slave. In a failover event, the switch adjusts the hash calculation to steer traffic over available slaves.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash destination-ip</h>

Turns lag hashing on the destination IP address field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash destination-ip on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash destination-mac</h>

Turns lag hashing on the destination MAC address field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash destination-mac on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash destination-port</h>

Turns lag hashing on the destination port field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash destination-port on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash ether-type</h>

Turns lag hashing on the ether type field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash ether-type on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash gtp-teid</h>

Turns lag hashing on the GTP TEID field on or off. GTP carries mobile data within the core of the mobile operator’s network. Traffic in the 5G Mobility core cluster, from cell sites to compute nodes, have the same source and destination IP address. The only way to identify individual flows is with the GTP TEID. Enabling GTP hashing adds the TEID as a hash parameter and helps the Cumulus Linux switches in the network to distribute mobile data traffic evenly across ECMP routes.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash gtp-teid on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash ip-protocol</h>

Turns lag hashing on the IP protocol field on or off. For IP traffic, the switch uses IP header source and destination fields in the hash calculation. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash ip-protocol on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash source-ip</h>

Turns lag hashing on the source IP address field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash source-ip on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash source-mac</h>

Turns lag hashing on the source MAC address field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash source-mac on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash source-port</h>

Turns lag hashing on the source port field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash source-port on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding lag-hash vlan</h>

Turns lag hashing on the VLAN ID field on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system forwarding lag-hash vlan on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding profile</h>

Configures the forwarding resource profile: `default`, `l2-heavy`, `l2-heavy-1`, `l2-heavy-3`, `v4-lpm-heavy`, `v4-lpm-heavy-1`, `v6-lpm-heavy`, `v6-lpm-heavy-1`, `ipmc-heavy`, `ipmc-max`, or `lpm-balanced`.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system forwarding profile l2-heavy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding programming</h>

Configures forwarding programming logging.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding programming log-level</h>

Configures the forwarding programming log level: `debug`, `info`, `critical`, `warning`, or `error`. The default log level is `info`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system forwarding programming log-level error
```
