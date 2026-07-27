---
title: New and Removed NVUE Commands
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.18"
toc: 1
---
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

## New NVUE Commands

The following NVUE commands are new in Cumulus Linux 5.18.

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
nv show interface --view ber
nv show interface --view dom
nv show interface link-tracking
nv show interface <interface-id> link-tracking
nv show platform inventory
nv show platform inventory BMC
nv show platform firmware BMC
nv show platform firmware BMC files
nv show platform environment leakage
nv show system aaa radius server <server> counters
nv show system aaa user cumulus --privileged
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
nv show system dot1x pre-auth
nv show system dot1x pre-auth allow-protocol
nv show system image
nv show system image onie
nv show system link-tracking
nv show system link-tracking group
nv show system link-tracking group <group-id>
nv show system link-tracking group <group-id> watch-interface
nv show system link-tracking group <group-id> watch-interface <interface-id>
nv show system packages archive
nv show system packages archive <id>
nv show system security alerts
nv show system security secure-boot
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
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability export-lldp
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability route <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability route <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability route <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability route <route-id> path <path-id> reporters
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability route <route-id> path <path-id> reporters <reporter-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability export-lldp
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability route <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability route <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability route <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability route <route-id> path <path-id> reporters
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability route <route-id> path <path-id> reporters <reporter-id>
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn advertise
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv4-unreachability
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv6-unreachability
nv show vrf <vrf-id> router rib <afi> unreachable-prefixes
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
nv set interface <interface-id> dot1x tx-identity-request max-retries
nv set interface <interface-id> link apsu-mode
nv set interface <interface-id> link module-precoding
nv set interface <interface-id> lldp tlv profile <lldp-profile-name-id>
nv set interface <interface-id> link-tracking group
nv set interface <interface-id> qos shared-headroom-pool
nv set interface <interface-id> security ip-source-guard
nv set maintenance unit system mode
nv set qos advance-buffer-config <profile-id> shared-headroom exclusive-headroom-per-pg
nv set qos advance-buffer-config <profile-id> shared-headroom oversubscription-ratio
nv set qos advance-buffer-config <profile-id> shared-headroom required-headroom-per-pg
nv set qos pfc <profile-id> small-packet-probability
nv set system aaa radius nas-ip-address <ipv4-address>
nv set system aaa radius nas-ipv6-address <ipv6-address>
nv set system aaa radius nas-identifier <identifier>
nv set system aaa tacacs authorization <privilege-level> all-commands
nv set system config backup state
nv set system do-spx profile <profile-id>
nv set system do-spx profile <profile-id> uplink <interface-id>
nv set system do-spx profile <profile-id> uplink <interface-id> breakout
nv set system do-spx profile <profile-id> downlink <interface-id>
nv set system do-spx profile <profile-id> downlink <interface-id> breakout
nv set system do-spx profile <profile-id> otlp-destination <destination-id>
nv set system do-spx profile <profile-id> otlp-destination <destination-id> otlp-port
nv set system dot1x pre-auth allow-protocol lldp ingress
nv set system dot1x pre-auth allow-protocol lldp egress
nv set system dot1x pre-auth allow-protocol lldp both
nv set system dot1x pre-auth allow-protocol lldp none
nv set system dot1x tx-identity-request max-retries
nv set system link-tracking group <group-id>
nv set system link-tracking group <group-id> watch-interface <interface-id>
nv set system link-tracking group <group-id> min-links
nv set system link-tracking group <group-id> state-change-action
nv set system link-tracking state
nv set system lldp tlv egress-policy <tlv-type> state
nv set system lldp tlv ingress-policy <tlv-type> state
nv set system lldp tlv profile <lldp-profile-name-id> description
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy <tlv-type> state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy <tlv-type> state
nv set system lldp unreachable-prefix max-limit
nv set system security password-hardening min-char-diff
nv set system security alerts audit-failure
nv set system telemetry export ipfix destination
nv set system telemetry export ipfix max-ip-packet-size
nv set system telemetry export ipfix port
nv set system telemetry export ipfix template-metadata-interval
nv set system telemetry export ipfix vrf <vrf-id>
nv set system telemetry hft export ipfix state
nv set system telemetry hft export-type 
nv set system telemetry hft ingress-buffer priority-group <hft-priority-group-id>
nv set system telemetry hft switch-priority <hft-switch-priority-id>
nv set system telemetry exclude-list
nv set system telemetry include-list
nv set system telemetry interface-stats class debounce sample-interval
nv set system telemetry interface-stats class debounce state
nv set system telemetry metric-list <metric-list-id>
nv set system telemetry metric-list <metric-list-id> description
nv set system telemetry metric-list <metric-list-id> metric <metric-id>
nv set system telemetry stats-group <stats-group-id> exclude-list
nv set system telemetry stats-group <stats-group-id> include-list
nv set system telemetry stats-group <stats-group-id> interface-stats class debounce sample-interval
nv set system telemetry stats-group <stats-group-id> interface-stats class debounce state
nv set system wjh channel buffer aggregate-cache-size
nv set system wjh channel buffer polling-interval
nv set system wjh channel <channel-id> buffer-threshold latency tc <wjh-tc-id>
nv set system wjh channel <channel-id> buffer-threshold latency tc <wjh-tc-id> interface <wjh-interface-id>
nv set system wjh channel <channel-id> buffer-threshold latency tc <wjh-tc-id> interface <wjh-interface-id> high 
nv set system wjh channel <channel-id> buffer-threshold congestion tc <wjh-tc-id>
nv set system wjh channel <channel-id> buffer-threshold congestion tc <wjh-tc-id> interface <wjh-interface-id>
nv set system wjh channel <channel-id> buffer-threshold congestion tc <wjh-tc-id> interface <wjh-interface-id> high
nv set interface <interface-id> telemetry congestion-event egress-buffer traffic-class <intf-tc-id> buffer-threshold
nv set system wjh channel <channel-id> drop-filter <filter-id>
nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id>
nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> drop-reason <drop-filter-drop-reason-id>
nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <drop-filter-drop-type-id> severity <drop-filter-severity-id>
nv set system wjh channel <channel-id> drop-filter <filter-id> ip
nv set vrf <vrf-id> router bgp address-family ipv4-unreachability export-lldp state
nv set vrf <vrf-id> router bgp address-family ipv6-unreachability export-lldp state
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv4-unreachability state
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv6-unreachability state
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
nv action change system security sed-password
nv action clear interface debounce-counters 
nv action clear interface <interface-id> counters link debounce
nv action clear interface <interface-id> link-tracking protodown
nv action clear platform asic <asic-id> resource
nv action clear system aaa radius counters
nv action delete system file-path <path>
nv action delete system packages archive <id>
nv action export system wjh packet-buffer <file-name>
nv action fetch system file-path <path> <uri> [file-permissions <value>] [vrf <vrf-name>]
nv action fetch system packages archive <path>
nv action install system image onie <path> [activate reboot] 
nv action install system image onie <path> ztp <script> [activate reboot]
nv action install system image onie <path> startup-config <file-name> [activate reboot]
nv action install system image onie ftp:<path> activate reboot
nv action install system packages archive <id>
nv action restore system config backup <path>
```

{{< /tab >}}
{{< tab "nv config ">}}

```
nv config lookup "<search-path>"
nv config verify
nv config verify filename filename <nvue-file>
nv config verify revision revision <revision>
```

{{< /tab >}}
{{< /tabs >}}

## Removed NVUE Commands

```
nv set system docker state
nv show system docker state
```
