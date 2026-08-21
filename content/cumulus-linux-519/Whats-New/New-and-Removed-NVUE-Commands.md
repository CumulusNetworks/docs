---
title: New and Removed NVUE Commands
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.19"
toc: 1
---
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

## New NVUE Commands

The following NVUE commands are new in Cumulus Linux 5.19.

{{< tabs "TabID15 ">}}
{{< tab "nv show ">}}

```
nv show system forwarding resilient-hash
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set system forwarding resilient-hash active-timer
nv set system forwarding resilient-hash bucket-size
nv set system forwarding resilient-hash state
nv set vrf <vrf-id> router bgp address-family <address-family> route-export to-evpn skip-evpn-imported
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> connection v6-lla
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action reboot system mode power-off
```

{{< /tab >}}
{{< tab "nv config ">}}

```

```

{{< /tab >}}
{{< /tabs >}}

## Removed NVUE Commands

```

```
