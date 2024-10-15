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

### New Features and Enhancements

- The NVIDIA SN5400 switch supports {{<link url="Synchronous-Ethernet-SyncE" text="syncE">}} and {{<link url="Precision-Time-Protocol-PTP/#noise-transfer-servo" text="ITU-T">}}
- {{<link url="Pulse-Per-Second-PPS" text="PPS on the NVIDIA SN5400 switch">}} is now generally available.
- {{<link url="Factory-Reset" text="Factory Reset">}}
- {{<link url="Forwarding-Table-Size-and-Profiles/#spectrum-1" text="ecmp-nh-heavy forwarding profile">}} for Spectrum 1 switches
- {{<link url="Optional-BGP-Configuration/#bgp-prefix-independent-convergence" text="BGP Prefix Independent Convergence">}}
- {{<link url="RADIUS-AAA/#radius-user-command-accounting" text="RADIUS user command accounting">}}
- {{<link url="Upgrading-Cumulus-Linux/#upgrade-cumulus-linux" text="Optimized image upgrade commands">}} (available for future upgrades)
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#adaptive-routing" text="Additional adaptive routing ECMP resource optimization for next hop groups">}} (Beta)
- OTLP
- {{<link url="ASIC-Monitoring/#histogram-collection" text="Packet and buffer histogram commands">}}
- NVUE
  - {{<link url="DHCP-Snooping" text="DHCP snooping commands">}}
  - {{<link url="Link-Layer-Discovery-Protocol/#disable-lldp" text="Disable LLDP commands">}}
  - {{<link url="Resource-Diagnostics/#disable-lldp" text="Show ASIC resources commands">}} (`cl-resource-query` equivalent)
  - {{<link url="Monitoring-System-Statistics-and-Network-Traffic-with-sFlow" text="sFlow commands">}}
  - {{<link url="DHCP-Servers/#assign-a-port-based-ip-address" text="IPv6 command to assign a port-based DHCP server address">}}
  - {{<link url="Zero-Touch-Provisioning-ZTP/#manually-run-ztp" text="Enable ZTP and run ZTP script commands">}}
  - {{<link url="Interface-Configuration-and-Management/#port-ranges" text="Additional port range support for breakout ports and subinterfaces">}}
  - {{<link url="Interface-Configuration-and-Management/#troubleshooting" text="nv show interface <interface>">}} commands now show the date and time the operational state of an interface changes and number of carrier transitions
  - {{<link url="NVUE-CLI/#show-switch-configuration" text="nv config show --all command">}} to show applied configuration on the switch and include all default options
  - {{<link url="Services-and-Daemons-in-Cumulus-Linux/#limit-resources-for-services" text="Commands to limit resources (memory and CPU usage) for Cumulus Linux services">}}.
  - {{<link url="Optional-BGP-Configuration/#bgp-community-lists" text="Commands to configure BGP large community lists">}}
  - {{<link url="Route-Filtering-and-Redistribution/#match-source-protocol" text="Command to match BGP as the source protocol in a route map">}}
  - {{<link url="Switch-Port-Attributes/#interface-settings" text="nv show interface --view command includes additional filtering options">}}: `svi`, `vrf`, `bonds`, `bond-members`, `up`, and `down`
  - {{<link url="FRRouting/#show-routes-in-the-routing-table" text="Commands to show the number of routes in the routing table">}}
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#show-transceiver-information" text="Commands to show optical information for transceivers">}}
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#show-transceiver-information" text="l1-show command equivalent">}}
  - BGP command output updates
  - EVPN command output updates
  - {{< expand "Changed NVUE Commands" >}}
| New Command | Previous Command |
| ----------- | ----------------|
| nv set system snmp-server<br>nv unset system snmp-server | nv set service snmp-server<br>nv unset service snmp-server |
| nv set system snmp-server state enable<br>nv set system snmp-server state disable| nv set service snmp-server enable on<br>nv set service snmp-server enable off|
| nv show system snmp-server | nv show service snmp-server|
| nv set qos advance-buffer-config default-global ingress-service-pool <pool-id> <property> <value> | nv set qos advance-buffer-config default-global ingress-pool <pool-id> <property> <value>|
| nv set qos advance-buffer-config default-global egress-service-pool <pool-id> <property> <value> | nv set qos advance-buffer-config default-global egress-pool <pool-id> <property> <value>  |
| nv show qos advance-buffer-config default-global ingress-service-pool | nv show qos advance-buffer-config default-global ingress-pool |
| nv show qos advance-buffer-config default-global egress-service-pool | nv show qos advance-buffer-config default-global egress-pool |
{{< /expand >}}
  - {{< expand "Deprecated NVUE Commands" >}}
| Deprecated Command | Replace with |
| ----------- | ----------------|
| nv show interface pluggables  | nv show platform transceiver|
| nv show interface <interface> pluggable | nv show platform transceiver <interface>|

{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show bridge domain <bridge-id> dhcp-snoop
nv show bridge domain <bridge-id> dhcp-snoop6
nv show bridge domain <bridge-id> dhcp-snoop vlan <vlan-id>
nv show bridge domain <bridge-id> dhcp-snoop6 vlan <vlan-id>
nv show bridge domain <bridge-id> dhcp-snoop vlan <vlan-id> trust <interface>
nv show bridge domain <bridge-id> dhcp-snoop6 vlan <vlan-id> trust <interface>
nv show platform asic resource
nv show platform asic resource acl
nv show platform asic resource global
nv show platform transceiver
nv show platform transceiver <interface-id> 
nv show platform transceiver <interface-id> channel 
nv show platform transceiver <interface-id> channel <channel-id> 
nv show platform transceiver <detail> 
nv show interface <interface-id> transceiver 
nv show interface <interface-id> transceiver thresholds
nv show platform transceiver
nv show platform transceiver <interface-id>
nv show platform transceiver <interface-id> channel
nv show platform transceiver <interface-id> channel <channel-id>
nv show platform transceiver <interface-id> thresholds
nv show system sflow
nv show system sflow agent
nv show system sflow collector
nv show system sflow policer
nv show system sflow sampling-rate
nv show interface <interface-id> sflow
nv show system telemetry interface-stats
nv show system telemetry interface-stats port-group
nv show system telemetry interface-stats port-group <port-group-id>
nv show system telemetry interface-stats port-group <port-group-id> snapshot-file
nv show system telemetry interface-stats port-group <port-group-id> threshold
nv show system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id>
nv show system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action
nv show system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action log
nv show system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action collect
nv show system telemetry interface-stats port-group <port-group-id> stats-type
nv show system telemetry interface-stats port-group <port-group-id> snapshot
nv show system telemetry interface-stats port-group <port-group-id> snapshot buffer
nv show system telemetry interface-stats port-group <port-group-id> snapshot buffer pool
nv show system telemetry interface-stats port-group <port-group-id> snapshot buffer pool <buffer-pool-id>
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id>
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet good
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet good tx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet good rx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet discard
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet discard tx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet discard rx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet discard general
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet all
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet all tx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet all rx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet tc
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet tc <tc-id>
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet tc <tc-id> tx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet pg
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet pg <pg-id>
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet pg <pg-id> tx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> packet pg <pg-id> rx
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> buffer
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> buffer tc
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> buffer tc <tc-id>
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> buffer pg
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> buffer pg <pg-id>
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> buffer ingress-port
nv show system telemetry interface-stats port-group <port-group-id> snapshot interface <intf-id> buffer ingress-port <buffer-pool-id>
nv show system telemetry interface-stats export
nv show system telemetry interface-stats switch-priority
nv show system telemetry interface-stats switch-priority <pg-id>
nv show system telemetry interface-stats ingress-buffer
nv show system telemetry interface-stats ingress-buffer priority-group
nv show system telemetry interface-stats ingress-buffer priority-group <pg-id>
nv show system telemetry interface-stats egress-buffer
nv show system telemetry interface-stats egress-buffer traffic-class
nv show system telemetry interface-stats egress-buffer traffic-class <tc-id>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set bridge domain <bridge-id> dhcp-snoop vlan <vlan-id>
nv set bridge domain <bridge-id> dhcp-snoop6 vlan <vlan-id>
nv set bridge domain <bridge-id> dhcp-snoop vlan <vlan-id> trust <interface-id>
nv set bridge domain <bridge-id> dhcp-snoop6 vlan <vlan-id> trust <interface-id>
nv set interface <interface-id> lldp state
nv set interface <interface-id> sflow state
nv set interface <interface-id> sflow sample-rate <rate>
nv set router policy large-community-list
nv set router policy route-map <map-id> rule <rule-id> match large-community-list
nv set service dhcp-server6 default static <server-id>
nv set service dhcp-server6 default static <server-id> ip-address <ip-address>
nv set service dhcp-server6 default static <server-id> ifname <interface-id>
nv set system sflow state
nv set system sflow collector <colector-id> port <port-id>
nv set system sflow collector <colector-id> interface <interface-id>
nv set system sflow sampling-rate <speed> <packets>
nv set system sflow poll-interval <interval>
nv set system sflow agent ip <ip-address>
nv set system sflow agent interface <interface-id>
nv set system sflow dropmon
nv set system sflow policer rate <samples>
nv set system sflow policer burst <sample-size>
nv set system telemetry interface-stats port-group <port-group-id>
nv set system telemetry interface-stats port-group <port-group-id> snapshot-file name <value>
nv set system telemetry interface-stats port-group <port-group-id> snapshot-file count
nv set system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id>
nv set system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action log
nv set system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action collect port-group <value>
nv set system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> value
nv set system telemetry interface-stats port-group <port-group-id> stats-type
nv set system telemetry interface-stats port-group <port-group-id> interface <value>
nv set system telemetry interface-stats port-group <port-group-id> timer-interval
nv set system telemetry interface-stats export state (enabled|disabled)
nv set system telemetry interface-stats switch-priority <pg-id>
nv set system telemetry interface-stats ingress-buffer priority-group <pg-id>
nv set system telemetry interface-stats egress-buffer traffic-class <tc-id>
nv set system telemetry interface-stats sample-interval
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset bridge domain <bridge-id> dhcp-snoop vlan <vlan-id>
nv unset bridge domain <bridge-id> dhcp-snoop6 vlan <vlan-id>
nv unset bridge domain <bridge-id> dhcp-snoop vlan <vlan-id> trust <interface-id>
nv unset bridge domain <bridge-id> dhcp-snoop6 vlan <vlan-id> trust <interface-id>
nv unset interface <interface-id> sflow sample-rate
nv unset router policy large-community-list
nv unset router policy route-map <map-id> rule <rule-id> match large-community-list
nv unset service dhcp-server6 default static <server-id>
nv unset service dhcp-server6 default static <server-id> ip-address <ip-address>
nv unset service dhcp-server6 default static <server-id> ifname <interface-id>
nv unset system sflow collector <colector-id> port <port-id>
nv unset system sflow collector <colector-id> interface <interface-id>
nv unset system sflow sampling-rate <speed> <packets>
nv unset system sflow poll-interval
nv unset system sflow agent ip <ip-address>
nv unset system sflow agent interface <interface-id>
nv unset system sflow dropmon
nv unset system sflow policer rate
nv unset system sflow policer burst
nv unset system telemetry interface-stats
nv unset system telemetry interface-stats port-group
nv unset system telemetry interface-stats port-group <port-group-id>
nv unset system telemetry interface-stats port-group <port-group-id> snapshot-file
nv unset system telemetry interface-stats port-group <port-group-id> snapshot-file name
nv unset system telemetry interface-stats port-group <port-group-id> snapshot-file count
nv unset system telemetry interface-stats port-group <port-group-id> threshold
nv unset system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id>
nv unset system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action
nv unset system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action log
nv unset system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action collect
nv unset system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> action collect port-group
nv unset system telemetry interface-stats port-group <port-group-id> threshold <threshold-stats-id> value
nv unset system telemetry interface-stats port-group <port-group-id> stats-type
nv unset system telemetry interface-stats port-group <port-group-id> interface
nv unset system telemetry interface-stats port-group <port-group-id> timer-interval
nv unset system telemetry interface-stats export
nv unset system telemetry interface-stats export state
nv unset system telemetry interface-stats switch-priority
nv unset system telemetry interface-stats switch-priority <if-pg-id>
nv unset system telemetry interface-stats ingress-buffer
nv unset system telemetry interface-stats ingress-buffer priority-group
nv unset system telemetry interface-stats ingress-buffer priority-group <if-pg-id>
nv unset system telemetry interface-stats egress-buffer
nv unset system telemetry interface-stats egress-buffer traffic-class
nv unset system telemetry interface-stats egress-buffer traffic-class <if-tc-id>
nv unset system telemetry interface-stats sample-interval
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action reset system factory-reset
nv action reset system factory-reset keep basic
nv action reset system factory-reset keep all-config
nv action reset system factory-reset keep all-files
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

{{%notice warning%}}
To align with a long-term vision of a common interface between Cumulus Linux, Nvidia OS (NVOS), and Host-Based Networking, certain NVUE commands in Cumulus Linux 5.11 have changed. Before you upgrade to 5.11, review the list of changed commands in Changed NVUE Commands above and be sure to make any necessary changes to your automation.
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
