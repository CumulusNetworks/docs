---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.13 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.13, see the {{<link title="Cumulus Linux 5.13 Release Notes" text="Cumulus Linux 5.13 Release Notes">}}.
- To upgrade to Cumulus Linux 5.13, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

{{%notice infonopad%}}
The upcoming Cumulus Linux 5.15.0 release includes updates to NVUE commands. These changes aim to standardize commands across Cumulus Linux, NVIDIA OS (NVOS), and Host-based Networking. To help you prepare, NVIDIA recommends reviewing the [list of NVUE command changes]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Configuration/NVUE-Command-Changes-515" >}}) so that you can update any automation accordingly.
{{%/notice%}}
## What's New in Cumulus Linux 5.13.1

Cumulus Linux 5.13.1 supports the NVIDIA SN5610 switch and provides bug fixes.

## What's New in Cumulus Linux 5.13

Cumulus Linux 5.13.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN5600D (800G Spectrum-4 DC version)

### New Features and Enhancements

- NVIDIA SN5400 ITU-T G.8273.2 Class C (Compliance)
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#enable-adaptive-routing" text="Enabling adaptive routing no longer restarts switchd">}}
- {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Optimized upgrade supports warm restart mode">}}
- {{<link url="802.1X-Interfaces/#ignore-reauthorization-timeout" text="802.1 option to keep the port in the current state when the RADIUS server is unreachable">}}
- {{<link url="DHCP-Servers/#multiple-static-ip-address-assignments" text="Support two DHCP static IP address assignments per port for a single host">}}
- {{<link url="Syslog/#selectors-and-filters" text="syslog log filters">}}
- {{<link title="Erase all Data from the Switch" text="Erase all data from the switch">}} (Beta)
- {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#amber-phy-health-management" text="Show SNR information for OSFP 100G per lane capable transceivers">}}
- {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="New maintenance mode commands">}}
- {{<link url="RADIUS-AAA/#optional-radius-configuration" text="RADIUS multiple VRF support">}} and {{<link url="RADIUS-AAA/#optional-radius-configuration" text="RADIUS require-message-authenticate attribute">}}
- {{<link url="SSH-for-Remote-Access/#message-of-the-day" text="Message of the day shows system reboot cause and health information">}}
- Telemetry
  - {{<link url="gNMI-Streaming/#gnmi-with-cumulus-linux" text="gNMI streaming with Cumulus Linux">}}
  - {{<link url="Open-Telemetry-Export/#adaptive-routing-statistics" text="OTEL adaptive routing statistics">}}
  - {{<link url="Open-Telemetry-Export/#lldp-statistics" text="OTEL LLDP metrics">}}
  - {{<link url="Open-Telemetry-Export/#software-statistics" text="OTEL systemd software metrics">}}
  - {{<link url="Open-Telemetry-Export/#platform-statistics" text="OTEL transceiver statistics">}}
  - {{<link url="Open-Telemetry-Export/#temporality-mode" text="OTEL temporality mode for histogram metrics">}}
- NVUE
  - {{<link url="NVUE-CLI/#list-directory-contents" text="Command to list directory contents">}}
  - {{<link url="NVUE-CLI/#get-the-hash-for-a-file" text="Command to get the hash for a file">}}
  - {{<link url="802.1X-Interfaces/#configure-8021x-interfaces" text="Commands to set the NAS IP address and NAS identifier for 802.1X">}}
  - {{<link url="System-Power/#power-cycle" text="Command to power cycle the switch">}}
  - {{<link url="SSH-for-Remote-Access/#certificate-based-authentication" text="SSH certificate-based authentication">}}
  - {{<link url="User-Accounts/#default-roles" text="Terminate a user session when you change the user role">}}
  - {{<link url="NVUE-CLI/#security-with-certificates-and-crls" text="CRL support">}}
  - {{<link url="NVUE-CLI/#replace-and-patch-a-pending-configuration" text="Replace and patch against a plain text file of nv set and nv unset commands">}}
  - {{<link url="NVUE-CLI/#maximum-revisions-limit" text="Maximum NVUE revisions limit">}}
  - {{<link url="NVUE-CLI/#view-differences-between-configurations" text="nv config diff --verbose option ">}} to see both previous and new configuration
  - {{<link url="Troubleshooting-BGP/#show-bgp-route-information" text="Filter BGP received routes by neighbor">}} and {{<link url="Troubleshooting-EVPN/#filter-evpn-routes-by-neighbor-rd-and-route-type" text="filter EVPN recieved routes by neighbor, RD and route type">}}
  - {{<link url="Monitoring-System-Hardware/#nvue-commands" text="Updated system health command output">}}
  - {{< expand "Changed NVUE Commands" >}}
| Cumulus Linux 5.13 | Cumulus Linux 5.12 and Earlier |
| --------------- |---------------------------------------|
| `nv set maintenance unit all-protocols mode enabled`| `nv action enable system maintenance mode` |
| `nv set maintenance unit all-protocols mode disabled` | `nv action disable system maintenance mode` |
| `nv set maintenance unit all-interfaces mode enabled` | `nv action enable system maintenance ports` |
| `nv set maintenance unit all-interfaces mode disabled` | `nv action disable system maintenance ports` |
| `nv set system syslog server <server-id>` | `nv set service syslog <vrf> server <server-id>`|
| `nv set system syslog server <server-id> port <port>` | `nv set service syslog <vrf> server <server-id> port <port>`|
| `nv set system syslog server <server-id> protocol <protocol>` | `nv set service syslog <vrf> server <server-id> protocol <protocol>`|
| `nv show system syslog`| `nv show service syslog`|
| `nv show system version` | Output includes `base-os` and `product-release` fields.|
| `nv show system version packages installed` | `nv show platform software`|
| `nv show --output native`| `nv show --output raw`|

{{< /expand >}}
  - {{< expand "Removed NVUE Commands" >}}
```
nv action enable system maintenance mode
nv action enable system maintenance ports
nv action disable system maintenance mode
nv action disable system maintenance ports
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-server-client
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-server-client
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-server-client
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-server-client
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-server-client
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-server-client
nv show service ptp <instance-id> domain 
nv show service ptp <instance-id> priority1
nv show service ptp <instance-id> priority2
nv show service ptp <instance-id> ip-dscp
nv show service ptp <instance-id> ipv6-scope
nv show service ptp <instance-id> servo
nv show service ptp <instance-id> force-version
nv show platform software
nv show platform software installed
nv show platform software installed <installed-id>
nv show system maintenace
```
{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show system aaa user <user-id> ssh cert-auth
nv show system aaa user <user-id> ssh cert-auth principals
nv show system aaa user <user-id> ssh cert-auth principals <cert-auth-principal>
nv show system gnmi-server
nv show system gnmi-server listening-address
nv show system gnmi-server listening-address <listening-address-id>
nv show system gnmi-server mtls
nv show system gnmi-server status
nv show system gnmi-server status client
nv show system gnmi-server status client <client-address-id>
nv show system grpc-tunnel
nv show system grpc-tunnel server
nv show system grpc-tunnel server <server-name-id>
nv show system grpc-tunnel server <server-name-id> status
nv show system grpc-tunnel server <server-name-id> status connection
nv show system security crl
nv show system security crl <crl-id>
nv show system ssh-server trusted-ca-keys
nv show system ssh-server trusted-ca-keys <ssh-trusted-ca-key-id>
nv show system syslog
nv show system syslog format
nv show system syslog server
nv show system syslog server <server-id>
nv show system syslog server <server-id> selector
nv show system syslog server <server-id> selector <priority-id>
nv show system syslog selector
nv show system syslog selector <selector-id>
nv show system syslog selector <selector-id> rate-limit
nv show system syslog selector <selector-id> filter
nv show system syslog selector <selector-id> filter <filter-id>
nv show system telemetry adaptive-routing-stats
nv show system telemetry adaptive-routing-stats export
nv show system telemetry software-stats
nv show system telemetry software-stats systemd
nv show system telemetry software-stats systemd export
nv show system telemetry software-stats systemd unit-profile
nv show system telemetry software-stats systemd unit-profile <unit-profile-id>
nv show system telemetry software-stats systemd unit-profile <unit-profile-id> unit
nv show system telemetry platform-stats class transceiver-info
nv show system telemetry lldp
nv show system telemetry lldp export
nv show system telemetry stats-group <stats-group-id> adaptive-routing-stats
nv show system telemetry stats-group <stats-group-id> adaptive-routing-stats export
nv show system telemetry stats-group <stats-group-id> software-stats
nv show system telemetry stats-group <stats-group-id> software-stats systemd
nv show system telemetry stats-group <stats-group-id> software-stats systemd export
nv show system telemetry stats-group <stats-group-id> platform-stats class transceiver-info
nv show system telemetry stats-group <stats-group-id> lldp
nv show system telemetry stats-group <stats-group-id> lldp export
nv show system version
nv show system version image
nv show system version packages installed
nv show system version packages installed <package_name>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set maintenance unit <unit-name>
nv set maintenance unit <unit-name> mode
nv set maintenance unit <unit-name> interfaces <value>
nv set maintenance unit <unit-name> protocols <value>
nv set service dhcp-server <vrf-id> static <static-id> vendor-class <value>
nv set service dhcp-server6 <vrf-id> static <static-id> vendor-class <value>
nv set system aaa radius require-message-authenticator
nv set system aaa radius server <server-id> vrf <vrf-id>
nv set system aaa user <user> ssh cert-auth state
nv set system aaa user <user> ssh cert-auth principals <principal>
nv set system api mtls crl <value>
nv set system dot1x radius nas-identifier
nv set system dot1x radius nas-ip-address
nv set system dot1x reauth-timeout-ignore
nv set system gnmi-server listening-address <listening-address-id>
nv set system gnmi-server mtls ca-certificate <value>
nv set system gnmi-server mtls crl <value>
nv set system gnmi-server state
nv set system gnmi-server certificate self-signed
nv set system gnmi-server port
nv set system grpc-tunnel server <server-name-id>
nv set system grpc-tunnel server <server-name-id> state
nv set system grpc-tunnel server <server-name-id> target-name
nv set system grpc-tunnel server <server-name-id> address
nv set system grpc-tunnel server <server-name-id> port
nv set system grpc-tunnel server <server-name-id> certificate self-signed
nv set system grpc-tunnel server <server-name-id> ca-certificate
nv set system grpc-tunnel server <server-name-id> target-type gnmi-gnoi
nv set system grpc-tunnel server <server-name-id> retry-interval
nv set system ssh-server trusted-ca-keys <key-id> key <key-string>
nv set system ssh-server trusted-ca-keys <key-id> type <key-type>
nv set system ssh-server pka-only
nv set system syslog format welf firewall-name
nv set system syslog server <server-id>
nv set system syslog server <server-id> selector <priority-id>
nv set system syslog server <server-id> selector <priority-id> selector-id
nv set system syslog server <server-id> port
nv set system syslog server <server-id> protocol
nv set system syslog server <server-id> vrf <vrf-name>
nv set system syslog selector <selector-id>
nv set system syslog selector <selector-id> rate-limit burst
nv set system syslog selector <selector-id> rate-limit interval
nv set system syslog selector <selector-id> filter <filter-id>
nv set system syslog selector <selector-id> filter <filter-id> match
nv set system syslog selector <selector-id> filter <filter-id> action
nv set system syslog selector <selector-id> facility
nv set system syslog selector <selector-id> program-name
nv set system syslog selector <selector-id> severity
nv set system syslog severity
nv set system syslog server <server-id>
nv set system syslog server <server-id> port
nv set system syslog server <server-id> protocol
nv set system syslog server <server-id> vrf mgmt
nv set system telemetry software-stats systemd export state
nv set system telemetry software-stats systemd unit-profile
nv set system telemetry software-stats systemd unit-profile
nv set system telemetry software-stats systemd sample-interval
nv set system telemetry software-stats systemd process-level
nv set system telemetry software-stats systemd active-profile
nv set system telemetry adaptive-routing-stats export state
nv set system telemetry adaptive-routing-stats sample-interval
nv set system telemetry platform-stats class transceiver-info state
nv set system telemetry platform-stats class transceiver-info sample-interval
nv set system telemetry histogram temporality
nv set system telemetry lldp export state
nv set system telemetry lldp sample-interval
nv set system telemetry stats-group <stats-group-id> adaptive-routing-stats export state
nv set system telemetry stats-group <stats-group-id> adaptive-routing-stats sample-interval
nv set system telemetry stats-group <stats-group-id> software-stats systemd export state
nv set system telemetry stats-group <stats-group-id> software-stats systemd sample-interval
nv set system telemetry stats-group <stats-group-id> software-stats systemd process-level
nv set system telemetry stats-group <stats-group-id> software-stats systemd active-profile
nv set system telemetry stats-group <stats-group-id> histogram temporality
nv set system telemetry stats-group <stats-group-id> platform-stats class transceiver-info state
nv set system telemetry stats-group <stats-group-id> platform-stats class transceiver-info sample-interval
nv set system telemetry stats-group <stats-group-id> lldp export state
nv set system telemetry stats-group <stats-group-id> lldp sample-interval
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset maintenance
nv unset maintenance unit
nv unset maintenance unit <unit-name>
nv unset maintenance unit <unit-name> mode
nv unset maintenance unit <unit-name> interfaces
nv unset maintenance unit <unit-name> protocols
nv unset service dhcp-server <vrf> static <host> vendor-class
nv unset service dhcp-server6 <vrf> static <host> vendor-class
nv unset system aaa user <user-id> ssh cert-auth
nv unset system aaa user <user-id> ssh cert-auth principals
nv unset system aaa user <user-id> ssh cert-auth principals <cert-auth-principal>
nv unset system aaa user <user-id> ssh cert-auth state
nv unset system aaa radius require-message-authenticator
nv unset system aaa radius server <server-id> vrf
nv unset system api mtls crl
nv unset system dot1x radius nas-identifier
nv unset system dot1x radius nas-ip-address
nv unset system dot1x reauth-timeout-ignore
nv unset system gnmi-server mtls
nv unset system gnmi-server mtls ca-certificate
nv unset system gnmi-server mtls crl
nv unset system gnmi-server state
nv unset system gnmi-server certificate
nv unset system gnmi-server port
nv unset system grpc-tunnel
nv unset system grpc-tunnel server
nv unset system grpc-tunnel server <server-name-id>
nv unset system grpc-tunnel server <server-name-id> state
nv unset system grpc-tunnel server <server-name-id> target-name
nv unset system grpc-tunnel server <server-name-id> address
nv unset system grpc-tunnel server <server-name-id> port
nv unset system grpc-tunnel server <server-name-id> certificate
nv unset system grpc-tunnel server <server-name-id> ca-certificate
nv unset system grpc-tunnel server <server-name-id> target-type
nv unset system grpc-tunnel server <server-name-id> retry-interval
nv unset system ssh-server trusted-ca-keys
nv unset system ssh-server trusted-ca-keys <key-id> key
nv unset system ssh-server trusted-ca-keys <ssh-trusted-ca-key-id>
nv unset system ssh-server trusted-ca-keys <ssh-trusted-ca-key-id> key
nv unset system ssh-server trusted-ca-keys <ssh-trusted-ca-key-id> type
nv unset system ssh-server pka-only
nv unset system syslog
nv unset system syslog format
nv unset system syslog format welf
nv unset system syslog format welf firewall-name
nv unset system syslog server
nv unset system syslog server <server-id>
nv unset system syslog server <server-id> selector
nv unset system syslog server <server-id> selector <priority-id>
nv unset system syslog server <server-id> selector <priority-id> selector-id
nv unset system syslog server <server-id> port
nv unset system syslog server <server-id> protocol
nv unset system syslog server <server-id> vrf
nv unset system syslog selector
nv unset system syslog selector <selector-id>
nv unset system syslog selector <selector-id> rate-limit
nv unset system syslog selector <selector-id> rate-limit burst
nv unset system syslog selector <selector-id> rate-limit interval
nv unset system syslog selector <selector-id> filter
nv unset system syslog selector <selector-id> filter <filter-id>
nv unset system syslog selector <selector-id> filter <filter-id> match
nv unset system syslog selector <selector-id> filter <filter-id> action
nv unset system syslog selector <selector-id> facility
nv unset system syslog selector <selector-id> program-name
nv unset system syslog selector <selector-id> severity
nv unset system telemetry software-stats
nv unset system telemetry software-stats systemd
nv unset system telemetry software-stats systemd export
nv unset system telemetry software-stats systemd export state
nv unset system telemetry software-stats systemd unit-profile
nv unset system telemetry software-stats systemd unit-profile <unit-profile-id>
nv unset system telemetry software-stats systemd unit-profile <unit-profile-id> unit
nv unset system telemetry software-stats systemd sample-interval
nv unset system telemetry software-stats systemd process-level
nv unset system telemetry software-stats systemd active-profile
nv unset system telemetry adaptive-routing-stats
nv unset system telemetry adaptive-routing-stats export
nv unset system telemetry adaptive-routing-stats export state
nv unset system telemetry adaptive-routing-stats sample-interval
nv unset system telemetry platform-stats class transceiver-info
nv unset system telemetry platform-stats class transceiver-info state
nv unset system telemetry platform-stats class transceiver-info sample-interval
nv unset system telemetry histogram temporality
nv unset system telemetry lldp
nv unset system telemetry lldp export
nv unset system telemetry lldp export state
nv unset system telemetry lldp sample-interval
nv unset system telemetry stats-group <stats-group-id> adaptive-routing-stats
nv unset system telemetry stats-group <stats-group-id> adaptive-routing-stats export
nv unset system telemetry stats-group <stats-group-id> adaptive-routing-stats export state
nv unset system telemetry stats-group <stats-group-id> adaptive-routing-stats sample-interval
nv unset system telemetry stats-group <stats-group-id> software-stats
nv unset system telemetry stats-group <stats-group-id> software-stats systemd
nv unset system telemetry stats-group <stats-group-id> software-stats systemd export
nv unset system telemetry stats-group <stats-group-id> software-stats systemd export state
nv unset system telemetry stats-group <stats-group-id> software-stats systemd sample-interval
nv unset system telemetry stats-group <stats-group-id> software-stats systemd process-level
nv unset system telemetry stats-group <stats-group-id> software-stats systemd active-profile
nv unset system telemetry stats-group <stats-group-id> histogram temporality
nv unset system telemetry stats-group <stats-group-id> platform-stats class transceiver-info
nv unset system telemetry stats-group <stats-group-id> platform-stats class transceiver-info state
nv unset system telemetry stats-group <stats-group-id> platform-stats class transceiver-info sample-interval
nv unset system telemetry stats-group <stats-group-id> lldp
nv unset system telemetry stats-group <stats-group-id> lldp export
nv unset system telemetry stats-group <stats-group-id> lldp export state
nv unset system telemetry stats-group <stats-group-id> lldp sample-interval
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action erase system disk 
nv action generate system file-hash md5 <filename>
nv action generate system file-hash sha1 <filename>
nv action generate system file-hash sha224 <filename>
nv action generate system file-hash sha256 <filename>
nv action generate system file-hash sha512 <filename>
nv action import system security crl
nv action delete system security crl
nv action list system file-path <path>
nv action power-cycle system
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.13.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.13 from Cumulus Linux 5.11.1 and later.

You can use {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.13 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- Cumulus Linux 5.12.1
- Cumulus Linux 5.12.0
- Cumulus Linux 5.11.1
- Cumulus Linux 5.11.0

To upgrade to Cumulus Linux 5.13 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux 5.13 includes a new option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. After upgrading to Cumulus Linux 5.13, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

{{%notice warning%}}
If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.13 or later.
{{%/notice%}}

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.13 or later, or after a new binary image installation:

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

### NVUE Commands After Upgrade

Cumulus Linux 5.13 includes the NVUE object model. After you upgrade to Cumulus Linux 5.13, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA AIR">}}.
