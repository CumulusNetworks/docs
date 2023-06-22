---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.3 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.3, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.3, see the {{<link title="Cumulus Linux 5.3 Release Notes" text="Cumulus Linux 5.3 Release Notes">}}.
- To upgrade to Cumulus Linux 5.3, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

<!-- vale off -->
## What's New in Cumulus Linux 5.3.1
<!-- vale on -->
Cumulus Linux 5.3.1 provides bug fixes.

<!-- vale off -->
## What's New in Cumulus Linux 5.3.0
<!-- vale on -->
Cumulus Linux 5.3.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN3750-SX (200G Spectrum-2) available for early access

{{%notice warning%}}
The NVIDIA SN3750-SX switch is available for [early access]({{<ref "/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined" >}}) and open to customer feedback. Do not use this switch in production; it is not supported through NVIDIA networking support.
{{%/notice%}}

### New Features and Enhancements

- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="Configure-SNMP" text="SNMP Server">}} and {{<link url="Configure-SNMP-Traps" text="SNMP trap">}} commands
  - {{<link url="Quality-of-Service" text="QoS commands">}} to configure COS and DSCP marking, egress queue mapping, egress traffic scheduling, PFC, ECN, and traffic pools
  - {{<link url="Configuring-switchd" text="switchd commands">}} to configure the statistic polling interval for physical and logical interfaces, log level for debugging, DSCP settings for encapsulation and decapsulation, host route preference, ACL mode, and reserved VLAN range
  - New {{<link url="Monitoring-and-Troubleshooting/#show-system-information" text="nv show system commands">}} include `nv show system memory` and `nv show system cpu`
  - New BGP configuration commands include {{<link url="Optional-BGP-Configuration/#bgp-dynamic-neighbors" text="BGP dynamic neighbor">}}, {{<link url="Optional-BGP-Configuration/#update-source" text="BGP update source">}}, {{<link url="Optional-BGP-Configuration/#bgp-neighbor-shutdown" text="BGP  neighbor shutdown">}}
  - New route map {{<link url="Route-Filtering-and-Redistribution/#match-and-set-statements" text="match and set statements">}} enable you to match on an EVPN default route, and set the BGP community, metric, originator ID, and forwarding address
  - {{<link title="What Just Happened (WJH)" text="WJH commands">}}
  - {{<link url="Storm-Control" text="Storm Control commands">}}
  - {{<link url="Prescriptive-Topology-Manager-PTM/#check-link-state" text="PTM enable command">}} to check link state
  - Support for hyphens in hostnames, VRF, route map, next hop groups, prefix list, AS path list, community list, and ACL names
  - {{<link url="Interface-Configuration-and-Management/#fast-linkup" text="Fast link up command">}} (`nv set interface <interface-id> link fast-linkup on`) to support fast link up between Spectrum1 switches and certain optic network interface cards that require links to come up fast
  - Improved error handling when applying invalid interface configuration with NVUE
  - New commands:
   {{< tabs "TabID40 ">}}
{{< tab "show commands ">}}

```
nv show action <action-job-id>
nv show interface <interface-id> qos congestion-control
nv show interface <interface-id> qos congestion-control traffic-class
nv show interface <interface-id> qos congestion-control traffic-class <if-qos-tc-id>
nv show interface <interface-id> qos egress-queue-mapping
nv show interface <interface-id> qos egress-queue-mapping switch-priority
nv show interface <interface-id> qos egress-queue-mapping switch-priority <qos-sp-id>
nv show interface <interface-id> qos egress-scheduler
nv show interface <interface-id> qos egress-scheduler traffic-class
nv show interface <interface-id> qos egress-scheduler traffic-class <if-qos-tc-id>
nv show interface <interface-id> qos mapping
nv show interface <interface-id> qos mapping dscp
nv show interface <interface-id> qos mapping dscp <qos-dscp-id>
nv show interface <interface-id> qos mapping pcp
nv show interface <interface-id> qos mapping pcp <qos-pcp-id>
nv show interface <interface-id> qos pfc
nv show interface <interface-id> storm-control
nv show nve vxlan decapsulation
nv show nve vxlan decapsulation dscp
nv show nve vxlan encapsulation
nv show nve vxlan encapsulation dscp
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
nv show qos mapping
nv show qos mapping <profile-id>
nv show qos mapping <profile-id> dscp
nv show qos mapping <profile-id> dscp <qos-dscp-id>
nv show qos mapping <profile-id> pcp
nv show qos mapping <profile-id> pcp <qos-pcp-id>
nv show qos pfc
nv show qos pfc <profile-id>
nv show qos pfc <profile-id> switch-priority
nv show qos pfc <profile-id> switch-priority <qos-sp-id>
nv show qos traffic-pool
nv show qos traffic-pool <traffic-pool-id>
nv show qos traffic-pool <traffic-pool-id> switch-priority
nv show qos traffic-pool <traffic-pool-id> switch-priority <qos-sp-id>
nv show router ptm
nv show service snmp-server
nv show service snmp-server listening-address
nv show service snmp-server listening-address <listening-address-id>
nv show service snmp-server mibs
nv show service snmp-server readonly-community
nv show service snmp-server readonly-community <readonly-community-id>
nv show service snmp-server readonly-community <readonly-community-id> access
nv show service snmp-server readonly-community <readonly-community-id> access <access-id>
nv show service snmp-server readonly-community-v6
nv show service snmp-server readonly-community-v6 <readonly-community-id>
nv show service snmp-server readonly-community-v6 <readonly-community-id> access
nv show service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
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
nv show service snmp-server trap-destination <trap-destination-id> username
nv show service snmp-server trap-destination <trap-destination-id> username <username-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv show service snmp-server trap-link-down
nv show service snmp-server trap-link-up
nv show service snmp-server trap-snmp-auth-failures
nv show service snmp-server username
nv show service snmp-server username <username-id>
nv show service snmp-server username <username-id> auth-md5
nv show service snmp-server username <username-id> auth-md5 <auth-id>
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server username <username-id> auth-none
nv show service snmp-server username <username-id> auth-sha
nv show service snmp-server username <username-id> auth-sha <auth-id>
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server viewname
nv show service snmp-server viewname <viewname-id>
nv show system acl
nv show system counter
nv show system counter polling-interval
nv show system cpu
nv show system forwarding programming
nv show system global reserved vlan internal
nv show system memory
nv show system wjh
nv show system wjh channel
nv show system wjh channel <channel-id>
nv show system wjh channel <channel-id> trigger
nv show system wjh packet-buffer
nv show vrf <vrf-id> router bgp dynamic-neighbor
nv show vrf <vrf-id> router bgp dynamic-neighbor listen-range
nv show vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id>
nv show vrf <vrf-id> router nexthop-tracking
nv show vrf <vrf-id> router nexthop-tracking <afi>
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id>
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol
nv show vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol <nht-protocol-id>
```

{{< /tab >}}
{{< tab "set commands ">}}

```
nv set interface <interface-id> ip neighbor-discovery home-agent enable (on|off)
nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime (0-4294967295|infinite)
nv set interface <interface-id> link fast-linkup (on|off)
nv set interface <interface-id> qos
nv set interface <interface-id> qos congestion-control
nv set interface <interface-id> qos congestion-control profile <profile-name>
nv set interface <interface-id> qos egress-scheduler
nv set interface <interface-id> qos egress-scheduler profile <profile-name>
nv set interface <interface-id> qos mapping
nv set interface <interface-id> qos mapping profile <profile-name>
nv set interface <interface-id> qos pfc
nv set interface <interface-id> qos pfc profile <profile-name>
nv set interface <interface-id> storm-control
nv set interface <interface-id> storm-control broadcast 1-4294967295
nv set interface <interface-id> storm-control multicast 1-4294967295
nv set interface <interface-id> storm-control unknown-unicast 1-4294967295
nv set nve vxlan decapsulation
nv set nve vxlan decapsulation dscp
nv set nve vxlan decapsulation dscp action (derive|copy|preserve)
nv set nve vxlan encapsulation
nv set nve vxlan encapsulation dscp
nv set nve vxlan encapsulation dscp action (derive|copy|set)
nv set nve vxlan encapsulation dscp value (0-63|af11|af12|af13|af21|af22|af23|af31|af32|af33|af41|af42|af43|cs1|cs2|cs3|cs4|cs5|cs6|cs7|be|ef)
nv set qos congestion-control <profile-id>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> ecn (enable|disable)
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> max-threshold <value>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> min-threshold <value>
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> probability 0-100
nv set qos congestion-control <profile-id> traffic-class <qos-tc-id> red (enable|disable)
nv set qos egress-queue-mapping <profile-id>
nv set qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id>
nv set qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id> traffic-class 0-7
nv set qos egress-scheduler <profile-id>
nv set qos egress-scheduler <profile-id> traffic-class <qos-tc-id>
nv set qos egress-scheduler <profile-id> traffic-class <qos-tc-id> bw-percent 0-100
nv set qos egress-scheduler <profile-id> traffic-class <qos-tc-id> mode (dwrr|strict)
nv set qos mapping <profile-id>
nv set qos mapping <profile-id> dscp <qos-dscp-id>
nv set qos mapping <profile-id> dscp <qos-dscp-id> switch-priority 0-7
nv set qos mapping <profile-id> pcp <qos-pcp-id>
nv set qos mapping <profile-id> pcp <qos-pcp-id> switch-priority 0-7
nv set qos mapping <profile-id> port-default-sp 0-7
nv set qos mapping <profile-id> trust (l2|l3|port|both)
nv set qos pfc <profile-id>
nv set qos pfc <profile-id> cable-length 1-100000
nv set qos pfc <profile-id> port-buffer <value>
nv set qos pfc <profile-id> rx (enable|disable)
nv set qos pfc <profile-id> switch-priority <qos-sp-id>
nv set qos pfc <profile-id> tx (enable|disable)
nv set qos pfc <profile-id> xoff-threshold <value>
nv set qos pfc <profile-id> xon-threshold <value>
nv set qos traffic-pool <traffic-pool-id>
nv set qos traffic-pool <traffic-pool-id> memory-percent 1-100
nv set qos traffic-pool <traffic-pool-id> switch-priority <qos-sp-id>
nv set router ptm
nv set router ptm enable (on|off)
nv set service snmp-server
nv set service snmp-server enable (on|off)
nv set service snmp-server listening-address <listening-address-id>
nv set service snmp-server listening-address <listening-address-id> vrf <vrf-name>
nv set service snmp-server mibs (cumulus-sensor-mib|cumulus-status-mib)
nv set service snmp-server readonly-community <readonly-community-id>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id> oid <oid>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id> view <value>
nv set service snmp-server readonly-community-v6 <readonly-community-id>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> oid <oid>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> view <value>
nv set service snmp-server system-contact <value>
nv set service snmp-server system-location <value>
nv set service snmp-server system-name <value>
nv set service snmp-server trap-cpu-load-average
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id>
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id>
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute <fifteen-minute-id>
nv set service snmp-server trap-destination <trap-destination-id>
nv set service snmp-server trap-destination <trap-destination-id> community-password <community-password-id>
nv set service snmp-server trap-destination <trap-destination-id> community-password <community-password-id> version (1|2c)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id> version (1|2c)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-link-down
nv set service snmp-server trap-link-down check-frequency 5-300
nv set service snmp-server trap-link-up
nv set service snmp-server trap-link-up check-frequency 5-300
nv set service snmp-server trap-snmp-auth-failures
nv set service snmp-server username <username-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> view <value>
nv set service snmp-server username <username-id> auth-none
nv set service snmp-server username <username-id> auth-none oid <oid>
nv set service snmp-server username <username-id> auth-none view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> view <value>
nv set service snmp-server viewname <viewname-id>
nv set service snmp-server viewname <viewname-id> excluded <snmp-branch>
nv set service snmp-server viewname <viewname-id> included <snmp-branch>
nv set system acl
nv set system acl mode (atomic|non-atomic)
nv set system counter
nv set system counter polling-interval
nv set system counter polling-interval logical-interface 1-30
nv set system counter polling-interval physical-interface 1-10
nv set system forwarding host-route-preference (route|neighbour|route-and-neighbour)
nv set system forwarding programming
nv set system forwarding programming log-level (debug|info|critical|warning|error)
nv set system global reserved vlan internal
nv set system global reserved vlan internal range <vlan-range>
nv set system wjh
nv set system wjh channel <channel-id>
nv set system wjh channel <channel-id> trigger (l1|l2|l3|tunnel)
nv set system wjh enable (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> shutdown (on|off)
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> update-source (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> shutdown (on|off)
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> update-source (<interface-name>|<ipv4>|<ipv6>)
nv set vrf <vrf-id> router nexthop-tracking <afi>
nv set vrf <vrf-id> router nexthop-tracking <afi> resolved-via-default (on|off)
nv set vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id>
nv set vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol
```

{{< /tab >}}
{{< tab "unset commands ">}}

```
nv unset interface <interface-id> ip neighbor-discovery home-agent enable
nv unset interface <interface-id> link fast-linkup
nv unset interface <interface-id> qos
nv unset interface <interface-id> qos congestion-control
nv unset interface <interface-id> qos congestion-control profile
nv unset interface <interface-id> qos egress-scheduler
nv unset interface <interface-id> qos egress-scheduler profile
nv unset interface <interface-id> qos mapping
nv unset interface <interface-id> qos mapping profile
nv unset interface <interface-id> qos pfc
nv unset interface <interface-id> qos pfc profile
nv unset interface <interface-id> storm-control
nv unset interface <interface-id> storm-control broadcast
nv unset interface <interface-id> storm-control multicast
nv unset interface <interface-id> storm-control unknown-unicast
nv unset nve vxlan decapsulation
nv unset nve vxlan decapsulation dscp
nv unset nve vxlan decapsulation dscp action
nv unset nve vxlan encapsulation
nv unset nve vxlan encapsulation dscp
nv unset nve vxlan encapsulation dscp action
nv unset nve vxlan encapsulation dscp value
nv unset qos congestion-control
nv unset qos congestion-control <profile-id>
nv unset qos congestion-control <profile-id> traffic-class
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id>
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> ecn
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> max-threshold
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> min-threshold
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> probability
nv unset qos congestion-control <profile-id> traffic-class <qos-tc-id> red
nv unset qos egress-queue-mapping
nv unset qos egress-queue-mapping <profile-id>
nv unset qos egress-queue-mapping <profile-id> switch-priority
nv unset qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id>
nv unset qos egress-queue-mapping <profile-id> switch-priority <qos-sp-id> traffic-class
nv unset qos egress-scheduler
nv unset qos egress-scheduler <profile-id>
nv unset qos egress-scheduler <profile-id> traffic-class
nv unset qos egress-scheduler <profile-id> traffic-class <qos-tc-id>
nv unset qos egress-scheduler <profile-id> traffic-class <qos-tc-id> bw-percent
nv unset qos egress-scheduler <profile-id> traffic-class <qos-tc-id> mode
nv unset qos mapping
nv unset qos mapping <profile-id>
nv unset qos mapping <profile-id> dscp
nv unset qos mapping <profile-id> dscp <qos-dscp-id>
nv unset qos mapping <profile-id> dscp <qos-dscp-id> switch-priority
nv unset qos mapping <profile-id> pcp
nv unset qos mapping <profile-id> pcp <qos-pcp-id>
nv unset qos mapping <profile-id> pcp <qos-pcp-id> switch-priority
nv unset qos mapping <profile-id> port-default-sp
nv unset qos mapping <profile-id> trust
nv unset qos pfc
nv unset qos pfc <profile-id>
nv unset qos pfc <profile-id> cable-length
nv unset qos pfc <profile-id> port-buffer
nv unset qos pfc <profile-id> rx
nv unset qos pfc <profile-id> switch-priority
nv unset qos pfc <profile-id> switch-priority <qos-sp-id>
nv unset qos pfc <profile-id> tx
nv unset qos pfc <profile-id> xoff-threshold
nv unset qos pfc <profile-id> xon-threshold
nv unset qos traffic-pool
nv unset qos traffic-pool <traffic-pool-id>
nv unset qos traffic-pool <traffic-pool-id> memory-percent
nv unset qos traffic-pool <traffic-pool-id> switch-priority
nv unset qos traffic-pool <traffic-pool-id> switch-priority <qos-sp-id>
nv unset router ptm
nv unset router ptm enable
nv unset service snmp-server
nv unset service snmp-server enable
nv unset service snmp-server listening-address
nv unset service snmp-server listening-address <listening-address-id>
nv unset service snmp-server listening-address <listening-address-id> vrf
nv unset service snmp-server mibs
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
nv unset service snmp-server system-contact
nv unset service snmp-server system-location
nv unset service snmp-server system-name
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
nv unset service snmp-server trap-destination <trap-destination-id> username
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id> version
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-link-down
nv unset service snmp-server trap-link-down check-frequency
nv unset service snmp-server trap-link-up
nv unset service snmp-server trap-link-up check-frequency
nv unset service snmp-server trap-snmp-auth-failures
nv unset service snmp-server username
nv unset service snmp-server username <username-id>
nv unset service snmp-server username <username-id> auth-md5
nv unset service snmp-server username <username-id> auth-md5 <auth-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> view
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> view
nv unset service snmp-server username <username-id> auth-md5 <auth-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> view
nv unset service snmp-server username <username-id> auth-none
nv unset service snmp-server username <username-id> auth-none oid
nv unset service snmp-server username <username-id> auth-none view
nv unset service snmp-server username <username-id> auth-sha
nv unset service snmp-server username <username-id> auth-sha <auth-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> view
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> view
nv unset service snmp-server username <username-id> auth-sha <auth-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> view
nv unset service snmp-server viewname
nv unset service snmp-server viewname <viewname-id>
nv unset service snmp-server viewname <viewname-id> excluded
nv unset service snmp-server viewname <viewname-id> included
nv unset system acl
nv unset system acl mode
nv unset system counter
nv unset system counter polling-interval
nv unset system counter polling-interval logical-interface
nv unset system counter polling-interval physical-interface
nv unset system forwarding host-route-preference
nv unset system forwarding programming
nv unset system forwarding programming log-level
nv unset system global reserved vlan internal
nv unset system global reserved vlan internal range
nv unset system wjh
nv unset system wjh channel
nv unset system wjh channel <channel-id>
nv unset system wjh channel <channel-id> trigger
nv unset system wjh enable
nv unset vrf <vrf-id> router bgp dynamic-neighbor
nv unset vrf <vrf-id> router bgp dynamic-neighbor limit
nv unset vrf <vrf-id> router bgp dynamic-neighbor listen-range
nv unset vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id>
nv unset vrf <vrf-id> router bgp dynamic-neighbor listen-range <ip-sub-prefix-id> peer-group
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> shutdown
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> update-source
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> shutdown
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> update-source
nv unset vrf <vrf-id> router nexthop-tracking
nv unset vrf <vrf-id> router nexthop-tracking <afi>
nv unset vrf <vrf-id> router nexthop-tracking <afi> resolved-via-default
nv unset vrf <vrf-id> router nexthop-tracking <afi> route-map
nv unset vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id>
nv unset vrf <vrf-id> router nexthop-tracking <afi> route-map <nht-routemap-id> protocol
```

{{< /tab >}}
{{< /tabs >}}
  <!--- Commands changed from `enable on` and `enable off` to `set enable` and `unset enable` (the `enable on` and `enable off` commands continue to be supported for backward compatability)
  <!--- Obfuscated passwords to protect passwords from casual viewing
  <!-- - {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="Search for a specific configuration">}} in the entire object model-->
{{%notice info%}}
Cumulus Linux 5.3 includes the NVUE object model. After you upgrade to Cumulus Linux 5.3, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
