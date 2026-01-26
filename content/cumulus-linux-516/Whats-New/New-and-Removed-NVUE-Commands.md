---
title: New and Removed NVUE Commands
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.16"
toc: 1
---
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

## New NVUE Commands

The following NVUE commands are new in Cumulus Linux 5.16.

{{< tabs "TabID49 ">}}
{{< tab "nv show ">}}

```
nv show system dot1x tx-identity-request
nv show system security fips
nv show system tech-support auto-generation
nv show vrf <vrf-id> router bgp address-family <address-family> conditional-disaggregation
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability route
nv show vrf <vrf-id> router bgp address-family ipv6-unreachability route-count
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability route
nv show vrf <vrf-id> router bgp address-family ipv4-unreachability route-count
nv show vrf <vrf-id> router fib
nv show vrf <vrf-id> router fib ipv4
nv show vrf <vrf-id> router fib ipv6
nv show vrf <vrf-id> router fib ipv4 route <route-id>
nv show vrf <vrf-id> router fib ipv6 route <route-id>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set acl <acl-id> rule <rule-id> match inner-ip dscp
nv set acl <acl-id> rule <rule-id> match inner-ip source-ip
nv set acl <acl-id> rule <rule-id> match inner-ip dest-ip
nv set acl <acl-id> rule <rule-id> match inner-ip protocol
nv set acl <acl-id> rule <rule-id> match inner-ip udp source-port
nv set acl <acl-id> rule <rule-id> match inner-ip udp dest-port
nv set acl <acl-id> rule <rule-id> match offset <offset> value
nv set acl <acl-id> rule <rule-id> match offset <offset> mask
nv set acl <acl-id> rule <rule-id> match offset <offset> match-from start-of-packet 
nv set router bfd offload
nv set system dot1x ipv6-profile <profile-id> preserve-on-link-down
nv set system dot1x tx-identity-request state
nv set system dot1x tx-identity-request delay
nv set system dot1x tx-identity-request interval
nv set system global icmp ipv6 errors-extension ingress-interface
nv set system global icmp ipv4 errors-extension ingress-interface
nv set system log secured-logs state
nv set system security fips mode
nv set system security user <user-id> max-logins
nv set system security group <group-id> max-logins
nv set system tech-support auto-generation burst-duration
nv set system tech-support auto-generation burst-size
nv set system tech-support auto-generation state
nv set qos egress-shaper <profile-id> mode
nv set interface <interface-id> qos headroom lossy extra-threshold
nv set interface <interface-id> link tx-squelch
nv set vrf <vrf-id> router bgp address-family <address-family> conditional-disaggregation
nv set vrf <vrf-id> router bgp address-family ipv6-unreachability advertise-origin
nv set vrf <vrf-id> router bgp address-family ipv6-unreachability state
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability state
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability prefix-limits
maximum
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability prefix-limits reestablish-wait
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability prefix-limits warning-only
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability prefix-limits warning-threshold
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability aspath allow-my-asn occurrences  
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability aspath allow-my-asn origin
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability aspath allow-my-asn route-map
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability aspath allow-my-asn state
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability aspath private-as
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unreachability aspath replace-peer-as
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability state
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability prefix-limits
maximum
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability prefix-limits reestablish-wait
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability prefix-limits warning-only
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability prefix-limits warning-threshold
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability aspath allow-my-asn occurrences  
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability aspath allow-my-asn origin
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability aspath allow-my-asn route-map
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability aspath allow-my-asn state
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability aspath private-as
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unreachability aspath replace-peer-as
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability state
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability prefix-limits reestablish-wait
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability prefix-limits warning-only
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability prefix-limits warning-threshold
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability aspath allow-my-asn occurrences  
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability aspath allow-my-asn origin
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability aspath allow-my-asn route-map
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability aspath allow-my-asn state
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability aspath private-as
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unreachability aspath replace-peer-as
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability state
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability prefix-limits
maximum
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability prefix-limits reestablish-wait
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability prefix-limits warning-only
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability prefix-limits warning-threshold
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability aspath allow-my-asn occurrences  
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability aspath allow-my-asn origin
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability aspath allow-my-asn route-map
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability aspath allow-my-asn state
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability aspath private-as
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unreachability aspath replace-peer-as
nv set vrf <vrf-id> router bgp soo-source
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action traceroute system <destination-id> errors-extension do-not-fragment
nv action activate system tech-support auto-generation
nv clear system control-plane policer statistics
nv action clear system control-plane policer <policer-id> statistics
```

{{< /tab >}}
{{< /tabs >}}

<!-- REMOVED FROM 5.16
nv set system dot1x dynamic-vrf 
-->
## Removed NVUE Commands

Cumulus Linux 5.16 no longer supports the following NVUE commands:

```
nv set system telemetry stats-group <group-id> acl-stats class acl-set export stat
```
