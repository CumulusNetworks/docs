---
title: Management VRF
author: Cumulus Networks
weight: 193
pageID: 8362410
---
*Management VRF* is a subset of
[VRF](/cumulus-linux-36/Layer-3/Virtual-Routing-and-Forwarding-VRF)
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
such as the `ip` command to list links, neighbors, or routes.

{{%notice tip%}}

The management VRF configurations in this chapter contain a localhost
loopback IP address (127.0.0.1/8). Adding the loopback address to the L3
domain of the management VRF prevents issues with applications that
expect the loopback IP address to exist in the VRF, such as NTP.

{{%/notice%}}

## Enabling Management VRF

To enable management VRF on eth0, complete the following steps:

{{%notice info%}}

**Example Management VRF Configuration**

The example NCLU commands below create a VRF called *mgmt*:

{{%notice info%}}

The management VRF must be named `mgmt` to differentiate from a data
plane VRF.

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

{{%notice info%}}

When you commit the change to add the management VRF, all connections
over eth0 are dropped. This can impact any automation that might be
running, such as Ansible or Puppet scripts.

{{%/notice%}}

{{%/notice%}}

### Bringing the Management VRF Up after Downing It with ifdown

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

## Running Services within the Management VRF

You can run a variety of services within the management VRF instead of
the default VRF. In most cases, you must stop and disable the instance
running in the default VRF before you can start the service in the
management VRF. This is because the instance running in the default VRF
owns the port across all VRFs. The list of services that must be
disabled in the default VRF are:

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
**only** on eth0; it no longer runs on any switch port. However, you can
keep the service running in the default VRF with a wildcard for
[agentAddress](/cumulus-linux-36/Monitoring-and-Troubleshooting/Simple-Network-Management-Protocol-SNMP/#configuring-snmp-manually).
This enables the service to run on **all** interfaces no matter which
VRF, so you don't have to run a different process for each VRF.

Some applications can work across all VRFs. The kernel provides a
`sysctl` that allows a single instance to accept connections over all
VRFs. For TCP, connected sockets are bound to the VRF on which the first
packet is received. This `sysctl` is enabled for Cumulus Linux.

To enable a service to run in the management VRF, do the following.
These steps use the NTP service, but you can use any of the services
listed above, except for `dhcrelay` (discussed
[here](/cumulus-linux-36/Layer-1-and-Switch-Ports/DHCP-Relays/#configuring-multiple-dhcp-relays)) and `hsflowd`
(discussed [below](#enabling-hsflowd)).

1.  Configure the management VRF as described in the Enabling Management
    VRF section above.

2.  If NTP is running, stop the service:
    
        cumulus@switch:~$ sudo systemctl stop ntp.service

3.  Disable NTP from starting automatically in the default VRF:
    
        cumulus@switch:~$ sudo systemctl disable ntp.service

4.  Start NTP in the management VRF.
    
        cumulus@switch:~$ sudo systemctl start ntp@mgmt.service

5.  Enable `ntp@mgmt` so that it starts when the switch boots:
    
        cumulus@switch:~$ sudo systemctl enable ntp@mgmt.service

After you enable `ntp@mgmt`, you can verify that NTP peers are active:

    cumulus@switch:~$ ntpq -pn
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    *38.229.71.1     204.9.54.119     2 u   42   64  377   31.275   -0.625   3.105
    -104.131.53.252  209.51.161.238   2 u   47   64  377   16.381   -5.251   0.681
    +45.79.10.228    200.98.196.212   2 u   44   64  377   42.998    0.115   0.585
    +74.207.240.206  127.67.113.92    2 u   43   64  377   73.240   -1.623   0.320 

### Enabling Polling with snmpd in a Management VRF

When you enable `snmpd` to run in the management VRF, you need to
specify that VRF with NCLU so that `snmpd` listens on eth0 in the
management VRF; you can also configure snmpd to listen on other ports
with the NCLU listening-address vrf command. As of CL 3.6, SNMP
configuration is VRF aware so snmpd can bind to multiple IP addresses
each configured with a particular VRFs (routing table). The `snmpd`
daemon responds to polling requests on the interfaces of the VRF on
which the request came in. SNMP version 1, 2c and 3 Traps and (v3)
Inform messages can be configured with NCLU. See the chapter on SNMP
management with NCLU for detailed instructions on how to configure SNMP
with VRFs.

{{%notice note%}}

The message `Duplicate IPv4 address detected, some interfaces may not be
visible in IP-MIB` displays after starting `snmpd` in the mgmt VRF. This
is because the IP-MIB assumes the same IP address cannot be used twice
on the same device; the IP-MIB is not VRF aware. This message is a
warning that the SNMP IP-MIB detects overlapping IP addresses on the
system; it does *not* indicate a problem and is non-impacting to the
operation of the switch.

{{%/notice%}}

### Enabling hsflowd

If you are using
[sFlow](https://docs.cumulusnetworks.com/display/CL31/Monitoring+System+Statistics+and+Network+Traffic+with+sFlow)
to monitor traffic in the management VRF, you need to complete the
following steps to enable sFlow.

1.  Add the `hsflowd` process to the `systemd` configuration file in
    `/etc/vrf`. Edit the `/etc/vrf/systemd.conf` file with a text
    editor.
    
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

2.  Stop the `hsflowd` daemon if it is running:
    
        cumulus@switch:~$ sudo systemctl stop hsflowd.service

3.  Disable `hsflowd` to ensure it does not start in the default VRF if
    the system is rebooted:
    
        cumulus@switch:~$ sudo systemctl disable hsflowd.service

4.  Run the `daemon-reload` command:
    
        cumulus@switch:~$ sudo systemctl daemon-reload

5.  Start `hsflowd` in management VRF:
    
        cumulus@switch:~$ sudo systemctl start hsflowd@mgmt.service

6.  Enable `hsflowd@mgmt` so it starts when the switch boots:
    
        cumulus@switch:~$ sudo systemctl enable hsflowd@mgmt.service

7.  Verify that the `hsflowd` service is running in the management VRF:
    
        cumulus@switch:~$ ps aux | grep flow
        root      7294  0.0  0.4  81320  2108 ?        Ssl  22:22   0:00 /usr/sbin/hsflowd
        cumulus   7906  0.0  0.4  12728  2056 pts/0    S+   22:34   0:00 grep flow
        cumulus@switch:~$ vrf task identify 7294
        mgmt

### Using ping or traceroute

By default, when you issue a `ping` or `traceroute`, the packet is sent
to the dataplane network (the main routing table). To use `ping` or
`traceroute` on the management network, use the `-I` flag for ping and
`-i` for `traceroute`.

    cumulus@switch:~$ ping -I mgmt

Or:

    cumulus@switch:~$ sudo traceroute -i mgmt

### Running Services as a Non-root User

Sometimes you may want to run services in the management VRF as a
non-root user. To do so, you need to create a custom service based on
the original service file.

1.  Copy the original service file to its new name and store the file in
    `/etc/systemd/system`.
    
        cumulus@switch:~$ sudo cp /lib/systemd/system/myservice.service /etc/systemd/system/myservice.service 

2.  If there is a *User* directive, comment it out. If it exists, you
    can find it under *\[Service\]*.
    
        cumulus@switch:~$ sudo nano /etc/systemd/system/myservice.service 
         
        [Unit]
        Description=Example
        Documentation=https://www.example.io/
         
        [Service]
        #User=username
        ExecStart=/usr/local/bin/myservice agent -data-dir=/tmp/myservice -bind=192.168.0.11
         
        [Install]
        WantedBy=multi-user.target

3.  Modify the *ExecStart* line to `/usr/bin/vrf exec mgmt /sbin/runuser
    -u USER -- COMMAND`. For example, to have the *cumulus* user run the
    *foocommand*:
    
        [Unit]
        Description=Example
        Documentation=https://www.example.io/
         
        [Service]
        #User=username
        ExecStart=/usr/bin/vrf task exec mgmt /sbin/runuser -u cumulus -- foocommand
         
        [Install]
        WantedBy=multi-user.target

4.  Save and exit the file.
    
        ^O
        ^X
        cumulus@switch:~$ 

5.  Reload the service so the changes take effect:
    
        cumulus@switch:~$ sudo systemctl daemon-reload

## OSPF and BGP

In general, no changes are required for either BGP or OSPF. FRRouting is
VRF-aware and automatically sends packets based on the switch port
routing table. This includes BGP peering via loopback interfaces. BGP
does routing lookups in the default table. However, depending on how
your routes are redistributed, you might want to perform the following
modification.

### Redistributing Routes in Management VRF

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

## Using SSH within a Management VRF Context

If you SSH to the switch through a switch port, SSH works as expected.
If you need to SSH from the device out of a switch port, use 
`vrf exec default ssh <ip_address_of_swp_port>`. For example:

    cumulus@switch:~$ sudo vrf exec default ssh 10.23.23.2 10.3.3.3

## Viewing the Routing Tables

When you look at the routing table with `ip route show`, you are looking
at the switch port (*main*) table. You can also see the dataplane
routing table with `net show route vrf main`.

To look at information about eth0 (the management routing table), use
`net show route vrf mgmt`.

    cumulus@switch:~$ net show route vrf mgmt
    default via 192.168.0.1 dev eth0
     
    cumulus@switch:~$ net show route
    default via 10.23.23.3 dev swp17  proto zebra  metric 20
    10.3.3.3 via 10.23.23.3 dev swp17
    10.23.23.0/24 dev swp17  proto kernel  scope link  src 10.23.23.2
    192.168.0.0/24 dev eth0  proto kernel  scope link  src 192.168.0.11

### Viewing a Single Route

If you use `ip route get` to return information about a single route,
the command resolves over the *mgmt* table by default. To obtain
information about the route in the switching silicon, use:

    cumulus@switch:~$ net show route <addr> 

To get the route for any VRF, run the following command:

    cumulus@switch:~$ net show route vrf mgmt <addr>

## Using the mgmt Interface Class

In `ifupdown2`, [interface classes](/cumulus-linux-36/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/#ifupdown2-interface-classes)
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
[NCLU](/cumulus-linux-36/System-Configuration/Network-Command-Line-Utility-NCLU/).

{{%/notice%}}

You configure the management interface in the ` /etc/network/interfaces
 `file. In the example below, the management interface, eth0 and the
management VRF stanzas are added to the *mgmt* interface class:

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

## Management VRF and DNS

Cumulus Linux supports both DHCP and static DNS entries over management
VRF through IP FIB rules. These rules are added to direct lookups to the
DNS addresses out of the management VRF.

For DNS to use the management VRF, the static DNS entries must reference
the management VRF in the `/etc/resolv.conf` file. For example:

    nameserver 192.0.2.1
    nameserver 198.51.100.31 # vrf mgmt
    nameserver 203.0.113.13 # vrf mgmt

Nameservers configured through DHCP are updated automatically,
Statically configured nameservers (configured in the `/etc/resolv.conf`
file) only get updated when you run `ifreload -a`.

{{%notice note%}}

Because DNS lookups are forced out of the management interface using FIB
rules, this might affect data plane ports if overlapping addresses are
used. For example, when the DNS server IP address is learned over the
management VRF, a FIB rule is created for that IP address. When DHCP
relay is configured for the same IP address, a DHCP discover packet
received on the front panel port is forwarded out of the management
interface (eth0) even though a route is present out the front-panel port.

{{%/notice%}}

## Incompatibility with cl-ns-mgmt

{{%notice warning%}}

Management VRF has replaced the management namespace functionality in
Cumulus Linux. The management namespace feature (used with the
`cl-ns-mgmt` utility) has been deprecated, and the `cl-ns-mgmt` command
has been removed.

{{%/notice%}}
