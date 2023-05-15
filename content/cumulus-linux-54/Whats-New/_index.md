---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.4 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.4, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.4, see the {{<link title="Cumulus Linux 5.4 Release Notes" text="Cumulus Linux 5.4 Release Notes">}}.
- To upgrade to Cumulus Linux 5.4, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.4.0c
<!-- vale on -->
Cumulus Linux 5.4.0c replaces Cumulus Linux 5.4.0b and includes new firmware (version 34.2012.0302) that provides improved thermal sensor data accuracy. Cumulus Linux 5.4.0b is no longer available.

Cumulus Linux 5.4.0c only supports the following platform, which is available as a proof of concept (POC):

- NVIDIA SN5600 (800G Spectrum-4)

{{%notice note%}}
- Cumulus Linux 5.4.0c does not support package upgrade; you must install the Cumulus Linux 5.4.0c image.
- If you install a new Cumulus Linux 5.4.0c image, you must power cycle the switch after installation.
- Cumulus Linux 5.4.0c does not support forced link speed; the switch uses auto-negotiation only.
- For information about NetQ features supported for Spectrum-4, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-45/More-Documents/Spectrum-Support/" text="NetQ Spectrum-4 Support">}}.
{{%/notice%}}

The following list describes open issues specific to the NVIDIA SN5600 (Spectrum-4) switch. See {{<link title="Cumulus Linux 5.4 Release Notes" text="Cumulus Linux 5.4.0 Release Notes">}} for additional open issues that are not fixed in this release.

{{< expand "Open Issues" >}}
| Issue ID | Description |
| -------  | ---------- |
| 3436305  | Auto-negotiation and link-training is not supported at 25G between the NVIDIA SN5600 switch and non-NVIDIA devices.|
| 3436298  | On rare occasions, when you use the MMS4X00-NS transceiver with the NVIDIA SN5600 switch, the port might not come up.|
| 3436296  | On the NVIDIA SN5600 switch, the 8x port breakout is not supported with the MCP4Y10-N00A cable.|
| 3436291  | The NVIDIA SN5600 switch does not support connecting to a Spectrum-2 or Spectrum-3 switch with an MCP7Y70-H001 4X  breakout cable.|
| 3436288  | When you connect two ports together on the same NVIDIA SN5600 switch with an MCP4Y10-N001 cable, you might see link flaps after the ports come up.|
| 3436287  | The NVIDIA SN5600 switch does not support connecting to a Spectrum 1 switch using a 2x breakout with the MCP7Y60-H001 cable at 25G. |
| 3436229  | On the NVIDIA SN5600 switch, when you connect a service port to non-NVIDIA devices, auto-negotiation is not supported for 25G links.|
| 3436215  | On the NVIDIA SN5600 switch, the thermal control service crashes when you remove a fan tray.|
| 3434855  | If the SDK becomes stuck and not able to process API calls, the `systemd` watchdog stops `switchd` and Cumulus Linux generates a `cl-support` file. `switchd` restarts after the watchdog timeout and then runs without issues. |
| 3419124  | On rare occasions, LLDP and other CPU originated IP packets that egress a port might get replicated in the data plane and forwarded out of another port as well. The peer node might discard the unicast packets on the wrong port because of destination MAC address; however, there might be problems with multicast packets, such as LLDP, which uses a multicast MAC address as the destination MAC address. To work around this issue, reboot the switch. |
| 3395489  | On a switch running MLAG, when you configure QoS buffer settings, MLAG peering resets.|
{{< /expand >}}

{{%notice warning%}}
The NVIDIA SN5600 switch is available as a POC and open to customer feedback. Do not use this switch in production; it is not supported through NVIDIA networking support.
{{%/notice%}}
<!-- vale off -->
## What's New in Cumulus Linux 5.4.0
<!-- vale on -->
Cumulus Linux 5.4.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

{{%notice note%}}
Early access features are now called beta features.
{{%/notice%}}

{{%notice warning%}}
- If you configured breakout ports with NVUE commands in Cumulus Linux 5.3 and earlier, the new port configuration changes might impact your Cumulus Linux 5.4 upgrade. Refer to {{<link url="Switch-Port-Attributes/#important-upgrade-information-for-breakout-ports-and-nvue" text="Important Upgrade Information for Breakout Ports and NVUE">}} for important upgrade information.
- Cumulus Linux 5.4 package upgrade (`apt-upgrade`) does not support warm restart to complete the upgrade; performing an unsupported upgrade can result in unexpected or undesirable behavior, such as a traffic outage. Refer to {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="Package Upgrade">}} for important information about package upgrade and warm restart.
{{%/notice%}}

### Platforms

- NVIDIA SN3750-SX (100G Spectrum-2) available for beta

{{%notice warning%}}
The NVIDIA SN3750-SX switch is available for [beta]({{<ref "/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined" >}}) and open to customer feedback. Do not use this switch in production; it is not supported through NVIDIA networking support.
{{%/notice%}}

### New Features and Enhancements

- Port configuration changes:
   - New format for {{<link url="Switch-Port-Attributes/#configure-a-breakout-port" text="port breakouts">}} in the `/etc/cumulus/ports.conf` file
   - {{<link url="Switch-Port-Attributes/#configure-a-breakout-port" text="Breakout port speed">}} configuration is now in the `/etc/network/interfaces` file
   - New {{<link url="Switch-Port-Attributes/#configure-port-lanes" text="port lane">}} and {{<link url="Switch-Port-Attributes/#set-the-number-of-lanes-per-split-port" text="breakout port lane">}} configuration settings
- 1G support (beta) for all NVIDIA Spectrum-2 and Spectrum-3 switches
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="User-Accounts" text="User management">}} commands
  - {{<link url="TACACS" text="TACACS+">}} commands (beta)
  - {{<link url="Supported-Route-Table-Entries/#supported-route-entries" text="ASIC Resource Slicing">}} (KVD) commands
  - {{<link url="Link-Layer-Discovery-Protocol/#set-lldp-mode" text="LLDP commands">}} to send either CDP frames only or LLDP frames only
  - QoS commands for {{<link url="Quality-of-Service/#shaping" text="egress traffic shaping">}}, {{<link url="Quality-of-Service/#pause-frames" text="link pause">}}, {{<link url="Quality-of-Service/#8021p-or-dscp-for-marking" text="traffic remarking">}}, and {{<link url="Quality-of-Service/#advanced-buffer-tuning" text="advanced buffer configuration">}}
  - {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="Search for a specific configuration">}} in the entire object model
  - {{<link url="NVUE-CLI/#configure-auto-save" text="Auto save configuration">}} option
  - {{<link url="NVUE-CLI/#add-configuration-apply-messages" text="Configuration apply messages">}}
  - New BGP show commands to show {{<link url="Troubleshooting-BGP/#bgp-update-groups" text="update groups">}}
  - Updated BGP {{<link url="Virtual-Routing-and-Forwarding-VRF/#verify-route-leaking-configuration" text="route import">}} show commands now show operational data
  - New {{<link url="Troubleshooting-EVPN" text="EVPN show commands">}} to show {{<link url="Troubleshooting-EVPN#show-the-vni-evpn-routing-table" text="EVPN local RIB">}} and {{<link url="Troubleshooting-EVPN/#show-evpn-vnis" text="VNI">}} information
  - The `nv set evpn evi`, `nv unset evpn evi`, and `nv show evpn evi` commands are now `nv set evpn vni`, `nv unset evpn vni`, and `nv show evpn vni`
  - Obfuscated passwords to protect passwords from casual viewing
  - The NVUE `startup.yaml` file shows NVUE version information in addition to saved configuration
  <!-- - {{<link url="Precision-Time-Protocol-PTP#ptp-traffic-shaping" text="PTP Shaping">}} for Spectrum 1 (Beta)-->
  - New commands:
   {{< tabs "TabID40 ">}}
{{< tab "show commands ">}}

```
nv show router nexthop rib
nv show router nexthop rib <nhg-id>
nv show router nexthop rib <nhg-id> resolved-via
nv show router nexthop rib <nhg-id> resolved-via <resolved-via-id>
nv show router nexthop rib <nhg-id> resolved-via-backup
nv show router nexthop rib <nhg-id> resolved-via-backup <resolved-via-id>
nv show router nexthop rib <nhg-id> depends
nv show router nexthop rib <nhg-id> dependents
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
nv show qos link-pause
nv show qos link-pause <profile-id>
nv show qos remark
nv show qos remark <profile-id>
nv show qos remark <profile-id> switch-priority
nv show qos remark <profile-id> switch-priority <qos-sp-id>
nv show qos egress-shaper
nv show qos egress-shaper <profile-id>
nv show qos egress-shaper <profile-id> traffic-class
nv show qos egress-shaper <profile-id> traffic-class <qos-tc-id>
nv show qos buffer
nv show qos buffer pool
nv show qos buffer multicast-switch-priority
nv show interface <interface-id> qos link-pause
nv show interface <interface-id> qos remark
nv show interface <interface-id> qos remark switch-priority
nv show interface <interface-id> qos remark switch-priority <qos-sp-id>
nv show interface <interface-id> qos egress-shaper
nv show interface <interface-id> qos egress-shaper traffic-class
nv show interface <interface-id> qos egress-shaper traffic-class <qos-tc-id>
nv show interface <interface-id> qos buffer
nv show interface <interface-id> qos buffer ingress-port
nv show interface <interface-id> qos buffer ingress-priority-group
nv show interface <interface-id> qos buffer egress-port
nv show interface <interface-id> qos buffer egress-traffic-class
nv show interface <interface-id> qos buffer egress-multicast
nv show system config auto-save
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
nv show vrf <vrf-id> evpn bgp-info
nv show vrf <vrf-id> evpn remote-router-mac
nv show vrf <vrf-id> evpn remote-router-mac <mac-address-id>
nv show vrf <vrf-id> evpn nexthop-vtep
nv show vrf <vrf-id> evpn nexthop-vtep <nexthop-vtep-id>
nv show vrf <vrf-id> router bgp nexthop
nv show vrf <vrf-id> router bgp nexthop <afi>
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id>
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id> resolved-via
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id> path
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id> sub-group
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
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id> sub-group
```

{{< /tab >}}
{{< tab "set commands ">}}

```
nv set evpn vni <vni-id>
nv set evpn vni <vni-id> route-advertise
nv set evpn vni <vni-id> route-advertise svi-ip (on|off|auto)
nv set evpn vni <vni-id> route-advertise default-gateway (on|off|auto)
nv set evpn vni <vni-id> route-target
nv set evpn vni <vni-id> route-target export <rt-id>
nv set evpn vni <vni-id> route-target import <rt-id>
nv set evpn vni <vni-id> route-target both <rt-id>
nv set evpn vni <vni-id> rd (auto|<route-distinguisher>)
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
nv set qos link-pause <profile-id>
nv set qos link-pause <profile-id> xoff-threshold <value>
nv set qos link-pause <profile-id> xon-threshold <value>
nv set qos link-pause <profile-id> port-buffer <value>
nv set qos link-pause <profile-id> cable-length 1-100000
nv set qos link-pause <profile-id> tx (enable|disable)
nv set qos link-pause <profile-id> rx (enable|disable)
nv set qos remark <profile-id>
nv set qos remark <profile-id> switch-priority <qos-sp-id>
nv set qos remark <profile-id> switch-priority <qos-sp-id> pcp 0-7
nv set qos remark <profile-id> switch-priority <qos-sp-id> dscp 0-63
nv set qos remark <profile-id> rewrite (l2|l3|both)
nv set qos egress-shaper <profile-id>
nv set qos egress-shaper <profile-id> traffic-class <qos-tc-id>
nv set qos egress-shaper <profile-id> traffic-class <qos-tc-id> min-rate 0-2147483647
nv set qos egress-shaper <profile-id> traffic-class <qos-tc-id> max-rate 0-2147483647
nv set qos egress-shaper <profile-id> port-max-rate 0-2147483647
nv set interface <interface-id> link breakout <mode-id>
nv set interface <interface-id> link breakout <mode-id> lanes-per-port (1|2|4|8)
nv set interface <interface-id> link lanes (1|2|4|8)
nv set interface <interface-id> qos link-pause
nv set interface <interface-id> qos link-pause profile <profile-name>
nv set interface <interface-id> qos remark
nv set interface <interface-id> qos remark profile <profile-name>
nv set interface <interface-id> qos egress-shaper
nv set interface <interface-id> qos egress-shaper profile <profile-name>
nv set service lldp mode
nv set service ptp <instance-id> logging-level
nv set system config auto-save
nv set system config auto-save enable (on|off)
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
```

{{< /tab >}}
{{< tab "unset commands ">}}

```
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
nv unset qos link-pause
nv unset qos link-pause <profile-id>
nv unset qos link-pause <profile-id> xoff-threshold
nv unset qos link-pause <profile-id> xon-threshold
nv unset qos link-pause <profile-id> port-buffer
nv unset qos link-pause <profile-id> cable-length
nv unset qos link-pause <profile-id> tx
nv unset qos link-pause <profile-id> rx
nv unset qos remark
nv unset qos remark <profile-id>
nv unset qos remark <profile-id> switch-priority
nv unset qos remark <profile-id> switch-priority <qos-sp-id>
nv unset qos remark <profile-id> switch-priority <qos-sp-id> pcp
nv unset qos remark <profile-id> switch-priority <qos-sp-id> dscp
nv unset qos remark <profile-id> rewrite
nv unset qos egress-shaper
nv unset qos egress-shaper <profile-id>
nv unset qos egress-shaper <profile-id> traffic-class
nv unset qos egress-shaper <profile-id> traffic-class <qos-tc-id>
nv unset qos egress-shaper <profile-id> traffic-class <qos-tc-id> min-rate
nv unset qos egress-shaper <profile-id> traffic-class <qos-tc-id> max-rate
nv unset qos egress-shaper <profile-id> port-max-rate
nv unset interface <interface-id> link breakout <mode-id> lanes-per-port
nv unset interface <interface-id> link lanes
nv unset interface <interface-id> qos link-pause
nv unset interface <interface-id> qos link-pause
nv unset interface <interface-id> qos link-pause profile
nv unset interface <interface-id> qos remark
nv unset interface <interface-id> qos remark profile
nv unset interface <interface-id> qos egress-shaper
nv unset interface <interface-id> qos egress-shaper profile
nv unset service lldp mode
nv unset service ptp <instance-id> logging-level
nv unset system config auto-save
nv unset system config auto-save enable
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
```

{{< /tab >}}
{{< /tabs >}}
  
{{%notice info%}}
Cumulus Linux 5.4 includes the NVUE object model. After you upgrade to Cumulus Linux 5.4, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
