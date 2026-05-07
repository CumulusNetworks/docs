---
title: New and Removed NVUE Commands
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.17"
toc: 1
---
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

## New NVUE Commands

The following NVUE commands are new in Cumulus Linux 5.17.

{{< tabs "TabID49 ">}}
{{< tab "nv show ">}}

```
nv show interface <interface-id> counters link debounce
nv show interface <interface-id> link debounce
nv show interface debounce-counters
nv show interface <interface-id> qos buffer shared-headroom-pool
nv show qos advance-buffer-config <profile-id> shared-headroom
nv show system aaa user cumulus --privileged
nv show system dot1x pre-auth
nv show system dot1x pre-auth allow-protocol
nv show system lldp tlv profile
nv show system lldp tlv profile <lldp-profile-name-id>
nv show system lldp tlv profile <lldp-profile-name-id> egress-policy
nv show system lldp tlv profile <lldp-profile-name-id> egress-policy <tlv-name-id>
nv show system lldp tlv profile <lldp-profile-name-id> ingress-policy
nv show system lldp tlv profile <lldp-profile-name-id> ingress-policy <tlv-name-id>
nv show system security alerts
nv show system security secure-boot
nv show system telemetry export ipfix
nv show system telemetry interface-stats class debounce
nv show system telemetry stats-group <stats-group-id> interface-stats class debounce
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability export-lldp
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability export-lldp
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface-id> dot1x tx-identity-request max-retries
nv set interface <interface-id> link debounce down
nv set interface <interface-id> link debounce up
nv set interface <interface-id> qos shared-headroom-pool
nv set qos advance-buffer-config <profile-id> shared-headroom exclusive-headroom-per-pg
nv set qos advance-buffer-config <profile-id> shared-headroom oversubscription-ratio
nv set qos advance-buffer-config <profile-id> shared-headroom required-headroom-per-pg
nv set qos pfc <profile-id> small-packet-probability
nv set system dot1x pre-auth allow-protocol lldp ingress
nv set system dot1x pre-auth allow-protocol lldp egress
nv set system dot1x pre-auth allow-protocol lldp both
nv set system dot1x pre-auth allow-protocol lldp none
nv set system dot1x tx-identity-request max-retries
nv set system lldp tlv egress-policy dcbx-app-priority state
nv set system lldp tlv egress-policy dcbx-ets-config state
nv set system lldp tlv egress-policy dcbx-ets-recomm state
nv set system lldp tlv egress-policy dcbx-pfc state
nv set system lldp tlv egress-policy link-aggregation state
nv set system lldp tlv egress-policy management-address state
nv set system lldp tlv egress-policy mac-phy-config state
nv set system lldp tlv egress-policy max-frame-size state
nv set system lldp tlv egress-policy media-capabilities state
nv set system lldp tlv egress-policy system-capabilities state
nv set system lldp tlv egress-policy system-description state
nv set system lldp tlv egress-policy system-name state
nv set system lldp tlv egress-policy port-description state
nv set system lldp tlv egress-policy port-vlan-id state      
nv set system lldp tlv egress-policy unreachable-prefix state
nv set system lldp tlv egress-policy vlan-name state
nv set system lldp tlv egress-policy unreachable-prefix state state
nv set system lldp tlv ingress-policy dcbx-app-priority state
nv set system lldp tlv ingress-policy dcbx-ets-config state
nv set system lldp tlv ingress-policy dcbx-ets-recomm state
nv set system lldp tlv ingress-policy dcbx-pfc state
nv set system lldp tlv ingress-policy link-aggregation state
nv set system lldp tlv ingress-policy mac-phy-config state
nv set system lldp tlv ingress-policy max-frame-size state
nv set system lldp tlv ingress-policy management-address state
nv set system lldp tlv ingress-policy media-capabilities state
nv set system lldp tlv ingress-policy system-capabilities state
nv set system lldp tlv ingress-policy system-description state
nv set system lldp tlv ingress-policy system-name state
nv set system lldp tlv ingress-policy port-description state
nv set system lldp tlv ingress-policy port-vlan-id state         
nv set system lldp tlv ingress-policy unreachable-prefix state
nv set system lldp tlv ingress-policy vlan-name state
nv set system lldp tlv profile <lldp-profile-name-id> description
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy dcbx-app-priority state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy dcbx-ets-config state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy dcbx-ets-recomm state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy dcbx-pfc state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy mac-phy-config state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy management-address state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy max-frame-size state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy media-capabilities state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy link-aggregation state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy port-description state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy port-vlan-id state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy system-capabilities state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy system-description state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy system-name state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy unreachable-prefix state
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy vlan-name state
nv set interface <interface-id> lldp tlv profile <lldp-profile-name-id>
nv set system lldp tlv profile <lldp-profile-name-id> description
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy dcbx-app-priority state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy dcbx-ets-config state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy dcbx-ets-recomm state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy dcbx-pfc state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy link-aggregation state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy mac-phy-config state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy management-address state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy max-frame-size state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy media-capabilities state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy port-description state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy port-vlan-id state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy system-capabilities state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy system-description state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy system-name state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy unreachable-prefix state
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy vlan-name state
nv set system security alerts audit-failure
nv set system aaa tacacs authorization <privilege-level> all-commands
nv set system telemetry export ipfix destination
nv set system telemetry export ipfix max-ip-packet-size
nv set system telemetry export ipfix port
nv set system telemetry export ipfix template-metadata-interval
nv set system telemetry export ipfix vrf <vrf-id>
nv set system telemetry hft export ipfix state
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
nv set vrf <vrf-id> router bgp address-family ipv4-unreachability export-lldp state
nv set vrf <vrf-id> router bgp address-family ipv6-unreachability export-lldp state
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv4-unreachability state
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv6-unreachability state
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action change system security sed-password
nv action clear interface debounce-counters 
nv action clear interface <interface-id> counters link debounce
nv action delete system file-path <path>
nv action fetch system file-path <path> <uri> [file-permissions <value>] [vrf <vrf-name>]
```

{{< /tab >}}
{{< tab "nv config ">}}

```
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
