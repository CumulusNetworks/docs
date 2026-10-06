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
nv show interface <interface-id> ipv6 neighbor-discovery prefix-lifetime
nv show interface <interface-id> telemetry histogram microburst
nv show interface <interface-id> telemetry histogram microburst direction
nv show interface <interface-id> telemetry histogram microburst direction <if-direction-id>
nv show interface <interface-id> telemetry histogram microburst direction <if-direction-id> snapshot
nv show interface <interface-id> telemetry histogram microburst direction <if-direction-id> threshold
nv show interface <interface-id> transceiver compliance
nv show platform transceiver <transceiver-id> compliance
nv show platform transceiver <transceiver-id> firmware
nv show platform transceiver <transceiver-id> firmware files
nv show platform transceiver <transceiver-id> firmware files <file>
nv show qos pfc-watchdog rx-pause-duration
nv show qos pfc-watchdog transmit-queue-threshold
nv show qos pfc-watchdog tx-frames-threshold
nv show router allow-reserved-range
nv show router allow-reserved-range <allow-reserved-range-id>
nv show router resource-limit
nv show system aaa class <class-id> os-command
nv show system aaa class <class-id> os-command <os-command-id>
nv show system aaa radius authorization
nv show system aaa radius authorization <privilege-level-id>
nv show system control-plane punt-classifier
nv show system control-plane punt-classifier <rule-id>
nv show system control-plane punt-classifier <rule-id> counters
nv show system control-plane punt-classifier <rule-id> counters hardware
nv show system control-plane punt-classifier <rule-id> match
nv show system control-plane punt-classifier <rule-id> match no-route
nv show system forwarding resilient-hash
nv show system log ztp
nv show system log ztp messages
nv show system security spdm
nv show system security spdm <component-id>
nv show system security spdm <component-id> certificates
nv show system security spdm <component-id> measurements
nv show system telemetry control-plane-stats class
nv show system telemetry control-plane-stats class punt-classifier
nv show system telemetry histogram microburst
nv show system telemetry histogram microburst summary
nv show system telemetry histogram microburst threshold
nv show system telemetry histogram microburst top
nv show system telemetry histogram microburst top <microburst-top-count-id>
nv show system telemetry histogram microburst top <microburst-top-count-id> interface
nv show system telemetry radius-stats
nv show system telemetry radius-stats export
nv show system telemetry stats-group <stats-group-id> control-plane-stats class
nv show system telemetry stats-group <stats-group-id> control-plane-stats class punt-classifier
nv show system telemetry stats-group <stats-group-id> radius-stats
nv show system telemetry stats-group <stats-group-id> radius-stats export
nv show system telemetry stats-group <stats-group-id> wjh
nv show system telemetry stats-group <stats-group-id> wjh export
nv show system telemetry wjh
nv show system telemetry wjh channel
nv show system telemetry wjh channel <channel-id>
nv show system telemetry wjh export
nv show system ztp wall-messages
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface-id> ipv6 neighbor-discovery prefix-lifetime preferred
nv set interface <interface-id> ipv6 neighbor-discovery prefix-lifetime valid
nv set interface <interface-id> telemetry histogram microburst direction <if-direction-id>
nv set interface <interface-id> telemetry histogram microburst direction <if-direction-id> bin-min-boundary
nv set interface <interface-id> telemetry histogram microburst direction <if-direction-id> histogram-size
nv set interface <interface-id> telemetry histogram microburst direction <if-direction-id> sample-interval
nv set interface <interface-id> telemetry histogram microburst direction <if-direction-id> threshold score
nv set interface <interface-id> telemetry histogram microburst direction <if-direction-id> unit
nv set platform firmware <platform-component-id> auto-update
nv set platform firmware <platform-component-id> fw-source
nv set qos pfc-watchdog recovery-interval
nv set qos pfc-watchdog rx-pause-duration multiplier
nv set qos pfc-watchdog rx-pause-duration state
nv set qos pfc-watchdog rx-pause-threshold
nv set qos pfc-watchdog transmit-queue-threshold percent
nv set qos pfc-watchdog transmit-queue-threshold state
nv set qos pfc-watchdog tx-frames-threshold state
nv set qos pfc-watchdog tx-frames-threshold value
nv set router allow-reserved-range <allow-reserved-range-id>
nv set router bfd offload-mode
nv set router resource-limit max-file-descriptors
nv set system aaa class <class-id> os-command <os-command-id>
nv set system aaa class <class-id> os-command <os-command-id> command
nv set system aaa radius authorization <privilege-level-id>
nv set system aaa radius authorization <privilege-level-id> role
nv set system control-plane punt-classifier <rule-id>
nv set system control-plane punt-classifier <rule-id> action drop
nv set system control-plane punt-classifier <rule-id> match dscp
nv set system control-plane punt-classifier <rule-id> match no-route
nv set system control-plane punt-classifier <rule-id> match packet-type
nv set system control-plane punt-classifier <rule-id> match udp-dport
nv set system forwarding resilient-hash active-timer
nv set system forwarding resilient-hash bucket-size
nv set system forwarding resilient-hash max-unbalanced-timer
nv set system forwarding resilient-hash state
nv set system log ztp messages state
nv set system telemetry control-plane-stats class punt-classifier sample-interval
nv set system telemetry control-plane-stats class punt-classifier state
nv set system telemetry histogram microburst bin-min-boundary
nv set system telemetry histogram microburst histogram-size
nv set system telemetry histogram microburst sample-interval
nv set system telemetry histogram microburst threshold score
nv set system telemetry histogram microburst unit
nv set system telemetry radius-stats export state
nv set system telemetry radius-stats sample-interval
nv set system telemetry stats-group <stats-group-id> control-plane-stats class punt-classifier sample-interval
nv set system telemetry stats-group <stats-group-id> control-plane-stats class punt-classifier state
nv set system telemetry stats-group <stats-group-id> radius-stats export state
nv set system telemetry stats-group <stats-group-id> radius-stats sample-interval
nv set system telemetry stats-group <stats-group-id> wjh export state
nv set system telemetry stats-group <stats-group-id> wjh sample-interval
nv set system telemetry wjh channel <channel-id>
nv set system telemetry wjh export state
nv set system telemetry wjh sample-interval
nv set system ztp wall-messages
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn skip-evpn-imported
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn skip-evpn-imported
nv set vrf <vrf-id> router bgp allow-as-sets
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> connection
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action clear interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id>
nv action clear system control-plane punt-classifier <rule-id> counters
nv action clear system control-plane punt-classifier counters
nv action delete platform firmware <platform-component-id> files <file>
nv action generate system security spdm <component-id> <value>
nv action install platform transceiver <transceiver-id> firmware files <file>
nv action prune system packages archive
nv action reboot system mode power-off
nv action rename platform firmware <platform-component-id> files <file> <name>
nv action upload platform firmware <platform-component-id> files <file> <url>
```

{{< /tab >}}
{{< /tabs >}}

## Changed NVUE Commands

| Cumulus Linux 5.19 | Cumulus Linux 5.18 |
| ------------------ | ------------------ |
| `nv set router bfd offload-mode (control-plane, kernel, hardware)` | `nv set router bfd offload (enabled, disabled)` |
| `nv action reboot system mode (halt, cold, immediate, warm, fast, power-cycle, power-off)` | `nv action reboot system mode (halt, cold, immediate, warm, fast, power-cycle)` |
| `nv set interface <interface-id> link mac-address (<mac>, <mac-unicast>)` | `nv set interface <interface-id> link mac-address <mac>` |
| `nv set interface <interface-id> qos headroom lossy extra-threshold (256-1818368, 192-1236480)` | `nv set interface <interface-id> qos headroom lossy extra-threshold (192-1236480)` |
| `nv set router segment-routing static srv6-sid <sid> locator-name <generic-name>` | `nv set router segment-routing static srv6-sid <sid> locator-name <value>` |
| `nv set system dot1x ipv6-profile <profile-id> property <property-id> value (0-4294967295, <valid-ipv6-profile-property-value>)` | `nv set system dot1x ipv6-profile <profile-id> property <property-id> value (0-18446744073709551615, <valid-ipv6-profile-property-value>)` |

## Removed NVUE Commands

```
nv action power-cycle system
nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> severity <drop-filter-severity-id>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability policy inbound prefix-list
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability policy outbound prefix-list
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability policy inbound prefix-list
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability policy outbound prefix-list
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability policy inbound prefix-list
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability policy outbound prefix-list
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability policy inbound prefix-list
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability policy outbound prefix-list
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> severity
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> severity <drop-filter-severity-id>
```
