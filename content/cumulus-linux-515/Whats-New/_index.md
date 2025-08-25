---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.14 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.14, see the {{<link title="Cumulus Linux 5.14 Release Notes" text="Cumulus Linux 5.14 Release Notes">}}.
- To upgrade to Cumulus Linux 5.14, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.14

Cumulus Linux 5.14.0 contains several new features and improvements, and provides bug fixes.

### New Features and Enhancements

- FRR upgrade to 10.0.3
- {{<link title="Erase all Data from the Switch" text="Erase all data from the switch">}} now generally available
- {{<link url="Switch-Port-Attributes/#auto-negotiation-and-link-speed" text="Link speed setting and auto-negotiation behavior change">}}
- {{<link url="Packet-Trimming" text="Packet trimming">}}
- {{<link url="RDMA-over-Converged-Ethernet-RoCE/#lossy-multi-tc-profile" text="RoCE lossy multi TC profile">}}
- {{<link url="Segment-Routing" text="Segment routing">}} and {{<link url="Segment-Routing/#clear-srv6-statistics" text="Clear SRv6 statistics">}}
- gNMI:
  - {{<link url="gNMI-Streaming/#metrics" text="New gNMI streaming metrics: Adaptive routing, packet trimming, SRv6, BGP, interface, LLDP, system, and platform">}}
  - {{<link url="gNMI-Streaming/#user-credentials-and-authentication" text="gRPC header based authentication support for gNMI subscription requests">}}
  - {{<link url="gNMI-Streaming/#gnmi-client-requests" text="Improved data formatting to include prefix field">}}
- {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#transceiver-thermal-control" text="Transceiver thermal control">}}
- {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#clear-interface-physical-layer-error-counters" text="Clear physical layer error counters for an interface">}}
- {{<link url="DHCP-Relays" text="Configure different DHCP servers per interface for DHCP relay">}}
- {{<link url="Quick-Start-Guide/#configure-the-domain-name" text="Domain name configuration">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#enable-adaptive-routing" text="Adaptive routing default profiles profile-1 and profile-2 removed and replaced with one profile that uses the default profile settings for your switch ASIC type">}}
- {{<link url="NVUE-API/#jwt-based-authentication" text="JWT authentication for REST API">}}
- {{<link url="TACACS/#tacacs-per-command-authorization" text="You can now bind TACACS per-command authorization to the default VRF">}} (in previous releases, you must specify the egress interface you use in the default VRF)
- {{< expand "Operational information added to NVUE BGP show commands" >}}
See {{<link url="Troubleshooting-BGP" text="Troubleshooting BGP">}} for command examples.

```
nv show router bgp
nv show router bgp convergence-wait
nv show router bgp graceful-restart
nv show router bgp queue-limit
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel
nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel
nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6
nv show vrf <vrf-id> router bgp path-selection
nv show vrf <vrf-id> router bgp path-selection med
nv show vrf <vrf-id> router bgp path-selection aspath
nv show vrf <vrf-id> router bgp path-selection multipath
nv show vrf <vrf-id> router bgp neighbor <interface-id> bfd
nv show vrf <vrf-id> router bgp neighbor <interface-id> local-as
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn
```
{{< /expand >}}
- {{< expand "New and updated vtysh commands" >}}
- The following lists the updated and new vtysh show bgp commands. To see command examples, refer to {{<link url="Troubleshooting-BGP" text="Troubleshooting BGP">}}.
```
show bgp router json
show bgp vrfs <vrf-id> json
show bgp vrf <vrf-id> bestpath json 
show bgp vrf <vrf-id> ipv4 unicast redistribute json 
show bgp vrf <vrf-id> ipv6 unicast redistribute json 
```

- In Cumulus Linux 5.14, the vtysh command to configure the area for OSPFv3 interfaces is under the interface instead of under `router ospf6`.

  If you configure OSPFv3 areas with NVUE snippets in Cumulus Linux 5.13 and earlier, you must delete the snippets before you upgrade to Linux 5.14, then reconfigure the areas for OSPFv3 interfaces with the new vtysh commands after upgrade. See {{<link url="Open-Shortest-Path-First-v3-OSPFv3/#basic-ospfv3-configuration" text="Basic OSPFv3 Configuration">}}.
{{< /expand >}}
- NVUE
  - {{<link url="Troubleshooting-EVPN/#show-evpn-vnis-across-all-vrfs" text="Commands to show EVPN information across all VRFs">}}
  - {{< expand "Changed NVUE commands and options" >}}
| Cumulus Linux 5.14 | Cumulus Linux 5.13 and Earlier |
| --------------- |---------------------------------------|
| BGP community `0:0`| BGP community `internet`|
| BGP `enforce-first-as` option is ON by default | BGP `enforce-first-as` option is OFF by default |
| The `nv set router adaptive-routing profile` option is `profile-custom` | The `nv set router adaptive-routing profile` options are `profile-1`, `profile-2`, or `profile-custom` |
| The `nv set system aaa radius server <hostname-id> priority` setting is between 1 and 100| The `nv set system aaa radius server <hostname-id> priority` setting is between 1 and 8|
|`nv set vrf <vrf-id> router bgp address-family <address-family> route-import from-vrf list <leak-vrf-id>`| `nv set vrf <vrf-id> router bgp address-family <address-family> route-import from-vrf list`|
| `nv set system telemetry ai-ethernet-stats`| `nv set system telemetry adaptive-routing-stats`|
| `nv set system telemetry stats-group <group-id> ai-ethernet-stats` | `nv set system telemetry stats-group <sg-id> adaptive-routing-stats`|
{{< /expand >}}
  - {{< expand "Removed NVUE commands" >}}
```
nv set service dhcp-relay <vrf-id> interface <interface-id>
nv set service dhcp-relay <vrf-id> server <server-id>
nv show service dhcp-relay <vrf-id> server
nv set service dhcp-relay <vrf-id> agent remote-id
```
{{< /expand >}}
  - {{< expand "New NVUE commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show interface <interface-id> link phy-detail hardware 
nv show interface <interface-id> packet-trim
nv show interface <interface-id> packet-trim egress-eligibility
nv show interface <interface-id> packet-trim egress-eligibility traffic-class
nv show interface <interface-id> packet-trim egress-eligibility traffic-class <tc-id>
nv show interface qos-congestion-control
nv show interface qos-roce-counters
nv show interface qos-roce-status
nv show interface qos-roce-status-pool-map
nv show platform transceiver <interface-id> temperature
nv show service dhcp-relay <vrf-id> server-group
nv show service dhcp-relay <vrf-id> server-group <server-group-id>
nv show service dhcp-relay <vrf-id> server-group <server-group-id> server
nv show service dhcp-relay <vrf-id> server-group <server-group-id> server <server-id>
nv show service dhcp-relay <vrf-id> server-group <server-group-id> upstream-interface
nv show service dhcp-relay <vrf-id> server-group <server-group-id> upstream-interface <interface-id>
nv show service dhcp-relay <vrf-id> downstream-interface
nv show service dhcp-relay <vrf-id> downstream-interface <downstream-interface-id>
nv show system forwarding packet-trim
nv show system forwarding packet-trim remark
nv show router segment-routing
nv show router segment-routing srv6
nv show router segment-routing srv6 stats sid <sid>
nv show router segment-routing srv6 stats no-sid-drops
nv show router segment-routing srv6 locator
nv show router segment-routing srv6 locator <locator-name>
nv show router segment-routing srv6 sid
nv show router segment-routing srv6 sid <sid>
nv show router segment-routing static
nv show router segment-routing static srv6-sid <sid>
nv show vrf evpn  --view=evpn
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set platform transceiver <interface-id> temperature setpoint
nv set router segment-routing srv6 locator <locator-name>
nv set router segment-routing srv6 locator <locator-name> prefix <ipv6-prefix>
nv set router segment-routing srv6 locator <locator-name> block-length (32-32)
nv set router segment-routing srv6 locator <locator-name> node-length (16-16)
nv set router segment-routing srv6 locator <locator-name> func-length (0-0)
nv set router segment-routing srv6 state (enabled|disabled)
nv set router segment-routing static srv6-sid <sid>
nv set router segment-routing static srv6-sid <sid> locator-name <value>
nv set router segment-routing static srv6-sid <sid> behavior (uN|uA)
nv set router segment-routing static srv6-sid <sid> interface <interface-id>
nv set service dhcp-relay <vrf-id> server-group <server-group-id>
nv set service dhcp-relay <vrf-id> server-group <server-group-id> server <server-id>
nv set service dhcp-relay <vrf-id> server-group <server-group-id> upstream-interface <interface-id>
nv set service dhcp-relay <vrf-id> downstream-interface <downstream-interface-id> server-group-name <value>
nv set system api token-expiration
nv set system dns domain <domain-name>
nv set interface <interface-id> packet-trim egress-eligibility traffic-class <tc-id>
nv set system forwarding packet-trim remark dscp
nv set system forwarding packet-trim state
nv set system forwarding packet-trim size
nv set system forwarding packet-trim profile packet-trim-default
nv set system forwarding packet-trim switch-priority
nv set system forwarding packet-trim service-port <port>
nv set system telemetry ai-ethernet-stats export state
nv set system telemetry ai-ethernet-stats sample-interval
nv set system telemetry platform-stats class platform-info state
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset platform transceiver <interface-id> temperature setpoint
nv unset router segment-routing
nv unset router segment-routing srv6
nv unset router segment-routing srv6 locator
nv unset router segment-routing srv6 locator <locator-name>
nv unset router segment-routing srv6 locator <locator-name> prefix
nv unset router segment-routing srv6 locator <locator-name> block-length
nv unset router segment-routing srv6 locator <locator-name> node-length
nv unset router segment-routing srv6 locator <locator-name> func-length
nv unset router segment-routing srv6 state
nv unset router segment-routing static
nv unset router segment-routing static srv6-sid
nv unset router segment-routing static srv6-sid <sid>
nv unset router segment-routing static srv6-sid <sid> locator-name
nv unset router segment-routing static srv6-sid <sid> behavior
nv unset router segment-routing static srv6-sid <sid> interface
nv unset system api token-expiration
nv unset system dns
nv unset system dns domain
nv unset service dhcp-relay <vrf-id> server-group
nv unset service dhcp-relay <vrf-id> server-group <server-group-id>
nv unset service dhcp-relay <vrf-id> server-group <server-group-id> server
nv unset service dhcp-relay <vrf-id> server-group <server-group-id> server <server-id>
nv unset service dhcp-relay <vrf-id> server-group <server-group-id> upstream-interface
nv unset service dhcp-relay <vrf-id> server-group <server-group-id> upstream-interface <interface-id>
nv unset service dhcp-relay <vrf-id> downstream-interface <downstream-interface-id> server-group-name
nv unset interface <interface-id> packet-trim
nv unset interface <interface-id> packet-trim egress-eligibility
nv unset interface <interface-id> packet-trim egress-eligibility traffic-class
nv unset interface <interface-id> packet-trim egress-eligibility traffic-class <tc-id>
nv unset system forwarding packet-trim
nv unset system forwarding packet-trim remark
nv unset system forwarding packet-trim remark dscp
nv unset system forwarding packet-trim state
nv unset system forwarding packet-trim size
nv unset system forwarding packet-trim profile
nv unset system forwarding packet-trim switch-priority
nv unset system forwarding packet-trim service-port
nv unset system telemetry ai-ethernet-stats export state
nv unset system telemetry ai-ethernet-stats sample-interval
nv unset system telemetry platform-stats class platform-info state
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action clear interface <interface-id> link phy-detail
nv action clear router segment-routing srv6 stats
nv action clear router segment-routing srv6 stats sid
nv action clear router segment-routing srv6 stats sid <sid>
nv action clear router segment-routing srv6 stats no-sid-drops
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.14.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.14 from Cumulus Linux 5.12.0 and later.

You can use {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.14 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- Cumulus Linux 5.13.1
- Cumulus Linux 5.13.0
- Cumulus Linux 5.12.1
- Cumulus Linux 5.12.0

To upgrade to Cumulus Linux 5.14 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux 5.13 and later includes a new option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. After upgrading to Cumulus Linux 5.14 from 5.12, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

{{%notice warning%}}
If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.14 or later.
{{%/notice%}}

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.14 or later, or after a new binary image installation:

1.  Disable NVUE auto save:

   ```
   cumulus@switch:~$ nv set system config auto-save state disabled
   cumulus@switch:~$ nv config apply
   cumulus@switch:~$ nv config save
   ```

2. Delete the `/etc/nvue.d/startup.yaml` file:

   ```
   cumulus@switch:~$ sudo rm -rf /etc/nvue.d/startup.yaml
   ```

3. Add the `PASSWORD_NVUE_SYNC=no` line to the `/etc/default/nvued` file:
   ```
   cumulus@switch:~$ sudo nano /etc/default/nvued
   PASSWORD_NVUE_SYNC=no
   ```

### DHCP Lease with the host-name Option

When a Cumulus Linux switch with NVUE enabled receives a DHCP lease containing the host-name option, it ignores the received hostname and does not apply it. For details, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Hostname-Option-Received-From-DHCP-Ignored" >}}).

### DHCP Relay Configuration

Cumulus Linux 5.14 introduces server groups and no longer provides the `nv show service dhcp-relay <vrf-id> server` commands. In Cumulus Linux 5.13 and earlier, DHCP relay does not use server groups, but instead, forwards all DHCP client requests to every DHCP server within the same VRF.

If you have configured DHCP relay in Cumulus Linux 5.13 or earlier, the upgrade process migrates the configuration to a new default configuration file called `isc-dhcp-relay-<server-group-id>-<vrf-id>` in the `/etc/default` directory and selects the uplink and downlink interfaces automatically. After upgrade, make sure to review the new configuration and adjust as needed.

### NVUE Commands After Upgrade

Cumulus Linux 5.14 includes the NVUE object model. After you upgrade to Cumulus Linux 5.14, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA AIR">}}.
