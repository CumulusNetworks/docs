---
title: NVUE Commands
author: NVIDIA
weight: 121
toc: 2
---
This section shows you how to list all the NVUE commands and see command descriptions.

## List All Commands

To see a list of all the NVUE `nv show`, `nv set`, `nv unset`, `nv action`, and `nv config` commands, run `nv list-commands`.

{{%notice note%}}
The following is only an example of the NVUE command list. To see the most up to date list of commands, run `nv list-commands` on your switch.
{{%/notice%}}

```
cumulus@leaf01:mgmt:~$ nv list-commands
nv show platform
nv show platform hardware
nv show platform hardware component
nv show platform hardware component <component-id>
nv show platform software
nv show platform software installed
nv show platform software installed <installed-id>
nv show platform capabilities
nv show platform environment
nv show platform environment fan
nv show platform environment fan <fan-id>
nv show platform environment psu
nv show platform environment psu <psu-id>
nv show platform environment led
nv show platform environment led <led-id>
nv show platform environment sensor
nv show platform environment sensor <sensor-id>
nv show action
nv show action <action-job-id>
nv show router
nv show router ptm
nv show router nexthop
nv show router nexthop group
nv show router nexthop group <nexthop-group-id>
nv show router nexthop group <nexthop-group-id> via
nv show router nexthop group <nexthop-group-id> via <via-id>
nv show router nexthop rib
nv show router nexthop rib <nhg-id>
nv show router nexthop rib <nhg-id> resolved-via
nv show router nexthop rib <nhg-id> resolved-via <resolved-via-id>
nv show router nexthop rib <nhg-id> resolved-via-backup
nv show router nexthop rib <nhg-id> resolved-via-backup <resolved-via-id>
nv show router nexthop rib <nhg-id> depends
nv show router nexthop rib <nhg-id> dependents
nv show router pbr
nv show router pbr map
nv show router pbr map <pbr-map-id>
nv show router pbr map <pbr-map-id> rule
nv show router pbr map <pbr-map-id> rule <rule-id>
nv show router pbr map <pbr-map-id> rule <rule-id> match
nv show router pbr map <pbr-map-id> rule <rule-id> action
nv show router pbr map <pbr-map-id> rule <rule-id> action nexthop-group
nv show router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>
nv show router policy
nv show router policy community-list
nv show router policy community-list <list-id>
nv show router policy community-list <list-id> rule
nv show router policy community-list <list-id> rule <rule-id>
nv show router policy community-list <list-id> rule <rule-id> community
nv show router policy community-list <list-id> rule <rule-id> community <community-id>
nv show router policy as-path-list
nv show router policy as-path-list <list-id>
nv show router policy as-path-list <list-id> rule
nv show router policy as-path-list <list-id> rule <rule-id>
nv show router policy ext-community-list
nv show router policy ext-community-list <list-id>
nv show router policy ext-community-list <list-id> rule
nv show router policy ext-community-list <list-id> rule <rule-id>
nv show router policy ext-community-list <list-id> rule <rule-id> ext-community
nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt
nv show router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id>
nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo
nv show router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id>
nv show router policy large-community-list
nv show router policy large-community-list <list-id>
nv show router policy large-community-list <list-id> rule
nv show router policy large-community-list <list-id> rule <rule-id>
nv show router policy large-community-list <list-id> rule <rule-id> large-community
nv show router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>
nv show router policy prefix-list
nv show router policy prefix-list <prefix-list-id>
nv show router policy prefix-list <prefix-list-id> rule
nv show router policy prefix-list <prefix-list-id> rule <rule-id>
nv show router policy prefix-list <prefix-list-id> rule <rule-id> match
nv show router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>
nv show router policy route-map
nv show router policy route-map <route-map-id>
nv show router policy route-map <route-map-id> rule
nv show router policy route-map <route-map-id> rule <rule-id>
nv show router policy route-map <route-map-id> rule <rule-id> match
nv show router policy route-map <route-map-id> rule <rule-id> set
nv show router policy route-map <route-map-id> rule <rule-id> set as-path-prepend
nv show router policy route-map <route-map-id> rule <rule-id> set community
nv show router policy route-map <route-map-id> rule <rule-id> set community <community-id>
nv show router policy route-map <route-map-id> rule <rule-id> set large-community
nv show router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>
nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as
nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id>
nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address
nv show router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id>
nv show router policy route-map <route-map-id> rule <rule-id> action
nv show router policy route-map <route-map-id> rule <rule-id> action deny
nv show router policy route-map <route-map-id> rule <rule-id> action permit
nv show router policy route-map <route-map-id> rule <rule-id> action permit exit-policy
nv show router bgp
nv show router bgp graceful-restart
nv show router bgp convergence-wait
nv show router ospf
nv show router ospf timers
nv show router ospf timers lsa
nv show router ospf timers spf
nv show router pim
nv show router pim timers
nv show router igmp
nv show router vrrp
nv show router vrr
nv show router adaptive-routing
nv show bridge
nv show bridge domain
nv show bridge domain <domain-id>
nv show bridge domain <domain-id> stp
nv show bridge domain <domain-id> stp state
nv show bridge domain <domain-id> multicast
nv show bridge domain <domain-id> multicast snooping
nv show bridge domain <domain-id> multicast snooping querier
nv show bridge domain <domain-id> vlan
nv show bridge domain <domain-id> vlan <vid>
nv show bridge domain <domain-id> vlan <vid> vni
nv show bridge domain <domain-id> vlan <vid> vni <vni-id>
nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding
nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication
nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>
nv show bridge domain <domain-id> vlan <vid> ptp
nv show bridge domain <domain-id> vlan <vid> multicast
nv show bridge domain <domain-id> vlan <vid> multicast snooping
nv show bridge domain <domain-id> vlan <vid> multicast snooping querier
nv show bridge domain <domain-id> mac-table
nv show bridge domain <domain-id> mdb
nv show bridge domain <domain-id> router-port
nv show mlag
nv show mlag consistency-checker
nv show mlag consistency-checker global
nv show mlag backup
nv show mlag backup <backup-ip>
nv show mlag fdb
nv show mlag fdb local
nv show mlag fdb peer
nv show mlag fdb permanent
nv show mlag mdb
nv show mlag mdb local
nv show mlag mdb peer
nv show mlag multicast-router-port
nv show mlag multicast-router-port local
nv show mlag multicast-router-port peer
nv show mlag vni
nv show mlag vni local
nv show mlag vni peer
nv show mlag lacpdb
nv show mlag lacpdb local
nv show mlag lacpdb peer
nv show mlag neighbor
nv show mlag neighbor dynamic
nv show mlag neighbor permanent
nv show evpn
nv show evpn route-advertise
nv show evpn dad
nv show evpn dad duplicate-action
nv show evpn dad duplicate-action freeze
nv show evpn vni
nv show evpn vni <vni-id>
nv show evpn vni <vni-id> route-advertise
nv show evpn vni <vni-id> route-target
nv show evpn vni <vni-id> route-target export
nv show evpn vni <vni-id> route-target export <rt-id>
nv show evpn vni <vni-id> route-target import
nv show evpn vni <vni-id> route-target import <rt-id>
nv show evpn vni <vni-id> route-target both
nv show evpn vni <vni-id> route-target both <rt-id>
nv show evpn vni <vni-id> mac
nv show evpn vni <vni-id> mac <mac-address-id>
nv show evpn vni <vni-id> host
nv show evpn vni <vni-id> host <ip-address-id>
nv show evpn vni <vni-id> bgp-info
nv show evpn multihoming
nv show evpn multihoming ead-evi-route
nv show evpn multihoming segment
nv show qos
nv show qos advance-buffer-config
nv show qos advance-buffer-config <profile-id>
nv show qos advance-buffer-config <profile-id> ingress-pool
nv show qos advance-buffer-config <profile-id> ingress-pool <pool-id>
nv show qos advance-buffer-config <profile-id> egress-pool
nv show qos advance-buffer-config <profile-id> egress-pool <pool-id>
nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer
nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group
nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id>
nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> switch-priority
nv show qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> switch-priority <qos-sp-id>
nv show qos advance-buffer-config <profile-id> ingress-lossless-buffer
nv show qos advance-buffer-config <profile-id> egress-lossless-buffer
nv show qos advance-buffer-config <profile-id> egress-lossy-buffer
nv show qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class
nv show qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id>
nv show qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority
nv show qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id>
nv show qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port
nv show qos traffic-pool
nv show qos traffic-pool <traffic-pool-id>
nv show qos traffic-pool <traffic-pool-id> switch-priority
nv show qos traffic-pool <traffic-pool-id> switch-priority <qos-sp-id>
nv show qos link-pause
nv show qos link-pause <profile-id>
nv show qos pfc
nv show qos pfc <profile-id>
nv show qos pfc <profile-id> switch-priority
nv show qos pfc <profile-id> switch-priority <qos-sp-id>
nv show qos mapping
nv show qos mapping <profile-id>
nv show qos mapping <profile-id> pcp
nv show qos mapping <profile-id> pcp <qos-pcp-id>
nv show qos mapping <profile-id> dscp
nv show qos mapping <profile-id> dscp <qos-dscp-id>
nv show qos remark
nv show qos remark <profile-id>
nv show qos remark <profile-id> switch-priority
nv show qos remark <profile-id> switch-priority <qos-sp-id>
nv show qos congestion-control
nv show qos congestion-control <profile-id>
nv show qos congestion-control <profile-id> traffic-class
nv show qos congestion-control <profile-id> traffic-class <qos-tc-id>
nv show qos egress-queue-mapping
nv show qos egress-queue-mapping <profile-id>
nv show qos egress-queue-mapping <profile-id> switch-priority
nv show qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id>
nv show qos egress-scheduler
nv show qos egress-scheduler <profile-id>
nv show qos egress-scheduler <profile-id> traffic-class
nv show qos egress-scheduler <profile-id> traffic-class <qos-tc-id>
nv show qos egress-shaper
nv show qos egress-shaper <profile-id>
nv show qos egress-shaper <profile-id> traffic-class
nv show qos egress-shaper <profile-id> traffic-class <qos-tc-id>
nv show qos roce
nv show qos roce prio-map
nv show qos roce tc-map
nv show qos roce pool-map
nv show qos roce pool
nv show qos buffer
nv show qos buffer pool
nv show qos buffer multicast-switch-priority
nv show interface
nv show interface <interface-id>
nv show interface <interface-id> pluggable
nv show interface <interface-id> ip
nv show interface <interface-id> ip address
nv show interface <interface-id> ip address <ip-prefix-id>
nv show interface <interface-id> ip gateway
nv show interface <interface-id> ip gateway <ip-address-id>
nv show interface <interface-id> ip neighbor
nv show interface <interface-id> ip neighbor ipv4
nv show interface <interface-id> ip neighbor ipv4 <neighbor-id>
nv show interface <interface-id> ip neighbor ipv6
nv show interface <interface-id> ip neighbor ipv6 <neighbor-id>
nv show interface <interface-id> ip ipv4
nv show interface <interface-id> ip ipv6
nv show interface <interface-id> ip vrr
nv show interface <interface-id> ip vrr address
nv show interface <interface-id> ip vrr address <ip-prefix-id>
nv show interface <interface-id> ip vrr state
nv show interface <interface-id> ip igmp
nv show interface <interface-id> ip igmp static-group
nv show interface <interface-id> ip igmp static-group <static-group-id>
nv show interface <interface-id> ip vrrp
nv show interface <interface-id> ip vrrp virtual-router
nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id>
nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address
nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>
nv show interface <interface-id> ip neighbor-discovery
nv show interface <interface-id> ip neighbor-discovery rdnss
nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>
nv show interface <interface-id> ip neighbor-discovery prefix
nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>
nv show interface <interface-id> ip neighbor-discovery dnssl
nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>
nv show interface <interface-id> ip neighbor-discovery router-advertisement
nv show interface <interface-id> ip neighbor-discovery home-agent
nv show interface <interface-id> link
nv show interface <interface-id> link state
nv show interface <interface-id> link breakout
nv show interface <interface-id> link breakout <mode-id>
nv show interface <interface-id> link stats
nv show interface <interface-id> link traffic-engineering
nv show interface <interface-id> link flag
nv show interface <interface-id> router
nv show interface <interface-id> router pbr
nv show interface <interface-id> router pbr map
nv show interface <interface-id> router pbr map <pbr-map-id>
nv show interface <interface-id> router ospf
nv show interface <interface-id> router ospf timers
nv show interface <interface-id> router ospf authentication
nv show interface <interface-id> router ospf bfd
nv show interface <interface-id> router pim
nv show interface <interface-id> router pim timers
nv show interface <interface-id> router pim bfd
nv show interface <interface-id> router pim address-family
nv show interface <interface-id> router pim address-family ipv4-unicast
nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp
nv show interface <interface-id> router adaptive-routing
nv show interface <interface-id> bond
nv show interface <interface-id> bond member
nv show interface <interface-id> bond member <member-id>
nv show interface <interface-id> bond mlag
nv show interface <interface-id> bond mlag consistency-checker
nv show interface <interface-id> bridge
nv show interface <interface-id> bridge domain
nv show interface <interface-id> bridge domain <domain-id>
nv show interface <interface-id> bridge domain <domain-id> stp
nv show interface <interface-id> bridge domain <domain-id> vlan
nv show interface <interface-id> bridge domain <domain-id> vlan <vid>
nv show interface <interface-id> lldp
nv show interface <interface-id> lldp neighbor
nv show interface <interface-id> lldp neighbor <neighbor-id>
nv show interface <interface-id> lldp neighbor <neighbor-id> bridge
nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan
nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid>
nv show interface <interface-id> qos
nv show interface <interface-id> qos pfc
nv show interface <interface-id> qos link-pause
nv show interface <interface-id> qos mapping
nv show interface <interface-id> qos mapping pcp
nv show interface <interface-id> qos mapping pcp <qos-pcp-id>
nv show interface <interface-id> qos mapping dscp
nv show interface <interface-id> qos mapping dscp <qos-dscp-id>
nv show interface <interface-id> qos remark
nv show interface <interface-id> qos remark switch-priority
nv show interface <interface-id> qos remark switch-priority <qos-sp-id>
nv show interface <interface-id> qos congestion-control
nv show interface <interface-id> qos congestion-control traffic-class
nv show interface <interface-id> qos congestion-control traffic-class <qos-tc-id>
nv show interface <interface-id> qos egress-scheduler
nv show interface <interface-id> qos egress-scheduler traffic-class
nv show interface <interface-id> qos egress-scheduler traffic-class <qos-tc-id>
nv show interface <interface-id> qos egress-queue-mapping
nv show interface <interface-id> qos egress-queue-mapping switch-priority
nv show interface <interface-id> qos egress-queue-mapping switch-priority <qos-sp-id>
nv show interface <interface-id> qos egress-shaper
nv show interface <interface-id> qos egress-shaper traffic-class
nv show interface <interface-id> qos egress-shaper traffic-class <qos-tc-id>
nv show interface <interface-id> qos counter
nv show interface <interface-id> qos counter port-stats
nv show interface <interface-id> qos counter port-stats rx-stats
nv show interface <interface-id> qos counter port-stats tx-stats
nv show interface <interface-id> qos counter egress-queue-stats
nv show interface <interface-id> qos counter ingress-buffer-stats
nv show interface <interface-id> qos counter pfc-stats
nv show interface <interface-id> qos roce
nv show interface <interface-id> qos roce counters
nv show interface <interface-id> qos roce status
nv show interface <interface-id> qos roce status pool-map
nv show interface <interface-id> qos roce status prio-map
nv show interface <interface-id> qos roce status tc-map
nv show interface <interface-id> qos buffer
nv show interface <interface-id> qos buffer ingress-port
nv show interface <interface-id> qos buffer ingress-priority-group
nv show interface <interface-id> qos buffer egress-port
nv show interface <interface-id> qos buffer egress-traffic-class
nv show interface <interface-id> qos buffer egress-multicast
nv show interface <interface-id> evpn
nv show interface <interface-id> evpn multihoming
nv show interface <interface-id> evpn multihoming segment
nv show interface <interface-id> acl
nv show interface <interface-id> acl <acl-id>
nv show interface <interface-id> acl <acl-id> statistics
nv show interface <interface-id> acl <acl-id> statistics <rule-id>
nv show interface <interface-id> acl <acl-id> inbound
nv show interface <interface-id> acl <acl-id> inbound control-plane
nv show interface <interface-id> acl <acl-id> outbound
nv show interface <interface-id> acl <acl-id> outbound control-plane
nv show interface <interface-id> ptp
nv show interface <interface-id> ptp timers
nv show interface <interface-id> ptp counters
nv show interface <interface-id> tunnel
nv show interface <interface-id> storm-control
nv show interface <interface-id> synce
nv show interface <interface-id> synce counters
nv show service
nv show service dhcp-server
nv show service dhcp-server <vrf-id>
nv show service dhcp-server <vrf-id> interface
nv show service dhcp-server <vrf-id> interface <interface-id>
nv show service dhcp-server <vrf-id> pool
nv show service dhcp-server <vrf-id> pool <pool-id>
nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server
nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>
nv show service dhcp-server <vrf-id> pool <pool-id> domain-name
nv show service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>
nv show service dhcp-server <vrf-id> pool <pool-id> gateway
nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>
nv show service dhcp-server <vrf-id> pool <pool-id> range
nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id>
nv show service dhcp-server <vrf-id> domain-name
nv show service dhcp-server <vrf-id> domain-name <domain-name-id>
nv show service dhcp-server <vrf-id> domain-name-server
nv show service dhcp-server <vrf-id> domain-name-server <server-id>
nv show service dhcp-server <vrf-id> static
nv show service dhcp-server <vrf-id> static <static-id>
nv show service dhcp-server6
nv show service dhcp-server6 <vrf-id>
nv show service dhcp-server6 <vrf-id> interface
nv show service dhcp-server6 <vrf-id> interface <interface-id>
nv show service dhcp-server6 <vrf-id> pool
nv show service dhcp-server6 <vrf-id> pool <pool-id>
nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server
nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>
nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name
nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>
nv show service dhcp-server6 <vrf-id> pool <pool-id> range
nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>
nv show service dhcp-server6 <vrf-id> domain-name
nv show service dhcp-server6 <vrf-id> domain-name <domain-name-id>
nv show service dhcp-server6 <vrf-id> domain-name-server
nv show service dhcp-server6 <vrf-id> domain-name-server <server-id>
nv show service dhcp-server6 <vrf-id> static
nv show service dhcp-server6 <vrf-id> static <static-id>
nv show service dns
nv show service dns <vrf-id>
nv show service dns <vrf-id> server
nv show service dns <vrf-id> server <dns-server-id>
nv show service syslog
nv show service syslog <vrf-id>
nv show service syslog <vrf-id> server
nv show service syslog <vrf-id> server <server-id>
nv show service ntp
nv show service ntp <vrf-id>
nv show service ntp <vrf-id> server
nv show service ntp <vrf-id> server <server-id>
nv show service ntp <vrf-id> pool
nv show service ntp <vrf-id> pool <server-id>
nv show service dhcp-relay
nv show service dhcp-relay <vrf-id>
nv show service dhcp-relay <vrf-id> server
nv show service dhcp-relay <vrf-id> server <server-id>
nv show service dhcp-relay <vrf-id> interface
nv show service dhcp-relay <vrf-id> interface <interface-id>
nv show service dhcp-relay <vrf-id> giaddress-interface
nv show service dhcp-relay <vrf-id> giaddress-interface <interface-id>
nv show service dhcp-relay6
nv show service dhcp-relay6 <vrf-id>
nv show service dhcp-relay6 <vrf-id> interface
nv show service dhcp-relay6 <vrf-id> interface upstream
nv show service dhcp-relay6 <vrf-id> interface upstream <interface-id>
nv show service dhcp-relay6 <vrf-id> interface downstream
nv show service dhcp-relay6 <vrf-id> interface downstream <interface-id>
nv show service snmp-server
nv show service snmp-server listening-address
nv show service snmp-server listening-address <listening-address-id>
nv show service snmp-server username
nv show service snmp-server username <username-id>
nv show service snmp-server username <username-id> auth-none
nv show service snmp-server username <username-id> auth-md5
nv show service snmp-server username <username-id> auth-md5 <auth-id>
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server username <username-id> auth-sha
nv show service snmp-server username <username-id> auth-sha <auth-id>
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server mibs
nv show service snmp-server viewname
nv show service snmp-server viewname <viewname-id>
nv show service snmp-server readonly-community
nv show service snmp-server readonly-community <readonly-community-id>
nv show service snmp-server readonly-community <readonly-community-id> access
nv show service snmp-server readonly-community <readonly-community-id> access <access-id>
nv show service snmp-server readonly-community-v6
nv show service snmp-server readonly-community-v6 <readonly-community-id>
nv show service snmp-server readonly-community-v6 <readonly-community-id> access
nv show service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
nv show service snmp-server trap-link-down
nv show service snmp-server trap-link-up
nv show service snmp-server trap-snmp-auth-failures
nv show service snmp-server trap-cpu-load-average
nv show service snmp-server trap-cpu-load-average one-minute
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id>
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id>
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute <fifteen-minute-id>
nv show service snmp-server trap-destination
nv show service snmp-server trap-destination <trap-destination-id>
nv show service snmp-server trap-destination <trap-destination-id> community-password
nv show service snmp-server trap-destination <trap-destination-id> community-password <community-password-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username
nv show service snmp-server trap-destination <trap-destination-id> username <username-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service synce
nv show service ptp
nv show service ptp <instance-id>
nv show service ptp <instance-id> acceptable-master
nv show service ptp <instance-id> acceptable-master <clock-id>
nv show service ptp <instance-id> unicast-master
nv show service ptp <instance-id> unicast-master <table-id>
nv show service ptp <instance-id> unicast-master <table-id> address
nv show service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv show service ptp <instance-id> profile
nv show service ptp <instance-id> profile <profile-id>
nv show service ptp <instance-id> monitor
nv show service ptp <instance-id> monitor timestamp-log
nv show service ptp <instance-id> monitor violations
nv show service ptp <instance-id> monitor violations log
nv show service ptp <instance-id> monitor violations log acceptable-master
nv show service ptp <instance-id> monitor violations log forced-master
nv show service ptp <instance-id> monitor violations log max-offset
nv show service ptp <instance-id> monitor violations log min-offset
nv show service ptp <instance-id> monitor violations log path-delay
nv show service ptp <instance-id> current
nv show service ptp <instance-id> clock-quality
nv show service ptp <instance-id> parent
nv show service ptp <instance-id> parent grandmaster-clock-quality
nv show service ptp <instance-id> time-properties
nv show service lldp
nv show system
nv show system message
nv show system cpu
nv show system memory
nv show system reboot
nv show system reboot reason
nv show system reboot history
nv show system config
nv show system config auto-save
nv show system config apply
nv show system config apply ignore
nv show system config apply ignore <ignore-id>
nv show system config snippet
nv show system ztp
nv show system ztp script
nv show system ztp status
nv show system acl
nv show system counter
nv show system counter polling-interval
nv show system control-plane
nv show system control-plane trap
nv show system control-plane trap <trap-id>
nv show system control-plane policer
nv show system control-plane policer <policer-id>
nv show system control-plane policer <policer-id> statistics
nv show system global
nv show system global reserved
nv show system global reserved routing-table
nv show system global reserved routing-table pbr
nv show system global reserved vlan
nv show system global reserved vlan internal
nv show system global reserved vlan l3-vni-vlan
nv show system forwarding
nv show system forwarding lag-hash
nv show system forwarding ecmp-hash
nv show system forwarding programming
nv show system forwarding profile-option
nv show system port-mirror
nv show system port-mirror session
nv show system port-mirror session <session-id>
nv show system port-mirror session <session-id> span
nv show system port-mirror session <session-id> span source-port
nv show system port-mirror session <session-id> span source-port <port-id>
nv show system port-mirror session <session-id> span destination
nv show system port-mirror session <session-id> span destination <port-id>
nv show system port-mirror session <session-id> span truncate
nv show system port-mirror session <session-id> erspan
nv show system port-mirror session <session-id> erspan source-port
nv show system port-mirror session <session-id> erspan source-port <port-id>
nv show system port-mirror session <session-id> erspan destination
nv show system port-mirror session <session-id> erspan destination source-ip
nv show system port-mirror session <session-id> erspan destination source-ip <source-ip>
nv show system port-mirror session <session-id> erspan destination dest-ip
nv show system port-mirror session <session-id> erspan destination dest-ip <dest-ip>
nv show system port-mirror session <session-id> erspan truncate
nv show system wjh
nv show system wjh channel
nv show system wjh channel <channel-id>
nv show system wjh channel <channel-id> trigger
nv show system wjh packet-buffer
nv show system aaa
nv show system aaa user
nv show system aaa user <user-id>
nv show system aaa user <user-id> ssh
nv show system aaa user <user-id> ssh authorized-key
nv show system aaa user <user-id> ssh authorized-key <ssh-authorized-key-id>
nv show system aaa role
nv show system aaa role <role-id>
nv show system aaa authentication-order
nv show system aaa authentication-order <priority-id>
nv show system aaa tacacs
nv show system aaa tacacs authentication
nv show system aaa tacacs accounting
nv show system aaa tacacs server
nv show system aaa tacacs server <priority-id>
nv show system aaa tacacs exclude-user
nv show vrf
nv show vrf <vrf-id>
nv show vrf <vrf-id> loopback
nv show vrf <vrf-id> loopback ip
nv show vrf <vrf-id> loopback ip address
nv show vrf <vrf-id> loopback ip address <ip-prefix-id>
nv show vrf <vrf-id> evpn
nv show vrf <vrf-id> evpn vni
nv show vrf <vrf-id> evpn vni <vni-id>
nv show vrf <vrf-id> evpn bgp-info
nv show vrf <vrf-id> evpn remote-router-mac
nv show vrf <vrf-id> evpn remote-router-mac <mac-address-id>
nv show vrf <vrf-id> evpn nexthop-vtep
nv show vrf <vrf-id> evpn nexthop-vtep <nexthop-vtep-id>
nv show vrf <vrf-id> router
nv show vrf <vrf-id> router rib
nv show vrf <vrf-id> router rib <afi>
nv show vrf <vrf-id> router rib <afi> protocol
nv show vrf <vrf-id> router rib <afi> protocol <import-protocol-id>
nv show vrf <vrf-id> router rib <afi> route
nv show vrf <vrf-id> router rib <afi> route <route-id>
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id>
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index>
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> flags
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> via
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> via <via-id>
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> via <via-id> flags
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> via <via-id> label
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> via <via-id> resolved-via
nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> entry-index <entry-index> via <via-id> resolved-via <resolved-via-id>
nv show vrf <vrf-id> router nexthop-tracking
nv show vrf <vrf-id> router nexthop-tracking <afi>
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id>
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol <nht-protocol-id>
nv show vrf <vrf-id> router bgp
nv show vrf <vrf-id> router bgp nexthop
nv show vrf <vrf-id> router bgp nexthop <afi>
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id>
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id> resolved-via
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id> path
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family
nv show vrf <vrf-id> router bgp address-family ipv4-unicast
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf
nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route
nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast network
nv show vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast multipaths
nv show vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> peer
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> flags
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> bestpath
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> aspath
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> ext-community
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id> sub-group
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd <rd-id>
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd <rd-id> route-type
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd <rd-id> route-type <route-type-id>
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd <rd-id> route-type <route-type-id> route
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd <rd-id> route-type <route-type-id> route <evpn-route-id>
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd <rd-id> route-type <route-type-id> route <evpn-route-id> path
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn loc-rib rd <rd-id> route-type <route-type-id> route <evpn-route-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn update-group
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn update-group <group-id>
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn update-group <group-id> sub-group
nv show vrf <vrf-id> router bgp address-family ipv6-unicast
nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route
nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast network
nv show vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list
nv show vrf <vrf-id> router bgp address-family ipv6-unicast multipaths
nv show vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> peer
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> flags
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> bestpath
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> aspath
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> community
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> large-community
nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> ext-community
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id> sub-group
nv show vrf <vrf-id> router bgp path-selection
nv show vrf <vrf-id> router bgp path-selection aspath
nv show vrf <vrf-id> router bgp path-selection med
nv show vrf <vrf-id> router bgp path-selection multipath
nv show vrf <vrf-id> router bgp route-reflection
nv show vrf <vrf-id> router bgp peer-group
nv show vrf <vrf-id> router bgp peer-group <peer-group-id>
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> local-as
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> timers
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound
nv show vrf <vrf-id> router bgp route-export
nv show vrf <vrf-id> router bgp route-export to-evpn
nv show vrf <vrf-id> router bgp route-export to-evpn route-target
nv show vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>
nv show vrf <vrf-id> router bgp route-import
nv show vrf <vrf-id> router bgp route-import from-evpn
nv show vrf <vrf-id> router bgp route-import from-evpn route-target
nv show vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>
nv show vrf <vrf-id> router bgp timers
nv show vrf <vrf-id> router bgp confederation
nv show vrf <vrf-id> router bgp confederation member-as
nv show vrf <vrf-id> router bgp dynamic-neighbor
nv show vrf <vrf-id> router bgp dynamic-neighbor listen-range
nv show vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id>
nv show vrf <vrf-id> router bgp neighbor
nv show vrf <vrf-id> router bgp neighbor <neighbor-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> local-as
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> message-stats
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ebgp-policy
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast capabilities
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast capabilities
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn capabilities
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> timers
nv show vrf <vrf-id> router static
nv show vrf <vrf-id> router static <route-id>
nv show vrf <vrf-id> router static <route-id> distance
nv show vrf <vrf-id> router static <route-id> distance <distance-id>
nv show vrf <vrf-id> router static <route-id> distance <distance-id> via
nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>
nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag
nv show vrf <vrf-id> router static <route-id> via
nv show vrf <vrf-id> router static <route-id> via <via-id>
nv show vrf <vrf-id> router static <route-id> via <via-id> flag
nv show vrf <vrf-id> router pim
nv show vrf <vrf-id> router pim timers
nv show vrf <vrf-id> router pim ecmp
nv show vrf <vrf-id> router pim msdp-mesh-group
nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>
nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address
nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>
nv show vrf <vrf-id> router pim address-family
nv show vrf <vrf-id> router pim address-family ipv4-unicast
nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover
nv show vrf <vrf-id> router pim address-family ipv4-unicast rp
nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>
nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range
nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>
nv show vrf <vrf-id> router ospf
nv show vrf <vrf-id> router ospf area
nv show vrf <vrf-id> router ospf area <area-id>
nv show vrf <vrf-id> router ospf area <area-id> filter-list
nv show vrf <vrf-id> router ospf area <area-id> range
nv show vrf <vrf-id> router ospf area <area-id> range <range-id>
nv show vrf <vrf-id> router ospf area <area-id> network
nv show vrf <vrf-id> router ospf area <area-id> network <network-id>
nv show vrf <vrf-id> router ospf default-originate
nv show vrf <vrf-id> router ospf distance
nv show vrf <vrf-id> router ospf max-metric
nv show vrf <vrf-id> router ospf log
nv show vrf <vrf-id> router ospf redistribute
nv show vrf <vrf-id> router ospf redistribute static
nv show vrf <vrf-id> router ospf redistribute connected
nv show vrf <vrf-id> router ospf redistribute kernel
nv show vrf <vrf-id> router ospf redistribute bgp
nv show vrf <vrf-id> router ospf timers
nv show vrf <vrf-id> router ospf timers lsa
nv show vrf <vrf-id> router ospf timers spf
nv show vrf <vrf-id> ptp
nv show nve
nv show nve vxlan
nv show nve vxlan mlag
nv show nve vxlan source
nv show nve vxlan flooding
nv show nve vxlan flooding head-end-replication
nv show nve vxlan flooding head-end-replication <hrep-id>
nv show nve vxlan encapsulation
nv show nve vxlan encapsulation dscp
nv show nve vxlan decapsulation
nv show nve vxlan decapsulation dscp
nv show acl
nv show acl <acl-id>
nv show acl <acl-id> rule
nv show acl <acl-id> rule <rule-id>
nv show acl <acl-id> rule <rule-id> match
nv show acl <acl-id> rule <rule-id> match ip
nv show acl <acl-id> rule <rule-id> match ip source-port
nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>
nv show acl <acl-id> rule <rule-id> match ip dest-port
nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>
nv show acl <acl-id> rule <rule-id> match ip fragment
nv show acl <acl-id> rule <rule-id> match ip ecn
nv show acl <acl-id> rule <rule-id> match ip ecn flags
nv show acl <acl-id> rule <rule-id> match ip tcp
nv show acl <acl-id> rule <rule-id> match ip tcp flags
nv show acl <acl-id> rule <rule-id> match ip tcp mask
nv show acl <acl-id> rule <rule-id> match mac
nv show acl <acl-id> rule <rule-id> action
nv show acl <acl-id> rule <rule-id> action permit
nv show acl <acl-id> rule <rule-id> action deny
nv show acl <acl-id> rule <rule-id> action log
nv show acl <acl-id> rule <rule-id> action set
nv show acl <acl-id> rule <rule-id> action erspan
nv show acl <acl-id> rule <rule-id> action police
nv set router
nv set router ptm
nv set router ptm enable (on|off)
nv set router nexthop
nv set router nexthop group <nexthop-group-id>
nv set router nexthop group <nexthop-group-id> via <via-id>
nv set router nexthop group <nexthop-group-id> via <via-id> interface (auto|<interface-name>)
nv set router nexthop group <nexthop-group-id> via <via-id> vrf (auto|<vrf-name>)
nv set router pbr
nv set router pbr map <pbr-map-id>
nv set router pbr map <pbr-map-id> rule <rule-id>
nv set router pbr map <pbr-map-id> rule <rule-id> match
nv set router pbr map <pbr-map-id> rule <rule-id> match source-ip (<ipv4-prefix>|<ipv6-prefix>)
nv set router pbr map <pbr-map-id> rule <rule-id> match destination-ip (<ipv4-prefix>|<ipv6-prefix>)
nv set router pbr map <pbr-map-id> rule <rule-id> match dscp 0-63
nv set router pbr map <pbr-map-id> rule <rule-id> match ecn 0-3
nv set router pbr map <pbr-map-id> rule <rule-id> action
nv set router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>
nv set router pbr map <pbr-map-id> rule <rule-id> action vrf <vrf-name>
nv set router pbr enable (on|off)
nv set router policy
nv set router policy community-list <list-id>
nv set router policy community-list <list-id> rule <rule-id>
nv set router policy community-list <list-id> rule <rule-id> community <community-id>
nv set router policy community-list <list-id> rule <rule-id> action (permit|deny)
nv set router policy as-path-list <list-id>
nv set router policy as-path-list <list-id> rule <rule-id>
nv set router policy as-path-list <list-id> rule <rule-id> action (permit|deny)
nv set router policy as-path-list <list-id> rule <rule-id> aspath-exp <bgp-regex>
nv set router policy ext-community-list <list-id>
nv set router policy ext-community-list <list-id> rule <rule-id>
nv set router policy ext-community-list <list-id> rule <rule-id> ext-community
nv set router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id>
nv set router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id>
nv set router policy ext-community-list <list-id> rule <rule-id> action (permit|deny)
nv set router policy large-community-list <list-id>
nv set router policy large-community-list <list-id> rule <rule-id>
nv set router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>
nv set router policy large-community-list <list-id> rule <rule-id> action (permit|deny)
nv set router policy prefix-list <prefix-list-id>
nv set router policy prefix-list <prefix-list-id> rule <rule-id>
nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>
nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len 0-128
nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len 0-128
nv set router policy prefix-list <prefix-list-id> rule <rule-id> action (permit|deny)
nv set router policy prefix-list <prefix-list-id> type (ipv4|ipv6)
nv set router policy route-map <route-map-id>
nv set router policy route-map <route-map-id> rule <rule-id>
nv set router policy route-map <route-map-id> rule <rule-id> match
nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list <generic-name>
nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len 0-128
nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list <generic-name>
nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len 0-32
nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop (<ipv4>|<ipv6>)
nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type blackhole
nv set router policy route-map <route-map-id> rule <rule-id> match as-path-list <generic-name>
nv set router policy route-map <route-map-id> rule <rule-id> match community-list <generic-name>
nv set router policy route-map <route-map-id> rule <rule-id> match large-community-list <generic-name>
nv set router policy route-map <route-map-id> rule <rule-id> match metric 1-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> match interface (<interface-name>|<vrf-name>)
nv set router policy route-map <route-map-id> rule <rule-id> match tag 1-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> match source-protocol (bgp|connected|kernel|ospf|ospf6|sharp|static)
nv set router policy route-map <route-map-id> rule <rule-id> match origin (egp|igp|incomplete)
nv set router policy route-map <route-map-id> rule <rule-id> match peer (local|<interface-name>|<ipv4>|<ipv6>)
nv set router policy route-map <route-map-id> rule <rule-id> match local-preference 0-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> match evpn-route-type (macip|imet|ip-prefix)
nv set router policy route-map <route-map-id> rule <rule-id> match evpn-vni <value>
nv set router policy route-map <route-map-id> rule <rule-id> match evpn-default-route (on|off)
nv set router policy route-map <route-map-id> rule <rule-id> match source-vrf <vrf-name>
nv set router policy route-map <route-map-id> rule <rule-id> match type (ipv4|ipv6)
nv set router policy route-map <route-map-id> rule <rule-id> set
nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend
nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as <asn-range>
nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as 1-10
nv set router policy route-map <route-map-id> rule <rule-id> set community <community-id>
nv set router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>
nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id>
nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id>
nv set router policy route-map <route-map-id> rule <rule-id> set as-path-exclude 1-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate (on|off)
nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-rt <route-distinguisher>
nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-soo <route-distinguisher>
nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-bw (1-25600|cumulative|multipaths|cumulative-non-transitive|multipaths-non-transitive)
nv set router policy route-map <route-map-id> rule <rule-id> set local-preference 0-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> set weight 0-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> set metric (1-4294967295|metric-plus|metric-minus|rtt|rtt-plus|rtt-minus)
nv set router policy route-map <route-map-id> rule <rule-id> set metric-type (type-1|type-2)
nv set router policy route-map <route-map-id> rule <rule-id> set origin (egp|igp|incomplete)
nv set router policy route-map <route-map-id> rule <rule-id> set tag 1-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global <ipv6>
nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local <ipv6>
nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global (on|off)
nv set router policy route-map <route-map-id> rule <rule-id> set ip-nexthop (unchanged|peer-addr|<ipv4>|<ipv6>)
nv set router policy route-map <route-map-id> rule <rule-id> set source-ip (<ipv4>|<ipv6>)
nv set router policy route-map <route-map-id> rule <rule-id> set community-delete-list (<generic-name>|<integer>)
nv set router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list (<generic-name>|<integer>)
nv set router policy route-map <route-map-id> rule <rule-id> set originator-id <ipv4>
nv set router policy route-map <route-map-id> rule <rule-id> set label-index 0-1048560
nv set router policy route-map <route-map-id> rule <rule-id> set forwarding-address <ipv6>
nv set router policy route-map <route-map-id> rule <rule-id> action
nv set router policy route-map <route-map-id> rule <rule-id> action deny
nv set router policy route-map <route-map-id> rule <rule-id> action permit
nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy
nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule <value>
nv set router policy route-map <route-map-id> rule <rule-id> description none
nv set router bgp
nv set router bgp graceful-restart
nv set router bgp graceful-restart mode (off|helper-only|full)
nv set router bgp graceful-restart restart-time 1-3600
nv set router bgp graceful-restart path-selection-deferral-time 0-3600
nv set router bgp graceful-restart stale-routes-time 1-3600
nv set router bgp convergence-wait
nv set router bgp convergence-wait time 0-3600
nv set router bgp convergence-wait establish-wait-time 0-3600
nv set router bgp enable (on|off)
nv set router bgp autonomous-system (1-4294967295|none|leaf|spine)
nv set router bgp router-id (none|<ipv4>)
nv set router bgp policy-update-timer 0-600
nv set router bgp graceful-shutdown (on|off)
nv set router bgp wait-for-install (on|off)
nv set router ospf
nv set router ospf timers
nv set router ospf timers lsa
nv set router ospf timers lsa min-arrival 0-600000
nv set router ospf timers lsa throttle 0-5000
nv set router ospf timers spf
nv set router ospf timers spf delay 0-600000
nv set router ospf timers spf holdtime 0-600000
nv set router ospf timers spf max-holdtime 0-600000
nv set router ospf timers refresh 10-1800
nv set router ospf enable (on|off)
nv set router ospf router-id (none|<ipv4>)
nv set router pim
nv set router pim timers
nv set router pim timers hello-interval 1-180
nv set router pim timers register-suppress 5-60000
nv set router pim timers join-prune-interval 60-600
nv set router pim timers keep-alive 31-60000
nv set router pim timers rp-keep-alive 31-60000
nv set router pim enable (on|off)
nv set router pim packets 1-100
nv set router igmp
nv set router igmp enable (on|off)
nv set router vrrp
nv set router vrrp enable (on|off)
nv set router vrrp priority 1-254
nv set router vrrp preempt (on|off)
nv set router vrrp advertisement-interval 10-40950
nv set router vrr
nv set router vrr enable (on|off)
nv set router adaptive-routing
nv set router adaptive-routing enable (on|off)
nv set bridge
nv set bridge domain <domain-id>
nv set bridge domain <domain-id> stp
nv set bridge domain <domain-id> stp state (up|down)
nv set bridge domain <domain-id> stp priority 4096-61440
nv set bridge domain <domain-id> multicast
nv set bridge domain <domain-id> multicast snooping
nv set bridge domain <domain-id> multicast snooping querier
nv set bridge domain <domain-id> multicast snooping querier enable (on|off)
nv set bridge domain <domain-id> multicast snooping enable (on|off)
nv set bridge domain <domain-id> vlan <vid>
nv set bridge domain <domain-id> vlan <vid> vni <vni-id>
nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding
nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>
nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding enable (on|off|auto)
nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group <ipv4-multicast>
nv set bridge domain <domain-id> vlan <vid> vni <vni-id> mac-learning (on|off|auto)
nv set bridge domain <domain-id> vlan <vid> ptp
nv set bridge domain <domain-id> vlan <vid> ptp enable (on|off)
nv set bridge domain <domain-id> vlan <vid> multicast
nv set bridge domain <domain-id> vlan <vid> multicast snooping
nv set bridge domain <domain-id> vlan <vid> multicast snooping querier
nv set bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip <ipv4>
nv set bridge domain <domain-id> type vlan-aware
nv set bridge domain <domain-id> untagged (1-4094|none)
nv set bridge domain <domain-id> encap 802.1Q
nv set bridge domain <domain-id> mac-address (auto|<mac>)
nv set bridge domain <domain-id> vlan-vni-offset 0-16773120
nv set mlag
nv set mlag backup <backup-ip>
nv set mlag backup <backup-ip> vrf <vrf-name>
nv set mlag enable (on|off)
nv set mlag mac-address (auto|<mac>)
nv set mlag peer-ip (linklocal|<ipv4>|<ipv6>)
nv set mlag priority 0-65535
nv set mlag init-delay 1-900
nv set mlag debug (on|off)
nv set mlag lacp-conflict
nv set evpn
nv set evpn route-advertise
nv set evpn route-advertise nexthop-setting (system-ip-mac|shared-ip-mac)
nv set evpn route-advertise svi-ip (on|off)
nv set evpn route-advertise default-gateway (on|off)
nv set evpn dad
nv set evpn dad duplicate-action
nv set evpn dad duplicate-action freeze
nv set evpn dad duplicate-action freeze duration (30-3600|permanent)
nv set evpn dad enable (on|off)
nv set evpn dad mac-move-threshold 2-1000
nv set evpn dad move-window 2-1800
nv set evpn vni <vni-id>
nv set evpn vni <vni-id> route-advertise
nv set evpn vni <vni-id> route-advertise svi-ip (on|off|auto)
nv set evpn vni <vni-id> route-advertise default-gateway (on|off|auto)
nv set evpn vni <vni-id> route-target
nv set evpn vni <vni-id> route-target export <rt-id>
nv set evpn vni <vni-id> route-target import <rt-id>
nv set evpn vni <vni-id> route-target both <rt-id>
nv set evpn vni <vni-id> rd (auto|<route-distinguisher>)
nv set evpn multihoming
nv set evpn multihoming ead-evi-route
nv set evpn multihoming ead-evi-route rx (on|off)
nv set evpn multihoming ead-evi-route tx (on|off)
nv set evpn multihoming segment
nv set evpn multihoming segment mac-address <mac>
nv set evpn multihoming segment df-preference 1-65535
nv set evpn multihoming enable (on|off)
nv set evpn multihoming mac-holdtime 0-86400
nv set evpn multihoming neighbor-holdtime 0-86400
nv set evpn multihoming startup-delay 0-3600
nv set evpn enable (on|off)
nv set qos
nv set qos advance-buffer-config <profile-id>
nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id>
nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id> memory-percent 0-100
nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id> infinite (true|false)
nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id> mode (static|dynamic)
nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id> reserved 0-4294967295
nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id> shared-bytes 0-4294967295
nv set qos advance-buffer-config <profile-id> ingress-pool <pool-id> shared-alpha (alpha_0|alpha_1_128|alpha_1_64|alpha_1_32|alpha_1_16|alpha_1_8|alpha_1_4|alpha_1_2|alpha_1|alpha_2|alpha_4|alpha_8|alpha_16|alpha_32|alpha_64|alpha_infinity)
nv set qos advance-buffer-config <profile-id> egress-pool <pool-id>
nv set qos advance-buffer-config <profile-id> egress-pool <pool-id> memory-percent 0-100
nv set qos advance-buffer-config <profile-id> egress-pool <pool-id> infinite (true|false)
nv set qos advance-buffer-config <profile-id> egress-pool <pool-id> mode (static|dynamic)
nv set qos advance-buffer-config <profile-id> egress-pool <pool-id> reserved 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-pool <pool-id> shared-bytes 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-pool <pool-id> shared-alpha (alpha_0|alpha_1_128|alpha_1_64|alpha_1_32|alpha_1_16|alpha_1_8|alpha_1_4|alpha_1_2|alpha_1|alpha_2|alpha_4|alpha_8|alpha_16|alpha_32|alpha_64|alpha_infinity)
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id>
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> switch-priority <qos-sp-id>
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> name <value>
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> reserved 0-4294967295
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> shared-bytes 0-4294967295
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> shared-alpha (alpha_0|alpha_1_128|alpha_1_64|alpha_1_32|alpha_1_16|alpha_1_8|alpha_1_4|alpha_1_2|alpha_1|alpha_2|alpha_4|alpha_8|alpha_16|alpha_32|alpha_64|alpha_infinity)
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> service-pool <integer>
nv set qos advance-buffer-config <profile-id> ingress-lossless-buffer
nv set qos advance-buffer-config <profile-id> ingress-lossless-buffer service-pool <integer>
nv set qos advance-buffer-config <profile-id> ingress-lossless-buffer shared-alpha (alpha_0|alpha_1_128|alpha_1_64|alpha_1_32|alpha_1_16|alpha_1_8|alpha_1_4|alpha_1_2|alpha_1|alpha_2|alpha_4|alpha_8|alpha_16|alpha_32|alpha_64|alpha_infinity)
nv set qos advance-buffer-config <profile-id> ingress-lossless-buffer shared-bytes 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossless-buffer
nv set qos advance-buffer-config <profile-id> egress-lossless-buffer service-pool <integer>
nv set qos advance-buffer-config <profile-id> egress-lossless-buffer reserved 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossless-buffer shared-alpha (alpha_0|alpha_1_128|alpha_1_64|alpha_1_32|alpha_1_16|alpha_1_8|alpha_1_4|alpha_1_2|alpha_1|alpha_2|alpha_4|alpha_8|alpha_16|alpha_32|alpha_64|alpha_infinity)
nv set qos advance-buffer-config <profile-id> egress-lossless-buffer shared-bytes 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id>
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> reserved 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> shared-bytes 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> shared-alpha (alpha_0|alpha_1_128|alpha_1_64|alpha_1_32|alpha_1_16|alpha_1_8|alpha_1_4|alpha_1_2|alpha_1|alpha_2|alpha_4|alpha_8|alpha_16|alpha_32|alpha_64|alpha_infinity)
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> service-pool <integer>
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id>
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> reserved 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> shared-bytes 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> shared-alpha (alpha_0|alpha_1_128|alpha_1_64|alpha_1_32|alpha_1_16|alpha_1_8|alpha_1_4|alpha_1_2|alpha_1|alpha_2|alpha_4|alpha_8|alpha_16|alpha_32|alpha_64|alpha_infinity)
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> service-pool <integer>
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port reserved 0-4294967295
nv set qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port shared-bytes 0-4294967295
nv set qos traffic-pool <traffic-pool-id>
nv set qos traffic-pool <traffic-pool-id> switch-priority <qos-sp-id>
nv set qos traffic-pool <traffic-pool-id> memory-percent 1-100
nv set qos link-pause <profile-id>
nv set qos link-pause <profile-id> xoff-threshold <value>
nv set qos link-pause <profile-id> xon-threshold <value>
nv set qos link-pause <profile-id> port-buffer <value>
nv set qos link-pause <profile-id> cable-length 1-100000
nv set qos link-pause <profile-id> tx (enable|disable)
nv set qos link-pause <profile-id> rx (enable|disable)
nv set qos pfc <profile-id>
nv set qos pfc <profile-id> switch-priority <qos-sp-id>
nv set qos pfc <profile-id> xoff-threshold <value>
nv set qos pfc <profile-id> xon-threshold <value>
nv set qos pfc <profile-id> port-buffer <value>
nv set qos pfc <profile-id> cable-length 1-100000
nv set qos pfc <profile-id> tx (enable|disable)
nv set qos pfc <profile-id> rx (enable|disable)
nv set qos mapping <profile-id>
nv set qos mapping <profile-id> pcp <qos-pcp-id>
nv set qos mapping <profile-id> pcp <qos-pcp-id> switch-priority 0-7
nv set qos mapping <profile-id> dscp <qos-dscp-id>
nv set qos mapping <profile-id> dscp <qos-dscp-id> switch-priority 0-7
nv set qos mapping <profile-id> port-default-sp 0-7
nv set qos mapping <profile-id> trust (l2|l3|port|both)
nv set qos remark <profile-id>
nv set qos remark <profile-id> switch-priority <qos-sp-id>
nv set qos remark <profile-id> switch-priority <qos-sp-id> pcp 0-7
nv set qos remark <profile-id> switch-priority <qos-sp-id> dscp 0-63
nv set qos remark <profile-id> rewrite (l2|l3|both)
nv set qos congestion-control <profile-id>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> min-threshold <value>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> max-threshold <value>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> probability 0-100
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> red (enable|disable)
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> ecn (enable|disable)
nv set qos egress-queue-mapping <profile-id>
nv set qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id>
nv set qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id> traffic-class 0-7
nv set qos egress-scheduler <profile-id>
nv set qos egress-scheduler <profile-id> traffic-class <qos-tc-id>
nv set qos egress-scheduler <profile-id> traffic-class <qos-tc-id> mode (dwrr|strict)
nv set qos egress-scheduler <profile-id> traffic-class <qos-tc-id> bw-percent 0-100
nv set qos egress-shaper <profile-id>
nv set qos egress-shaper <profile-id> traffic-class <qos-tc-id>
nv set qos egress-shaper <profile-id> traffic-class <qos-tc-id> min-rate 0-2147483647
nv set qos egress-shaper <profile-id> traffic-class <qos-tc-id> max-rate 0-2147483647
nv set qos egress-shaper <profile-id> port-max-rate 0-2147483647
nv set qos roce
nv set qos roce enable (on|off)
nv set qos roce mode (lossy|lossless)
nv set interface <interface-id>
nv set interface <interface-id> ip
nv set interface <interface-id> ip address <ip-prefix-id>
nv set interface <interface-id> ip gateway <ip-address-id>
nv set interface <interface-id> ip ipv4
nv set interface <interface-id> ip ipv4 forward (on|off)
nv set interface <interface-id> ip ipv6
nv set interface <interface-id> ip ipv6 enable (on|off)
nv set interface <interface-id> ip ipv6 forward (on|off)
nv set interface <interface-id> ip vrr
nv set interface <interface-id> ip vrr address <ip-prefix-id>
nv set interface <interface-id> ip vrr state (up|down)
nv set interface <interface-id> ip vrr enable (on|off)
nv set interface <interface-id> ip vrr mac-id (1-255|none)
nv set interface <interface-id> ip vrr mac-address (auto|<mac>)
nv set interface <interface-id> ip igmp
nv set interface <interface-id> ip igmp static-group <static-group-id> source-address
nv set interface <interface-id> ip igmp enable (on|off)
nv set interface <interface-id> ip igmp version (2|3)
nv set interface <interface-id> ip igmp query-interval 1-1800
nv set interface <interface-id> ip igmp query-max-response-time 10-250
nv set interface <interface-id> ip igmp last-member-query-interval 1-255
nv set interface <interface-id> ip vrrp
nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id>
nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>
nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> version (2|3)
nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> priority (1-254|auto)
nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt (on|off|auto)
nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> advertisement-interval (10-40950|auto)
nv set interface <interface-id> ip vrrp enable (on|off)
nv set interface <interface-id> ip neighbor-discovery
nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>
nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime (0-4294967295|infinite)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime (0-4294967295|infinite)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime (0-4294967295|infinite)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link (on|off)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig (on|off)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address (on|off)
nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>
nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime (0-4294967295|infinite)
nv set interface <interface-id> ip neighbor-discovery router-advertisement
nv set interface <interface-id> ip neighbor-discovery router-advertisement enable (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement interval 70-1800000
nv set interface <interface-id> ip neighbor-discovery router-advertisement interval-option (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime 0-9000
nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time 0-3600000
nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time 0-4294967295
nv set interface <interface-id> ip neighbor-discovery router-advertisement managed-config (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement other-config (on|off)
nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit 0-255
nv set interface <interface-id> ip neighbor-discovery router-advertisement router-preference (high|medium|low)
nv set interface <interface-id> ip neighbor-discovery home-agent
nv set interface <interface-id> ip neighbor-discovery home-agent enable (on|off)
nv set interface <interface-id> ip neighbor-discovery home-agent lifetime 0-65520
nv set interface <interface-id> ip neighbor-discovery home-agent preference 0-65535
nv set interface <interface-id> ip neighbor-discovery enable (on|off)
nv set interface <interface-id> ip neighbor-discovery mtu 1-65535
nv set interface <interface-id> ip vrf <vrf-name>
nv set interface <interface-id> link
nv set interface <interface-id> link state (up|down)
nv set interface <interface-id> link breakout <mode-id>
nv set interface <interface-id> link breakout <mode-id> lanes-per-port (1|2|4|8)
nv set interface <interface-id> link auto-negotiate (on|off)
nv set interface <interface-id> link duplex (half|full)
nv set interface <interface-id> link lanes (1|2|4|8)
nv set interface <interface-id> link speed (auto|10M|100M|1G|10G|25G|40G|50G|100G|200G|400G|800G)
nv set interface <interface-id> link fec (auto|baser|off|rs|driver-auto)
nv set interface <interface-id> link mtu 552-9216
nv set interface <interface-id> link fast-linkup (on|off)
nv set interface <interface-id> router
nv set interface <interface-id> router pbr
nv set interface <interface-id> router pbr map <pbr-map-id>
nv set interface <interface-id> router ospf
nv set interface <interface-id> router ospf timers
nv set interface <interface-id> router ospf timers dead-interval (1-65535|minimal)
nv set interface <interface-id> router ospf timers hello-multiplier 1-10
nv set interface <interface-id> router ospf timers hello-interval 1-65535
nv set interface <interface-id> router ospf timers retransmit-interval 1-65535
nv set interface <interface-id> router ospf timers transmit-delay 1-65535
nv set interface <interface-id> router ospf authentication
nv set interface <interface-id> router ospf authentication enable (on|off)
nv set interface <interface-id> router ospf authentication message-digest-key 1-255
nv set interface <interface-id> router ospf authentication md5-key <value>
nv set interface <interface-id> router ospf bfd
nv set interface <interface-id> router ospf bfd enable (on|off)
nv set interface <interface-id> router ospf bfd detect-multiplier 2-255
nv set interface <interface-id> router ospf bfd min-receive-interval 50-60000
nv set interface <interface-id> router ospf bfd min-transmit-interval 50-60000
nv set interface <interface-id> router ospf enable (on|off)
nv set interface <interface-id> router ospf area (0-4294967295|none|<ipv4>)
nv set interface <interface-id> router ospf cost (1-65535|auto)
nv set interface <interface-id> router ospf mtu-ignore (on|off)
nv set interface <interface-id> router ospf network-type (broadcast|non-broadcast|point-to-multipoint|point-to-point)
nv set interface <interface-id> router ospf passive (on|off)
nv set interface <interface-id> router ospf priority 0-255
nv set interface <interface-id> router pim
nv set interface <interface-id> router pim timers
nv set interface <interface-id> router pim timers hello-interval (1-180|auto)
nv set interface <interface-id> router pim bfd
nv set interface <interface-id> router pim bfd enable (on|off)
nv set interface <interface-id> router pim bfd detect-multiplier 2-255
nv set interface <interface-id> router pim bfd min-receive-interval 50-60000
nv set interface <interface-id> router pim bfd min-transmit-interval 50-60000
nv set interface <interface-id> router pim address-family
nv set interface <interface-id> router pim address-family ipv4-unicast
nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp
nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp enable (on|off)
nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp rp-list (none|<generic-name>)
nv set interface <interface-id> router pim address-family ipv4-unicast multicast-boundary-oil (none|<generic-name>)
nv set interface <interface-id> router pim address-family ipv4-unicast use-source (none|<ipv4>)
nv set interface <interface-id> router pim enable (on|off)
nv set interface <interface-id> router pim dr-priority 1-4294967295
nv set interface <interface-id> router pim active-active (on|off)
nv set interface <interface-id> router adaptive-routing
nv set interface <interface-id> router adaptive-routing enable (on|off)
nv set interface <interface-id> router adaptive-routing link-utilization-threshold 1-100
nv set interface <interface-id> bond
nv set interface <interface-id> bond member <member-id>
nv set interface <interface-id> bond mlag
nv set interface <interface-id> bond mlag enable (on|off)
nv set interface <interface-id> bond mlag id (1-65535|auto)
nv set interface <interface-id> bond mlag lacp-conflict
nv set interface <interface-id> bond down-delay 0-65535
nv set interface <interface-id> bond lacp-bypass (on|off)
nv set interface <interface-id> bond lacp-rate (fast|slow)
nv set interface <interface-id> bond mode (lacp|static)
nv set interface <interface-id> bond up-delay 0-65535
nv set interface <interface-id> bridge
nv set interface <interface-id> bridge domain <domain-id>
nv set interface <interface-id> bridge domain <domain-id> stp
nv set interface <interface-id> bridge domain <domain-id> stp bpdu-filter (on|off)
nv set interface <interface-id> bridge domain <domain-id> stp bpdu-guard (on|off)
nv set interface <interface-id> bridge domain <domain-id> stp admin-edge (on|off)
nv set interface <interface-id> bridge domain <domain-id> stp auto-edge (on|off)
nv set interface <interface-id> bridge domain <domain-id> stp network (on|off)
nv set interface <interface-id> bridge domain <domain-id> stp restrrole (on|off)
nv set interface <interface-id> bridge domain <domain-id> vlan <vid>
nv set interface <interface-id> bridge domain <domain-id> learning (on|off)
nv set interface <interface-id> bridge domain <domain-id> untagged (1-4094|none|auto)
nv set interface <interface-id> bridge domain <domain-id> access (1-4094|auto)
nv set interface <interface-id> lldp
nv set interface <interface-id> lldp dcbx-pfc-tlv (on|off)
nv set interface <interface-id> lldp dcbx-ets-config-tlv (on|off)
nv set interface <interface-id> lldp dcbx-ets-recomm-tlv (on|off)
nv set interface <interface-id> qos
nv set interface <interface-id> qos pfc
nv set interface <interface-id> qos pfc profile <profile-name>
nv set interface <interface-id> qos link-pause
nv set interface <interface-id> qos link-pause profile <profile-name>
nv set interface <interface-id> qos mapping
nv set interface <interface-id> qos mapping profile <profile-name>
nv set interface <interface-id> qos remark
nv set interface <interface-id> qos remark profile <profile-name>
nv set interface <interface-id> qos congestion-control
nv set interface <interface-id> qos congestion-control profile <profile-name>
nv set interface <interface-id> qos egress-scheduler
nv set interface <interface-id> qos egress-scheduler profile <profile-name>
nv set interface <interface-id> qos egress-shaper
nv set interface <interface-id> qos egress-shaper profile <profile-name>
nv set interface <interface-id> evpn
nv set interface <interface-id> evpn multihoming
nv set interface <interface-id> evpn multihoming segment
nv set interface <interface-id> evpn multihoming segment enable (on|off)
nv set interface <interface-id> evpn multihoming segment local-id 1-16777215
nv set interface <interface-id> evpn multihoming segment identifier <es-identifier>
nv set interface <interface-id> evpn multihoming segment mac-address (auto|<mac>)
nv set interface <interface-id> evpn multihoming segment df-preference (1-65535|auto)
nv set interface <interface-id> evpn multihoming uplink (on|off)
nv set interface <interface-id> acl <acl-id>
nv set interface <interface-id> acl <acl-id> inbound
nv set interface <interface-id> acl <acl-id> inbound control-plane
nv set interface <interface-id> acl <acl-id> outbound
nv set interface <interface-id> acl <acl-id> outbound control-plane
nv set interface <interface-id> ptp
nv set interface <interface-id> ptp timers
nv set interface <interface-id> ptp timers announce-interval -3-4
nv set interface <interface-id> ptp timers sync-interval -7-1
nv set interface <interface-id> ptp timers delay-req-interval -7-6
nv set interface <interface-id> ptp timers announce-timeout 2-10
nv set interface <interface-id> ptp enable (on|off)
nv set interface <interface-id> ptp instance 1-16
nv set interface <interface-id> ptp forced-master (on|off)
nv set interface <interface-id> ptp acceptable-master (on|off)
nv set interface <interface-id> ptp delay-mechanism end-to-end
nv set interface <interface-id> ptp transport (ipv4|ipv6|802.3)
nv set interface <interface-id> ptp ttl 1-255
nv set interface <interface-id> ptp mixed-multicast-unicast (on|off)
nv set interface <interface-id> ptp unicast-service-mode (client|server)
nv set interface <interface-id> ptp unicast-request-duration 10-1000
nv set interface <interface-id> ptp unicast-master-table-id <integer>
nv set interface <interface-id> tunnel
nv set interface <interface-id> tunnel source-ip <ipv4>
nv set interface <interface-id> tunnel dest-ip <ipv4>
nv set interface <interface-id> tunnel ttl 1-255
nv set interface <interface-id> tunnel mode gre
nv set interface <interface-id> tunnel interface <interface-name>
nv set interface <interface-id> storm-control
nv set interface <interface-id> storm-control broadcast 1-4294967295
nv set interface <interface-id> storm-control multicast 1-4294967295
nv set interface <interface-id> storm-control unknown-unicast 1-4294967295
nv set interface <interface-id> synce
nv set interface <interface-id> synce enable (on|off)
nv set interface <interface-id> synce provider-priority 1-255
nv set interface <interface-id> type (swp|eth|bond|loopback|svi|sub|peerlink|tunnel|bridge|vrf)
nv set interface <interface-id> base-interface (none|<interface-name>)
nv set interface <interface-id> vlan 1-4094
nv set interface <interface-id> description <value>
nv set service
nv set service dhcp-server <vrf-id>
nv set service dhcp-server <vrf-id> interface <interface-id>
nv set service dhcp-server <vrf-id> pool <pool-id>
nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>
nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>
nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name <idn-hostname>
nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>
nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id>
nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to <ipv4>
nv set service dhcp-server <vrf-id> pool <pool-id> pool-name <value>
nv set service dhcp-server <vrf-id> pool <pool-id> lease-time 180-31536000
nv set service dhcp-server <vrf-id> pool <pool-id> ping-check (on|off)
nv set service dhcp-server <vrf-id> pool <pool-id> default-url <value>
nv set service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url <value>
nv set service dhcp-server <vrf-id> domain-name <domain-name-id>
nv set service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name <idn-hostname>
nv set service dhcp-server <vrf-id> domain-name-server <server-id>
nv set service dhcp-server <vrf-id> static <static-id>
nv set service dhcp-server <vrf-id> static <static-id> mac-address <mac>
nv set service dhcp-server <vrf-id> static <static-id> ip-address <ipv4>
nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url <value>
nv set service dhcp-server <vrf-id> static <static-id> host-id-circuit-id <value>
nv set service dhcp-server6 <vrf-id>
nv set service dhcp-server6 <vrf-id> interface <interface-id>
nv set service dhcp-server6 <vrf-id> pool <pool-id>
nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>
nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>
nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name <idn-hostname>
nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>
nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to <ipv6>
nv set service dhcp-server6 <vrf-id> pool <pool-id> pool-name <value>
nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time 180-31536000
nv set service dhcp-server6 <vrf-id> pool <pool-id> ping-check (on|off)
nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url <value>
nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url <value>
nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id>
nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name <idn-hostname>
nv set service dhcp-server6 <vrf-id> domain-name-server <server-id>
nv set service dhcp-server6 <vrf-id> static <static-id>
nv set service dhcp-server6 <vrf-id> static <static-id> mac-address <mac>
nv set service dhcp-server6 <vrf-id> static <static-id> ip-address <ipv6>
nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url <value>
nv set service dns <vrf-id>
nv set service dns <vrf-id> server <dns-server-id>
nv set service syslog <vrf-id>
nv set service syslog <vrf-id> server <server-id>
nv set service syslog <vrf-id> server <server-id> port 1-32767
nv set service syslog <vrf-id> server <server-id> protocol (tcp|udp)
nv set service ntp <vrf-id>
nv set service ntp <vrf-id> server <server-id>
nv set service ntp <vrf-id> server <server-id> iburst (on|off)
nv set service ntp <vrf-id> pool <server-id>
nv set service ntp <vrf-id> pool <server-id> iburst (on|off)
nv set service ntp <vrf-id> listen <interface-name>
nv set service dhcp-relay <vrf-id>
nv set service dhcp-relay <vrf-id> server <server-id>
nv set service dhcp-relay <vrf-id> interface <interface-id>
nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id>
nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id> address (auto|<ipv4>)
nv set service dhcp-relay <vrf-id> source-ip (auto|giaddress)
nv set service dhcp-relay6 <vrf-id>
nv set service dhcp-relay6 <vrf-id> interface
nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id>
nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address <ipv6>
nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id>
nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address <ipv6>
nv set service snmp-server
nv set service snmp-server listening-address <listening-address-id>
nv set service snmp-server listening-address <listening-address-id> vrf <vrf-name>
nv set service snmp-server username <username-id>
nv set service snmp-server username <username-id> auth-none
nv set service snmp-server username <username-id> auth-none oid <oid>
nv set service snmp-server username <username-id> auth-none view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> view <value>
nv set service snmp-server mibs (cumulus-sensor-mib|cumulus-status-mib)
nv set service snmp-server viewname <viewname-id>
nv set service snmp-server viewname <viewname-id> excluded <snmp-branch>
nv set service snmp-server viewname <viewname-id> included <snmp-branch>
nv set service snmp-server readonly-community <readonly-community-id>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id> oid <oid>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id> view <value>
nv set service snmp-server readonly-community-v6 <readonly-community-id>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> oid <oid>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> view <value>
nv set service snmp-server trap-link-down
nv set service snmp-server trap-link-down check-frequency 5-300
nv set service snmp-server trap-link-up
nv set service snmp-server trap-link-up check-frequency 5-300
nv set service snmp-server trap-snmp-auth-failures
nv set service snmp-server trap-cpu-load-average
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id>
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id>
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute <fifteen-minute-id>
nv set service snmp-server trap-destination <trap-destination-id>
nv set service snmp-server trap-destination <trap-destination-id> community-password <community-password-id>
nv set service snmp-server trap-destination <trap-destination-id> community-password <community-password-id> version (1|2c)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id> version (1|2c)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server enable (on|off)
nv set service snmp-server system-contact <value>
nv set service snmp-server system-location <value>
nv set service snmp-server system-name <value>
nv set service synce
nv set service synce enable (on|off)
nv set service synce wait-to-restore-time 1-720
nv set service synce log-level (info|debug)
nv set service synce provider-default-priority 1-256
nv set service ptp <instance-id>
nv set service ptp <instance-id> acceptable-master <clock-id>
nv set service ptp <instance-id> acceptable-master <clock-id> alt-priority 0-255
nv set service ptp <instance-id> unicast-master <table-id>
nv set service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv set service ptp <instance-id> unicast-master <table-id> query-interval -3-4
nv set service ptp <instance-id> unicast-master <table-id> peer-address (<ipv4>|<ipv6>)
nv set service ptp <instance-id> profile <profile-id>
nv set service ptp <instance-id> profile <profile-id> profile-type (ieee-1588|itu-g-8275-1)
nv set service ptp <instance-id> profile <profile-id> priority1 0-255
nv set service ptp <instance-id> profile <profile-id> priority2 0-255
nv set service ptp <instance-id> profile <profile-id> local-priority 0-255
nv set service ptp <instance-id> profile <profile-id> domain 0-255
nv set service ptp <instance-id> profile <profile-id> delay-mechanism end-to-end
nv set service ptp <instance-id> profile <profile-id> transport (ipv4|ipv6|802.3)
nv set service ptp <instance-id> profile <profile-id> announce-interval -7-7
nv set service ptp <instance-id> profile <profile-id> sync-interval -7-7
nv set service ptp <instance-id> profile <profile-id> delay-req-interval -7-7
nv set service ptp <instance-id> profile <profile-id> announce-timeout 2-255
nv set service ptp <instance-id> monitor
nv set service ptp <instance-id> monitor min-offset-threshold -1000000000-0
nv set service ptp <instance-id> monitor max-offset-threshold 0-1000000000
nv set service ptp <instance-id> monitor path-delay-threshold 0-1000000000
nv set service ptp <instance-id> monitor max-timestamp-entries 100-200
nv set service ptp <instance-id> monitor max-violation-log-sets 2-4
nv set service ptp <instance-id> monitor max-violation-log-entries 4-8
nv set service ptp <instance-id> monitor violation-log-interval 0-60
nv set service ptp <instance-id> enable (on|off)
nv set service ptp <instance-id> current-profile <value>
nv set service ptp <instance-id> priority1 0-255
nv set service ptp <instance-id> priority2 0-255
nv set service ptp <instance-id> domain 0-127
nv set service ptp <instance-id> ip-dscp 0-63
nv set service lldp
nv set service lldp tx-interval 10-300
nv set service lldp tx-hold-multiplier 1-10
nv set service lldp dot1-tlv (on|off)
nv set service lldp mode (default|force-send-cdpv1|force-send-cdpv2|force-send-lldp)
nv set system
nv set system message
nv set system message pre-login <value>
nv set system message post-login <value>
nv set system config
nv set system config auto-save
nv set system config auto-save enable (on|off)
nv set system config apply
nv set system config apply ignore <ignore-id>
nv set system config apply overwrite (all|controlled)
nv set system acl
nv set system acl mode (atomic|non-atomic)
nv set system counter
nv set system counter polling-interval
nv set system counter polling-interval logical-interface 1-30
nv set system counter polling-interval physical-interface 1-10
nv set system control-plane
nv set system control-plane trap <trap-id>
nv set system control-plane trap <trap-id> state (on|off)
nv set system control-plane policer <policer-id>
nv set system control-plane policer <policer-id> state (on|off)
nv set system control-plane policer <policer-id> burst 10-10000
nv set system control-plane policer <policer-id> rate 10-50000
nv set system global
nv set system global reserved
nv set system global reserved routing-table
nv set system global reserved routing-table pbr
nv set system global reserved routing-table pbr begin 10000-4294966272
nv set system global reserved routing-table pbr end 10000-4294966272
nv set system global reserved vlan
nv set system global reserved vlan internal
nv set system global reserved vlan internal range <vlan-range>
nv set system global reserved vlan l3-vni-vlan
nv set system global reserved vlan l3-vni-vlan begin 1-4093
nv set system global reserved vlan l3-vni-vlan end 2-4093
nv set system global system-mac (auto|<mac>)
nv set system global anycast-mac (none|<mac>)
nv set system global anycast-id (1-65535|none)
nv set system global fabric-mac (none|<mac>)
nv set system global fabric-id 1-255
nv set system forwarding
nv set system forwarding lag-hash
nv set system forwarding lag-hash ip-protocol (on|off)
nv set system forwarding lag-hash source-mac (on|off)
nv set system forwarding lag-hash destination-mac (on|off)
nv set system forwarding lag-hash source-ip (on|off)
nv set system forwarding lag-hash destination-ip (on|off)
nv set system forwarding lag-hash source-port (on|off)
nv set system forwarding lag-hash destination-port (on|off)
nv set system forwarding lag-hash ether-type (on|off)
nv set system forwarding lag-hash vlan (on|off)
nv set system forwarding lag-hash gtp-teid (on|off)
nv set system forwarding ecmp-hash
nv set system forwarding ecmp-hash ip-protocol (on|off)
nv set system forwarding ecmp-hash source-ip (on|off)
nv set system forwarding ecmp-hash destination-ip (on|off)
nv set system forwarding ecmp-hash source-port (on|off)
nv set system forwarding ecmp-hash destination-port (on|off)
nv set system forwarding ecmp-hash ipv6-label (on|off)
nv set system forwarding ecmp-hash ingress-interface (on|off)
nv set system forwarding ecmp-hash gtp-teid (on|off)
nv set system forwarding ecmp-hash inner-ip-protocol (on|off)
nv set system forwarding ecmp-hash inner-source-ip (on|off)
nv set system forwarding ecmp-hash inner-destination-ip (on|off)
nv set system forwarding ecmp-hash inner-source-port (on|off)
nv set system forwarding ecmp-hash inner-destination-port (on|off)
nv set system forwarding ecmp-hash inner-ipv6-label (on|off)
nv set system forwarding programming
nv set system forwarding programming log-level (debug|info|critical|warning|error)
nv set system forwarding hash-seed 0-4294967295
nv set system forwarding host-route-preference (route|neighbour|route-and-neighbour)
nv set system forwarding profile (default|l2-heavy|l2-heavy-1|l2-heavy-3|v4-lpm-heavy|v4-lpm-heavy-1|v6-lpm-heavy|v6-lpm-heavy-1|ipmc-heavy|ipmc-max|lpm-balanced)
nv set system port-mirror
nv set system port-mirror session <session-id>
nv set system port-mirror session <session-id> span
nv set system port-mirror session <session-id> span source-port <port-id>
nv set system port-mirror session <session-id> span destination <port-id>
nv set system port-mirror session <session-id> span truncate
nv set system port-mirror session <session-id> span truncate enable (on|off)
nv set system port-mirror session <session-id> span truncate size (4-4088|none)
nv set system port-mirror session <session-id> span enable (on|off)
nv set system port-mirror session <session-id> span direction (ingress|egress)
nv set system port-mirror session <session-id> erspan
nv set system port-mirror session <session-id> erspan source-port <port-id>
nv set system port-mirror session <session-id> erspan destination
nv set system port-mirror session <session-id> erspan destination source-ip <source-ip>
nv set system port-mirror session <session-id> erspan destination dest-ip <dest-ip>
nv set system port-mirror session <session-id> erspan truncate
nv set system port-mirror session <session-id> erspan truncate enable (on|off)
nv set system port-mirror session <session-id> erspan truncate size (4-4088|none)
nv set system port-mirror session <session-id> erspan enable (on|off)
nv set system port-mirror session <session-id> erspan direction (ingress|egress)
nv set system wjh
nv set system wjh channel <channel-id>
nv set system wjh channel <channel-id> trigger (l1|l2|l3|tunnel)
nv set system wjh enable (on|off)
nv set system aaa
nv set system aaa user <user-id>
nv set system aaa user <user-id> ssh
nv set system aaa user <user-id> ssh authorized-key <ssh-authorized-key-id>
nv set system aaa user <user-id> ssh authorized-key <ssh-authorized-key-id> key <key-string>
nv set system aaa user <user-id> ssh authorized-key <ssh-authorized-key-id> type (ecdsa-sha2-nistp256|ecdsa-sha2-nistp384|ecdsa-sha2-nistp521|ssh-ed25519|ssh-dss|ssh-rsa)
nv set system aaa user <user-id> role (system-admin|nvue-admin|nvue-monitor)
nv set system aaa user <user-id> full-name <value>
nv set system aaa user <user-id> password <value>
nv set system aaa user <user-id> hashed-password <value>
nv set system aaa user <user-id> enable (on|off)
nv set system aaa authentication-order <priority-id> (tacacs|local)
nv set system aaa tacacs
nv set system aaa tacacs authentication
nv set system aaa tacacs authentication mode (pap|chap|login)
nv set system aaa tacacs authentication per-user-homedir (on|off)
nv set system aaa tacacs accounting
nv set system aaa tacacs accounting enable (on|off)
nv set system aaa tacacs accounting send-records (all|first-response)
nv set system aaa tacacs server <priority-id>
nv set system aaa tacacs server <priority-id> host (<idn-hostname>|<ipv4>)
nv set system aaa tacacs server <priority-id> port 0-65535
nv set system aaa tacacs server <priority-id> secret <value>
nv set system aaa tacacs exclude-user
nv set system aaa tacacs exclude-user username <value>
nv set system aaa tacacs enable (on|off)
nv set system aaa tacacs timeout 0-60
nv set system aaa tacacs debug-level 0-2
nv set system aaa tacacs source-ip <ipv4>
nv set system aaa tacacs vrf <vrf-name>
nv set system hostname <idn-hostname>
nv set system timezone (Africa/Abidjan|Africa/Accra|Africa/Addis_Ababa|Africa/Algiers|Africa/Asmara|Africa/Bamako|Africa/Bangui|Africa/Banjul|Africa/Bissau|Africa/Blantyre|Africa/Brazzaville|Africa/Bujumbura|Africa/Cairo|Africa/Casablanca|Africa/Ceuta|Africa/Conakry|Africa/Dakar|Africa/Dar_es_Salaam|Africa/Djibouti|Africa/Douala|Africa/El_Aaiun|Africa/Freetown|Africa/Gaborone|Africa/Harare|Africa/Johannesburg|Africa/Juba|Africa/Kampala|Africa/Khartoum|Africa/Kigali|Africa/Kinshasa|Africa/Lagos|Africa/Libreville|Africa/Lome|Africa/Luanda|Africa/Lubumbashi|Africa/Lusaka|Africa/Malabo|Africa/Maputo|Africa/Maseru|Africa/Mbabane|Africa/Mogadishu|Africa/Monrovia|Africa/Nairobi|Africa/Ndjamena|Africa/Niamey|Africa/Nouakchott|Africa/Ouagadougou|Africa/Porto-Novo|Africa/Sao_Tome|Africa/Timbuktu|Africa/Tripoli|Africa/Tunis|Africa/Windhoek|America/Adak|America/Anchorage|America/Anguilla|America/Antigua|America/Araguaina|America/Argentina/Buenos_Aires|America/Argentina/Catamarca|America/Argentina/ComodRivadavia|America/Argentina/Cordoba|America/Argentina/Jujuy|America/Argentina/La_Rioja|America/Argentina/Mendoza|America/Argentina/Rio_Gallegos|America/Argentina/Salta|America/Argentina/San_Juan|America/Argentina/San_Luis|America/Argentina/Tucuman|America/Argentina/Ushuaia|America/Aruba|America/Asuncion|America/Atikokan|America/Atka|America/Bahia|America/Bahia_Banderas|America/Barbados|America/Belem|America/Belize|America/Blanc-Sablon|America/Boa_Vista|America/Bogota|America/Boise|America/Buenos_Aires|America/Cambridge_Bay|America/Campo_Grande|America/Cancun|America/Caracas|America/Catamarca|America/Cayenne|America/Cayman|America/Chicago|America/Chihuahua|America/Coral_Harbour|America/Cordoba|America/Costa_Rica|America/Creston|America/Cuiaba|America/Curacao|America/Danmarkshavn|America/Dawson|America/Dawson_Creek|America/Denver|America/Detroit|America/Dominica|America/Edmonton|America/Eirunepe|America/El_Salvador|America/Ensenada|America/Fort_Nelson|America/Fort_Wayne|America/Fortaleza|America/Glace_Bay|America/Godthab|America/Goose_Bay|America/Grand_Turk|America/Grenada|America/Guadeloupe|America/Guatemala|America/Guayaquil|America/Guyana|America/Halifax|America/Havana|America/Hermosillo|America/Indiana/Indianapolis|America/Indiana/Knox|America/Indiana/Marengo|America/Indiana/Petersburg|America/Indiana/Tell_City|America/Indiana/Vevay|America/Indiana/Vincennes|America/Indiana/Winamac|America/Indianapolis|America/Inuvik|America/Iqaluit|America/Jamaica|America/Jujuy|America/Juneau|America/Kentucky/Louisville|America/Kentucky/Monticello|America/Knox_IN|America/Kralendijk|America/La_Paz|America/Lima|America/Los_Angeles|America/Louisville|America/Lower_Princes|America/Maceio|America/Managua|America/Manaus|America/Marigot|America/Martinique|America/Matamoros|America/Mazatlan|America/Mendoza|America/Menominee|America/Merida|America/Metlakatla|America/Mexico_City|America/Miquelon|America/Moncton|America/Monterrey|America/Montevideo|America/Montreal|America/Montserrat|America/Nassau|America/New_York|America/Nipigon|America/Nome|America/Noronha|America/North_Dakota/Beulah|America/North_Dakota/Center|America/North_Dakota/New_Salem|America/Ojinaga|America/Panama|America/Pangnirtung|America/Paramaribo|America/Phoenix|America/Port-au-Prince|America/Port_of_Spain|America/Porto_Acre|America/Porto_Velho|America/Puerto_Rico|America/Rainy_River|America/Rankin_Inlet|America/Recife|America/Regina|America/Resolute|America/Rio_Branco|America/Rosario|America/Santa_Isabel|America/Santarem|America/Santiago|America/Santo_Domingo|America/Sao_Paulo|America/Scoresbysund|America/Shiprock|America/Sitka|America/St_Barthelemy|America/St_Johns|America/St_Kitts|America/St_Lucia|America/St_Thomas|America/St_Vincent|America/Swift_Current|America/Tegucigalpa|America/Thule|America/Thunder_Bay|America/Tijuana|America/Toronto|America/Tortola|America/Vancouver|America/Virgin|America/Whitehorse|America/Winnipeg|America/Yakutat|America/Yellowknife|Antarctica/Casey|Antarctica/Davis|Antarctica/DumontDUrville|Antarctica/Macquarie|Antarctica/Mawson|Antarctica/McMurdo|Antarctica/Palmer|Antarctica/Rothera|Antarctica/South_Pole|Antarctica/Syowa|Antarctica/Troll|Antarctica/Vostok|Arctic/Longyearbyen|Asia/Aden|Asia/Almaty|Asia/Amman|Asia/Anadyr|Asia/Aqtau|Asia/Aqtobe|Asia/Ashgabat|Asia/Ashkhabad|Asia/Atyrau|Asia/Baghdad|Asia/Bahrain|Asia/Baku|Asia/Bangkok|Asia/Barnaul|Asia/Beirut|Asia/Bishkek|Asia/Brunei|Asia/Calcutta|Asia/Chita|Asia/Choibalsan|Asia/Chongqing|Asia/Chungking|Asia/Colombo|Asia/Dacca|Asia/Damascus|Asia/Dhaka|Asia/Dili|Asia/Dubai|Asia/Dushanbe|Asia/Famagusta|Asia/Gaza|Asia/Harbin|Asia/Hebron|Asia/Ho_Chi_Minh|Asia/Hong_Kong|Asia/Hovd|Asia/Irkutsk|Asia/Istanbul|Asia/Jakarta|Asia/Jayapura|Asia/Jerusalem|Asia/Kabul|Asia/Kamchatka|Asia/Karachi|Asia/Kashgar|Asia/Kathmandu|Asia/Katmandu|Asia/Khandyga|Asia/Kolkata|Asia/Krasnoyarsk|Asia/Kuala_Lumpur|Asia/Kuching|Asia/Kuwait|Asia/Macao|Asia/Macau|Asia/Magadan|Asia/Makassar|Asia/Manila|Asia/Muscat|Asia/Nicosia|Asia/Novokuznetsk|Asia/Novosibirsk|Asia/Omsk|Asia/Oral|Asia/Phnom_Penh|Asia/Pontianak|Asia/Pyongyang|Asia/Qatar|Asia/Qyzylorda|Asia/Rangoon|Asia/Riyadh|Asia/Saigon|Asia/Sakhalin|Asia/Samarkand|Asia/Seoul|Asia/Shanghai|Asia/Singapore|Asia/Srednekolymsk|Asia/Taipei|Asia/Tashkent|Asia/Tbilisi|Asia/Tehran|Asia/Tel_Aviv|Asia/Thimbu|Asia/Thimphu|Asia/Tokyo|Asia/Tomsk|Asia/Ujung_Pandang|Asia/Ulaanbaatar|Asia/Ulan_Bator|Asia/Urumqi|Asia/Ust-Nera|Asia/Vientiane|Asia/Vladivostok|Asia/Yakutsk|Asia/Yangon|Asia/Yekaterinburg|Asia/Yerevan|Atlantic/Azores|Atlantic/Bermuda|Atlantic/Canary|Atlantic/Cape_Verde|Atlantic/Faeroe|Atlantic/Faroe|Atlantic/Jan_Mayen|Atlantic/Madeira|Atlantic/Reykjavik|Atlantic/South_Georgia|Atlantic/St_Helena|Atlantic/Stanley|Australia/ACT|Australia/Adelaide|Australia/Brisbane|Australia/Broken_Hill|Australia/Canberra|Australia/Currie|Australia/Darwin|Australia/Eucla|Australia/Hobart|Australia/LHI|Australia/Lindeman|Australia/Lord_Howe|Australia/Melbourne|Australia/NSW|Australia/North|Australia/Perth|Australia/Queensland|Australia/South|Australia/Sydney|Australia/Tasmania|Australia/Victoria|Australia/West|Australia/Yancowinna|Brazil/Acre|Brazil/DeNoronha|Brazil/East|Brazil/West|Canada/Atlantic|Canada/Central|Canada/East-Saskatchewan|Canada/Eastern|Canada/Mountain|Canada/Newfoundland|Canada/Pacific|Canada/Saskatchewan|Canada/Yukon|Chile/Continental|Chile/EasterIsland|Etc/GMT|Etc/GMT0|Etc/GMT+0|Etc/GMT+1|Etc/GMT+2|Etc/GMT+3|Etc/GMT+4|Etc/GMT+5|Etc/GMT+6|Etc/GMT+7|Etc/GMT+8|Etc/GMT+9|Etc/GMT+10|Etc/GMT+11|Etc/GMT+12|Etc/GMT-0|Etc/GMT-1|Etc/GMT-2|Etc/GMT-3|Etc/GMT-4|Etc/GMT-5|Etc/GMT-6|Etc/GMT-7|Etc/GMT-8|Etc/GMT-9|Etc/GMT-10|Etc/GMT-11|Etc/GMT-12|Etc/GMT-13|Etc/GMT-14|Etc/Greenwich|Etc/UTC|Etc/Universal|Etc/Zulu|Europe/Amsterdam|Europe/Andorra|Europe/Astrakhan|Europe/Athens|Europe/Belfast|Europe/Belgrade|Europe/Berlin|Europe/Bratislava|Europe/Brussels|Europe/Bucharest|Europe/Budapest|Europe/Busingen|Europe/Chisinau|Europe/Copenhagen|Europe/Dublin|Europe/Gibraltar|Europe/Guernsey|Europe/Helsinki|Europe/Isle_of_Man|Europe/Istanbul|Europe/Jersey|Europe/Kaliningrad|Europe/Kiev|Europe/Kirov|Europe/Lisbon|Europe/Ljubljana|Europe/London|Europe/Luxembourg|Europe/Madrid|Europe/Malta|Europe/Mariehamn|Europe/Minsk|Europe/Monaco|Europe/Moscow|Europe/Nicosia|Europe/Oslo|Europe/Paris|Europe/Podgorica|Europe/Prague|Europe/Riga|Europe/Rome|Europe/Samara|Europe/San_Marino|Europe/Sarajevo|Europe/Saratov|Europe/Simferopol|Europe/Skopje|Europe/Sofia|Europe/Stockholm|Europe/Tallinn|Europe/Tirane|Europe/Tiraspol|Europe/Ulyanovsk|Europe/Uzhgorod|Europe/Vaduz|Europe/Vatican|Europe/Vienna|Europe/Vilnius|Europe/Volgograd|Europe/Warsaw|Europe/Zagreb|Europe/Zaporozhye|Europe/Zurich|Indian/Antananarivo|Indian/Chagos|Indian/Christmas|Indian/Cocos|Indian/Comoro|Indian/Kerguelen|Indian/Mahe|Indian/Maldives|Indian/Mauritius|Indian/Mayotte|Indian/Reunion|Mexico/BajaNorte|Mexico/BajaSur|Mexico/General|Pacific/Apia|Pacific/Auckland|Pacific/Bougainville|Pacific/Chatham|Pacific/Chuuk|Pacific/Easter|Pacific/Efate|Pacific/Enderbury|Pacific/Fakaofo|Pacific/Fiji|Pacific/Funafuti|Pacific/Galapagos|Pacific/Gambier|Pacific/Guadalcanal|Pacific/Guam|Pacific/Honolulu|Pacific/Johnston|Pacific/Kiritimati|Pacific/Kosrae|Pacific/Kwajalein|Pacific/Majuro|Pacific/Marquesas|Pacific/Midway|Pacific/Nauru|Pacific/Niue|Pacific/Norfolk|Pacific/Noumea|Pacific/Pago_Pago|Pacific/Palau|Pacific/Pitcairn|Pacific/Pohnpei|Pacific/Ponape|Pacific/Port_Moresby|Pacific/Rarotonga|Pacific/Saipan|Pacific/Samoa|Pacific/Tahiti|Pacific/Tarawa|Pacific/Tongatapu|Pacific/Truk|Pacific/Wake|Pacific/Wallis|Pacific/Yap|US/Alaska|US/Aleutian|US/Arizona|US/Central|US/East-Indiana|US/Eastern|US/Hawaii|US/Indiana-Starke|US/Michigan|US/Mountain|US/Pacific|US/Pacific-New|US/Samoa)
nv set vrf <vrf-id>
nv set vrf <vrf-id> loopback
nv set vrf <vrf-id> loopback ip
nv set vrf <vrf-id> loopback ip address <ip-prefix-id>
nv set vrf <vrf-id> evpn
nv set vrf <vrf-id> evpn vni <vni-id>
nv set vrf <vrf-id> evpn enable (on|off)
nv set vrf <vrf-id> evpn vlan (1-4094|auto)
nv set vrf <vrf-id> evpn prefix-routes-only (on|off)
nv set vrf <vrf-id> router
nv set vrf <vrf-id> router rib <afi>
nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id>
nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id> fib-filter (none|<generic-name>)
nv set vrf <vrf-id> router nexthop-tracking <afi>
nv set vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id>
nv set vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol
nv set vrf <vrf-id> router nexthop-tracking <afi> resolved-via-default (on|off)
nv set vrf <vrf-id> router bgp
nv set vrf <vrf-id> router bgp address-family
nv set vrf <vrf-id> router bgp address-family ipv4-unicast
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>
nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>
nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map <generic-name>
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map <generic-name>
nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths
nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp 1-128
nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp 1-128
nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance
nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external 1-255
nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal 1-255
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination (on|off)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast rib-filter (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast enable (on|off)
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn
nv set vrf <vrf-id> router bgp address-family l2vpn-evpn enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast
nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>
nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> summary-only (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>
nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> route-map <generic-name>
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map <generic-name>
nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths
nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp 1-128
nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp 1-128
nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance
nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external 1-255
nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal 1-255
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 enable (on|off)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 metric (0-4294967295|auto)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast rib-filter (none|<generic-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast enable (on|off)
nv set vrf <vrf-id> router bgp path-selection
nv set vrf <vrf-id> router bgp path-selection aspath
nv set vrf <vrf-id> router bgp path-selection aspath compare-lengths (on|off)
nv set vrf <vrf-id> router bgp path-selection aspath compare-confed (on|off)
nv set vrf <vrf-id> router bgp path-selection med
nv set vrf <vrf-id> router bgp path-selection med compare-always (on|off)
nv set vrf <vrf-id> router bgp path-selection med compare-deterministic (on|off)
nv set vrf <vrf-id> router bgp path-selection med compare-confed (on|off)
nv set vrf <vrf-id> router bgp path-selection med missing-as-max (on|off)
nv set vrf <vrf-id> router bgp path-selection multipath
nv set vrf <vrf-id> router bgp path-selection multipath aspath-ignore (on|off)
nv set vrf <vrf-id> router bgp path-selection multipath generate-asset (on|off)
nv set vrf <vrf-id> router bgp path-selection multipath bandwidth (bandwidth|all-paths|skip-missing|default-weight-for-missing|ignore)
nv set vrf <vrf-id> router bgp path-selection routerid-compare (on|off)
nv set vrf <vrf-id> router bgp route-reflection
nv set vrf <vrf-id> router bgp route-reflection enable (on|off)
nv set vrf <vrf-id> router bgp route-reflection cluster-id (0-4294967295|<ipv4>)
nv set vrf <vrf-id> router bgp route-reflection reflect-between-clients (on|off)
nv set vrf <vrf-id> router bgp route-reflection outbound-policy (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier 2-255
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval 50-60000
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval 50-60000
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops 1-254
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities extended-nexthop (on|off|auto)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities source-address (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart mode (auto|off|helper-only|full)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn 1-4294967295
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as prepend (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as replace (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers keepalive (0-65535|none|auto)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers hold (3-65535|none|auto)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers connection-retry (1-65535|auto)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers route-advertisement (1-600|none|auto)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise regular (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise extended (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise large (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod aspath (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod med (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod nexthop (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn origin (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences 1-10
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath replace-peer-as (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath private-as (none|remove|replace)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound maximum (0-4294967295|none)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold 1-100
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-only (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination policy (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list none
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound unsuppress-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list none
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map <generic-name>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map <generic-name>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map <generic-name>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-reflector-client (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-server-client (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft-reconfiguration (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast nexthop-setting (auto|self|force)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast add-path-tx (off|all-paths|best-per-as)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight 0-65535
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list none
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound unsuppress-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list none
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn origin (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences 1-10
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath replace-peer-as (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath private-as (none|remove|replace)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound maximum (0-4294967295|none)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold 1-100
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-only (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination policy (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise regular (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise extended (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise large (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod aspath (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod med (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod nexthop (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map <generic-name>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map <generic-name>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map <generic-name>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-reflector-client (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-server-client (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft-reconfiguration (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast nexthop-setting (auto|self|force)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast add-path-tx (off|all-paths|best-per-as)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight 0-65535
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod aspath (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod med (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod nexthop (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn origin (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences 1-10
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath replace-peer-as (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath private-as (none|remove|replace)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound unsuppress-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn enable (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-reflector-client (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-server-client (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft-reconfiguration (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn nexthop-setting (auto|self|force)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn add-path-tx (off|all-paths|best-per-as)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> password none
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> enforce-first-as (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> passive-mode (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> nexthop-connected-check (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> multihop-ttl (1-255|auto)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> description none
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> shutdown (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> update-source (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> remote-as (1-4294967295|internal|external)
nv set vrf <vrf-id> router bgp route-export
nv set vrf <vrf-id> router bgp route-export to-evpn
nv set vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>
nv set vrf <vrf-id> router bgp route-import
nv set vrf <vrf-id> router bgp route-import from-evpn
nv set vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>
nv set vrf <vrf-id> router bgp timers
nv set vrf <vrf-id> router bgp timers keepalive (0-65535|none)
nv set vrf <vrf-id> router bgp timers hold (3-65535|none)
nv set vrf <vrf-id> router bgp timers connection-retry 1-65535
nv set vrf <vrf-id> router bgp timers route-advertisement (1-600|none)
nv set vrf <vrf-id> router bgp timers conditional-advertise (5-240|none)
nv set vrf <vrf-id> router bgp confederation
nv set vrf <vrf-id> router bgp confederation member-as
nv set vrf <vrf-id> router bgp confederation id (1-4294967295|none)
nv set vrf <vrf-id> router bgp dynamic-neighbor
nv set vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id>
nv set vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id> peer-group <generic-name>
nv set vrf <vrf-id> router bgp dynamic-neighbor limit 1-5000
nv set vrf <vrf-id> router bgp neighbor <neighbor-id>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier 2-255
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval 50-60000
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval 50-60000
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities extended-nexthop (on|off|auto)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities source-address (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn 1-4294967295
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as prepend (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as replace (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart mode (auto|off|helper-only|full)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops 1-254
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod aspath (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod med (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod nexthop (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn origin (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences 1-10
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath replace-peer-as (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath private-as (none|remove|replace)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list none
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound unsuppress-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list none
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound maximum (0-4294967295|none)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold 1-100
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-only (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination policy (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise regular (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise extended (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise large (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map <generic-name>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map <generic-name>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map <generic-name>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-reflector-client (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-server-client (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft-reconfiguration (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast nexthop-setting (auto|self|force)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast add-path-tx (off|all-paths|best-per-as)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight 0-65535
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod aspath (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod med (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod nexthop (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn origin (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences 1-10
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath replace-peer-as (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath private-as (none|remove|replace)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound maximum (0-4294967295|none)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold 1-100
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-only (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination policy (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list none
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound unsuppress-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list none
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise regular (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise extended (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise large (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map <generic-name>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map <generic-name>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map <generic-name>
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-reflector-client (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-server-client (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft-reconfiguration (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast nexthop-setting (auto|self|force)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast add-path-tx (off|all-paths|best-per-as)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight 0-65535
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod aspath (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod med (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod nexthop (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn origin (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences 1-10
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath replace-peer-as (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath private-as (none|remove|replace)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound route-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound unsuppress-map (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-reflector-client (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-server-client (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft-reconfiguration (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn nexthop-setting (auto|self|force)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn add-path-tx (off|all-paths|best-per-as)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers keepalive (0-65535|none|auto)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers hold (3-65535|none|auto)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers connection-retry (1-65535|auto)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers route-advertisement (1-600|none|auto)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> password none
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> enforce-first-as (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> passive-mode (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop-connected-check (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> multihop-ttl (1-255|auto)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> description none
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> shutdown (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> update-source (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> type (numbered|unnumbered)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> peer-group (none|<generic-name>)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> remote-as (1-4294967295|auto|internal|external)
nv set vrf <vrf-id> router bgp enable (on|off)
nv set vrf <vrf-id> router bgp autonomous-system (1-4294967295|auto|leaf|spine)
nv set vrf <vrf-id> router bgp router-id (auto|<ipv4>)
nv set vrf <vrf-id> router bgp rd (none|<route-distinguisher>)
nv set vrf <vrf-id> router static <route-id>
nv set vrf <vrf-id> router static <route-id> distance <distance-id>
nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>
nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag onlink
nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> interface (auto|<interface-name>)
nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> vrf (auto|<vrf-name>)
nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> type (interface|ipv4-address|ipv6-address|blackhole|reject)
nv set vrf <vrf-id> router static <route-id> distance <distance-id> tag (1-4294967295|none)
nv set vrf <vrf-id> router static <route-id> via <via-id>
nv set vrf <vrf-id> router static <route-id> via <via-id> flag onlink
nv set vrf <vrf-id> router static <route-id> via <via-id> interface (auto|<interface-name>)
nv set vrf <vrf-id> router static <route-id> via <via-id> vrf (auto|<vrf-name>)
nv set vrf <vrf-id> router static <route-id> via <via-id> type (interface|ipv4-address|ipv6-address|blackhole|reject)
nv set vrf <vrf-id> router static <route-id> tag (1-4294967295|none)
nv set vrf <vrf-id> router static <route-id> address-family (ipv4-unicast|ipv6-unicast)
nv set vrf <vrf-id> router pim
nv set vrf <vrf-id> router pim timers
nv set vrf <vrf-id> router pim timers keep-alive (31-60000|auto)
nv set vrf <vrf-id> router pim timers rp-keep-alive (31-60000|auto)
nv set vrf <vrf-id> router pim ecmp
nv set vrf <vrf-id> router pim ecmp enable (on|off)
nv set vrf <vrf-id> router pim ecmp rebalance (on|off)
nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>
nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>
nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address <ipv4>
nv set vrf <vrf-id> router pim address-family
nv set vrf <vrf-id> router pim address-family ipv4-unicast
nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover
nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover action (immediate|infinity)
nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list <generic-name>
nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>
nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>
nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list <generic-name>
nv set vrf <vrf-id> router pim address-family ipv4-unicast ssm-prefix-list (none|<generic-name>)
nv set vrf <vrf-id> router pim address-family ipv4-unicast register-accept-list (none|<generic-name>)
nv set vrf <vrf-id> router pim address-family ipv4-unicast send-v6-secondary (on|off)
nv set vrf <vrf-id> router pim enable (on|off)
nv set vrf <vrf-id> router ospf
nv set vrf <vrf-id> router ospf area <area-id>
nv set vrf <vrf-id> router ospf area <area-id> filter-list
nv set vrf <vrf-id> router ospf area <area-id> filter-list in (none|<generic-name>)
nv set vrf <vrf-id> router ospf area <area-id> filter-list out (none|<generic-name>)
nv set vrf <vrf-id> router ospf area <area-id> range <range-id>
nv set vrf <vrf-id> router ospf area <area-id> range <range-id> suppress (on|off)
nv set vrf <vrf-id> router ospf area <area-id> range <range-id> cost (0-16777215|auto)
nv set vrf <vrf-id> router ospf area <area-id> network <network-id>
nv set vrf <vrf-id> router ospf area <area-id> type (normal|stub|totally-stub|nssa|totally-nssa)
nv set vrf <vrf-id> router ospf area <area-id> default-lsa-cost 0-16777215
nv set vrf <vrf-id> router ospf default-originate
nv set vrf <vrf-id> router ospf default-originate enable (on|off)
nv set vrf <vrf-id> router ospf default-originate metric (0-16777214|none)
nv set vrf <vrf-id> router ospf default-originate metric-type 1-2
nv set vrf <vrf-id> router ospf default-originate route-map (none|<generic-name>)
nv set vrf <vrf-id> router ospf default-originate always (on|off)
nv set vrf <vrf-id> router ospf distance
nv set vrf <vrf-id> router ospf distance external (1-255|none)
nv set vrf <vrf-id> router ospf distance inter-area (1-255|none)
nv set vrf <vrf-id> router ospf distance intra-area (1-255|none)
nv set vrf <vrf-id> router ospf max-metric
nv set vrf <vrf-id> router ospf max-metric administrative (on|off)
nv set vrf <vrf-id> router ospf max-metric on-shutdown (5-100|none)
nv set vrf <vrf-id> router ospf max-metric on-startup (5-86400|none)
nv set vrf <vrf-id> router ospf log
nv set vrf <vrf-id> router ospf log adjacency-changes (on|off|detail)
nv set vrf <vrf-id> router ospf redistribute
nv set vrf <vrf-id> router ospf redistribute static
nv set vrf <vrf-id> router ospf redistribute static enable (on|off)
nv set vrf <vrf-id> router ospf redistribute static metric (0-16777214|none)
nv set vrf <vrf-id> router ospf redistribute static metric-type 1-2
nv set vrf <vrf-id> router ospf redistribute static route-map (none|<generic-name>)
nv set vrf <vrf-id> router ospf redistribute connected
nv set vrf <vrf-id> router ospf redistribute connected enable (on|off)
nv set vrf <vrf-id> router ospf redistribute connected metric (0-16777214|none)
nv set vrf <vrf-id> router ospf redistribute connected metric-type 1-2
nv set vrf <vrf-id> router ospf redistribute connected route-map (none|<generic-name>)
nv set vrf <vrf-id> router ospf redistribute kernel
nv set vrf <vrf-id> router ospf redistribute kernel enable (on|off)
nv set vrf <vrf-id> router ospf redistribute kernel metric (0-16777214|none)
nv set vrf <vrf-id> router ospf redistribute kernel metric-type 1-2
nv set vrf <vrf-id> router ospf redistribute kernel route-map (none|<generic-name>)
nv set vrf <vrf-id> router ospf redistribute bgp
nv set vrf <vrf-id> router ospf redistribute bgp enable (on|off)
nv set vrf <vrf-id> router ospf redistribute bgp metric (0-16777214|none)
nv set vrf <vrf-id> router ospf redistribute bgp metric-type 1-2
nv set vrf <vrf-id> router ospf redistribute bgp route-map (none|<generic-name>)
nv set vrf <vrf-id> router ospf timers
nv set vrf <vrf-id> router ospf timers lsa
nv set vrf <vrf-id> router ospf timers lsa min-arrival (0-600000|auto)
nv set vrf <vrf-id> router ospf timers lsa throttle (0-5000|auto)
nv set vrf <vrf-id> router ospf timers spf
nv set vrf <vrf-id> router ospf timers spf delay (0-600000|auto)
nv set vrf <vrf-id> router ospf timers spf holdtime (0-600000|auto)
nv set vrf <vrf-id> router ospf timers spf max-holdtime (0-600000|auto)
nv set vrf <vrf-id> router ospf timers refresh (10-1800|auto)
nv set vrf <vrf-id> router ospf enable (on|off)
nv set vrf <vrf-id> router ospf reference-bandwidth 1-4294967
nv set vrf <vrf-id> router ospf rfc1583-compatible (on|off)
nv set vrf <vrf-id> router ospf router-id (auto|<ipv4>)
nv set vrf <vrf-id> ptp
nv set vrf <vrf-id> ptp enable (on|off)
nv set vrf <vrf-id> table auto
nv set nve
nv set nve vxlan
nv set nve vxlan mlag
nv set nve vxlan mlag shared-address (none|<ipv4-unicast>)
nv set nve vxlan source
nv set nve vxlan source address (auto|<ipv4>)
nv set nve vxlan flooding
nv set nve vxlan flooding head-end-replication <hrep-id>
nv set nve vxlan flooding enable (on|off)
nv set nve vxlan flooding multicast-group <ipv4-multicast>
nv set nve vxlan encapsulation
nv set nve vxlan encapsulation dscp
nv set nve vxlan encapsulation dscp action (derive|copy|set)
nv set nve vxlan encapsulation dscp value (0-63|af11|af12|af13|af21|af22|af23|af31|af32|af33|af41|af42|af43|cs1|cs2|cs3|cs4|cs5|cs6|cs7|be|ef)
nv set nve vxlan decapsulation
nv set nve vxlan decapsulation dscp
nv set nve vxlan decapsulation dscp action (derive|copy|preserve)
nv set nve vxlan enable (on|off)
nv set nve vxlan mac-learning (on|off)
nv set nve vxlan arp-nd-suppress (on|off)
nv set nve vxlan mtu 552-9216
nv set acl <acl-id>
nv set acl <acl-id> rule <rule-id>
nv set acl <acl-id> rule <rule-id> match
nv set acl <acl-id> rule <rule-id> match ip
nv set acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>
nv set acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>
nv set acl <acl-id> rule <rule-id> match ip fragment
nv set acl <acl-id> rule <rule-id> match ip ecn
nv set acl <acl-id> rule <rule-id> match ip ecn flags (tcp-cwr|tcp-ece)
nv set acl <acl-id> rule <rule-id> match ip ecn ip-ect 0-3
nv set acl <acl-id> rule <rule-id> match ip tcp
nv set acl <acl-id> rule <rule-id> match ip tcp flags (syn|ack|fin|rst|urg|psh|all|none)
nv set acl <acl-id> rule <rule-id> match ip tcp mask (syn|ack|fin|rst|urg|psh|all|none)
nv set acl <acl-id> rule <rule-id> match ip tcp state established
nv set acl <acl-id> rule <rule-id> match ip source-ip (ANY|<ipv4>|<ipv6>|<ipv4-prefix>|<ipv6-prefix>|<ipv4-netmask>|<ipv6-netmask>)
nv set acl <acl-id> rule <rule-id> match ip dest-ip (ANY|<ipv4>|<ipv6>|<ipv4-prefix>|<ipv6-prefix>|<ipv4-netmask>|<ipv6-netmask>)
nv set acl <acl-id> rule <rule-id> match ip protocol (0-255|tcp|udp|ospf|pim|icmp|icmpv6|igmp)
nv set acl <acl-id> rule <rule-id> match ip dscp (0-64|ANY|af11|af12|af13|af21|af22|af23|af31|af32|af33|af41|af42|af43|cs1|cs2|cs3|cs4|cs5|cs6|cs7|be|ef)
nv set acl <acl-id> rule <rule-id> match ip icmp-type (0-255|echo-reply|echo-request|time-exceeded|dest-unreachable|port-unreachable)
nv set acl <acl-id> rule <rule-id> match ip icmpv6-type (0-255|router-solicitation|router-advertisement|neighbor-solicitation|neighbor-advertisement)
nv set acl <acl-id> rule <rule-id> match mac
nv set acl <acl-id> rule <rule-id> match mac source-mac (ANY|bpdu|cdp|cisco-pvst|lacp|lldp|<mac>)
nv set acl <acl-id> rule <rule-id> match mac source-mac-mask <mac>
nv set acl <acl-id> rule <rule-id> match mac dest-mac (ANY|bpdu|cdp|cisco-pvst|lacp|lldp|<mac>)
nv set acl <acl-id> rule <rule-id> match mac dest-mac-mask <mac>
nv set acl <acl-id> rule <rule-id> match mac protocol (0-255|ANY|arp|ipv4|ipv6)
nv set acl <acl-id> rule <rule-id> match vlan 1-4094
nv set acl <acl-id> rule <rule-id> action
nv set acl <acl-id> rule <rule-id> action permit
nv set acl <acl-id> rule <rule-id> action deny
nv set acl <acl-id> rule <rule-id> action log
nv set acl <acl-id> rule <rule-id> action log log-prefix <value>
nv set acl <acl-id> rule <rule-id> action set
nv set acl <acl-id> rule <rule-id> action set dscp (0-64|ANY|af11|af12|af13|af21|af22|af23|af31|af32|af33|af41|af42|af43|cs1|cs2|cs3|cs4|cs5|cs6|cs7|be|ef)
nv set acl <acl-id> rule <rule-id> action set class 0-7
nv set acl <acl-id> rule <rule-id> action set cos 0-7
nv set acl <acl-id> rule <rule-id> action erspan
nv set acl <acl-id> rule <rule-id> action erspan source-ip (<ipv4>|<ipv6>)
nv set acl <acl-id> rule <rule-id> action erspan dest-ip (<ipv4>|<ipv6>)
nv set acl <acl-id> rule <rule-id> action erspan ttl 1-255
nv set acl <acl-id> rule <rule-id> action police
nv set acl <acl-id> rule <rule-id> action police mode (packet|kbps|mbps|gbps)
nv set acl <acl-id> rule <rule-id> action police burst 1-2147483647
nv set acl <acl-id> rule <rule-id> action police rate 1-2147483647
nv set acl <acl-id> rule <rule-id> action police class 0-7
nv set acl <acl-id> rule <rule-id> action span <interface-name>
nv set acl <acl-id> rule <rule-id> remark <value>
nv set acl <acl-id> type (ipv4|ipv6|mac)
nv unset router
nv unset router ptm
nv unset router ptm enable
nv unset router nexthop
nv unset router nexthop group
nv unset router nexthop group <nexthop-group-id>
nv unset router nexthop group <nexthop-group-id> via
nv unset router nexthop group <nexthop-group-id> via <via-id>
nv unset router nexthop group <nexthop-group-id> via <via-id> interface
nv unset router nexthop group <nexthop-group-id> via <via-id> vrf
nv unset router pbr
nv unset router pbr map
nv unset router pbr map <pbr-map-id>
nv unset router pbr map <pbr-map-id> rule
nv unset router pbr map <pbr-map-id> rule <rule-id>
nv unset router pbr map <pbr-map-id> rule <rule-id> match
nv unset router pbr map <pbr-map-id> rule <rule-id> match source-ip
nv unset router pbr map <pbr-map-id> rule <rule-id> match destination-ip
nv unset router pbr map <pbr-map-id> rule <rule-id> match dscp
nv unset router pbr map <pbr-map-id> rule <rule-id> match ecn
nv unset router pbr map <pbr-map-id> rule <rule-id> action
nv unset router pbr map <pbr-map-id> rule <rule-id> action nexthop-group
nv unset router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>
nv unset router pbr map <pbr-map-id> rule <rule-id> action vrf
nv unset router pbr enable
nv unset router policy
nv unset router policy community-list
nv unset router policy community-list <list-id>
nv unset router policy community-list <list-id> rule
nv unset router policy community-list <list-id> rule <rule-id>
nv unset router policy community-list <list-id> rule <rule-id> community
nv unset router policy community-list <list-id> rule <rule-id> community <community-id>
nv unset router policy community-list <list-id> rule <rule-id> action
nv unset router policy as-path-list
nv unset router policy as-path-list <list-id>
nv unset router policy as-path-list <list-id> rule
nv unset router policy as-path-list <list-id> rule <rule-id>
nv unset router policy as-path-list <list-id> rule <rule-id> action
nv unset router policy as-path-list <list-id> rule <rule-id> aspath-exp
nv unset router policy ext-community-list
nv unset router policy ext-community-list <list-id>
nv unset router policy ext-community-list <list-id> rule
nv unset router policy ext-community-list <list-id> rule <rule-id>
nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community
nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community rt
nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id>
nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community soo
nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id>
nv unset router policy ext-community-list <list-id> rule <rule-id> action
nv unset router policy large-community-list
nv unset router policy large-community-list <list-id>
nv unset router policy large-community-list <list-id> rule
nv unset router policy large-community-list <list-id> rule <rule-id>
nv unset router policy large-community-list <list-id> rule <rule-id> large-community
nv unset router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>
nv unset router policy large-community-list <list-id> rule <rule-id> action
nv unset router policy prefix-list
nv unset router policy prefix-list <prefix-list-id>
nv unset router policy prefix-list <prefix-list-id> rule
nv unset router policy prefix-list <prefix-list-id> rule <rule-id>
nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match
nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>
nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len
nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len
nv unset router policy prefix-list <prefix-list-id> rule <rule-id> action
nv unset router policy prefix-list <prefix-list-id> type
nv unset router policy route-map
nv unset router policy route-map <route-map-id>
nv unset router policy route-map <route-map-id> rule
nv unset router policy route-map <route-map-id> rule <rule-id>
nv unset router policy route-map <route-map-id> rule <rule-id> match
nv unset router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list
nv unset router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len
nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list
nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len
nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop
nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type
nv unset router policy route-map <route-map-id> rule <rule-id> match as-path-list
nv unset router policy route-map <route-map-id> rule <rule-id> match community-list
nv unset router policy route-map <route-map-id> rule <rule-id> match large-community-list
nv unset router policy route-map <route-map-id> rule <rule-id> match metric
nv unset router policy route-map <route-map-id> rule <rule-id> match interface
nv unset router policy route-map <route-map-id> rule <rule-id> match tag
nv unset router policy route-map <route-map-id> rule <rule-id> match source-protocol
nv unset router policy route-map <route-map-id> rule <rule-id> match origin
nv unset router policy route-map <route-map-id> rule <rule-id> match peer
nv unset router policy route-map <route-map-id> rule <rule-id> match local-preference
nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-route-type
nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-vni
nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-default-route
nv unset router policy route-map <route-map-id> rule <rule-id> match source-vrf
nv unset router policy route-map <route-map-id> rule <rule-id> match type
nv unset router policy route-map <route-map-id> rule <rule-id> set
nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend
nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as
nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as
nv unset router policy route-map <route-map-id> rule <rule-id> set community
nv unset router policy route-map <route-map-id> rule <rule-id> set community <community-id>
nv unset router policy route-map <route-map-id> rule <rule-id> set large-community
nv unset router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>
nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as
nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id>
nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address
nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id>
nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-exclude
nv unset router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate
nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-rt
nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-soo
nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-bw
nv unset router policy route-map <route-map-id> rule <rule-id> set local-preference
nv unset router policy route-map <route-map-id> rule <rule-id> set weight
nv unset router policy route-map <route-map-id> rule <rule-id> set metric
nv unset router policy route-map <route-map-id> rule <rule-id> set metric-type
nv unset router policy route-map <route-map-id> rule <rule-id> set origin
nv unset router policy route-map <route-map-id> rule <rule-id> set tag
nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global
nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local
nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global
nv unset router policy route-map <route-map-id> rule <rule-id> set ip-nexthop
nv unset router policy route-map <route-map-id> rule <rule-id> set source-ip
nv unset router policy route-map <route-map-id> rule <rule-id> set community-delete-list
nv unset router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list
nv unset router policy route-map <route-map-id> rule <rule-id> set originator-id
nv unset router policy route-map <route-map-id> rule <rule-id> set label-index
nv unset router policy route-map <route-map-id> rule <rule-id> set forwarding-address
nv unset router policy route-map <route-map-id> rule <rule-id> action
nv unset router policy route-map <route-map-id> rule <rule-id> action deny
nv unset router policy route-map <route-map-id> rule <rule-id> action permit
nv unset router policy route-map <route-map-id> rule <rule-id> action permit exit-policy
nv unset router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule
nv unset router policy route-map <route-map-id> rule <rule-id> description
nv unset router bgp
nv unset router bgp graceful-restart
nv unset router bgp graceful-restart mode
nv unset router bgp graceful-restart restart-time
nv unset router bgp graceful-restart path-selection-deferral-time
nv unset router bgp graceful-restart stale-routes-time
nv unset router bgp convergence-wait
nv unset router bgp convergence-wait time
nv unset router bgp convergence-wait establish-wait-time
nv unset router bgp enable
nv unset router bgp autonomous-system
nv unset router bgp router-id
nv unset router bgp policy-update-timer
nv unset router bgp graceful-shutdown
nv unset router bgp wait-for-install
nv unset router ospf
nv unset router ospf timers
nv unset router ospf timers lsa
nv unset router ospf timers lsa min-arrival
nv unset router ospf timers lsa throttle
nv unset router ospf timers spf
nv unset router ospf timers spf delay
nv unset router ospf timers spf holdtime
nv unset router ospf timers spf max-holdtime
nv unset router ospf timers refresh
nv unset router ospf enable
nv unset router ospf router-id
nv unset router pim
nv unset router pim timers
nv unset router pim timers hello-interval
nv unset router pim timers register-suppress
nv unset router pim timers join-prune-interval
nv unset router pim timers keep-alive
nv unset router pim timers rp-keep-alive
nv unset router pim enable
nv unset router pim packets
nv unset router igmp
nv unset router igmp enable
nv unset router vrrp
nv unset router vrrp enable
nv unset router vrrp priority
nv unset router vrrp preempt
nv unset router vrrp advertisement-interval
nv unset router vrr
nv unset router vrr enable
nv unset router adaptive-routing
nv unset router adaptive-routing enable
nv unset bridge
nv unset bridge domain
nv unset bridge domain <domain-id>
nv unset bridge domain <domain-id> stp
nv unset bridge domain <domain-id> stp state
nv unset bridge domain <domain-id> stp priority
nv unset bridge domain <domain-id> multicast
nv unset bridge domain <domain-id> multicast snooping
nv unset bridge domain <domain-id> multicast snooping querier
nv unset bridge domain <domain-id> multicast snooping querier enable
nv unset bridge domain <domain-id> multicast snooping enable
nv unset bridge domain <domain-id> vlan
nv unset bridge domain <domain-id> vlan <vid>
nv unset bridge domain <domain-id> vlan <vid> vni
nv unset bridge domain <domain-id> vlan <vid> vni <vni-id>
nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding
nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication
nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>
nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding enable
nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group
nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> mac-learning
nv unset bridge domain <domain-id> vlan <vid> ptp
nv unset bridge domain <domain-id> vlan <vid> ptp enable
nv unset bridge domain <domain-id> vlan <vid> multicast
nv unset bridge domain <domain-id> vlan <vid> multicast snooping
nv unset bridge domain <domain-id> vlan <vid> multicast snooping querier
nv unset bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip
nv unset bridge domain <domain-id> type
nv unset bridge domain <domain-id> untagged
nv unset bridge domain <domain-id> encap
nv unset bridge domain <domain-id> mac-address
nv unset bridge domain <domain-id> vlan-vni-offset
nv unset mlag
nv unset mlag backup
nv unset mlag backup <backup-ip>
nv unset mlag backup <backup-ip> vrf
nv unset mlag enable
nv unset mlag mac-address
nv unset mlag peer-ip
nv unset mlag priority
nv unset mlag init-delay
nv unset mlag debug
nv unset mlag lacp-conflict
nv unset evpn
nv unset evpn route-advertise
nv unset evpn route-advertise nexthop-setting
nv unset evpn route-advertise svi-ip
nv unset evpn route-advertise default-gateway
nv unset evpn dad
nv unset evpn dad duplicate-action
nv unset evpn dad duplicate-action freeze
nv unset evpn dad duplicate-action freeze duration
nv unset evpn dad enable
nv unset evpn dad mac-move-threshold
nv unset evpn dad move-window
nv unset evpn vni
nv unset evpn vni <vni-id>
nv unset evpn vni <vni-id> route-advertise
nv unset evpn vni <vni-id> route-advertise svi-ip
nv unset evpn vni <vni-id> route-advertise default-gateway
nv unset evpn vni <vni-id> route-target
nv unset evpn vni <vni-id> route-target export
nv unset evpn vni <vni-id> route-target export <rt-id>
nv unset evpn vni <vni-id> route-target import
nv unset evpn vni <vni-id> route-target import <rt-id>
nv unset evpn vni <vni-id> route-target both
nv unset evpn vni <vni-id> route-target both <rt-id>
nv unset evpn vni <vni-id> rd
nv unset evpn multihoming
nv unset evpn multihoming ead-evi-route
nv unset evpn multihoming ead-evi-route rx
nv unset evpn multihoming ead-evi-route tx
nv unset evpn multihoming segment
nv unset evpn multihoming segment mac-address
nv unset evpn multihoming segment df-preference
nv unset evpn multihoming enable
nv unset evpn multihoming mac-holdtime
nv unset evpn multihoming neighbor-holdtime
nv unset evpn multihoming startup-delay
nv unset evpn enable
nv unset qos
nv unset qos advance-buffer-config
nv unset qos advance-buffer-config <profile-id>
nv unset qos advance-buffer-config <profile-id> ingress-pool
nv unset qos advance-buffer-config <profile-id> ingress-pool <pool-id>
nv unset qos advance-buffer-config <profile-id> ingress-pool <pool-id> memory-percent
nv unset qos advance-buffer-config <profile-id> ingress-pool <pool-id> infinite
nv unset qos advance-buffer-config <profile-id> ingress-pool <pool-id> mode
nv unset qos advance-buffer-config <profile-id> ingress-pool <pool-id> reserved
nv unset qos advance-buffer-config <profile-id> ingress-pool <pool-id> shared-bytes
nv unset qos advance-buffer-config <profile-id> ingress-pool <pool-id> shared-alpha
nv unset qos advance-buffer-config <profile-id> egress-pool
nv unset qos advance-buffer-config <profile-id> egress-pool <pool-id>
nv unset qos advance-buffer-config <profile-id> egress-pool <pool-id> memory-percent
nv unset qos advance-buffer-config <profile-id> egress-pool <pool-id> infinite
nv unset qos advance-buffer-config <profile-id> egress-pool <pool-id> mode
nv unset qos advance-buffer-config <profile-id> egress-pool <pool-id> reserved
nv unset qos advance-buffer-config <profile-id> egress-pool <pool-id> shared-bytes
nv unset qos advance-buffer-config <profile-id> egress-pool <pool-id> shared-alpha
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id>
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> switch-priority
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> switch-priority <qos-sp-id>
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> name
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> reserved
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> shared-bytes
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> shared-alpha
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group-id> service-pool
nv unset qos advance-buffer-config <profile-id> ingress-lossless-buffer
nv unset qos advance-buffer-config <profile-id> ingress-lossless-buffer service-pool
nv unset qos advance-buffer-config <profile-id> ingress-lossless-buffer shared-alpha
nv unset qos advance-buffer-config <profile-id> ingress-lossless-buffer shared-bytes
nv unset qos advance-buffer-config <profile-id> egress-lossless-buffer
nv unset qos advance-buffer-config <profile-id> egress-lossless-buffer service-pool
nv unset qos advance-buffer-config <profile-id> egress-lossless-buffer reserved
nv unset qos advance-buffer-config <profile-id> egress-lossless-buffer shared-alpha
nv unset qos advance-buffer-config <profile-id> egress-lossless-buffer shared-bytes
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id>
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> reserved
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> shared-bytes
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> shared-alpha
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer traffic-class <traffic-class-id> service-pool
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id>
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> reserved
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> shared-bytes
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> shared-alpha
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-switch-priority <qos-sp-id> service-pool
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port reserved
nv unset qos advance-buffer-config <profile-id> egress-lossy-buffer multicast-port shared-bytes
nv unset qos traffic-pool
nv unset qos traffic-pool <traffic-pool-id>
nv unset qos traffic-pool <traffic-pool-id> switch-priority
nv unset qos traffic-pool <traffic-pool-id> switch-priority <qos-sp-id>
nv unset qos traffic-pool <traffic-pool-id> memory-percent
nv unset qos link-pause
nv unset qos link-pause <profile-id>
nv unset qos link-pause <profile-id> xoff-threshold
nv unset qos link-pause <profile-id> xon-threshold
nv unset qos link-pause <profile-id> port-buffer
nv unset qos link-pause <profile-id> cable-length
nv unset qos link-pause <profile-id> tx
nv unset qos link-pause <profile-id> rx
nv unset qos pfc
nv unset qos pfc <profile-id>
nv unset qos pfc <profile-id> switch-priority
nv unset qos pfc <profile-id> switch-priority <qos-sp-id>
nv unset qos pfc <profile-id> xoff-threshold
nv unset qos pfc <profile-id> xon-threshold
nv unset qos pfc <profile-id> port-buffer
nv unset qos pfc <profile-id> cable-length
nv unset qos pfc <profile-id> tx
nv unset qos pfc <profile-id> rx
nv unset qos mapping
nv unset qos mapping <profile-id>
nv unset qos mapping <profile-id> pcp
nv unset qos mapping <profile-id> pcp <qos-pcp-id>
nv unset qos mapping <profile-id> pcp <qos-pcp-id> switch-priority
nv unset qos mapping <profile-id> dscp
nv unset qos mapping <profile-id> dscp <qos-dscp-id>
nv unset qos mapping <profile-id> dscp <qos-dscp-id> switch-priority
nv unset qos mapping <profile-id> port-default-sp
nv unset qos mapping <profile-id> trust
nv unset qos remark
nv unset qos remark <profile-id>
nv unset qos remark <profile-id> switch-priority
nv unset qos remark <profile-id> switch-priority <qos-sp-id>
nv unset qos remark <profile-id> switch-priority <qos-sp-id> pcp
nv unset qos remark <profile-id> switch-priority <qos-sp-id> dscp
nv unset qos remark <profile-id> rewrite
nv unset qos congestion-control
nv unset qos congestion-control <profile-id>
nv unset qos congestion-control <profile-id> traffic-class
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id>
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> min-threshold
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> max-threshold
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> probability
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> red
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> ecn
nv unset qos egress-queue-mapping
nv unset qos egress-queue-mapping <profile-id>
nv unset qos egress-queue-mapping <profile-id> switch-priority
nv unset qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id>
nv unset qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id> traffic-class
nv unset qos egress-scheduler
nv unset qos egress-scheduler <profile-id>
nv unset qos egress-scheduler <profile-id> traffic-class
nv unset qos egress-scheduler <profile-id> traffic-class <qos-tc-id>
nv unset qos egress-scheduler <profile-id> traffic-class <qos-tc-id> mode
nv unset qos egress-scheduler <profile-id> traffic-class <qos-tc-id> bw-percent
nv unset qos egress-shaper
nv unset qos egress-shaper <profile-id>
nv unset qos egress-shaper <profile-id> traffic-class
nv unset qos egress-shaper <profile-id> traffic-class <qos-tc-id>
nv unset qos egress-shaper <profile-id> traffic-class <qos-tc-id> min-rate
nv unset qos egress-shaper <profile-id> traffic-class <qos-tc-id> max-rate
nv unset qos egress-shaper <profile-id> port-max-rate
nv unset qos roce
nv unset qos roce enable
nv unset qos roce mode
nv unset interface
nv unset interface <interface-id>
nv unset interface <interface-id> ip
nv unset interface <interface-id> ip address
nv unset interface <interface-id> ip address <ip-prefix-id>
nv unset interface <interface-id> ip gateway
nv unset interface <interface-id> ip gateway <ip-address-id>
nv unset interface <interface-id> ip ipv4
nv unset interface <interface-id> ip ipv4 forward
nv unset interface <interface-id> ip ipv6
nv unset interface <interface-id> ip ipv6 enable
nv unset interface <interface-id> ip ipv6 forward
nv unset interface <interface-id> ip vrr
nv unset interface <interface-id> ip vrr address
nv unset interface <interface-id> ip vrr address <ip-prefix-id>
nv unset interface <interface-id> ip vrr state
nv unset interface <interface-id> ip vrr enable
nv unset interface <interface-id> ip vrr mac-id
nv unset interface <interface-id> ip vrr mac-address
nv unset interface <interface-id> ip igmp
nv unset interface <interface-id> ip igmp static-group
nv unset interface <interface-id> ip igmp static-group <static-group-id>
nv unset interface <interface-id> ip igmp enable
nv unset interface <interface-id> ip igmp version
nv unset interface <interface-id> ip igmp query-interval
nv unset interface <interface-id> ip igmp query-max-response-time
nv unset interface <interface-id> ip igmp last-member-query-interval
nv unset interface <interface-id> ip vrrp
nv unset interface <interface-id> ip vrrp virtual-router
nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id>
nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> address
nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>
nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> version
nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> priority
nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt
nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> advertisement-interval
nv unset interface <interface-id> ip vrrp enable
nv unset interface <interface-id> ip neighbor-discovery
nv unset interface <interface-id> ip neighbor-discovery rdnss
nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>
nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime
nv unset interface <interface-id> ip neighbor-discovery prefix
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig
nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address
nv unset interface <interface-id> ip neighbor-discovery dnssl
nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>
nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime
nv unset interface <interface-id> ip neighbor-discovery router-advertisement
nv unset interface <interface-id> ip neighbor-discovery router-advertisement enable
nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval
nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval-option
nv unset interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit
nv unset interface <interface-id> ip neighbor-discovery router-advertisement lifetime
nv unset interface <interface-id> ip neighbor-discovery router-advertisement reachable-time
nv unset interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time
nv unset interface <interface-id> ip neighbor-discovery router-advertisement managed-config
nv unset interface <interface-id> ip neighbor-discovery router-advertisement other-config
nv unset interface <interface-id> ip neighbor-discovery router-advertisement hop-limit
nv unset interface <interface-id> ip neighbor-discovery router-advertisement router-preference
nv unset interface <interface-id> ip neighbor-discovery home-agent
nv unset interface <interface-id> ip neighbor-discovery home-agent enable
nv unset interface <interface-id> ip neighbor-discovery home-agent lifetime
nv unset interface <interface-id> ip neighbor-discovery home-agent preference
nv unset interface <interface-id> ip neighbor-discovery enable
nv unset interface <interface-id> ip neighbor-discovery mtu
nv unset interface <interface-id> ip vrf
nv unset interface <interface-id> link
nv unset interface <interface-id> link state
nv unset interface <interface-id> link breakout
nv unset interface <interface-id> link breakout <mode-id>
nv unset interface <interface-id> link breakout <mode-id> lanes-per-port
nv unset interface <interface-id> link auto-negotiate
nv unset interface <interface-id> link duplex
nv unset interface <interface-id> link lanes
nv unset interface <interface-id> link speed
nv unset interface <interface-id> link fec
nv unset interface <interface-id> link mtu
nv unset interface <interface-id> link fast-linkup
nv unset interface <interface-id> router
nv unset interface <interface-id> router pbr
nv unset interface <interface-id> router pbr map
nv unset interface <interface-id> router pbr map <pbr-map-id>
nv unset interface <interface-id> router ospf
nv unset interface <interface-id> router ospf timers
nv unset interface <interface-id> router ospf timers dead-interval
nv unset interface <interface-id> router ospf timers hello-multiplier
nv unset interface <interface-id> router ospf timers hello-interval
nv unset interface <interface-id> router ospf timers retransmit-interval
nv unset interface <interface-id> router ospf timers transmit-delay
nv unset interface <interface-id> router ospf authentication
nv unset interface <interface-id> router ospf authentication enable
nv unset interface <interface-id> router ospf authentication message-digest-key
nv unset interface <interface-id> router ospf authentication md5-key
nv unset interface <interface-id> router ospf bfd
nv unset interface <interface-id> router ospf bfd enable
nv unset interface <interface-id> router ospf bfd detect-multiplier
nv unset interface <interface-id> router ospf bfd min-receive-interval
nv unset interface <interface-id> router ospf bfd min-transmit-interval
nv unset interface <interface-id> router ospf enable
nv unset interface <interface-id> router ospf area
nv unset interface <interface-id> router ospf cost
nv unset interface <interface-id> router ospf mtu-ignore
nv unset interface <interface-id> router ospf network-type
nv unset interface <interface-id> router ospf passive
nv unset interface <interface-id> router ospf priority
nv unset interface <interface-id> router pim
nv unset interface <interface-id> router pim timers
nv unset interface <interface-id> router pim timers hello-interval
nv unset interface <interface-id> router pim bfd
nv unset interface <interface-id> router pim bfd enable
nv unset interface <interface-id> router pim bfd detect-multiplier
nv unset interface <interface-id> router pim bfd min-receive-interval
nv unset interface <interface-id> router pim bfd min-transmit-interval
nv unset interface <interface-id> router pim address-family
nv unset interface <interface-id> router pim address-family ipv4-unicast
nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp
nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp enable
nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp rp-list
nv unset interface <interface-id> router pim address-family ipv4-unicast multicast-boundary-oil
nv unset interface <interface-id> router pim address-family ipv4-unicast use-source
nv unset interface <interface-id> router pim enable
nv unset interface <interface-id> router pim dr-priority
nv unset interface <interface-id> router pim active-active
nv unset interface <interface-id> router adaptive-routing
nv unset interface <interface-id> router adaptive-routing enable
nv unset interface <interface-id> router adaptive-routing link-utilization-threshold
nv unset interface <interface-id> bond
nv unset interface <interface-id> bond member
nv unset interface <interface-id> bond member <member-id>
nv unset interface <interface-id> bond mlag
nv unset interface <interface-id> bond mlag enable
nv unset interface <interface-id> bond mlag id
nv unset interface <interface-id> bond mlag lacp-conflict
nv unset interface <interface-id> bond down-delay
nv unset interface <interface-id> bond lacp-bypass
nv unset interface <interface-id> bond lacp-rate
nv unset interface <interface-id> bond mode
nv unset interface <interface-id> bond up-delay
nv unset interface <interface-id> bridge
nv unset interface <interface-id> bridge domain
nv unset interface <interface-id> bridge domain <domain-id>
nv unset interface <interface-id> bridge domain <domain-id> stp
nv unset interface <interface-id> bridge domain <domain-id> stp bpdu-filter
nv unset interface <interface-id> bridge domain <domain-id> stp bpdu-guard
nv unset interface <interface-id> bridge domain <domain-id> stp admin-edge
nv unset interface <interface-id> bridge domain <domain-id> stp auto-edge
nv unset interface <interface-id> bridge domain <domain-id> stp network
nv unset interface <interface-id> bridge domain <domain-id> stp restrrole
nv unset interface <interface-id> bridge domain <domain-id> vlan
nv unset interface <interface-id> bridge domain <domain-id> vlan <vid>
nv unset interface <interface-id> bridge domain <domain-id> learning
nv unset interface <interface-id> bridge domain <domain-id> untagged
nv unset interface <interface-id> bridge domain <domain-id> access
nv unset interface <interface-id> lldp
nv unset interface <interface-id> lldp dcbx-pfc-tlv
nv unset interface <interface-id> lldp dcbx-ets-config-tlv
nv unset interface <interface-id> lldp dcbx-ets-recomm-tlv
nv unset interface <interface-id> qos
nv unset interface <interface-id> qos pfc
nv unset interface <interface-id> qos pfc profile
nv unset interface <interface-id> qos link-pause
nv unset interface <interface-id> qos link-pause profile
nv unset interface <interface-id> qos mapping
nv unset interface <interface-id> qos mapping profile
nv unset interface <interface-id> qos remark
nv unset interface <interface-id> qos remark profile
nv unset interface <interface-id> qos congestion-control
nv unset interface <interface-id> qos congestion-control profile
nv unset interface <interface-id> qos egress-scheduler
nv unset interface <interface-id> qos egress-scheduler profile
nv unset interface <interface-id> qos egress-shaper
nv unset interface <interface-id> qos egress-shaper profile
nv unset interface <interface-id> evpn
nv unset interface <interface-id> evpn multihoming
nv unset interface <interface-id> evpn multihoming segment
nv unset interface <interface-id> evpn multihoming segment enable
nv unset interface <interface-id> evpn multihoming segment local-id
nv unset interface <interface-id> evpn multihoming segment identifier
nv unset interface <interface-id> evpn multihoming segment mac-address
nv unset interface <interface-id> evpn multihoming segment df-preference
nv unset interface <interface-id> evpn multihoming uplink
nv unset interface <interface-id> acl
nv unset interface <interface-id> acl <acl-id>
nv unset interface <interface-id> acl <acl-id> inbound
nv unset interface <interface-id> acl <acl-id> inbound control-plane
nv unset interface <interface-id> acl <acl-id> outbound
nv unset interface <interface-id> acl <acl-id> outbound control-plane
nv unset interface <interface-id> ptp
nv unset interface <interface-id> ptp timers
nv unset interface <interface-id> ptp timers announce-interval
nv unset interface <interface-id> ptp timers sync-interval
nv unset interface <interface-id> ptp timers delay-req-interval
nv unset interface <interface-id> ptp timers announce-timeout
nv unset interface <interface-id> ptp enable
nv unset interface <interface-id> ptp instance
nv unset interface <interface-id> ptp forced-master
nv unset interface <interface-id> ptp acceptable-master
nv unset interface <interface-id> ptp delay-mechanism
nv unset interface <interface-id> ptp transport
nv unset interface <interface-id> ptp ttl
nv unset interface <interface-id> ptp mixed-multicast-unicast
nv unset interface <interface-id> ptp unicast-service-mode
nv unset interface <interface-id> ptp unicast-request-duration
nv unset interface <interface-id> ptp unicast-master-table-id
nv unset interface <interface-id> tunnel
nv unset interface <interface-id> tunnel source-ip
nv unset interface <interface-id> tunnel dest-ip
nv unset interface <interface-id> tunnel ttl
nv unset interface <interface-id> tunnel mode
nv unset interface <interface-id> tunnel interface
nv unset interface <interface-id> storm-control
nv unset interface <interface-id> storm-control broadcast
nv unset interface <interface-id> storm-control multicast
nv unset interface <interface-id> storm-control unknown-unicast
nv unset interface <interface-id> synce
nv unset interface <interface-id> synce enable
nv unset interface <interface-id> synce provider-priority
nv unset interface <interface-id> type
nv unset interface <interface-id> base-interface
nv unset interface <interface-id> vlan
nv unset interface <interface-id> description
nv unset service
nv unset service dhcp-server
nv unset service dhcp-server <vrf-id>
nv unset service dhcp-server <vrf-id> interface
nv unset service dhcp-server <vrf-id> interface <interface-id>
nv unset service dhcp-server <vrf-id> pool
nv unset service dhcp-server <vrf-id> pool <pool-id>
nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name-server
nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>
nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name
nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>
nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name
nv unset service dhcp-server <vrf-id> pool <pool-id> gateway
nv unset service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>
nv unset service dhcp-server <vrf-id> pool <pool-id> range
nv unset service dhcp-server <vrf-id> pool <pool-id> range <range-id>
nv unset service dhcp-server <vrf-id> pool <pool-id> range <range-id> to
nv unset service dhcp-server <vrf-id> pool <pool-id> pool-name
nv unset service dhcp-server <vrf-id> pool <pool-id> lease-time
nv unset service dhcp-server <vrf-id> pool <pool-id> ping-check
nv unset service dhcp-server <vrf-id> pool <pool-id> default-url
nv unset service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url
nv unset service dhcp-server <vrf-id> domain-name
nv unset service dhcp-server <vrf-id> domain-name <domain-name-id>
nv unset service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name
nv unset service dhcp-server <vrf-id> domain-name-server
nv unset service dhcp-server <vrf-id> domain-name-server <server-id>
nv unset service dhcp-server <vrf-id> static
nv unset service dhcp-server <vrf-id> static <static-id>
nv unset service dhcp-server <vrf-id> static <static-id> mac-address
nv unset service dhcp-server <vrf-id> static <static-id> ip-address
nv unset service dhcp-server <vrf-id> static <static-id> cumulus-provision-url
nv unset service dhcp-server <vrf-id> static <static-id> host-id-circuit-id
nv unset service dhcp-server6
nv unset service dhcp-server6 <vrf-id>
nv unset service dhcp-server6 <vrf-id> interface
nv unset service dhcp-server6 <vrf-id> interface <interface-id>
nv unset service dhcp-server6 <vrf-id> pool
nv unset service dhcp-server6 <vrf-id> pool <pool-id>
nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server
nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>
nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name
nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>
nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name
nv unset service dhcp-server6 <vrf-id> pool <pool-id> range
nv unset service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>
nv unset service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to
nv unset service dhcp-server6 <vrf-id> pool <pool-id> pool-name
nv unset service dhcp-server6 <vrf-id> pool <pool-id> lease-time
nv unset service dhcp-server6 <vrf-id> pool <pool-id> ping-check
nv unset service dhcp-server6 <vrf-id> pool <pool-id> default-url
nv unset service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url
nv unset service dhcp-server6 <vrf-id> domain-name
nv unset service dhcp-server6 <vrf-id> domain-name <domain-name-id>
nv unset service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name
nv unset service dhcp-server6 <vrf-id> domain-name-server
nv unset service dhcp-server6 <vrf-id> domain-name-server <server-id>
nv unset service dhcp-server6 <vrf-id> static
nv unset service dhcp-server6 <vrf-id> static <static-id>
nv unset service dhcp-server6 <vrf-id> static <static-id> mac-address
nv unset service dhcp-server6 <vrf-id> static <static-id> ip-address
nv unset service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url
nv unset service dns
nv unset service dns <vrf-id>
nv unset service dns <vrf-id> server
nv unset service dns <vrf-id> server <dns-server-id>
nv unset service syslog
nv unset service syslog <vrf-id>
nv unset service syslog <vrf-id> server
nv unset service syslog <vrf-id> server <server-id>
nv unset service syslog <vrf-id> server <server-id> port
nv unset service syslog <vrf-id> server <server-id> protocol
nv unset service ntp
nv unset service ntp <vrf-id>
nv unset service ntp <vrf-id> server
nv unset service ntp <vrf-id> server <server-id>
nv unset service ntp <vrf-id> server <server-id> iburst
nv unset service ntp <vrf-id> pool
nv unset service ntp <vrf-id> pool <server-id>
nv unset service ntp <vrf-id> pool <server-id> iburst
nv unset service ntp <vrf-id> listen
nv unset service dhcp-relay
nv unset service dhcp-relay <vrf-id>
nv unset service dhcp-relay <vrf-id> server
nv unset service dhcp-relay <vrf-id> server <server-id>
nv unset service dhcp-relay <vrf-id> interface
nv unset service dhcp-relay <vrf-id> interface <interface-id>
nv unset service dhcp-relay <vrf-id> giaddress-interface
nv unset service dhcp-relay <vrf-id> giaddress-interface <interface-id>
nv unset service dhcp-relay <vrf-id> giaddress-interface <interface-id> address
nv unset service dhcp-relay <vrf-id> source-ip
nv unset service dhcp-relay6
nv unset service dhcp-relay6 <vrf-id>
nv unset service dhcp-relay6 <vrf-id> interface
nv unset service dhcp-relay6 <vrf-id> interface upstream
nv unset service dhcp-relay6 <vrf-id> interface upstream <interface-id>
nv unset service dhcp-relay6 <vrf-id> interface upstream <interface-id> address
nv unset service dhcp-relay6 <vrf-id> interface downstream
nv unset service dhcp-relay6 <vrf-id> interface downstream <interface-id>
nv unset service dhcp-relay6 <vrf-id> interface downstream <interface-id> address
nv unset service snmp-server
nv unset service snmp-server listening-address
nv unset service snmp-server listening-address <listening-address-id>
nv unset service snmp-server listening-address <listening-address-id> vrf
nv unset service snmp-server username
nv unset service snmp-server username <username-id>
nv unset service snmp-server username <username-id> auth-none
nv unset service snmp-server username <username-id> auth-none oid
nv unset service snmp-server username <username-id> auth-none view
nv unset service snmp-server username <username-id> auth-md5
nv unset service snmp-server username <username-id> auth-md5 <auth-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> view
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> view
nv unset service snmp-server username <username-id> auth-md5 <auth-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> view
nv unset service snmp-server username <username-id> auth-sha
nv unset service snmp-server username <username-id> auth-sha <auth-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> view
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> view
nv unset service snmp-server username <username-id> auth-sha <auth-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> view
nv unset service snmp-server mibs
nv unset service snmp-server viewname
nv unset service snmp-server viewname <viewname-id>
nv unset service snmp-server viewname <viewname-id> excluded
nv unset service snmp-server viewname <viewname-id> included
nv unset service snmp-server readonly-community
nv unset service snmp-server readonly-community <readonly-community-id>
nv unset service snmp-server readonly-community <readonly-community-id> access
nv unset service snmp-server readonly-community <readonly-community-id> access <access-id>
nv unset service snmp-server readonly-community <readonly-community-id> access <access-id> oid
nv unset service snmp-server readonly-community <readonly-community-id> access <access-id> view
nv unset service snmp-server readonly-community-v6
nv unset service snmp-server readonly-community-v6 <readonly-community-id>
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> oid
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> view
nv unset service snmp-server trap-link-down
nv unset service snmp-server trap-link-down check-frequency
nv unset service snmp-server trap-link-up
nv unset service snmp-server trap-link-up check-frequency
nv unset service snmp-server trap-snmp-auth-failures
nv unset service snmp-server trap-cpu-load-average
nv unset service snmp-server trap-cpu-load-average one-minute
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id>
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id>
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute <fifteen-minute-id>
nv unset service snmp-server trap-destination
nv unset service snmp-server trap-destination <trap-destination-id>
nv unset service snmp-server trap-destination <trap-destination-id> community-password
nv unset service snmp-server trap-destination <trap-destination-id> community-password <community-password-id>
nv unset service snmp-server trap-destination <trap-destination-id> community-password <community-password-id> version
nv unset service snmp-server trap-destination <trap-destination-id> vrf
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id> version
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server enable
nv unset service snmp-server system-contact
nv unset service snmp-server system-location
nv unset service snmp-server system-name
nv unset service synce
nv unset service synce enable
nv unset service synce wait-to-restore-time
nv unset service synce log-level
nv unset service synce provider-default-priority
nv unset service ptp
nv unset service ptp <instance-id>
nv unset service ptp <instance-id> acceptable-master
nv unset service ptp <instance-id> acceptable-master <clock-id>
nv unset service ptp <instance-id> acceptable-master <clock-id> alt-priority
nv unset service ptp <instance-id> unicast-master
nv unset service ptp <instance-id> unicast-master <table-id>
nv unset service ptp <instance-id> unicast-master <table-id> address
nv unset service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv unset service ptp <instance-id> unicast-master <table-id> query-interval
nv unset service ptp <instance-id> unicast-master <table-id> peer-address
nv unset service ptp <instance-id> profile
nv unset service ptp <instance-id> profile <profile-id>
nv unset service ptp <instance-id> profile <profile-id> profile-type
nv unset service ptp <instance-id> profile <profile-id> priority1
nv unset service ptp <instance-id> profile <profile-id> priority2
nv unset service ptp <instance-id> profile <profile-id> local-priority
nv unset service ptp <instance-id> profile <profile-id> domain
nv unset service ptp <instance-id> profile <profile-id> delay-mechanism
nv unset service ptp <instance-id> profile <profile-id> transport
nv unset service ptp <instance-id> profile <profile-id> announce-interval
nv unset service ptp <instance-id> profile <profile-id> sync-interval
nv unset service ptp <instance-id> profile <profile-id> delay-req-interval
nv unset service ptp <instance-id> profile <profile-id> announce-timeout
nv unset service ptp <instance-id> monitor
nv unset service ptp <instance-id> monitor min-offset-threshold
nv unset service ptp <instance-id> monitor max-offset-threshold
nv unset service ptp <instance-id> monitor path-delay-threshold
nv unset service ptp <instance-id> monitor max-timestamp-entries
nv unset service ptp <instance-id> monitor max-violation-log-sets
nv unset service ptp <instance-id> monitor max-violation-log-entries
nv unset service ptp <instance-id> monitor violation-log-interval
nv unset service ptp <instance-id> enable
nv unset service ptp <instance-id> current-profile
nv unset service ptp <instance-id> priority1
nv unset service ptp <instance-id> priority2
nv unset service ptp <instance-id> domain
nv unset service ptp <instance-id> ip-dscp
nv unset service lldp
nv unset service lldp tx-interval
nv unset service lldp tx-hold-multiplier
nv unset service lldp dot1-tlv
nv unset service lldp mode
nv unset system
nv unset system message
nv unset system message pre-login
nv unset system message post-login
nv unset system config
nv unset system config auto-save
nv unset system config auto-save enable
nv unset system config apply
nv unset system config apply ignore
nv unset system config apply ignore <ignore-id>
nv unset system config apply overwrite
nv unset system acl
nv unset system acl mode
nv unset system counter
nv unset system counter polling-interval
nv unset system counter polling-interval logical-interface
nv unset system counter polling-interval physical-interface
nv unset system control-plane
nv unset system control-plane trap
nv unset system control-plane trap <trap-id>
nv unset system control-plane trap <trap-id> state
nv unset system control-plane policer
nv unset system control-plane policer <policer-id>
nv unset system control-plane policer <policer-id> state
nv unset system control-plane policer <policer-id> burst
nv unset system control-plane policer <policer-id> rate
nv unset system global
nv unset system global reserved
nv unset system global reserved routing-table
nv unset system global reserved routing-table pbr
nv unset system global reserved routing-table pbr begin
nv unset system global reserved routing-table pbr end
nv unset system global reserved vlan
nv unset system global reserved vlan internal
nv unset system global reserved vlan internal range
nv unset system global reserved vlan l3-vni-vlan
nv unset system global reserved vlan l3-vni-vlan begin
nv unset system global reserved vlan l3-vni-vlan end
nv unset system global system-mac
nv unset system global anycast-mac
nv unset system global anycast-id
nv unset system global fabric-mac
nv unset system global fabric-id
nv unset system forwarding
nv unset system forwarding lag-hash
nv unset system forwarding lag-hash ip-protocol
nv unset system forwarding lag-hash source-mac
nv unset system forwarding lag-hash destination-mac
nv unset system forwarding lag-hash source-ip
nv unset system forwarding lag-hash destination-ip
nv unset system forwarding lag-hash source-port
nv unset system forwarding lag-hash destination-port
nv unset system forwarding lag-hash ether-type
nv unset system forwarding lag-hash vlan
nv unset system forwarding lag-hash gtp-teid
nv unset system forwarding ecmp-hash
nv unset system forwarding ecmp-hash ip-protocol
nv unset system forwarding ecmp-hash source-ip
nv unset system forwarding ecmp-hash destination-ip
nv unset system forwarding ecmp-hash source-port
nv unset system forwarding ecmp-hash destination-port
nv unset system forwarding ecmp-hash ipv6-label
nv unset system forwarding ecmp-hash ingress-interface
nv unset system forwarding ecmp-hash gtp-teid
nv unset system forwarding ecmp-hash inner-ip-protocol
nv unset system forwarding ecmp-hash inner-source-ip
nv unset system forwarding ecmp-hash inner-destination-ip
nv unset system forwarding ecmp-hash inner-source-port
nv unset system forwarding ecmp-hash inner-destination-port
nv unset system forwarding ecmp-hash inner-ipv6-label
nv unset system forwarding programming
nv unset system forwarding programming log-level
nv unset system forwarding hash-seed
nv unset system forwarding host-route-preference
nv unset system forwarding profile
nv unset system port-mirror
nv unset system port-mirror session
nv unset system port-mirror session <session-id>
nv unset system port-mirror session <session-id> span
nv unset system port-mirror session <session-id> span source-port
nv unset system port-mirror session <session-id> span source-port <port-id>
nv unset system port-mirror session <session-id> span destination
nv unset system port-mirror session <session-id> span destination <port-id>
nv unset system port-mirror session <session-id> span truncate
nv unset system port-mirror session <session-id> span truncate enable
nv unset system port-mirror session <session-id> span truncate size
nv unset system port-mirror session <session-id> span enable
nv unset system port-mirror session <session-id> span direction
nv unset system port-mirror session <session-id> erspan
nv unset system port-mirror session <session-id> erspan source-port
nv unset system port-mirror session <session-id> erspan source-port <port-id>
nv unset system port-mirror session <session-id> erspan destination
nv unset system port-mirror session <session-id> erspan destination source-ip
nv unset system port-mirror session <session-id> erspan destination source-ip <source-ip>
nv unset system port-mirror session <session-id> erspan destination dest-ip
nv unset system port-mirror session <session-id> erspan destination dest-ip <dest-ip>
nv unset system port-mirror session <session-id> erspan truncate
nv unset system port-mirror session <session-id> erspan truncate enable
nv unset system port-mirror session <session-id> erspan truncate size
nv unset system port-mirror session <session-id> erspan enable
nv unset system port-mirror session <session-id> erspan direction
nv unset system wjh
nv unset system wjh channel
nv unset system wjh channel <channel-id>
nv unset system wjh channel <channel-id> trigger
nv unset system wjh enable
nv unset system aaa
nv unset system aaa user
nv unset system aaa user <user-id>
nv unset system aaa user <user-id> ssh
nv unset system aaa user <user-id> ssh authorized-key
nv unset system aaa user <user-id> ssh authorized-key <ssh-authorized-key-id>
nv unset system aaa user <user-id> ssh authorized-key <ssh-authorized-key-id> key
nv unset system aaa user <user-id> ssh authorized-key <ssh-authorized-key-id> type
nv unset system aaa user <user-id> role
nv unset system aaa user <user-id> full-name
nv unset system aaa user <user-id> password
nv unset system aaa user <user-id> hashed-password
nv unset system aaa user <user-id> enable
nv unset system aaa authentication-order
nv unset system aaa authentication-order <priority-id>
nv unset system aaa tacacs
nv unset system aaa tacacs authentication
nv unset system aaa tacacs authentication mode
nv unset system aaa tacacs authentication per-user-homedir
nv unset system aaa tacacs accounting
nv unset system aaa tacacs accounting enable
nv unset system aaa tacacs accounting send-records
nv unset system aaa tacacs server
nv unset system aaa tacacs server <priority-id>
nv unset system aaa tacacs server <priority-id> host
nv unset system aaa tacacs server <priority-id> port
nv unset system aaa tacacs server <priority-id> secret
nv unset system aaa tacacs exclude-user
nv unset system aaa tacacs exclude-user username
nv unset system aaa tacacs enable
nv unset system aaa tacacs timeout
nv unset system aaa tacacs debug-level
nv unset system aaa tacacs source-ip
nv unset system aaa tacacs vrf
nv unset system hostname
nv unset system timezone
nv unset vrf
nv unset vrf <vrf-id>
nv unset vrf <vrf-id> loopback
nv unset vrf <vrf-id> loopback ip
nv unset vrf <vrf-id> loopback ip address
nv unset vrf <vrf-id> loopback ip address <ip-prefix-id>
nv unset vrf <vrf-id> evpn
nv unset vrf <vrf-id> evpn vni
nv unset vrf <vrf-id> evpn vni <vni-id>
nv unset vrf <vrf-id> evpn enable
nv unset vrf <vrf-id> evpn vlan
nv unset vrf <vrf-id> evpn prefix-routes-only
nv unset vrf <vrf-id> router
nv unset vrf <vrf-id> router rib
nv unset vrf <vrf-id> router rib <afi>
nv unset vrf <vrf-id> router rib <afi> protocol
nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id>
nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id> fib-filter
nv unset vrf <vrf-id> router nexthop-tracking
nv unset vrf <vrf-id> router nexthop-tracking <afi>
nv unset vrf <vrf-id> router nexthop-tracking <afi> route-map
nv unset vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id>
nv unset vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol
nv unset vrf <vrf-id> router nexthop-tracking <afi> resolved-via-default
nv unset vrf <vrf-id> router bgp
nv unset vrf <vrf-id> router bgp address-family
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static enable
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static metric
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected enable
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected metric
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel enable
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel metric
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf enable
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf metric
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast network
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf enable
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn enable
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn route-map
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast rib-filter
nv unset vrf <vrf-id> router bgp address-family ipv4-unicast enable
nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn
nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn enable
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> summary-only
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast network
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf enable
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn enable
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static enable
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static metric
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected enable
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected metric
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel enable
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel metric
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 enable
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 metric
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 route-map
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast rib-filter
nv unset vrf <vrf-id> router bgp address-family ipv6-unicast enable
nv unset vrf <vrf-id> router bgp path-selection
nv unset vrf <vrf-id> router bgp path-selection aspath
nv unset vrf <vrf-id> router bgp path-selection aspath compare-lengths
nv unset vrf <vrf-id> router bgp path-selection aspath compare-confed
nv unset vrf <vrf-id> router bgp path-selection med
nv unset vrf <vrf-id> router bgp path-selection med compare-always
nv unset vrf <vrf-id> router bgp path-selection med compare-deterministic
nv unset vrf <vrf-id> router bgp path-selection med compare-confed
nv unset vrf <vrf-id> router bgp path-selection med missing-as-max
nv unset vrf <vrf-id> router bgp path-selection multipath
nv unset vrf <vrf-id> router bgp path-selection multipath aspath-ignore
nv unset vrf <vrf-id> router bgp path-selection multipath generate-asset
nv unset vrf <vrf-id> router bgp path-selection multipath bandwidth
nv unset vrf <vrf-id> router bgp path-selection routerid-compare
nv unset vrf <vrf-id> router bgp route-reflection
nv unset vrf <vrf-id> router bgp route-reflection enable
nv unset vrf <vrf-id> router bgp route-reflection cluster-id
nv unset vrf <vrf-id> router bgp route-reflection reflect-between-clients
nv unset vrf <vrf-id> router bgp route-reflection outbound-policy
nv unset vrf <vrf-id> router bgp peer-group
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id>
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities extended-nexthop
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities source-address
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart mode
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as prepend
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as replace
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers keepalive
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers hold
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers connection-retry
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers route-advertisement
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise regular
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise extended
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise large
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod aspath
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod med
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod nexthop
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn origin
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath replace-peer-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath private-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound maximum
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-only
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination policy
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound route-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound prefix-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound route-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound unsuppress-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound prefix-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-reflector-client
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-server-client
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft-reconfiguration
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast nexthop-setting
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast add-path-tx
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound route-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound prefix-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound route-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound unsuppress-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound prefix-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn origin
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath replace-peer-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath private-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound maximum
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-only
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination policy
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise regular
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise extended
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise large
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod aspath
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod med
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod nexthop
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-reflector-client
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-server-client
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft-reconfiguration
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast nexthop-setting
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast add-path-tx
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod aspath
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod med
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod nexthop
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn origin
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath replace-peer-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath private-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound route-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound route-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound unsuppress-map
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn enable
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-reflector-client
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-server-client
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft-reconfiguration
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn nexthop-setting
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn add-path-tx
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> password
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> enforce-first-as
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> passive-mode
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> nexthop-connected-check
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> multihop-ttl
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> description
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> shutdown
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> update-source
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> remote-as
nv unset vrf <vrf-id> router bgp route-export
nv unset vrf <vrf-id> router bgp route-export to-evpn
nv unset vrf <vrf-id> router bgp route-export to-evpn route-target
nv unset vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>
nv unset vrf <vrf-id> router bgp route-import
nv unset vrf <vrf-id> router bgp route-import from-evpn
nv unset vrf <vrf-id> router bgp route-import from-evpn route-target
nv unset vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>
nv unset vrf <vrf-id> router bgp timers
nv unset vrf <vrf-id> router bgp timers keepalive
nv unset vrf <vrf-id> router bgp timers hold
nv unset vrf <vrf-id> router bgp timers connection-retry
nv unset vrf <vrf-id> router bgp timers route-advertisement
nv unset vrf <vrf-id> router bgp timers conditional-advertise
nv unset vrf <vrf-id> router bgp confederation
nv unset vrf <vrf-id> router bgp confederation member-as
nv unset vrf <vrf-id> router bgp confederation id
nv unset vrf <vrf-id> router bgp dynamic-neighbor
nv unset vrf <vrf-id> router bgp dynamic-neighbor listen-range
nv unset vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id>
nv unset vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id> peer-group
nv unset vrf <vrf-id> router bgp dynamic-neighbor limit
nv unset vrf <vrf-id> router bgp neighbor
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id>
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities extended-nexthop
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities source-address
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as prepend
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as replace
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart mode
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod aspath
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod med
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod nexthop
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn origin
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath replace-peer-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath private-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound route-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound prefix-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound route-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound unsuppress-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound prefix-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound maximum
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-only
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination policy
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise regular
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise extended
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise large
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-reflector-client
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-server-client
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft-reconfiguration
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast nexthop-setting
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast add-path-tx
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod aspath
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod med
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod nexthop
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn origin
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath replace-peer-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath private-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound maximum
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-only
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination policy
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound route-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound prefix-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound route-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound unsuppress-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound prefix-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise regular
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise extended
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise large
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-reflector-client
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-server-client
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft-reconfiguration
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast nexthop-setting
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast add-path-tx
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod aspath
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod med
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod nexthop
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn origin
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath replace-peer-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath private-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound route-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound route-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound unsuppress-map
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-reflector-client
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-server-client
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft-reconfiguration
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn nexthop-setting
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn add-path-tx
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers keepalive
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers hold
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers connection-retry
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers route-advertisement
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> password
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> enforce-first-as
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> passive-mode
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop-connected-check
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> multihop-ttl
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> description
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> shutdown
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> update-source
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> enable
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> type
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> peer-group
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> remote-as
nv unset vrf <vrf-id> router bgp enable
nv unset vrf <vrf-id> router bgp autonomous-system
nv unset vrf <vrf-id> router bgp router-id
nv unset vrf <vrf-id> router bgp rd
nv unset vrf <vrf-id> router static
nv unset vrf <vrf-id> router static <route-id>
nv unset vrf <vrf-id> router static <route-id> distance
nv unset vrf <vrf-id> router static <route-id> distance <distance-id>
nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via
nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>
nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag
nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> interface
nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> vrf
nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> type
nv unset vrf <vrf-id> router static <route-id> distance <distance-id> tag
nv unset vrf <vrf-id> router static <route-id> via
nv unset vrf <vrf-id> router static <route-id> via <via-id>
nv unset vrf <vrf-id> router static <route-id> via <via-id> flag
nv unset vrf <vrf-id> router static <route-id> via <via-id> interface
nv unset vrf <vrf-id> router static <route-id> via <via-id> vrf
nv unset vrf <vrf-id> router static <route-id> via <via-id> type
nv unset vrf <vrf-id> router static <route-id> tag
nv unset vrf <vrf-id> router static <route-id> address-family
nv unset vrf <vrf-id> router pim
nv unset vrf <vrf-id> router pim timers
nv unset vrf <vrf-id> router pim timers keep-alive
nv unset vrf <vrf-id> router pim timers rp-keep-alive
nv unset vrf <vrf-id> router pim ecmp
nv unset vrf <vrf-id> router pim ecmp enable
nv unset vrf <vrf-id> router pim ecmp rebalance
nv unset vrf <vrf-id> router pim msdp-mesh-group
nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>
nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address
nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>
nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address
nv unset vrf <vrf-id> router pim address-family
nv unset vrf <vrf-id> router pim address-family ipv4-unicast
nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover
nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover action
nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list
nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp
nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>
nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range
nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>
nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list
nv unset vrf <vrf-id> router pim address-family ipv4-unicast ssm-prefix-list
nv unset vrf <vrf-id> router pim address-family ipv4-unicast register-accept-list
nv unset vrf <vrf-id> router pim address-family ipv4-unicast send-v6-secondary
nv unset vrf <vrf-id> router pim enable
nv unset vrf <vrf-id> router ospf
nv unset vrf <vrf-id> router ospf area
nv unset vrf <vrf-id> router ospf area <area-id>
nv unset vrf <vrf-id> router ospf area <area-id> filter-list
nv unset vrf <vrf-id> router ospf area <area-id> filter-list in
nv unset vrf <vrf-id> router ospf area <area-id> filter-list out
nv unset vrf <vrf-id> router ospf area <area-id> range
nv unset vrf <vrf-id> router ospf area <area-id> range <range-id>
nv unset vrf <vrf-id> router ospf area <area-id> range <range-id> suppress
nv unset vrf <vrf-id> router ospf area <area-id> range <range-id> cost
nv unset vrf <vrf-id> router ospf area <area-id> network
nv unset vrf <vrf-id> router ospf area <area-id> network <network-id>
nv unset vrf <vrf-id> router ospf area <area-id> type
nv unset vrf <vrf-id> router ospf area <area-id> default-lsa-cost
nv unset vrf <vrf-id> router ospf default-originate
nv unset vrf <vrf-id> router ospf default-originate enable
nv unset vrf <vrf-id> router ospf default-originate metric
nv unset vrf <vrf-id> router ospf default-originate metric-type
nv unset vrf <vrf-id> router ospf default-originate route-map
nv unset vrf <vrf-id> router ospf default-originate always
nv unset vrf <vrf-id> router ospf distance
nv unset vrf <vrf-id> router ospf distance external
nv unset vrf <vrf-id> router ospf distance inter-area
nv unset vrf <vrf-id> router ospf distance intra-area
nv unset vrf <vrf-id> router ospf max-metric
nv unset vrf <vrf-id> router ospf max-metric administrative
nv unset vrf <vrf-id> router ospf max-metric on-shutdown
nv unset vrf <vrf-id> router ospf max-metric on-startup
nv unset vrf <vrf-id> router ospf log
nv unset vrf <vrf-id> router ospf log adjacency-changes
nv unset vrf <vrf-id> router ospf redistribute
nv unset vrf <vrf-id> router ospf redistribute static
nv unset vrf <vrf-id> router ospf redistribute static enable
nv unset vrf <vrf-id> router ospf redistribute static metric
nv unset vrf <vrf-id> router ospf redistribute static metric-type
nv unset vrf <vrf-id> router ospf redistribute static route-map
nv unset vrf <vrf-id> router ospf redistribute connected
nv unset vrf <vrf-id> router ospf redistribute connected enable
nv unset vrf <vrf-id> router ospf redistribute connected metric
nv unset vrf <vrf-id> router ospf redistribute connected metric-type
nv unset vrf <vrf-id> router ospf redistribute connected route-map
nv unset vrf <vrf-id> router ospf redistribute kernel
nv unset vrf <vrf-id> router ospf redistribute kernel enable
nv unset vrf <vrf-id> router ospf redistribute kernel metric
nv unset vrf <vrf-id> router ospf redistribute kernel metric-type
nv unset vrf <vrf-id> router ospf redistribute kernel route-map
nv unset vrf <vrf-id> router ospf redistribute bgp
nv unset vrf <vrf-id> router ospf redistribute bgp enable
nv unset vrf <vrf-id> router ospf redistribute bgp metric
nv unset vrf <vrf-id> router ospf redistribute bgp metric-type
nv unset vrf <vrf-id> router ospf redistribute bgp route-map
nv unset vrf <vrf-id> router ospf timers
nv unset vrf <vrf-id> router ospf timers lsa
nv unset vrf <vrf-id> router ospf timers lsa min-arrival
nv unset vrf <vrf-id> router ospf timers lsa throttle
nv unset vrf <vrf-id> router ospf timers spf
nv unset vrf <vrf-id> router ospf timers spf delay
nv unset vrf <vrf-id> router ospf timers spf holdtime
nv unset vrf <vrf-id> router ospf timers spf max-holdtime
nv unset vrf <vrf-id> router ospf timers refresh
nv unset vrf <vrf-id> router ospf enable
nv unset vrf <vrf-id> router ospf reference-bandwidth
nv unset vrf <vrf-id> router ospf rfc1583-compatible
nv unset vrf <vrf-id> router ospf router-id
nv unset vrf <vrf-id> ptp
nv unset vrf <vrf-id> ptp enable
nv unset vrf <vrf-id> table
nv unset nve
nv unset nve vxlan
nv unset nve vxlan mlag
nv unset nve vxlan mlag shared-address
nv unset nve vxlan source
nv unset nve vxlan source address
nv unset nve vxlan flooding
nv unset nve vxlan flooding head-end-replication
nv unset nve vxlan flooding head-end-replication <hrep-id>
nv unset nve vxlan flooding enable
nv unset nve vxlan flooding multicast-group
nv unset nve vxlan encapsulation
nv unset nve vxlan encapsulation dscp
nv unset nve vxlan encapsulation dscp action
nv unset nve vxlan encapsulation dscp value
nv unset nve vxlan decapsulation
nv unset nve vxlan decapsulation dscp
nv unset nve vxlan decapsulation dscp action
nv unset nve vxlan enable
nv unset nve vxlan mac-learning
nv unset nve vxlan port
nv unset nve vxlan arp-nd-suppress
nv unset nve vxlan mtu
nv unset acl
nv unset acl <acl-id>
nv unset acl <acl-id> rule
nv unset acl <acl-id> rule <rule-id>
nv unset acl <acl-id> rule <rule-id> match
nv unset acl <acl-id> rule <rule-id> match ip
nv unset acl <acl-id> rule <rule-id> match ip source-port
nv unset acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>
nv unset acl <acl-id> rule <rule-id> match ip dest-port
nv unset acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>
nv unset acl <acl-id> rule <rule-id> match ip fragment
nv unset acl <acl-id> rule <rule-id> match ip ecn
nv unset acl <acl-id> rule <rule-id> match ip ecn flags
nv unset acl <acl-id> rule <rule-id> match ip ecn ip-ect
nv unset acl <acl-id> rule <rule-id> match ip tcp
nv unset acl <acl-id> rule <rule-id> match ip tcp flags
nv unset acl <acl-id> rule <rule-id> match ip tcp mask
nv unset acl <acl-id> rule <rule-id> match ip tcp state
nv unset acl <acl-id> rule <rule-id> match ip source-ip
nv unset acl <acl-id> rule <rule-id> match ip dest-ip
nv unset acl <acl-id> rule <rule-id> match ip protocol
nv unset acl <acl-id> rule <rule-id> match ip dscp
nv unset acl <acl-id> rule <rule-id> match ip icmp-type
nv unset acl <acl-id> rule <rule-id> match ip icmpv6-type
nv unset acl <acl-id> rule <rule-id> match mac
nv unset acl <acl-id> rule <rule-id> match mac source-mac
nv unset acl <acl-id> rule <rule-id> match mac source-mac-mask
nv unset acl <acl-id> rule <rule-id> match mac dest-mac
nv unset acl <acl-id> rule <rule-id> match mac dest-mac-mask
nv unset acl <acl-id> rule <rule-id> match mac protocol
nv unset acl <acl-id> rule <rule-id> match vlan
nv unset acl <acl-id> rule <rule-id> action
nv unset acl <acl-id> rule <rule-id> action permit
nv unset acl <acl-id> rule <rule-id> action deny
nv unset acl <acl-id> rule <rule-id> action log
nv unset acl <acl-id> rule <rule-id> action log log-prefix
nv unset acl <acl-id> rule <rule-id> action set
nv unset acl <acl-id> rule <rule-id> action set dscp
nv unset acl <acl-id> rule <rule-id> action set class
nv unset acl <acl-id> rule <rule-id> action set cos
nv unset acl <acl-id> rule <rule-id> action erspan
nv unset acl <acl-id> rule <rule-id> action erspan source-ip
nv unset acl <acl-id> rule <rule-id> action erspan dest-ip
nv unset acl <acl-id> rule <rule-id> action erspan ttl
nv unset acl <acl-id> rule <rule-id> action police
nv unset acl <acl-id> rule <rule-id> action police mode
nv unset acl <acl-id> rule <rule-id> action police burst
nv unset acl <acl-id> rule <rule-id> action police rate
nv unset acl <acl-id> rule <rule-id> action police class
nv unset acl <acl-id> rule <rule-id> action span
nv unset acl <acl-id> rule <rule-id> remark
nv unset acl <acl-id> type
nv action clear mlag lacp-conflict
nv action clear qos buffer pool
nv action clear qos buffer multicast-switch-priority
nv action clear interface <interface-id> bond mlag lacp-conflict
nv action clear interface <interface-id> qos counter
nv action clear interface <interface-id> qos roce counters
nv action clear interface <interface-id> qos buffer
nv action disconnect system aaa user <user-id>
nv config apply [<revision>]
nv config save
nv config replace <nvue-file>
nv config detach
nv config diff [<revision>] [<revision>]
nv config show
nv config find <search-string>
nv config patch <nvue-file>
nv config history [<revision>]
```

## Show a Command Description

To see a description for a command, type the command with `-h` at the end:

```
cumulus@leaf01:mgmt:~$ nv set mlag backup -h
usage: 
  nv [options] set mlag backup <backup-ip>

Description:
  backup                Set of MLAG backups

Identifiers:
  <backup-ip>           Backup IP of MLAG peer (ipv4 | ipv6)

Output Options:
  -o <format>, --output <format>
                        Supported formats: json, yaml, auto, constable, end-table, commands (default:auto)
  --color (on|off|auto)
                        Toggle coloring of output (default: auto)
  --paginate (on|off|auto)
                        Whether to send output to a pager (default: off)

General Options:
  -h, --help            Show help.
```

When you use `-h`, replace any variables in the command with a value. For example, for the `nv set vrf <vrf-id> router pim` command, type `nv set vrf default router pim -h`:

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim -h
usage: 
  nv [options] set vrf <vrf-id> router pim [address-family ...]
  nv [options] set vrf <vrf-id> router pim [ecmp ...]
  nv [options] set vrf <vrf-id> router pim [enable ...]
  nv [options] set vrf <vrf-id> router pim [msdp-mesh-group ...]
  nv [options] set vrf <vrf-id> router pim [timers ...]

Description:
  pim                   PIM VRF configuration.

Identifiers:
  <vrf-id>              VRF (vrf-name)

Attributes:
  address-family        Address family specific configuration
  ecmp                  Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.
  enable                Turn the feature 'on' or 'off'.  The default is 'off'.
  msdp-mesh-group       To connect multiple PIM-SM multicast domains using RPs.
  timers                Timers

Output Options:
  -o <format>, --output <format>
                        Supported formats: json, yaml, auto, constable, end-table, commands (default:auto)
  --color (on|off|auto)
                        Toggle coloring of output (default: auto)
  --paginate (on|off|auto)
                        Whether to send output to a pager (default: off)

General Options:
  -h, --help            Show help.
```
