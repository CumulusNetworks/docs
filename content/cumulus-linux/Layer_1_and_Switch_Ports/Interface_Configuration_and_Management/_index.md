---
title: Interface Configuration and Management
author: Cumulus Networks
weight: 91
aliases:
 - /display/DOCS/Interface+Configuration+and+Management
 - /pages/viewpage.action?pageId=8363023
pageID: 8363023
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
`ifupdown` is the network interface manager for Cumulus Linux. Cumulus
Linux uses an updated version of this tool, `ifupdown2`.

For more information on network interfaces, see [Switch Port
Attributes](/cumulus-linux/Layer_1_and_Switch_Ports/Interface_Configuration_and_Management/Switch_Port_Attributes).

{{%notice info%}}

By default, `ifupdown` is quiet; use the verbose option `-v` when you
want to know what is going on when bringing an interface down or up.

{{%/notice%}}

## <span>Basic Commands</span>

To bring up an interface or apply changes to an existing interface, run:

    cumulus@switch:~$ sudo ifup <ifname>

To bring down a single interface, run:

    cumulus@switch:~$ sudo ifdown <ifname>

{{%notice info%}}

`ifdown` always deletes logical interfaces after bringing them down. Use
the `--admin-state` option if you only want to administratively bring
the interface up or down.

{{%/notice%}}

To see the link and administrative state, use the `ip link show`
command:

    cumulus@switch:~$ ip link show dev swp1 
    3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff

In this example, swp1 is administratively UP and the physical link is UP
(LOWER\_UP flag). More information on interface administrative state and
physical state can be found in [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/202693826).

To put an interface into an admin down state. The interface remains down
after any future reboots or applying configuration changes with
`ifreload -a`. For example:

    cumulus@switch:~$ net add interface swp1 link down

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
        link-down yes

## <span id="src-8363023_InterfaceConfigurationandManagement-classes" class="confluence-anchor-link"></span><span>ifupdown2 Interface Classes</span>

`ifupdown2` provides for the grouping of interfaces into separate
classes, where a class is a user-defined label that groups interfaces
sharing a common function (like uplink, downlink or compute). You
specify classes in the `/etc/network/interfaces` file.

The most common class is *auto*, which you configure like this:

    auto swp1
    iface swp1

You can add other classes using the *allow* prefix. For example, if you
have multiple interfaces used for uplinks, you can make up a class
called *uplinks:*

    auto swp1
    allow-uplink swp1
    iface swp1 inet static
        address 10.1.1.1/31
     
    auto swp2
    allow-uplink swp2
    iface swp2 inet static
        address 10.1.1.3/31

This allows you to perform operations on only these interfaces using the
`--allow=uplinks` option, or still use the `-a` options since these
interfaces are also in the auto class:

    cumulus@switch:~$ sudo ifup --allow=uplinks 
    cumulus@switch:~$ sudo ifreload -a 

If you are using [Management
VRF](/cumulus-linux/Layer_3/Management_VRF), you can use the special
interface class called *mgmt*, and put the management interface into
that class.

{{%notice warning%}}

The mgmt interface class is not supported if you are configuring Cumulus
Linux using
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU).

{{%/notice%}}

    allow-mgmt eth0
    iface eth0 inet dhcp
        vrf mgmt
      
    allow-mgmt mgmt
    iface mgmt
        address 127.0.0.1/8
        vrf-table auto

All `ifupdown2` commands (`ifup`, `ifdown`, `ifquery`, `ifreload`) can
take a class. Include the `--allow=<class>` option when you run the
command. For example, to reload the configuration for the management
interface described above, run:

    cumulus@switch:~$ sudo ifreload --allow=mgmt 

You can easily bring up or down all interfaces marked with the common
`auto` <span style="color: #333333;"> class in </span>
`/etc/network/interfaces` <span style="color: #333333;"> . Use the
</span> `-a` <span style="color: #333333;"> option. For further details,
see individual man pages for </span> `ifup(8)`
<span style="color: #333333;"> , </span> `ifdown(8)`
<span style="color: #333333;"> , </span> `ifreload(8)`
<span style="color: #333333;"> . </span>

To administratively bring up all interfaces marked auto, run:

    cumulus@switch:~$ sudo ifup -a

To administratively bring down all interfaces marked auto, run:

    cumulus@switch:~$ sudo ifdown -a

To reload all network interfaces marked `auto`, use the `ifreload`
command, which is equivalent to running `ifdown` then `ifup`, the one
difference being that `ifreload` skips any configurations that didn't
change):

    cumulus@switch:~$ sudo ifreload -a

{{%notice tip%}}

Some syntax checks are done by default, however it may be safer to apply
the configs only if the syntax check passes, using the following
compound command:

    cumulus@switch:~$ sudo bash -c "ifreload -s -a && ifreload -a"

{{%/notice%}}

## <span id="src-8363023_InterfaceConfigurationandManagement-loopback" class="confluence-anchor-link"></span><span>Configure a Loopback Interface</span>

Cumulus Linux has a loopback preconfigured in `/etc/network/interfaces`.
When the switch boots up, it has a loopback interface, called *lo*,
which is up and assigned an IP address of 127.0.0.1.

{{%notice tip%}}

The loopback interface *lo* must always be specified in
`/etc/network/interfaces` and must always be up.

{{%/notice%}}

## <span id="src-8363023_InterfaceConfigurationandManagement-ip" class="confluence-anchor-link"></span><span>ifupdown Behavior with Child Interfaces</span>

By default, `ifupdown` recognizes and uses any interface present on the
system — whether a VLAN, bond or physical interface — that is listed as
a dependent of an interface. You are not required to list them in the
`interfaces` file unless they need a specific configuration, for [MTU,
link speed, and so
forth](/cumulus-linux/Layer_1_and_Switch_Ports/Interface_Configuration_and_Management/Switch_Port_Attributes).
And if you need to delete a child interface, you should delete all
references to that interface from the `interfaces` file.

For this example, swp1 and swp2 below do not need an entry in the
`interfaces` file. The following stanzas defined in
`/etc/network/interfaces` provide the exact same configuration:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>With Child Interfaces Defined</strong></p>
<pre><code>auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 1-100
    bridge-pvid 1
    bridge-stp on</code></pre></td>
<td><p><strong>Without Child Interfaces Defined</strong></p>
<pre><code>auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 1-100
    bridge-pvid 1
    bridge-stp on</code></pre></td>
</tr>
</tbody>
</table>

Bridge in Traditional Mode - Example

For this example, swp1.100 and swp2.100 below do not need an entry in
the `interfaces` file. The following stanzas defined in
`/etc/network/interfaces` provide the exact same configuration:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>With Child Interfaces Defined</strong></p>
<pre><code>auto swp1.100
iface swp1.100
 
auto swp2.100
iface swp2.100
 
auto br-100
iface br-100
    address 10.0.12.2/24
    address 2001:dad:beef::3/64
    bridge-ports swp1.100 swp2.100
    bridge-stp on</code></pre></td>
<td><p><strong>Without Child Interfaces Defined</strong></p>
<pre><code>auto br-100
iface br-100
    address 10.0.12.2/24
    address 2001:dad:beef::3/64
    bridge-ports swp1.100 swp2.100
    bridge-stp on</code></pre></td>
</tr>
</tbody>
</table>

For more information on the bridge in traditional mode vs the bridge in
VLAN-aware mode, please read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/204909397).

## <span>ifupdown2 Interface Dependencies</span>

`ifupdown2` understands interface dependency relationships. When `ifup`
and `ifdown` are run with all interfaces, they always run with all
interfaces in dependency order. When run with the interface list on the
command line, the default behavior is to not run with dependents. But if
there are any built-in dependents, they will be brought up or down.

To run with dependents when you specify the interface list, use the
`--with-depends` option. `--with-depends` walks through all dependents
in the dependency tree rooted at the interface you specify. Consider the
following example configuration:

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

Using `ifup --with-depends br2001` brings up all dependents of br2001:
bond1.2001, bond2.2001, bond1, bond2, bond1.2001, bond2.2001, swp29,
swp30, swp31, swp32.

    cumulus@switch:~$ sudo ifup --with-depends br2001

Similarly, specifying `ifdown --with-depends br2001` brings down all
dependents of br2001: bond1.2001, bond2.2001, bond1, bond2, bond1.2001,
bond2.2001, swp29, swp30, swp31, swp32.

    cumulus@switch:~$ sudo ifdown --with-depends br2001

{{%notice warning%}}

As mentioned earlier, `ifdown2` always deletes logical interfaces after
bringing them down. Use the `--admin-state` option if you only want to
administratively bring the interface up or down. In terms of the above
example, `ifdown br2001` deletes `br2001`.

{{%/notice%}}

To guide you through which interfaces will be brought down and up, use
the `--print-dependency` option to get the list of dependents.

Use `ifquery --print-dependency=list -a` to get the dependency list of
all interfaces:

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

To print the dependency list of a single interface, use:

    cumulus@switch:~$ sudo ifquery --print-dependency=list br2001
    br2001 : ['bond1.2001', 'bond2.2001']
    bond1.2001 : ['bond1']
    bond2.2001 : ['bond2']
    bond1 : ['swp29', 'swp30']
    bond2 : ['swp31', 'swp32']
    swp29 : None
    swp30 : None
    swp31 : None
    swp32 : None

To print the dependency information of an interface in `dot` format:

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

You can use `dot` to render the graph on an external system where `dot`
is installed.

{{% imgOld 0 %}}

To print the dependency information of the entire `interfaces` file:

    cumulus@switch:~$ sudo ifquery --print-dependency=dot -a >interfaces_all.dot

{{% imgOld 1 %}}

## <span id="src-8363023_InterfaceConfigurationandManagement-subinterface" class="confluence-anchor-link"></span><span>Subinterfaces</span>

On Linux an *interface* is a network device, and can be either a
physical device like switch port (such as swp1), or virtual, like a VLAN
(vlan100). A *VLAN subinterface* is a VLAN device on an interface, and
the VLAN ID is appended to the parent interface using dot (.) VLAN
notation. For example, a VLAN with ID 100 that is a subinterface of swp1
is named swp1.100 in Cumulus Linux. The dot VLAN notation for a VLAN
device name is a standard way to specify a VLAN device on Linux. Many
Linux configuration tools, most notably `ifupdown2` and its predecessor
`ifupdown`, recognize such a name as a VLAN interface name.

A VLAN subinterface only receives traffic
[tagged](/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/VLAN_Tagging)
for that VLAN, so swp1.100 only receives packets tagged with VLAN 100 on
switch port swp1. Similarly, any transmits from swp1.100 result in
tagging the packet with VLAN 100.

For an
[MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG)
deployment, the peerlink interface that connects the two switches in the
MLAG pair has a VLAN subinterface named 4094 by default, provided you
configured the subinterface with
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU).
The peerlink.4094 subinterface only receives traffic tagged for VLAN
4094.

## <span>ifup and Upper (Parent) Interfaces</span>

When you run `ifup` on a logical interface (like a bridge, bond or VLAN
interface), if the `ifup` resulted in the creation of the logical
interface, by default it implicitly tries to execute on the interface's
upper (or parent) interfaces as well. This helps in most cases,
especially when a bond is brought down and up, as in the example below.
This section describes the behavior of bringing up the upper interfaces.

Consider this example configuration:

    auto br100
    iface br100
        bridge-ports bond1.100 bond2.100
     
    auto bond1
    iface bond1
        bond-slaves swp1 swp2

If you run `ifdown bond1`, `ifdown` deletes bond1 and the VLAN interface
on bond1 (bond1.100); it also removes bond1 from the bridge br100. Next,
when you run `ifup bond1`, it creates bond1 and the VLAN interface on
bond1 (bond1.100); it also executes `ifup br100` to add the bond VLAN
interface (bond1.100) to the bridge br100.

As you can see above, implicitly bringing up the upper interface helps,
but there can be cases where an upper interface (like br100) is not in
the right state, which can result in warnings. The warnings are mostly
harmless.

If you want to disable these warnings, you can disable the implicit
upper interface handling by setting `skip_upperifaces=1` in
`/etc/network/ifupdown2/ifupdown2.conf`.

With `skip_upperifaces=1`, you will have to explicitly execute `ifup` on
the upper interfaces. In this case, you will have to run `ifup br100`
after an `ifup bond1` to add bond1 back to bridge br100.

{{%notice note%}}

Although specifying a subinterface like swp1.100 and then running `ifup
swp1.100` will also result in the automatic creation of the swp1
interface in the kernel, Cumulus Networks recommends you specify the
parent interface swp1 as well. A parent interface is one where any
physical layer configuration can reside, such as `link-speed 1000` or
`link-duplex full`.

It's important to note that if you only create swp1.100 and not swp1,
then you cannot run `ifup swp1` since you did not specify it.

{{%/notice%}}

## <span id="src-8363023_InterfaceConfigurationandManagement-ip" class="confluence-anchor-link"></span><span>Configure IP Addresses</span>

IP addresses are configured with the `net add interface` command.

{{%notice info%}}

**Example IP Address Configuration**

The following commands configure three IP addresses for swp1: two IPv4
addresses, and one IPv6 address.

    cumulus@switch:~$ net add interface swp1 ip address 12.0.0.1/30
    cumulus@switch:~$ net add interface swp1 ip address 12.0.0.2/30
    cumulus@switch:~$ net add interface swp1 ipv6 address 2001:DB8::1/126
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet:

    auto swp1
    iface swp1
        address 12.0.0.1/30
        address 12.0.0.2/30
        address 2001:DB8::1/126

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

You can specify both IPv4 and IPv6 addresses for the same interface.

For IPv6 addresses, you can create or modify the IP address for an
interface using either "::" or "0:0:0" notation. Both of the following
examples are valid:

    cumulus@switch:~$ net add bgp neighbor 2620:149:43:c109:0:0:0:5 remote-as internal
    cumulus@switch:~$ 
    cumulus@switch:~$ net add interface swp1 ipv6 address 2001:DB8::1/126

{{%/notice%}}

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

The address method and address family are added by NCLU when needed,
specifically when you are creating DHCP or loopback interfaces.

    auto lo
    iface lo inet loopback

{{%/notice%}}

{{%/notice%}}

To show the assigned address on an interface, use `ip addr show`:

    cumulus@switch:~$ ip addr show dev swp1
    3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
        inet 192.0.2.1/30 scope global swp1
        inet 192.0.2.2/30 scope global swp1
        inet6 2001:DB8::1/126 scope global tentative
           valid_lft forever preferred_lft forever

### <span>Specify IP Address Scope </span>

`ifupdown2` does not honor the configured IP address scope setting in
`/etc/network/interfaces`, treating all addresses as global. It does not
report an error. Consider this example configuration:

    auto swp2
    iface swp2
        address 35.21.30.5/30
        address 3101:21:20::31/80
        scope link

When you run `ifreload -a` on this configuration, `ifupdown2` considers
all IP addresses as global.

    cumulus@switch:~$ ip addr show swp2
    5: swp2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 74:e6:e2:f5:62:82 brd ff:ff:ff:ff:ff:ff
    inet 35.21.30.5/30 scope global swp2
    valid_lft forever preferred_lft forever
    inet6 3101:21:20::31/80 scope global 
    valid_lft forever preferred_lft forever
    inet6 fe80::76e6:e2ff:fef5:6282/64 scope link 
    valid_lft forever preferred_lft forever

To work around this issue, configure the IP address scope:

{{%notice info%}}

**Example post-up Configuration**

    cumulus@switch:~$ net add interface swp6 post-up ip address add 71.21.21.20/32 dev swp6 scope site
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet in the
`/etc/network/interfaces` file:

    auto swp6
    iface swp6
        post-up ip address add 71.21.21.20/32 dev swp6 scope site

{{%/notice%}}

Now it has the correct scope:

    cumulus@switch:~$ ip addr show swp6
    9: swp6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 74:e6:e2:f5:62:86 brd ff:ff:ff:ff:ff:ff
    inet 71.21.21.20/32 scope site swp6
    valid_lft forever preferred_lft forever
    inet6 fe80::76e6:e2ff:fef5:6286/64 scope link 
    valid_lft forever preferred_lft forever

### <span>Purge Existing IP Addresses on an Interface</span>

By default, `ifupdown2` purges existing IP addresses on an interface. If
you have other processes that manage IP addresses for an interface, you
can disable this feature including the `address-purge` setting in the
interface's configuration.

    cumulus@switch:~$ net add interface swp1 address-purge no
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
        address-purge no

{{%notice note%}}

Purging existing addresses on interfaces with multiple `iface` stanzas
is not supported. Doing so can result in the configuration of multiple
addresses for an interface after you change an interface address and
reload the configuration with `ifreload -a`. If this happens, you must
shut down and restart the interface with `ifup` and `ifdown`, or
manually delete superfluous addresses with `ip address delete
specify.ip.address.here/mask dev DEVICE`. See also the [Caveats and
Errata](#src-8363023_InterfaceConfigurationandManagement-caveats)
section below for some cautions about using multiple `iface` stanzas for
the same interface.

{{%/notice%}}

## <span>Specify User Commands</span>

You can specify additional user commands in the `interfaces` file. As
shown in the example below, the interface stanzas in
`/etc/network/interfaces` can have a command that runs at pre-up, up,
post-up, pre-down, down, and post-down:

    cumulus@switch:~$ net add interface swp1 post-up /sbin/foo bar
    cumulus@switch:~$ net add interface ip address 12.0.0.1/30
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
        address 12.0.0.1/30
        post-up /sbin/foo bar

Any valid command can be hooked in the sequencing of bringing an
interface up or down, although commands should be limited in scope to
network-related commands associated with the particular interface.

For example, it wouldn't make sense to install some Debian package on
`ifup` of swp1, even though that is technically possible. See `man
interfaces` for more details.

{{%notice warning%}}

If your `post-up` command also starts, restarts or reloads any `systemd`
service, you must use the `--no-block` option with `systemctl`.
Otherwise, that service or even the switch itself may hang after
starting or restarting.

For example, to restart the `dhcrelay` service after bringing up VLAN
100, first run:

    cumulus@switch:~$ net add vlan 100 post-up systemctl --no-block restart dhcrelay.service

This command creates the following configuration in the
`/etc/network/interfaces` file:

    auto bridge
    iface bridge
        bridge-vids 100
        bridge-vlan-aware yes
     
    auto vlan100
    iface vlan100
        post-up systemctl --no-block restart dhcrelay.service
        vlan-id 100
        vlan-raw-device bridge

{{%/notice%}}

## <span>Source Interface File Snippets</span>

Sourcing interface files helps organize and manage the `interfaces`
file. For example:

    cumulus@switch:~$ cat /etc/network/interfaces
    # The loopback network interface
    auto lo
    iface lo inet loopback
     
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
     
    source /etc/network/interfaces.d/bond0

The contents of the sourced file used above are:

    cumulus@switch:~$ cat /etc/network/interfaces.d/bond0
    auto bond0
    iface bond0
        address 14.0.0.9/30
        address 2001:ded:beef:2::1/64
        bond-slaves swp25 swp26

## <span>Use Globs for Port Lists</span>

NCLU supports globs to define port lists (that is, a range of ports).
The `glob` keyword is implied when you specify bridge ports and bond
slaves:

    cumulus@switch:~$ net add bridge bridge ports swp1-4,6,10-12
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice tip%}}

While you must use commas to separate different ranges of ports in the
NCLU command, the /etc/network/interfaces file renders the list of ports
individually, as in the example output below.

{{%/notice%}}

These commands produce the following snippet in the
`/etc/network/interfaces` file:

    ...
     
    auto bridge
    iface bridge
        bridge-ports swp1 swp2 swp3 swp4 swp6 swp10 swp11 swp12
        bridge-vlan-aware yes
    auto swp1
    iface swp1
     
    auto swp2
    iface swp2
     
    auto swp3
    iface swp3
     
    auto swp4
    iface swp4
     
    auto swp6
    iface swp6
     
    auto swp10
    iface swp10
     
    auto swp11
    iface swp11
     
    auto swp12
    iface swp12

## <span>Use Templates</span>

`ifupdown2` supports [Mako-style
templates](http://www.makotemplates.org/). The Mako template engine is
run over the `interfaces` file before parsing.

Use the template to declare cookie-cutter bridges in the `interfaces`
file:

    %for v in [11,12]:
    auto vlan${v}
    iface vlan${v}
        address 10.20.${v}.3/24
        bridge-ports glob swp19-20.${v}
        bridge-stp on
    %endfor

And use it to declare addresses in the `interfaces` file:

    %for i in [1,12]:
    auto swp${i}
    iface swp${i}
        address 10.20.${i}.3/24

{{%notice note%}}

Regarding Mako syntax, use square brackets (`[1,12]`) to specify a list
of individual numbers (in this case, 1 and 12). Use `range(1,12)` to
specify a range of interfaces.

{{%/notice%}}

{{%notice tip%}}

You can test your template and confirm it evaluates correctly by running
`mako-render /etc/network/interfaces`.

{{%/notice%}}

{{%notice tip%}}

For more examples of configuring Mako templates, read this [knowledge
base
article](https://support.cumulusnetworks.com/hc/en-us/articles/202868023).

{{%/notice%}}

To comment out content in Mako templates, use double hash marks (\#\#).
For example:

    ## % for i in range(1, 4):
    ## auto swp${i}
    ## iface swp${i}
    ## % endfor
    ##

## <span>Run ifupdown Scripts under /etc/network/ with ifupdown2</span>

<span style="color: #434343;"> Unlike the traditional
<span style="color: #434343;"> `ifupdown` </span>
<span style="color: #434343;"> </span> </span>
<span style="color: #434343;"> system, `ifupdown2` </span>
<span style="color: #434343;"> does not </span>
<span style="color: #000000;"> run scripts installed in
`/etc/network/*/` </span> <span style="color: #242729;"> </span>
<span style="color: #434343;"> a </span> <span style="color: #000000;">
utomatically to configure network interfaces. </span>

<span style="color: #000000;"> <span style="color: #000000;"> To enable
or disable `ifupdown2` </span> <span style="color: #000000;"> scripting,
edit the <span style="color: #000000;"> `addon_scripts_support` </span>
</span> <span style="color: #000000;"> line
<span style="color: #000000;"> in the </span>
`/etc/network/ifupdown2/ifupdown2.conf` </span>
<span style="color: #000000;"> file. `1` </span>
<span style="color: #000000;"> enables scripting and `2` </span>
<span style="color: #000000;"> disables scripting. The following example
enables scripting. </span> </span>

<span style="color: #000000;"> <span style="color: #000000;"> </span>
</span>

    cumulus@switch:~$ sudo nano /etc/network/ifupdown2/ifupdown2.conf
    # Support executing of ifupdown style scripts.
    # Note that by default python addon modules override scripts with the same name
    addon_scripts_support=1

<span style="color: #000000;"> `ifupdown2` sets the following
environment variables when executing commands: </span>

  - <span style="color: #000000;"> <span style="color: #000000;">
    `$IFACE` represents the physical name of the interface being
    processed; for example, `br0` <span style="color: #000000;"> or
    </span> vxlan42. </span> </span> <span style="color: #000000;">
    <span style="color: #000000;"> <span style="color: #000000;"> The
    name is obtained from <span style="color: #000000;"> the </span>
    `/etc/network/interfaces` </span> <span style="color: #000000;">
    file. </span> </span> </span>

  - <span style="color: #000000;"> <span style="color: #000000;">
    <span style="color: #000000;"> `$LOGICAL`
    <span style="color: #000000;"> represents the logical name
    (configuration name) of the interface being processed. </span>
    </span> </span> </span>

  - <span style="color: #000000;"> <span style="color: #000000;">
    <span style="color: #000000;"> `$METHOD` </span> </span> </span>
    represents the address method; for example, loopback, DHCP, DHCP6,
    manual, static, and so on.

  - <span style="color: #000000;"> <span style="color: #000000;">
    <span style="color: #000000;"> `$ADDRFAM` r </span> </span> </span>
    epresents the address families associated with the interface,
    formatted in a comma-separated list; for example,
    <span style="color: #000000;"> </span> `"inet,inet6"`
    <span style="color: #000000;"> . </span>

## <span>Add Descriptions to Interfaces</span>

You can add descriptions to the interfaces configured in
`/etc/network/interfaces` by using the *alias* keyword.

{{%notice info%}}

**Example Alias Configuration**

The following commands create an alias for swp1:

    cumulus@switch:~$ net add interface swp1 alias hypervisor_port_1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet:

    auto swp1
    iface swp1
        alias hypervisor_port_1

{{%/notice%}}

You can query the interface description using NCLU:

    cumulus@switch$ net show interface swp1
        Name   MAC                Speed     MTU   Mode
    --  ----   -----------------  -------   -----  ---------
    UP  swp1   44:38:39:00:00:04  1G        1500   Access/L2
    Alias
    -----
    hypervisor_port_1

Interface descriptions also appear in the
[SNMP](/cumulus-linux/Monitoring_and_Troubleshooting/Simple_Network_Management_Protocol_\(SNMP\)_Monitoring/)
OID
[IF-MIB::ifAlias](https://cumulusnetworks.com/static/mibs/IF-MIB.txt).

{{%notice note%}}

Aliases are limited to 256 characters.

{{%/notice%}}

<span style="color: #000000;">
<span id="src-8363023_InterfaceConfigurationandManagement-show_alias"></span>To
show the interface description (alias) for all interfaces on the switch,
run the `net show interface alias` command. For example: </span>

    cumulus@switch:~$ net show interface alias
    State    Name            Mode              Alias
    -----    -------------   -------------     ------------------
    UP       bond01          LACP
    UP       bond02          LACP
    UP       bridge          Bridge/L2
    UP       eth0            Mgmt
    UP       lo              Loopback          loopback interface
    UP       mgmt            Interface/L3
    UP       peerlink        LACP
    UP       peerlink.4094   SubInt/L3
    UP       swp1            BondMember        hypervisor_port_1
    UP       swp2            BondMember        to Server02
    ...

<span style="color: #000000;"> To show the interface description for all
interfaces on the switch in JSON format, run the `net show interface
alias json` command. </span>

## <span>Caveats and Errata</span>

While `ifupdown2` supports the inclusion of multiple `iface` stanzas for
the same interface, Cumulus Networks recommends you use a single `iface`
stanza for each interface, if possible.

There are cases where you must specify more than one `iface` stanza for
the same interface. For example, the configuration for a single
interface can come from many places, like a template or a sourced file.

If you do specify multiple `iface` stanzas for the same interface, make
sure the stanzas do not specify the same interface attributes.
Otherwise, unexpected behavior can result.

For example, swp1 is configured in two places:

    cumulus@switch:~$ cat /etc/network/interfaces
     
    source /etc/network/interfaces.d/speed_settings
     
    auto swp1
    iface swp1
      address 10.0.14.2/24

As well as `/etc/network/interfaces.d/speed_settings`

    cumulus@switch:~$ cat /etc/network/interfaces.d/speed_settings
     
    auto swp1
    iface swp1
      link-speed 1000
      link-duplex full

`ifupdown2` correctly parses a configuration like this because the same
attributes are not specified in multiple `iface` stanzas.

And, as stated in the note above, you cannot purge existing addresses on
interfaces with multiple `iface` stanzas.

### <span>ifupdown2 and sysctl</span>

<span style="color: #000000;"> For sysctl commands in
<span style="color: #000000;"> the </span> `pre-up`
<span style="color: #000000;"> , `up` <span style="color: #000000;"> ,
</span> `post-up` </span> , <span style="color: #000000;"> </span>
`pre-down` <span style="color: #000000;"> , </span> `down`, and
<span style="color: #000000;"> </span> `post-down` lines that use the
`$IFACE` <span style="color: #000000;"> </span> </span>
<span style="color: #000000;"> variable, if the interface name contains
a dot (.), `ifupdown2` </span> <span style="color: #000000;"> does not
change the name to work with sysctl. For example, the interface name
`bridge.1` </span> <span style="color: #000000;"> is not converted to
<span style="color: #000000;"> `bridge/1` </span> </span>
<span style="color: #000000;"> . </span>

### <span>Long Interface Names</span>

<span style="color: #000000;"> The Linux kernel limits interface names
to 15 characters in length and cannot have a number as the first
character. Longer interface names can result in errors. To work around
this issue, remove the interface from the `/etc/network/interfaces`
file, then restart the networking.service. </span>

<span style="color: #000000;"> </span>

    cumulus@switch:~$ sudo vi /etc/network/interfaces
    cumulus@switch:~$ sudo systemctl restart networking.service

## <span>Related Information</span>

  - [Debian - Network
    Configuration](http://wiki.debian.org/NetworkConfiguration)

  - [Linux Foundation -
    Bonds](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)

  - [Linux Foundation -
    VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)

  - man ifdown(8)

  - man ifquery(8)

  - man ifreload

  - man ifup(8)

  - man ifupdown-addons-interfaces(5)

  - man interfaces(5)
