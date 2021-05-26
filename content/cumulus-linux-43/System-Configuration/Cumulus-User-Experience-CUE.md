---
title: Cumulus User Experience - CUE
author: NVIDIA
weight: 115
toc: 3
---
{{%notice warning%}}
Cumulus User Experience (CUE) is an [early access feature]({{<ref "/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined" >}}) currently in ALPHA and open to customer feedback.

CUE is not currently intended to run in production and is not supported through NVIDIA networking support.
{{%/notice%}}
<!-- vale off -->
Your evaluation is welcome and appreciated as we start to roll out this new Cumulus Linux CLI. You can provide feedback by sending an email to net-cl-cue-ea-feedback@nvidia.com.
<!-- vale on -->
## What is CUE?

CUE is an object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) providing a robust API that allows for multiple interfaces to both view (show) and configure (set and unset) any element within a system running the CUE software. The CUE CLI and the REST API leverage the same API to interface with Cumulus Linux.

CUE follows a declarative model, removing context-specific commands and settings. It is structured as a *big tree* that represents the entire state of a Cumulus Linux instance. At the base of the tree are high level branches representing objects, such as *router* and *interface*. Under each of these branches are further branches. As you navigate through the tree, you gain a more specific context. At the leaves of the tree are actual attributes, represented as key/value pairs. The path through the tree is similar to a filesystem path.

{{<img src = "/images/cumulus-linux/cue-architecture.png">}}

In this ALPHA release of CUE, you have full access to the new CLI, which leverages the underlying CUE API. Future releases will provide access to the API through REST, Python and more.

This documentation describes how to access CUE and navigate the CUE CLI to configure and monitor Cumulus Linux.

## Install CUE

CUE is not installed by default on Cumulus Linux. To install CUE, follow the procedure below.

{{%notice info%}}
Do not install CUE in a production environment.
{{%/notice%}}

1. Stop then disable the `netd` service:

   ```
   cumulus@switch:~$ sudo systemctl stop netd
   cumulus@switch:~$ sudo systemctl disable netd
   ```

3. Update the local cache listing of available packages, then install the CUE package:

   ```
   cumulus@switch:~$ sudo -E apt-get update
   cumulus@switch:~$ sudo -E apt-get install python3-cue
   ```

4. Enable then start the CUE service:

   ```
   cumulus@switch:~$ sudo systemctl enable cued
   cumulus@switch:~$ sudo systemctl start cued
   ```

5. Log out of the switch, then log back in to get the CUE CLI prompt.

<!--## Launch the CUE Simulation in Cumulus in the Cloud

CUE evaluation is available in Cumulus in the Cloud (CITC); a virtual data center network with all of the features and functionality of Cumulus Linux running on real networking hardware.

To start your CUE similation in CITC:

1. Go to {{<exlink url="https://www.nvidia.com/en-us/networking/network-simulation/Cumulus" text="CUE" >}} NEED REAL LINK HERE.

2. On the dashboard, click the CUE simulation link under Simulations.

   GRAPHIC

   The simulation consists of six leaf switches, four spine switches, 8 Ubuntu servers, two *firewall* devices to isolate tenants, and a complete out of band management networking.

3. On the topology graphic, click the `oob-server` to open a terminal window, then ssh to leaf01.

   GRAPHIC

You are now on the leaf01 switch and can explore the CUE CLI by entering commands. The CUE CLI is described below.-->

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

### Command List

You can list all the CUE commands by running `cl list-commands`. See {{<link url="#list-all-cue-commands" text="List All CUE Commands">}} below.

### Command History

At the command prompt, press the Up Arrow and Down Arrow keys to move back and forth through the list of commands previously entered. When you find a given command, you can run the command by pressing Enter. Optionally, you can modify the command before you run it.

## Command Categories

The CUE CLI has a flat structure; however, the commands are conceptually grouped into three functional categories:

- Configuration
- Monitoring
- Configuration Management

### Configuration Commands

The CUE configuration commands modify switch configuration. You can set and unset configuration options.

The `cl set` and `cl unset` commands are grouped into the following categories. Each command group includes arguments. Use command completion (Tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `cl set router`<br>`cl unset router` | Configures router policies, such as prefix list rules and route maps, and global BGP options. This is where you enable and disable BGP, set the ASN and the router ID, and configure BGP graceful restart and shutdown. |
| `cl set platform`<br>`cl unset platform` | Configures hostname options, such as the static hostname for the switch, the local domain, and whether DHCP is allowed to override the hostname. You can also set how configuration apply operations are performed (such as which files to ignore and which files to overwrite). |
| `cl set bridge`<br>`cl unset bridge` | Configures a bridge domain. This is where you configure the bridge type (such as VLAN-aware), 802.1Q encapsulation, the STP state and priority, and the VLANs in the bridge domain. |
| `cl set mlag`<br>`cl unset mlag` | Configures MLAG. This is where you configure the backup IP address or interface, MLAG system MAC address, peer IP address, MLAG priority, and the delay before bonds are brought up. |
| `cl set evpn`<br>`cl unset evpn` | Configures EVPN. This is where you enable and disable the EVPN control plane, and set EVPN route advertise options, default gateway configuration for centralized routing, and duplicate address detection options. |
| `cl set interface <interface-id>`<br>`cl unset interface <interface-id>` | Configures the switch interfaces. Use this command to configure bond interfaces, bridge interfaces, interface IP addresses, VLAN IDs, and links (MTU, FEC, speed, duplex, and so on).|
| `cl set system`<br>`cl unset system` | Configures global system settings, such as NTP, DHCP servers, DNS, LLDP, and syslog. |
| `cl set vrf  <vrf-id>`<br>`cl unset vrf <vrf-id>` | Configures VRFs. This is where you configure VRF-level router configuration such as BGP, including BGP for the default VRF. |
| `cl set service`<br>`cl unset service` | Configures DHCP relays. This is where you configure the DHCP relay server IP address, the set of interfaces on which to handle DHCP relay traffic, the DHCP relay gateway IP address on the interfaces, and the source IP address to use on the relayed packet. |
| `cl set nve`<br>`cl unset nve` | Configures network virtualization (VXLAN) settings. This is where you configure the UDP port for VXLAN frames, control dynamic MAC learning over VXLAN tunnels, and configure how Cumulus Linux handles BUM traffic in the overlay.|

### Monitoring Commands

The CUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration or only interface configuration. The monitoring commands are grouped into the following categories. Each command group includes subcommands. Use command completion (Tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `cl show router` | Shows router configuration, such as router policies and global BGP configuration. |
| `cl show platform` | Shows platform configuration, such as hardware and software components, and the hostname of the switch. |
| `cl show bridge` | Shows bridge domain configuration.|
| `cl show mlag` | Shows MLAG configuration. |
| `cl show evpn` |Shows EVPN configuration. |
| `cl show interface` |Shows interface configuration. |
| `cl show system` | Shows global system settings, such as NTP, DHCP server, DNS, syslog and LLDP. |
| `cl show service` | Shows DHCP relay configuration, such as the DHCP relay server IP address, the set of interfaces on which DHCP relay traffic is handled, and the DHCP relay gateway IP address on the interfaces. |
| `cl show vrf` | Shows VRF configuration.|
| `cl show nve` | Shows network virtualization configuration, such as VXLAN-specfic MLAG configuration and VXLAN flooding.|

The following example shows the `cl show router` commands after pressing the TAB key, then shows the output of the `cl show router bgp` command.

```
cumulus@leaf01:mgmt:~$ cl show router <<press Tab>>
bgp     policy
cumulus@leaf01:mgmt:~$ cl show router bgp
                                running  applied      pending      description
------------------------------  -------  -----------  -----------  ----------------------------------------------------------------------
enable                                   on                        Turn the feature 'on' or 'off'.  The default is 'off'.
autonomous-system                        65101                     ASN for all VRFs, if a single AS is in use.  If "none", then ASN mu...
graceful-shutdown                        off                       Graceful shutdown enable will initiate the GSHUT community to be an...
policy-update-timer                      5                         Wait time in seconds before processing updates to policies to ensur...
router-id                                10.10.10.1                BGP router-id for all VRFs, if a common one is used.  If "none", th...
convergence-wait
  establish-wait-time                    0                         Maximum time to wait to establish BGP sessions. Any peerswhich do...
  time                                   0                         Time to wait for peers to send end-of-RIB before router performs pa...
graceful-restart
  mode                                   helper-only               Role of router during graceful restart. helper-only, router is in h...
  path-selection-deferral-time           360                       Used by the restarter as an upper-bounds for waiting for peering es...
  restart-time                           120                       Amount of time taken to restart by router. It is advertised to the...
  stale-routes-time                      360                       Specifies an upper-bounds on how long we retain routes from a ....
```

{{%notice note%}}
If there are no pending or applied configuration changes, the `cl show` command only shows the running configuration.
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
| `cl config detach` | Detaches the configuration from the current pending configuration. The detached configuration is called `pending` and includes a timestamp with extra characters. For example: `pending_20210128_212626_4WSY`|
| `cl config diff <revision> <revision>` | Shows differences between configurations, such as the pending configuration and the applied configuration or the detached configuration and the pending configuration.|
| `cl config patch <cue-file>` | Updates the pending configuration with the specified YAML configuration file. |
| `cl config replace <cue-file>` | Replaces the pending configuration with the specified YAML configuration file. |
| `cl config save` | Overwrites the startup configuration with the applied configuration by writing to the `/etc/cue.d/startup.yaml` file. The configuration persists after a reboot. |

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
cl show interface <interface-id> bond
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
cumulus@switch:~$ cl config apply
```

### Configure an Interface

The example below shows the CUE commands required to bring up swp1.

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

The example below shows the CUE commands required to create a VLAN-aware bridge that contains two switch ports (swp1 and swp2) and includes 3 VLANs; tagged VLANs 10 and 20 and an untagged (native) VLAN of 1.

With CUE, there is a default bridge called `br_default`, which has no ports assigned to it. The example below configures this default bridge.

```
cumulus@switch:~$ cl set interface swp1-2 bridge domain br_default
cumulus@switch:~$ cl set bridge domain br_default vlan 10,20
cumulus@switch:~$ cl set bridge domain br_default untagged 1
cumulus@switch:~$ cl config apply
```

### Configure MLAG

The example below shows the CUE commands required to configure MLAG on leaf01. The commands:
- Place swp1 into bond1 and swp2 into bond2.
- Configure the MLAG ID to 1 for bond1 and to 2 for bond2.
- Add bond1 and bond2 to the default bridge (br_default).
- Create the inter-chassis bond (swp49 and swp50) and the peer link (peerlink)
- Set the peer link IP address to linklocal, the MLAG system MAC address to 44:38:39:BE:EF:AA, and the backup interface to 10.10.10.2.

```
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf01:~$ cl set interface bond2 bond mlag id 2
cumulus@switch:~$ cl set interface bond1-2 bridge domain br_default 
cumulus@leaf01:~$ cl set interface peerlink bond member swp49-50
cumulus@leaf01:~$ cl set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set mlag backup 10.10.10.2
cumulus@leaf01:~$ cl set mlag peer-ip linklocal
cumulus@leaf01:~$ cl config apply
```

### Configure BGP Unnumbered

The example below shows the CUE commands required to configure BGP unnumbered on leaf01. The commands:
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

## Example Monitoring Commands

This section provides monitoring command examples.

### Show Installed Software

The following example command lists the software installed on the switch:

```
cumulus@switch:~$ cl show platform software
             running                                applied  description
-----------  -------------------------------------  -------  --------------------------
[installed]  acpi                                            List of installed software
[installed]  acpi-support-base
[installed]  acpid
[installed]  adduser
[installed]  apt
[installed]  arping
[installed]  arptables
[installed]  auditd
[installed]  base-files
[installed]  base-passwd
[installed]  bash
[installed]  bash-completion
[installed]  bind9-host
[installed]  binutils
[installed]  binutils-common
[installed]  binutils-x86-64-linux-gnu
...
```

### Show Interface Configuration

The following example command shows the running and applied swp1 interface configuration. There is no pending configuration.

```
cumulus@leaf01:~$ cl show interface swp1
                        running     applied      description
-----------------------  ----------  -----------  ----------------------------------------------------------------------
type                     swp         swp          The type of interface
bridge
  [domain]               br_default  br_default   Bridge domains on this interface
  [domain]                           bridge
ip
  vrf                                default      Virtual routing and forwarding
  ipv4                               forward      IPv4 support on the interface. A value of 'on' means IPv4 is enable...
  ipv6                               forward      IPv6 support on the interface. A value of 'on' means IPv6 is enable...
  [address]                          10.1.1.1/30  ipv4 and ipv6 address
link
  auto-negotiate                     on           Link speed and characteritic auto negotiation
  breakout                           1x           sub-divide, aggregate, or disable ports (only valid on plug interfa...
  duplex                             full         Link duplex
  fec                                auto         Link forward error correction mechanism
  mtu                    9216        9216         interface mtu
  speed                              auto         Link speed
  dot1x
    mab                              off          bypass MAC authentication
    parking-vlan                     off          VLAN for unauthorized MAC addresses
  state                  down        up           The state of the interface
  stats
    carrier-transitions  3                        Number of times the interface state has transitioned between up and...
    in-bytes             0                        total number of bytes received on the interface
    in-drops             0                        number of received packets dropped
    in-errors            0                        number of received packets with errors
    in-pkts              0                        total number of packets received on the interface
    out-bytes            65700                    total number of bytes transmitted out of the interface
    out-drops            0                        The number of outbound packets that were chosen to be discarded eve...
    out-errors           0                        The number of outbound packets that could not be transmitted becaus...
    out-pkts             934                      total number of packets transmitted out of the interface
```

## Example Configuration Management Commands

This section provides examples of how to use the configuration management commands to apply, save, and detach configurations.

### Apply and Save a Configuration

The following example command configures the front panel port interfaces swp1 thru swp4 to be slaves in bond0. The configuration is only in a pending configuration state. The configuration is **not** applied. CUE has not yet made any changes to the running configuration.

```
cumulus@switch:~$ cl set interface bond0 bond member swp1-4
```

To apply the pending configuration to the running configuration, run the `cl config apply` command. The configuration does **not** persist after a reboot.

```
cumulus@switch:~$ cl config apply
```

To save the applied configuration to the startup configuration, run the `cl config save` command. This command overwrites the startup configuration with the applied configuration by writing to the `/etc/cue.d/startup.yaml` file. The configuration persists after a reboot.

```
cumulus@switch:~$ cl config save
```

### Detach a Pending Configuration

The following example configures the IP address of the loopback interface, then detaches the configuration from the current pending configuration. The detached configuration is saved to a file called `pending` that includes a timestamp with extra characters to distinguish it from other pending configurations; for example, `pending_20210128_212626_4WSY`.

```
cumulus@switch:~$ cl set interface lo ip address 10.10.10.1
cumulus@switch:~$ cl config detach
```

### View Differences between Configurations

To view differences between configurations, run the `cl config diff` command.

To view differences between two detached pending configurations, run the `cl config diff` <<TAB>> command to list all the current detached pending configurations, then run the `cl config diff` command with the pending configurations you want to diff:

```
cumulus@switch:~$ cl config diff <<press Tab>>
cumulus@switch:~$ cl config diff
applied                              pending_20210208_201140_MJ0V
pending_20210208_195315_MJ0P         pending_20210208_204655_MJ12
pending_20210208_195937_MJ0S         startup
```

```
cumulus@switch:~$ cl config diff pending_20210208_201140_MJ0V pending_20210208_195315_MJ0P
```

To view differences between a detached pending configuration and the applied configuration:

```
cumulus@switch:~$ cl config diff pending_20210208_201140_MJ0V applied
```

### Replace and Patch a Pending Configuration

The following example replaces the pending configuration with the contents of the YAML configuration file called `cl-02/13/2021.yaml` located in the `/deps` directory:

```
cumulus@switch:~$ cl config replace /deps/cl-02/13/2021.yaml
```

The following example patches the pending configuration (runs the set or unset commands from the configuration in the `cl-02/13/2021.yaml` file located in the `/deps` directory):

```
cumulus@switch:~$ cl config patch /deps/cl-02/13/2021.yaml
```

## How is CUE Different from NCLU?

This section lists some of the differences between CUE and the NCLU command line interface to help you navigate configuration.

### Configuration File

When you save network configuration using CUE, the configuration is written to the `/etc/cue.d/startup.yaml` file.

CUE also writes to underlying Linux files when you apply a configuration, such as the `/etc/network/interfaces` and `/etc/frr/frr.conf` files. You can view these configuration files; however NVIDIA recommends that you do not manually edit them while using CUE.

### Bridge Configuration

You set global bridge configuration on the bridge domain. For example:

```
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10,20
```

However, you set specific bridge interface options with interface commands. For example:

```
cumulus@leaf01:~$ cl set interface swp1 bridge domain br_default learning on
```

The default vlan-aware bridge in CUE is `br_default`. The default vlan-aware bridge in NCLU is `bridge`.

### BGP Configuration

You can set global BGP configuration, such as the ASN, router ID, graceful shutdown and restart with the `cl set router bgp` command. For example:

```
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
```

However, BGP peer and peer group, route information, timer, and address family configuration requires a VRF. For example:

```
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 remote-as external
```
