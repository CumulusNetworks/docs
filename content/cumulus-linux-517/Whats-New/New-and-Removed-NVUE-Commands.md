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
nv show interface <interface-id> qos buffer shared-headroom-pool
nv show interface debounce-counters
nv show qos advance-buffer-config <profile-id> shared-headroom
nv show system dot1x pre-auth
nv show system dot1x pre-auth allow-protocol
nv show system lldp tlv profile
nv show system lldp tlv profile <lldp-profile-name-id>
nv show system lldp tlv profile <lldp-profile-name-id> egress-policy
nv show system lldp tlv profile <lldp-profile-name-id> egress-policy <tlv-name-id>
nv show system lldp tlv profile <lldp-profile-name-id> ingress-policy
nv show system lldp tlv profile <lldp-profile-name-id> ingress-policy <tlv-name-id>
nv show system telemetry export ipfix
nv show system telemetry interface-stats class debounce
nv show system telemetry stats-group <stats-group-id> interface-stats class debounce
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability export-lldp
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability export-lldp

```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface-id> dot1x tx-identity-request (enabled|disabled)
nv set interface <interface-id> link debounce down
nv set interface <interface-id> link debounce up
nv set qos advance-buffer-config <profile-id> shared-headroom exclusive-headroom-per-pg
nv set qos advance-buffer-config <profile-id> shared-headroom required-headroom-per-pg
nv set qos link-pause <profile-id> small-packet-probability
nv set system dot1x pre-auth allow-protocol lldp
nv set system dot1x tx-identity-request max-retries
nv set system lldp tlv egress-policy <tlv-name-id>
nv set system lldp tlv ingress-policy <tlv-name-id>
nv set system lldp tlv ingress-policy <tlv-name-id> state (enabled|disabled)
nv set system lldp tlv profile <lldp-profile-name-id>
nv set system lldp tlv profile <lldp-profile-name-id> description <value>
nv set system lldp tlv profile <lldp-profile-name-id> egress-policy <tlv-name-id>
nv set system lldp tlv profile <lldp-profile-name-id> ingress-policy <tlv-name-id>
nv set system security alerts audit-failure (enabled|disabled)
nv set system telemetry exclude-list <value>
nv set system telemetry include-list <value>
nv set system telemetry interface-stats class debounce sample-interval (10-86400)
nv set system telemetry interface-stats class debounce state (enabled|disabled)
nv set system telemetry metric-list <metric-list-id>
nv set system telemetry metric-list <metric-list-id> description <value>
nv set system telemetry metric-list <metric-list-id> metric <metric-id>
nv set system telemetry stats-group <stats-group-id> exclude-list <value>
nv set system telemetry stats-group <stats-group-id> include-list <value>
nv set system telemetry stats-group <stats-group-id> interface-stats class debounce sample-interval (10-86400)
nv set system telemetry stats-group <stats-group-id> interface-stats class debounce state (enabled|disabled)
nv set vrf <vrf-id> router bgp address-family ipv4-unreachability export-lldp state (enabled|disabled)
nv set vrf <vrf-id> router bgp address-family ipv6-unreachability export-lldp state (enabled|disabled)
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv4-unreachability state (enabled|disabled)
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn advertise ipv6-unreachability state (enabled|disabled)
nv set vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id> peer-group <generic-name>
```

{{< /tab >}}
{{< tab "nv action ">}}

```
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

Cumulus Linux 5.17 no longer supports the following NVUE commands:

```

```
