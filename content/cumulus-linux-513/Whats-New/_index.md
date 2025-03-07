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
- {{<link url="System-Power/#power-cycle" text="Recovery mechanism for thermal ASIC shutdown">}}
- Erase SSD before switch RMA
- OTLP Phase 4
- gNMI support
- Default AR profile update
- New maintenance mode commands
- Export per transceiver temperature and power
- Filters for RSYSLOG log per facility level
- 802.1x on router ports with dynamic VRF assignments
- Ability to disconnect or disable remote access to the switch
- Enable RADIUS for multiple VRFs
- Support Docker container
- Show SNR for transceivers
- Reflect switch hardware revision
- Enable ssh public key only
- OTLP
  - Device level configuration of histogram
  - Buffer Occupancy and watermark metrics
- gNMI support
- NVUE
  - {{<link url="NVUE-CLI/#list-directory-contents" text="Command to list directory contents">}}
  - {{<link url="NVUE-CLI/#get-the-hash-for-a-file" text="Command to get the hash for a file">}}
  - {{<link url="802.1X-Interfaces/#configure-8021x-interfaces" text="Commands to set the NAS IP address and NAS identifier for 802.1X">}}
  - Enable CRL support
  - SSH certificate-based authorization
  - Additional FRR filters
  - {{< expand "Changed NVUE Commands" >}}
| Cumulus Linux 5.13 | Cumulus Linux 12 and Earlier |
| --------------- |---------------------------------------|
| `nv set maintenance unit all-protocols state maintenance`| `nv action enable system maintenance mode`<br>`nv action disable system maintenance mode` |
| | `nv action enable system maintenance ports`<br>`nv action disable system maintenance ports` |
{{< /expand >}}
  - {{< expand "Removed NVUE Commands" >}}
```
nv action enable system maintenance mode
nv action enable system maintenance ports
nv action disable system maintenance mode
nv action disable system maintenance ports
nv show system maintenace
```
{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```

```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set service dhcp-server <vrf> static <host>> vendor-class
nv set system dot1x radius nas-identifier
nv set system dot1x radius nas-ip-address
nv set system dot1x reauth-timeout-ignore
```

{{< /tab >}}
{{< tab "nv unset ">}}

```

```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action generate file-hash md5 <filename>
nv action generate file-hash sha1 <filename>
nv action generate file-hash sha224 <filename>
nv action generate file-hash sha256 <filename>
nv action generate file-hash sha512 <filename>
nv action list system file-path <path>
nv action power-cycle system
```

{{< /tab >}}
{{< tab "nv config ">}}

```

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
