---
title: NVUE CLI
author: NVIDIA
weight: 119
toc: 3
---
The NVUE CLI has a flat structure as opposed to a modal structure. This means that you can run all commands from the primary prompt instead of only in a specific mode.

{{%notice warning%}}
You can choose to configure Cumulus Linux either with NVUE commands **or** Linux commands (with vtysh or by manually editing configuration files). Do **not** run both NVUE configuration commands (such as `nv set`, `nv unset`, `nv action`, and `nv config`) and Linux commands to configure the switch. NVUE commands replace the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf`, and remove any configuration you add manually or with automation tools like Ansible, Chef, or Puppet.

If you choose to configure Cumulus Linux with NVUE, you can configure features that do not yet support the NVUE Object Model by creating snippets. See {{<link url="NVUE-Snippets" text="NVUE Snippets">}}.
{{%/notice%}}

## Command Syntax

NVUE commands all begin with `nv` and fall into one of four syntax categories:
- Configuration (`nv set` and ` nv unset`)
- Monitoring (`nv show`)
- Configuration management (`nv config`)
- Action commands (`nv action`)

## Command Completion
<!-- vale off -->
As you enter commands, you can get help with the valid keywords or options using the Tab key. For example, using Tab completion with `nv set` displays the possible options for the command and returns you to the command prompt to complete the command.
<!-- vale on -->
```
cumulus@switch:~$ nv set <<press Tab>>
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
    <arg>                  (integer:552 - 9216)
cumulus@switch:~$ nv set interface swp1 link speed ?
   (auto|10M|100M|1G|10G|25G|40G|50G|100G|200G|400G)    Link speed
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
Usage:
  nv set interface [options] <interface-id> ...

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
At the command prompt, press the Up Arrow and Down Arrow keys to move back and forth through the list of commands you entered. When you find a given command, you can run the command by pressing Enter. Optionally, you can modify the command before you run it.
<!-- vale on -->

## Command Categories

The NVUE CLI has a flat structure; however, the commands are in four functional categories:

- {{<link url="#configuration-commands" text="Configuration">}}
- {{<link url="#monitoring-commands" text="Monitoring">}}
- {{<link url="#configuration-management-commands" text="Configuration Management">}}
- {{<link url="#action-commands" text="Action">}}

### Configuration Commands

The NVUE configuration commands modify switch configuration. You can set and unset configuration options.
<!-- vale off -->
The `nv set` and `nv unset` commands are in the following categories. Each command group includes subcommands. Use command completion (Tab key) to list the subcommands.
<!-- vale on -->
| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv set acl`<br>`nv unset acl` | Configures ACLs in Cumulus Linux.|
| `nv set bridge`<br>`nv unset bridge` | Configures a bridge domain. This is where you configure the bridge type (such as VLAN-aware), 802.1Q encapsulation, the STP state and priority, and the VLANs in the bridge domain. |
| `nv set evpn`<br>`nv unset evpn` | Configures EVPN. This is where you enable and disable the EVPN control plane, and set EVPN route advertise, multihoming, and duplicate address detection options. |
| `nv set interface <interface-id>`<br>`nv unset interface <interface-id>` | Configures the switch interfaces. Use this command to configure bond interfaces, bridge interfaces, interface IP addresses, interface descriptions, VLAN IDs, and links (MTU, FEC, speed, duplex, and so on).|
| `nv set mlag`<br>`nv unset mlag` | Configures MLAG. This is where you configure the backup IP address or interface, MLAG system MAC address, peer IP address, MLAG priority, and the delay before bonds come up. |
| `nv set nve`<br>`nv unset nve` | Configures network virtualization (VXLAN) settings. This is where you configure the UDP port for VXLAN frames, control dynamic MAC learning over VXLAN tunnels, enable and disable ARP and ND suppression, and configure how Cumulus Linux handles BUM traffic in the overlay.|
| `nv set platform`<br>`nv unset platform` | Configures hardware component options. |
| `nv set qos`<br>`nv unset qos` | Configures QoS RoCE. |
| `nv set router`<br>`nv unset router` | Configures router policies (prefix list rules and route maps), sets global BGP options (enable and disable, ASN and router ID, BGP graceful restart and shutdown), global OSPF options (enable and disable, router ID, and OSPF timers) PIM, IGMP, PBR, VRR, and VRRP. |
| `nv set service`<br>`nv unset service` | Configures DHCP relays and servers, NTP, PTP, LLDP, and syslog. |
| `nv set system`<br>`nv unset system` | Configures the hostname of the switch, pre and post login messages, the time zone and global system settings, such as the anycast ID, the system MAC address, and the anycast MAC address. This is also where you configure SPAN and ERSPAN sessions and set how configuration apply operations work (which files to ignore and which files to overwrite; see {{<link title="#configure-nvue-to-ignore-linux-files" text="Configure NVUE to Ignore Linux Files">}}).|
| `nv set vrf  <vrf-id>`<br>`nv unset vrf <vrf-id>` | Configures VRFs. This is where you configure VRF-level configuration for PTP, BGP, OSPF, and EVPN. |

### Monitoring Commands
<!-- vale off -->
The NVUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration or only interface configuration. The monitoring commands are in the following categories. Each command group includes subcommands. Use command completion (Tab key) to list the subcommands.
<!-- vale on -->
| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv show acl` | Shows ACL configuration. |
| `nv show action`| Shows information about the action commands that reset counters and remove conflicts.|
| `nv show bridge` | Shows bridge domain configuration.|
| `nv show evpn` |Shows EVPN configuration. |
| `nv show interface` |Shows interface configuration. |
| `nv show mlag` | Shows MLAG configuration. |
| `nv show nve` | Shows network virtualization configuration, such as VXLAN-specfic MLAG configuration and VXLAN flooding.|
| `nv show platform` | Shows platform configuration, such as hardware and software components. |
| `nv show qos` | Shows QoS RoCE configuration.|
| `nv show router` | Shows router configuration, such as router policies, global BGP and OSPF configuration, PBR, PIM, IGMP, VRR, and VRRP configuration. |
| `nv show service` | Shows DHCP relays and server, NTP, PTP, LLDP, and syslog configuration. |
| `nv show system` | Shows global system settings, such as the reserved routing table range for PBR and the reserved VLAN range for layer 3 VNIs. You can also see system login messages and switch reboot history. |
| `nv show vrf` | Shows VRF configuration.|

The following example shows the `nv show router` commands after pressing the TAB key, then shows the output of the `nv show router bgp` command.

```
cumulus@leaf01:mgmt:~$ nv show router <<TAB>>
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
| `--applied`       | Shows configuration applied with the `nv config apply` command. For example, `nv show --applied interface bond1`. |
| `--color`         | Turns colored output on or off. For example, `nv show --color on interface bond1`|
| `--help`          | Shows `help` for the NVUE commands. |
| `--operational`   | Shows the running configuration (the actual system state). For example, `nv show --operational interface bond1` shows the running configuration for bond1. The running and applied configuration should be the same. If different, inspect the logs. |
| `--output`        | Shows command output in table format (auto), `json` format or `yaml` format. For example:<br>`nv show --output auto interface bond1`<br>`nv show --output json interface bond1`<br>`nv show --output yaml interface bond1` |
| `--paginate`      | Paginates the output. For example, `nv show --paginate on interface bond1`. |
| `--pending`       | Shows the last applied configuration and any pending set or unset configuration that you have not yet applied. For example, `nv show --pending interface bond1`.|
| `--rev <revision>`| Shows a detached pending configuration. See the `nv config detach` configuration management command below. For example, `nv show --rev 1`. |
| `--startup`  | Shows configuration saved with the `nv config save` command. This is the configuration after the switch boots. |
| `--view` | Shows these different views: brief, lldp, mac, pluggables, and small. This option is available for the `nv show interface` command only. For example, the `nv show interface --view=small` command shows a list of the interfaces on the switch and the `nv show interface --view=brief` command shows information about each interface on the switch, such as the interface type, speed, remote host and port. |

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

### Net Show commands

In addition to the `nv show` commands, Cumulus Linux continues to provide a subset of the NCLU `net show` commands. Use these commands to get additional views of various parts of your network configuration.

```
cumulus@leaf01:mgmt:~$ net show 
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
| `nv config apply` | Applies the pending configuration to become the applied configuration.<br>You can also use these prompt options:<ul><li>`--y` or `--assume-yes` to automatically reply `yes` to all prompts.</li><li>`--assume-no` to automatically reply `no` to all prompts.</li></ul> {{%notice note%}}Cumulus Linux applies but does not save the configuration; the configuration does not persist after a reboot.{{%/notice%}}You can also use these apply options:<br>`--confirm` applies the configuration change but you must confirm the applied configuration. If you do not confirm within ten minutes, the configuration rolls back automatically. You can change the default time with the apply `--confirm <time>` command. For example, `apply --confirm 60` requires you to confirm within one hour.<br>`--confirm-status` shows the amount of time left before the automatic rollback.|
| `nv config detach` | Detaches the configuration from the current pending configuration and uses an integer to identify it; for example, `4`. To list all the current detached pending configurations, run `nv config diff <<press Tab>`.|
| `nv config diff <revision> <revision>` | Shows differences between configurations, such as the pending configuration and the applied configuration or the detached configuration and the pending configuration.|
| `nv config history <revision>` | Shows the apply history for the revision. |
| `nv config patch <nvue-file>` | Updates the pending configuration with the specified YAML configuration file. |
| `nv config replace <nvue-file>` | Replaces the pending configuration with the specified YAML configuration file. |
| `nv config save` | Overwrites the startup configuration with the applied configuration by writing to the `/etc/nvue.d/startup.yaml` file. The configuration persists after a reboot. |
| `nv config show` | Shows the currently applied configuration in `yaml` format. |
| `nv config show -o commands` | Shows the currently applied configuration commands. |
| `nv config diff -o commands` | Shows differences between two configuration revisions. |

You can use the NVUE configuration management commands to back up and restore configuration when you upgrade Cumulus Linux on the switch. Refer to {{<link url="Upgrading-Cumulus-Linux/#back-up-configuration-with-nvue" text="Upgrading Cumulus Linux">}}.

### Action Commands

The NVUE action commands reset counters for interfaces and remove conflicts from protodown MLAG bonds.

| <div style="width:450px">Command | Description |
| ------- | ----------- |
|`nv action clear interface <interface> qos roce counters`  | Resets counters that the `nv show interface <interface> qos roce` command displays. |
|`nv action clear interface <interface> bond mlag lacp-conflict`| Removes duplicate partner MAC address or partner MAC address mismatch conflicts from protodown MLAG bonds.|

### List All NVUE Commands

To show the full list of NVUE commands, run `nv list-commands`. For example:

```
cumulus@switch:~$ nv list-commands
nv show platform
nv show platform capabilities
nv show platform hardware
nv show platform hardware component
nv show platform hardware component <component-id>
nv show platform hardware component <component-id> linecard
nv show platform hardware component <component-id> port
nv show platform hardware component <component-id> port <port-id>
nv show platform hardware component <component-id> port <port-id> breakout-mode
nv show platform hardware component <component-id> port <port-id> breakout-mode <mode-id>
nv show platform environment
nv show platform environment fan
nv show platform environment fan <fan-id>
nv show platform environment sensor
nv show platform environment sensor <sensor-id>
...
```

You can show the list of commands for a command grouping. For example, to show the list of interface commands:

```
cumulus@switch:~$ nv list-commands interface
nv show interface
nv show interface <interface-id>
nv show interface <interface-id> pluggable
nv show interface <interface-id> ip
nv show interface <interface-id> ip address
nv show interface <interface-id> ip address <ip-prefix-id>
nv show interface <interface-id> ip neighbor
nv show interface <interface-id> ip neighbor ipv4
nv show interface <interface-id> ip neighbor ipv4 <neighbor-id>
nv show interface <interface-id> ip neighbor ipv6
nv show interface <interface-id> ip neighbor ipv6 <neighbor-id>
...
```
<!-- vale off -->
Use the Tab key to get help for the command lists you want to see. For example, to show the list of command options available for the interface swp1, run:
<!-- vale on -->
```
cumulus@switch:~$ nv list-commands interface swp1 <<press Tab>>
acl            bridge         ip             lldp           ptp            router         tunnel
bond           evpn           link           pluggable      qos            storm-control  
```

## NVUE Configuration File

When you save network configuration using NVUE, Cumulus Linux writes the configuration to the `/etc/nvue.d/startup.yaml` file.

You can edit or replace the contents of the `/etc/nvue.d/startup.yaml` file. NVUE applies the configuration in the `/etc/nvue.d/startup.yaml` file during system boot only if the `nvue-startup.service` is running. If this service is not running, the switch reboots with the same configuration that is running before the reboot.

To start `nvue-startup.service`:

```
cumulus@switch:~$ sudo systemctl enable nvue-startup.service
cumulus@switch:~$ sudo systemctl start nvue-startup.service
```

When you apply a configuration with `nv config apply`, NVUE also writes to underlying Linux files such as `/etc/network/interfaces` and `/etc/frr/frr.conf`. You can view these configuration files; however NVIDIA recommends that you do not manually edit them while using NVUE. If you need to configure certain network settings manually or use automation such as Ansible to configure the switch, see {{<link title="#configure-nvue-to-ignore-linux-files" text="Configure NVUE to Ignore Linux Files">}} below.

<!--## OUT of 5.3-Maybe in 5.4? Search for a Specific Configuration

To search for a specific portion of the NVUE configuration, run the `nv config find <search string>` command. The search shows all items above and below the search string. For example, to search the entire NVUE object model configuration for any mention of `ptm`:

```
cumulus@switch:~$ nv config find ptm
- set:
    router:
      ptm:
        enable: off
```
-->
## Configure NVUE to Ignore Linux Files

You can configure NVUE to ignore certain underlying Linux files when applying configuration changes. For example, if you push certain configuration to the switch using Ansible and Jinja2 file templates or you want to use custom configuration for a particular service such as PTP, you can ensure that NVUE never writes to those configuration files.

The following example configures NVUE to ignore the Linux `/etc/ptp4l.conf` file when applying configuration changes and saves the configuration so it persists after a reboot.

```
cumulus@switch:~$ nv set system config apply ignore /etc/ptp4l.conf
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv config save
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
                      description                                                     package                version
--------------------- ----------------------------                                    --------------------   ------------
acpi                  displays information on ACPI devices                            acpi                   1.7-1.1                   
acpi-support-base     scripts for handling base ACPI events such as the power button  acpi-support-base      0.142-8
acpid                 Advanced Configuration and Power Interface event daemon         acpid                  1:2.0.31-1
adduser               add and remove users and groups                                 adduser                3.118
apt                   commandline package manager                                     apt                    1.8.2.3
arping                sends IP and/or ARP pings (to the MAC address)                  arping                 2.19-6
arptables             ARP table administration                                        arptables              0.0.4+snapshot20181021-4
atftp                 advanced TFTP client                                            atftp                  0.7.git20120829-3.               
atftpd                advanced TFTP server                                            atftpd                 0.7.git20120829-3.2~deb10u1 
auditd                User space tools for security auditing                          auditd                 1:2.8.4-3              
...
```

### Show Interface Configuration

The following example command shows the running, applied, and pending swp1 interface configuration.

```
cumulus@leaf01:~$ nv show interface swp1
                         operational  applied  description
-----------------------  -----------  -------  ----------------------------------------------------------------------
type                     swp                   The type of interface
ip
  [address]                                    ipv4 and ipv6 address
link
  mtu                    9216                  interface mtu
  state                  down                  The state of the interface
  stats
    carrier-transitions  3                     Number of times the interface state has transitioned between up and...
    in-bytes             300 Bytes             total number of bytes received on the interface
    in-drops             5                     number of received packets dropped
    in-errors            0                     number of received packets with errors
    in-pkts              5                     total number of packets received on the interface
    out-bytes            0 Bytes               total number of bytes transmitted out of the interface
    out-drops            0                     The number of outbound packets that were chosen to be discarded eve...
    out-errors           0                     The number of outbound packets that could not be transmitted becaus...
    out-pkts             0                     total number of packets transmitted out of the interface
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

To view differences between two detached pending configurations, run the `nv config diff` <<TAB>> command to list all the current detached pending configurations, then run the `nv config diff` command with the pending configurations you want to diff.

```
cumulus@switch:~$ nv config diff <<press Tab>>
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

{{%notice note%}}
A patch contains a single request to the NVUE service. Ordering of parameters within a patch is not guaranteed; NVUE does not support both unset and set commands for the same object in a single patch.
{{%/notice%}}

## NVUE and FRR Restart

NVUE restarts the FRR service when you:
- Change the `/etc/frr/daemons` file.
- Change the BGP ASN.
- Remove the default instance.
- Disable the SNMP server with `agentx` configured.

Restarting FRR restarts all the routing protocol daemons that you enable and that are running, which might impact traffic.
