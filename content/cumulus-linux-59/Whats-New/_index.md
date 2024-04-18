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
- {{<link url="/Link-Layer-Discovery-Protocol/#application-priority-tlvs" text="LLDP application priority TLV">}} transmission
- {{<link url="Firewall-Rules" text="Firewall rules">}}
- {{<link url="CLI-Configuration" text="CLI Session pagination and timeout options">}}
- {{<link url="User-Accounts/#password-security" text="Password security commands">}}
- {{<link url="Switch-Port-Attributes/#set-the-number-of-lanes-per-split-port" text="4x breakout on QSFP-DD/OSFP 8 lane ports">}} now allocates two lanes per port by default instead of one
- {{<link url="Interface-Configuration-and-Management/#bring-an-interface-up-or-down" text="New Linux ifreload -a --diff option">}} processes and applies only incremental changes instead of reloading entire configuration
- NVUE
  - {{<link url="In-Service-System-Upgrade-ISSU/#upgrade-mode" text="ISSU upgrade mode">}} and {{<link url="Upgrading-Cumulus-Linux/#upgrade-the-switch" text="package upgrade">}} commands
  - {{<link url="NVUE-CLI/#monitoring-commands" text="New nv show --output raw option">}} shows native vtysh (FRR) output
  - {{<link url="Interface-Configuration-and-Management/#troubleshooting" text="nv show interface <interface> command output">}} shows both the admin and physical state of an interface
  - NVUE ships with a default `/etc/nvue.d/startup.yaml` file
  - BGP now shows paths in a sorted order with the best path always first
  - {{< expand "Redesigned nv show platform commands" >}}
{{%notice info%}}
The NVUE `nv show platform` commands have changed. If you are using automation, be sure to update your automation scripts.
{{%/notice%}}
{{< tabs "TabID34 ">}}
{{< tab "5.9 commands ">}}

```
cumulus@leaf01:mgmt:~$ nv show platform <<TAB>>
capabilities      environment       firmware          inventory         pulse-per-second  software
```

| Command | Description |
|--------------------|------------------|
| `nv show platform` | Shows platform hardware information on the switch, such as the model and manufacturer, memory, Cumulus Linux release, serial number and system MAC address. |
| `nv show platform capabilities` | Shows the switch platform capabilities.|
| `nv show platform environment` | Shows information about the sensors, fans, LEDs, and PSUs on the switch.|
| `nv show platform firmware` | Shows information about the switch firmware.|
| `nv show platform inventory` | Shows the switch inventory, which includes fan and PSU hardware version, model, serial number, state, and type. |
| `nv show platform pulse-per-second` | Shows a summary of the PPS In and PPS out configuration settings.|
| `nv show platform software` | Shows the software installed on the switch.|

{{< /tab >}}
{{< tab "5.8 and earlier">}}

```
cumulus@leaf01:mgmt:~$ nv show platform <<TAB>>
capabilities      hardware          software
environment       pulse-per-second
```

| Command | Description |
|--------------------|------------------|
| `nv show platform` | Shows the software installed on the switch. |
| `nv show platform capabilities` | Shows the switch platform capabilities.|
| `nv show platform environment` | Shows a list of sensors, fans, LEDs, and PSUs on the switch.|
| `nv show platform hardware` | Shows information about the switch hardware, such as the model and manufacturer, memory, Cumulus Linux release, serial number and system MAC address.|
| `nv show platform pulse-per-second` | Shows a summary of the PPS In and PPS out configuration settings.|
| `nv show platform software` | Shows the software installed on the switch and includes version numbers. |

{{< /tab >}}
{{< /tabs >}}
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
nv show system cli
nv show system cli pagination
nv show system reboot required
nv show system security password-hardening
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
nv set system cli pagination
nv set system cli pagination state
nv set system cli pagination pager
nv set system cli inactive-timeout
nv set system control-plane acl acl-default-dos inbound
nv set system control-plane acl acl-default-whitelist inbound
nv set system security password-hardening digits-class
nv set system security password-hardening expiration
nv set system security password-hardening expiration-warning
nv set system security password-hardening history-cnt
nv set system security password-hardening len-min
nv set system security password-hardening lower-class
nv set system security password-hardening reject-user-passw-match
nv set system security password-hardening special-class
nv set system security password-hardening state
nv set system security password-hardening upper-class
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
nv unset system security password-hardening
nv unset system security password-hardening digits-class
nv unset system security password-hardening expiration
nv unset system security password-hardening expiration-warning
nv unset system security password-hardening history-cnt
nv unset system security password-hardening len-min
nv unset system security password-hardening lower-class
nv unset system security password-hardening reject-user-passw-match
nv unset system security password-hardening special-class
nv unset system security password-hardening state
nv unset system security password-hardening upper-class
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action upgrade system packages to latest use-vrf <vrf> dry-run
nv action upgrade system packages to latest use-vrf <vrf>
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
