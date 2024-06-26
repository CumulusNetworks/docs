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
- Additional OID support for SNMP MIBs
- High frequency telemetry
- {{<link url="SSH-for-Remote-Access/#ssh-login-notifications" text="SSH login notifications">}}
- {{<link url="Quality-of-Service/#lossy-headroom" text="QoS lossy headroom configuration">}}
- {{<link url="VXLAN-Devices/#reserved-field-in-vxlan-header" text="Ignore reserved field in VXLAN header">}}
- {{<link url="Quick-Start-Guide/#get-started" text="DHCP Option 61">}} (pre-provision a switch with its serial number) is enabled by default when Cumulus Linux boots
- {{<link url="Optional-BGP-Configuration/#graceful-bgp-shutdown-on-a-peer" text="Graceful shutdown on a peer">}}
- NVUE
  - AmBER counters and gauges
  - {{<link url="LDAP-Authentication-and-Authorization" text="LDAP authentication and encryption configuration">}}
  - {{<link url="Interface-Configuration-and-Management/#interface-mac-addresses" text="Interface MAC address configuration">}}
  - Redesigned BGP show output flags to be similar to vtysh output
  - Radius keys are encrypted in the NVUE `startup.yaml` file
  - {{< expand "Changed NVUE Commands" >}}
| New Command| Previous Command |
| ----------- | ----------------|
| `nv set system config auto-save state enabled`<br>`nv set system config auto-save state disabled` | `nv set system config auto-save enable on`<br>`nv set system config auto-save enable off`|
{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show qos advance-buffer-config default-global egress-mgmt-buffer 
nv show qos advance-buffer-config default-global ingress-mgmt-buffer
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface> link mac-address <mac-address>
nv set system ssh-server login-record-period
nv set qos advance-buffer-config default-global egress-mgmt-buffer 
nv set qos advance-buffer-config default-global ingress-mgmt-buffer
nv set qos advance-buffer-config default-global ingress-lossy-buffer priority-group <priority-group> headroom
<bytes>
nv set vrf default router bgp neighbor swp51 graceful-shutdown on|off
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset interface <interface> link mac-address <mac-address>
nv unset vrf default router bgp neighbor swp51 graceful-shutdown
```

{{< /tab >}}
{{< tab "nv action ">}}

```

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
