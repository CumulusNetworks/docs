---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.6 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.6, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.6, see the {{<link title="Cumulus Linux 5.6 Release Notes" text="Cumulus Linux 5.6 Release Notes">}}.
- To upgrade to Cumulus Linux 5.6, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.6.0
<!-- vale on -->
Cumulus Linux 5.6.0 supports new platforms, contains several new features and improvements, and provides bug fixes.

### Platforms

- NVIDIA SN5600 (800G Spectrum-4) - (supports 1G on the bonus port)
- NVIDIA SN3750-SX (200G Spectrum-2) is now generally available

### New Features and Enhancements

- FRR upgrade to version 8.4.3
- PTP stack upgrade to linuxptp 4.0
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#adaptive-routing" text="Adaptive routing">}} is generally available for a switch with the Spectrum-4 ASIC and provides enhancements that include support for {{<link url="Equal-Cost-Multipath-Load-Sharing/#adaptive-routing" text="VXLAN-encapsulated RoCE traffic">}} and {{<link url="BGP-Weighted-Equal-Cost-Multipath/#bgp-w-ecmp-with-adaptive-routing" text="BGP W-ECMP">}} (see the {{<link url="Equal-Cost-Multipath-Load-Sharing/#adaptive-routing" text="Adaptive Routing">}} section for important upgrade information)
- {{<link title="Spanning Tree and Rapid Spanning Tree - STP/#configure-the-mode-for-a-vlan-aware-bridge" text="PVRST with VLAN-aware bridges ">}}
- {{<link url="Quality-of-Service/#pfc-watchdog" text="QOS PFC watchdog">}} for lossless queues
- {{<link url="Precision-Time-Protocol-PTP/#clock-timestamp-mode" text="PTP one-step clock timestamp mode">}} for Spectrum-2 and Spectrum-3
- {{<link url="Switch-Port-Attributes/#breakout-ports" text="PAM4 encoding ">}} support for the NVIDIA SN4410 switch
- {{<link url="Monitoring-System-Hardware" text="Fan airflow direction">}} in NVUE `nv show platform environment fan` and Linux `smonctl -v` command output; a {{<link url="Monitoring-Best-Practices#hardware" text="fan direction mismatch">}} triggers a log message
- NVUE enhancements include:
  - {{<link url="SSH-for-Remote-Access" text="SSH commands">}}
  - {{<link url="NVUE-API/#use-the-api" text="Enable and disable external API access">}} commands (Cumulus Linux 5.6 and later enables the NVUE REST API by default; be sure to disable or secure the API if needed)
  - {{<link url="Address-Resolution-Protocol-ARP/#neighbor-base-reachable-timer" text="ARP Neighbor Base Reachable Timer">}} and {{<link url="Neighbor-Discovery-ND/#neighbor-base-reachable-timer" text="ND Neighbor Base Reachable Timer">}} commands
  - {{<link url="Protocol-Independent-Multicast-PIM/#igmp-settings" text="IGMP fast leave processing">}} and {{<link url="Protocol-Independent-Multicast-PIM/#igmp-settings" text="last member query count">}} commands
  - {{<link url="Troubleshooting-BGP/#clear-bgp-routes" text="Clear BGP route">}} commands to clear all BGP sessions and to refresh routes for all neighbors
  - {{<link url="Protocol-Independent-Multicast-PIM/#clear-pim-state-and-statistics" text="Clear PIM state and statistics">}} commands
  - {{<link url="EVPN-Enhancements/#clear-duplicate-addresses" text="Clear EVPN duplicate address">}} commands
  - {{<link url="Protocol-Independent-Multicast-PIM/#pim-show-commands" text="Show IGMP group commands ">}}
  - {{<link url="VLAN-aware-Bridge-Mode/#troubleshooting" text="Show commands">}} to see the ports mapped to a bridge and the VLANs mapped to bridge ports
  - {{<link url="Virtual-Router-Redundancy-Protocol-VRRP/#show-vrrp-configuration" text="VRRP show commands ">}} include operational data
  - Changes to the `nv show platform` command outputs to improve readability:
    - Shows a concise summary of all sensors
    - Improved memory format
    - Modified disk size output from KB to GB
    - Output fields display `n/a` for VX models where needed
    - Removed the `applied` column from the `nv show platform hardware component device` command
    - Removed the `applied` and `pending` columns from the `nv show platform software installed python3-nvue` command
  - The `nv show` commands provide a {{<link url="NVUE-CLI/#monitoring-commands" text="--filter option">}} to filter output data
  - EVPN multihoming configuration with NVUE no longer supports a 10-byte ESI value starting with a non 00 hex value

{{< expand "New Commands" >}}

{{< tabs "TabID40 ">}}
{{< tab "nv show commands ">}}

```
nv show router pbr nexthop-group
nv show router pbr nexthop-group <nexthop-group-id>
nv show bridge domain <domain-id> port
nv show bridge domain <domain-id> stp counters
nv show bridge domain <domain-id> stp port
nv show bridge domain <domain-id> stp port <interface-id>
nv show bridge domain <domain-id> stp vlan
nv show bridge domain <domain-id> stp vlan <vid>
nv show evpn vni <vni-id> remote-vtep
nv show qos pfc-watchdog
nv show interface <interface-id> ip igmp group
nv show interface <interface-id> ip igmp group <static-group-id>
nv show interface <interface-id> bridge domain <domain-id> stp vlan
nv show interface <interface-id> bridge domain <domain-id> stp vlan <vid>
nv show interface <interface-id> qos pfc-watchdog
nv show interface <interface-id> qos pfc-watchdog status
nv show interface <interface-id> qos pfc-watchdog status <qos-tc-id>
nv show service ptp <instance-id> counters
nv show system api
nv show system api listening-address
nv show system api listening-address <listening-address-id>
nv show system api connections
nv show system global arp
nv show system global arp garbage-collection-threshold
nv show system global nd
nv show system global nd garbage-collection-threshold
nv show system ssh-server
nv show system ssh-server max-unauthenticated
nv show system ssh-server vrf
nv show system ssh-server vrf <vrf-id>
nv show system ssh-server allow-users
nv show system ssh-server allow-users <user-id>
nv show system ssh-server deny-users
nv show system ssh-server deny-users <user-id>
nv show system ssh-server port
nv show system ssh-server port <port-id>
nv show system ssh-server active-sessions
```

{{< /tab >}}
{{< tab "nv set commands ">}}

```
nv set router adaptive-routing link-utilization-threshold (on|off)
nv set router password-obfuscation (enabled|disabled)
nv set bridge domain <domain-id> stp vlan <vid>
nv set bridge domain <domain-id> stp vlan <vid> bridge-priority 4096-61440
nv set bridge domain <domain-id> stp vlan <vid> hello-time 1-10
nv set bridge domain <domain-id> stp vlan <vid> forward-delay 4-30
nv set bridge domain <domain-id> stp vlan <vid> max-age 6-40
nv set bridge domain <domain-id> stp mode (rstp|pvrst)
nv set qos pfc-watchdog polling-interval 100-5000
nv set qos pfc-watchdog robustness 1-1000
nv set interface <interface-id> ip igmp fast-leave
nv set interface <interface-id> ip igmp last-member-query-count
nv set interface <interface-id> router adaptive-routing link-utilization-threshold 1-100
nv set interface <interface-id> bridge domain <domain-id> stp vlan <vid>
nv set interface <interface-id> bridge domain <domain-id> stp vlan <vid> priority 0-240
nv set interface <interface-id> bridge domain <domain-id> stp vlan <vid> path-cost
nv set interface <interface-id> bridge domain <domain-id> stp path-cost 1-200000000 
nv set interface <interface-id> qos pfc-watchdog state (enable|disable)
nv set service ptp <instance-id> profile <profile-id> two-step (on|off)
nv set service ptp <instance-id> two-step (on|off)
nv set system api listening-address <listening-address-id>
nv set system api state (enabled|disabled)
nv set system api port 1-65535
nv set system global arp base-reachable-time (30-2147483|auto)
nv set system global nd base-reachable-time (30-2147483|auto)
nv set system ssh-server max-unauthenticated session-count 1-10000
nv set system ssh-server max-unauthenticated throttle-percent 1-100
nv set system ssh-server max-unauthenticated throttle-start 1-10000
nv set system ssh-server vrf <vrf-id>
nv set system ssh-server allow-users <user-id>
nv set system ssh-server deny-users <user-id>
nv set system ssh-server port <port-id>
nv set system ssh-server authentication-retries 3-100
nv set system ssh-server login-timeout 1-600
nv set system ssh-server inactive-timeout <value>
nv set system ssh-server permit-root-login (disabled|prohibit-password|forced-commands-only|enabled)
nv set system ssh-server max-sessions-per-connection 1-100
nv set system ssh-server state (enabled|disabled)
```

{{< /tab >}}
{{< tab "nv unset commands ">}}

```
nv unset router adaptive-routing link-utilization-threshold
nv unset router password-obfuscation
nv unset bridge domain <domain-id> stp vlan
nv unset bridge domain <domain-id> stp vlan <vid>
nv unset bridge domain <domain-id> stp vlan <vid> bridge-priority
nv unset bridge domain <domain-id> stp vlan <vid> hello-time
nv unset bridge domain <domain-id> stp vlan <vid> forward-delay
nv unset bridge domain <domain-id> stp vlan <vid> max-age
nv unset bridge domain <domain-id> stp mode
nv unset qos pfc-watchdog
nv unset qos pfc-watchdog polling-interval
nv unset qos pfc-watchdog robustness
nv unset interface <interface-id> ip igmp fast-leave
nv unset interface <interface-id> ip igmp last-member-query-count
nv unset interface <interface-id> bridge domain <domain-id> stp vlan
nv unset interface <interface-id> bridge domain <domain-id> stp vlan <vid>
nv unset interface <interface-id> bridge domain <domain-id> stp vlan <vid> priority
nv unset interface <interface-id> bridge domain <domain-id> stp vlan <vid> path-cost
nv unset interface <interface-id> bridge domain <domain-id> stp path-cost
nv unset interface <interface-id> qos pfc-watchdog
nv unset interface <interface-id> qos pfc-watchdog state
nv unset service ptp <instance-id> profile <profile-id> two-step
nv unset service ptp <instance-id> two-step
nv unset system api
nv unset system api listening-address
nv unset system api listening-address <listening-address-id>
nv unset system api state
nv unset system api port
nv unset system api port 1-65535
nv unset system global arp base-reachable-time
nv unset system global nd base-reachable-time
nv unset system ssh-server
nv unset system ssh-server max-unauthenticated
nv unset system ssh-server max-unauthenticated session-count
nv unset system ssh-server max-unauthenticated throttle-percent
nv unset system ssh-server max-unauthenticated throttle-start
nv unset system ssh-server vrf
nv unset system ssh-server vrf <vrf-id>
nv unset system ssh-server allow-users
nv unset system ssh-server allow-users <user-id>
nv unset system ssh-server deny-users
nv unset system ssh-server deny-users <user-id>
nv unset system ssh-server port
nv unset system ssh-server port <port-id>
nv unset system ssh-server authentication-retries
nv unset system ssh-server login-timeout
nv unset system ssh-server inactive-timeout
nv unset system ssh-server permit-root-login
nv unset system ssh-server max-sessions-per-connection
nv unset system ssh-server state
```

{{< /tab >}}
{{< tab "nv action commands ">}}

```
nv action clear router policy prefix-list
nv action clear router policy prefix-list <prefix-list-id>
nv action clear router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>
nv action clear router bgp
nv action clear router bgp in prefix-filter
nv action clear router bgp out
nv action clear router bgp soft
nv action clear router bgp soft in
nv action clear router bgp soft out
nv action clear router igmp interfaces
nv action clear evpn vni
nv action clear evpn vni <vni-id>
nv action clear evpn vni <vni-id> mac <mac-address-id>
nv action clear evpn vni <vni-id> host <ip-address-id>
nv action clear interface <interface-id> qos pfc-watchdog deadlock-count
nv action clear vrf <vrf-id> router bgp in prefix-filter
nv action clear vrf <vrf-id> router bgp out
nv action clear vrf <vrf-id> router bgp soft
nv action clear vrf <vrf-id> router bgp soft in
nv action clear vrf <vrf-id> router bgp soft out
nv action clear vrf <vrf-id> router pim interfaces
nv action clear vrf <vrf-id> router pim interface-traffic
```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.6 includes the NVUE object model. After you upgrade to Cumulus Linux 5.6, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
