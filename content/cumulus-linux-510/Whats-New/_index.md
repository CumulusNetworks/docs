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

### New Features and Enhancements

- PPS supported on the NVIDIA SN5400 switch
- {{<link url="ASIC-Monitoring/#high-frequency-telemetry" text="High frequency telemetry">}}
- Telemetry export with Prometheus and OTLP (SN5600 switch only)
- {{<link url="SSH-for-Remote-Access/#ssh-login-notifications" text="SSH login notifications">}}
- {{<link url="Quality-of-Service/#lossy-headroom" text="QoS lossy headroom configuration">}} and {{<link url="Quality-of-Service/#ingress-and-egress-management-buffers" text=" QoS Ingress and Egress Management Buffer Configuration">}}
- {{<link url="VXLAN-Devices/#reserved-field-in-vxlan-header" text="Ignore reserved field in VXLAN header">}}
- {{<link url="Quick-Start-Guide/#get-started" text="DHCP Option 61">}} (pre-provision a switch with its serial number) is enabled by default when Cumulus Linux boots
- {{<link url="Optional-BGP-Configuration/#graceful-bgp-shutdown-on-a-peer" text="Graceful shutdown on a peer">}}
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
  - {{<link url="LDAP-Authentication-and-Authorization" text="LDAP authentication">}}
  - {{<link url="Interface-Configuration-and-Management/#interface-mac-addresses" text="Interface MAC address configuration">}}
  - {{<link url="Understanding-the-cl-support-Output-File/#manual-cl-support-file" text="Command to generate a cl-support file">}}
  - {{<link url="NVUE-CLI/#session-based-authentication" text="Session-based authentication">}}
  - Redesigned BGP show output flags similar to vtysh output
  - Radius keys are encrypted in the NVUE `startup.yaml` file
  - {{< expand "Changed NVUE Commands" >}}
| New Command| Previous Command |
| ----------- | ----------------|
| `nv set system config auto-save state enabled`<br>`nv set system config auto-save state disabled` | `nv set system config auto-save enable on`<br>`nv set system config auto-save enable off`|

These commands include additional information in the output.

| Changed Command Output | Additional Information |
| ----------- | ----------------|
| `nv show interface <interface>` |  Port hardware information such as eyes, grade and troubleshooting information, if available.|
| `nv show interface <interface> link` | Port hardware information such as eyes, grade and troubleshooting information, if available. |
| `nv show interface <interface> pluggable` | Cable length, date code, revision compliance, temperature, and voltage. |

{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show interface <interface> link phy-detail 
nv show interface <interface> link phy-diag
nv show qos advance-buffer-config default-global egress-mgmt-buffer 
nv show qos advance-buffer-config default-global ingress-mgmt-buffer
nv show service telemetry hft job
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface> link mac-address
nv set system telemetry hft profile <profile> counter
nv set system telemetry hft profile <profile> sample-interval
nv set system telemetry hft profile <profile> traffic-class
nv set system telemetry hft target local
nv set system telemetry hft target influxdb bucket
nv set system telemetry hft target influxdb host
nv set system telemetry hft target influxdb org
nv set system telemetry hft target influxdb port
nv set system telemetry hft target influxdb token
nv set system ssh-server login-record-period
nv set qos advance-buffer-config default-global egress-mgmt-buffer 
nv set qos advance-buffer-config default-global ingress-mgmt-buffer
nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group <priority-group> headroom
nv set vrf <vrf>> router bgp neighbor <neighbor-id>> graceful-shutdown
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset interface <interface> link mac-address
nv unset system telemetry hft profile <profile>
nv unset system telemetry hft profile <profile> counter
nv unset system telemetry hft profile <profile> sample-interval
nv unset system telemetry hft profile <profile> traffic-class
nv unset system telemetry hft target local
nv unset system telemetry hft target influxdb
nv unset system telemetry hft target influxdb bucket
nv unset system telemetry hft target influxdb host
nv unset system telemetry hft target influxdb org
nv unset system telemetry hft target influxdb port
nv unset system telemetry hft target influxdb token
nv unset system ssh-server login-record-period
nv unset qos advance-buffer-config default-global egress-mgmt-buffer 
nv unset qos advance-buffer-config default-global ingress-mgmt-buffer
nv unset qos advance-buffer-config default-global ingress-lossy-buffer priority-group <priority-group> headroom
nv unset vrf <vrf>> router bgp neighbor <neighbor-id>> graceful-shutdown
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action cancel service telemetry hft job
nv action clear system api session user
nv action generate system tech-support
nv action schedule service telemetry hft job
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
