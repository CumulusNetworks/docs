---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.11 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.11, see the {{<link title="Cumulus Linux 5.11 Release Notes" text="Cumulus Linux 5.11 Release Notes">}}.
- To upgrade to Cumulus Linux 5.11, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->

## What's New in Cumulus Linux 5.11

### Platforms

- NVIDIA SN2201M (100G Spectrum 1)
- NVIDIA SN5400 switch includes P2C Forward Airflow support

### New Features and Enhancements

- The NVIDIA SN5400 switch supports {{<link url="Synchronous-Ethernet-SyncE" text="syncE">}} and {{<link url="Precision-Time-Protocol-PTP/#noise-transfer-servo" text="ITU-T">}}
- {{<link url="Pulse-Per-Second-PPS" text="PPS on the NVIDIA SN5400 switch">}} is now generally available.
- {{<link url="Factory-Reset" text="Factory Reset">}}
- {{<link url="Forwarding-Table-Size-and-Profiles/#spectrum-1" text="ecmp-nh-heavy forwarding profile">}} for Spectrum 1 switches
- {{<link url="RADIUS-AAA/#radius-user-command-accounting" text="RADIUS user command accounting">}}
- {{<link url="Upgrading-Cumulus-Linux/#upgrade-cumulus-linux" text="Optimized image upgrade commands">}} (available for future upgrades)
- {{<link url="Open-Telemetry-Export" text="New OTLP Statistics and Export">}}
- {{<link url="ASIC-Monitoring/#interface-packet-and-buffer-statistics" text="Interface packet and buffer statistics collection">}}
- NVUE
  - {{<link url="DHCP-Snooping" text="DHCP snooping commands">}}
  - {{<link url="LDAP-Authentication-and-Authorization" text="LDAP authentication and authorization commands">}}
  - {{<link url="Link-Layer-Discovery-Protocol/#enable-or-disable-lldp" text="Enable and disable LLDP commands">}}
  - {{<link url="Resource-Diagnostics/#enable-or-disable-lldp" text="Show ASIC resources commands">}} (`cl-resource-query` equivalent)
  - {{<link url="Monitoring-System-Statistics-and-Network-Traffic-with-sFlow" text="sFlow commands">}}
  - {{<link url="DHCP-Servers/#assign-a-port-based-ip-address" text="IPv6 command to assign a port-based DHCP server address">}}
  - {{<link url="Zero-Touch-Provisioning-ZTP/#manually-run-ztp" text="Enable ZTP and run ZTP script commands">}}
  - {{<link url="Interface-Configuration-and-Management/#port-ranges" text="Additional port range support for breakout ports and subinterfaces">}}
  - {{<link url="Interface-Configuration-and-Management/#troubleshooting" text="nv show interface <interface>">}} commands now show the date and time the operational state of an interface changes and number of carrier transitions
  - {{<link url="NVUE-CLI/#show-switch-configuration" text="nv config show --all command">}} to show applied configuration on the switch and include all default options
  - {{<link url="Services-and-Daemons-in-Cumulus-Linux/#limit-resources-for-services" text="Commands to limit resources (memory and CPU usage) for Cumulus Linux services">}}.
  - {{<link url="Optional-BGP-Configuration/#bgp-community-lists" text="Commands to configure BGP large community lists">}}
  - {{<link url="Route-Filtering-and-Redistribution/#match-source-protocol" text="Command to match BGP as the source protocol in a route map">}}
  - {{<link url="Switch-Port-Attributes/#interface-settings" text="nv show interface --view command includes additional filtering options">}}: `svi`, `vrf`, `bonds`, `bond-members`, and `down`
  - {{<link url="FRRouting/#show-routes-in-the-routing-table" text="Commands to show the number of routes in the routing table">}}
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#show-transceiver-information" text="Commands to show optical information for transceivers">}}
  - {{<link url="Troubleshoot-Layer-1/#show-layer-1-information" text="l1-show command equivalent">}}
  - {{<link url="Troubleshooting-BGP" text="BGP">}} and {{<link url="Troubleshooting-EVPN" text="EVPN">}} command changes and output cleanup
  - {{< expand "Changed NVUE Commands" >}}
| New Commands | Previous Commands |
| ----------- | ----------------|
| `nv set system snmp-server`<br>`nv unset system snmp-server` | `nv set service snmp-server`<br>`nv unset service snmp-server` |
| `nv set system snmp-server state enable`<br>`nv set system snmp-server state disable`| `nv set service snmp-server enable on`<br>`nv set service snmp-server enable off`|
| `nv show system snmp-server` | `nv show service snmp-server`|
| `nv set qos advance-buffer-config <profile-id> ingress-service-pool <pool-id> <property> <value>` | `nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id> <property> <value>`|
| `nv set qos advance-buffer-config <profile-id> egress-service-pool <pool-id> <property> <value>` | `nv set qos advance-buffer-config <profile-id> egress-pool <pool-id> <property> <value> ` |
| `nv show qos advance-buffer-config <profile-id> ingress-service-pool` | `nv show qos advance-buffer-config default-global ingress-pool` |
| `nv show qos advance-buffer-config <profile-id> egress-service-pool` | `nv show qos advance-buffer-config default-global egress-pool` |
{{< /expand >}}
  - {{< expand "Removed NVUE Commands" >}}
| Removed Commands |
| --------------- |
|`nv show interface pluggable` (replaced with `nv show platform transceiver`) |
|`nv show interface <interface>` pluggable (replaced with `nv show platform transceiver <interface>`)|
|`nv show vrf <vrf-id> router bgp address-family <afi> loc-rib` (replaced with `nv show vrf <vrf-id> router bgp address-family <afi>> route`) |
| `nv set vrf <vrf-id> router rib ipv4 protocol bgp fib-filter` |
| `nv show vrf <vrf-id> router rib ipv6 protocol` |
| `nv show router nexthop rib <nhg-id> dependents` |
| `nv show router nexthop rib <nhg-id> depends` |
| `nv show router nexthop rib <nhg-id> resolved-via <resolved-via-id>` |
| `nv show router nexthop rib <nhg-id> resolved-via-backup <resolved-via-id>` |

{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show bridge domain <domain-id> dhcp-snoop
nv show bridge domain <domain-id> dhcp-snoop vlan
nv show bridge domain <domain-id> dhcp-snoop vlan <vid>
nv show bridge domain <domain-id> dhcp-snoop vlan <vid> trust
nv show bridge domain <domain-id> dhcp-snoop vlan <vid> trust <interface-id>
nv show bridge domain <domain-id> dhcp-snoop vlan <vid> bind
nv show bridge domain <domain-id> dhcp-snoop vlan <vid> bind <interface-id>
nv show bridge domain <domain-id> dhcp-snoop6
nv show bridge domain <domain-id> dhcp-snoop6 vlan
nv show bridge domain <domain-id> dhcp-snoop6 vlan <vid>
nv show bridge domain <domain-id> dhcp-snoop6 vlan <vid> trust
nv show bridge domain <domain-id> dhcp-snoop6 vlan <vid> trust <interface-id>
nv show bridge domain <domain-id> dhcp-snoop6 vlan <vid> bind
nv show bridge domain <domain-id> dhcp-snoop6 vlan <vid> bind <interface-id>
nv show interface bonds
nv show interface bond-members
nv show interface carrier-stats
nv show interface down
nv show interface svi
nv show interface vrf
nv show interface <interface-id> sflow
nv show interface <interface-id> transceiver 
nv show interface <interface-id> transceiver thresholds
nv show qos buffer descriptor-pool
nv show platform asic resource
nv show platform asic resource acl
nv show platform asic resource global
nv show platform transceiver
nv show platform transceiver <interface-id> 
nv show platform transceiver <interface-id> channel 
nv show platform transceiver <interface-id> channel <channel-id> 
nv show platform transceiver brief
nv show platform transceiver detail
nv show router policy large-community-list
nv show router policy large-community-list <list-id>
nv show router policy large-community-list <list-id> rule
nv show router policy large-community-list <list-id> rule <rule-id>
nv show router policy large-community-list <list-id> rule <rule-id> large-community
nv show router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>
nv show router policy route-map <route-map-id> rule <rule-id> set large-community
nv show router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>
nv show service control
nv show service control <service-name-id>
nv show service control <service-name-id> resource-limit
nv show system aaa ldap
nv show system aaa ldap hostname
nv show system aaa ldap hostname <hostname-id>
nv show system aaa ldap ssl
nv show system aaa radius accounting
nv show system image
nv show system image files
nv show system image files <image>
nv show system sflow
nv show system sflow collector
nv show system sflow collector <collector-ip>
nv show system sflow sampling-rate
nv show system sflow agent
nv show system sflow policer
nv show system sflow dropmon
nv show system sflow dropmon <drop-type>
nv show interface swp1 telemetry label
nv show interface swp1 telemetry label <label-id>
nv show system telemetry label
nv show system telemetry label <label-id>
nv show system telemetry snapshot
nv show system telemetry snapshot port-group
nv show system telemetry snapshot port-group <port-group-id>
nv show system telemetry snapshot port-group <port-group-id> snapshot-file
nv show system telemetry snapshot port-group <port-group-id> threshold
nv show system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id>
nv show system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action
nv show system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action log
nv show system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action collect
nv show system telemetry snapshot port-group <port-group-id> stats-type
nv show system telemetry snapshot port-group <port-group-id> stats
nv show system telemetry snapshot port-group <port-group-id> stats buffer
nv show system telemetry snapshot port-group <port-group-id> stats buffer pool
nv show system telemetry snapshot port-group <port-group-id> stats buffer pool <buffer-pool-id>
nv show system telemetry snapshot port-group <port-group-id> stats interface
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id>
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet good
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet good tx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet good rx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet discard
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet discard tx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet discard rx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet discard general
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet all
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet all tx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet all rx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet tc
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet tc <if-tc-id>
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet tc <if-tc-id> tx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet pg
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet pg <if-pg-id>
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet pg <if-pg-id> tx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> packet pg <if-pg-id> rx
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> buffer
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> buffer tc
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> buffer tc <if-tc-id>
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> buffer pg
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> buffer pg <if-pg-id>
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> buffer ingress-port
nv show system telemetry snapshot port-group <port-group-id> stats interface <intf-id> buffer ingress-port <buffer-pool-id>
nv show system ztp
nv show system ztp script
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id> large-community
nv show vrf <vrf-id> router rib <address-family> fib-filter
nv show vrf <vrf-id> router rib <address-family> fib-filter protocol
nv show vrf <vrf-id> router rib <address-family> fib-filter protocol <import-protocol-id>
nv show vrf <vrf-id> router bgp address-family <address-family> route
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id>
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> nexthop <nexthop-id>
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> peer
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> flags
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> bestpath
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> aspath
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp address-family <address-family> route <route-id> path <path-id> ext-community
nv show vrf <vrf-id> router bgp address-family <address-family> route-count
nv show vrf <vrf-id> router rib <address-family> route-count
nv show vrf <vrf-id> router rib <address-family> route-count <prefix>
nv show vrf <vrf-id> router rib <address-family> route-count protocol
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry>
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry> flags
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry> via-entry
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry> via-entry <via-entry-id>
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry> via-entry <via-entry-id> flags
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry> via-entry <via-entry-id> label
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry> via-entry <via-entry-id> resolved-via-entry
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry> via-entry <via-entry-id> resolved-via-entry <resolved-via-entry-id>
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address <nht-ip-id> resolved-via <nht-resolved-id>
nv show vrf <vrf-id> router nexthop-tracking <afi> ip-address <nht-ip-id> protocol <protocol-id>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set bridge domain <domain-id> dhcp-snoop vlan <vid>
nv set bridge domain <domain-id> dhcp-snoop vlan <vid> trust <interface-id>
nv set bridge domain <domain-id> dhcp-snoop6 vlan <vid>
nv set bridge domain <domain-id> dhcp-snoop6 vlan <vid> trust <interface-id>
nv set interface <interface-id> lldp state
nv set interface <interface-id> sflow state
nv set interface <interface-id> sflow sample-rate <rate>
nv set interface <interface-id> telemetry label <label-id>
nv set interface <interface-id> telemetry label <label-id> description <value>
nv set router policy large-community-list <list-id>
nv set router policy large-community-list <list-id> rule <rule-id>
nv set router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>
nv set router policy large-community-list <list-id> rule <rule-id> action
nv set router policy route-map <route-map-id> rule <rule-id> match large-community-list
nv set router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>
nv set router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list 
nv set service control <service-name-id>
nv set service control <service-name-id> resource-limit memory <size>
nv set service control <service-name-id> resource-limit cpu (percent)
nv set service dhcp-server6 default static <server-id> ip-address <ip-address>
nv set service dhcp-server6 default static <server-id> ifname <interface-id>
nv set service lldp state
nv set system aaa radius accounting state
nv set system aaa ldap base-dn <value>
nv set system aaa ldap bind-dn <value>
nv set system aaa ldap hostname <hostname-id>
nv set system aaa ldap hostname <hostname-id> priority
nv set system aaa ldap port
nv set system aaa ldap referrals <value>
nv set system aaa ldap secret <nslcd-string>
nv set system aaa ldap ssl ca-list
nv set system aaa ldap ssl crl-check <value>
nv set system aaa ldap ssl mode
nv set system aaa ldap ssl port
nv set system aaa ldap ssl tls-ciphers
nv set system aaa ldap timeout-bind
nv set system aaa ldap timeout-search
nv set system aaa ldap version
nv set system aaa ldap vrf <value>
nv set system sflow collector <collector-ip>
nv set system sflow collector <collector-ip> port
nv set system sflow collector <collector-ip> interface <interface-name>
nv set system sflow sampling-rate default
nv set system sflow sampling-rate speed-100m
nv set system sflow sampling-rate speed-1g
nv set system sflow sampling-rate speed-10g
nv set system sflow sampling-rate speed-25g
nv set system sflow sampling-rate speed-40g
nv set system sflow sampling-rate speed-50g
nv set system sflow sampling-rate speed-100g
nv set system sflow sampling-rate speed-200g
nv set system sflow sampling-rate speed-400g
nv set system sflow sampling-rate speed-800g
nv set system sflow agent ip <ipv4-prefix>
nv set system sflow agent interface <interface-name>
nv set system sflow dropmon <drop-type>
nv set system sflow poll-interval
nv set system sflow state
nv set system telemetry label <label-id>
nv set system telemetry label <label-id> description <value>
nv set system telemetry snapshot port-group <port-group-id>
nv set system telemetry snapshot port-group <port-group-id> snapshot-file name <value>
nv set system telemetry snapshot port-group <port-group-id> snapshot-file count
nv set system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id>
nv set system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action log
nv set system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action collect port-group <value>
nv set system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> value
nv set system telemetry snapshot port-group <port-group-id> stats-type
nv set system telemetry snapshot port-group <port-group-id> interface <interface>
nv set system telemetry snapshot port-group <port-group-id> timer-interval
nv set vrf <vrf> router bgp address-family <address-family> advertise-origin
nv set vrf <vrf> router bgp address-family <address-family> nhg-per-origin
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset bridge domain <domain-id> dhcp-snoop
nv unset bridge domain <domain-id> dhcp-snoop vlan
nv unset bridge domain <domain-id> dhcp-snoop vlan <vid>
nv unset bridge domain <domain-id> dhcp-snoop vlan <vid> trust
nv unset bridge domain <domain-id> dhcp-snoop vlan <vid> trust <interface-id>
nv unset bridge domain <domain-id> dhcp-snoop6
nv unset bridge domain <domain-id> dhcp-snoop6 vlan
nv unset bridge domain <domain-id> dhcp-snoop6 vlan <vid>
nv unset bridge domain <domain-id> dhcp-snoop6 vlan <vid> trust
nv unset bridge domain <domain-id> dhcp-snoop6 vlan <vid> trust <interface-id>
nv unset interface <interface-id> lldp state
nv unset interface <interface-id> sflow
nv unset interface <interface-id> sflow sample-rate
nv unset interface <interface-id> sflow state
nv unset interface <interface-id> telemetry label
nv unset interface <interface-id> telemetry label <label-id>
nv unset interface <interface-id> telemetry label <label-id> description
nv unset router policy large-community-list
nv unset router policy large-community-list <list-id>
nv unset router policy large-community-list <list-id> rule
nv unset router policy large-community-list <list-id> rule <rule-id>
nv unset router policy large-community-list <list-id> rule <rule-id> large-community
nv unset router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>
nv unset router policy large-community-list <list-id> rule <rule-id> action
nv unset router policy route-map <route-map-id> rule <rule-id> match large-community-list
nv unset router policy route-map <route-map-id> rule <rule-id> set large-community
nv unset router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>
nv unset router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list
nv unset service control
nv unset service control <service-name-id>
nv unset service control <service-name-id> resource-limit
nv unset service control <service-name-id> resource-limit memory
nv unset service control <service-name-id> resource-limit cpu
nv unset service dhcp-server6 default static <server-id> ip-address <ip-address>
nv unset service dhcp-server6 default static <server-id> ifname <interface-id>
nv unset service lldp state
nv unset system aaa radius accounting
nv unset system aaa ldap base-dn
nv unset system aaa ldap bind-dn
nv unset system aaa ldap hostname <hostname-id>
nv unset system aaa ldap hostname <hostname-id> priority
nv unset system aaa ldap port
nv unset system aaa ldap referrals
nv unset system aaa ldap secret
nv unset system aaa ldap ssl ca-list
nv unset system aaa ldap ssl crl-check <value>
nv unset system aaa ldap ssl mode
nv unset system aaa ldap ssl port
nv unset system aaa ldap ssl tls-ciphers
nv unset system aaa ldap timeout-bind
nv unset system aaa ldap timeout-search
nv unset system aaa ldap version
nv unset system aaa ldap vrf
nv unset system sflow
nv unset system sflow collector
nv unset system sflow collector <collector-ip>
nv unset system sflow collector <collector-ip> port
nv unset system sflow collector <collector-ip> interface
nv unset system sflow sampling-rate
nv unset system sflow sampling-rate default
nv unset system sflow sampling-rate speed-100m
nv unset system sflow sampling-rate speed-1g
nv unset system sflow sampling-rate speed-10g
nv unset system sflow sampling-rate speed-25g
nv unset system sflow sampling-rate speed-40g
nv unset system sflow sampling-rate speed-50g
nv unset system sflow sampling-rate speed-100g
nv unset system sflow sampling-rate speed-200g
nv unset system sflow sampling-rate speed-400g
nv unset system sflow sampling-rate speed-800g
nv unset system sflow agent
nv unset system sflow agent ip
nv unset system sflow agent interface
nv unset system sflow policer
nv unset system sflow dropmon
nv unset system sflow dropmon <drop-type>
nv unset system sflow poll-interval
nv unset system sflow state
nv unset system telemetry label
nv unset system telemetry label <label-id>
nv unset system telemetry label <label-id> description
nv unset system telemetry snapshot
nv unset system telemetry snapshot port-group
nv unset system telemetry snapshot port-group <port-group-id>
nv unset system telemetry snapshot port-group <port-group-id> snapshot-file
nv unset system telemetry snapshot port-group <port-group-id> snapshot-file name
nv unset system telemetry snapshot port-group <port-group-id> snapshot-file count
nv unset system telemetry snapshot port-group <port-group-id> threshold
nv unset system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id>
nv unset system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action
nv unset system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action log
nv unset system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action collect
nv unset system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> action collect port-group
nv unset system telemetry snapshot port-group <port-group-id> threshold <threshold-stats-id> value
nv unset system telemetry snapshot port-group <port-group-id> stats-type
nv unset system telemetry snapshot port-group <port-group-id> interface
nv unset system telemetry snapshot port-group <port-group-id> timer-interval
nv unset vrf <vrf-id> router bgp address-family <address-family> advertise-origin
nv unset vrf <vr-id> router bgp address-family <address-family> nhg-per-origin
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action reset system factory-default
nv action reset system factory-default keep basic
nv action reset system factory-default keep all-config
nv action reset system factory-default keep only-files
nv action enable system ztp
nv action disable system ztp
nv action run system ztp
nv action abort system ztp
nv action fetch system image
nv action install system image files <image>
nv action upload system image files <image> <remote-url-upload>
```

{{< /tab >}}
{{< tab "nv config ">}}

```
nv config show --all
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

{{%notice warning%}}
To align with a long-term vision of a common interface between Cumulus Linux, Nvidia OS (NVOS), and Host-Based Networking, certain NVUE commands in Cumulus Linux 5.11 have changed. Before you upgrade to 5.11, review the list of changed and removed NVUE commands above and be sure to make any necessary changes to your automation.
{{%/notice%}}

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.11.

### DHCP Lease with the host-name Option

When a Cumulus Linux switch with NVUE enabled receives a DHCP lease containing the host-name option, it ignores the received hostname and does not apply it. For details, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Hostname-Option-Received-From-DHCP-Ignored" >}}).

### NVUE Commands After Upgrade

Cumulus Linux 5.11 includes the NVUE object model. After you upgrade to Cumulus Linux 5.11, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.
