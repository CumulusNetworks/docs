---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.9 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.9, see the {{<link title="Cumulus Linux 5.9 Release Notes" text="Cumulus Linux 5.9 Release Notes">}}.
- To upgrade to Cumulus Linux 5.9, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.9.0
<!-- vale on -->

Cumulus Linux 5.9 is an Extended-Support Release (ESR). For more information, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/knowledge-base/Support/Support-Offerings/Cumulus-Linux-Release-Versioning-and-Support-Policy" text="this Knowledge base article">}}.

{{%notice info%}}
- Due to a critical issue, NVIDIA does not recommend that you install Cumulus Linux 5.9 on a switch with the Spectrum-4 ASIC. For more information, contact Technical Support.
- You can only upgrade to Cumulus 5.9 from a previous release by installing the binary image; package upgrade is not supported.
- Cumulus Linux 5.9 provides a set of default firewall rules that allows only specific IP addresses and ports, and drops packets that are disallowed. Be sure to review the {{<link url="Firewall-Rules" text="firewall rules">}} before upgrading.
{{%/notice%}}

Cumulus Linux 5.9.0 contains several new features and improvements, and provides bug fixes.

### New Features and Enhancements
- Cumulus Linux upgrade to Debian 12 (bookworm)
- All systems that ship with SSD include a 32 GB or larger secondary partition for future use
- {{<link url="ASIC-Monitoring" text="Latency histogram">}} for ASIC monitoring
- {{<link url="/Link-Layer-Discovery-Protocol/#application-priority-tlvs" text="LLDP application priority TLV">}} transmission
- {{<link url="Firewall-Rules" text="Firewall rules">}}
- {{<link url="CLI-Configuration" text="CLI Session pagination and timeout options">}}
- {{<link url="User-Accounts/#password-security" text="Password security commands">}}
- {{<link url="SSH-for-Remote-Access/#ssh-strict-mode" text="SSH strict mode">}}
- {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Warmboot support for VXLAN EVPN">}} is now generally available
- {{<link url="Switch-Port-Attributes/#set-the-number-of-lanes-per-split-port" text="4x breakout on QSFP-DD/OSFP 8 lane ports">}} now allocates two lanes per port by default instead of one
- {{<link url="Interface-Configuration-and-Management/#bring-an-interface-up-or-down" text="New Linux ifreload -a --diff option">}} processes and applies only incremental changes instead of reloading entire configuration
- Cumulus Linux no longer supports NCLU; all `net show` commands have been removed
- NVUE
  - {{<link url="In-Service-System-Upgrade-ISSU/#upgrade-mode" text="ISSU upgrade mode">}} and {{<link url="Upgrading-Cumulus-Linux/#upgrade-the-switch" text="package upgrade">}} commands
  - {{<link url="NVUE-CLI/#monitoring-commands" text="New nv show --output raw option">}} shows native vtysh (FRR) output
  - {{<link url="NVUE-CLI/#auto-save" text="Auto save">}} is enabled by default; when you run `nv config apply`, NVUE saves the configuration to the startup configuration file
  - NVUE ships with a {{<link url="NVUE-CLI/#default-startup-file" text="default /etc/nvue.d/startup.yaml file">}}
  {{%notice note%}}
- The default startup file sets the default hostname as cumulus; Cumulus Linux does not accept the DHCP host-name option. If you do not manage your switch with NVUE and want to change this behavior with Linux configuration files, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Hostname-Option-Received-From-DHCP-Ignored" >}}).
- The default NVUE `startup.yaml` file includes the `cumulus` user account, which is the default account for the system. Modifying the NVUE configuration to not include the `cumulus` user account, replacing the configuration or applying a startup configuration, deletes the `cumulus` account. To merge in configuration changes or to restore a backup `startup.yaml` file, use the `nv config patch` command.
{{%/notice%}}
  - {{< expand "Redesigned nv show interface commands" >}}
{{%notice info%}}
The {{<link url="Interface-Configuration-and-Management/#troubleshooting" text="nv show interface command outputs">}} have changed. If you are using automation, be sure to update your automation scripts.
{{%/notice%}}
{{< tabs "TabID49 ">}}
{{< tab "5.9 commands ">}}

`nv show interface` and `nv show interface <interface>` output shows the administrative status and the operational status of an interface

{{< /tab >}}
{{< tab "5.8 and earlier">}}

`nv show interface` and `nv show interface <interface>` output shows the NVUE configured state of an interface

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}
  - {{< expand "Redesigned nv show platform commands" >}}
{{%notice info%}}
The NVUE `nv show platform` commands have changed. If you are using automation, be sure to update your automation scripts.
{{%/notice%}}
{{< tabs "TabID62 ">}}
{{< tab "5.9 commands ">}}

```
cumulus@leaf01:mgmt:~$ nv show platform <<TAB>>
capabilities      firmware          pulse-per-second  
environment       inventory         software
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
| `nv show platform environment` | Shows information about the sensors, fans, LEDs, and PSUs on the switch.|
| `nv show platform hardware` | Shows information about the switch hardware, such as the model and manufacturer, memory, Cumulus Linux release, serial number and system MAC address.|
| `nv show platform pulse-per-second` | Shows a summary of the PPS In and PPS out configuration settings.|
| `nv show platform software` | Shows the software installed on the switch and includes version numbers. |

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show acl acl-default-dos
nv show acl acl-default-dos rule <rule>
nv show acl acl-default-whitelist
nv show acl <acl-id> rule <rule-id> match ip connection-state
nv show acl <acl-id> rule <rule-id> match ip recent-list
nv show acl <acl-id> rule <rule-id> match ip hashlimit
nv show acl <acl-id> rule <rule-id> action recent
nv show interface <interface-id> telemetry histogram latency
nv show interface <interface-id> telemetry histogram latency traffic-class
nv show interface <interface-id> telemetry histogram latency traffic-class <if-tc-id>
nv show interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold
nv show interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> snapshot
nv show interface <interface-id> link protodown-reason
nv show interface <interface> lldp application-tlv
nv show interface <interface> lldp application-tlv app
nv show interface <interface-id> lldp application-tlv app <app-id>
nv show interface <interface> lldp application-tlv tcp-port
nv show interface <interface> lldp application-tlv tcp-port <port-id>
nv show interface <interface> lldp application-tlv udp-port
nv show interface <interface> lldp application-tlv udp-port <port-id>
nv show platform environment temperature
nv show platform environment temperature <sensor-id>
nv show platform environment voltage
nv show platform environment voltage <volt-sensor-id>
nv show platform firmware
nv show platform firmware <platform-component-id>
nv show platform inventory
nv show platform inventory <inventory-id>
nv show service ptp <instance-id> ipv6-scope
nv show service lldp application-tlv
nv show service lldp application-tlv app
nv show service lldp application-tlv app <app-id>
nv show service lldp application-tlv tcp-port
nv show service lldp application-tlv tcp-port <port-id>
nv show service lldp application-tlv udp-port
nv show service lldp application-tlv udp-port <port-id>
nv show service telemetry histogram latency
nv show system cli
nv show system cli pagination
nv show system reboot required
nv show system security password-hardening
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart timers
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart timers stale-path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart timers selection-deferral
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart timers
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart timers stale-path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart timers selection-deferral
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart timers
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart timers stale-path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart timers selection-deferral
nv show vrf <vrf-id> router ospf area <area-id> network <network-id>
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set acl <acl-id> rule <rule-id> action log rate (1-50000)
nv set acl <acl-id> rule <rule-id> action log level (0-7)
nv set acl <acl-id> rule <rule-id> action recent
nv set acl <acl-id> rule <rule-id> match ip tcp mss <tcpmss-format>
nv set acl <acl-id> rule <rule-id> match ip tcp all-mss-except <tcpmss-format>
nv set acl <acl-id> rule <rule-id> match ip connection-state (established|related|new|invalid)
nv set acl <acl-id> rule <rule-id> match ip recent-list name <value>
nv set acl <acl-id> rule <rule-id> match ip recent-list update-interval (1-4294967295)
nv set acl <acl-id> rule <rule-id> match ip recent-list hit-count (1-4294967295)
nv set acl <acl-id> rule <rule-id> match ip recent-list action (set|update)
nv set acl <acl-id> rule <rule-id> match ip hashlimit name <generic-name>
nv set acl <acl-id> rule <rule-id> match ip hashlimit rate-above <rate-limit>
nv set acl <acl-id> rule <rule-id> match ip hashlimit burst <integer>
nv set acl <acl-id> rule <rule-id> match ip hashlimit source-mask <value>
nv set acl <acl-id> rule <rule-id> match ip hashlimit destination-mask <value>
nv set acl <acl-id> rule <rule-id> match ip hashlimit expire <value>
nv set acl <acl-id> rule <rule-id> match ip hashlimit mode (src-ip|dst-ip)
nv set interface <interface> lldp application-tlv app <application> 
nv set interface <interface> lldp application-tlv tcp-port <port>
nv set interface <interface> lldp application-tlv udp-port <port>
nv set interface <interface-id> ptp ipv6-scope
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id>
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold action log
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold value
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> bin-min-boundary
nv set interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> histogram-size
nv set service lldp application-tlv app <application> priority <priority> 
nv set service lldp application-tlv tcp-port <port> priority <priority> 
nv set service lldp application-tlv udp-port <port> priority <priority>
nv set service ptp <instance-id> ipv6-scope
nv set service telemetry histogram latency bin-min-boundary
nv set service telemetry histogram latency histogram-size
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
nv set system ssh-server strict
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset acl <acl-id> rule <rule-id> match ip tcp mss
nv unset acl <acl-id> rule <rule-id> match ip tcp all-mss-except
nv unset acl <acl-id> rule <rule-id> match ip connection-state
nv unset acl <acl-id> rule <rule-id> match ip recent-list
nv unset acl <acl-id> rule <rule-id> match ip recent-list name
nv unset acl <acl-id> rule <rule-id> match ip recent-list update-interval
nv unset acl <acl-id> rule <rule-id> match ip recent-list hit-count
nv unset acl <acl-id> rule <rule-id> match ip recent-list action
nv unset acl <acl-id> rule <rule-id> match ip hashlimit
nv unset acl <acl-id> rule <rule-id> match ip hashlimit name
nv unset acl <acl-id> rule <rule-id> match ip hashlimit rate-above
nv unset acl <acl-id> rule <rule-id> match ip hashlimit burst
nv unset acl <acl-id> rule <rule-id> match ip hashlimit source-mask
nv unset acl <acl-id> rule <rule-id> match ip hashlimit destination-mask
nv unset acl <acl-id> rule <rule-id> match ip hashlimit expire
nv unset acl <acl-id> rule <rule-id> match ip hashlimit mode
nv unset acl <acl-id> rule <rule-id> action log rate
nv unset acl <acl-id> rule <rule-id> action log level
nv unset acl <acl-id> rule <rule-id> action recent
nv unset interface <interface> lldp application-tlv
nv unset interface <interface> lldp application-tlv app <application> 
nv unset interface <interface> lldp application-tlv tcp-port
nv unset interface <interface> lldp application-tlv tcp-port <port>
nv unset interface <interface> lldp application-tlv udp-port <port>
nv unset interface <interface> lldp application-tlv udp-port
nv unset interface <interface-id> ptp ipv6-scope
nv unset interface <interface-id> telemetry histogram latency
nv unset interface <interface-id> telemetry histogram latency traffic-class
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id>
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold action
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> threshold value
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> bin-min-boundary
nv unset interface <interface-id> telemetry histogram latency traffic-class <if-tc-id> histogram-size
nv unset service lldp application-tlv
nv unset service lldp application-tlv app
nv unset service lldp application-tlv app <application>
nv unset service lldp application-tlv app <application> priority <priority>
nv unset service lldp application-tlv tcp-port
nv unset service lldp application-tlv tcp-port <port> 
nv unset service lldp application-tlv tcp-port <port> priority <priority>
nv unset service lldp application-tlv udp-port
nv unset service lldp application-tlv udp-port <port>
nv unset service lldp application-tlv udp-port <port> priority <priority>
nv unset service ptp <instance-id> ipv6-scope
nv unset service telemetry histogram latency
nv unset service telemetry histogram latency bin-min-boundary
nv unset service telemetry histogram latency histogram-size
nv unset system cli
nv unset system cli pagination
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
nv unset system ssh-server strict
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action clear interface <interface-id> link flap-protection violation
nv action clear system link flap-protection violation
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
