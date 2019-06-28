---
title: Configuring Quagga
author: Cumulus Networks
weight: 129
aliases:
 - /display/CL25ESR/Configuring+Quagga
 - /pages/viewpage.action?pageId=5116108
pageID: 5116108
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
This section provides an overview of configuring `quagga`.

Before you run `quagga`, make sure all relevant daemons, such as
`zebra`, are running. Make your changes in `/etc/quagga/daemons` then
restart `quagga` with `service quagga restart`.

## <span>Configuration Files</span>

At startup, `quagga` reads a set of files to determine the startup
configuration. The files and what they contain are specified below:

| File        | Description                                                                  |
| ----------- | ---------------------------------------------------------------------------- |
| Quagga.conf | The default, integrated, single configuration file for all `quagga` daemons. |
| daemons     | Contains the list of `quagga` daemons that must be started.                  |
| zebra.conf  | Configuration file for the `zebra` daemon.                                   |
| ospfd.conf  | Configuration file for the OSPFv2 daemon.                                    |
| ospf6d.conf | Configuration file for the OSPFv3 daemon.                                    |
| bgpd.conf   | Configuration file for the BGP daemon.                                       |

### <span>Starting Quagga</span>

Quagga does not start by default in Cumulus Linux 2.0 and later
versions.

Before you start `quagga`, modify `/etc/quagga/daemons` to enable the
corresponding daemons:

    zebra=yes (* this one is mandatory to bring the others up)
    bgpd=yes
    ospfd=yes
    ospf6d=yes
    ripd=no
    ripngd=no
    isisd=no
    babeld=no

Then, start `quagga`:

    cumulus@switch1:~$ sudo service quagga start

### <span>Understanding Integrated Configurations</span>

By default in Cumulus Linux, `quagga` saves the configuration of all
daemons in a single integrated configuration file, `Quagga.conf`.

You can disable this mode by running:

    quagga(config)# no service integrated-vtysh-config
    quagga(config)#

To enable the integrated configuration file mode again, run:

    quagga(config)# service integrated-vtysh-config
    quagga(config)#

If you disable the integrated configuration mode, `quagga` saves each
daemon-specific configuration file in a separate file. At a minimum for
a daemon to start, that daemon must be specified in the `daemons` file
and the daemon-specific configuration file must be present, even if that
file is empty.

For example, to start `bgpd`, the `daemons` file needs to be formatted
as follows, at minimum:

    cumulus@switch:~$ sudo cat /etc/quagga/daemons
    zebra=yes
    bgpd=yes

The current configuration can be saved by running:

    quagga# write mem
    Building Configuration...
    Integrated configuration saved to /etc/quagga/Quagga.conf
    [OK]

{{%notice note%}}

You can use `write file` instead of `write mem`.

{{%/notice%}}

When the integrated configuration mode disabled, the output looks like
this:

    quagga# write mem
    Building Configuration...
    Configuration saved to /etc/quagga/zebra.conf
    Configuration saved to /etc/quagga/bgpd.conf
    [OK]

{{%notice note%}}

The `daemons` file is not written using the `write mem` command.

{{%/notice%}}

### <span>Restoring the Default Quagga Configuration</span>

If you need to restore the Quagga configuration to the default running
configuration, you need to delete the `Quagga.conf` file and restart the
`quagga` service.

1.  Confirm `service integrated-vtysh-config` is enabled:
    
    ``` 
    cumulus@switch$ sudo cl-rctl running-config |grep integrated
              service integrated-vtysh-config  
    ```

2.  Remove `/etc/quagga/Quagga.conf`:
    
        cumulus@switch$ sudo rm /etc/quagga/Quagga.conf

3.  Restart the `quagga` service:
    
        cumulus@switch$ sudo service quagga restart

{{%notice note%}}

If for some reason `service integrated-vtysh-config` is not configured,
then you should remove `zebra.conf` instead of `Quagga.conf` in step 2
above.

{{%/notice%}}

## <span>Interface IP Addresses</span>

Quagga inherits the IP addresses for the network interfaces from the
`/etc/network/interfaces` file. This is the recommended way to define
the addresses. For more information, see [Configuring IP
Addresses](Configuring_and_Managing_Network_Interfaces.html#src-5116095_ConfiguringandManagingNetworkInterfaces-ip).

## <span>Using the vtysh Modal CLI</span>

Quagga provides a CLI – `vtysh` – for configuring and displaying the
state of the protocols. It is invoked by running:

    cumulus@switch:~$ sudo vtysh
    
    Hello, this is Quagga (version 0.99.21).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
    
    quagga#

Launching `vtysh` brings you into `zebra` initially. From here, you can
log into other protocol daemons, such as `bgpd`, `ospfd` or `babeld`.

`vtysh` provides a Cisco-like modal CLI, and many of the commands are
similar to Cisco IOS commands. By modal CLI, we mean that there are
different modes to the CLI, and certain commands are only available
within a specific mode. Configuration is available with the `configure
terminal` command, which is invoked thus:

    quagga# configure terminal
    quagga(config)#

The prompt displays the mode the CLI is in. For example, when the
interface-specific commands are invoked, the prompt changes to:

    quagga(config)# interface swp1
    quagga(config-if)#

When the routing protocol specific commands are invoked, the prompt
changes to:

    quagga(config)# router ospf
    quagga(config-router)#

At any level, ”?” displays the list of available top-level commands at
that level:

    quagga(config-if)# ?
    babel        Babel interface commands
    bandwidth    Set bandwidth informational parameter
    description  Interface specific description
    end          End current mode and change to enable mode
    exit         Exit current mode and down to previous mode
    ip           Interface Internet Protocol config commands
    ipv6         Interface IPv6 config commands
    isis         IS-IS commands
    link-detect  Enable link detection on interface
    list         Print command list
    mpls-te      MPLS-TE specific commands
    multicast    Set multicast flag to interface
    no           Negate a command or set its defaults
    ospf         OSPF interface commands
    quit         Exit current mode and down to previous mode
    shutdown     Shutdown the selected interface

?-based completion is also available to see the parameters that a
command takes:

    quagga(config-if)# bandwidth ?
    <1-10000000>  Bandwidth in kilobits
    quagga(config-if)# ip ?
    address  Set the IP address of an interface
    irdp     Alter ICMP Router discovery preference this interface
    ospf     OSPF interface commands
    rip      Routing Information Protocol
    router   IP router interface commands

Displaying state can be done at any level, including the top level. For
example, to see the routing table as seen by `zebra`, you use:

    quagga# show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel,
           > - selected route, * - FIB route
    
    K>* 0.0.0.0/0 via 192.168.0.2, eth0
    C>* 192.0.2.11/24 is directly connected, swp1
    C>* 192.0.2.12/24 is directly connected, swp2
    B>* 203.0.113.30/24 [200/0] via 192.0.2.2, swp1, 10:43:05
    B>* 203.0.113.31/24 [200/0] via 192.0.2.2, swp1, 10:43:05
    B>* 203.0.113.32/24 [200/0] via 192.0.2.2, swp1, 10:43:05
    C>* 127.0.0.0/8 is directly connected, lo
    C>* 192.168.0.0/24 is directly connected, eth0

To run the same command at a config level, you prepend `do` to it:

    quagga(config-router)# do show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel,
           > - selected route, * - FIB route
    
    K>* 0.0.0.0/0 via 192.168.0.2, eth0
    C>* 192.0.2.11/24 is directly connected, swp1
    C>* 192.0.2.12/24 is directly connected, swp2
    B>* 203.0.113.30/24 [200/0] via 192.0.2.2, swp1, 10:43:05
    B>* 203.0.113.31/24 [200/0] via 192.0.2.2, swp1, 10:43:05
    B>* 203.0.113.32/24 [200/0] via 192.0.2.2, swp1, 10:43:05
    C>* 127.0.0.0/8 is directly connected, lo
    C>* 192.168.0.0/24 is directly connected, eth0

Running single commands with `vtysh` is possible using the `-c` option
of `vtysh`:

    cumulus@switch:~$ sudo vtysh -c 'sh ip route'
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel,
           > - selected route, * - FIB route
    
    K>* 0.0.0.0/0 via 192.168.0.2, eth0
    C>* 192.0.2.11/24 is directly connected, swp1
    C>* 192.0.2.12/24 is directly connected, swp2
    B>* 203.0.113.30/24 [200/0] via 192.0.2.2, swp1, 11:05:10
    B>* 203.0.113.31/24 [200/0] via 192.0.2.2, swp1, 11:05:10
    B>* 203.0.113.32/24 [200/0] via 192.0.2.2, swp1, 11:05:10
    C>* 127.0.0.0/8 is directly connected, lo
    C>* 192.168.0.0/24 is directly connected, eth0

Running a command multiple levels down is done thus:

    cumulus@switch:~$ sudo vtysh -c 'configure terminal' -c 'router ospf' -c 'area 0.0.0.1 range 10.10.10.0/24'

Notice that the commands also take a partial command name (for example,
`sh ip route` above) as long as the partial command name is not aliased:

    cumulus@switch:~$ sudo vtysh -c 'sh ip r'
    % Ambiguous command.

A command or feature can be disabled by prepending the command with
`no`. For example:

    quagga(config-router)# no area 0.0.0.1 range 10.10.10.0/24

The current state of the configuration can be viewed via:

    quagga# show running-config
    Building configuration...
    
    Current configuration:
    !
    hostname quagga
    log file /media/node/zebra.log
    log file /media/node/bgpd.log
    log timestamp precision 6
    !
    service integrated-vtysh-config
    !
    password xxxxxx
    enable password xxxxxx
    !
    interface eth0
    ipv6 nd suppress-ra
    link-detect
    !
    interface lo
    link-detect
    !
    interface swp1
    ipv6 nd suppress-ra
    link-detect
    !
    interface swp2
    ipv6 nd suppress-ra
    link-detect
    !
    router bgp 65000
    bgp router-id 0.0.0.9
    bgp log-neighbor-changes
    bgp scan-time 20
    network 29.0.1.0/24
    timers bgp 30 90
    neighbor tier-2 peer-group
    neighbor 192.0.2.2 remote-as 65000
    neighbor 192.0.2.2 ttl-security hops 1
    neighbor 192.0.2.2 advertisement-interval 30
    neighbor 192.0.2.2 timers 30 90
    neighbor 192.0.2.2 timers connect 30
    neighbor 192.0.2.2 next-hop-self
    neighbor 192.0.2.12 remote-as 65000
    neighbor 192.0.2.12 next-hop-self
    neighbor 203.0.113.1 remote-as 65000
    !
    ip forwarding
    ipv6 forwarding
    !
    line vty
    exec-timeout 0 0
    !
    end

<span id="src-5116108_ConfiguringQuagga-nonmodal"></span>

## <span>Using the Cumulus Linux Non-Modal CLI</span>

The `vtysh` modal CLI can be difficult to work with and even more
difficult to script. As an alternative to this, Cumulus Linux contains a
non-modal version of these commands, structured similar to the Linux
`ip` command. The available commands are:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>cl-bgp</p></td>
<td><p><a href="/version/cumulus-linux-2512-esr/Layer_3_Features/Configuring_Border_Gateway_Protocol_-_BGP">BGP</a> commands. See <code>man cl-bgp </code>for details.</p></td>
</tr>
<tr class="even">
<td><p>cl-ospf</p></td>
<td><p><a href="/version/cumulus-linux-2512-esr/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol">OSPFv2</a> commands. For example:<br />
<code>cumulus@switch:~$ sudo cl-ospf area 0.0.0.1 range 10.10.10.0/24</code></p></td>
</tr>
<tr class="odd">
<td><p>cl-ospf6</p></td>
<td><p><a href="/version/cumulus-linux-2512-esr/Layer_3_Features/Open_Shortest_Path_First_v3_-_OSPFv3_-_Protocol">OSPFv3</a> commands.</p></td>
</tr>
<tr class="even">
<td><p>cl-ra</p></td>
<td><p>Route advertisement commands. See <code>man cl-ra</code> for details.</p></td>
</tr>
<tr class="odd">
<td><p>cl-rctl</p></td>
<td><p>Zebra and non-routing protocol-specific commands. See <code>man cl-rctl</code> for details.</p></td>
</tr>
</tbody>
</table>

## <span>Comparing vtysh and Cumulus Linux Commands</span>

This section describes how you can use the various Cumulus Linux CLI
commands to configure Quagga, without using `vtysh`.

### <span>Displaying the Routing Table</span>

To display the routing table under Quagga, you would run:

    quagga# show ip route

To display the routing table with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl route

### <span>Creating a New Neighbor</span>

To create a new neighbor under Quagga, you would run:

    quagga(config)# router bgp 65002
    quagga(config-router)# neighbor 14.0.0.22 remote-as 65007

To create a new neighbor with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-bgp as 65002 neighbor add 14.0.0.22 remote-as 65007

### <span>Redistributing Routing Information</span>

To redistribute routing information from static route entries into RIP
tables under Quagga, you would run:

    quagga(config)# router bgp 65002
    quagga(config-router)# redistribute static

To redistribute routing information from static route entries into RIP
tables with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-bgp as 65002 redistribute add static

### <span>Defining a Static Route</span>

To define a static route under Quagga, you would run:

    quagga(config)# ip route 155.1.2.20/24 br2 45

To define a static route with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl ip route add 175.0.0.0/28 interface br1 distance 25

### <span>Configuring an IPv6 Interface</span>

To configure an IPv6 address under Quagga, you would run:

    quagga(config)# int br3
    quagga(config-if)# ipv6 address  3002:2123:1234:1abc::21/64

To configure an IPv6 address with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl interface add swp3 ipv6 address 3002:2123:abcd:2120::41/64

### <span>Enabling PTM</span>

To enable topology checking (PTM) under Quagga, you would run:

    quagga(config)# ptm-enable

To enable topology checking (PTM) with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl ptm-enable set

### <span>Configuring MTU in IPv6 Network Discovery</span>

To configure
[MTU](Layer_1_and_Switch_Port_Attributes.html#src-5116098_Layer1andSwitchPortAttributes-mtu)
in IPv6 network discovery for an interface under Quagga, you would run:

    quagga(config)# int swp3
    quagga(config-if)# ipv6 nd mtu 9000

To configure MTU in IPv6 network discovery for an interface with the
Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ra interface swp3 set mtu 9000

### <span>Logging OSPF Adjacency Changes</span>

To log adjacency of OSPF changes under Quagga, you would run:

    quagga(config)# router ospf
    quagga(config-router)# router-id 2.0.0.21
    quagga(config-router)# log-adjacency-changes

To log adjacency changes of OSPF with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf log-adjacency-changes set
    cumulus@switch:~$ sudo cl-ospf router-id set 3.0.0.21

### <span>Setting OSPF Interface Priority</span>

To set the OSPF interface priority under Quagga, you would run:

    quagga(config)# int swp3
    quagga(config-if)# ip ospf priority  120

To set the OSPF interface priority with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf interface set swp3 priority 120

### <span>Configuring Timing for OSPF SPF Calculations</span>

To configure timing for OSPF SPF calculations under Quagga, you would
run:

    quagga(config)# router ospf6
    quagga(config-ospf6)# timer throttle spf 40 50 60

To configure timing for OSPF SPF calculations with the Cumulus Linux
CLI, run:

    cumulus@switch:~$ sudo cl-ospf6 timer add throttle spf 40 50 60

### <span>Configuring Hello Packet Intervals</span>

To configure the OSPF Hello packet interval in number of seconds for an
interface under Quagga, you would run:

    quagga(config)# int swp4
    quagga(config-if)# ipv6 ospf6 hello-interval  60

To configure the OSPF Hello packet interval in number of seconds for an
interface with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf6 interface set swp4 hello-interval 60

### <span>Displaying OSPF Debugging Status</span>

To display OSPF debugging status under Quagga, you would run:

    quagga# show debugging ospf

To display OSPF debugging status with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf debug show

### <span>Displaying BGP Information</span>

To display BGP information under Quagga, you would run:

    quagga# show ip bgp summary

To display BGP information with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-bgp summary

## <span>Useful Links</span>

  - <http://www.nongnu.org/quagga/docs/docs-info.html#BGP>

  - <http://www.nongnu.org/quagga/docs/docs-info.html#IPv6-Support>

  - <http://www.nongnu.org/quagga/docs/docs-info.html#Zebra>
