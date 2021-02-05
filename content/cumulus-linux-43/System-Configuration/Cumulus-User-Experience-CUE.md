---
title: Cumulus User Experience - CUE
author: NVIDIA
weight: 115
toc: 3
---
{{%notice warning%}}
Cumulus User Experience (CUE) is an {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined/" text="early access feature">}} and is open BETA, seeking customer and real world feedback. CUE is not currently intended to run in production and is not supported through NVIDIA networking support.
{{%/notice%}}

CUE is currently available for evaluation. Your feedback is welcome and appreciated as we start to roll out the new Cumulus Linux CLI. You can provide feedback by sending an email to net-cl-cue-ea-feedback@nvidia.com.

## What is CUE?

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
- Configuration (`cl set` and ` cl unset`)
- Monitoring (`cl show`)
- Configuration management (`cl config`).

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
cl set interface <interface-id> ...

Description:
  Interfaces

Identifiers:
  <interface-id>    Interface

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

The `cl set` and `cl unset` commands are grouped into the following categories. Each command group includes subcommands. Use command completion (Tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `cl set router`<br>`cl unset router` | Configures router policies, such as prefix list rules and route maps, and global BGP options. This is where you enable and disable BGP, set the ASN, set the router ID, and configure BGP graceful restart and shutdown. |
| `cl set platform`<br>`cl unset platform` | Configures hostname options, such as the static hostname for the switch, the local domain, and whether DHCP is allowed to override the hostname. You can also set how configuration apply operations are performed (specify which files to ignore and which files to overwrite). |
| `cl set bridge`<br>`cl unset bridge` | Configures a bridge domain. This is where you configure the bridge type (VLAN-aware), 802.1Q encapsulation, the STP state and priority, and the VLANs in the bridge domain. |
| `cl set mlag`<br>`cl unset mlag` | Configures MLAG. This is where you configure the backup IP address or interface, MLAG system MAC address, peer IP address, MLAG priority, and the delay before bonds are brought up. |
| `cl set evpn`<br>`cl unset evpn` | Configures EVPN. This is where you enable and disable the EVPN control plane, and set EVPN route advertise options, default gateway configuration for centralized routing, and duplicate address detection options. |
| `cl set interface <interface-id>`<br>`cl unset interface <interface-id>` | Configures the switch interfaces. Use this command to configure bond interfaces, bridge interfaces, interface IP addresses, VLAN IDs, and links (MTU, FEC, speed, duplex, and so on).|
| `cl set system`<br>`cl unset system` | Configures global system settings, such as NTP, DHCP servers, DNS, LLDP, and syslog. |
| `cl set vrf  <vrf-id>`<br>`cl unset vrf <vrf-id>` | Configures VRFs. |
| `cl set nve`<br>`cl unset nve` | Configures network virtualization (VXLAN) settings. This is where you configure the UDP port for VXLAN frames, control dynamic MAC learning over VXLAN tunnels, and configure how Cumulus Linux handles BUM traffic in the overlay.|

### Monitoring Commands

The CUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration, or only interface configuration. The monitoring commands are grouped into the following categories. Each command group includes subcommands. Use command completion (Tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `cl show router` | Shows router information, such as router policies and global BGP configuration. |
| `cl show platform` | Shows platform information, such as hardware and software components, and the hostname of the switch. |
| `cl show bridge` | Shows bridge domain information.|
| `cl show mlag` | Shows MLAG information. |
| `cl show evpn` |Shows EVPN information. |
| `cl show interface` |Shows interface information. |
| `cl show system` | Shows global system settings, such as NTP, DHCP server, DNS, syslog and LLDP. |
| `cl show vrf` | Shows VRF information.|
| `cl show nve` | Shows network virtualization information, such as VXLAN-specfic MLAG configuration and VXLAN flooding.|

The following example shows the `cl show system commands` after pressing the TAB key, then shows the output of the `cl show system lldp` command.

```
cumulus@switch:~$  cl show system <<press Tab>>
dhcp-server   dns           lldp          syslog
dhcp-server6  global        ntp
cumulus@switch:~$  cl show system lldp
                    running  applied  pending  description
------------------  -------  -------  -------  ----------------------------------------------------------------------
dot1-tlv            off      off      off      Enable dot1 TLV advertisements on enabled ports
tx-hold-multiplier  4        4        4        < TTL of transmitted packets is calculated by multiplying the tx-in...
tx-interval         30       30       30       change transmit delay
cumulus@switch:~$ 
```

{{%notice note%}}
If there are no pending or applied configuration changes, the `cl show system` command only shows the running configuration.
{{%/notice%}}

*Revision* options are available for the `cl show` commands. You can choose the configuration you want to show (pending, applied, startup, or running):

| <div style="width:200px">Option | Description |
| ------ | ----------- |
| `--rev <revision>` | Shows a detached pending configuration. See the `cl config detach` configuration management command below.  |
| `--pending`       |  Shows the configuration you `set` and `unset` but have not yet applied or saved.|
| `--applied`       |  Shows the last set of commands applied with the `cl config apply` command. |
| `--startup`       |  Shows the set of commands saved with the `cl config save` command. This will be the configuration after the switch boots. |
| `--running`       |  Shows the running configuration (the actual system state). The running and applied configuration should be the same. If different, inspect the logs. |

The following example shows *pending* BGP graceful restart configuration:

```
cumulus@switch:~$ cl show router bgp graceful-restart --pending
                             pending_20210128_212626_4WSY  description
----------------------------  ----------------------------  ----------------------------------------------------------------------
mode                          helper-only                   Role of router during graceful restart. helper-only, router is in h...
path-selection-deferral-time  360                           Used by the restarter as an upper-bounds for waiting for peeringes...
restart-time                  120                           Amount of time taken to restart by router. It is advertised to the...
stale-routes-time             360                           Specifies an upper-bounds on how long we retain routes from a resta...
```

### Configuration Management Commands

The CUE configuration management commands manage and apply configurations.

| <div style="width:450px">Command | Description |
| ------- | ----------- |
| `cl config apply` | Applies the pending configuration to become the applied configuration.<br>You can also use these prompt options:<ul><li>`--y` or `--assume-yes` to automatically reply `yes` to all prompts.</li><li>`--assume-no` to automatically reply `no` to all prompts.</li></ul> {{%notice note%}}The configuration is applied but not saved and does not persist after a reboot.{{%/notice%}}|
| `cl config detach` | Detaches the configuration from the current pending revision. The detached revision is called `pending` and includes a timestamp with extra characters. For example: `pending_20210128_212626_4WSY`|
| `cl config diff <revision> <revision>` | Shows differences between configurations, such as the pending configuration and the applied configuration or the detached configuration and the pending configuration.|
| `cl config patch <cue-file>` | Updates the pending configuration with a configuration YAML file. |
| `cl config replace <cue-file>` | Replaces the pending configuration with the specified configuration YAML file. |
| `cl config save` | Overwrites the startup configuration with the applied configuration by writing to the `/etc/cued file`. The configuration persists after a reboot. |

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

Use the Tab key to get help for the command lists you want to see. For example, to show the list of command options available for the interface swp1, run:

```
cumulus@switch:~$ cl list-commands interface swp1 <<press Tab>>
bond    bridge  ip      link
cumulus@switch:~$ cl list-commands interface swp1 bond
l show interface <interface-id> bond
cl show interface <interface-id> bond member
cl show interface <interface-id> bond member <member-id>
cl show interface <interface-id> bond mlag
cl set interface <interface-id> bond
cl set interface <interface-id> bond member <member-id>
cl set interface <interface-id> bond mlag
cl set interface <interface-id> bond mlag id (1-65535|auto)
cl set interface <interface-id> bond down-delay 0-65535
cl set interface <interface-id> bond lacp-bypass (on|off)
cl set interface <interface-id> bond lacp-rate (fast|slow)
cl set interface <interface-id> bond mode (lacp|static)
cl set interface <interface-id> bond up-delay 0-65535
cl unset interface <interface-id> bond
cl unset interface <interface-id> bond member
cl unset interface <interface-id> bond member <member-id>
cl unset interface <interface-id> bond mlag
cl unset interface <interface-id> bond mlag id
cl unset interface <interface-id> bond down-delay
cl unset interface <interface-id> bond lacp-bypass
cl unset interface <interface-id> bond lacp-rate
cl unset interface <interface-id> bond mode
cl unset interface <interface-id> bond up-delay
```

## Example Configuration Commands

This section provides some examples of how to configure a Cumulus Linux switch using CUE commands.

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
cumulus@switch:~$ cl config apply
```

### Configure an Interface

The following commands brings up swp1.

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

## How is CUE Different from NCLU?

This section lists some of the differences between CUE and the NCLU command line interface to help you navigate configuration.

### Configuration File

When you **save** network configuration using CUE, the configuration is written to the `/etc/cue.d/startup.yaml` file. Nvidia recommends that you do not edit this file.

Cumulus Linux also writes to the `/etc/network/interfaces` and `/etc/frr/frr.conf` files when you apply a configuration. You can view these configuration files; however Nvidia recommends that you do not manually edit them while using CUE.

## Bridge Configuration

You set global bridge configuration on the bridge domain. For example:

```
cumulus@leaf01:~$ cl set bridge domain br_default vlan 100,200
```

However, you set specific bridge interface options with interface commands. For example:

```
cumulus@leaf01:~$ cl set interface swp1 bridge domain br_default learning on
```

The default vlan-aware bridge in CUE is `br_default`. The default vlan-aware bridge in NCLU is `bridge`.

## BGP Configuration

You can set global BGP configuration, such as the ASN, router ID, graceful shutdown and restart with the `cl set router bgp` command. For example:

```
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
```

However, bgp peer and peer group, route information, timer, and address family configuration requires a VRF. For example:

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 remote-as external
```
