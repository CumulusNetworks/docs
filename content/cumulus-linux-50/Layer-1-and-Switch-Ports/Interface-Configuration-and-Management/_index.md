---
title: Interface Configuration and Management
author: NVIDIA
weight: 290
toc: 3
---
This section discusses how to configure and manage network interfaces.

Cumulus Linux uses `ifupdown2` to manage network interfaces, which is a new implementation of the Debian network interface manager `ifupdown`.

## Basic Commands

### Bring up the Physical Connection to an Interface

To bring up the physical connection to an interface or apply changes to an existing interface, run the `sudo ifup <interface>` command. The following example command brings up the physical connection to swp1:

```
cumulus@switch:~$ sudo ifup swp1
```

To bring down the physical connection to a single interface, run the `sudo ifdown <interface>` command. The following example command brings down the physical connection to swp1:

```
cumulus@switch:~$ sudo ifdown swp1
```

The `ifdown` command always deletes logical interfaces after bringing them down. When you bring down the physical connection to an interface, it is brought back up automatically after any future reboots or configuration changes with `ifreload -a`.

{{%notice note%}}
By default, `ifupdown` is quiet. Use the verbose option (`-v`) to show commands as they are executed when bringing an interface down or up.
{{%/notice%}}

### Bring up an Interface Administratively

When you bring an interface up or down administratively (admin up or admin down), you bring down a port, bridge, or bond but not the physical connection for the port, bridge, or bond.

When you put an interface into an admin down state, the interface *remains down* after any future reboots or configuration changes with `ifreload -a`.

{{< tabs "TabID39 ">}}
{{< tab "CUE Commands ">}}

To put an interface into an admin *down* state:

```
cumulus@switch:~$ cl set interface swp1 link state down
cumulus@switch:~$ cl config apply
```

To bring the interface back *up*:

```
cumulus@switch:~$ cl set interface swp1 link state up
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

To put an interface into an admin *down* state:

```
cumulus@switch:~$ net add interface swp1 link down
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To bring the interface back *up*:

```
cumulus@switch:~$ net del interface swp1 link down
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To put an interface into an *admin* *down* state:

```
cumulus@switch:~$ sudo ifdown swp1 --admin-state
```

To bring the interface back *up*:

```
cumulus@switch:~$ sudo ifup swp1 --admin-state
```

{{< /tab >}}
{{< /tabs >}}

For additional information on interface administrative state and physical state, refer to {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Monitoring/Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux/" text="this knowledge base article">}}.

## Interface Classes

`ifupdown2` enables you to group interfaces into separate classes. A class is a user-defined label that groups interfaces that share a common function (such as uplink, downlink or compute). You specify classes in the `/etc/network/interfaces` file.

The most common class is *auto*, which you configure like this:

```
auto swp1
iface swp1
```

You can add other classes using the *allow* prefix. For example, if you have multiple interfaces used for uplinks, you can define a class called *uplinks:*

```
auto swp1
allow-uplink swp1
iface swp1 inet static
    address 10.1.1.1/31

auto swp2
allow-uplink swp2
iface swp2 inet static
    address 10.1.1.3/31
```

This allows you to perform operations on only these interfaces using the `--allow=uplinks` option. You can still use the `-a` options because these interfaces are also in the *auto* class:

```
cumulus@switch:~$ sudo ifup --allow=uplinks
cumulus@switch:~$ sudo ifreload -a
```

If you are using {{<link title="Management VRF">}}, you can use the special interface class called *mgmt* and put the management interface into that class. The management VRF must have an IPv6 address in addition to an IPv4 address to work correctly.

```
allow-mgmt eth0
iface eth0 inet dhcp
    vrf mgmt

allow-mgmt mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
```

All `ifupdown2` commands (`ifup`, `ifdown`, `ifquery`, `ifreload`) can take a class. Include the `--allow=<class>` option when you run the command. For example, to reload the configuration for the management interface described above, run:

```
cumulus@switch:~$ sudo ifreload --allow=mgmt
```

Use the `-a` option to bring up or down all interfaces that are marked with the common `auto` class in the
`/etc/network/interfaces` file.

To administratively bring up all interfaces marked `auto`, run:

```
cumulus@switch:~$ sudo ifup -a
```

To administratively bring down all interfaces marked `auto`, run:

```
cumulus@switch:~$ sudo ifdown -a
```

To reload all network interfaces marked `auto`, use the `ifreload` command. This command is equivalent to running `ifdown` then `ifup`; however, `ifreload` skips unchanged configurations:

```
cumulus@switch:~$ sudo ifreload -a
```

{{%notice note%}}
Certain syntax checks are done by default. As a precaution, apply configurations only if the syntax check passes. Use the following compound command:

```
cumulus@switch:~$ sudo bash -c "ifreload -s -a && ifreload -a"
```
{{%/notice%}}

For more information, see the individual man pages for `ifup(8)`, `ifdown(8)`, `ifreload(8)`.

## Loopback Interface

Cumulus Linux has a preconfigured loopback interface. When the switch boots up, the loopback interface called *lo* is up and assigned an IP address of 127.0.0.1.

{{%notice note%}}
The loopback interface *lo* must always exist and must always be up.
{{%/notice%}}

You can configure multiple IP addresses for the loopback interface:

{{< tabs "TabID196 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface lo ip address 172.16.2.1/24
cumulus@switch:~$ cl set interface lo ip address 10.0.0.1
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add loopback lo ip address 172.16.2.1/24
cumulus@switch:~$ net add loopback lo ip address 10.0.0.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add multiple `address` lines in the `/etc/network/interfaces` file:

```
auto lo
iface lo inet loopback
    address 10.0.0.1
    address 172.16.2.1/24
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
If the IP address is configured without a mask, the IP address automatically becomes a /32. For example, 10.1.1.1 is 10.1.1.1/32.
{{%/notice%}}

## Child Interfaces

By default, `ifupdown2` recognizes and uses any interface present on the system that is listed as a dependent (child) of an interface (for example, a VLAN, bond, or physical interface). You do not need to list interfaces in the `/etc/network/interfaces` file unless the interfaces need specific configuration for {{<link url="Switch-Port-Attributes" text="MTU, link speed, and so on">}}. If you need to delete a child interface, delete all references to that interface from the `/etc/network/interfaces` file.

In the following example, swp1 and swp2 do not need an entry in the `interfaces` file. The following stanzas defined in `/etc/network/interfaces` provide the exact same configuration:

**With Child Interfaces Defined**:

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
    bridge-stp on</code></pre></td>
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

`ifupdown2` understands interface dependency relationships. When you run `ifup` and `ifdown` with all interfaces, the commands always run with all interfaces in dependency order. When you run `ifup` and `ifdown` with the interface list on the command line, the default behavior is to *not* run with dependents; however, if there are any built-in dependents, they will be brought up or down.

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

To guide you through which interfaces will be brought down and up, use the `--print-dependency` option.

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

You can use `dot` to render the graph on an external system where `dot` is installed.

{{< img src = "/images/cumulus-linux/layer1-interfaces.png" >}}

To print the dependency information of the entire `interfaces` file, run the following command:

```
cumulus@switch:~$ sudo ifquery --print-dependency=dot -a >interfaces_all.dot
```

{{< img src = "/images/cumulus-linux/layer1-interfaces-all.png" >}}

## Subinterfaces

On Linux, an *interface* is a network device that can be either physical, (for example, swp1) or virtual (for example, vlan100). A *VLAN subinterface* is a VLAN device on an interface, and the VLAN ID is appended to the parent interface using dot (.) VLAN notation. For example, a VLAN with ID 100 that is a subinterface of swp1 is named swp1.100. The dot VLAN notation for a VLAN device name is a standard way to specify a VLAN device on Linux.

A VLAN subinterface only receives traffic  {{<link url="VLAN-Tagging" text="tagged">}} for that VLAN; therefore, swp1.100 only receives packets tagged with VLAN 100 on switch port swp1. Any packets transmitted from swp1.100 are tagged with VLAN 100.

In an {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} configuration, the peer link interface that connects the two switches in the MLAG pair has a VLAN subinterface named 4094. The peerlink.4094 subinterface only receives traffic tagged for VLAN 4094.

## Parent Interfaces

When you run `ifup` on a logical interface (like a bridge, bond, or VLAN interface), if the `ifup` results in the creation of the logical interface, it implicitly tries to execute on the interface's upper (or parent) interfaces as well.

Consider this example configuration:

```
auto br100
iface br100
    bridge-ports bond1.100 bond2.100

auto bond1
iface bond1
    bond-slaves swp1 swp2
```

If you run `ifdown bond1`, `ifdown` deletes bond1 and the VLAN interface on bond1 (bond1.100); it also removes bond1 from the bridge br100. Next, when you run `ifup bond1`, it creates bond1 and the VLAN interface on bond1 (bond1.100); it also executes `ifup br100` to add the bond VLAN interface (bond1.100) to the bridge br100.

There can be cases where an upper interface (like br100) is not in the right state, which can result in warnings. The warnings are mostly harmless.

If you want to disable these warnings, set `skip_upperifaces=1` in the `/etc/network/ifupdown2/ifupdown2.conf` file.

With `skip_upperifaces=1`, you have to explicitly execute `ifup` on the upper interfaces. In this case, you will have to run `ifup br100` after an `ifup bond1` to add bond1 back to bridge br100.

{{%notice note%}}
Although specifying a subinterface like swp1.100 and then running `ifup swp1.100` results in the automatic creation of the swp1 interface in the kernel, consider also specifying the parent interface swp1. A parent interface is one where any physical layer configuration can reside, such as `link-speed 1000` or `link-duplex full`. If you only create swp1.100 and not swp1, then you cannot run `ifup swp1` because you did not specify it.
{{%/notice%}}

## Interface IP Addresses

You can specify both IPv4 and IPv6 addresses for the same interface.

For IPv6 addresses, you can create or modify the IP address for an interface using either `::` or `0:0:0` notation. For example,both 2620:149:43:c109:0:0:0:5 and 2001:DB8::1/126 are valid.

The following example commands configure three IP addresses for swp1; two IPv4 addresses and one IPv6 address.

{{< tabs "TabID464 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface swp1 ip address 10.0.0.1/30
cumulus@switch:~$ cl set interface swp1 ip address 10.0.0.2/30
cumulus@switch:~$ cl set interface swp1 ip address 2001:DB8::1/126
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp1 ip address 10.0.0.1/30
cumulus@switch:~$ net add interface swp1 ip address 10.0.0.2/30
cumulus@switch:~$ net add interface swp1 ipv6 address 2001:DB8::1/126
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

NCLU adds the address method and address family when needed (for example, when you create DHCP or loopback interfaces).

```
auto lo
iface lo inet loopback
```

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

## Interface Descriptions

You can add a description (alias) to an interface.

Interface descriptions also appear in the {{<link url="Simple-Network-Management-Protocol-SNMP" text="SNMP">}} OID {{<exlink url="https://cumulusnetworks.com/static/mibs/IF-MIB.txt" text="IF-MIB::ifAlias">}}.

{{%notice note%}}
- Interface descriptions are limited to 256 characters.
- Avoid using apostrophes or non-ASCII characters. Cumulus Linux does not parse these characters.
{{%/notice%}}

The following example commands create a description for swp1:

{{< tabs "TabID838 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp1 alias hypervisor_port_1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, add a description using the *alias* keyword:

```
cumulus@switch:~# sudo nano /etc/network/interfaces

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
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp1 post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
cumulus@switch:~$ net add interface ip address 10.0.0.1/30
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice warning%}}
If your `post-up` command also starts, restarts, or reloads any `systemd` service, you must use the `--no-block` option with `systemctl`. Otherwise, that service or even the switch itself might hang after starting or restarting. For example, to restart the `dhcrelay` service after bringing up VLAN 100, first run:
{{%/notice%}}

```
cumulus@switch:~$ net add vlan 100 post-up systemctl --no-block restart dhcrelay.service
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~# sudo nano /etc/network/interfaces
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

You can specify port ranges in commands (for example, swp1-4,6,10-12).

{{< tabs "TabID725 ">}}
{{< tab "CUE Commands ">}}

Use commas to separate different port ranges (for example, swp1-46,10-12):

```
cumulus@switch:~$ cl set interface swp1-4,6,10-12 bridge domain br_default
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

Use commas to separate different port ranges in the command:

```
cumulus@switch:~$ net add bridge bridge ports swp1-4,6,10-12
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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

## Mako Templates

`ifupdown2` supports {{<exlink url="http://www.makotemplates.org/" text="Mako-style templates">}}. The Mako template engine is run over the `interfaces` file before parsing.

{{%notice warning%}}

While `ifupdown2` supports Mako templates, NCLU does not understand them. As a result, NCLU cannot read or write to the `/etc/network/interfaces` file.

{{%/notice%}}

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

For more Mako template examples, refer to this {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Automation/Configure-the-interfaces-File-with-Mako/" text="knowledge base article">}}.

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

- `$IFACE` represents the physical name of the interface being processed; for example, `br0` or vxlan42. The name is obtained from the `/etc/network/interfaces` file.
- `$LOGICAL` represents the logical name (configuration name) of the interface being processed.
- `$METHOD` represents the address method; for example, loopback, DHCP, DHCP6, manual, static, and so on.
- `$ADDRFAM` represents the address families associated with the interface, formatted in a comma-separated list for example, `"inet,inet6"`.

## Troubleshooting

To see the link and administrative state of an interface:

{{< tabs "TabID875 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl show interface swp1 link state
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

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
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl show interface swp1 ip address
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
{{< tab "CUE Commands ">}}

```
cumulus@switch$ cl show interface swp1
```

To show the interface description (alias) for all interfaces on the switch:

```
cumulus@switch$ NEED COMMAND
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch$ net show interface swp1
    Name   MAC                Speed     MTU   Mode
--  ----   -----------------  -------   -----  ---------
UP  swp1   44:38:39:00:00:04  1G        1500   Access/L2
Alias
-----
hypervisor_port_1
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

To see the status of the loopback interface (lo):

{{< tabs "TabID951 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl show interface lo
                         running      applied   description
-----------------------  -----------  --------  ----------------------------------------------------------------------
type                     loopback     loopback  The type of interface
ip
  vrf                                 default   Virtual routing and forwarding
  [address]              127.0.0.1/8            ipv4 and ipv6 address
  [address]              ::1/128
  ipv4
    forward                           on        Enable or disable forwarding.
  ipv6
    enable                            on        Turn the feature 'on' or 'off'.  The default is 'on'.
    forward                           on        Enable or disable forwarding.
link
  mtu                    65536                  interface mtu
  state                  up                     The state of the interface
  stats
    carrier-transitions  0                      Number of times the interface state has transitioned between up and...
    in-bytes             27211641               total number of bytes received on the interface
    in-drops             0                      number of received packets dropped
    in-errors            0                      number of received packets with errors
    in-pkts              413828                 total number of packets received on the interface
    out-bytes            27211641               total number of bytes transmitted out of the interface
    out-drops            0                      The number of outbound packets that were chosen to be discarded eve...
    out-errors           0                      The number of outbound packets that could not be transmitted becaus...
    out-pkts             413828                 total number of packets transmitted out of the interface
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net show interface lo
    Name    MAC                Speed    MTU    Mode
--  ------  -----------------  -------  -----  --------
UP  lo      00:00:00:00:00:00  N/A      65536  Loopback
Alias
-----
loopback interface
IP Details
-------------------------  --------------------
IP:                        127.0.0.1/8, ::1/128
IP Neighbor(ARP) Entries:  0
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ ip addr show lo
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
        valid_lft forever preferred_lft forever
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

Even though `ifupdown2` supports the inclusion of multiple `iface` stanzas for the same interface, use a single `iface` stanza for each interface. If you must specify more than one `iface` stanza; for example, if the configuration for a single interface comes from many places, like a template or a sourced file, make sure the stanzas do not specify the same interface attributes. Otherwise, unexpected behavior can result.

In the following example, swp1 is configured in two places: the `/etc/network/interfaces` file and the `/etc/network/interfaces.d/speed_settings` file. `ifupdown2` correctly parses this configuration because the same attributes are not specified in multiple `iface` stanzas.

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

### ifupdown2 and sysctl

For `sysctl` commands in the `pre-up`, `up`, `post-up`, `pre-down`, `down`, and `post-down` lines that use the
`$IFACE` variable, if the interface name contains a dot (.), `ifupdown2` does not change the name to work with `sysctl`. For example, the interface name `bridge.1` is not converted to `bridge/1`.

### ifupdown2 and the gateway Parameter

The default route created by the `gateway` parameter in ifupdown2 is not installed in FRRouting, therefore cannot be redistributed into other routing protocols. Define a static default route instead, which is installed in FRR and redistributed, if needed.

The following shows an example of the `/etc/network/interfaces` file when you use a static route instead of a gateway parameter:

```
auto swp2
iface swp2
address 172.16.3.3/24
up ip route add default via 172.16.3.2
```

### Interface Name Limitations

Interface names are limited to 15 characters in length, the first character cannot be a number and the name cannot include a dash (-). In addition, any name that matches with the regular expression `.{0,13}\-v.*` is not supported.

If you encounter issues, remove the interface name from the `/etc/network/interfaces` file, then restart the `networking.service`.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
cumulus@switch:~$ sudo systemctl restart networking.service
```

### IP Address Scope

`ifupdown2` does not honor the configured IP address scope setting in the `/etc/network/interfaces` file, treating all addresses as global. It does not report an error. Consider this example configuration:

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
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp6 post-up ip address add 71.21.21.20/32 dev swp6 scope site
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

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
- {{<exlink url="http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding" text="Linux Foundation - Bonds">}}
- {{<exlink url="http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan" text="Linux Foundation - VLANs">}}
- man ifdown(8)
- man ifquery(8)
- man ifreload
- man ifup(8)
- man ifupdown-addons-interfaces(5)
- man interfaces(5)
