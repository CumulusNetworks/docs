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

- PPS supported on the NVIDIA SN5400 switch
- Additional SNMP MIBs
- High frequency telemetry
- {{<link url="SSH-for-Remote-Access/#ssh-login-notifications" text="SSH login notifications">}}
- Lossy headroom configuration
- Allow reserved field in VXLAN header
- DHCP Option 61 on by default when Cumulus Linux boots
- Graceful shutdown for a peer
- NVUE
  - AmBER counters and gauges
  - {{<link url="Interface-Configuration-and-Management/#interface-mac-addresses" text="Interface MAC address configuration">}}
  - Redesigned BGP show output flags to be similar to vtysh output
  - EVPN show output updates
  - LDAP authentication and encryption configuration
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```

```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface> link mac-address <mac-address>
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset interface <interface> link mac-address <mac-address>
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
