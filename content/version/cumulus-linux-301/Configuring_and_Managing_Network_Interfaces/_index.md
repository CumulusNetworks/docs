---
title: Configuring and Managing Network Interfaces
author: Cumulus Networks
weight: 19
aliases:
 - /display/CL30/Configuring+and+Managing+Network+Interfaces
 - /pages/viewpage.action?pageId=5118370
pageID: 5118370
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
`ifupdown` is the network interface manager for Cumulus Linux. Cumulus
Linux 2.1 and later uses an updated version of this tool, `ifupdown2`.

For more information on network interfaces, see [Layer 1 and Switch Port
Attributes](/version/cumulus-linux-301/Configuring_and_Managing_Network_Interfaces/Layer_1_and_Switch_Port_Attributes).

{{%notice info%}}

By default, `ifupdown` is quiet; use the verbose option `-v` when you
want to know what is going on when bringing an interface down or up.

{{%/notice%}}

## <span>Commands</span>

  - ifdown

  - ifquery

  - ifreload

  - ifup

  - mako-render

## <span>Man Pages</span>

The following man pages have been updated for `ifupdown2`:

  - man ifdown(8)

  - man ifquery(8)

  - man ifreload

  - man ifup(8)

  - man ifupdown-addons-interfaces(5)

  - man interfaces(5)

## <span>Configuration Files</span>

  - /etc/network/interfaces

## <span>Basic Commands</span>

To bring up an interface or apply changes to an existing interface, run:

    cumulus@switch:~$ sudo ifup <ifname>

To bring down a single interface, run:

    cumulus@switch:~$ sudo ifdown <ifname>

Runtime Configuration (Advanced)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{%notice warning%}}</p>
<p>A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.</p>
<p>{{%/notice%}}</p>
<p>To administratively bring an interface up or down, run:</p>
<pre><code>cumulus@switch:~$ sudo ip link set dev swp1 {up|down}</code></pre>
<p>{{%notice note%}}</p>
<p>If you specified <em>manual</em> as the address family, you must bring up that interface manually using <code>ifconfig</code>. For example, if you configured a bridge like this:</p>
<pre><code>auto bridge01
iface bridge01 inet manual</code></pre>
<p>You can only bring it up by running <code>ifconfig bridge01 up</code>.</p>
<p>{{%/notice%}}</p></td>
</tr>
</tbody>
</table>

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

## <span id="src-5118370_ConfiguringandManagingNetworkInterfaces-classes" class="confluence-anchor-link"></span><span>ifupdown2 Interface Classes</span>

`ifupdown2` provides for the grouping of interfaces into separate
classes, where a class is simply a user-defined label used to group
interfaces that share a common function (like uplink, downlink or
compute). You specify classes in `/etc/network/interfaces`.

The most common class users are familiar with is *auto*, which you
configure like this:

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
--allow-uplinks option, or still use the `-a` options since these
interfaces are also in the auto class:

    cumulus@switch:~$ sudo ifup --allow=uplinks 
    cumulus@switch:~$ sudo ifreload -a 

Another example where this feature is useful is if you're using
[Management
VRF](/version/cumulus-linux-301/Layer_3_Features/Management_VRF), you
can use the special interface class called *mgmt*, and put the
management interface into that class:

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

### <span>Bringing All auto Interfaces Up or Down</span>

You can easily bring up or down all interfaces marked with the common
`auto` class in `/etc/network/interfaces`. Use the `-a` option. For
further details, see individual man pages for `ifup(8)`, `ifdown(8)`,
`ifreload(8)`.

To administratively bring up all interfaces marked auto, run:

    cumulus@switch:~$ sudo ifup -a

To administratively bring down all interfaces marked auto, run:

    cumulus@switch:~$ sudo ifdown -a

To reload all network interfaces marked `auto`, use the `ifreload`
command, which is equivalent to running `ifdown` then `ifup`, the one
difference being that `ifreload` skips any configurations that didn't
change):

    cumulus@switch:~$ sudo ifreload -a

## <span>Configuring a Loopback Interface</span>

Cumulus Linux has a loopback preconfigured in `/etc/network/interfaces`.
When the switch boots up, it has a loopback interface, called *lo*,
which is up and assigned an IP address of 127.0.0.1.

{{%notice tip%}}

The loopback interface *lo* must always be specified in
`/etc/network/interfaces` and must always be up.

{{%/notice%}}

<span id="src-5118370_ConfiguringandManagingNetworkInterfaces-ip"></span>ifupdown
Behavior with Child Interfaces

By default, `ifupdown` recognizes and uses any interface present on the
system — whether a VLAN, bond or physical interface — that is listed as
a dependent of an interface. You are not required to list them in the
`interfaces` file unless they need a specific configuration, for [MTU,
link speed, and so
forth](/version/cumulus-linux-301/Configuring_and_Managing_Network_Interfaces/Layer_1_and_Switch_Port_Attributes).
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

### <span>ifup Handling of Upper (Parent) Interfaces</span>

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

## <span>Configuring IP Addresses</span>

In `/etc/network/interfaces`, list all IP addresses as shown below under
the `iface` section (see `man interfaces` for more information):

    auto swp1
    iface swp1
        address 12.0.0.1/30
        address 12.0.0.2/30

The address method and address family are not mandatory. They default to
`inet/inet6` and `static`, but `inet/inet6` **must** be specified if you
need to specify `dhcp` or `loopback`:

    auto lo
    iface lo inet loopback

You can specify both IPv4 and IPv6 addresses in the same `iface` stanza:

    auto swp1
    iface swp1
        address 192.0.2.1/30
        address 192.0.2.2/30
        address 2001:DB8::1/126

Runtime Configuration (Advanced)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{%notice warning%}}</p>
<p>A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.</p>
<p>{{%/notice%}}</p>
<p>To make non-persistent changes to interfaces at runtime, use <code>ip addr add</code>:</p>
<pre><code>cumulus@switch:~$ sudo ip addr add 192.0.2.1/30 dev swp1
cumulus@switch:~$ sudo ip addr add 2001:DB8::1/126 dev swp1</code></pre>
<p>To remove an addresses from an interface, use <code>ip addr del</code>:</p>
<pre><code>cumulus@switch:~$ sudo ip addr del 192.0.2.1/30 dev swp1
cumulus@switch:~$ sudo ip addr del 2001:DB8::1/126 dev swp1</code></pre>
<p>See <code>man ip</code> for more details on the options available to manage and query interfaces.</p></td>
</tr>
</tbody>
</table>

To show the assigned address on an interface, use `ip addr show`:

    cumulus@switch:~$ ip addr show dev swp1
    3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
        inet 192.0.2.1/30 scope global swp1
       inet 192.0.2.2/30 scope global swp1
        inet6 2001:DB8::1/126 scope global tentative
           valid_lft forever preferred_lft forever

### <span>Purging Existing IP Addresses on an Interface</span>

By default, `ifupdown2` purges existing IP addresses on an interface. If
you have other processes that manage IP addresses for an interface, you
can disable this feature including the `address-purge` setting in the
interface's configuration. For example, add the following to the
interface configuration in `/etc/network/interfaces`:

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
Errata](#src-5118370_ConfiguringandManagingNetworkInterfaces-caveats)
section below for some cautions about using multiple `iface` stanzas for
the same interface.

{{%/notice%}}

## <span>Specifying User Commands</span>

You can specify additional user commands in the `interfaces` file. As
shown in the example below, the interface stanzas in
`/etc/network/interfaces` can have a command that runs at pre-up, up,
post-up, pre-down, down, and post-down:

    auto swp1
    iface swp1
        address 12.0.0.1/30
        up /sbin/foo bar

Any valid command can be hooked in the sequencing of bringing an
interface up or down, although commands should be limited in scope to
network-related commands associated with the particular interface.

For example, it wouldn't make sense to install some Debian package on
`ifup` of swp1, even though that is technically possible. See `man
interfaces` for more details.

## <span>Sourcing Interface File Snippets</span>

Sourcing interface files helps organize and manage the `interfaces(5)`
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

## <span>Using Globs for Port Lists</span>

Some modules support globs to define port lists (that is, a range of
ports). You can use the `glob` keyword to specify bridge ports and bond
slaves:

    auto br0
    iface br0
        bridge-ports glob swp1-6.100
    
    auto br1
    iface br1
        bridge-ports glob swp7-9.100  swp11.100 glob swp15-18.100

## <span>Using Templates</span>

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

## <span>Adding Descriptions to Interfaces</span>

You can add descriptions to the interfaces configured in
`/etc/network/interfaces` by using the *alias* keyword. For example:

    auto swp1
    iface swp1
        alias swp1 hypervisor_port_1

You can query interface descriptions by running `ip link show`. The
alias appears on the `alias` line:

    cumulus@switch$ ip link show swp1
    3: swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500
        link/ether aa:aa:aa:aa:aa:bc brd ff:ff:ff:ff:ff:ff
        alias hypervisor_port_1

Interface descriptions also appear in the [SNMP
OID](Monitoring_System_Hardware.html#src-5118231_MonitoringSystemHardware-snmp)
[IF-MIB::ifAlias](http://www.net-snmp.org/docs/mibs/ifMIBObjects.html#ifAlias).

{{%notice note%}}

Aliases are limited to 256 characters.

{{%/notice%}}

<span id="src-5118370_ConfiguringandManagingNetworkInterfaces-caveats"></span>

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
    
    source /etc/interfaces.d/speed_settings
    
    auto swp1
    iface swp1
      address 10.0.14.2/24

As well as `/etc/interfaces.d/speed_settings`

    cumulus@switch:~$ cat /etc/interfaces.d/speed_settings
    
    auto swp1
    iface swp1
      link-speed 1000
      link-duplex full

`ifupdown2` correctly parses a configuration like this because the same
attributes are not specified in multiple `iface` stanzas.

And, as stated in the note above, you cannot purge existing addresses on
interfaces with multiple `iface` stanzas.

## <span>Useful Links</span>

  - <http://wiki.debian.org/NetworkConfiguration>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan>
