---
title: Cumulus User Experience - CUE
author: NVIDIA
weight: 115
toc: 3
---
{{%notice warning%}}
Cumulus User Experience (CUE) is an {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined/" text="early access feature">}}.
{{%/notice%}}

CUE is a command line interface for Cumulus Linux. Embracing the power of open networking, CUE brings an entirely new interface to Cumulus Linux based on modern operating principles and schema oriented YANG based models.

The CUE object model is structured as a *big tree* that represents the entire state of a Cumulus Linux instance. At the base of the tree are high level branches such as *router* and *interface*. Under each of these branches are further branches.  As you navigate through the tree, you gain a more specific context. At the leaves of the tree are actual attributes, represented as key/value pairs. The path through the tree is implemented as through a filesystem.

## Install CUE

CUE is not installed by default on Cumulus Linux. To install CUE, follow the procedure below.

{{%notice info%}}
Installing CUE disables NCLU; after installation you will no longer have access to the NCLU CLI.
{{%/notice%}}

1. Stop then disable the `netd` service:

   ```
   cumulus@switch:~$ systemctl stop netd
   cumulus@switch:~$ systemctl disable netd
   ```

3. Update the local cache listing of available packages, then install the CUE package:

   ```
   cumulus@switch:~$ sudo -E apt-get update
   cumulus@switch:~$ sudo -E apt-get install python3-cue
   ```

4. Enable then start the CUE service:

   ```
   cumulus@switch:~$ systemctl enable cued
   cumulus@switch:~$ systemctl start cued
   ```

## Command Line Basics

The CUE command line has a flat structure as opposed to a modal structure. This means that you can run all commands from the primary prompt instead of only in a specific mode.

### Command Syntax

CUE commands all begin with `cl` and fall into one of three syntax categories:
- Configuration (`set` and `unset`)
- Monitoring (`show`)
- Configuration management (`config`).

The commands include attributes and options. Attributes (`<attributes>`) specify configuration and show settings. Options `[options]` are either general options that provide help for a command (`-h` or `--help`) or revision options that let you specify where to apply or show the configuration. If you do not specify a revision option, the command is applied to the running configuration. For a description of the revision options, see {{<link url="#revision-options" text="Revision Options">}} below.

```
cumulus@switch:~$ cl set [options] <attribute>
cumulus@switch:~$ cl unset [options] <attribute>
cumulus@switch:~$ cl show [options] <attribute>
cumulus@switch:~$ cl config <command> [options]
```

### Command Completion

As you enter commands, you can get help with the valid keywords or options using the Tab key. For example, using Tab completion with `cl set` displays the possible objects for the command, and returns you to the command prompt to complete the command.

```
cumulus@switch:~$ cl set <<press Tab>>
bridge     interface  nve        router     vrf
evpn       mlag       platform   system

cumulus@switch:~$ cl set
```

### Command Help

As you enter commands, you can get help with command syntax by entering `-h` or `--help` at various points within a command entry. For example, to find out what options are available for `cl set interface`, enter `cl set interface -h` or `cl set interface --help`.

```
cumulus@switch:~$ cl set interface -h
Usage:
cl set interface [options] <interface-id> ...

Description:
  Interfaces

Identifiers:
  <interface-id>    Interface

Revision Options:
  --rev <revision>  The revision id to operate on
  --pending         Alias of '--rev=pending'
  --applied         Alias of '--rev=applied'
  --startup         Alias of '--rev=startup'
  --running         Alias of '--rev=running'

General Options:
  -h, --help        Show help.
```

### Command History

The CUE CLI stores commands issued within a session, which enables you to review and rerun commands. At the command prompt, press the Up Arrow and Down Arrow keys to move back and forth through the list of commands previously entered. When you find a given command, you can run the command by pressing Enter. Optionally, you can modify the command before you run it.

## Command Categories

The CLI has a flat structure; however, the commands are conceptually grouped into three functional categories:

- Configuration
- Monitoring
- Configuration Management

### Configuration Commands

The CUE configuration commands modify switch configuration. You can set and unset configuration options.

The `cl set` and `cl unset` commands are grouped into the following categories. Each command group includes subcommands.

| <div style="width:450px">Command Category | Description |
| ------- | ----------- |
| `cl set router [options] [<attribute> ...]`<br>`cl unset router [options] [<attribute> ...]` | Configures router policies, such as prefix list rules and route maps, and global BGP options. This is where you enable and disable BGP, set the ASN, set the router ID, and configure BGP graceful restart and shutdown. |
| `cl set platform [options] [<attribute> ...]`<br>`cl unset platform [options] [<attribute> ...]` | Configures hostname options, such as the static hostname for the switch, the local domain, and whether DHCP is allowed to overrride the hostname. You can also set how configuration apply operations are performed (specify which files to ignore and which files to overwrite). |
| `cl set bridge [options] [<attribute> ...]`<br>`cl unset bridge [options] [<attribute> ...]` | Configures a bridge domain. This is where you configure the bridge type (VLAN-aware), 802.1Q encapsulation, the STP state and priority on the bridge, and the VLANs in the bridge domain. |
| `cl set mlag [options] [<attribute> ...]`<br>`cl unset mlag [options] [<attribute> ...]` | Configures MLAG. This is where you configure the backup IP address or interface, MLAG system MAC address, peer IP address, MLAG priority, and the delay before bonds are brought up. |
| `cl set evpn [options] [<attribute> ...]`<br>`cl unset evpn [options] [<attribute> ...]` | Configures EVPN. This is where you  enable and disable the EVPN control plane, and set EVPN route advertise options, default gateway configuration for centralized routing, and duplicate address detection options. |
| `cl set interface [options] <interface-id> ...`<br>`cl unset interface [options] <interface-id> ...` | Configures the switch interfaces. Use this command to configure bond interfaces, bridge interfaces, interface IP addresses, VLAN IDs, and links (MTU, FEC, speed, duplex, and so on).|
| `cl set system [options] [<attribute> ...]`<br>`cl unset system [options] [<attribute> ...]` | Configures global system settings, such as NTP, DHCP server, DNS, LLDP, and syslog. |
| `cl set vrf [options] <vrf-id> ...`<br>`cl unset vrf [options] <vrf-id> ...` | Configures VRFs. |
| `cl set nve [options] [<attribute> ...]`<br>`cl unset nve [options] [<attribute> ...]` | Configures network virtualization (VXLAN) settings. This is where you configure the UDP port for VXLAN frames, control dynamic MAC learning over VXLAN tunnels, and configure how Cumulus Linux handles BUM traffic in the overlay.|

### Monitoring Commands

The CUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration, or bridge, interface, VRF, MLAG, BGP or EVPN configuration. The monitoring commands are grouped into the following categories. Each command group includes subcommands.

| <div style="width:450px">Command | Description |
| ------- | ----------- |
| `cl show router [options] [<attribute> ...]` | Shows router information, such as router policies and BGP. |
| `cl show platform [options] [<attribute> ...]` | Shows platform information, such as hardware and software components, and the hostname of the switch. |
| `cl show bridge [options] [<attribute> ...]` | Shows bridge information.|
| `cl show mlag [options] [<attribute> ...]` | Shows MLAG information. |
| `cl show evpn [options] [<attribute> ...]` |Shows EVPN information. |
| `cl show interface [options] [<interface-id> ...]` |Shows interface information. |
| `cl show system [options] [<attribute> ...]` | Shows global system settings, such as NTP, DHCP server, DNS, syslog and LLDP. |
| `cl show vrf [options] [<vrf-id> ...]` | Shows VRF information.|
| `cl show nve [options] [<attribute> ...]` | Shows network virtualization information, such as VXLAN-specfic MLAG configuration and VXLAN flooding.|

### Configuration Management Commands

The CUE configuration management commands manage and apply configurations.

| <div style="width:450px">Command | Description |
| ------- | ----------- |
| `cl config apply [options] [<revision>]` | Applies the running configuration.<br> You can specify the revision you want to apply to the running configuration. If no revision is specified, the pending configuration is applied to the running configuration.<br>You can also use these prompt options:<ul><li>`--y` or `--assume-yes` to automatically reply `yes` to all prompts.</li><li>`--assume-no` to automatically reply `no` to all prompts.</li></ul> {{%notice note%}}The configuration is applied but not saved and does not persist after a reboot.{{%/notice%}}|
| `cl config save [options]` | Overwrites the startup configuration with the applied revision. The configuration persists after a reboot. |
| `cl config replace [options] <cue-file>` | Replaces the pending configuration with the specified configuration YAML file. |
| `cl config detach [options]` | Detaches the configuration from the current pending revision. |
| `cl config diff [options] [(<revision>|--empty)] [<revision>]` | Shows differences between two configuration revisions. |
| `cl config patch [options] <cue-file>` | Updates the pending revision with a configuration YAML file. |

## Options

The CUE commands include general options and revision options.

The general options `-h` or `--help` provide help for the commands.

The revision options enable you to .......

| Option | Description |
| ------ | ----------- |
| `--rev <revision>` |  Applies the set or unset command to the revision ID you specify. |
|  `--pending`       |  Applies the set or unset command to one or more configurations that are awaiting to be applied.|
|  `--applied`       |  Applies the set or unset command to the applied revision. |
|  `--startup`       |  Applies the set or unset command to the startup revision. The new configuration will run when you restart the switch. |
|  `--running`       |  Applies the set or unset command to the running revision (the actual system state).  |

## List all CUE Commands

To show the full list of CUE commands, run `cl list-commands`. For example:

```
cumulus@switch:~$ cl list-commands
...
cl show interface <interface-id> link lldp neighbor
cl show interface <interface-id> link lldp neighbor <neighbor-id>
cl show interface <interface-id> link lldp neighbor <neighbor-id> bridge
cl show interface <interface-id> link lldp neighbor <neighbor-id> bridge vlan
cl show interface <interface-id> link lldp neighbor <neighbor-id> bridge vlan <vid>
cl show interface <interface-id> link stats
cl show system
cl show system global
cl show system ntp
cl show system ntp server
cl show system ntp server <server-id>
cl show system ntp pool
cl show system ntp pool <server-id>
cl show system dhcp-server
...
```

You can show the list of commands for a command grouping and for subcommands. For example, to show the list of interface commands:

```
cumulus@switch:~$ cl list-commands interface
cl show interface
cl show interface <interface-id>
cl show interface <interface-id> bond
cl show interface <interface-id> bond member
cl show interface <interface-id> bond member <member-id>
cl show interface <interface-id> bond mlag
cl show interface <interface-id> bridge
cl show interface <interface-id> bridge domain
cl show interface <interface-id> bridge domain <domain-id>
cl show interface <interface-id> bridge domain <domain-id> stp
cl show interface <interface-id> bridge domain <domain-id> vlan
cl show interface <interface-id> bridge domain <domain-id> vlan <vid>
cl show interface <interface-id> ip
...
```

Use the Tab key to get help the command lists you want to see. For example, to show the list of commands available for the interface swp1, run:

```
cumulus@switch:~$ cl list-commands interface swp1 <<press Tab>>
bond    bridge  ip      link
cumulus@switch:~$ cl list-commands interface swp1
```

## Example CUE Commands

This section provides examples of how to configure a Cumulus Linux switch using CUE commands.

### Configure the System Hostname

The example below shows the CUE commands required to change the hostname for the switch to leaf01:

```
cumulus@switch:~$ cl set platform hostname value leaf01
cumulus@switch:~$ cl config apply
```

### Configure the System DNS Server

The example below shows the CUE commands required to define the DNS server for the switch:

```
cumulus@switch:~$ cl set system dns server 192.168.200.1
```

### Configure an Interface

The following commands brings up swp1 in the running configuration.

```
cumulus@switch:~$ cl set interface swp1 link state up
cumulus@switch:~$ cl config apply 
```

### Configure a Bond

The example below shows the CUE commands required to configure the front panel port interfaces swp1 thru swp4 to be slaves in bond0.

```
cumulus@switch:~$ cl set interface bond0 bond member swp1-4
cumulus@switch:~$ cl config apply
```

### Configure a Bridge

The example below shows the CUE commands required to create a VLAN-aware bridge that contains two switch ports and includes 3 VLANs; tagged VLANs 100 and 200 and an untagged (native) VLAN of 1.

With CUE, there is a default bridge called `br_default`, which has no ports assigned to it. The example below configures this default bridge.

```
cumulus@switch:~$ cl set interface swp1-2 bridge domain br_default
cumulus@switch:~$ cl set bridge domain br_default vlan 100,200
cumulus@switch:~$ cl set bridge domain br_default untagged 1
cumulus@switch:~$ cl config apply
```

### Configure MLAG

The following commands configure MLAG on leaf01. The CUE commands:
- Places swp1 into bond1 and swp2 into bond2.
- Configure the MLAG ID to 1 for bond1 and to 2 for bond2.
- Add the bond1 and bond2 to the default bridge (br_default).
- Creates the inter-chassis bond (swp49 and swp50) and the peer link (peerlink)
- Sets the peer link IP address to linklocal, the MLAG system MAC address to 44:38:39:BE:EF:AA, and the backup interface to 10.10.10.2.

```
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf01:~$ cl set interface bond2 bond mlag id 2
cumulus@switch:~$ cl set interface bond1-2 bridge domain br_default 
cumulus@leaf01:~$ cl set interface swp49-50 type peerlink
cumulus@leaf01:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set mlag backup 10.10.10.2
cumulus@leaf01:~$ cl set mlag peer-ip linklocal
cumulus@leaf01:~$ cl config apply
```

### Configure BGP Unnumbered

The following commands configure BGP unnumbered on leaf01. The CUE commands:
- Assign the ASN for this BGP node to 65101.
- Set the router ID to 10.10.10.1.
- Distribute routing information to the peer on swp51.
- Originate prefixes 10.10.10.1/32 from this BGP node.

```
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32
cumulus@leaf01:~$ cl config apply
```

## How is CUE Different from NCLU

DESCRIBE THE MAIN DIFFERENCES THAT MIGHT TRIP YOU UP
