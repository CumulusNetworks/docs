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
nv show system control-plane punt-classifier
nv show system control-plane punt-classifier <rule-id>
nv show system control-plane punt-classifier <rule-id> counters
nv show system ztp wall-messages
nv show platform transceiver <transceiver-id> firmware
nv show platform transceiver <transceiver-id> firmware files
nv show platform transceiver <transceiver-id> firmware files <file>
nv show router allow-reserved-range
nv show system forwarding resilient-hash
nv show system security spdm
nv show system security spdm <component-id>
nv show system security spdm <component-id> certificate
nv show system security spdm <component-id> measurements
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set system control-plane punt-classifier <rule-id> match
nv set system control-plane punt-classifier <rule-id> action
nv set system ztp wall-messages
nv set platform firmware <platform-component-id> auto-update 
nv set platform firmware <platform-component-id> fw-source
nv set router allow-reserved-range class-e
nv set router bfd offload-mode kernel
nv set system forwarding resilient-hash active-timer
nv set system forwarding resilient-hash bucket-size
nv set system forwarding resilient-hash state
nv set vrf <vrf-id> router bgp address-family <address-family> route-export to-evpn skip-evpn-imported
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> connection v6-lla
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action clear interface <interface> ipv6 neighbor-discovery prefix <prefix>
nv action clear system control-plane punt-classifier <rule-id> counters
nv action delete platform firmware <platform-component-id> files <file> 
nv action install platform firmware <platform-component-id> files <file> [force] [skip-reboot] [skip-version-check]
nv action install platform transceiver <id> firmware files <file>
nv action generate system security spdm <component-id> nonce <nonce>
nv action reboot system mode power-off
nv action rename platform firmware <platform-component-id> files <file> <str>
nv action upload platform firmware <platform-component-id> files <file> <url> 
```

{{< /tab >}}
{{< /tabs >}}

## Changed NVUE Commands

| Cumulus Linux 5.19               | Cumulus Linux 5.18 |
| -------------------------------- | --------------------------- |
| `nv set router bfd offload-mode` | `nv set router bfd offload` |

