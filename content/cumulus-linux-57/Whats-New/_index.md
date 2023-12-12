---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.7 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.7, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.7, see the {{<link title="Cumulus Linux 5.7 Release Notes" text="Cumulus Linux 5.7 Release Notes">}}.
- To upgrade to Cumulus Linux 5.7, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.7.0
<!-- vale on -->
Cumulus Linux 5.7.0 supports new platforms, contains several new features and improvements, and provides bug fixes.

### Platforms

### New Features and Enhancements

- {{<link url="802.1X-Interfaces" text="802.1x support">}}
- {{<link url="MAC-Address-Translation" text="MAC address translation">}}
- {{<link url="ASIC-Monitoring" text="Updated histograms for ASIC monitoring">}}
- {{<link url="Pulse-Per-Second-PPS" text="Pulse Per Second (PPS) synchronization">}}
- {{<link url="BGP-Weighted-Equal-Cost-Multipath/#weight-normalization" text="Weight normalization for BGP weighted ECMP">}} 
- NVUE enhancements include:
  - {{<link url="Port-Security" text="Port security commands">}}
  - {{<link url="Network-Address-Translation-NAT" text="NAT commands">}}
  - {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="ISSU maintenance mode commands">}}
  - {{<link url="RADIUS-AAA" text="RADIUS AAA commands">}}
  - {{<link url="Interface-Configuration-and-Management/#link-flap-protection" text="Link flap protection commands ">}}
  - {{<link title="Spanning Tree and Rapid Spanning Tree - STP" text="MLAG support for PVST & PVRST VLAN-aware bridge mode">}}
  - {{<link title="Setting the Date and Time/#set-the-date-and-time" text="Set date and time command">}}
  - {{<link url="Role-Based-Access-Control" text="Role-based access control">}}
  - {{<link url="NVUE-API/#certificates" text="Manage certificate commands">}} for the NVUE REST API
  - {{<link url="Optional-BGP-Configuration/#bgp-input-and-ouput-message-queue-limit" text="BGP Input and Ouput Message Queue Limit">}} commands
  - {{<link url="EVPN-Enhancements/#configure-a-site-id-for-mlag" text="Command to configure a site ID for MLAG">}}
  - {{<link url="DHCP-Relays/#dhcp-agent-information-option-option-82" text="DHCP agent information (Option 82) commands">}}
  - {{<link url="DHCP-Servers/#basic-configuration" text="DNS server interface name command">}}
  - Enhanced {{<link url="NVUE-API/#certificates" text="nv show system api">}} command output to show the certificate used for the API and additional {{<link url="NVUE-API/#certificates" text="nv show system api certificate">}} commands to show information about the certificates installed on the switch.
  - Commands to show {{<link url="Troubleshooting-EVPN" text="VLAN to VNI mapping for all bridges">}} and {{<link url="Troubleshooting-EVPN" text="VLAN to VNI mapping for a specific bridge">}}
  - Commands to show the {{<link url="Address-Resolution-Protocol-ARP/#show-the-arp-table" text="ARP table">}} and {{<link url="Neighbor-Discovery-ND#show-the-ip-neighbor-table" text="ND table">}} and to add static entries to the {{<link url="Address-Resolution-Protocol-ARP/#add-static-arp-table-entries" text="ARP table">}} and {{<link url="Neighbor-Discovery-ND/#add-static-ip-neighbor-table-entries" text="ND table">}}
  - Enhanced {{<link url="NVUE-CLI/#configuration-management-commands" text="show config history">}} command output now in table format
  - Improvements to {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="nv show mlag command outputs">}}
  - FRR now restarts only when you enable or disable a routing protocol, change the BGP ASN, or disable the SNMP server.

{{< expand "Commands that no longer require a switchd restart" >}}

```
nv set/unset system acl mode non-atomic
nv set/unset system acl mode atomic
nv set/unset system forwarding host-route-preference route
nv set/unset system forwarding host-route-preference neighbor
nv set/unset system forwarding host-route-preference route-and-neighbour
nv set/unset nve vxlan encapsulation dscp action
nv set/unset nve vxlan encapsulation dscp value
nv set/unset nve vxlan decapsulation dscp action
nv set/unset interface <interface-id> router adaptive-routing link-utilization-threshold 
nv set/unset router bgp wait-for-install
```

{{< /expand >}}

{{< expand "Changed Commands" >}}

| Previous Command  |  New Command  |
| ------------ | ------------- |
| `nv set router pim timers keep-alive`| `nv set router pim timers keepalive` |
| `nv set router pim timers rp-keep-alive`| `nv set router pim timers rp-keepalive` |
| `nv set vrf default router pim timers keep-alive`| `nv set vrf default router pim timers keepalive` |
| `nv set vrf default router pim timers rp-keep-alive`| `nv set vrf default router pim timers rp-keepalive` |
| `nv set acl <acl-ID> rule <rule-ID> match ip dest-port <port>` | `nv set acl <acl-ID> rule <rule-ID> match ip <protocol>    dest-port <port>`|
| `nv set acl <acl-ID> rule <rule-ID> match ip source-port <port>`| `nv set acl <acl-ID> rule <rule-ID> match ip <protocol>    source-port <port>` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast` | `nv unset vrf <vrf-id> router pim address-family ipv4` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover` | `nv set vrf <vrf-id> router pim address-family ipv4 spt-switchover`|
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover action` | `nv set vrf <vrf-id> router pim address-family ipv4 spt-switchover action` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list` | `nv set vrf <vrf-id> router pim address-family ipv4 spt-switchover prefix-list` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast rp` | `nv set vrf <vrf-id> router pim address-family ipv4 rp` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>` | `nv set vrf <vrf-id> router pim address-family ipv4 rp <rp-id>` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range` | `nv set vrf <vrf-id> router pim address-family ipv4 rp <rp-id> group-range` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>` | `nv set vrf <vrf-id> router pim address-family ipv4 rp <rp-id> group-range <group-range-id>` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list` | `nv set vrf <vrf-id> router pim address-family ipv4 rp <rp-id> prefix-list` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast ssm-prefix-list` | `nv set vrf <vrf-id> router pim address-family ipv4 ssm-prefix-list` |
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast register-accept-list` | `nv set vrf <vrf-id> router pim address-family ipv4 register-accept-list`|
| `nv set vrf <vrf-id> router pim address-family ipv4-unicast send-v6-secondary`| `nv set vrf <vrf-id> router pim address-family ipv4 send-v6-secondary` |
| `nv set system aaa tacacs authorization <privilege-level-id> role (nvue-monitor system-admin nvue-admin)` |
`nv set system aaa tacacs authorization <privilege-level-id> role <value>`|
| `nv show interface <interface-id> synce counters` | `nv show interface <interface-id> counters synce`|
| `nv show acl <acl-id> rule <rule-id> match ip source-port` |`nv show acl <acl-id> rule <rule-id> match ip udp source-port`<br>`nv show acl <acl-id> rule <rule-id> match ip tcp source-port` |
| `nv show acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>` | `nv show acl <acl-id> rule <rule-id> match ip udp source-port <ip-port-id>` <br>`nv show acl <acl-id> rule <rule-id> match ip tcp source-port <ip-port-id>`|
| `nv show acl <acl-id> rule <rule-id> match ip dest-port` | `nv show acl <acl-id> rule <rule-id> match ip udp dest-port`<br>`nv show acl <acl-id> rule <rule-id> match ip tcp dest-port`|
| `nv show acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>` |`nv show acl <acl-id> rule <rule-id> match ip udp dest-port <ip-port-id>`<br>`nv show acl <acl-id> rule <rule-id> match ip tcp dest-port <ip-port-id>` |
| `nv show vrf <vrf-id> router pim address-family ipv4-unicast` | `nv show vrf <vrf-id> router pim address-family ipv4`|
| `nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover` | `nv show vrf <vrf-id> router pim address-family ipv4 spt-switchover`|
| `nv show vrf <vrf-id> router pim address-family ipv4-unicast rp` | `nv show vrf <vrf-id> router pim address-family ipv4 rp` |
| `nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>` | `nv show vrf <vrf-id> router pim address-family ipv4 rp <rp-id>` |
| `nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range` | `nv show vrf <vrf-id> router pim address-family ipv4 rp <rp-id> group-range` |
| `nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>` | `nv show vrf <vrf-id> router pim address-family ipv4 rp <rp-id> group-range <group-range-id>` |
| `nv action clear interface <interface> synce counters` | `nv action clear interface <interface> counters synce`|

{{< /expand >}}

{{< expand "New NVUE Commands" >}}

For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

{{< tabs "TabID40 ">}}
{{< tab "nv show ">}}

```
nv show platform pulse-per-second
nv show platform pulse-per-second in
nv show platform pulse-per-second out
nv show router bgp queue-limit
nv show bridge vlan-vni-map
nv show bridge domain <domain-id> vlan-vni-map
nv show interface <interface-id> link flap-protection
nv show interface <interface-id> link protodown
nv show interface <interface-id> port-security
nv show interface <interface-id> port-security static-mac
nv show interface <interface-id> port-security mac-addresses
nv show interface <interface-id> neighbor
nv show interface <interface-id> neighbor ipv6
nv show interface <interface-id> neighbor ipv6 <neighbor-id>
nv show interface <interface-id> neighbor ipv6 <neighbor-id> lladdr
nv show interface <interface-id> neighbor ipv6 <neighbor-id> lladdr <lladdr-id>
nv show interface <interface-id> neighbor ipv6 <neighbor-id> lladdr <lladdr-id> state
nv show interface <interface-id> neighbor ipv6 <neighbor-id> lladdr <lladdr-id> flag
nv show interface <interface-id> neighbor ipv4
nv show interface <interface-id> neighbor ipv4 <neighbor-id>
nv show interface <interface-id> neighbor ipv4 <neighbor-id> lladdr
nv show interface <interface-id> neighbor ipv4 <neighbor-id> lladdr <lladdr-id>
nv show interface <interface-id> neighbor ipv4 <neighbor-id> lladdr <lladdr-id> state
nv show interface <interface-id> neighbor ipv4 <neighbor-id> lladdr <lladdr-id> flag
nv show interface <interface-id> telemetry
nv show interface <interface-id> telemetry histogram
nv show interface <interface-id> telemetry histogram ingress-buffer
nv show interface <interface-id> telemetry histogram ingress-buffer priority-group
nv show interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id>
nv show interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold
nv show interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> snapshot
nv show interface <interface-id> telemetry histogram egress-buffer
nv show interface <interface-id> telemetry histogram egress-buffer traffic-class
nv show interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id>
nv show interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold
nv show interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> snapshot
nv show interface <interface-id> telemetry histogram counter
nv show interface <interface-id> telemetry histogram counter counter-type
nv show interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id>
nv show interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold
nv show interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> snapshot
nv show interface <interface-id> telemetry bw-gauge
nv show interface <interface-id> dot1x
nv show interface <interface-id> dot1x authenticated-sessions
nv show interface <interface-id> dot1x authenticated-sessions <mac-address-id>
nv show interface <interface-id> dot1x authenticated-sessions <mac-address-id> counters
nv show service dhcp-relay <vrf-id> agent
nv show service dhcp-relay <vrf-id> agent remote-id
nv show service dhcp-relay <vrf-id> agent remote-id <remote-id>
nv show service dhcp-relay <vrf-id> agent use-pif-circuit-id
nv show service ptp <instance-id> servo
nv show service telemetry
nv show service telemetry histogram
nv show service telemetry histogram ingress-buffer
nv show service telemetry histogram egress-buffer
nv show service telemetry histogram counter
nv show service telemetry histogram interface
nv show service telemetry bw-gauge
nv show service telemetry bw-gauge interface
nv show service telemetry snapshot-file
nv show system link
nv show system link flap-protection
nv show system config files
nv show system config files <config-file-id>
nv show system security certificate
nv show system security certificate <cert-id>
nv show system security certificate <cert-id> installed
nv show system security certificate <cert-id> dump
nv show system security ca-certificate
nv show system security ca-certificate <cert-id>
nv show system security ca-certificate <cert-id> dump
nv show system maintenance
nv show system date-time
nv show system forwarding ecmp-weight-normalisation
nv show system dot1x
nv show system dot1x radius
nv show system dot1x radius server
nv show system dot1x radius server <server-id>
nv show system aaa radius
nv show system aaa radius server
nv show system aaa radius server <hostname-id>
nv show system aaa role <role-id> class
nv show system aaa role <role-id> class <class-id>
nv show system aaa class
nv show system aaa class <class-id>
nv show system aaa class <class-id> command-path
nv show system aaa class <class-id> command-path <command-path-id>
nv show system nat
nv show acl <acl-id> rule <rule-id> action source-nat
nv show acl <acl-id> rule <rule-id> action source-nat translate-ip
nv show acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv show acl <acl-id> rule <rule-id> action source-nat translate-port
nv show acl <acl-id> rule <rule-id> action source-nat translate-port <translate-port-id>
nv show acl <acl-id> rule <rule-id> action dest-nat
nv show acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv show acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv show acl <acl-id> rule <rule-id> action dest-nat translate-port
nv show acl <acl-id> rule <rule-id> action dest-nat translate-port <translate-port-id>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set router bgp queue-limit input 1-4294967295
nv set router bgp queue-limit output 1-4294967295
nv set bridge domain <domain-id> stp force-protocol-version (stp|rstp)
nv set evpn mac-vrf-soo <route-distinguisher>
nv set interface <interface-id> link flap-protection enable (on|off)
nv set interface <interface-id> link protodown
nv set interface <interface-id> neighbor ipv4
nv set interface <interface-id> neighbor ipv4 <address> lladdr
nv set interface <interface-id> neighbor ipv4 <address> lladdr <address> flag
nv set interface <interface-id> neighbor ipv4 <address> lladdr <address> state
nv set interface <interface-id> neighbor ipv6
nv set interface <interface-id> neighbor ipv6 <address> lladdr
nv set interface <interface-id> neighbor ipv6 <address> lladdr <address> flag
nv set interface <interface-id> neighbor ipv6 <address> lladdr <address> state
nv set interface <interface-id> port-security static-mac
nv set interface <interface-id> port-security enable (on|off)
nv set interface <interface-id> port-security mac-limit 1-512
nv set interface <interface-id> port-security sticky-mac (enabled|disabled)
nv set interface <interface-id> port-security sticky-timeout 0-3600
nv set interface <interface-id> port-security sticky-ageing (enabled|disabled)
nv set interface <interface-id> port-security violation-mode (protodown|restrict)
nv set interface <interface-id> port-security violation-timeout 1-60
nv set interface <interface-id> synce bundle-id 0-256
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id>
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold action log
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold value 96-4294967295
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> bin-min-boundary 96-4294967295
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> histogram-size 96-4294967295
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> sample-interval 128-1000000000
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id>
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold action log
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold value 96-4294967295
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> bin-min-boundary 96-4294967295
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> histogram-size 96-4294967295
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> sample-interval 128-1000000000
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id>
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold action log
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold value 1-4294967295
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> bin-min-boundary 1-4294967295
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> histogram-size 1-4294967295
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> sample-interval 128-1000000000
nv set interface <interface-id> dot1x auth-fail-vlan (enabled|disabled)
nv set service dhcp-server <vrf-id> static <static-id> ifname <interface-name>
nv set service dhcp-relay <vrf-id> agent remote-id <remote-id>
nv set service dhcp-relay <vrf-id> agent use-pif-circuit-id enable (on|off)
nv set service dhcp-relay <vrf-id> agent enable (on|off)
nv set service telemetry histogram ingress-buffer bin-min-boundary 96-4294967295
nv set service telemetry histogram ingress-buffer histogram-size 96-4294967295
nv set service telemetry histogram ingress-buffer sample-interval 128-1000000000
nv set service telemetry histogram egress-buffer bin-min-boundary 96-4294967295
nv set service telemetry histogram egress-buffer histogram-size 96-4294967295
nv set service telemetry histogram egress-buffer sample-interval 128-1000000000
nv set service telemetry histogram counter bin-min-boundary 1-4294967295
nv set service telemetry histogram counter histogram-size 1-4294967295
nv set service telemetry histogram counter sample-interval 128-1000000000
nv set service telemetry snapshot-file name <value>
nv set service telemetry snapshot-file count 3-100
nv set service telemetry enable (on|off)
nv set service telemetry snapshot-interval 1-604800
nv set system api certificate self-signed
nv set system link flap-protection threshold 0-30
nv set system link flap-protection interval 0-60
nv set system forwarding ecmp-weight-normalisation mode (enabled|disabled)
nv set system forwarding ecmp-weight-normalisation max-hw-weight 10-255
nv set system dot1x radius server <server-id>
nv set system dot1x radius server <server-id> priority 1-3
nv set system dot1x radius server <server-id> vrf <value>
nv set system dot1x radius server <server-id> accounting-port 1-65535
nv set system dot1x radius server <server-id> authentication-port 1-65535
nv set system dot1x radius server <server-id> shared-secret <value>
nv set system dot1x radius client-src-ip <ipv4>
nv set system dot1x reauthentication-interval 0-86640
nv set system dot1x dynamic-vlan (required|disabled|optional)
nv set system dot1x auth-fail-vlan 1-4094
nv set system dot1x max-stations 1-255
nv set system aaa radius server <hostname-id>
nv set system aaa radius server <hostname-id> port 0-65535
nv set system aaa radius server <hostname-id> timeout 1-60
nv set system aaa radius server <hostname-id> secret <value>
nv set system aaa radius server <hostname-id> priority 1-100
nv set system aaa radius server <hostname-id> source-ip (<ipv4>|<ipv6>)
nv set system aaa radius enable (on|off)
nv set system aaa radius vrf <vrf-name>
nv set system aaa radius debug (enabled|disabled)
nv set system aaa radius privilege-level 0-15
nv set system aaa radius retransmit 0-10
nv set system aaa radius port 0-65535
nv set system aaa radius timeout 1-60
nv set system aaa radius source-ipv4 <ipv4>
nv set system aaa radius source-ipv6 <ipv6>
nv set system aaa role <role-id>
nv set system aaa role <role-id> class <class-id>
nv set system aaa class <class-id>
nv set system aaa class <class-id> command-path <command-path-id>
nv set system aaa class <class-id> command-path <command-path-id> permission (ro|rw|act|all)
nv set system aaa class <class-id> action (allow|deny)
nv set system nat age-poll-interval 1-1440
nv set system nat translate-table-size 1024-8192
nv set system nat rule-table-size 64-1024
nv set system nat mode dynamic
nv set nve vxlan ageing 0-4096
nv set acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv set acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id> to <ipv4>
nv set acl <acl-id> rule <rule-id> action source-nat translate-port <translate-port-id>
nv set acl <acl-id> rule <rule-id> action source-nat translate-mac <mac>
nv set acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv set acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id> to <ipv4>
nv set acl <acl-id> rule <rule-id> action dest-nat translate-port <translate-port-id>
nv set acl <acl-id> rule <rule-id> action dest-nat translate-mac <mac>
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset router policy route-map <route-map-id> rule <rule-id> action permit exit-policy exit
nv unset router bgp queue-limit
nv unset router bgp queue-limit input
nv unset router bgp queue-limit output
nv unset bridge domain <domain-id> stp force-protocol-version
nv unset evpn mac-vrf-soo
nv unset interface <interface-id> link flap-protection
nv unset interface <interface-id> link flap-protection enable
nv unset interface <interface-id> link protodown
nv unset interface <interface-id> neighbor ipv4
nv unset interface <interface-id> neighbor ipv4 <address> lladdr
nv unset interface <interface-id> neighbor ipv4 <address> lladdr <address> flag
nv unset interface <interface-id> neighbor ipv4 <address> lladdr <address> state
nv unset interface <interface-id> neighbor ipv6
nv unset interface <interface-id> neighbor ipv6 <address> lladdr
nv unset interface <interface-id> neighbor ipv6 <address> lladdr <address> flag
nv unset interface <interface-id> neighbor ipv6 <address> lladdr <address> state
nv unset interface <interface-id> port-security
nv unset interface <interface-id> port-security static-mac
nv unset interface <interface-id> port-security enable
nv unset interface <interface-id> port-security mac-limit
nv unset interface <interface-id> port-security sticky-mac
nv unset interface <interface-id> port-security sticky-timeout
nv unset interface <interface-id> port-security sticky-ageing
nv unset interface <interface-id> port-security violation-mode
nv unset interface <interface-id> port-security violation-timeout
nv unset interface <interface-id> synce bundle-id
nv unset interface <interface-id> telemetry
nv unset interface <interface-id> telemetry histogram
nv unset interface <interface-id> telemetry histogram ingress-buffer
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id>
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold action
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold value
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> bin-min-boundary
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> histogram-size
nv unset interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> sample-interval
nv unset interface <interface-id> telemetry histogram egress-buffer
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id>
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold action
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold value
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> bin-min-boundary
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> histogram-size
nv unset interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> sample-interval
nv unset interface <interface-id> telemetry histogram counter
nv unset interface <interface-id> telemetry histogram counter counter-type
nv unset interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id>
nv unset interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold
nv unset interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold action
nv unset interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold value
nv unset interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> bin-min-boundary
nv unset interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> histogram-size
nv unset interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> sample-interval
nv unset interface <interface-id> telemetry bw-gauge
nv unset interface <interface-id> telemetry bw-gauge enable
nv unset interface <interface-id> dot1x
nv unset interface <interface-id> dot1x eap
nv unset interface <interface-id> dot1x mba
nv unset interface <interface-id> dot1x auth-fail-vlan
nv unset service dhcp-server <vrf-id> static <static-id> ifname
nv unset service dhcp-relay <vrf-id> agent
nv unset service dhcp-relay <vrf-id> agent remote-id <remote-id>
nv unset service dhcp-relay <vrf-id> agent use-pif-circuit-id
nv unset service dhcp-relay <vrf-id> agent use-pif-circuit-id enable
nv unset service dhcp-relay <vrf-id> agent enable
nv unset service ptp <instance-id> servo
nv unset service telemetry
nv unset service telemetry histogram
nv unset service telemetry histogram ingress-buffer
nv unset service telemetry histogram ingress-buffer bin-min-boundary
nv unset service telemetry histogram ingress-buffer histogram-size
nv unset service telemetry histogram ingress-buffer sample-interval
nv unset service telemetry histogram egress-buffer
nv unset service telemetry histogram egress-buffer bin-min-boundary
nv unset service telemetry histogram egress-buffer histogram-size
nv unset service telemetry histogram egress-buffer sample-interval
nv unset service telemetry histogram counter
nv unset service telemetry histogram counter bin-min-boundary
nv unset service telemetry histogram counter histogram-size
nv unset service telemetry histogram counter sample-interval
nv unset service telemetry snapshot-file
nv unset service telemetry snapshot-file name
nv unset service telemetry snapshot-file count
nv unset service telemetry enable
nv unset service telemetry snapshot-interval
nv unset system api certificate
nv unset system link
nv unset system link flap-protection
nv unset system link flap-protection threshold
nv unset system link flap-protection interval
nv unset system forwarding ecmp-weight-normalisation
nv unset system forwarding ecmp-weight-normalisation mode
nv unset system forwarding ecmp-weight-normalisation max-hw-weight
nv unset system dot1x
nv unset system dot1x radius
nv unset system dot1x radius server
nv unset system dot1x radius server <server-id>
nv unset system dot1x radius server <server-id> priority
nv unset system dot1x radius server <server-id> vrf
nv unset system dot1x radius server <server-id> accounting-port
nv unset system dot1x radius server <server-id> authentication-port
nv unset system dot1x radius server <server-id> shared-secret
nv unset system dot1x radius client-src-ip
nv unset system dot1x reauthentication-interval
nv unset system dot1x dynamic-vlan
nv unset system dot1x auth-fail-vlan
nv unset system dot1x max-stations
nv unset system aaa radius
nv unset system aaa radius server
nv unset system aaa radius server <hostname-id>
nv unset system aaa radius server <hostname-id> port
nv unset system aaa radius server <hostname-id> timeout
nv unset system aaa radius server <hostname-id> secret
nv unset system aaa radius server <hostname-id> priority
nv unset system aaa radius server <hostname-id> source-ip
nv unset system aaa radius enable
nv unset system aaa radius vrf
nv unset system aaa radius debug
nv unset system aaa radius privilege-level
nv unset system aaa radius retransmit
nv unset system aaa radius port
nv unset system aaa radius timeout
nv unset system aaa radius source-ipv4
nv unset system aaa radius source-ipv6
nv unset system aaa role
nv unset system aaa role <role-id>
nv unset system aaa role <role-id> class
nv unset system aaa role <role-id> class <class-id>
nv unset system aaa class
nv unset system aaa class <class-id>
nv unset system aaa class <class-id> command-path
nv unset system aaa class <class-id> command-path <command-path-id>
nv unset system aaa class <class-id> command-path <command-path-id> permission
nv unset system aaa class <class-id> action
nv unset system nat
nv unset system nat age-poll-interval
nv unset system nat translate-table-size
nv unset system nat rule-table-size
nv unset system nat mode
nv unset acl <acl-id> rule <rule-id> action source-nat
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id> to
nv unset acl <acl-id> rule <rule-id> action source-nat translate-port
nv unset acl <acl-id> rule <rule-id> action source-nat translate-port <translate-port-id>
nv unset acl <acl-id> rule <rule-id> action source-nat translate-mac
nv unset acl <acl-id> rule <rule-id> action dest-nat
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id> to
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-port
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-port <translate-port-id>
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-mac
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action change system date-time
nv action clear interface <interface-id> bridge domain <domain-id> stp bpduguardviolation
nv action clear interface <interface-id> link protodown
nv action clear system link protodown
nv action delete system config files
nv action delete system security ca-certificate
nv action delete system security certificate
nv action disable system maintenance
nv action enable system maintenance
nv action export system config
nv action import system security ca-certificate
nv action import system security certificate
nv action rename system config files
nv action upload system config files
```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.7 includes the NVUE object model. After you upgrade to Cumulus Linux 5.7, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
