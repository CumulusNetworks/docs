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

{{< tabs "TabID49 ">}}
{{< tab "nv show ">}}

```
nv show bridge domain <domain-id> arp-inspection
nv show bridge domain <domain-id> arp-inspection vlan
nv show bridge domain <domain-id> arp-inspection vlan <vid>
nv show bridge domain <domain-id> arp-inspection vlan <vid> interface
nv show bridge domain <domain-id> arp-inspection vlan <vid> interface <interface-id>
nv show bridge domain <domain-id> arp-inspection vlan <vid> static-binding
nv show bridge domain <domain-id> arp-inspection vlan <vid> static-binding <arp-inspection-static-binding-id>
nv show evpn l3vxi
nv show interface --view ber
nv show interface --view dom
nv show interface link-tracking
nv show interface <interface-id> link-tracking
nv show platform inventory BMC
nv show platform firmware BMC
nv show platform firmware BMC files
nv show platform environment leakage
nv show system aaa radius server <server> counters
nv show system config backup
nv show system do-spx
nv show system do-spx active-profile
nv show system do-spx profile
nv show system do-spx profile <profile-id>
nv show system do-spx profile <profile-id> uplink
nv show system do-spx profile <profile-id> uplink <interface-id>
nv show system do-spx profile <profile-id> downlink
nv show system do-spx profile <profile-id> downlink <interface-id>
nv show system do-spx profile <profile-id> otlp-destination
nv show system do-spx profile <profile-id> otlp-destination <destination-id>
nv show system image
nv show system image onie
nv show system link-tracking
nv show system link-tracking group
nv show system link-tracking group <group-id>
nv show system link-tracking group <group-id> watch-interface
nv show system link-tracking group <group-id> watch-interface <interface-id>
nv show system packages archive
nv show system packages archive <id>
nv show system wjh channel <channel-id> buffer-threshold
nv show system wjh channel <channel-id> buffer-threshold latency
nv show system wjh channel <channel-id> buffer-threshold latency tc
nv show system wjh channel <channel-id> buffer-threshold latency tc <wjh-tc-id>
nv show system wjh channel <channel-id> buffer-threshold latency tc <wjh-tc-id> interface
nv show system wjh channel <channel-id> buffer-threshold latency tc <wjh-tc-id> interface <wjh-interface-id>
nv show system wjh channel <channel-id> buffer-threshold congestion
nv show system wjh channel <channel-id> buffer-threshold congestion tc
nv show system wjh channel <channel-id> buffer-threshold congestion tc <wjh-tc-id>
nv show system wjh channel <channel-id> buffer-threshold congestion tc <wjh-tc-id> interface
nv show system wjh channel <channel-id> buffer-threshold congestion tc <wjh-tc-id> interface <wjh-interface-id>
nv show system wjh channel <channel-id> drop-filter
nv show system wjh channel <channel-id> drop-filter <filter-id>
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id>
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> drop-reason
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> drop-reason <drop-filter-drop-reason-id>
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> severity
nv show system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> severity <drop-filter-severity-id>
nv show system wjh channel <channel-id> drop-filter <filter-id> ip
nv show system wjh channel <channel-id> drop-filter <filter-id> ip <ip-address-id>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set bridge default-vlan <vlan-id>
nv set bridge domain <domain-id> arp-inspection vlan <vid>
nv set bridge domain <domain-id> arp-inspection vlan <vid> interface <interface-id>
nv set bridge domain <domain-id> arp-inspection vlan <vid> static-binding <arp-inspection-static-binding-id>
nv set bridge domain <domain-id> arp-inspection vlan <vid> static-binding <arp-inspection-static-binding-id> mac <mac>
nv set bridge domain <domain-id> arp-inspection vlan <vid> static-binding <arp-inspection-static-binding-id> ip <ipv4>
nv set bridge domain <domain-id> arp-inspection vlan <vid> static-binding <arp-inspection-static-binding-id> port <interface-name>
nv set bridge domain <domain-id> arp-inspection vlan <vid> state (enabled|disabled)
nv set evpn l3vxi state
nv set interface <interface-id> link-tracking group
nv set interface <interface-id> security ip-source-guard
nv set maintenance unit system mode
nv set system aaa radius nas-ip-address <ipv4-address>
nv set system aaa radius nas-ipv6-address <ipv6-address>
nv set system aaa radius nas-identifier <identifier>
nv set system config backup state
nv set system do-spx profile <profile-id>
nv set system do-spx profile <profile-id> uplink <interface-id> breakout
nv set system do-spx profile <profile-id> downlink <interface-id> breakout
nv set system do-spx profile <profile-id> otlp-destination <destination-id>
nv set system do-spx profile <profile-id> otlp-destination <destination-id> otlp-port
nv set system link-tracking group <group-id>
nv set system link-tracking group <group-id> watch-interface <interface-id>
nv set system link-tracking group <group-id> min-links
nv set system link-tracking group <group-id> state-change-action
nv set system link-tracking state
nv set system security password-hardening min-char-diff
nv set system telemetry dot1x-stats class server-metrics state
nv set system telemetry platform-stats class asic-resource state
nv set system telemetry platform-stats class asic-resource sample-interval
nv set system wjh channel buffer aggregate-cache-size
nv set system wjh channel buffer polling-interval
nv set system wjh channel <channel-id> buffer-threshold latency tc <wjh-tc-id> interface <wjh-interface-id> high 
nv set system wjh channel <channel-id> buffer-threshold congestion tc <wjh-tc-id> interface <wjh-interface-id> high
nv set interface <interface-id> telemetry congestion-event egress-buffer traffic-class <intf-tc-id> buffer-threshold
nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> drop-reason <drop-filter-drop-reason-id>
nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> severity <drop-filter-severity-id>
nv set system wjh channel <channel-id> drop-filter <filter-id> ip
nv set vrf <vfr-id> router bgp plane-id
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action activate system do-spx profile <profile-id>
nv action activate system image onie
nv action boot-next system image onie install
nv action boot-next system image onie rescue
nv action boot-next system image onie uninstall
nv action cancel system image onie
nv action clear interface <interface-id> link-tracking protodown
nv action clear platform asic <asic-id> resource
nv action clear system aaa radius counters
nv action clear vrf <vrf-id> router rib ipv4 unreachable-prefixes <ipv4-prefix>
nv action clear vrf <vrf-id> router rib ipv6 unreachable-prefixes <ipv6-prefix>
nv action delete system packages archive <id>
nv action export system wjh packet-buffer <file-name>
nv action fetch system packages archive <path>
nv action install system image onie <path> [activate reboot] 
nv action install system image onie <path> ztp <script> [activate reboot]
nv action install system image onie <path> startup-config <file-name> [activate reboot]
nv action install system image onie ftp:<path> activate reboot
nv action install system packages archive <id>
nv action restore system config backup <path>
nv action uninstall system packages archive <archive-id>
```

{{< /tab >}}
{{< tab "nv config ">}}

```
nv config lookup "<search-path>"
```

{{< /tab >}}
{{< /tabs >}}

## Removed NVUE Commands

```
nv set system docker state
nv show system docker state
```
