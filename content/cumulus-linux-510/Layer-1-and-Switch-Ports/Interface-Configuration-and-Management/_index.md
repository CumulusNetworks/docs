---
title: Interface Configuration and Management
author: NVIDIA
weight: 290
toc: 3
---
Cumulus Linux uses `ifupdown2` to manage network interfaces, which is a new implementation of the Debian network interface manager `ifupdown`.

## Bring an Interface Up or Down

An interface status can be in an:
- Administrative state, where you configure the interface to be up or down.
- Operational state, which reflects the current operational status of an interface.

{{< tabs "TabID17 ">}}
{{< tab "NVUE Commands ">}}

To configure and bring an interface up administratively, use the `nv set interface` command:

```
cumulus@switch:~$ nv set interface swp1
cumulus@switch:~$ nv config apply
```

After you bring up an interface, you can bring it down administratively by changing the link state to `down`:

```
cumulus@switch:~$ nv set interface swp1 link state down
cumulus@switch:~$ nv config apply
```

To bring the interface back up, change the link state back to `up`:

```
cumulus@switch:~$ nv set interface swp1 link state up
cumulus@switch:~$ nv config apply
```

To remove an interface from the configuration entirely, use the `nv unset interface` command:

```
cumulus@switch:~$ nv unset interface swp1
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
NVUE applies only current configuration changes instead of processing the entire `/etc/network/interfaces` file.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

To configure and bring an interface up administratively, edit the `/etc/network/interfaces` file to add the interface stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.1/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
...
```

To bring an interface down administratively after you configure it, add `link-down yes` to the interface stanza in the `/etc/network/interfaces` file, then run `ifreload -a`:

```
auto swp1
iface swp1
 link-down yes
```

If you configure an interface in the `/etc/network/interfaces` file, you can bring it down administratively with the `ifdown swp1` command, then bring the interface back up with the `ifup swp1` command. These changes do not persist after a reboot. After a reboot, the configuration present in `/etc/network/interfaces` takes effect.

{{%notice note%}}
- By default, the `ifupdown` and `ifup` commands are quiet. Use the verbose option (`-v`) to show commands as they execute when you bring an interface down or up.
- For configurations at scale, you can run the `ifreload -a --diff` command to apply only current configuration changes instead of processing the entire `/etc/network/interfaces` file.
{{%/notice%}}

To remove an interface from the configuration entirely, remove the interface stanza from the `/etc/network/interfaces` file, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

For additional information on interface administrative state and physical state, refer to [this knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux" >}}).

## Loopback Interface

Cumulus Linux has a preconfigured loopback interface. When the switch boots up, the loopback interface called *lo* is up and assigned an IP address of 127.0.0.1.

{{%notice note%}}
The loopback interface *lo* must always exist on the switch and must always be up.
{{%/notice%}}

To configure an IP address for the loopback interface:

{{< tabs "TabID196 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add an `address` line:

```
auto lo
iface lo inet loopback
    address 10.10.10.1
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- If the IP address has no subnet mask, it automatically becomes a /32 IP address. For example, 10.10.10.1 is 10.10.10.1/32.
- You can configure multiple IP addresses for the loopback interface.
{{%/notice%}}

## Child Interfaces

By default, `ifupdown2` recognizes and uses any interface present on the system that is a dependent (child) of an interface (for example, a VLAN, bond, or physical interface). You do not need to list interfaces in the `/etc/network/interfaces` file unless the interfaces need specific configuration for {{<link url="Switch-Port-Attributes" text="MTU, link speed, and so on">}}. If you need to delete a child interface, delete all references to that interface from the `/etc/network/interfaces` file.

In the following example, swp1 and swp2 do not need an entry in the `interfaces` file. The following stanzas in `/etc/network/interfaces` provide the exact same configuration:

**With Child Interfaces Defined**

```
auto swp1
iface swp1

auto swp2
iface swp2

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 1-100
    bridge-pvid 1
    bridge-stp on
```

**Without Child Interfaces Defined**

```
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 1-100
    bridge-pvid 1
    bridge-stp on
```

In the following example, swp1.100 and swp2.100 do not need an entry in the `interfaces` file. The following stanzas defined in `/etc/network/interfaces` provide the exact same configuration:

**With Child Interfaces Defined**

```
auto swp1.100
iface swp1.100

auto swp2.100
iface swp2.100

auto br-100
iface br-100
    address 10.0.12.2/24
    address 2001:dad:beef::3/64
    bridge-ports swp1.100 swp2.100
    bridge-stp on
```

**Without Child Interfaces Defined**

```
auto br-100
iface br-100
    address 10.0.12.2/24
    address 2001:dad:beef::3/64
    bridge-ports swp1.100 swp2.100
    bridge-stp on
```

## Interface Dependencies

`ifupdown2` understands interface dependency relationships. When you run `ifup` and `ifdown` with all interfaces, the commands always run with all interfaces in dependency order. When you run `ifup` and `ifdown` with the interface list on the command line, the default behavior is to *not* run with dependents; however, if there are any built-in dependents, they do come up or go down.

To run with dependents when you specify the interface list, use the `--with-depends` option. The `--with-depends` option walks through all dependents in the dependency tree rooted at the interface you specify. Consider the following example configuration:

```
auto bond1
iface bond1
    address 100.0.0.2/16
    bond-slaves swp29 swp30

auto bond2
iface bond2
    address 100.0.0.5/16
    bond-slaves swp31 swp32

auto br2001
iface br2001
    address 12.0.1.3/24
    bridge-ports bond1.2001 bond2.2001
    bridge-stp on
```

The `ifup --with-depends br2001` command brings up all dependents of br2001: bond1.2001, bond2.2001, bond1, bond2, bond1.2001, bond2.2001, swp29, swp30, swp31, swp32.

```
cumulus@switch:~$ sudo ifup --with-depends br2001
```

The `ifdown --with-depends br2001` command brings down all dependents of br2001: bond1.2001, bond2.2001, bond1, bond2, bond1.2001, bond2.2001, swp29, swp30, swp31, swp32.

```
cumulus@switch:~$ sudo ifdown --with-depends br2001
```

{{%notice warning%}}
`ifdown2` always deletes logical interfaces after bringing them down. Use the `--admin-state` option if you only want to administratively bring the interface up or down. In the above example, `ifdown br2001` deletes `br2001`.
{{%/notice%}}

To guide you through which interfaces go down and come up, use the `--print-dependency` option.

For example, run `ifquery --print-dependency=list -a` to show the dependency list for all interfaces:

```
cumulus@switch:~$ sudo ifquery --print-dependency=list -a
lo : None
eth0 : None
bond0 : ['swp25', 'swp26']
bond1 : ['swp29', 'swp30']
bond2 : ['swp31', 'swp32']
br0 : ['bond1', 'bond2']
bond1.2000 : ['bond1']
bond2.2000 : ['bond2']
br2000 : ['bond1.2000', 'bond2.2000']
bond1.2001 : ['bond1']
bond2.2001 : ['bond2']
br2001 : ['bond1.2001', 'bond2.2001']
swp40 : None
swp25 : None
swp26 : None
swp29 : None
swp30 : None
swp31 : None
swp32 : None
```

To print the dependency list of a single interface, run the `ifquery --print-dependency=list <interface>` command.

To show the dependency information for an interface in `dot` format, run the `ifquery --print-dependency=dot <interface>` command. The following example command shows the dependency information for interface br2001 in `dot` format:

```
cumulus@switch:~$ sudo ifquery --print-dependency=dot br2001
/* Generated by GvGen v.0.9 (http://software.inl.fr/trac/wiki/GvGen) */
digraph G {
    compound=true;
    node1 [label="br2001"];
    node2 [label="bond1.2001"];
    node3 [label="bond2.2001"];
    node4 [label="bond1"];
    node5 [label="bond2"];
    node6 [label="swp29"];
    node7 [label="swp30"];
    node8 [label="swp31"];
    node9 [label="swp32"];
    node1->node2;
    node1->node3;
    node2->node4;
    node3->node5;
    node4->node6;
    node4->node7;
    node5->node8;
    node5->node9;
}
```

You can use `dot` to render the graph on an external system.

{{< img src = "/images/cumulus-linux/layer1-interfaces.png" >}}

To print the dependency information of the entire `interfaces` file, run the following command:

```
cumulus@switch:~$ sudo ifquery --print-dependency=dot -a >interfaces_all.dot
```

{{< img src = "/images/cumulus-linux/layer1-interfaces-all.png" >}}

## Subinterfaces

On Linux, an *interface* is a network device that can be either physical, (for example, swp1) or virtual (for example, vlan100). A *VLAN subinterface* is a VLAN device on an interface, and the VLAN ID appends to the parent interface using dot (.) VLAN notation. For example, a VLAN with ID 100 that is a subinterface of swp1 is swp1.100. The dot VLAN notation for a VLAN device name is a standard way to specify a VLAN device on Linux.

A VLAN subinterface only receives traffic tagged for that VLAN; therefore, swp1.100 only receives packets that have a VLAN 100 tag on switch port swp1. Any packets that transmit from swp1.100 have a VLAN 100 tag.

The following example configures a routed subinterface on swp1 in VLAN 100:

{{< tabs "TabID316 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1.100 ip address 192.168.100.1/24
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run `ifreload -a`:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1.100
iface swp1.100
 address 192.168.100.1/24
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- If you are using a VLAN subinterface, do not add that VLAN under the bridge stanza.
- You cannot use NVUE commands to create a routed subinterface for VLAN 1.
{{%/notice%}}

## Interface IP Addresses

You can specify both IPv4 and IPv6 addresses for the same interface.

For IPv6 addresses:
- You can create or modify the IP address for an interface using either `::` or `0:0:0` notation. For example, both 2620:149:43:c109:0:0:0:5 and 2001:DB8::1/126 are valid.
- Cumulus Linux assigns the IPv6 address with all zeroes in the interface identifier (2001:DB8::/126) for each subnet; connected hosts cannot use this address.

The following example commands configure three IP addresses for swp1; two IPv4 addresses and one IPv6 address.

{{< tabs "TabID464 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ip address 10.0.0.1/30
cumulus@switch:~$ nv set interface swp1 ip address 10.0.0.2/30
cumulus@switch:~$ nv set interface swp1 ip address 2001:DB8::1/126
cumulus@switch:~$ nv config apply
```

To show the MAC address for an interface, run the `nv show interface <interface> link` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, list all IP addresses under the `iface` section.

```
auto swp1
iface swp1
    address 10.0.0.1/30
    address 10.0.0.2/30
    address 2001:DB8::1/126
```

The address method and address family are not mandatory; they default to `inet/inet6` and `static`. However, you must specify `inet/inet6` when you are creating DHCP or loopback interfaces.

```
auto lo
iface lo inet loopback
```

To make non-persistent changes to interfaces at runtime, use `ip addr add`:

```
cumulus@switch:~$ sudo ip addr add 10.0.0.1/30 dev swp1
cumulus@switch:~$ sudo ip addr add 2001:DB8::1/126 dev swp1
```

To remove an addresses from an interface, use `ip addr del`:

```
cumulus@switch:~$ sudo ip addr del 10.0.0.1/30 dev swp1
cumulus@switch:~$ sudo ip addr del 2001:DB8::1/126 dev swp1
```

{{< /tab >}}
{{< /tabs >}}

## Interface MAC Addresses

You can configure a MAC address for an interface with the `nv set interface <interface> link mac-address <mac-address>` command.

{{< tabs "TabID410 ">}}
{{< tab "NVUE Commands ">}}

The following command configures swp1 with MAC address 00:02:00:00:00:05:

```
cumulus@switch:~$ nv set interface swp1 link mac-address 00:02:00:00:00:05
cumulus@switch:~$ nv config apply
```

The following command configures vlan10 with MAC address 00:00:5E:00:01:00:

```
cumulus@switch:~$ nv set interface vlan10 link mac-address 00:00:5E:00:01:00
cumulus@switch:~$ nv config apply
```

To unset the MAC address for an interface, run the `nv unset interface <interface> link mac-address` command:

```
cumulus@switch:~$ nv unset interface swp1 link mac-address
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, add a MAC address for the interface in the interface stanza, then run `ifreload -a`.

The following example configures swp1 with MAC address 00:02:00:00:00:05:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    address 10.0.0.2/24
    hwaddress 00:02:00:00:00:05
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

The following example configures vlan10 with MAC address 00:00:5E:00:01:00:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan10
    address 10.1.10.5/24
    hwaddress 00:00:5E:00:01:00
```

```
cumulus@switch:~$ sudo ifreload -a
```

To unset the MAC address for an interface, remove the mac address from the interface stanza, then run the `sudo ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

## Interface Descriptions

You can add a description (alias) to an interface.

Interface descriptions also appear in the {{<link url="Simple-Network-Management-Protocol-SNMP" text="SNMP">}} OID {{<mib_link text="IF-MIB::ifAlias" url="mibs/IF-MIB.txt" >}}

{{%notice note%}}
- Interface descriptions can have a maximum of 256 characters.
- Avoid using apostrophes or non-ASCII characters. Cumulus Linux does not parse these characters.
{{%/notice%}}

The following example commands create the description `hypervisor_port_1` for swp1:

{{< tabs "TabID838 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 description hypervisor_port_1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, add a description using the *alias* keyword:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    alias swp1 hypervisor_port_1
```

{{< /tab >}}
{{< /tabs >}}

## Interface Commands

You can specify user commands for an interface that run at pre-up, up, post-up, pre-down, down, and post-down.

You can add any valid command in the sequence to bring an interface up or down; however, limit the scope to network-related commands associated with the particular interface. For example, it does not make sense to install a Debian package on `ifup` of swp1, even though it is technically possible. See `man interfaces` for more details.

The following examples adds a command to an interface to enable proxy ARP:

{{< tabs "TabID640 ">}}
{{< tab "NVUE Commands ">}}

NVUE does not provide commands to configure this feature.

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
auto swp1
iface swp1
    address 12.0.0.1/30
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
```

{{%notice warning%}}
If your `post-up` command also starts, restarts, or reloads any `systemd` service, you must use the `--no-block` option with `systemctl`. Otherwise, that service or even the switch itself might hang after starting or restarting. For example, to restart the `dhcrelay` service after bringing up a VLAN, the `/etc network/interfaces` configuration looks like this:

```
auto bridge.100
iface bridge.100
    post-up systemctl --no-block restart dhcrelay.service
```
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Source Interface File Snippets

Sourcing interface files helps organize and manage the `/etc/network/interfaces` file. For example:

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp

source /etc/network/interfaces.d/bond0
```

The contents of the sourced file used above are:

```
cumulus@switch:~$ sudo cat /etc/network/interfaces.d/bond0
auto bond0
iface bond0
    address 14.0.0.9/30
    address 2001:ded:beef:2::1/64
    bond-slaves swp25 swp26
```

## Port Ranges

To specify port ranges in commands:

{{< tabs "TabID725 ">}}
{{< tab "NVUE Commands ">}}

Use commas to separate different port ranges (for example, swp1-46,10-12):

```
cumulus@switch:~$ nv set interface swp1-4,6,10-12 bridge domain br_default
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Use the `glob` keyword to specify bridge ports and bond slaves:

```
auto br0
iface br0
    bridge-ports glob swp1-6.100

auto br1
iface br1
    bridge-ports glob swp7-9.100  swp11.100 glob swp15-18.100
```

{{< /tab >}}
{{< /tabs >}}

## Fast Linkup

Cumulus Linux supports fast linkup on interfaces on NVIDIA Spectrum1 switches. Fast linkup enables you to bring up ports with cards that require links to come up fast, such as certain 100G optical network interface cards.

{{%notice note%}}
You must configure both sides of the connection with the same speed and FEC settings.
{{%/notice%}}

{{< tabs "TabID607 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set interface swp1 link fast-linkup on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file and add the `interface.<interface>.enable_media_depended_linkup_flow=TRUE` and `interface.<interface>.enable_port_short_tuning=TRUE` settings for the interfaces on which you want to enable fast linkup. The following example enables fast linkup on swp1:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
interface.swp1.enable_media_depended_linkup_flow=TRUE
interface.swp1.enable_short_tuning=TRUE
```

Reload `switchd` with the `sudo systemctl reload switchd.service` command.

{{< /tab >}}
{{< /tabs >}}

## Link Flap Protection

Cumulus Linux enables link flap detection by default. Link flap detection triggers when there are five link flaps within ten seconds, at which point the interface goes into a protodown state and shows `linkflap` as the reason. The `switchd` service also shows a log message similar to the following:

```
2023-02-10T17:53:21.264621+00:00 cumulus switchd[10109]: sync_port.c:2263 ERR swp2 link flapped more than 3 times in the last 60 seconds, setting protodown
```

To show interfaces with the protodown flag, run the NVUE `nv show interface` command or the Linux `ip link` command. To check a specific interface, run the `nv show interface <interface> link` command.

```
cumulus@switch:~$ nv show interface
Interface  State  Speed  MTU    Type      Remote Host      Remote Port  Summary                                 
---------  -----  -----  -----  --------  ---------------  -----------  ----------------------------------------
eth0       up     1G     1500   eth       oob-mgmt-switch  swp10        IP Address:            192.168.200.11/24
                                                                        IP Address:  fe80::4638:39ff:fe22:17a/64
lo         up            65536  loopback                                IP Address:                  127.0.0.1/8
                                                                        IP Address:                      ::1/128
mgmt       up            65575  vrf                                     IP Address:                  127.0.0.1/8
                                                                        IP Address:                      ::1/128
swp1       up            1500   swp                                                                             
swp2       protodown     9178   swp                                                                             
swp3       up            1500   swp                                                                             
swp4       up            1500   swp                                                                             
...
```

```
cumulus@switch:~$ ip link
...
37: swp2: <NO-CARRIER,BROADCAST,MULTICAST,SLAVE,UP> mtu 9178 qdisc pfifo_fast master bond131 state DOWN mode DEFAULT group default qlen 1000
  link/ether 1c:34:da:ba:bb:2a brd ff:ff:ff:ff:ff:ff protodown on protodown_reason <linkflap>
...
```

```
cumulus@switch:~$ nv show interface swp1 link
                       operational                     
---------------------  ------------------------------
admin-status           up
oper-status            up
protodown              disabled
auto-negotiate         on
duplex                 full
speed                  800G
mac-address            9c:05:91:9a:e0:b8
fec                    rs
mtu                    9216
fast-linkup            off
stats
  in-bytes             145.08 KB
  in-pkts              756
  in-drops             8
  in-errors            0
  out-bytes            145.42 KB
  out-pkts             757
  out-drops            0
  out-errors           0
  carrier-transitions  12
eyes                   65, 62, 70, 65, 80, 82, 81, 82
grade                  65, 62, 70, 65, 80, 82, 81, 82
troubleshooting-info   No issue was observed
```

### Clear the Interface Protodown State and Reason

To clear the protodown state and the reason:

{{< tabs "TabID654 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv action clear interface swp1 link flap-protection violation 
```

After a few seconds the port state returns to `up`. Run the `nv show <interface> link state` command to verify that the interface is no longer in a protodown state and that the reason clears:

```
cumulus@switch:~$ nv show swp1 link state
operational    applied
  -----------    -------
  up             up
```

To clear all the interfaces from a protodown state, run the `nv action clear system link flap-protection violation`.

{{< /tab >}}
{{< tab "Linux Commands ">}}

The `ifdown` and `ifup` commands do not clear the protodown state. You must clear the protodown state and the reason manually using the `sudo ip link set <interface> protodown_reason linkflap off` and `sudo ip link set <interface> protodown off` commands.

```
cumulus@switch:~$ sudo ip link set swp2 protodown_reason linkflap off
cumulus@switch:~$ sudo ip link set swp2 protodown off
```

After a few seconds, the port state returns to UP. To verify that the interface is no longer in a protodown state and that the reason clears, run the `ip link show <interface>` command:

```
cumulus@switch:~$ ip link show swp2
37: swp2: <NO-CARRIER,BROADCAST,MULTICAST,SLAVE,UP> mtu 9178 qdisc pfifo_fast master bond131 state UP mode DEFAULT group default qlen 1000
  link/ether 1c:34:da:ba:bb:2a brd ff:ff:ff:ff:ff:ff
```

{{< /tab >}}
{{< /tabs >}}

### Change Link Flap Protection Settings

You can change the following link flap protection settings:
- The duration in seconds during which a link must flap the number of times set in the link flap threshold before link flap protection triggers. You can specify a value between 0 (off) and 60. The default setting is 10.
- The number of times the link can flap within the link flap window before link flap protection triggers. You can specify a value between 0 (off) and 30. The default setting is 5.

The following example configures the link flap duration to 30 and the number of times the link must flap to 8.

{{< tabs "TabID671 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system link flap-protection interval 30
cumulus@switch:~$ nv set system link flap-protection threshold 8 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file to change the `link_flap_window` and `link_flap_threshold` settings.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
link_flap_window = 30
link_flap_threshold = 8
...
```

After you change the link flap settings, you must restart `switchd` with the `sudo systemctl restart switchd.service` command.

{{< /tab >}}
{{< /tabs >}}

### Disable Link Flap Protection

To disable link flap protection:

{{< tabs "TabID682 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link flap-protection enable off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file, and set the `link_flap_window` and `link_flap_threshold` parameters to 0 (zero).

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
link_flap_window = 0
link_flap_threshold = 0
```

{{< /tab >}}
{{< /tabs >}}

### Show Link Flap Protection Configuration

To show the link flap protection time interval and threshold settings:

```
cumulus@switch:~$ nv show system link flap-protection
           applied
---------  -------
threshold  8      
interval   30 
```

To show if link flap protection is on an interface, run the `nv show interface <interface> link flap-protection` command:

```
cumulus@switch:~$ nv show interface swp1 link flap-protection
        applied
------  -------
enable  off
```

## Mako Templates

`ifupdown2` supports {{<exlink url="http://www.makotemplates.org/" text="Mako-style templates">}}. The Mako template engine processes the `interfaces` file before parsing.

Use the template to declare cookie-cutter bridges and to declare addresses in the `interfaces` file:

```
%for i in [1,12]:
auto swp${i}
iface swp${i}
    address 10.20.${i}.3/24
```

{{%notice note%}}
- In Mako syntax, use square brackets (`[1,12]`) to specify a list of individual numbers. Use `range(1,12)` to specify a range of interfaces.
- To test your template and confirm it evaluates correctly, run `mako-render /etc/network/interfaces`.
{{%/notice%}}

To comment out content in Mako templates, use double hash marks (##). For example:

```
## % for i in range(1, 4):
## auto swp${i}
## iface swp${i}
## % endfor
##
```

For more Mako template examples, refer to this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Automation/Configure-the-interfaces-File-with-Mako" >}}).

## ifupdown Scripts

Unlike the traditional `ifupdown` system, `ifupdown2` does not run scripts installed in `/etc/network/*/` automatically to configure network interfaces.

To enable or disable `ifupdown2` scripting, edit the `addon_scripts_support` line in the `/etc/network/ifupdown2/ifupdown2.conf` file. `1` enables scripting and `2` disables scripting. For example:

```
cumulus@switch:~$ sudo nano /etc/network/ifupdown2/ifupdown2.conf
# Support executing of ifupdown style scripts.
# Note that by default python addon modules override scripts with the same name
addon_scripts_support=1
```

`ifupdown2` sets the following environment variables when executing commands:

- `$IFACE` represents the physical name of the interface; for example, `br0` or vxlan42. The name comes from the `/etc/network/interfaces` file.
- `$LOGICAL` represents the logical name (configuration name) of the interface.
- `$METHOD` represents the address method; for example, loopback, DHCP, DHCP6, manual, static, and so on.
- `$ADDRFAM` represents the address families associated with the interface in a comma-separated list; for example, `"inet,inet6"`.

## Troubleshooting

To show the administrative and physical (operational) state of all interfaces on the switch:

```
cumulus@switch:~$ nv show interface
Interface  Admin Status  Oper Status  Speed  MTU    Type      Remote Host      Remote Port  Summary                                 
---------  ------------  -----------  -----  -----  --------  ---------------  -----------  ----------------------------------------
eth0       up            up           1G     1500   eth       oob-mgmt-switch  swp10        IP Address:            192.168.200.11/24
                                                                                            IP Address:  fe80::4638:39ff:fe22:17a/64
lo         up            unknown             65536  loopback                                IP Address:                  127.0.0.1/8
                                                                                            IP Address:                      ::1/128
mgmt       up            up                  65575  vrf                                     IP Address:                  127.0.0.1/8
                                                                                            IP Address:                      ::1/128
swp1       up            up           1G     9216   swp                                     IP Address: fe80::4ab0:2dff:fe50:fecf/64
swp2       down          down                1500   swp                                                                             
swp3       down          down                1500   swp                                                                             
swp4       down          down                1500   swp                                                                             
swp5       down          down                1500   swp                                                                             
swp6       down          down                1500   swp                                                                             
swp7       down          down                1500   swp
...
```

To show the administrative and physical (operational) state of an interface:

{{< tabs "TabID875 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show interface swp1
                         operational        applied
-----------------------  -----------------  -------
...
  oper-status            down                      
  admin-status           down 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Run the `ip link show dev <interface>` command.

In the following example, swp1 is administratively UP and the physical link is UP (LOWER_UP).

```
cumulus@switch:~$ ip link show dev swp1
3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
```

{{< /tab >}}
{{< /tabs >}}

To show the assigned IP address on an interface:

{{< tabs "TabID898 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show interface lo ip address
nv show interface lo ip address
             
-------------
10.10.10.1/24
127.0.0.1/8  
::1/128
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ ip addr show swp1
3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    inet 192.0.2.1/30 scope global swp1
    inet 192.0.2.2/30 scope global swp1
    inet6 2001:DB8::1/126 scope global tentative
        valid_lft forever preferred_lft forever
```

{{< /tab >}}
{{< /tabs >}}

To show the description (alias) for an interface:

{{< tabs "TabID923 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch$ nv show interface swp1
                         operational        applied
------------------------  -----------------  -------
type                      swp                swp    
router                                              
  pbr                                               
    [map]                                           
  ospf                                              
    enable                                   off    
  pim                                               
    enable                                   off    
  adaptive-routing                                  
    enable                                   off    
  ospf6                                             
    enable                                   off    
lldp                                                
  dcbx-pfc-tlv            off                       
  dcbx-ets-config-tlv     off                       
  dcbx-ets-recomm-tlv     off                       
  [neighbor]                                        
evpn                                                
  multihoming                                       
    uplink                                   off    
ptp                                                 
  enable                                     off    
[acl]                                               
synce                                               
  enable                                     off    
neighbor                                            
  [ipv4]                                            
  [ipv6]                                            
description               server1            server1
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch$ ip link show swp1
3: swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500
    link/ether aa:aa:aa:aa:aa:bc brd ff:ff:ff:ff:ff:ff
    alias hypervisor_port_1
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

Even though `ifupdown2` supports the inclusion of multiple `iface` stanzas for the same interface, use a single `iface` stanza for each interface. If you must specify more than one `iface` stanza; for example, if the configuration for a single interface comes from many places, like a template or a sourced file, make sure the stanzas do not specify the same interface attributes. Otherwise, you see unexpected behavior.

In the following example, swp1 is in two files: `/etc/network/interfaces` and `/etc/network/interfaces.d/speed_settings`. `ifupdown2` parses this configuration because the same attributes are not in multiple `iface` stanzas.

```
cumulus@switch:~$ sudo cat /etc/network/interfaces

source /etc/network/interfaces.d/speed_settings

auto swp1
iface swp1
  address 10.0.14.2/24

cumulus@switch:~$ cat /etc/network/interfaces.d/speed_settings

auto swp1
iface swp1
  link-speed 1000
  link-duplex full
```

<!-- vale off -->
<!-- specific commands in title -->
### ifupdown2 and sysctl
<!-- vale on -->

For `sysctl` commands in the `pre-up`, `up`, `post-up`, `pre-down`, `down`, and `post-down` lines that use the
`$IFACE` variable, if the interface name contains a dot (.), `ifupdown2` does not change the name to work with `sysctl`. For example, the interface name `bridge.1` does not convert to `bridge/1`.

<!-- vale off -->
<!-- specific commands in title -->
### ifupdown2 and the gateway Parameter
<!-- vale on -->

The default route that the `gateway` parameter creates in ifupdown2 does not install in FRR, therefore does not redistribute into other routing protocols. Define a static default route instead, which installs in FRR and redistributes, if needed.

The following shows an example of the `/etc/network/interfaces` file when you use a static route instead of a gateway parameter:

```
auto swp2
iface swp2
address 172.16.3.3/24
up ip route add default via 172.16.3.2
```

### Interface Name Limitations

Interface names can be a maximum of 15 characters. You cannot use a number for the first character and you cannot include a dash (-) in the name. In addition, you cannot use any name that matches with the regular expression `.{0,13}\-v.*`.

If you encounter issues, remove the interface name from the `/etc/network/interfaces` file, then restart the `networking.service`.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
cumulus@switch:~$ sudo systemctl restart networking.service
```

### IP Address Scope

`ifupdown2` does not honor the configured IP address scope setting in the `/etc/network/interfaces` file and treats all addresses as global. It does not report an error. Consider this example configuration:

```
auto swp2
iface swp2
    address 35.21.30.5/30
    address 3101:21:20::31/80
    scope link
```

When you run `ifreload -a` on this configuration, `ifupdown2` considers all IP addresses as global.

```
cumulus@switch:~$ ip addr show swp2
5: swp2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
link/ether 74:e6:e2:f5:62:82 brd ff:ff:ff:ff:ff:ff
inet 35.21.30.5/30 scope global swp2
valid_lft forever preferred_lft forever
inet6 3101:21:20::31/80 scope global
valid_lft forever preferred_lft forever
inet6 fe80::76e6:e2ff:fef5:6282/64 scope link
valid_lft forever preferred_lft forever
```

To work around this issue, configure the IP address scope:

{{< tabs "TabID589 ">}}
{{< tab "NVUE Commands ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, configure the IP address scope using `post-up ip address add <address> dev <interface> scope <scope>`. For example:

```
auto swp6
iface swp6
    post-up ip address add 71.21.21.20/32 dev swp6 scope site
```

Then run the `ifreload -a` command on this configuration.

{{< /tab >}}
{{< /tabs >}}

The following configuration shows the correct scope:

```
cumulus@switch:~$ ip addr show swp6
9: swp6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
link/ether 74:e6:e2:f5:62:86 brd ff:ff:ff:ff:ff:ff
inet 71.21.21.20/32 scope site swp6
valid_lft forever preferred_lft forever
inet6 fe80::76e6:e2ff:fef5:6286/64 scope link
valid_lft forever preferred_lft forever
```

## Related Information

- {{<link url="Troubleshoot-Layer-1">}}
- {{<exlink url="http://wiki.debian.org/NetworkConfiguration" text="Debian - Network Configuration">}}
