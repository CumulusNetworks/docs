---
title: NVUE CLI
author: NVIDIA
weight: 119
toc: 3
---
The NVUE CLI has a flat structure instead of a modal structure. Therefore, you can run all commands from the primary prompt instead of only in a specific mode.

{{%notice warning%}}
You can choose to configure Cumulus Linux either with NVUE commands **or** Linux commands (with vtysh or by manually editing configuration files). Do **not** run both NVUE configuration commands (such as `nv set`, `nv unset`, `nv action`, and `nv config`) and Linux commands to configure the switch. NVUE commands replace the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf`, and remove any configuration you add manually or with automation tools like Ansible, Chef, or Puppet.

If you choose to configure Cumulus Linux with NVUE, you can configure features that do not yet support the NVUE Object Model by creating snippets. See {{<link url="NVUE-Snippets" text="NVUE Snippets">}}.
{{%/notice%}}

## Command Syntax

NVUE commands all begin with `nv` and fall into one of three syntax categories:
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
acl        evpn       mlag       qos        service    vrf        
bridge     interface  nve        router     system

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
    <arg>                  (integer:552 - 9216)
cumulus@switch:~$ nv set interface swp1 link speed ?
    <arg>                  (string | enum:10M,100M,1G,10G,25G,40G,50G,100G,200G,40
                           0G,800G,auto)
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
Ambiguous Command: 
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
  interface             Update all interfaces

Identifiers:
  <interface-id>        Interface (interface-name)

Output Options:
  -o <format>, --output <format>
                        Supported formats: json, yaml, auto, constable, end-table, commands (default:auto)
  --color (on|off|auto)
                        Toggle coloring of output (default: auto)
  --paginate (on|off|auto)
                        Whether to send output to a pager (default: off)

General Options:
  -h, --help            Show help.
```

## Command List

You can list all the NVUE commands by running `nv list-commands`. See {{<link url="#list-all-nvue-commands" text="List All NVUE Commands">}} below.

## Command History
<!-- vale off -->
At the command prompt, press the Up Arrow and Down Arrow keys to move back and forth through the list of commands you entered previously. When you find the command you want to use, you can run the command by pressing Enter. You can also modify the command before you run it.
<!-- vale on -->

## Command Categories

The NVUE CLI has a flat structure; however, the commands are in three functional categories:

- Configuration
- Monitoring
- Configuration Management
- Action

### Configuration Commands

The NVUE configuration commands modify switch configuration. You can set and unset configuration options.
<!-- vale off -->
The `nv set` and `nv unset` commands are in the following categories. Each command group includes subcommands. Use command completion (press the tab key) to list the subcommands.
<!-- vale on -->
| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv set acl`<br>`nv unset acl` | Configures ACLs.|
| `nv set bridge`<br>`nv unset bridge` | Configures a bridge domain. This is where you configure bridge attributes, such as the bridge type (VLAN-aware), the STP state and priority, and VLANs. |
| `nv set evpn`<br>`nv unset evpn` | Configures EVPN. This is where you enable and disable the EVPN control plane, and set EVPN route advertise, multihoming, and duplicate address detection options. |
| `nv set interface <interface-id>`<br>`nv unset interface <interface-id>` | Configures the switch interfaces. Use this command to configure bond and bridge interfaces, interface IP addresses and descriptions, VLAN IDs, and links (MTU, FEC, speed, duplex, and so on).|
| `nv set mlag`<br>`nv unset mlag` | Configures MLAG. This is where you configure the backup IP address or interface, MLAG system MAC address, peer IP address, MLAG priority, and the delay before bonds come up. |
| `nv set nve`<br>`nv unset nve` | Configures network virtualization (VXLAN) settings. This is where you configure the UDP port for VXLAN frames, control dynamic MAC learning over VXLAN tunnels, enable and disable ARP and ND suppression, and configure how Cumulus Linux handles BUM traffic in the overlay.|
| `nv set qos`<br>`nv unset qos` | Configures QoS RoCE. |
| `nv set router`<br>`nv unset router` | Configures router policies (prefix list rules and route maps), sets global BGP options (enable and disable, ASN and router ID, BGP graceful restart and shutdown), global OSPF options (enable and disable, router ID, and OSPF timers) PIM, IGMP, PBR, VRR, and VRRP. |
| `nv set service`<br>`nv unset service` | Configures DHCP relays and servers, NTP, PTP, LLDP, SNMP servers, DNS, and syslog. |
| `nv set system`<br>`nv unset system` | Configures system settings, such as the hostname of the switch, pre and post login messages, reboot options (warm, cold, fast), the time zone and global system settings, such as the anycast ID, the system MAC address, and the anycast MAC address. This is also where you configure SPAN and ERSPAN sessions and set how configuration apply operations work (which files to ignore and which files to overwrite; see {{<link title="#configure-nvue-to-ignore-linux-files" text="Configure NVUE to Ignore Linux Files">}}).|
| `nv set vrf  <vrf-id>`<br>`nv unset vrf <vrf-id>` | Configures VRFs. This is where you configure VRF-level configuration for PTP, BGP, OSPF, and EVPN. |

### Monitoring Commands
<!-- vale off -->
The NVUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration or only interface configuration. The monitoring commands are in the following categories. Each command group includes subcommands. Use command completion (press the tab key) to list the subcommands.
<!-- vale on -->
| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv show acl` | Shows ACL configuration. |
| `nv show action`| Shows information about the action commands that reset counters and remove conflicts.|
| `nv show bridge` | Shows bridge domain configuration.|
| `nv show evpn` |Shows EVPN configuration. |
| `nv show interface` |Shows interface configuration and counters. |
| `nv show mlag` | Shows MLAG configuration. |
| `nv show nve` | Shows network virtualization configuration, such as VXLAN-specfic MLAG configuration and VXLAN flooding.|
| `nv show platform` | Shows platform configuration, such as hardware and software components. |
| `nv show qos` | Shows QoS RoCE configuration.|
| `nv show router` | Shows router configuration, such as router policies, global BGP and OSPF configuration, PBR, PIM, IGMP, VRR, and VRRP configuration. |
| `nv show service` | Shows DHCP relays and server, NTP, PTP, LLDP, and syslog configuration. |
| `nv show system` | Shows global system settings, such as the reserved routing table range for PBR and the reserved VLAN range for layer 3 VNIs. You can also see system login messages and switch reboot history. |
| `nv show vrf` | Shows VRF configuration.|

The following example shows the `nv show router` commands after pressing the tab key, then shows the output of the `nv show router bgp` command.

```
cumulus@leaf01:mgmt:~$ nv show router <<tab>>
adaptive-routing  igmp              ospf              pim               ptm               vrrp              
bgp               nexthop-group     pbr               policy            vrr               

cumulus@leaf01:mgmt:~$ nv show router bgp
                                operational  applied  pending      description
------------------------------  -----------  -------  -----------  ----------------------------------------------------------------------
enable                                       off      on           Turn the feature 'on' or 'off'.  The default is 'off'.
autonomous-system                                     none         ASN for all VRFs, if a single AS is in use.  If "none", then ASN mu...
graceful-shutdown                                     off          Graceful shutdown enable will initiate the GSHUT community to be an...
policy-update-timer                                   5            Wait time in seconds before processing updates to policies to ensur...
router-id                                             none         BGP router-id for all VRFs, if a common one is used.  If "none", th...
wait-for-install                                      off          bgp waits for routes to be installed into kernel/asic before advert...
convergence-wait
  establish-wait-time                                 0            Maximum time to wait to establish BGP sessions. Any peers which do...
  time                                                0            Time to wait for peers to send end-of-RIB before router performs pa...
graceful-restart
  mode                                                helper-only  Role of router during graceful restart. helper-only, router is in h...
  path-selection-deferral-time                        360          Used by the restarter as an upper-bounds for waiting for peering es...
  restart-time                                        120          Amount of time taken to restart by router. It is advertised to the...
  stale-routes-time                                   360          Specifies an upper-bounds on how long we retain routes from a resta...
cumulus@leaf01:mgmt:~$ 
```

{{%notice note%}}
If there are no pending or applied configuration changes, the `nv show` command only shows the running configuration (under operational).
{{%/notice%}}

Additional options are available for the `nv show` commands. For example, you can choose the configuration you want to show (pending, applied, startup, or operational). You can also turn on colored output, and paginate specific output.

| <div style="width:200px">Option | Description |
| ------ | ----------- |
| `--view` | Shows these different views: `acl-statistics`, `brief`, `detail`, `lldp`, `mac`, `mlag-cc`, `pluggables`, `qos-profile`, and `small`. This option is available for the `nv show interface` command only.</br></b>For example, the `nv show interface --view=small` command shows a list of the interfaces on the switch and the `nv show interface --view=brief` command shows information about each interface on the switch, such as the interface type, speed, remote host and port.</br></b>The `nv show interface --view=mac` command shows the MAC address of each interface and the `nv show interface --view=qos-profile` command shows the QoS profile for the interfaces on the switch.</br></b>Note: The description column only shows in the output when you use the `--view=detail` option.|
| `--filter` | Filters show command output on column data. For example, the `nv show interface --filter mtu=1500` shows only the interfaces with MTU set to 1500.</br>To filter on multiple column outputs, enclose the filter types in parentheses; for example, `nv show interface --filter "type=bridge&mtu=9216"` shows data for bridges with MTU 9216.</br>You can use wildcards; for example, `nv show interface swp1 --filter "ip.address=1*"` shows all IP addresses that start with `1` for swp1.</br>You can filter on all revisions (operational, applied, and pending); for example, `nv show interface  --filter "ip.address=1*" --rev=applied` shows all IP addresses that start with `1` for swp1 in the applied revision.|
| `--rev <revision>`| Shows a detached pending configuration. See the `nv config detach` configuration management command below. For example, `nv show --rev 1`. You can also show only applied or only operational information in the `nv show` output. For example, to show only the applied settings for swp1 configuration, run the `nv show interface swp1 --rev=applied` command. To show only the operational settings for swp1 configuration, run the `nv show interface swp1 --rev=operational` command. |
| `--applied`       | Shows configuration applied with the `nv config apply` command. For example, `nv show --applied interface bond1`. |
| `--operational`   | Shows the running configuration (the actual system state). For example, `nv show --operational interface bond1` shows the running configuration for bond1. The running and applied configuration should be the same. If different, inspect the logs. |
| `--pending`       | Shows the last applied configuration and any pending set or unset configuration that you have not yet applied. For example, `nv show --pending interface bond1`.|
| `--startup`  | Shows configuration saved with the `nv config save` command. This is the configuration after the switch boots. |
| `--output`        | Shows command output in table (`auto`), `json`, or `yaml` format. For example:<br>`nv show --ouptut auto interface bond1`<br>`nv show --output json interface bond1`<br>`nv show --ouptut yaml interface bond1` |
| `--color`         | Turns colored output on or off. For example, `nv show --color on interface bond1`|
| `--paginate`      | Paginates the output. For example, `nv show --paginate on interface bond1`. |
| `--help` | Shows `help` for the NVUE commands. |

The following example shows *pending* BGP graceful restart configuration:

```
cumulus@switch:~$ nv show router bgp graceful-restart --pending
                              4                  description
----------------------------  -----------------  ----------------------------------------------------------------------
mode                          helper-only        Role of router during graceful restart. helper-only, router is in h...
path-selection-deferral-time  360                Used by the restarter as an upper-bounds for waiting for peeringes...
restart-time                  120                Amount of time taken to restart by router. It is advertised to the...
stale-routes-time             360                Specifies an upper-bounds on how long we retain routes from a resta...
```

**Monitoring Commands and FRR Daemons**

If you run an NVUE show command but the corresponding FRR routing daemons are not running on the switch, you see an error message; for example:
- If OSPF is not running when you run `nv show vrf <vrf-id> ospf` commands, NVUE returns `Error: The requested item does not exist` because the OSPF deamon is not running in FRR.
- If PIM and IGMP are not running when you run the `nv show interface <interface> ip igmp -o json` command, NVUE returns `Error: The requested item does not exist` because the PIM daemon is not running in FRR.
- If PIM is running but IGMP is not running when you the `nv show interface <interface> ip igmp group -o json` command, NVUE does not return an error message but shows an empty { } response.

### Net Show commands

In addition to the `nv show` commands, Cumulus Linux continues to provide a subset of the NCLU `net show` commands. Use these commands to get additional views of various parts of your network configuration.

```
cumulus@leaf01:mgmt:~$ net show <<TAB>>
    bfd            :  Bidirectional forwarding detection
    bgp            :  Border Gateway Protocol
    bridge         :  a layer2 bridge
    clag           :  Multi-Chassis Link Aggregation
    commit         :  apply the commit buffer to the system
    configuration  :  settings, configuration state, etc
    counters       :  net show counters
    debugs         :  Debugs
    dhcp-snoop     :  DHCP snooping for IPv4
    dhcp-snoop6    :  DHCP snooping for IPv6
    dot1x          :  Configure, Enable, Delete or Show IEEE 802.1X EAPOL
    evpn           :  Ethernet VPN
    hostname       :  local hostname
    igmp           :  Internet Group Management Protocol
    interface      :  An interface, such as swp1, swp2, etc.
    ip             :  Internet Protocol version 4/6
    ipv6           :  Internet Protocol version 6
    lldp           :  Link Layer Discovery Protocol
    mpls           :  Multiprotocol Label Switching
    mroute         :  Static unicast routes in MRIB for multicast RPF lookup
    msdp           :  Multicast Source Discovery Protocol
    neighbor       :  A BGP, OSPF, PIM, etc neighbor
    ospf           :  Open Shortest Path First (OSPFv2)
    ospf6          :  Open Shortest Path First (OSPFv3)
    package        :  A Cumulus Linux package name
    pbr            :  Policy Based Routing
    pim            :  Protocol Independent Multicast
    port-mirror    :  port-mirror
    port-security  :  Port security
    ptp            :  Precision Time Protocol
    roce           :  Enable RoCE on all interfaces, default mode is lossless
    rollback       :  revert to a previous configuration state
    route          :  EVPN route information
    route-map      :  Route-map
    snmp-server    :  Configure the SNMP server
    system         :  System
    time           :  Time
    version        :  Version number
    vrf            :  Virtual routing and forwarding
    vrrp           :  Virtual Router Redundancy Protocol
```

### Configuration Management Commands

The NVUE configuration management commands manage and apply configurations.

| <div style="width:450px">Command | Description |
| ------- | ----------- |
| `nv config apply` | Applies the pending configuration (`nv config apply`) or a specific revision (`nv config apply 2`) to become the applied configuration. <br>You can also use these prompt options:<ul><li>`--y` or `--assume-yes` to automatically reply `yes` to all prompts.</li><li>`--assume-no` to automatically reply `no` to all prompts.</li></ul> {{%notice note%}}Cumulus Linux applies but does not save the configuration; the configuration does not persist after a reboot.{{%/notice%}}You can also use these apply options:<br>`--confirm` applies the configuration change but you must confirm the applied configuration. If you do not confirm within ten minutes, the configuration rolls back automatically. You can change the default time with the apply `--confirm <time>` command. For example, `apply --confirm 60` requires you to confirm within one hour.<br>`--confirm-status` shows the amount of time left before the automatic rollback.</br></br>To save the pending configuration to the startup configuration automatically when you run `nv config apply` so that you do not have to run the `nv config save` command, enable {{<link url="#configure-auto-save" text="auto save">}}.|
| `nv config detach` | Detaches the configuration from the current pending configuration and uses an integer to identify it; for example, `4`. To list all the current detached pending configurations, run `nv config diff <<press tab>`.|
| `nv config diff <revision> <revision>` | Shows differences between configurations, such as the pending configuration and the applied configuration, or the detached configuration and the pending configuration.|
| `nv config history` | Enables you to keep track of the configuration changes on the switch and shows a table with the configuration revision ID, the date and time the change was made, the user account that made the change, and the the type of change (such as CLI or REST API). The `nv config history <revision>` command shows the apply history for a specific revision. |
| `nv config patch <nvue-file>` | Updates the pending configuration with the specified YAML configuration file. |
| `nv config replace <nvue-file>` | Replaces the pending configuration with the specified YAML configuration file. |
| `nv config save` | Overwrites the startup configuration with the applied configuration by writing to the `/etc/nvue.d/startup.yaml` file. The configuration persists after a reboot. |
| `nv config show` | Shows the currently applied configuration in `yaml` format. This command also shows NVUE version information. |
| `nv config show -o commands` | Shows the currently applied configuration commands. |
| `nv config diff -o commands` | Shows differences between two configuration revisions. |

You can use the NVUE configuration management commands to back up and restore configuration when you upgrade Cumulus Linux on the switch. Refer to {{<link url="Upgrading-Cumulus-Linux/#back-up-and-restore-configuration-with-nvue" text="Upgrading Cumulus Linux">}}.

### Action Commands

The NVUE action commands clear counters, and provide system reboot and TACACS user disconnect options.

| <div style="width:400px">Command | Description |
| ------- | ----------- |
| `nv action change `| Sets the software clock date and time. |
| `nv action clear` | Provides commands to clear ACL statistics, {{<link url="EVPN-Enhancements/#clear-duplicate-addresses" text="duplicate addresses">}}, {{<link url="Precision-Time-Protocol-PTP/#clear-ptp-violation-logs" text="PTP violations">}}, {{<link url="Interface-Configuration-and-Management/#clear-the-interface-protodown-state-and-reason" text="interfaces from a protodown state">}}, {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#clear-interface-counters" text="interface counters">}}, {{<link url="Quality-of-Service/#clear-qos-buffers" text="Qos buffers">}}, {{<link url="Troubleshooting-BGP/#clear-bgp-routes" text="BGP routes">}}, {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#clear-ospf-counters" text="OSPF interface counters">}}, {{<link url="Route-Filtering-and-Redistribution/#clear-matches-against-a-route-map" text="matches against a route map">}}, and remove {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#lacp-partner-mac-address-duplicate-or-mismatch" text="conflicts from protodown MLAG bonds">}}. |
| `nv action delete` | Provides commands to delete system configuration files, and CA and entity certificates. |
| `nv action disable system maintenance mode`<br>`nv action disable system maintenance ports`| Disables system maintenance mode<br> Brings up the ports.|
| `nv action disconnect system aaa user`|  Provides commands to disconnect users logged into the switch. |
| `nv action enable system maintenance mode`<br>`nv action enable system maintenance ports`| Enables system maintenance mode.<br> Brings all the ports down for maintenance. |
| `nv action export system config` | Exports a configuration file. |
| `nv action fetch system config` | Fetches a configuration file.|
| `nv action import system security` | Provides commands to import CA and entity certificates. |
| `nv action reboot system` |  Reboots the switch in the configured restart mode ({{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="fast, cold, or warm">}}). You must specify the `no-confirm` option with this command. |
| `nv action rename system config files`| Renames system configuration files. |
| `nv action upload system config files`| Uploads system configuration files. |

### List All NVUE Commands

To show the full list of NVUE commands, run `nv list-commands`. For example:

```
cumulus@switch:~$ nv list-commands
nv show platform
nv show platform hardware
nv show platform hardware component
nv show platform hardware component <component-id>
nv show platform software
nv show platform software installed
nv show platform software installed <installed-id>
nv show platform capabilities
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
<!-- vale off -->
Use the tab key to get help for the command lists you want to see. For example, to show the list of command options available for swp1, run the `nv list-commands interface swp1` command and press the tab key:
<!-- vale on -->
```
cumulus@switch:~$ nv list-commands interface swp1 <<press tab>>
acl            counters       link           ptp            storm-control  
bond           evpn           lldp           qos            synce          
bridge         ip             pluggable      router         tunnel
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
| `/etc/ntp.conf` | Configures NTP settings. |
| `/etc/ptp4l.conf` | Configures PTP settings.|
| `/etc/snmp/snmpd.conf`| Configures SNMP settings.|

## Search for a Specific Configuration

To search for a specific portion of the NVUE configuration, run the `nv config find <search string>` command. The search shows all items above and below the search string. For example, to search the entire NVUE object model configuration for any mention of `ptm`:

```
cumulus@switch:~$ nv config find ptm
- set:
    router:
      ptm:
        enable: off
```

## Configure NVUE to Ignore Linux Files

You can configure NVUE to ignore certain underlying Linux files when applying configuration changes. For example, if you push certain configuration to the switch using Ansible and Jinja2 file templates or you want to use custom configuration for a particular service such as PTP, you can ensure that NVUE never writes to those configuration files.

The following example configures NVUE to ignore the Linux `/etc/ptp4l.conf` file when applying configuration changes and saves the configuration so it persists after a reboot.

```
cumulus@switch:~$ nv set system config apply ignore /etc/ptp4l.conf
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv config save
```

## Configure Auto Save

By default, when you run the `nv config apply` command to apply a configuration setting, NVUE applies the pending configuration to become the applied configuration but does not update the startup configuration file (`/etc/nvue.d/startup.yaml`). To save the applied configuration to the startup configuration so that the changes persist after the reboot, you must run the `nv config save` command. The auto save option lets you save the pending configuration to the startup configuration automatically when you run `nv config apply` so that you do not have to run the `nv config save` command.

To enable auto save:

```
cumulus@switch:~$ nv set system config auto-save enable on
cumulus@switch:~$ nv config apply
```

To disable auto save, run the `nv set system config auto-save enable off` command.

## Add Configuration Apply Messages

When you run the `nv config apply` command, you can add a message that describes the configuration updates you make. You can see the message when you run the `nv config history` command.

To add a configuration apply message, run the `nv config apply -m <message>` command. If the message includes more than one word, enclose the message in quotes.

```
cumulus@switch:~$ nv config apply -m "this is my message"
```

## Reset NVUE Configuration to Default Values

To reset the NVUE configuration on the switch back to the default values, run the following command:

```
cumulus@switch:~$ nv config apply empty
```

## Example Configuration Commands

This section provides examples of how to configure a Cumulus Linux switch using NVUE commands.

### Configure the System Hostname

The example below shows the NVUE commands required to change the hostname for the switch to leaf01:

```
cumulus@switch:~$ nv set system hostname leaf01
cumulus@switch:~$ nv config apply
```

### Configure the System DNS Server

The example below shows the NVUE commands required to define the DNS server for the switch:

```
cumulus@switch:~$ nv set service dns mgmt server 192.168.200.1
cumulus@switch:~$ nv config apply
```

### Configure an Interface

The example below shows the NVUE commands required to bring up swp1.

```
cumulus@switch:~$ nv set interface swp1
cumulus@switch:~$ nv config apply 
```

### Configure a Bond

The example below shows the NVUE commands required to configure the front panel port interfaces swp1 thru swp4 to be slaves in bond0.

```
cumulus@switch:~$ nv set interface bond0 bond member swp1-4
cumulus@switch:~$ nv config apply
```

### Configure a Bridge

The example below shows the NVUE commands required to create a VLAN-aware bridge that contains two switch ports (swp1 and swp2) and includes 3 VLANs; tagged VLANs 10 and 20 and an untagged (native) VLAN of 1.

With NVUE, there is a default bridge called `br_default`, which has no ports assigned to it. The example below configures this default bridge.

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10,20
cumulus@switch:~$ nv set bridge domain br_default untagged 1
cumulus@switch:~$ nv config apply
```

### Configure MLAG

The example below shows the NVUE commands required to configure MLAG on leaf01. The commands:
- Place swp1 into bond1 and swp2 into bond2.
- Configure the MLAG ID to 1 for bond1 and to 2 for bond2.
- Add bond1 and bond2 to the default bridge (br_default).
- Create the inter-chassis bond (swp49 and swp50) and the peer link (peerlink)
- Set the peer link IP address to `linklocal`, the MLAG system MAC address to 44:38:39:BE:EF:AA, and the backup interface to 10.10.10.2.

```
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@switch:~$ nv set interface bond1-2 bridge domain br_default 
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv config apply
```

### Configure BGP Unnumbered

The example below shows the NVUE commands required to configure BGP unnumbered on leaf01. The commands:
- Assign the ASN for this BGP node to 65101.
- Set the router ID to 10.10.10.1.
- Distribute routing information to the peer on swp51.
- Originate prefixes 10.10.10.1/32 from this BGP node.

```
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
cumulus@leaf01:~$ nv config apply
```

## Example Monitoring Commands

This section provides monitoring command examples.

### Show Installed Software

The following example command lists the software installed on the switch:

```
cumulus@switch:~$ nv show platform software
Installed Software
=====================
Installed software            description                     package                      version                       
---------------------------   ---------------------------     --------------------------   -----------------------------
acpi                          displays information on ACPI    acpi                         1.7-1.1                       
                              devices                                                                                  
acpi-support-base             scripts for handling base       acpi-support-base            0.142-8                       
                              ACPI events such as the                                                                  
                              power button                                                                             
acpid                         Advanced Configuration and      acpid                        1:2.0.31-1                    
                              Power Interface event daemon                                                             
adduser                       add and remove users and        adduser                      3.118                         
                              groups                                                                                   
apt                           commandline package manager     apt                          1.8.2.3             
...
```

### Show Interface Configuration

The following example command shows the running, applied, and pending swp1 interface configuration.

```
cumulus@leaf01:~$ nv show interface swp1
                          operational        applied   
------------------------  -----------------  ----------
type                      swp                swp       
[acl]                                                  
bridge                                                 
  [domain]                br_default         br_default
evpn                                                   
  multihoming                                          
    uplink                                   off       
ptp                                                    
  enable                                     off       
router                                                 
  adaptive-routing                                     
    enable                                   off       
  ospf                                                 
    enable                                   off       
  ospf6                                                
    enable                                   off       
  pbr                                                  
    [map]                                              
  pim            
...
```

## Example Configuration Management Commands

This section provides examples of how to use the configuration management commands to apply, save, and detach configurations.

### Apply and Save a Configuration

The following example command configures the front panel port interfaces swp1 thru swp4 to be slaves in bond0. The configuration is only in a pending configuration state. The configuration is **not** applied. NVUE has not yet made any changes to the running configuration.

```
cumulus@switch:~$ nv set interface bond0 bond member swp1-4
```

To apply the pending configuration to the running configuration, run the `nv config apply` command. The configuration does **not** persist after a reboot.

```
cumulus@switch:~$ nv config apply
```

To save the applied configuration to the startup configuration, run the `nv config save` command. This command overwrites the startup configuration with the applied configuration by writing to the `/etc/nvue.d/startup.yaml` file. The configuration persists after a reboot.

```
cumulus@switch:~$ nv config save
```

### Detach a Pending Configuration

The following example configures the IP address of the loopback interface, then detaches the configuration from the current pending configuration. Cumulus Linux saves the detached configuration to a file with a numerical value to distinguish it from other pending configurations.

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@switch:~$ nv config detach
```

### View Differences Between Configurations

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

### Replace and Patch a Pending Configuration

The following example replaces the pending configuration with the contents of the YAML configuration file called `nv-02/13/2021.yaml` located in the `/deps` directory:

```
cumulus@switch:~$ nv config replace /deps/nv-02/13/2021.yaml
```

The following example patches the pending configuration (runs the set or unset commands from the configuration in the `nv-02/13/2021.yaml` file located in the `/deps` directory):

```
cumulus@switch:~$ nv config patch /deps/nv-02/13/2021.yaml
```
