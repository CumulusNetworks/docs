---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.13 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.13, see the {{<link title="Cumulus Linux 5.13 Release Notes" text="Cumulus Linux 5.13 Release Notes">}}.
- To upgrade to Cumulus Linux 5.13, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.13

Cumulus Linux 5.13.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN5600D (200G Spectrum-4 DC version)

### New Features and Enhancements

- NVIDIA SN5400 ITU-T G.8273.2 Class C (Compliance)
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#enable-adaptive-routing" text="Enabling adaptive routing no longer restarts switchd">}}
- {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="Optimized upgrade supports warmboot">}}
- {{<link url="802.1X-Interfaces/#ignore-reauthorization-timeout" text="802.1 option to keep the port in the current state when the RADIUS server is unreachable">}}
- {{<link url="Monitoring-System-Hardware/#nvue-commands" text="Updated system health command">}}
- {{<link url="DHCP-Servers/#multiple-static-ip-address-assignments" text="Support two DHCP static IP address assignments per port for a single host">}}
- {{<link url="Syslog" text="syslog log filters">}}
- {{<link title="Docker with Cumulus Linux" text="Support Docker containers">}}
- {{<link title="Erase all Data from the Switch" text="Erase all data from the switch">}} (Beta)
- {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#amber-phy-health-management" text="Show SNR information for transceivers">}}
- {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="New maintenance mode commands">}}
- {{<link url="802.1X-Interfaces/#dynamic-vrf-assignments" text="802.1x on router ports with dynamic VRF assignments">}}
- {{<link url="RADIUS-AAA/#optional-radius-configuration" text="RADIUS multiple VRF support">}}
- {{<link url="RADIUS-AAA/#optional-radius-configuration" text="RADIUS require-message-authenticate attribute">}}
- {{<link url="SSH-for-Remote-Access/#message-of-the-day" text="Message of the day shows system reboot cause and health information">}}
- Telemetry
  - {{<link url="gNMI-Streaming" text="gNMI streaming">}}
  - {{<link url="Open-Telemetry-Export/#lldp-statistics" text="OTEL LLDP metrics">}}
  - {{<link url="Open-Telemetry-Export/#adaptive-routing-statistics" text="OTEL Adaptive routing statistics">}}
  - {{<link url="Open-Telemetry-Export/#platform-statistics" text="OTEL Transceiver statistics">}}
  - {{<link url="Open-Telemetry-Export/#temporality-mode" text="OTEL temporality mode for histogram metrics">}}
  - OTEL Buffer Occupancy and watermark metrics
- NVUE
  - {{<link url="NVUE-CLI/#list-directory-contents" text="Command to list directory contents">}}
  - {{<link url="NVUE-CLI/#get-the-hash-for-a-file" text="Command to get the hash for a file">}}
  - {{<link url="802.1X-Interfaces/#configure-8021x-interfaces" text="Commands to set the NAS IP address and NAS identifier for 802.1X">}}
  - {{<link url="System-Power/#power-cycle" text="Command to power cycle the switch">}}
  - {{<link url="SSH-for-Remote-Access/#certificate-based-authentication" text="SSH certificate-based authentication">}}
  - Additional FRR filters
  - {{< expand "Changed NVUE Commands" >}}
| Cumulus Linux 5.13 | Cumulus Linux 12 and Earlier |
| --------------- |---------------------------------------|
| `nv set maintenance unit all-protocols state maintenance`| `nv action enable system maintenance mode` |
| `nv set maintenance unit all-protocols state production` | `nv action disable system maintenance mode` |
| `nv set maintenance unit all-interfaces state maintenance` | `nv action enable system maintenance ports` |
| `nv set maintenance unit all-interfaces state production` | `nv action disable system maintenance ports` |
| `nv set system lldp` | `nv set service lldp` |
| `nv show system lldp` | `nv show service lldp` |
| `nv set system syslog server <server-id>` | `nv set service syslog <vrf> server <server-id>`|
| `nv set system syslog server <server-id> port <port>` | `nv set service syslog <vrf> server <server-id> port <port>`|
| `nv set system syslog server <server-id> protocol <protocol>` | `nv set service syslog <vrf> server <server-id> protocol <protocol>`|
| `nv show system`| `build` and `product-release` fields removed from output. |
| `nv show system version`| Updated and new fields in output.|

{{< /expand >}}
  - {{< expand "Removed NVUE Commands" >}}
```
nv action enable system maintenance mode
nv action enable system maintenance ports
nv action disable system maintenance mode
nv action disable system maintenance ports
nv show platform software
nv show system maintenace
```
{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show maintenance unit all-protocols
nv show system docker
nv show system docker container
nv show system docker container stats
nv show system docker container <container-id-name> stats
nv show system docker engine
nv show system docker image
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
nv show system ssh-server trusted-ca-keys
nv show system syslog
nv show system syslog format
nv show system syslog server
nv show system syslog server <server-id>
nv show system syslog selector <selector-id>
nv show system syslog selector <selector-id> filter
nv show system syslog selector <selector-id> filter <filter-id>
nv show system version
nv show system version image
nv show system version packages installed
nv show system version packages installed <package_name>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set maintenance unit all-interfaces state maintenance
nv set maintenance unit all-interfaces state production
nv set maintenance unit all-protocols state maintenance
nv set maintenance unit all-protocols state production
nv set service dhcp-server <vrf> static <host> vendor-class
nv set system aaa radius require-message-authenticator
nv set system aaa radius server <server-id> vrf <vrf-id>
nv set system aaa user <user> ssh cert-auth state
nv set system aaa user <user> ssh cert-auth principals <principal>
nv set system docker vrf <vrf-name>
nv set system dot1x radius nas-identifier
nv set system dot1x radius nas-ip-address
nv set system dot1x reauth-timeout-ignore
nv set system gnmi-server listening-address <listening-address-id>
nv set system gnmi-server mtls ca-certificate <value>
nv set system gnmi-server mtls crl <value>
nv set system gnmi-server state
nv set system gnmi-server certificate self-signed
nv set system gnmi-server port
nv set system grpc-tunnel server <server-name-id> target-type gnmi-gnoi
nv set system grpc-tunnel server <server-name-id>
nv set system grpc-tunnel server <server-name-id> state
nv set system grpc-tunnel server <server-name-id> target-name 
nv set system grpc-tunnel server <server-name-id> address
nv set system grpc-tunnel server <server-name-id> port
nv set system grpc-tunnel server <server-name-id> certificate self-signed
nv set system grpc-tunnel server <server-name-id> ca-certificate
nv set system grpc-tunnel server <server-name-id> target-type gnmi-gnoi
nv set system grpc-tunnel server <server-name-id> retry-interval
nv set system ssh-server trusted-ca-keys <key-id> key <key-literal>
nv set system ssh-server trusted-ca-keys <key-id> type <key-type>
nv set system syslog format welf
nv set system syslog format welf firewall-name
nv set system syslog selector
nv set system syslog selector facility
nv set system syslog selector <selector-id> program-name
nv set system syslog selector <selector-id> severity
nv set system syslog selector <selector-id> filter <filter-id> action
nv set system syslog selector <selector-id> filter <filter-id> match
nv set system syslog severity
nv set system syslog server <server-id>
nv set system syslog server <server-id> port
nv set system syslog server <server-id> protocol
nv set system syslog server <server-id> vrf mgmt
nv set system telemetry histogram temporality <mode>
nv set system telemetry adaptive-routing-stats sample-interval
nv set system telemetry adaptive-routing-stats export state
nv set system telemetry lldp export state
nv set system telemetry lldp sample-interval
nv set system telemetry platform-stats class transceiver-info sample-interval
nv set system telemetry platform-stats class transceiver-info state
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset maintenance unit all-intefaces state
nv unset maintenance unit all-protocols state
nv unset maintenance unit system-protocols state
nv unset service dhcp-server <vrf> static <host>> vendor-class
nv unset system aaa user <user> ssh cert-auth state
nv unset system aaa user <user> ssh cert-auth principals
nv unset system aaa radius require-message-authenticator
nv unset system aaa radius server <server-id> vrf
nv unset system docker vrf
nv unset system dot1x radius nas-identifier
nv unset system dot1x radius nas-ip-address
nv unset system dot1x reauth-timeout-ignore
nv unset system gnmi-server
nv unset system gnmi-server listening-address
nv unset system gnmi-server listening-address <listening-address-id>
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
nv unset system ssh-server trusted-ca-keys <key-id> key
nv unset system ssh-server trusted-ca-keys <key-id> type
nv unset system syslog format welf
nv unset system syslog format welf firewall-name
nv unset system syslog selector
nv unset system syslog selector facility
nv unset system syslog selector <selector-id> program-name
nv unset system syslog selector <selector-id> severity
nv unset system syslog selector <selector-id> filter <filter-id> action
nv unset system syslog selector <selector-id> filter <filter-id> match
nv unset system syslog severity
nv unset system syslog server <server-id>
nv unset system syslog server <server-id> port
nv unset system syslog server <server-id> protocol
nv unset system syslog server <server-id> vrf mgmt
nv unset system telemetry histogram temporality <mode>
nv unset system telemetry adaptive-routing-stats sample-interval
nv unset system telemetry adaptive-routing-stats export state
nv unset system telemetry lldp export state
nv unset system telemetry lldp sample-interval
nv unset system telemetry platform-stats class transceiver-info sample-interval
nv unset system telemetry platform-stats class transceiver-info state
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action erase system disk 
nv action generate file-hash md5 <filename>
nv action generate file-hash sha1 <filename>
nv action generate file-hash sha224 <filename>
nv action generate file-hash sha256 <filename>
nv action generate file-hash sha512 <filename>
nv action list system file-path <path>
nv action power-cycle system
nv action pull system docker image <image-id>
nv action remove system docker image <image-id>
nv action remove system docker container <container-id>
nv action start system docker container <container-name> image <image-id>
nv action stop system docker container <container-name>
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.13.

### Linux Configuration Files Overwritten

{{%notice warning%}}
If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.13 or later.
{{%/notice%}}

Cumulus Linux includes a default NVUE `startup.yaml` file. In addition, NVUE configuration auto save is enabled by default. As a result, Cumulus Linux overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur and no action is needed.
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
