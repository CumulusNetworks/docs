---
title: WJH
author: Cumulus Networks
weight: 820

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh</h>

Provides commands to configure <span class="a-tooltip">[WJH](## "What Just Happened")</span> to provide real time visibility into network problems. You can diagnose network problems by looking at dropped packets.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\></h>

Configures a WJH channel where you want to monitor packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name.  |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> aggregate-cache-size</h>

Configures the cache size for the WJH channel. You can specify a value between 500 and 5000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name.  |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding aggregate-cache-size 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> buffer-threshold congestion tc \<tc-id\> interface \<interface-id\> high</h>

Configures the channel buffer congestion (the percentage of the buffer occupancy on the switch) for all traffic classes or a specific traffic class for an interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<tc-id>` | The traffic class. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding buffer-threshold congestion tc 3 interface all high 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> buffer-threshold latency tc \<tc-id\> interface \<interface-id\> high</h>

Configures the channel buffer packet latency (the time spent in the switch) for all traffic classes or a specific traffic class for an interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<tc-id>` | The traffic class. |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding buffer-threshold latency tc all interface swp1-3 high 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> drop-filter \<filter-id\> drop-type \<drop-filter-drop-type-id\> drop-reason \<drop-filter-drop-reason-id\></h>

Configures traffic drop filters to prevent drops from being monitored based on the reason for the drop.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<filter-id>` | The filter name. |
| `<drop-filter-drop-type-id>` | The drop type. |
| `<drop-filter-drop-reason-id>` | The drop reason. See table below.|

| Traffic Drop Type | Drop Reasons |
| ----------------- | ------------ |
| ACL |egress-cpu-port-acl<br> egress-tunnel-acl<br>ingress-router-acl<br>egress-port-acl<br>ingress-cpu-port-acl<br>ingress-tunnel-acl<br>egress-router-acl<br>ingress-port-acl<br>multi-points-acl |
| Buffer | packet-latency-threshold-crossed<br>tail-drop<br>port-tc-congestion-threshold-crossed<br>wred |
| l2 |dest-mac-is-reserved<br>source-mac-is-multicast<br>ingress-spanning-tree-filter<br>source-mac-is-zero<br>ingress-vlan-filtering<br>unicast-egress-port-list-is-empty<br>mlag-port-isolation<br>unicast-mac-table-action-discard<br>multicast-egress-port-list-is-empty<br>vlan-or-vni-lookup-failed<br>port-loopback-filter<br>vlan-tagging-mismatch<br>source-mac-equals-dest-mac |
| l3 | blackhole-arp<br>blackhole-route<br>checksum-or-ipver-or-ipv4-ihl-too-short<br>dest-ip-is-loopback-addr<br>egress-router-intf-is-disabled<br>ingress-router-intf-is-disabled<br>ipv4-dest-ip-is-link-local<br>ipv4-dest-ip-is-local-network<br>ipv4-routing-table-unicast-miss<br>ipv4-src-ip-is-limited-broadcast<br>ipv6-dest-in-multicast-scope-ffx0<br>ipv6-dest-in-multicast-scope-ffx1<br>ipv6-routing-table-unicast-miss<br>multicast-mac-mismatch<br>non-ip-packet<br>non-routable-pck<br>packet-size-is-larger-than-router-intf-mtu<br>packet-source-ip-cant-be-verified<br>router-interface-loopback<br>src-ip-equals-dest-ip<br>src-ip-is-in-class-e<br>src-ip-is-loopback-addr<br>src-ip-is-multicast<br>src-ip-is-unspecified<br>ttl-value-is-too-small<br>unicast-dest-ip-but-multicast-dest-mac<br>unresolved-neighbor |
| Tunnel |decapsulation-error<br>encapsulation-port-isolation<br>overlay-switch-src-mac-equals-dest-mac<br>overlay-switch-src-mac-equals-zero<br>overlay-switch-src-mac-is-multicast |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding drop-filter TUNNEL1 drop-type tunnel drop-reason overlay-switch-src-mac-equals-dest-mac
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> drop-filter \<filter-id\> drop-type \<drop-filter-drop-type-id\> severity <drop-filter-severity-id></h>

Configures traffic drop filters to prevent drops from being monitored based on severity level.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<filter-id>` | The filter name. |
| `<drop-filter-drop-type-id>` | The drop type. |
| `<drop-filter-severity-id` | The severity: `error`, `warning`, or `notice`. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding drop-filter SEVERITY drop-type l2 severity notice
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> drop-filter \<filter-id\> ip</h>

Configures traffic drop filters to prevent drops from being monitored based on IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |
| `<filter-id>` | The filter name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding drop-filter IP-DROPS ip 10.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> polling-interval</h>

Configures aggregation interval for the WJH channel. You can specify a value between 5 and 300 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |

### Version History

Introduced in Cumulus Linux 5.18.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding polling-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> trigger</h>

Configures the type of packet drops you want to monitor. You can monitor layer 1 (`l1`), layer 2 (`l2`), layer 3 (`l3`), or tunnel (`tunnel1`) related packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding trigger l3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh state</h>

Enables and disables the WJH service. The default value is `enabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh state enabled
```
