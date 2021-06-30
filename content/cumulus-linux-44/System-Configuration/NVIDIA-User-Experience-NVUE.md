---
title: NVIDIA User Experience - NVUE
author: NVIDIA
weight: 115
toc: 3
---
NVUE is an object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) providing a robust API that allows for multiple interfaces to both view (show) and configure (set and unset) any element within a system running the NVUE software. The NVUE command line interface (CLI) and the REST API leverage the same API to interface with Cumulus Linux.

NVUE follows a declarative model, removing context-specific commands and settings. It is structured as a *big tree* that represents the entire state of a Cumulus Linux instance. At the base of the tree are high level branches representing objects, such as *router* and *interface*. Under each of these branches are further branches. As you navigate through the tree, you gain a more specific context. At the leaves of the tree are actual attributes, represented as key-value pairs. The path through the tree is similar to a filesystem path.

{{<img src = "/images/cumulus-linux/nvue-architecture.png">}}

## Start the NVUE Service

NVUE is installed by default in Cumulus Linux but the NVUE service is disabled. To run NVUE commands, you must enable and start the NVUE service (`nvued`):

```
cumulus@switch:~$ sudo systemctl enable nvued
cumulus@switch:~$ sudo systemctl start nvued
```

{{%notice info%}}
Do not mix NVUE and NCLU commands to configure the switch; use either the NCLU CLI or the NVUE CLI.
{{%/notice%}}

## NVUE REST API

To access the NVUE API, run these commands:

```
cumulus@switch:~$ sudo ln -s /etc/nginx/sites-{available,enabled}/nvue.conf
cumulus@switch:~$ sudo sed -i 's/listen localhost:8765 ssl;/listen \[::\]:8765 ipv6only=off ssl;/g' /etc/nginx/sites-available/nvue.conf
cumulus@switch:~$ sudo systemctl restart nginx
```

You can run the cURL commands from the command line. For example:

```
cumulus@switch:~$ curl  -u 'cumulus:CumulusLinux!' --insecure https://127.0.0.1:8765/cue_v1/interface
{
  "eth0": {
    "ip": {
      "address": {
        "192.168.200.12/24": {}
      }
    },
    "link": {
      "mtu": 1500,
      "state": {
        "up": {}
      },
      "stats": {
        "carrier-transitions": 2,
        "in-bytes": 184151,
        "in-drops": 0,
        "in-errors": 0,
        "in-pkts": 2371,
        "out-bytes": 117506,
        "out-drops": 0,
        "out-errors": 0,
        "out-pkts": 762
      }
...
```

For information about using the NVUE API, refer to the {{<kb_link url="cumulus-linux-44/api" text="NVUE API documentation.">}}

## NVUE CLI

The NVUE CLI has a flat structure as opposed to a modal structure. This means that you can run all commands from the primary prompt instead of only in a specific mode.

{{%notice note%}}
The NVUE commands and outputs in this documentation are subject to change.
{{%/notice%}}

### Command Syntax

NVUE commands all begin with `nv` and fall into one of three syntax categories:
- Configuration (`nv set` and ` nv unset`)
- Monitoring (`nv show`)
- Configuration management (`nv config`).

### Command Completion

As you enter commands, you can get help with the valid keywords or options using the Tab key. For example, using Tab completion with `nv set` displays the possible options for the command, and returns you to the command prompt to complete the command.

```
cumulus@switch:~$ nv set <<press Tab>>
acl        evpn       mlag       platform   router     system     
bridge     interface  nve        qos        service    vrf 

cumulus@switch:~$ nv set
```

### Command Help

As you enter commands, you can get help with command syntax by entering `-h` or `--help` at various points within a command entry. For example, to find out what options are available for `nv set interface`, enter `nv set interface -h` or `nv set interface --help`.

```
cumulus@switch:~$ nv set interface -h
Usage:
  nv set interface [options] <interface-id> ...

Description:
  Interfaces

Identifiers:
  <interface-id>    Interface

General Options:
  -h, --help        Show help.
```

### Command List

You can list all the NVUE commands by running `nv list-commands`. See {{<link url="#list-all-nvue-commands" text="List All NVUE Commands">}} below.

### Command History

At the command prompt, press the Up Arrow and Down Arrow keys to move back and forth through the list of commands previously entered. When you find a given command, you can run the command by pressing Enter. Optionally, you can modify the command before you run it.

## Command Categories

The NVUE CLI has a flat structure; however, the commands are grouped into three functional categories:

- Configuration
- Monitoring
- Configuration Management

### Configuration Commands

The NVUE configuration commands modify switch configuration. You can set and unset configuration options.

The `nv set` and `nv unset` commands are grouped into the following categories. Each command group includes subcommands. Use command completion (Tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv set acl`<br>`nv unset acl` | Configures ACLs in Cumulus Linux.|
| `nv set bridge`<br>`nv unset bridge` | Configures a bridge domain. This is where you configure the bridge type (such as VLAN-aware), 802.1Q encapsulation, the STP state and priority, and the VLANs in the bridge domain. |
| `nv set evpn`<br>`nv unset evpn` | Configures EVPN. This is where you enable and disable the EVPN control plane, and set EVPN route advertise options, default gateway configuration for centralized routing, multihoming, and duplicate address detection options. |
| `nv set interface <interface-id>`<br>`nv unset interface <interface-id>` | Configures the switch interfaces. Use this command to configure bond interfaces, bridge interfaces, interface IP addresses, VLAN IDs, and links (MTU, FEC, speed, duplex, and so on).|
| `nv set mlag`<br>`nv unset mlag` | Configures MLAG. This is where you configure the backup IP address or interface, MLAG system MAC address, peer IP address, MLAG priority, and the delay before bonds are brought up. |
| `nv set nve`<br>`nv unset nve` | Configures network virtualization (VXLAN) settings. This is where you configure the UDP port for VXLAN frames, control dynamic MAC learning over VXLAN tunnels, enable and disable ARP/ND suppression, and configure how Cumulus Linux handles BUM traffic in the overlay.|
| `nv set platform`<br>`nv unset platform` | Configures the hostname of the switch and sets how configuration apply operations are performed (such as which files to ignore and which files to overwrite). |
| `nv set qos`<br>`nv unset qos` | Configures QoS RoCE. |
| `nv set router`<br>`nv unset router` | Configures router policies (prefix list rules and route maps), global BGP options (enable and disable BGP, set the ASN and the router ID, and configure BGP graceful restart and shutdown), global OSPF options (enable and disable OSPF, set the router ID, and configure OSPF timers), and PBR. |
| `nv set service`<br>`nv unset service` | Configures DHCP relays and servers, NTP, PTP, LLDP, and syslog. |
| `nv set system`<br>`nv unset system` | Configures global system settings, such as the anycast ID, the system MAC address, and the anycast MAC address. This is also where you configure SPAN and ERSPAN sessions. |
| `nv set vrf  <vrf-id>`<br>`nv unset vrf <vrf-id>` | Configures VRFs. This is where you configure VRF-level router configuration including PTP, BGP, OSPF, and EVPN. |

### Monitoring Commands

The NVUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration or only interface configuration. The monitoring commands are grouped into the following categories. Each command group includes subcommands. Use command completion (Tab key) to list the subcommands.

| <div style="width:300px">Command Group | Description |
| ------- | ----------- |
| `nv show acl` | Shows ACL configuration. |
| `nv show bridge` | Shows bridge domain configuration.|
| `nv show evpn` |Shows EVPN configuration. |
| `nv show interface` |Shows interface configuration. |
| `nv show mlag` | Shows MLAG configuration. |
| `nv show nve` | Shows network virtualization configuration, such as VXLAN-specfic MLAG configuration and VXLAN flooding.|
| `nv show platform` | Shows platform configuration, such as hardware and software components, and the hostname of the switch. |
| `nv show qos` | Shows QoS RoCE configuration.|
| `nv show router` | Shows router configuration, such as router policies, and global BGP and OSPF configuration. |
| `nv show service` | Shows DHCP relays and server, NTP, PTP, LLDP, and syslog configuration. |
| `nv show system` | Shows global system settings, such as the reserved routing table range for PBR and the reserved VLAN range for layer 3 VNIs. You can also see switch reboot history with the reason why the switch rebooted. |
| `nv show vrf` | Shows VRF configuration.|

The following example shows the `nv show router` commands after pressing the TAB key, then shows the output of the `nv show router bgp` command.

```
cumulus@leaf01:mgmt:~$ nv show router <<TAB>>
bgp     ospf    pbr     policy
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
If there are no pending or applied configuration changes, the `nv show` command only shows the running (opertional) configuration.
{{%/notice%}}

Aditional options are available for the `nv show` commands. For example, you can choose the configuration you want to show (pending, applied, startup, or operational). You can also turn on colored output, and paginate specific output.

| <div style="width:200px">Option | Description |
| ------ | ----------- |
| `--applied`       | Shows configuration applied with the `nv config apply` command. For example, `nv show --applied interface bond1`. |
| `--color`         | Turns colored output on or off. For example, `nv show --color on interface bond1`|
| `--help`          | Shows help for the NVUE commands. |
| `--operational`   | Shows the running configuration (the actual system state). For example, `nv show --operational interface bond1` shows the running configuration for bond1. The running and applied configuration should be the same. If different, inspect the logs. |
| `--output`        | Shows command output in table format (auto), json format or yaml format. For example:<br>`nv show --ouptut auto interface bond1`<br>`nv show --ouptut json interface bond1`<br>`nv show --ouptut yaml interface bond1` |
| `--paginate`      | Paginates the output. For example, `nv show --paginate on interface bond1`. |
| `--pending`       | Shows configuration that is `set` and `unset` but not yet applied or saved. For example, `nv show --pending interface bond1`.|
| `--rev <revision>`| Shows a detached pending configuration. See the `nv config detach` configuration management command below. For example, `nv show --rev changeset/cumulus/2021-06-11_16.16.41_FPKK interface bond1`. |
| `--startup`       | Shows configuration saved with the `nv config save` command. This is the configuration after the switch boots. |

The following example shows *pending* BGP graceful restart configuration:

```
cumulus@switch:~$ nv show router bgp graceful-restart --pending
                             pending_20210128_212626_4WSY  description
----------------------------  ----------------------------  ----------------------------------------------------------------------
mode                          helper-only                   Role of router during graceful restart. helper-only, router is in h...
path-selection-deferral-time  360                           Used by the restarter as an upper-bounds for waiting for peeringes...
restart-time                  120                           Amount of time taken to restart by router. It is advertised to the...
stale-routes-time             360                           Specifies an upper-bounds on how long we retain routes from a resta...
```

### Show Legacy Commands

Cumulus Linux includes show legacy commands that provide the same output as the NCLU show commands. To use the show legacy commands, the NCLU service (`netd`) must be running.

{{%notice note%}}
When the NVUE service is running, NCLU commands (`net add`, `net del`, `net show`) are disabled to prevent you from configuring the switch with both NVUE and NVUE commands. For example, if you try to run the `net show interface` command, you see the error `Using NCLU with 'nvued' running is not supported`.
{{%/notice%}}

To run the show legacy commands, replace `net show` with `nv show --legacy`.

For example, to show the link and administrative state of an interface (such as swp1), run the `nv show --legacy interface swp1` command:

```
cumulus@switch:~$ nv show --legacy interface swp1
    Name  MAC                Speed  MTU   Mode
--  ----  -----------------  -----  ----  ------------
UP  swp1  44:38:39:00:00:31  1G     9216  Interface/L3

IP Details
-------------------------  -----------
IP:                        10.0.0.9/32
IP Neighbor(ARP) Entries:  0

cl-netstat counters
-------------------
RX_OK  RX_ERR  RX_DRP  RX_OVR  TX_OK  TX_ERR  TX_DRP  TX_OVR
-----  ------  ------  ------  -----  ------  ------  ------
    4       0       4       0  55425       0       0       0

Routing
-------
  Interface swp1 is up, line protocol is up
  Link ups:       0    last: (never)
  Link downs:     0    last: (never)
  PTM status: disabled
  vrf: default
  index 3 metric 0 mtu 9216 speed 1000
  flags: <UP,BROADCAST,RUNNING,MULTICAST>
  Type: Ethernet
  HWaddr: 44:38:39:00:00:31
  inet 10.0.0.9/32 unnumbered
  inet6 fe80::4638:39ff:fe00:31/64
  Interface Type Other
  protodown: off
```

To see a summary of layer 3 fabric connectivity, run the `nv show --legacy bgp` command:

```
cumulus@switch:~$ nv show --legacy bgp
show bgp ipv4 unicast
=====================
BGP table version is 0, local router ID is 10.10.10.2, vrf id 0
Default local pref 100, local AS 65102
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
   10.10.10.2/32    0.0.0.0                  0         32768 i

Displayed  1 routes and 1 total paths


show bgp ipv6 unicast
=====================
No BGP prefixes displayed, 0 exist
...
```

{{%notice note%}}
Not all `net show` commands are available as `nv show --legacy` commands.
{{%/notice%}}

### Configuration Management Commands

The NVUE configuration management commands manage and apply configurations.

| <div style="width:450px">Command | Description |
| ------- | ----------- |
| `nv config apply` | Applies the pending configuration to become the applied configuration.<br>You can also use these prompt options:<ul><li>`--y` or `--assume-yes` to automatically reply `yes` to all prompts.</li><li>`--assume-no` to automatically reply `no` to all prompts.</li></ul> {{%notice note%}}The configuration is applied but not saved and does not persist after a reboot.{{%/notice%}}You can also use these apply options:<br>`--confirm` applies the configuration change but requires you to confirm the applied configuration. If you do not confirm within ten minutes, the configuration is rolled back automatically. You can change the default time with the apply `--confirm <time>` command. For example, `apply --confirm 60` requires you to confirm within one hour.<br>`--confirm-status` shows the amount of time left before the automatic rollback.|
| `nv config detach` | Detaches the configuration from the current pending configuration. The detached configuration is called `pending` and includes a timestamp with extra characters. For example: `pending_20210128_212626_4WSY`|
| `nv config diff <revision> <revision>` | Shows differences between configurations, such as the pending configuration and the applied configuration or the detached configuration and the pending configuration.|
| `nv config history <nvue-file>` | Shows the apply history for the revision. |
| `nv config patch <nvue-file>` | Updates the pending configuration with the specified YAML configuration file. |
| `nv config replace <nvue-file>` | Replaces the pending configuration with the specified YAML configuration file. |
| `nv config save` | Overwrites the startup configuration with the applied configuration by writing to the `/etc/nvue.d/startup.yaml` file. The configuration persists after a reboot. |

### List All NVUE Commands

To show the full list of NVUE commands, run `nv list-commands`. For example:

```
cumulus@switch:~$ nv list-commands
nv show router
nv show router pbr
nv show router pbr nexthop-group
nv show router pbr nexthop-group <nexthop-group-id>
nv show router pbr nexthop-group <nexthop-group-id> via
nv show router pbr nexthop-group <nexthop-group-id> via <nhg-via-id>
nv show router pbr map
nv show router pbr map <pbr-map-id>
nv show router pbr map <pbr-map-id> rule
nv show router pbr map <pbr-map-id> rule <rule-id>
nv show router pbr map <pbr-map-id> rule <rule-id> match
nv show router pbr map <pbr-map-id> rule <rule-id> action
nv show router policy
nv show router policy community-list
...
```

You can show the list of commands for a command grouping and for subcommands. For example, to show the list of interface commands:

```
cumulus@switch:~$ nv list-commands interface
nv show interface
nv show interface <interface-id>
nv show interface <interface-id> router
nv show interface <interface-id> router pbr
nv show interface <interface-id> router ospf
nv show interface <interface-id> router ospf timers
nv show interface <interface-id> router ospf authentication
nv show interface <interface-id> router ospf bfd
nv show interface <interface-id> bond
nv show interface <interface-id> bond member
nv show interface <interface-id> bond member <member-id>
nv show interface <interface-id> bond mlag
nv show interface <interface-id> bridge
...
```

Use the Tab key to get help for the command lists you want to see. For example, to show the list of command options available for the interface swp1, run:

```
cumulus@switch:~$ nv list-commands interface swp1 <<press Tab>>
acl      bond     bridge   evpn     ip       link     qos      router   service
```

## NVUE Configuration File

When you save network configuration using NVUE, the configuration is written to the `/etc/nvue.d/startup.yaml` file.

NVUE also writes to underlying Linux files, such as `/etc/network/interfaces` and `/etc/frr/frr.conf`, when you apply a configuration. You can view these configuration files; however NVIDIA recommends that you do not manually edit them while using NVUE.

You can edit or replace the contents of the `/etc/nvue.d/startup.yaml` file. NVUE applies the configuration in the `/etc/nvue.d/startup.yaml` file during system boot only if the `nvue-startup.service` is running. If this service is not running, the running configuration that was last applied is loaded when the switch boots.

To start `nvue-startup.service`:

```
cumulus@switch:~$ sudo systemctl enable nvue-startup.service
cumulus@switch:~$ sudo systemctl start nvue-startup.service
```

## Example Configuration Commands

This section provides examples of how to configure a Cumulus Linux switch using NVUE commands.

### Configure the System Hostname

The example below shows the NVUE commands required to change the hostname for the switch to leaf01:

```
cumulus@switch:~$ nv set platform hostname value leaf01
cumulus@switch:~$ nv config apply
```

### Configure the System DNS Server

The example below shows the NVUE commands required to define the DNS server for the switch:

```
cumulus@switch:~$ nv set service dhcp-server 192.168.200.1
cumulus@switch:~$ nv config apply
```

### Configure an Interface

The example below shows the NVUE commands required to bring up swp1.

```
cumulus@switch:~$ nv set interface swp1 link state up
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
- Set the peer link IP address to linklocal, the MLAG system MAC address to 44:38:39:BE:EF:AA, and the backup interface to 10.10.10.2.

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
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32
cumulus@leaf01:~$ nv config apply
```

## Example Monitoring Commands

This section provides monitoring command examples.

### Show Installed Software

The following example command lists the software installed on the switch:

```
cumulus@switch:~$ nv show platform software
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

The following example command shows the running (operationa), applied, and pending swp1 interface configuration.

```
cumulus@leaf01:~$ nv show interface swp1
                         operational  applied  pending  description
-----------------------  -----------  -------  -------  ----------------------------------------------------------------------
type                     swp                   swp      The type of interface
[acl]                                                   Interface ACL rules
evpn
  multihoming
    uplink                                     off      Enable evpn multihoming tracking to prevent traffic loss due to NVE...
ip
  vrf                                          default  Virtual routing and forwarding
  [address]                                             ipv4 and ipv6 address
  [gateway]                                             default ipv4 and ipv6 gateways
  ipv4
    forward                                    on       Enable or disable forwarding.
  ipv6
    enable                                     on       Turn the feature 'on' or 'off'.  The default is 'on'.
    forward                                    on       Enable or disable forwarding.
link
  auto-negotiate                               on       Link speed and characteritic auto negotiation
  breakout                                     1x       sub-divide or disable ports (only valid on plug interfaces)
  duplex                                       full     Link duplex
  fec                                          auto     Link forward error correction mechanism
  mtu                    9216                  9216     interface mtu
  speed                                        auto     Link speed
  dot1x
    mab                                        off      bypass MAC authentication
    parking-vlan                               off      VLAN for unauthorized MAC addresses
  state                  up                    up       The state of the interface
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

The following example configures the IP address of the loopback interface, then detaches the configuration from the current pending configuration. The detached configuration is saved to a file `changeset/cumulus/<date>_<time>_xxxx` that includes a timestamp with extra characters to distinguish it from other pending configurations; for example, `changeset/cumulus/2021-06-11_18.35.06_FPKP`.

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.1
cumulus@switch:~$ nv config detach
```

### View Differences Between Configurations

To view differences between configurations, run the `nv config diff` command.

To view differences between two detached pending configurations, run the `nv config diff` <<TAB>> command to list all the current detached pending configurations, then run the `nv config diff` command with the pending configurations you want to diff:

```
cumulus@switch:~$ nv config diff <<press Tab>>
applied                                     changeset/cumulus/2021-06-11_18.35.06_FPKP
changeset/cumulus/2021-06-11_16.16.41_FPKK  empty
changeset/cumulus/2021-06-11_17.05.12_FPKN  startup
```

```
cumulus@switch:~$ nv config diff changeset/cumulus/2021-06-11_18.35.06_FPKP changeset/cumulus/2021-06-11_17.05.12_FPKN
```

To view differences between a detached pending configuration and the applied configuration:

```
cumulus@switch:~$ nv config diff changeset/cumulus/2021-06-11_18.35.06_FPKP applied
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

## How Is NVUE Different from NCLU?

This section lists some of the differences between NVUE CLI and the NCLU CLI to help you navigate configuration.

### Configuration File

When you save network configuration using NVUE, the configuration is written to the `/etc/nvue.d/startup.yaml` file.

NVUE also writes to underlying Linux files when you apply a configuration, such as the `/etc/network/interfaces` and `/etc/frr/frr.conf` files. You can view these configuration files; however NVIDIA recommends that you do not manually edit them while using NVUE.

### Bridge Configuration

You set global bridge configuration on the bridge domain. For example:

```
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20
```

However, you set specific bridge interface options with interface commands. For example:

```
cumulus@leaf01:~$ nv set interface swp1 bridge domain br_default learning on
```

The default vlan-aware bridge in NVUE is `br_default`. The default vlan-aware bridge in NCLU is `bridge`.

### BGP Configuration

You can set global BGP configuration, such as the ASN, router ID, graceful shutdown and restart with the `nv set router bgp` command. For example:

```
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
```

However, BGP peer and peer group, route information, timer, and address family configuration requires a VRF. For example:

```
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 remote-as external
```
