---
title: Management VRF
author: Cumulus Networks
weight: 195
aliases:
 - /display/CL34/Management+VRF
 - /pages/viewpage.action?pageId=7112679
pageID: 7112679
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
*Management VRF* is a subset of
[VRF](/version/cumulus-linux-343/Layer_Three/Virtual_Routing_and_Forwarding_-_VRF)
(virtual routing tables and forwarding) and provides a separation
between the out-of-band management network and the in-band data plane
network. For all VRFs, the *main* routing table is the default table for
all of the data plane switch ports. With management VRF, a second table,
*mgmt*, is used for routing through the Ethernet ports of the switch.
The *mgmt* name is special cased to identify the management VRF from a
data plane VRF. FIB rules are installed for DNS servers because this is
the typical deployment case.

Cumulus Linux only supports eth0 as the management interface, or eth1,
depending on the switch platform. The Ethernet ports are software-only
parts that are not hardware accelerated by `switchd`. VLAN
subinterfaces, bonds, bridges, and the front panel switch ports are not
supported as management interfaces.

When management VRF is enabled, logins to the switch are set into the
management VRF context. IPv4 and IPv6 networking applications (for
example, Ansible, Chef, and `apt-get`) run by an administrator
communicate out the management network by default. This default context
does not impact services run through `systemd` and the `systemctl`
command, and does not impact commands examining the state of the switch,
such as the `ip` command to list links, neighbors or routes.

{{%notice tip%}}

The management VRF configurations in this chapter contain a localhost
loopback IP address (127.0.0.1/8). Adding the loopback address to the L3
domain of the management VRF prevents issues with applications that
expect the loopback IP address to exist in the VRF, such as NTP.

{{%/notice%}}

## <span id="src-7112679_ManagementVRF-enablevrf" class="confluence-anchor-link"></span><span>Enabling Management VRF</span>

To enable management VRF on eth0, complete the following steps:

{{%notice info has%}}

**Example Management VRF Configuration**

The example NCLU commands below create a VRF called *mgmt*:

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info has%}}

To differentiate from a data plane VRF, you must name the management VRF
`mgmt`.

{{%/notice%}}

    cumulus@switch:~$ net add vrf mgmt
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The NCLU commands above create the following snippets in the
`/etc/network/interfaces` file:

    ...
     
    auto eth0
    iface eth0 inet dhcp
        vrf mgmt
     
    ...
     
    auto mgmt
    iface mgmt
        address 127.0.0.1/8
        vrf-table auto
     
    ...

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info has%}}

When you commit the change to add the management VRF, all connections
over eth0 are dropped. This can impact any automation that might be
running, such as Ansible or Puppet scripts.

{{%/notice%}}

{{%/notice%}}

### <span>Bringing the Management VRF Up after Downing It with ifdown</span>

If you take down the management VRF using `ifdown`, to bring it back up
you need to do one of two things:

  - Use `ifup --with-depends <vrf>`

  - Use `ifreload -a`

For example:

    cumulus@switch:~$ sudo ifdown mgmt
    cumulus@switch:~$ sudo ifup --with-depends mgmt

{{%notice note%}}

Running `ifreload -a` disconnects the session for any interface
configured as *auto*.

{{%/notice%}}

## <span id="src-7112679_ManagementVRF-services" class="confluence-anchor-link"></span><span>Running Services within the Management VRF</span>

You can run a variety of services within the management VRF instead of
the default VRF. In most cases, you must stop and disable the instance
running in the default VRF before you can start the service in the
management VRF. This is because the instance running in the default VRF
owns the port across all VRFs. The list of services that you must
disable in the default VRF are:

  - chef-client

  - collectd

  - dhcpd

  - dhcrelay

  - hsflowd

  - netq-agent

  - ntp

  - puppet

  - snmpd

  - snmptrapd

  - ssh

  - zabbix-agent

When you run a service inside the management VRF, that service runs
**only** on eth0 and no longer on any switch port. However, you can keep
the service running in the default VRF with a wildcard for
[agentAddress](SNMP_Monitoring.html#src-7112365_SNMPMonitoring-agentAddress).
This enables the service to run on **all** interfaces no matter which
VRF, so you don't have to run a different process for each VRF.

Some applications can work across all VRFs. The kernel provides a sysctl
that allows a single instance to accept connections over all VRFs. For
TCP, connected sockets are bound to the VRF on which the first packet
was received. This sysctl is enabled for Cumulus Linux.

To enable a service to run in the management VRF, do the following.
These steps use the NTP service, but you can use any of the services
listed above, except for `dhcrelay` (discussed
[here](Configuring_DHCP_Relays.html#src-7112627_ConfiguringDHCPRelays-multiple))
and `hsflowd` (discussed [below](#src-7112679_ManagementVRF-hsflowd)).

1.  Configure the management VRF as described in the Enabling Management
    VRF section above.

2.  If NTP is running, stop the service:
    
        cumulus@switch:~$ sudo systemctl stop ntp.service

3.  Disable NTP from starting automatically in the default VRF:
    
        cumulus@switch:~$ sudo systemctl disable ntp.service

4.  Start NTP in the mgmt VRF.
    
        cumulus@switch:~$ sudo systemctl start ntp@mgmt.service

5.  Enable `ntp@mgmt` so that it starts when the switch boots:
    
        cumulus@switch:~$ sudo systemctl enable ntp@mgmt.service

After you enable `ntp@mgmt`, verify that NTP peers are active:

    cumulus@switch:~$ ntpq -pn
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    *38.229.71.1     204.9.54.119     2 u   42   64  377   31.275   -0.625   3.105
    -104.131.53.252  209.51.161.238   2 u   47   64  377   16.381   -5.251   0.681
    +45.79.10.228    200.98.196.212   2 u   44   64  377   42.998    0.115   0.585
    +74.207.240.206  127.67.113.92    2 u   43   64  377   73.240   -1.623   0.320 

### <span id="src-7112679_ManagementVRF-snmpd" class="confluence-anchor-link"></span><span>Enabling Polling with snmpd in a Management VRF</span>

When you enable `snmpd` to run in the management VRF, `snmpd` listens
**only** on eth0; you can no longer listen on a switch port.

SNMP configuration in NCLU is not VRF aware so the `snmpd` daemon is
always started in the default VRF. Because interfaces in a particular
VRF (routing table) are not aware of interfaces in a different VRF, the
`snmpd` daemon only responds to polling requests and sends traps on the
interfaces of the VRF on which it is running. If you configure a
management VRF, you need to start the `snmpd` daemon manually in the
management VRF and stop all other `snmpd` daemons.

### <span id="src-7112679_ManagementVRF-hsflowd" class="confluence-anchor-link"></span><span>Enabling hsflowd</span>

If you are using
[sFlow](https://docs.cumulusnetworks.com/display/CL31/Monitoring+System+Statistics+and+Network+Traffic+with+sFlow)
to monitor traffic in the mgmt VRF, complete the following steps to
enable sFlow.

1.  Add the `hsflowd` process to the `systemd` configuration file in
    `/etc/vrf`. Edit `/etc/vrf/systemd.conf` using a text editor.
    
        cumulus@switch:~$ sudo nano /etc/vrf/systemd.conf 
        # Systemd-based services that are expected to be run in a VRF context.
        #
        # If changes are made to this file run systemctl daemon-reload
        # to re-generate systemd files.
        chef-client
        collectd
        dhcpd
        dhcrelay
        hsflowd  <<< Add this line
        ntp
        puppet
        snmpd
        snmptrapd
        ssh
        zabbix-agent

2.  Stop the `snmpd` daemon, if it is running:
    
        cumulus@switch:~$ sudo systemctl stop hsflowd.service

3.  Disable `snmpd` to ensure it does not start in the default VRF when
    the system is rebooted:
    
        cumulus@switch:~$ sudo systemctl disable hsflowd.service

4.  Start `snmpd` in the the mgmt VRF:
    
        cumulus@switch:~$ sudo systemctl start hsflowd@mgmt.service

5.  Enable `hsflowd@mgmt` so it starts when the switch boots:
    
        cumulus@switch:~$ sudo systemctl enable hsflowd@mgmt.service

6.  Verify that the `hsflowd` service is running in the mgmt VRF:
    
        cumulus@switch:~$ ps aux | grep flow
        root      7294  0.0  0.4  81320  2108 ?        Ssl  22:22   0:00 /usr/sbin/hsflowd
        cumulus   7906  0.0  0.4  12728  2056 pts/0    S+   22:34   0:00 grep flow
        cumulus@switch:~$ vrf task identify 7294
        mgmt

### <span>Using ping or traceroute</span>

By default, when you issue a `ping` or `traceroute`, the packet is sent
to the dataplane network (the main routing table). To use `ping` or
`traceroute` on the management network, use the `-I` flag for ping and
`-i` for `traceroute`.

    cumulus@switch:~$ ping -I mgmt

Or:

    cumulus@switch:~$ sudo traceroute -i mgmt

## <span>OSPF and BGP</span>

In general, no changes are required for either BGP or OSPF. FRRouting is
VRF-aware and automatically sends packets based on the switch port
routing table. This includes BGP peering through loopback interfaces.
BGP does routing lookups in the default table. However, depending on how
your routes are redistributed, you might want to perform the following
modification.

### <span>Redistributing Routes in Management VRF</span>

Management VRF uses the mgmt table, including local routes. It does not
affect how the routes are redistributed when using routing protocols
such as OSPF and BGP.

To redistribute the routes in your network, use the `redistribute
connected` command under BGP or OSPF. This enables the
directly-connected network out of eth0 to be advertised to its neighbor.

{{%notice note%}}

This also creates a route on the neighbor device to the management
network through the data plane, which might not be desired.

{{%/notice%}}

Cumulus Networks recommends you always use route maps to control the
advertised networks redistributed by the `redistribute connected`
command. For example, you can specify a route map to redistribute routes
in this way (for both BGP and OSPF):

    cumulus@leaf01:~$ net add routing route-map REDISTRIBUTE-CONNECTED deny 100 match interface eth0
    cumulus@leaf01:~$ net add routing route-map REDISTRIBUTE-CONNECTED permit 1000

These commands produce the following configuration snippet in the
`/etc/frr/frr.conf` file:

    <routing protocol> 
    redistribute connected route-map REDISTRIBUTE-CONNECTED
     
    route-map REDISTRIBUTE-CONNECTED deny 100
     match interface eth0
    !
    route-map REDISTRIBUTE-CONNECTED permit 1000

## <span>Using SSH within a Management VRF Context</span>

If you SSH to the switch through a switch port, SSH works as expected.
If you need to SSH from the device out of a switch port, use `vrf exec
default ssh <ip_address_of_swp_port>`. For example:

    cumulus@switch:~$ sudo vrf exec default ssh 10.23.23.2 10.3.3.3

## <span>Viewing the Routing Tables</span>

When you look at the routing table with `ip route show`, you are looking
at the switch port (*main*) table. You can also see the dataplane
routing table with `net show route vrf main`.

To view information about eth0 (the management routing table), use `net
show route vrf mgmt`.

    cumulus@switch:~$ net show route vrf mgmt
    default via 192.168.0.1 dev eth0
     
    cumulus@switch:~$ net show route
    default via 10.23.23.3 dev swp17  proto zebra  metric 20
    10.3.3.3 via 10.23.23.3 dev swp17
    10.23.23.0/24 dev swp17  proto kernel  scope link  src 10.23.23.2
    192.168.0.0/24 dev eth0  proto kernel  scope link  src 192.168.0.11

### <span>Viewing a Single Route</span>

If you use `ip route get` to return information about a single route,
the command resolves over the *mgmt* table by default. To obtain
information about the route in the switching silicon, use the following
commands:

    cumulus@switch:~$ net show route <addr> 

To get the route for any VRF, run:

    cumulus@switch:~$ net show route vrf mgmt <addr>

## <span>Using the mgmt Interface Class</span>

In `ifupdown2`, [interface
classes](Interface_Configuration_and_Management.html#src-7112612_InterfaceConfigurationandManagement-classes)
are used to create a user-defined grouping for interfaces. The special
class *mgmt* is available to separate the management interfaces of the
switch from the data interfaces. This allows you to manage the data
interfaces by default using `ifupdown2` commands. Performing operations
on the *mgmt* interfaces requires specifying the `--allow-mgmt` option,
which prevents inadvertent outages on the management interfaces. Cumulus
Linux by default brings up all interfaces in both the *auto* (default)
class and the *mgmt* interface class when the switch boots.

{{%notice warning%}}

The management VRF interface class is not supported if you are
configuring Cumulus Linux using
[NCLU](/version/cumulus-linux-343/System_Configuration/Network_Command_Line_Utility_-_NCLU).

{{%/notice%}}

You configure the management interface in `/etc/network/interfaces`. In
the example below, the management interface, eth0, and the mgmt VRF
stanzas are added to the *mgmt* interface class:

    auto lo
    iface lo inet loopback 
     
    allow-mgmt eth0
    iface eth0 inet dhcp
        vrf mgmt
      
    allow-mgmt mgmt
    iface mgmt
        address 127.0.0.1/8
        vrf-table auto 

When you run `ifupdown2` commands against the interfaces in the mgmt
class, include `--allow=mgmt` with the commands. For example, to see
which interfaces are in the mgmt interface class, run:

    cumulus@switch:~$ ifquery l --allow=mgmt
    eth0
    mgmt 

To reload the configurations for interfaces in the mgmt class, run:

    cumulus@switch:~$ sudo ifreload --allow=mgmt

You can still bring the management interface up and down using `ifup
eth0` and `ifdown eth0`.

## <span>Management VRF and DNS</span>

Cumulus Linux supports both DHCP and static DNS entries over management
VRF through IP FIB rules. These rules are added to direct lookups to the
DNS addresses out of the management VRF.

For DNS to use the management VRF, the static DNS entries must reference
the management VRF in the `/etc/resolv.conf` file. For example:

    nameserver 192.0.2.1
    nameserver 198.51.100.31 # vrf mgmt
    nameserver 203.0.113.13 # vrf mgmt

Nameservers configured through DHCP are updated automatically.
Statically configured nameservers (configured in the `/etc/resolv.conf`
file) are updated only when you run `ifreload -a`. Because DNS lookups
are forced out of the management interface using FIB rules, this could
affect data plane ports if overlapping addresses exist.

## <span>Incompatibility with cl-ns-mgmt</span>

{{%notice warning%}}

Management VRF has replaced the management namespace functionality in
Cumulus Linux. The management namespace feature (via the `cl-ns-mgmt`
utility) has been deprecated, and the `cl-ns-mgmt` command has been
removed.

{{%/notice%}}
