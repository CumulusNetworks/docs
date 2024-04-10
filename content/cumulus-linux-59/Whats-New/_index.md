---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.9 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.9, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.9, see the {{<link title="Cumulus Linux 5.9 Release Notes" text="Cumulus Linux 5.9 Release Notes">}}.
- To upgrade to Cumulus Linux 5.9, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.9.0
<!-- vale on -->
Cumulus Linux 5.9.0 contains several new features and improvements, and provides bug fixes.

### New Features and Enhancements

- Cumulus Linux upgrade to Debian 12 (bookworm)
- {{<link url="ASIC-Monitoring" text="Latency histogram">}} for ASIC monitoring
- {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Warmboot support for VXLAN EVPN">}} is now generally available
- {{<link url="Link-Layer-Discovery-Protocol/#transmit-application-priority-tlvs" text="LLDP application priority TLV">}} transmission
- {{<link url="Firewall-Rules" text="Firewall rules">}}
- {{<link url="CLI-Configuration" text="CLI Session pagination and timeout options">}}
- {{<link url="User-Accounts/#epassword-security" text="Password security commands">}}
- {{<link url="Switch-Port-Attributes/#set-the-number-of-lanes-per-split-port" text="4x breakout on QSFP-DD/OSFP 8 lane ports">}} now allocates two lanes per port by default instead of one.
- NVUE
  - {{<link url="In-Service-System-Upgrade-ISSU/#upgrade-mode" text="ISSU upgrade mode">}} and {{<link url="Upgrading-Cumulus-Linux/#upgrade-the-switch" text="package upgrade">}} commands
  - `nv show` commands support {{<link url="NVUE-CLI/#monitoring-commands" text="native vtysh (FRR) output">}}
  - `nv show interface` command output now includes the admin state of an interface in addition to the physical state.
  - `nv show platform` command redesign
  - {{< expand "Improved tab completion for NVUE routing commands" >}}
```
```
{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
  
{{< tabs "TabID49 ">}}
{{< tab "nv show ">}}

```
nv show interface <interface-id> telemetry histogram latency
nv show interface <interface-id> telemetry histogram latency traffic-class
nv show interface <interface-id> telemetry histogram latency traffic-class <if-tc-id>
nv show interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold
nv show interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> snapshot
nv show interface <interface> lldp application-tlv
nv show interface <interface> lldp application-tlv app
nv show interface <interface> lldp application-tlv tcp-port
nv show interface <interface> lldp application-tlv udp-port
nv show service lldp application-tlv app
nv show service lldp application-tlv tcp-port
nv show service lldp application-tlv udp-port
nv show service telemetry histogram latency
nv show system reboot required
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface> lldp application-tlv app <application> 
nv set interface <interface> lldp application-tlv tcp-port <port>
nv set interface <interface> lldp application-tlv udp-port <port>
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id>
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold action log
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold value
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> bin-min-boundary
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> histogram-size
nv set service lldp application-tlv app <application> priority <priority> 
nv set service lldp application-tlv tcp-port <port> priority <priority> 
nv set service lldp application-tlv udp-port <port> priority <priority> 
nv set service telemetry histogram latency bin-min-boundary
nv set service telemetry histogram latency histogram-size
nv set system cli pagination state
nv set system cli pagination pager
nv set system cli inactive-timeout
nv set system control-plane acl acl-default-dos inbound
nv set system control-plane acl acl-default-whitelist inbound
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset interface <interface> lldp application-tlv app <application> 
nv unset interface <interface> lldp application-tlv tcp-port <port>
nv unset interface <interface> lldp application-tlv udp-port <port> 
nv unset interface <interface-id> telemetry histogram latency
nv unset interface <interface-id> telemetry histogram latency traffic-class
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id>
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold action
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold value
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> bin-min-boundary
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> histogram-size
nv unset service lldp application-tlv app <application> priority <priority> 
nv unset service lldp application-tlv tcp-port <port> priority <priority> 
nv unset service lldp application-tlv udp-port <port> priority <priority> 
nv unset service telemetry histogram latency
nv unset service telemetry histogram latency bin-min-boundary
nv unset service telemetry histogram latency histogram-size
nv unset system cli pagination state
nv unset system cli pagination pager
nv unset system cli inactive-timeout
nv unset system control-plane acl acl-default-dos
nv unset system control-plane acl acl-default-whitelist
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action upgrade system packages to <version> dry-run
nv action upgrade system packages to <version>
```

{{< /tab >}}
{{< /tabs >}}
  
{{< /expand >}}

{{%notice note%}}
The repository key stored in Cumulus Linux 5.5.0 and earlier has expired. Before performing a package upgrade to Cumulus Linux 5.9.0 from Cumulus Linux 5.5.0 and earlier, you must install the new key. See [this knowledge base article]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Update-Expired-GPG-Keys" >}}).
{{%/notice%}}

{{%notice info%}}
Cumulus Linux 5.9 includes the NVUE object model. After you upgrade to Cumulus Linux 5.9, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
