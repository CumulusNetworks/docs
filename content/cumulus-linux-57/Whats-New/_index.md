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
- {{<link url="Pulse-Per-Second-PPS" text=" Pulse Per Second (PPS) synchronization">}}
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

{{< /expand >}}

{{< expand "New NVUE Commands" >}}

For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

{{< tabs "TabID40 ">}}
{{< tab "nv show ">}}

```
nv show acl <acl-id> rule <rule-id> action dest-nat
nv show acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv show acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv show acl <acl-id> rule <rule-id> action dest-nat translate-port
nv show acl <acl-id> rule <rule-id> action dest-nat translate-port <translate-port-id>
nv show acl <acl-id> rule <rule-id> action source-nat
nv show acl <acl-id> rule <rule-id> action source-nat translate-ip
nv show acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv show acl <acl-id> rule <rule-id> action source-nat translate-port
nv show acl <acl-id> rule <rule-id> action source-nat translate-port <translate-port-id>
nv show bridge vlan-vni-map
nv show bridge domain <domain-id> vlan-vni-map
nv show interface <interface-id> dot1x
nv show interface <interface-id> dot1x authenticated-sessions
nv show interface <interface-id> dot1x authenticated-sessions <mac-address-id>
nv show interface <interface-id> dot1x authenticated-sessions <mac-address-id> counters
nv show interface <interface-id> link flap-protection
nv show interface <interface-id> neighbor
nv show interface <interface-id> neighbor ipv4
nv show interface <interface-id> neighbor ipv4 <neighbor-id>
nv show interface <interface-id> neighbor ipv4 <neighbor-id> lladdr
nv show interface <interface-id> neighbor ipv4 <neighbor-id> lladdr <lladdr-id>
nv show interface <interface-id> neighbor ipv6
nv show interface <interface-id> neighbor ipv6 <neighbor-id>
nv show interface <interface-id> neighbor ipv6 <neighbor-id> lladdr
nv show interface <interface-id> neighbor ipv6 <neighbor-id> lladdr <lladdr-id>
nv show interface <interface-id> port-security
nv show interface <interface-id> port-security static-mac
nv show interface <interface-id> port-security mac-addresses
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
nv show interface neighbor
nv show platform pulse-per-second
nv show platform pulse-per-second in
nv show platform pulse-per-second out
nv show service telemetry
nv show service telemetry histogram
nv show service telemetry histogram ingress-buffer
nv show service telemetry histogram egress-buffer
nv show service telemetry histogram counter
nv show service telemetry histogram interface
nv show service telemetry bw-gauge
nv show service telemetry bw-gauge interface
nv show service telemetry snapshot-file
nv show system aaa class
nv show system aaa class <class-id>
nv show system aaa class <class-id> command-path
nv show system aaa class <class-id> command-path <command-path-id>
nv show system aaa radius
nv show system aaa radius server
nv show system aaa radius server <hostname-id>
nv show system aaa role
nv show system aaa role <role-id>
nv show system aaa role <role-id> class
nv show system aaa role <role-id> class <class-id>
nv show system dot1x
nv show system dot1x radius
nv show system dot1x radius server
nv show system dot1x radius server <server-id>
nv show system maintenance
nv show system link flap-protection
nv show system security ca-certificate
nv show system security ca-certificate <cert-id>
nv show system security ca-certificate <cert-id> dump
nv show system security certificate
nv show system security certificate <cert-id>
nv show system security certificate <cert-id> installed
nv show system security certificate <cert-id> dump
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv set acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv set acl <acl-id> rule <rule-id> action dest-nat translate-port
nv set acl <acl-id> rule <rule-id> action dest-nat translate-mac
nv set acl <acl-id> rule <rule-id> action source-nat translate-ip
nv set acl <acl-id> rule <rule-id> action source-nat translate-ip
nv set acl <acl-id> rule <rule-id> action source-nat translate-port
nv set acl <acl-id> rule <rule-id> action source-nat translate-mac
nv set interface <interface-id> dot1x eap
nv set interface <interface-id> dot1x mba
nv set interface <interface-id> dot1x auth-fail-vlan
nv set interface <interface-id> link flap-protection enable
nv set interface <interface-id> neighbor <address> lladdr
nv set interface <interface-id> neighbor <address> lladdr <address> state permanent
nv set interface <interface-id> neighbor <address> lladdr <address> flag is-router
nv set interface <interface-id> port-security static-mac
nv set interface <interface-id> port-security enable
nv set interface <interface-id> port-security mac-limit
nv set interface <interface-id> port-security sticky-mac
nv set interface <interface-id> port-security sticky-timeout
nv set interface <interface-id> port-security sticky-ageing
nv set interface <interface-id> port-security violation-mode
nv set interface <interface-id> port-security violation-timeout
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold action log
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> threshold value
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> bin-min-boundary
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> histogram-size
nv set interface <interface-id> telemetry histogram ingress-buffer priority-group <if-pg-id> sample-interval
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold action log
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> threshold value
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> bin-min-boundary
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> histogram-size
nv set interface <interface-id> telemetry histogram egress-buffer traffic-class <if-tc-id> sample-interval
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id>
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold action log
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> threshold value
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> bin-min-boundary
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> histogram-size
nv set interface <interface-id> telemetry histogram counter counter-type <if-counter-type-id> sample-interval
nv set interface <interface-id> telemetry bw-gauge enable
nv set platform pulse-per-second in state
nv set platform pulse-per-second in channel-index
nv set platform pulse-per-second in pin-index
nv set platform pulse-per-second in signal-width
nv set platform pulse-per-second in timestamp-correction
nv set platform pulse-per-second in logging-level 
nv set platform pulse-per-second in signal-polarity
nv set platform pulse-per-second out channel-index
nv set platform pulse-per-second out signal-width
nv set platform pulse-per-second out phase-adjustment
nv set platform pulse-per-second out frequency-adjustment
nv set platform pulse-per-second out state
nv set router bgp queue-limit input-queue
nv set router bgp queue-limit output-queue
nv set service telemetry histogram ingress-buffer bin-min-boundary
nv set service telemetry histogram ingress-buffer histogram-size
nv set service telemetry histogram ingress-buffer sample-interval
nv set service telemetry histogram egress-buffer bin-min-boundary
nv set service telemetry histogram egress-buffer histogram-size
nv set service telemetry histogram egress-buffer sample-interval
nv set service telemetry histogram counter bin-min-boundary
nv set service telemetry histogram counter histogram-size
nv set service telemetry histogram counter sample-interval
nv set service telemetry snapshot-file name <value>
nv set service telemetry snapshot-file count
nv set service telemetry enable (on|off)
nv set service telemetry snapshot-interval
nv set system aaa class <class-id>
nv set system aaa class <class-id> command-path
nv set system aaa class <class-id> command-path <command-path-id> permission
nv set system aaa class <class-id> action
nv set system aaa radius server <hostname-id>
nv set system aaa radius server <hostname-id> port
nv set system aaa radius server <hostname-id> timeout
nv set system aaa radius server <hostname-id> secret
nv set system aaa radius server <hostname-id> priority
nv set system aaa radius server <hostname-id> source-ip
nv set system aaa radius enable
nv set system aaa radius vrf <vrf-name>
nv set system aaa radius debug
nv set system aaa radius privilege-level
nv set system aaa radius retransmit
nv set system aaa radius port
nv set system aaa radius timeout 1-60
nv set system aaa radius source-ipv4
nv set system aaa radius source-ipv6
nv set system aaa authentication-order <priority-id>
nv set system aaa role <role-id>
nv set system aaa role <role-id> class <class-id>
nv set system api certificate
nv set system dot1x radius server <server-id>
nv set system dot1x radius server <server-id> priority
nv set system dot1x radius server <server-id> vrf
nv set system dot1x radius server <server-id> accounting-port
nv set system dot1x radius server <server-id> authentication-port
nv set system dot1x radius server <server-id> shared-secret
nv set system dot1x radius client-src-ip
nv set system dot1x reauthentication-interval
nv set system dot1x dynamic-vlan
nv set system dot1x auth-fail-vlan
nv set system dot1x max-stations
nv set system link flap-protection threshold
nv set system link flap-protection interval
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset acl <acl-id> rule <rule-id> action dest-nat
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id> to
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-port
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-port <translate-port-id>
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-mac
nv unset acl <acl-id> rule <rule-id> action source-nat
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id> to
nv unset acl <acl-id> rule <rule-id> action source-nat translate-port
nv unset acl <acl-id> rule <rule-id> action source-nat translate-port <translate-port-id>
nv unset acl <acl-id> rule <rule-id> action source-nat translate-mac
nv unset interface <interface-id> dot1x
nv unset interface <interface-id> dot1x eap
nv unset interface <interface-id> dot1x mba
nv unset interface <interface-id> dot1x auth-fail-vlan
nv unset interface <interface-id> link flap-protection
nv unset interface <interface-id> link flap-protection enable
nv unset interface <interface-id> neighbor <address> lladdr <address>
nv unset interface <interface-id> neighbor <address> lladdr <address> state permanent
nv unset interface <interface-id> neighbor <address> lladdr <address> flag is-router
nv unset interface <interface-id> port-security
nv unset interface <interface-id> port-security static-mac
nv unset interface <interface-id> port-security enable
nv unset interface <interface-id> port-security mac-limit
nv unset interface <interface-id> port-security sticky-mac
nv unset interface <interface-id> port-security sticky-timeout
nv unset interface <interface-id> port-security sticky-ageing
nv unset interface <interface-id> port-security violation-mode
nv unset interface <interface-id> port-security violation-timeout
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
nv unset router bgp queue-limit input-queue
nv unset router bgp queue-limit output-queue
nv unset platform pulse-per-second in state
nv unset platform pulse-per-second in channel-index
nv unset platform pulse-per-second in pin-index
nv unset platform pulse-per-second in signal-width
nv unset platform pulse-per-second in timestamp-correction
nv unset platform pulse-per-second in logging-level
nv unset platform pulse-per-second in signal-polarity
nv unset platform pulse-per-second out channel-index
nv unset platform pulse-per-second out signal-width
nv unset platform pulse-per-second out phase-adjustment
nv unset platform pulse-per-second out frequency-adjustment
nv unset platform pulse-per-second out state
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
nv unset system aaa class
nv unset system aaa class <class-id>
nv unset system aaa class <class-id> command-path
nv unset system aaa class <class-id> command-path <command-path-id>
nv unset system aaa class <class-id> command-path <command-path-id> permission
nv unset system aaa class <class-id> action
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
nv unset system api certificate
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
nv unset system link flap-protection
nv unset system link flap-protection threshold
nv unset system link flap-protection interval
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action change system date-time
nv action delete system security ca-certificate <cert-id>
nv action delete system security certificate <cert-id>
nv action disable system maintenance (mode|ports)
nv action enable system maintenance (mode|ports)
nv action import system security ca-certificate <cert-id>
nv action import system security certificate <cert-id>
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
