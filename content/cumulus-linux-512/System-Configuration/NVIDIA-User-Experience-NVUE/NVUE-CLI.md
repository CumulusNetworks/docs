---
title: NVUE CLI
author: NVIDIA
weight: 119
toc: 3
---
The NVUE CLI has a flat structure instead of a modal structure. Therefore, you can run all commands from the primary prompt instead of only in a specific mode.

{{%notice warning%}}
You can choose to configure Cumulus Linux either with NVUE commands **or** Linux commands (with vtysh or by manually editing configuration files). Do **not** run both NVUE configuration commands (such as `nv set`, `nv unset`, `nv action`, and `nv config`) and Linux commands to configure the switch. NVUE commands replace the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf`, and remove any configuration you add manually or with automation tools like Ansible, Chef, or Puppet.

If you choose to configure Cumulus Linux with NVUE, you can configure features that do not yet support the NVUE object model by creating snippets. See {{<link url="NVUE-Snippets" text="NVUE Snippets">}}.
{{%/notice%}}

## Command Syntax

NVUE commands all begin with `nv` and fall into one of four syntax categories:
- Configuration (`nv set` and ` nv unset`)
- Monitoring (`nv show`)
- Configuration management (`nv config`)
- Action commands (`nv action`)

## Command Completion
<!-- vale off -->
As you enter commands, you can get help with the valid keywords or options using the tab key. For example, using tab completion with `nv set` displays the possible options for the command and returns you to the command prompt to complete the command.
<!-- vale on -->
```
cumulus@switch:~$ nv set <<press tab>>
acl        evpn       mlag       platform   router     system     
bridge     interface  nve        qos        service    vrf
cumulus@switch:~$ nv set
```

## Command Question Mark

You can type a question mark (`?`) after a command to display required information quickly and concisely. When you type `?`, NVUE specifies the value type, range, and options with a brief description of each; for example:

```
cumulus@switch:~$ nv set interface swp1 link state ?
    [Enter]               
    down                   The interface is not ready
    up                     The interface is ready
cumulus@switch:~$ nv set interface swp1 link mtu ?
    <arg>                  Interface MTU (default:9216 | integer:552 - 9216)
cumulus@switch:~$ nv set interface swp1 link speed ?
    <arg>                  Link speed (default:auto | enum:auto, 10M, 100M, 1G, 10G, 25G,
                           40G, 50G, 100G, 200G, 400G, 800G | string)
```

NVUE also indicates if you need to provide specific values for the command:

```
cumulus@switch:~$ nv set interface swp1 bridge domain ?
    <domain-id>            Domain (bridge-name)
```

## Command Abbreviation

NVUE supports command abbreviation, where you can type a certain number of characters instead of a whole command to speed up CLI interaction. For example, instead of typing `nv show interface`, you can type `nv sh int`.

If the command you type is ambiguous, NVUE shows the reason for the ambiguity so that you can correct the shortcut. For example:

```
cumulus@switch:~$ nv s i 
Error: Ambiguous Command:
  set interface
  show interface 
```

## Command Help
<!-- vale off -->
As you enter commands, you can get help with command syntax by entering `-h` or `--help` at various points within a command entry. For example, to examine the options available for `nv set interface`, enter `nv set interface -h` or `nv set interface --help`.
<!-- vale on -->
```
cumulus@switch:~$ nv set interface -h
usage: 
  nv [options] set interface <interface-id>

Description:
  interface       Update all interfaces. Provide single interface or multiple interfaces using ranging (e.g. swp1-2,5-6 -> swp1,swp2,swp5,swp6).

Identifiers:
  <interface-id>  Interface (interface-name)

General Options:
  -h, --help      Show help.
```

## Command List

You can list all the NVUE commands by running `nv list-commands`. See {{<link url="#list-all-nvue-commands" text="List All NVUE Commands">}} below.

## Command History
<!-- vale off -->
At the command prompt, press the Up Arrow and Down Arrow keys to move back and forth through the list of commands you entered previously. When you find the command you want to use, you can run the command by pressing Enter. You can also modify the command before you run it.
<!-- vale on -->

## Command Categories

The NVUE CLI has a flat structure; however, the commands are in four functional categories:

- {{<link url="#configuration-commands" text="Configuration">}}
- {{<link url="#monitoring-commands" text="Monitoring">}}
- {{<link url="#configuration-management-commands" text="Configuration Management">}}
- {{<link url="#action-commands" text="Action">}}

### Configuration Commands

The NVUE configuration commands modify switch configuration. You can set and unset configuration options.

The `nv set` and `nv unset` commands are in the following categories. Each command group includes subcommands. Use command completion (press the tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv set acl`<br>`nv unset acl` | Configures {{<link url="Access-Control-Lists" text="Access Control Lists">}}.|
| `nv set bridge`<br>`nv unset bridge` | Configures a {{<link url="Ethernet-Bridging-VLANs" text="bridge">}}. This is where you configure bridge attributes, such as the bridge type (VLAN-aware), the STP state and priority, and VLANs. |
| `nv set evpn`<br>`nv unset evpn` | Configures {{<link url="Basic-Configuration" text="EVPN">}}. This is where you enable and disable the EVPN control plane, and set EVPN route advertise, multihoming, and duplicate address detection options. |
| `nv set interface <interface-id>`<br>`nv unset interface <interface-id>` | Configures the {{<link url="Interface-Configuration-and-Management" text="switch interfaces">}}. Use this command to configure bond and bridge interfaces, interface IP addresses and descriptions, VLAN IDs, and {{<link url="Switch-Port-Attributes" text="links (MTU, FEC, speed, duplex, and so on)">}}.|
| `nv set mlag`<br>`nv unset mlag` | Configures {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}}. This is where you configure the backup IP address or interface, MLAG system MAC address, peer IP address, MLAG priority, and the delay before bonds come up. |
| `nv set nve`<br>`nv unset nve` | Configures {{<link url="Network-Virtualization" text="network virtualization (VXLAN) settings">}}. This is where you configure the UDP port for VXLAN frames, control dynamic MAC learning over VXLAN tunnels, enable and disable ARP and ND suppression, and configure how Cumulus Linux handles BUM traffic in the overlay.|
| `nv set platform`<br>`nv unset platform`|  Configures {{<link url="Pulse-Per-Second-PPS" text="Pulse per Second">}}; the simplest form of synchronization for the physical hardware clock.|
| `nv set qos`<br>`nv unset qos` | Configures {{<link title="RDMA over Converged Ethernet - RoCE" text="QoS RoCE">}}. |
| `nv set router`<br>`nv unset router` | Configures {{<link url="Route-Filtering-and-Redistribution" text="router policies">}} (prefix list rules and route maps), sets {{<link url="Basic-BGP-Configuration" text="global BGP options">}} (enable and disable, ASN and router ID, BGP graceful restart and shutdown), {{<link url="Open-Shortest-Path-First-v2-OSPFv2" text="global OSPF options">}} (enable and disable, router ID, and OSPF timers) {{<link url="Protocol-Independent-Multicast-PIM" text="PIM">}}, {{<link url="IGMP-and-MLD-Snooping" text="IGMP">}}, {{<link url="Policy-based-Routing" text="PBR">}}, {{<link url="Virtual-Router-Redundancy-VRR" text="VRR">}}, and {{<link url="Virtual-Router-Redundancy-Protocol-VRRP" text="VRRP">}}. |
| `nv set service`<br>`nv unset service` | Configures {{<link url="DHCP-Relays" text="DHCP relays">}} and {{<link url="DHCP-Servers" text="DHCP servers">}}, {{<link url="Network-Time-Protocol-NTP" text="NTP">}}, {{<link url="Precision-Time-Protocol-PTP" text="PTP">}}, {{<link url="Link-Layer-Discovery-Protocol" text="LLDP">}}, DNS, and {{<link url="Log-Files-with-NVUE" text="syslog">}}. |
| `nv set system`<br>`nv unset system` | Configures system settings, such as the {{<link title="Quick Start Guide/#configure-the-hostname" text="hostname of the switch">}}, pre and post login messages, {{<link title="In Service System Upgrade - ISSU/#restart-mode" text="reboot options (warm, cold, fast)">}}, {{<link title="Setting the Date and Time/#set-the-time-zone" text="time zone ">}} and global system settings, such as the anycast ID, the system MAC address, and the anycast MAC address. This is also where you configure {{<link url="Configure-SNMP" text="SNMP">}}, {{<link url="SPAN-and-ERSPAN" text="SPAN and ERSPAN sessions">}}, {{<link url="Open-Telemetry-Export" text="telemetry">}}, and set how configuration apply operations work (which files to ignore and which files to overwrite; see {{<link title="#configure-nvue-to-ignore-linux-files" text="Configure NVUE to Ignore Linux Files">}}).|
| `nv set vrf  <vrf-id>`<br>`nv unset vrf <vrf-id>` | Configures {{<link url="VRFs" text="VRFs">}}. This is where you configure VRF-level configuration for PTP, BGP, OSPF, and EVPN. |

### Monitoring Commands

The NVUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration or only interface configuration. The monitoring commands are in the following categories. Each command group includes subcommands. Use command completion (press the tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv show acl` | Shows {{<link url="Access-Control-Lists" text="Access Control List">}} configuration. |
| `nv show action`| Shows information about the action commands that reset counters and remove conflicts.|
| `nv show bridge` | Shows {{<link url="VLAN-aware-Bridge-Mode/#troubleshooting" text="bridge">}} configuration.|
| `nv show evpn` |Shows {{<link url="EVPN-Enhancements/#show-current-evpn-configuration" text="EVPN">}} configuration. |
| `nv show interface` |Shows {{<link url="Interface-Configuration-and-Management/#show-interface-information" text="interface">}} configuration and counters. |
| `nv show mlag` | Shows {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#troubleshooting" text="MLAG">}} configuration. |
| `nv show nve` | Shows {{<link url="Network-Virtualization" text="network virtualization (VXLAN)">}} configuration, such as VXLAN-specfic MLAG configuration and VXLAN flooding.|
| `nv show platform` | Shows {{<link url="Monitoring-Best-Practices/#hardware" text="platform configuration">}}, such as hardware and software components. |
| `nv show qos` | Shows {{<link title="RDMA over Converged Ethernet - RoCE/#verify-roce-configuration" text="QoS RoCE">}} configuration.|
| `nv show router` | Shows router configuration, such as router policies, global BGP and OSPF configuration, PBR, PIM, IGMP, VRR, and VRRP configuration. |
| `nv show service` | Shows {{<link url="DHCP-Relays/#troubleshooting" text="DHCP-Relays">}} and {{<link url="DHCP-Servers/#troubleshooting" text="DHCP server">}} configuration, {{<link url="Network-Time-Protocol-NTP" text="NTP">}}, {{<link url="Precision-Time-Protocol-PTP/#troubleshooting" text="PTP">}}, {{<link url="Link-Layer-Discovery-Protocol" text="LLDP">}}, and syslog configuration. |
| `nv show system` | Shows system settings. |
| `nv show vrf` | Shows {{<link url="VRFs" text="VRFs">}} configuration.|

The following example shows the `nv show router` commands after pressing the tab key, then shows the output of the `nv show router bgp` command.

```
cumulus@leaf01:mgmt:~$ nv show router <<tab>>
adaptive-routing  igmp              pbr               ptm               
bgp               nexthop           pim               vrr               
graceful-restart  ospf              policy            vrrp               

cumulus@leaf01:mgmt:~$ nv show router bgp
                                applied    
------------------------------  -----------
enable                          on         
autonomous-system               65101      
router-id                       10.10.10.1 
policy-update-timer             5          
graceful-shutdown               off        
wait-for-install                off        
graceful-restart                           
  mode                          helper-only
  restart-time                  120        
  path-selection-deferral-time  360        
  stale-routes-time             360        
convergence-wait                           
  time                          0          
  establish-wait-time           0          
queue-limit                                
  input                         10000      
  output                        10000 
```

{{%notice note%}}
If there are no pending or applied configuration changes, the `nv show` command only shows the running configuration (under operational).
{{%/notice%}}

Additional options are available for certain `nv show` commands. For example, you can choose the configuration you want to show (pending, applied, startup, or operational). You can also turn on colored output, and paginate specific output.

| <div style="width:200px">Option | Description |
| ------ | ----------- |
| `--applied`| Shows configuration applied with the `nv config apply` command. For example, `nv show --applied`. |
| `--brief-help` | Shows help about the `nv show` command. For example, `nv show interface swp1 --brief-help`|
| `--color`  | Turns colored output on or off. For example, `nv show interface swp1 --color on`|
| `--filter` | Filters show command output on column data. For example, the `nv show interface --filter mtu=1500` shows only the interfaces with MTU set to 1500. For more information, see {{<link url="#filter-nv-show-command-output" text="Filter nv show Command Output">}} below.|
| `--hostname`| Shows system configuration for the switch with the specified hostname. For example, `nv show --hostname leaf01`.|
| `--operational` | Shows the running configuration (the actual system state). For example, `nv show interface swp1 --operational` shows the running configuration for swp1. The running and applied configuration should be the same. If different, inspect the logs. |
| `--output`        | Shows command output in table (`auto`), `json`, or `yaml` format. For example:<br>`nv show interface bond1 --output auto`<br>`nv show interface bond1 --output json`<br>`nv show interface bond1 --output yaml`|
| `--paginate`      | Paginates the output. For example, `nv show interface bond1 --paginate on`. |
| `--pending`       | Shows the last applied configuration and any pending set or unset configuration that you have not yet applied. For example, `nv show interface bond1 --pending`.|
| `--rev <revision>`| Shows a detached pending configuration. See the `nv config detach` configuration management command below. For example, `nv show --rev 1`. You can also show only applied or only operational information in the `nv show` output. For example, to show only the applied settings for swp1 configuration, run the `nv show interface swp1 --rev=applied` command. To show only the operational settings for swp1 configuration, run the `nv show interface swp1 --rev=operational` command. |
| `--startup`  | Shows configuration saved with the `nv config apply` command. This is the configuration after the switch boots. For example: `nv show interface --startup`.|
| `--tab`| Show information in tab format. For example, `nv show interface swp1 --tab.`|
| `--view` | Shows different views. A view is a subset of information provided by certain `nv show` commands. To see the views available for an `nv show` command, run the command with `--view` and press TAB (for example `nv show interface --view`).|

The following example shows *pending* BGP graceful restart configuration:

```
cumulus@switch:~$ nv show router bgp graceful-restart --pending
                              Rev ID: 8                  
----------------------------  -----------------  
mode                          helper-only        
path-selection-deferral-time  360              
restart-time                  120              
stale-routes-time             360              
```

The following example shows the views available for the `nv show interface` command:

```
cumulus@switch:~$ nv show interface --view <<TAB>>
acl-statistics  counters        down            neighbor        small           vrf
bond-members    description     lldp            physical        status          
bonds           detail          lldp-detail     port-security   svi             
brief           dot1x-counters  mac             qos-profile     synce-counters  
carrier-stats   dot1x-summary   mlag-cc         rates           up
```

### Configuration Management Commands

The NVUE configuration management commands manage and apply configurations.

| <div style="width:450px">Command | Description |
| ------- | ----------- |
| `nv config apply` | Saves the pending configuration (`nv config apply`) or a specific revision (`nv config apply 2`) to the startup configuration automatically (when auto save is `on`, which is the default setting). To see the list of revisions you can apply, run `nv config apply <<Tab>>`. <br>You can also use these prompt options:<ul><li>`--assume-yes` to automatically reply `yes` to all prompts.</li><li>`--assume-no` to automatically reply `no` to all prompts.</li></ul>You can also use these apply options:<br>`--confirm` applies the configuration change but you must confirm the applied configuration. If you do not confirm within ten minutes, the configuration rolls back automatically. You can change the default time with the apply `--confirm <time>` command. For example, `nv config apply --confirm 60m` requires you to confirm within one hour.<br>`--confirm-status` shows the amount of time left before the automatic rollback.</br>|
| `nv config detach` | Detaches the configuration from the current pending configuration and uses an integer to identify it; for example, `4`. To list all the current detached pending configurations, run `nv config diff <<press tab>`.|
| `nv config diff <revision> <revision>` | {{<link url="NVUE-CLI/#view-differences-between-configurations" text="Shows differences between configurations">}}, such as the pending configuration and the applied configuration, or the detached configuration and the pending configuration.|
| `nv config find <string>`| {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="Finds a portion of the applied configuration">}} according to the search string you provide. For example to find swp1 in the applied configuration, run `nv config find swp1`.|
| `nv config history` | Enables you to keep track of the configuration changes on the switch and shows a table with the configuration revision ID, the date and time of the change, the user account that made the change, and the type of change (such as CLI or REST API). The `nv config history <revision>` command shows the apply history for a specific revision. |
| `nv config patch <nvue-file>` | {{<link url="NVUE-CLI/#replace-and-patch-a-pending-configuration" text="Updates the pending configuration">}} with the specified YAML configuration file. |
| `nv config replace <nvue-file>` | {{<link url="NVUE-CLI/#replace-and-patch-a-pending-configuration" text="Replaces the pending configuration">}} with the specified YAML configuration file. |
|`nv config revision` | Shows all the configuration revisions on the switch. |
| `nv config save` | {{<link url="NVUE-CLI/#auto-save" text="Overwrites the startup configuration">}} with the applied configuration by writing to the `/etc/nvu.d/startup.yaml` file. The configuration persists after a reboot. Use this command when the auto save option is off.|
| `nv config show` | Shows the {{<link url="NVUE-CLI/#show-switch-configuration" text="currently applied configuration">}} in `yaml` format. This command also shows NVUE version information. |
| `nv config show -o commands` | Shows the currently applied configuration commands. |
| `nv config diff -o commands` | Shows differences between two configuration revisions. |

You can use the NVUE configuration management commands to back up and restore configuration when you upgrade Cumulus Linux on the switch. Refer to {{<link url="Upgrading-Cumulus-Linux/#back-up-and-restore-configuration-with-nvue" text="Upgrading Cumulus Linux">}}.

### Action Commands

The NVUE action commands fetch and install image files, upgrade system packages, run ping and traceroute, disable system maintenance and ZTP scripts, clear counters, rotate log files, and provide system reboot and TACACS user disconnect options.

| <div style="width:400px">Command | Description |
| ------- | ----------- |
| `nv action abort`| Terminates {{<link url="Zero-Touch-Provisioning-ZTP" text="ZTP">}} if it is in the discovery process or is not currently running a script. |
| `nv action boot-next`| Sets the boot partition for {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="optimized (two partition) upgrade">}}.|
| `nv action change`| Sets the {{<link title="Setting the Date and Time/#set-the-date-and-time" text="software clock date and time">}}. |
| `nv action clear` | Provides commands to clear ACL statistics, {{<link url="EVPN-Enhancements/#clear-duplicate-addresses" text="duplicate addresses">}}, {{<link url="Precision-Time-Protocol-PTP/#clear-ptp-violation-logs" text="PTP violations">}}, {{<link url="Interface-Configuration-and-Management/#clear-the-interface-protodown-state-and-reason" text="interfaces from a protodown state">}}, {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#clear-interface-counters" text="interface counters">}}, {{<link url="Quality-of-Service/#clear-qos-buffers" text="Qos buffers">}}, {{<link url="Troubleshooting-BGP/#clear-bgp-routes" text="BGP routes">}}, {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#clear-ospf-counters" text="OSPF interface counters">}}, {{<link url="Route-Filtering-and-Redistribution/#clear-matches-against-a-route-map" text="matches against a route map">}}, and remove {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#lacp-partner-mac-address-duplicate-or-mismatch" text="conflicts from protodown MLAG bonds">}}. |
| `nv action deauthenticate interface <interface> dot1x authorized-sessions`| {{<link url="802.1X-Interfaces/#deauthenticate-an-8021x-supplicant" text="Deauthenticates the 802.1X supplicant">}} on the specified interface. If you do not want to notify the supplicant when deauthenticating, you can add the silent option; for example, `nv action deauthenticate interface swp1 dot1x authorized-sessions 00:55:00:00:00:09 silent`.|
| `nv action delete` | Provides commands to delete {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="binary image files">}}, {{<link url="Log-Files-with-NVUE/#delete-system-log-files" text="log files">}}, {{<link url="Adding-and-Updating-Packages/#manage-repository-keys" text="packages">}}, {{<link url="NVUE-API/#delete-certificates" text="CA and entity certificates">}} and {{<link url="Understanding-the-cl-support-Output-File/#delete-cl-support-files" text="tech support files">}}. |
| `nv action disable`| Provides commands to disable {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="system maintenance mode">}} and {{<link url="Zero-Touch-Provisioning-ZTP" text="ZTP scripts">}}.|
| `nv action disconnect`|  Provides commands to {{<link url="User-Accounts/#disconnect-user-account-active-terminals" text="disconnect users logged into the switch">}}. |
| `nv action enable`| Provides commands to enable {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="system maintenance mode">}} and {{<link url="Zero-Touch-Provisioning-ZTP" text="ZTP scripts">}}. |
| `nv action export`| Exports a system configuration file.|
| `nv action fetch`| Fetches {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="binary image files">}}, {{<link url="Adding-and-Updating-Packages/#manage-repository-keys" text="package files">}}, configuration files, and platform firmware. |
| `nv action generate` | Generates {{<link url="Understanding-the-cl-support-Output-File/#manual-cl-support-file" text="cl-support files">}}.|
| `nv action import` | Provides commands to {{<link url="NVUE-API/#import-a-certificate" text="import CA and entity certificates">}}. |
| `nv action install` | Installs {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="system image files">}}. |
| `nv action lookup`| Looks up the {{<link url="FRRouting/#look-up-the-route-for-a-destination" text="route in the routing table">}} for a specific destination. |
| `nv action ping` | Provides commands to run {{<link url="Network-Troubleshooting/#ping" text="ping">}}.|
| `nv action reboot` | Reboots the switch in the configured restart mode ({{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="fast, cold, or warm">}}). You must specify the `no-confirm` option with this command. |
| `nv action rename` | Provides commands to {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="system image files">}}.|
| `nv action reset` | Provides commands to {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#reset-a-transceiver" text="reset transceivers">}} and to reset the switch to {{<link url="Factory-Reset" text="factory defaults">}}.|
| `nv action rotate` | Provides commands to {{<link url="Log-Files-with-NVUE/#rotate-the-system-log-file" text="rotate the system log file">}}.|
| `nv action run` | Provides commands to run {{<link url="Zero-Touch-Provisioning-ZTP" text="ZTP scripts">}}.|
| `nv action schedule` | Configures the schedule for {{<link url="ASIC-Monitoring/#high-frequency-telemetry" text="high frequency telemetry data collection">}}.|
| `nv action traceroute` | Provides commands to run {{<link url="Network-Troubleshooting/#traceroute" text="traceroute">}}.|
| `nv action rename`| Renames the system configuration.|
| `nv action upgrade` | {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="Upgrades system packages">}}.|
| `nv action upload` | Uploads {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="system image files">}}, {{<link url="Understanding-the-cl-support-Output-File/#manual-cl-support-file" text="cl-support files">}}, and configuration files to the switch.|

### List All NVUE Commands

To show the full list of NVUE commands, run `nv list-commands`. For example:

```
cumulus@switch:~$ nv list-commands
nv show platform
nv show platform inventory
nv show platform inventory <inventory-id>
nv show platform software
nv show platform software installed
nv show platform software installed <installed-id>
nv show platform firmware
nv show platform firmware <platform-component-id>
nv show platform environment
...
```

You can show the list of commands for a command grouping. For example, to show the list of interface commands:

```
cumulus@switch:~$ nv list-commands interface
nv show interface
nv show interface <interface-id>
nv show interface <interface-id> ip
nv show interface <interface-id> ip address
nv show interface <interface-id> ip address <ip-prefix-id>
nv show interface <interface-id> ip gateway
nv show interface <interface-id> ip gateway <ip-address-id>
...
```

To view the NVUE command reference for Cumulus Linux, which describes all the NVUE CLI commands and provides examples, go to the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvue-reference/" text="NVUE Command Reference">}}.

## NVUE Configuration File

When you save network configuration, NVUE writes the configuration to the `/etc/nvue.d/startup.yaml` file.

You can edit or replace the contents of the `/etc/nvue.d/startup.yaml` file. NVUE applies the configuration in the `/etc/nvue.d/startup.yaml` file during system boot only if the `nvue-startup.service` is running. If this service is not running, the switch reboots with the same configuration that is running before the reboot.

To start `nvue-startup.service`:

```
cumulus@switch:~$ sudo systemctl enable nvue-startup.service
cumulus@switch:~$ sudo systemctl start nvue-startup.service
```

When you apply a configuration with `nv config apply`, NVUE also writes to underlying Linux files such as `/etc/network/interfaces` and `/etc/frr/frr.conf`. You can view these configuration files; however, do *not* manually edit them while using NVUE. If you need to configure certain network settings manually or use automation such as Ansible to configure the switch, see {{<link title="#configure-nvue-to-ignore-linux-files" text="Configure NVUE to Ignore Linux Files">}} below.

### Default Startup File

NVUE provides a default `/etc/nvue.d/startup.yaml` file that includes configuration such as the switch hostname, default firewall rules, and `cumulus` user account credentials. The file also enables the NVUE API. This file is the factory configuration file that you can restore at any time.

{{%notice info%}}
- The default startup configuration file sets the default hostname as `cumulus`; therefore, Cumulus Linux does not accept the DHCP `host-name` option. To set a different hostname with NVUE, see {{<link url="Quick-Start-Guide/#configure-the-hostname" text="Configure the Hostname">}}. If you do not manage your switch with NVUE and want to change this behavior with Linux configuration files, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Hostname-Option-Received-From-DHCP-Ignored" >}}).
- The default NVUE `startup.yaml` file includes the `cumulus` user account, which is the default account for the system. Modifying the NVUE configuration to not include the `cumulus` user account, replacing the configuration or applying a startup configuration, deletes the `cumulus` account. To merge in configuration changes or to restore a backup `startup.yaml` file, use the `nv config patch` command as described in {{<link url="Upgrading-Cumulus-Linux#back-up-and-restore-configuration-with-nvue" text=" Back up and Restore Configuration with NVUE">}}.
- You cannot delete a logged in user account.
{{%/notice%}}

### Encrypted Passwords

By default, NVUE encrypts passwords, such as the RADIUS secret, TACACS secret, BGP peer password, OSPF MD5 key, and SNMP strings in the `startup.yaml` file. You can disable password encryption with the `nv set system security encryption db state disabled` command:

```
cumulus@switch:~$ nv set system security encryption db state disabled
cumulus@switch:~$ nv config apply
```

To set password encryption back to the default setting (enabled), run the `nv unset system security encryption db state` command or the `nv set system security encryption db state enabled` command.

To show if password encryption is `on`, run the `nv show system security encryption` command:

```
cumulus@switch:~$ nv show system security encryption
         operational  applied
-------  -----------  -------
db                           
  state               enabled
```

## Configuration Files that NVUE Manages

NVUE manages the following configuration files:

| File  | Description|
| ----- | ---------- |
| `/etc/network/interfaces` | Configures the network interfaces available on your system.|
| `/etc/frr/frr.conf` | Configures FRRouting.|
| `/etc/cumulus/switchd.conf` |  Configures `switchd` options.|
| `/etc/cumulus/switchd.d/ptp.conf` | Configures PTP timestamping.|
| `/etc/frr/daemons` | Configures FRRouting services.|
| `/etc/hosts` | Configures the hostname of the switch. |
| `/etc/default/isc-dhcp-relay-default`| Configures DHCP relay options.|
| `/etc/dhcp/dhcpd.conf`| Configures DHCP server options.|
| `/etc/hostname` | Configures the hostname of the switch. |
| `/etc/cumulus/datapath/qos/qos_features.conf` |Configures QoS settings, such as traffic marking, shaping and flow control.  |
| `/etc/mlx/datapath/qos/qos_infra.conf` |  Configures QoS platform specific configurations, such as buffer allocations and Alpha values.|
| `/etc/cumulus/switchd.d/qos.conf` | Configures QoS settings. |
| `/etc/cumulus/ports.conf` | Configures port breakouts.|
| `etc/ntpsec/ntp.conf` | Configures NTP settings. |
| `/etc/ptp4l.conf` | Configures PTP settings.|
| `/etc/snmp/snmpd.conf`| Configures SNMP settings.|

## Search for a Specific Configuration

To search for a specific portion of the NVUE configuration, run the `nv config find <search string>` command. The search shows all items above and below the search string. For example, to search the entire NVUE object model configuration for any mention of `bond1`:

```
cumulus@switch:~$ nv config find bond1
- set:
    interface:
      bond1:
        bond:
          lacp-bypass: on
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default:
              access: 10
        link:
          mtu: 9000
        type: bond
```

## Configure NVUE to Ignore Linux Files

You can configure NVUE to ignore certain underlying Linux files when applying configuration changes. For example, if you push certain configuration to the switch using Ansible and Jinja2 file templates or you want to use custom configuration for a particular service such as PTP, you can ensure that NVUE never writes to those configuration files.

The following example configures NVUE to ignore the Linux `/etc/ptp4l.conf` file when applying configuration changes.

```
cumulus@switch:~$ nv set system config apply ignore /etc/ptp4l.conf
cumulus@switch:~$ nv config apply
```

## Auto Save

By default, when you run the `nv config apply` command to apply a configuration setting, NVUE applies the pending configuration to become the applied configuration and automatically saves the changes to the startup configuration file (`/etc/nvue.d/startup.yaml`).

To disable auto save so that NVUE does not save applied configuration changes, run the `nv set system config auto-save state disabled` command:

```
cumulus@switch:~$ nv set system config auto-save state disabled
cumulus@switch:~$ nv config apply
```

When you disable auto save, you must run the `nv config save` command to save the applied configuration to the startup configuration so that the changes persist after a reboot.

To renable auto save, run the `nv set system config auto-save state enabled` command.

## Show Switch Configuration

To show the applied configuration on the switch, run the `nv config show` command:

```
cumulus@switch:~$ nv config show
header:
    model: VX
    nvue-api-version: nvue_v1
    rev-id: 1.0
    version: Cumulus Linux 5.7.0
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
            '30':
              vni:
                '30': {}
...
```

To show the configuration on the switch in YAML format and include all default options, run the `nv config show --all` command.

## Add Configuration Apply Messages

When you run the `nv config apply` command, you can add a message that describes the configuration updates you make. You can see the message when you run the `nv config history` command.

To add a configuration apply message, run the `nv config apply -m <message>` command. If the message includes more than one word, enclose the message in quotes.

```
cumulus@switch:~$ nv config apply -m "this is my message"
```

## Reset NVUE Configuration to Default Values

To reset the NVUE configuration on the switch back to the default values, run the `nv config replace <filename>` command; for example:

```
cumulus@switch:~$ nv config replace /usr/lib/python3/dist-packages/cue_config_v1/initial.yaml
cumulus@switch:~$ nv config apply
```

## Detach a Pending Configuration

The following example configures the IP address of the loopback interface, then detaches the configuration from the current pending configuration. Cumulus Linux saves the detached configuration to a file with a numerical value to distinguish it from other pending configurations.

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@switch:~$ nv config detach
```

## View Differences Between Configurations

To view differences between configurations, run the `nv config diff` command.

To view differences between two detached pending configurations, run the `nv config diff` <<tab>> command to list all the current detached pending configurations, then run the `nv config diff` command with the pending configurations you want to diff.

```
cumulus@switch:~$ nv config diff <<press tab>>
1        2        3        4        5        6        applied  empty    startup
```

```
cumulus@switch:~$ nv config diff 2 3
- unset:
    system:
      wjh:
        channel:
          forwarding:
            trigger:
              l2:
```

To view differences between the applied configuration and the startup configuration:

```
cumulus@switch:~$ nv config diff applied startup
- unset:
    interface:
    system:
      wjh:
```

## Replace and Patch a Pending Configuration

The following example replaces the pending configuration with the contents of the YAML configuration file called `nv-02/13/2021.yaml` located in the `/deps` directory:

```
cumulus@switch:~$ nv config replace /deps/nv-02/13/2021.yaml
```

The following example patches the pending configuration (runs the set or unset commands from the configuration in the `nv-02/13/2021.yaml` file located in the `/deps` directory):

```
cumulus@switch:~$ nv config patch /deps/nv-02/13/2021.yaml
```

{{%notice note%}}
A patch contains a single request to the NVUE service. Ordering of parameters within a patch is not guaranteed; NVUE does not support both unset and set commands for the same object in a single patch.
{{%/notice%}}

## Translate a Configuration Revision or File

NVUE provides commands to translate an NVUE configuration revision or yaml file into NVUE commands. The revision ID must be either an integer or a named revision (such as startup or applied). The configuration file must be located on the switch and must include the full path to the file containing the configuration you want to translate. The file must be in YAML format and must be accessible with proper read permissions.

To translate a specific NVUE configuration revision, run the `nv config translate revision <revision-id>` command. NVUE displays the translation on the console.

The following command translates the configuration in revision 1:

```
cumulus@switch:~$ nv config translate revision 10 
```

The following command translates the configuration in the applied revision:

```
cumulus@switch:~$ nv config translate revision applied 
```

To translate a configuration file, run the `nv config translate filename <filename>` command. The following example translates the `backup.yaml` file in the `/home/cumulus` directory. NVUE displays the translation on the console.

```
cumulus@switch:~$ nv config translate filename /home/cumulus/backup.yaml
```

If the revision or yaml file is not readable, is in an invalid format, or includes invalid parameters, NVUE returns an error message and prompts you to correct the issue before proceeding.

## Session-Based Authentication

NVUE uses sessions to authenticate and authorize requests. After authenticating the user with the first request, NVUE stores the session in the `nvued` cache. NVUE authenticates subsequent interactions within the session locally so that it does not have to keep checking with external authentication servers. This process enhances system performance and efficiency, making it ideal for high-traffic environments.

- If you make changes to a user group, password, RADIUS, TACACS, or LDAP server setting locally on the switch, NVUE clears the current session automatically.
- If you make changes directly on the RADIUS, TACACS, or LDAP server, you must clear the user session with the `nv action clear system api session user <user>` command or clear all sessions with the `nv action clear system api session` command.

The following example clears the `admin` user session:

```
cumulus@switch:~$ nv action clear system api session user admin
```

The following example clears all sessions:

```
cumulus@switch:~$ nv action clear system api session
```

{{%notice note%}}
If you do not clear a user session after making changes directly on the RADIUS, TACACS, or LDAP server, NVUE uses the existing session for authentication and authorization until the session times out (up to 60 minutes).
{{%/notice%}}

## Passwords and Special Characters

If you use certain special characters in a password, you must quote or escape (with a backslash) these characters so that the system understands that they are part of the password.

The following table shows which quote or escape you can use for each special character.

- *Normal Use* indicates that you can use the special character without quotes or a backslash.
- *Single Quotes* and *Double Quotes* indicate that you need to enclose the entire password in quotes.

| Special Character | Normal Use  | Single Quotes ('') | Double Quotes ("") | Escape (`\`)|
|---------- | ------- | ------------------ | ------------------ | ------ |
| backtick (`) | x | ✓ | 1 | ✓ |
| exclamation point (`!`) | x | ✓ | x | ✓ |
| semicolon (`;`) | x | ✓ | ✓ | ✓ |
| ampersand (`&`) | x | ✓ | ✓ | ✓ |
| question mark (`?`) |x | ✓ | ✓ | x |
| tilde (~) | x | ✓ | ✓ | ✓ |
| at-sign (`@`) | ✓ | ✓ | ✓ | ✓ |
| hash sign (`#`) | x | ✓ | ✓ | ✓ |
| dollar sign (`$`) | x | ✓ | x | ✓ |
| percent sign (`%`) | ✓ | ✓ | ✓ | ✓ |
| caret (`^`) | ✓ | ✓ | ✓ | ✓ |
| asterisk (`*`) | ✓ | ✓ | ✓ | ✓ |
| parentheses (`()`) | x |  ✓ | ✓ | ✓ |
| dash (`-`) | ✓ | ✓ | ✓ | ✓ |
| underscore (`_`)| ✓ | ✓ | ✓ | ✓ |
| equals sign (`=`) | ✓ | ✓ | ✓ | ✓ |
| plus sign (`+`) | ✓ | ✓ | ✓ | ✓ |
| vertical bar | x | ✓ | ✓ | ✓ |
| brackets (`[]`) | ✓ | ✓ | ✓ | ✓ |
| braces (`{}`) | ✓ | ✓ | ✓ | ✓ |
| colon (`:`) | ✓ | ✓ | ✓ | ✓ |
| single quote (`‘`) | x | x |  ✓ | ✓ |
| double quote (`“`) | x | ✓ |  x | ✓ |
| comma (`,`) | ✓ | ✓ | ✓ | ✓ |
| angle brackets (`<>`) | x | ✓ | ✓ | ✓ |
| slash (`/`) | ✓ | ✓ | ✓ | ✓ |
| dot (`.`) | 2 | 2 | 2 | 2 |
| white space | x | x | 3 | x |

1. Requires escape (`\`) in addition to the double quotes (`""`).
2. You cannot use this character at the beginning of a word.
3. A word cannot consist entirely of white space, even inside double quotes.

The following example shows a password that includes a question mark (?):

```
cumulus@switch:~$ nv set system aaa user cumulus password “Hello?world123”
```

The following example shows a password that includes a dot (.):

```
cumulus@switch:~$ nv set system aaa user cumulus password “Hello.world.123”
```

The following example shows a password that includes a dot (.) and tilde (~):

```
cumulus@switch:~$ nv set system aaa user cumulus password “Hello.world\~123”
```

You might need to encode special characters in a password, for example in a URL.  The following table shows the special character encoding.
- `✓` indicates that encoding is not needed.
- `%xx` indicates that you need to replace the special character with `%xx`.

| Symbol             | Normal | Single Quotes ('') | Double Quotes ("") | Escape (`\`)|
|--------------------|--------|-----------------|-----------------|---------|
| backtick (`)      | %60    | ✓               | %60             | ✓       |
| exclamation point (`!`)  | %21    | ✓               | %21             | ✓       |
| semicolon (`;`)      | %3B    | ✓               | ✓               | ✓       |
| ampersand (`&`)     | %26    | ✓               | ✓               | ✓       |
| question mark (`?`)      | %3F    | %3F             | %3F             | %3F     |
| tilde (~)         | ✓      | ✓               | ✓               | ✓       |
| at-sign (`@`)       | ✓      | ✓               | ✓               | ✓       |
| hash sign (`#`)         | %23    | %23             | %23             | %23     |
| dollar sign (`$`)        | %24    | ✓               | %24             | ✓       |
| percent sign (`%`)        | ✓      | ✓               | ✓               | ✓       |
| caret (`^`)         | ✓      | ✓               | ✓               | ✓       |
| asterisk (`*`)    | ✓      | ✓               | ✓               | ✓       |
| left parenthesis (`(`)     | %28    | ✓               | ✓               | ✓       |
| right parenthesis (`)`)   | %29    | ✓               | ✓               | ✓       |
| dash (`-`)        | ✓      | ✓               | ✓               | ✓       |
| underscore (`_`) | ✓      | ✓               | ✓               | ✓       |
| equals sign (`=`) | ✓      | ✓               | ✓               | ✓       |
| plus sign (`+`)         | ✓      | ✓               | ✓               | ✓       |
| vertical bar  | %7C    | ✓               | ✓               | ✓       |
| left bracket (`[`)  | %5B    | %5B             | %5B             | %5B     |
| right bracket (`]`) | %5D    | %5D             | %5D             | %5D     |
| braces (`{}`)        | ✓      | ✓               | ✓               | ✓       |
| colon (`:`)          | ✓      | ✓               | ✓               | ✓       |
| single quote (`‘`)   | %27    | %27             | ✓               | ✓       |
| double quote (`“`)   | %22    | ✓               | %22             | ✓       |
| comma (`,`)         | ✓      | ✓               | ✓               | ✓       |
| left angle bracket (`<`)    | %3C    | ✓               | ✓               | ✓       |
| right angle bracket (`>`)  | %3E    | ✓               | ✓               | ✓       |
| slash (`/`)         | %2F    | %2F             | %2F             | %2F     |
| dot (`.`)             | ✓      | ✓               | ✓               | ✓       |
| white space  | %20    | ✓               | ✓               | ✓       |

The following example fetches an image stored on a device with IP address 10.0.1.251 using the password `Pass#pass1` for user1:

```
cumulus@switch:~$ nv action fetch system image scp://user1:Pass1%23pass1@10.0.1.251/host/nos-images/nvos-amd64-25.02.1857.bin
```

## Filter nv show Command Output

Filters show command output on column data; for example, to show only the interfaces with MTU set to 1500:

```
cumulus@switch:~$ nv show interface --filter mtu=1500
Interface  Admin Status  Oper Status  Speed  MTU   Type  Remote Host      Remote Port  Summary                                
---------  ------------  -----------  -----  ----  ----  ---------------  -----------  ---------------------------------------
eth0       up            up           1G     1500  eth   oob-mgmt-switch  swp10        IP Address:           192.168.200.11/24
                                                                                       IP Address: fe80::4638:39ff:fe22:17a/64
swp4       down          down                1500  swp                                                                        
swp5       down          down                1500  swp                                                                        
swp6       down          down                1500  swp                                                                        
swp7       down          down                1500  swp                                                                        
swp8       down          down                1500  swp                                                                        
swp9       down          down                1500  swp                                                                        
swp10      down          down                1500  swp                                                                        
swp11      down          down                1500  swp                                                                        
swp12      down          down                1500  swp                                                                        
swp13      down          down                1500  swp
...
```

To filter on multiple column outputs, enclose the entire filter in double quotes; for example, to show data for bridges with MTU 9216:

```
cumulus@switch:~$ nv show interface --filter "type=bridge&mtu=9216" 
Interface   Admin Status  Oper Status  Speed  MTU   Type    Remote Host  Remote Port  Summary                                
----------  ------------  -----------  -----  ----  ------  -----------  -----------  ---------------------------------------
br_default  up            up                  9216  bridge                            IP Address: fe80::4638:39ff:fe22:17a/64
```

You can use wildcards; for example, to show all IP addresses that start with 1 for swp1, run the `nv show interface swp1 --filter "ip.address=1*"` command.

You can filter on all revisions (operational, applied, and pending); for example, to show all IP addresses that start with 1 for swp1 in the applied revision:

```
cumulus@switch:~$ nv show interface --filter "ip.address=1*" --rev=applied
Interface  Admin Status  Oper Status  Speed  MTU   Type      Remote Host  Remote Port  Summary                  
---------  ------------  -----------  -----  ----  --------  -----------  -----------  -------------------------
lo                                                 loopback                            IP Address: 10.10.10.1/32
vlan10                                       9216  svi                                 IP Address:  10.1.10.2/24
vlan20                                       9216  svi                                 IP Address:  10.1.20.2/24
vlan30                                       9216  svi                                 IP Address:  10.1.30.2/24
```

You can filter the FRR `nv show vrf <vrf> router rib` command output by protocol (gp, ospf, kernel, static, ospf6, sharp, or connected); for example, to show all BGP IPv4 routes in the routing table:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route --filter=protocol=bgp                                                                             
Flags - * - selected, q - queued, o - offloaded, i - installed, S - fib-        
selected, x - failed                                                            
                                                                                
Route            Protocol  Distance  Uptime                NHGId  Metric  Flags
---------------  --------  --------  --------------------  -----  ------  -----
10.0.1.34/32     bgp       20        2024-12-17T10:24:14Z  127    0       *Si  
10.0.1.255/32    bgp       20        2024-12-17T10:24:10Z  127    0       *Si  
10.10.10.2/32    bgp       20        2024-12-17T10:24:10Z  62     0       *Si  
10.10.10.3/32    bgp       20        2024-12-17T10:24:17Z  127    0       *Si  
10.10.10.4/32    bgp       20        2024-12-17T10:24:10Z  127    0       *Si  
10.10.10.63/32   bgp       20        2024-12-17T10:24:10Z  127    0       *Si  
10.10.10.64/32   bgp       20        2024-12-17T10:24:17Z  127    0       *Si  
10.10.10.101/32  bgp       20        2024-12-17T10:24:10Z  102    0       *Si  
10.10.10.102/32  bgp       20        2024-12-17T10:24:10Z  115    0       *Si  
10.10.10.103/32  bgp       20        2024-12-17T10:24:10Z  121    0       *Si  
10.10.10.104/32  bgp       20        2024-12-17T10:24:10Z  113    0       *Si  
```

You can filter the FRR `nv show vrf <vrf> router bgp neighbor` command output by state (established or non-established); for example, to show all BGP established neighbors:

```
cumulus@switch:~$ nv show vrf default router bgp neighbor --filter=state=established                                                                             
AS - Remote Autonomous System, PeerEstablishedTime - Peer established time in   
UTC format, UpTime - Uptime in milliseconds, Afi-Safi - Address family, PfxSent 
- Transmitted prefix counter, PfxRcvd - Recieved prefix counter                 
                                                                                
Neighbor       AS     State        PeerEstablishedTime   UpTime   MsgRcvd  MsgSent  Afi-Safi      PfxSent  PfxRcvd
-------------  -----  -----------  --------------------  -------  -------  -------  ------------  -------  -------
peerlink.4094  65102  established  2024-12-17T10:22:36Z  8998000  3145     3151     ipv4-unicast  13       12     
                                                                                    l2vpn-evpn    72       51     
swp51          65199  established  2024-12-17T10:22:41Z  8998000  3132     3149     ipv4-unicast  13       8      
                                                                                    l2vpn-evpn    72       51     
swp52          65199  established  2024-12-17T10:22:44Z  8998000  3125     3139     ipv4-unicast  13       8      
                                                                                    l2vpn-evpn    72       51     
swp53          65199  established  2024-12-17T10:22:44Z  8998000  3138     3139     ipv4-unicast  13       8      
                                                                                    l2vpn-evpn    72       51     
swp54          65199  established  2024-12-17T10:22:44Z  8998000  3143     3139     ipv4-unicast  13       8      
                                                                                    l2vpn-evpn    72       51  
```

To show all BGP non-established neighbors:

```
cumulus@switch:~$ nv show vrf default router bgp neighbor --filter=state!=established
AS - Remote Autonomous System, PeerEstablishedTime - Peer established time in
UTC format, UpTime - Uptime in milliseconds, Afi-Safi - Address family, PfxSent
- Transmitted prefix counter, PfxRcvd - Recieved prefix counter

Neighbor  AS  State  PeerEstablishedTime  UpTime   MsgRcvd  MsgSent  Afi-Safi      PfxSent  PfxRcvd
--------  --  -----  -------------------  -------  -------  -------  ------------  -------  -------
swp53         idle                        9318000  0        0        ipv4-unicast                  
                                                                     l2vpn-evpn                    
swp54         idle                        9318000  0        0        ipv4-unicast                  
                                                                     l2vpn-evpn
```

To show a summary of the connection information for all BGP neighbors:

```
cumulus@switch:~$ nv show vrf default router bgp neighbor --view=detail

AS - Remote Autonomous System, PeerEstablishedTime - Peer established time in
UTC format, UpTime - Uptime in milliseconds, Afi-Safi - Address family, PfxSent
- Transmitted prefix counter, PfxRcvd - Recieved prefix counter

Neighbor       AS     State        PeerEstablishedTime   UpTime    MsgRcvd  MsgSent  Afi-Safi      PfxSent  PfxRcvd
-------------  -----  -----------  --------------------  --------  -------  -------  ------------  -------  -------
peerlink.4094  65102  established  2025-01-26T15:28:11Z  27073000  561127   473795   ipv4-unicast  11       10     
                                                                                     l2vpn-evpn    70       50     
swp51          65199  established  2025-01-26T15:28:16Z  27073000  548373   473791   ipv4-unicast  11       8      
                                                                                     l2vpn-evpn    70       50     
swp52          65199  established  2025-01-26T15:28:19Z  27073000  548377   473789   ipv4-unicast  11       8      
                                                                                     l2vpn-evpn    70       50     
swp53                 idle                               27073000  0        0        ipv4-unicast                  
                                                                                     l2vpn-evpn                    
swp54                 idle                               27073000  0        0        ipv4-unicast                  
                                                                                     l2vpn-evpn                    
```

To show a summary of the connection information for all BGP neighbors in json format, run the `nv show vrf default router bgp neighbor -o json` command.

{{%notice note%}}
In Cumulus Linux 5.11 and earlier, the `nv show vrf default router bgp neighbor -o json` command output shows more detailed information about BGP peers. To show the more detailed information in Cumulus Linux 5.12, run the `nv show vrf <vrf> router bgp neighbor --view=detail -o json` command.
{{%/notice%}}

## Show Command View Include and Omit Options

NVUE show commands provide `--view` include and omit options that let you specify which table columns you want to include or omit from the command output.

The following example shows the `nv show vrf default router rib ipv4 route` command output (without the `--view` include or omit option):

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route
Flags - * - selected, q - queued, o - offloaded, i - installed, S - fib-
selected, x - failed

Route            Protocol   Distance  Uptime                NHGId  Metric  Flags
---------------  ---------  --------  --------------------  -----  ------  -----
10.0.1.12/32     connected  0         2025-02-08T16:26:22Z  12     0       *Sio 
10.0.1.34/32     bgp        20        2025-02-11T16:05:22Z  124    0       *Si  
10.0.1.255/32    bgp        20        2025-02-11T16:05:22Z  124    0       *Si  
10.10.10.1/32    connected  0         2025-02-08T16:26:13Z  12     0       *Sio 
10.10.10.2/32    bgp        20        2025-02-11T16:05:22Z  62     0       *Si  
10.10.10.3/32    bgp        20        2025-02-11T16:05:22Z  124    0       *Si  
10.10.10.4/32    bgp        20        2025-02-11T16:05:22Z  124    0       *Si  
10.10.10.63/32   bgp        20        2025-02-11T16:05:22Z  124    0       *Si  
10.10.10.64/32   bgp        20        2025-02-11T16:05:22Z  124    0       *Si  
10.10.10.101/32  bgp        20        2025-02-11T16:05:22Z  100    0       *Si  
10.10.10.102/32  bgp        20        2025-02-11T16:05:22Z  120    0       *Si 
```

The following example shows the `nv show vrf default router rib ipv4 route` command with the option to only include the Routes, Protocol, Uptime, and NHGID (nexthop group ID) columns in the output:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route --view "include=/*/route-entry/*/protocol,/*/route-entry/*/nexthop-group-id,/*/route-entry/*/uptime"
Route            Protocol   Uptime                NHGId
---------------  ---------  --------------------  -----
10.0.1.12/32     connected  2025-02-08T16:26:22Z  12   
10.0.1.34/32     bgp        2025-02-11T16:05:22Z  124  
10.0.1.255/32    bgp        2025-02-11T16:05:22Z  124  
10.10.10.1/32    connected  2025-02-08T16:26:13Z  12   
10.10.10.2/32    bgp        2025-02-11T16:05:22Z  62   
10.10.10.3/32    bgp        2025-02-11T16:05:22Z  124  
10.10.10.4/32    bgp        2025-02-11T16:05:22Z  124  
10.10.10.63/32   bgp        2025-02-11T16:05:22Z  124  
10.10.10.64/32   bgp        2025-02-11T16:05:22Z  124  
10.10.10.101/32  bgp        2025-02-11T16:05:22Z  100  
10.10.10.102/32  bgp        2025-02-11T16:05:22Z  120
```

The following example shows the `nv show vrf default router rib ipv4 route` command with the option to omit all columns (except Route) in the output:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route --view "omit=/*/*"
Route          
---------------
10.0.1.12/32   
10.0.1.34/32   
10.0.1.255/32  
10.10.10.1/32  
10.10.10.2/32  
10.10.10.3/32  
10.10.10.4/32  
10.10.10.63/32 
10.10.10.64/32 
10.10.10.101/32
10.10.10.102/32
```

## NVUE and FRR Restart

NVUE restarts the FRR service when you:
- Change the `/etc/frr/daemons` file.
- Change the BGP ASN.
- Remove the default instance.
- Disable the SNMP server with `agentx` configured.

Restarting FRR restarts all the routing protocol daemons that you enable and that are running, which might impact traffic.
