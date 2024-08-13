---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.10 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.10, see the {{<link title="Cumulus Linux 5.10 Release Notes" text="Cumulus Linux 5.10 Release Notes">}}.
- To upgrade to Cumulus Linux 5.10, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->

## What's New in Cumulus Linux 5.10

### Platforms

NVIDIA SN5400 (400G Spectrum-4)

{{%notice note%}}
{{<link url="Precision-Time-Protocol-PTP" text="PTP">}} and {{<link url="Pulse-Per-Second-PPS" text="PPS">}} on the NVIDIA SN5400 switch are in BETA.
{{%/notice%}}

### New Features and Enhancements

- {{<link url="ASIC-Monitoring/#high-frequency-telemetry" text="High frequency telemetry">}}
- {{<link url="Open-Telemetry-Export" text="Telemetry export with OTLP">}} on Spectrum-4 switches (BETA)
- {{<link url="SSH-for-Remote-Access/#ssh-login-notifications" text="SSH login notifications">}}
- {{<link url="Quality-of-Service/#lossy-headroom" text="QoS lossy headroom configuration">}} and {{<link url="Quality-of-Service/#ingress-and-egress-management-buffers" text=" QoS Ingress and Egress Management Buffer Configuration">}}
- {{<link url="VXLAN-Devices/#reserved-field-in-vxlan-header" text="Ignore reserved field in VXLAN header">}}
- {{<link url="Quick-Start-Guide/#get-started" text="DHCP Option 61">}} (pre-provision a switch with its serial number) is enabled by default when Cumulus Linux boots
- {{<link url="Optional-BGP-Configuration/#graceful-bgp-shutdown-on-a-peer" text="Graceful shutdown on a peer">}}
- {{<link url="Synchronous-Ethernet-SyncE/#minimum-acceptable-quality-level" text="SyncE minimum acceptable quality level option">}}
- {{< expand "Additional OID support for SNMP MIBs" >}}
| <div style="width:250px">MIB | OID | Description |
| --- | ----| ----------- |
| CUMULUS-COUNTERS-MIB | .1.3.6.1.4.1.40310.2.2.5.1.4<br>clCarrierChangesCount | The number of times the operational status of the interface link transitions between up and down. |
| CUMULUS-COUNTERS-MIB | .1.3.6.1.4.1.40310.2.2.6.1.4<br>clIntOutBytes | The number of bytes transmitted from the egress queue. |
| CUMULUS-RESOURCE-QUERY-MIB | .1.3.6.1.4.1.40310.1.1.28<br>l3RoutingTableCurrentIpv4Entries | The total number of IPv4 routes in the FIB.|
| CUMULUS-RESOURCE-QUERY-MIB | .1.3.6.1.4.1.40310.1.1.29<br>l3RoutingTableCurrentIpv4EntriesForPrefixLen24 | The total number of IPv4/24 routes in the FIB.|
| CUMULUS-RESOURCE-QUERY-MIB | .1.3.6.1.4.1.40310.1.1.30<br>l3RoutingTableCurrentIpv4EntriesForPrefixLen32 | The total number of IPv4/32 routes in the FIB.|

{{<link url="Supported-MIBs" text="Supported MIBs">}}
{{< /expand >}}
- NVUE
  - {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#amber-phy-health-management" text="AmBER PHY counters">}}
  - {{<link url="Interface-Configuration-and-Management/#interface-mac-addresses" text="Interface MAC address configuration">}}
  - {{<link url="Understanding-the-cl-support-Output-File/#manual-cl-support-file" text="Commands to generate and delete a cl-support file">}}
  - {{<link url="NVUE-CLI/#session-based-authentication" text="Session-based authentication">}}
  - Redesigned {{<link url="Troubleshooting-BGP/#show-bgp-route-information" text="BGP show output flags">}} now similar to vtysh output
  - {{<link url="NVUE-CLI/#encrypted-passwords" text="NVUE encrypts passwords by default">}} in the NVUE `startup.yaml` file
  - {{< expand "Changed NVUE Commands" >}}
| New Command| Previous Command |
| ----------- | ----------------|
| `nv set system config auto-save state enabled`<br>`nv set system config auto-save state disabled` | `nv set system config auto-save enable on`<br>`nv set system config auto-save enable off`|
| `nv set system telemetry` commands | `nv set service telemetry` commands|
| `nv show system telemetry` commands | `nv show service telemetry` commands |
| `nv show system time` | `nv show system date-time` |
| `nv action change system time`| `nv action change system date-time`|
| `nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group service7` | `nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group control` |

These commands include additional information in the output.

| Changed Command Output | Additional Information |
| ----------- | ----------------|
| `nv show interface <interface> link` | Port hardware information such as eyes, grade and troubleshooting information, if available. |
| `nv show interface <interface> pluggable` | Cable length, date code, revision compliance, temperature, and voltage. |

The minimum and maximum values for the `nv set system forwarding ecmp-weight-normalisation max-hw-weight` command have changed.

| New Values | Previous Values |
| ----------- | ----------------|
| minimum: 8<br> maximum: 4096 | minimum: 10<br> maximum: 255|

{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show interface <interface> link phy-detail 
nv show interface <interface> link phy-diag
nv show qos advance-buffer-config <profile-id> egress-mgmt-buffer 
nv show qos advance-buffer-config <profile-id> ingress-mgmt-buffer
nv show system health
nv show system security encryption
nv show system security encryption db
nv show system tech-support
nv show system tech-support files
nv show system telemetry
nv show system telemetry export
nv show system telemetry export otlp gRPC
nv show system telemetry export otlp gRPC destination
nv show system telemetry export otlp grpc destination <destination-id>
nv show system telemetry hft
nv show system telemetry hft job
nv show system telemetry hft job <hft-job-id>
nv show system telemetry hft profile
nv show system telemetry hft profile <profile-id>
nv show system telemetry hft profile <profile-id> counter
nv show system telemetry hft profile <profile-id> traffic-class
nv show system telemetry hft target
nv show system telemetry interface-stats
nv show system telemetry interface-stats egress-buffer
nv show system telemetry interface-stats export
nv show system telemetry interface-stats ingress-buffer
nv show system version
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface> link mac-address
nv set system security encryption db state
nv set system ssh-server login-record-period
nv set system synce min-acceptable-ql
nv set system telemetry export otlp grpc cert-id <certificate>
nv set system telemetry export otlp grpc destination <destination> port <port>
nv set system telemetry export otlp grpc insecure
nv set system telemetry export otlp state
nv set system telemetry hft profile <profile-id> counter
nv set system telemetry hft profile <profile-id> sample-interval
nv set system telemetry hft profile <profile-id> traffic-class
nv set system telemetry hft target local
nv set system telemetry histogram export state
nv set system telemetry interface-stats egress-buffer traffic-class
nv set system telemetry interface-stats export state
nv set system telemetry interface-stats ingress-buffer priority-group
nv set system telemetry interface-stats sample-interval
nv set qos advance-buffer-config <profile-id> egress-mgmt-buffer
nv set qos advance-buffer-config <profile-id> egress-mgmt-buffer reserved
nv set qos advance-buffer-config <profile-id> egress-mgmt-buffer service-pool
nv set qos advance-buffer-config <profile-id> egress-mgmt-buffer shared-alpha
nv set qos advance-buffer-config <profile-id> egress-mgmt-buffer shared-bytes
nv set qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group> headroom
nv set qos advance-buffer-config <profile-id> ingress-mgmt-buffer
nv set qos advance-buffer-config <profile-id> ingress-mgmt-buffer headroom
nv set qos advance-buffer-config <profile-id> ingress-mgmt-buffer reserved
nv set qos advance-buffer-config <profile-id> ingress-mgmt-buffer service-pool
nv set qos advance-buffer-config <profile-id> ingress-mgmt-buffer shared-alpha
nv set qos advance-buffer-config <profile-id> ingress-mgmt-buffer shared-bytes
nv set vrf <vrf>> router bgp neighbor <neighbor-id>> graceful-shutdown
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset interface <interface> link mac-address
nv unset system security encryption db state
nv unset system telemetry export otlp grpc cert-id
nv unset system telemetry export otlp grpc destination
nv unset system telemetry export otlp grpc insecure
nv unset system telemetry export otlp state
nv unset system telemetry hft
nv unset system telemetry hft profile <profile-id>
nv unset system telemetry hft profile <profile-id> counter
nv unset system telemetry hft profile <profile-id> sample-interval
nv unset system telemetry hft profile <profile-id> traffic-class
nv unset system telemetry hft target
nv unset system telemetry hft target local
nv unset system telemetry histogram export state
nv unset system telemetry interface-stats
nv unset system telemetry interface-stats export
nv unset system telemetry interface-stats export state
nv unset system telemetry interface-stats ingress-buffer
nv unset system telemetry interface-stats egress-buffer
nv unset system telemetry interface-stats sample-interval
nv unset system ssh-server login-record-period
nv unset qos advance-buffer-config <profile-id> egress-mgmt-buffer
nv unset qos advance-buffer-config <profile-id> egress-mgmt-buffer reserved
nv unset qos advance-buffer-config <profile-id> egress-mgmt-buffer service-pool
nv unset qos advance-buffer-config <profile-id> egress-mgmt-buffer shared-alpha
nv unset qos advance-buffer-config <profile-id> egress-mgmt-buffer shared-bytes
nv unset qos advance-buffer-config <profile-id> ingress-lossy-buffer priority-group <priority-group> headroom
nv unset qos advance-buffer-config <profile-id> ingress-mgmt-buffer
nv unset qos advance-buffer-config <profile-id> ingress-mgmt-buffer headroom
nv unset qos advance-buffer-config <profile-id> ingress-mgmt-buffer reserved
nv unset qos advance-buffer-config <profile-id> ingress-mgmt-buffer service-pool
nv unset qos advance-buffer-config <profile-id> ingress-mgmt-buffer shared-alpha
nv unset qos advance-buffer-config <profile-id> ingress-mgmt-buffer shared-bytes
nv unset vrf <vrf>> router bgp neighbor <neighbor-id>> graceful-shutdown
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action cancel system telemetry hft job
nv action clear system api session user
nv action clear vrf <vrf> router ospf database
nv action delete system tech-support files <file-name>
nv action generate system tech-support
nv action rotate system log
nv action schedule system telemetry hft job
nv action upload system tech-support files <file-name> <remote-url-upload>
nv action upload system telemetry hft job <hft-job-id> <remote-url-upload>
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

## Release Considerations

Cumulus Linux 5.10 includes the NVUE object model. After you upgrade to Cumulus Linux 5.10, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
