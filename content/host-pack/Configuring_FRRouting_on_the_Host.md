---
title: Configuring FRRouting on the Host
author: Cumulus Networks
weight: 13
aliases:
 - /display/HOSTPACK/Configuring+FRRouting+on+the+Host
 - /pages/viewpage.action?pageId=5868796
pageID: 5868796
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
---
This section provides an overview of configuring
[FRRouting](https://frrouting.org) (FRR), the IP routing protocol suite
for Linux and Unix platforms so you can configure routing directly to
your Ubuntu or Red Hat Enterprise Linux hosts or in containers.

{{%notice note%}}

All [BFD](/display/HOSTPACK/Bidirectional+Forwarding+Detection+-+BFD)
(bidirectional forwarding detection) and
[PTM](/display/HOSTPACK/Prescriptive+Topology+Manager+-+PTM)
(Prescriptive Topology Manager) commands do not work on server hosts
because PTM is not enabled on the host.

{{%/notice%}}

## <span>Configuration Files</span>

At startup, FRR reads a set of files to determine the startup
configuration. The files and what they contain are specified below:

| File        | Description                                                                        |
| ----------- | ---------------------------------------------------------------------------------- |
| frr.conf    | The default, integrated, single configuration file for all `frr` daemons.          |
| daemons     | Contains the list of `frr` daemons that must be started.                           |
| zebra.conf  | Configuration file for the `zebra` daemon.                                         |
| ospfd.conf  | Configuration file for the OSPFv2 daemon.                                          |
| ospf6d.conf | Configuration file for the OSPFv3 daemon.                                          |
| bgpd.conf   | Configuration file for the BGP daemon.                                             |
| ripd.conf   | Configuration file for the RIP daemon. Cumulus Networks has not tested RIP.        |
| ripngd.conf | Configuration file for the IPv6 RIP daemon. Cumulus Networks has not tested RIPv6. |
| isisd.conf  | Configuration file for the IS-IS daemon. Cumulus Networks has not tested IS-IS.    |

{{%notice note%}}

The individual configuration files are not present unless you disable
`integrated-vtysh-config`; [see
below](#src-5868796_ConfiguringFRRoutingontheHost-integrated_cfg) for
details.

{{%/notice%}}

## <span>Configure FRRouting</span>

FRR does not start by default. Before you run FRR, make sure all you
have enabled relevant daemons that you intend to use — `zebra`, `bgpd`,
`ospfd`, `ospf6d`, `ripd`, `ripngd`, `isisd` — in the `/etc/frr/daemons`
file.

The `zebra` daemon must always be enabled. The others you can enable
according to how you plan to route your network — using BGP for example,
instead of OSPF.

Before you start FRR, you need to enable the corresponding daemons
(remember, you must always enable `zebra`). Edit `/etc/frr/daemons` and
set to *yes* each daemon you are enabling. For example, to start `bgpd`,
you need to enable the `zebra` and `bgpd` daemons.

    zebra=yes (* this one is mandatory to bring the others up)
    bgpd=yes
    ospfd=no
    ospf6d=no
    ripd=no
    ripngd=no
    isisd=no

{{%notice note%}}

In the containerized image, the `zebra`, `bgpd`, `ospfd` and `ospf6d`
daemons are enabled by default. If you only intend to use BGP, for
example, you will need to disable the two OSPF daemons. To disable any
of these daemons, create a `daemons` file on the server host and enable
only the daemons you intend to use in the container (remember, `zebra`
must always be enabled). Then copy the daemons file to the container
(named *FRR* in the example below) by running:

    vagrant@server02:~$ sudo docker cp daemons FRR:/etc/frr/daemons

After you copy the file to the container, start FRR, as described below.

{{%/notice%}}

### <span>Start the FRR Service</span>

On an Ubuntu 16.04 or RHEL 7 host, enable and start the FRR service:

    root@host:~# systemctl enable frr.service
    root@host:~# systemctl start frr.service

On an Ubuntu 14.04 host, run this command:

    root@host:~# service frr start

For a Docker container, on the host, run:

    root@host:~# docker exec FRR /usr/lib/frr/frr start
    Starting FRR daemons (prio:10):. zebra. bgpd. ripd. ripngd. ospfd. ospf6d. isisd.
    Starting FRR monitor daemon: watchfrr.
    Exiting from the script

### <span id="src-5868796_ConfiguringFRRoutingontheHost-integrated_cfg" class="confluence-anchor-link"></span><span>Integrated Configurations</span>

By default, FRR saves the configuration of all daemons in a single
integrated configuration file, `frr.conf`.

You can disable this mode by running:

    host(config)# no service integrated-vtysh-config

To enable the integrated configuration file mode again, run:

    host(config)# service integrated-vtysh-config

If you disable the integrated configuration mode, FRR saves each
daemon-specific configuration file in a separate file. At minimum for a
daemon to start, that daemon must be enabled and its daemon-specific
configuration file must be present, even if that file is empty.

You can save the current configuration by running:

    host# write mem
    Building Configuration...
    Integrated configuration saved to /etc/frr/frr.conf
    [OK]

{{%notice note%}}

You can use `write file` instead of `write mem`.

{{%/notice%}}

When the integrated configuration mode disabled, the output looks like
this:

    switch# write mem
    Building Configuration...
    Configuration saved to /etc/frr/zebra.conf
    Configuration saved to /etc/frr/bgpd.conf
    [OK]

### <span>Cumulus FRR Defaults for the Data Center</span>

Located within the default configuration of FRRouting is the following
line:

    frr defaults datacenter

The standard FRR package located on the [FRR
Release](https://github.com/FRRouting/frr/releases/) page displays this
line a little differently.

    frr defaults traditional

This specific line of configuration is an option that is provided at the
time FRRouting is compiled and cannot be changed after compilation
completes. However, it sets the following FRR options:

  - Sets BGP Connect Timer to 10 seconds

  - Sets BGP Holdtimer to 9 seconds

  - Sets BGP Keepalive Timer to 3 seconds

  - Enables Logging of BGP Neighbor Changes

  - Enables BGP show hostname functionality

  - Enables BGP Determinisitic-MED

  - Enables BGP Import Check

  - Enables Logging of OSPF and OSPFv3 adjacency changes

You can modify these settings on the command line.

### <span>Set the Source on a Route-map for BGP Unnumbered Configurations</span>

When using a [BGP unnumbered interfaces
configuration](/display/HOSTPACK/Border+Gateway+Protocol+-+BGP), the
Linux kernel may choose the eth0 management interface for external
communications instead of the loopback interface. To ensure that the
loopback interface is used for external communications, set the source
for a route-map utilizing the loopback IP address. Add a command similar
to the following to the `/etc/frr/frr.conf` file:

    root@host:~# vi /etc/frr/frr.conf
     
    route-map SET_SOURCE permit 10
     set src 192.168.0.1
    !
    ip protocol bgp route-map SET_SOURCE

That sets the ping source to 192.168.0.1 for traffic destined to routes
learned via BGP, which is very useful for Linux hosts. The actual route
looks like this:

    root@host:# ip route show
     
    10.97.1.1 via 169.254.0.1 dev eth1 proto bgp src 10.97.1.161 metric 20 onlink

### <span>Restore the Default Configuration</span>

If you need to restore the FRR configuration to the default running
configuration, you need to delete the `frr.conf` file and restart the
`frr` service. You should back up `frr.conf` (or any configuration files
you may remove, see the note below) before proceeding.

1.  Confirm service `integrated-vtysh-config` is enabled:
    
    ``` 
    root@host:~# vtysh -c "show run" | grep integrated
    service integrated-vtysh-config  
    ```

2.  Remove `/etc/frr/frr.conf`:
    
        root@host:~# rm /etc/frr/frr.conf

3.  Restart FRR. On an Ubuntu 16.04 or RHEL 7 host, run this command:
    
        root@host:~# systemctl restart frr.service
    
    On an Ubuntu 14.04 host, run this command:
    
        root@host:~# service frr restart
    
    For a Docker container, on the host, run:
    
        root@host:~# docker exec FRR /usr/lib/frr/frr restart

{{%notice note%}}

If for some reason `service integrated-vtysh-config` is not configured,
then you should remove all the configuration files (such as `zebra.conf`
or `ospf6d.conf`) instead of `frr.conf` in step 2 above.

{{%/notice%}}

## <span>Configure FRR in a Container</span>

If you're using FRR with containers, you have three ways to configure
FRR:

  - Directly from the host, outside the container

  - By creating an frr`.conf` file on the host and copying it into the
    container

  - Logging into the container and using `vtysh`, the FRR CLI

To configure FRR inside the container directly from the host, run the
following command with the appropriate settings for your network:

    root@host:/etc/apt/sources.list.d# docker exec frr /usr/bin/vtysh -c 'configure t' \ 
              -c 'router bgp 65030' -c 'neighbor 2.1.1.1 remote-as external'

You can configure FRR with a custom `frr.conf` file on the host and copy
it into the container, as containers do not contain text editors such as
`vi` or `nano`. Create the `frr.conf` file, copy it into container and
restart FRR:

    root@host:~# docker cp frr.conf FRR:/etc/frr/frr.conf
    root@host:~# docker exec frr /usr/lib/frr/frr restart 

{{%notice note%}}

The `reload` command does not work at this time.

{{%/notice%}}

Finally you can log into the container to configure FRR using `vtysh`:

    root@host:/etc/apt/sources.list.d# docker exec -it frr /bin/bash
    root@host:/# vtysh
     
    Hello, this is FRR (version 0.99.23.1+cl3u2).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
     
    host# config t
    host(config)#

{{%notice note%}}

When you log into to privileged container, the prompt does not change.

{{%/notice%}}

Configure FRR as you would for a host, described above.

### <span>Stop and Remove Containers</span>

To stop and remove all containers (a container must be stopped before it
can be removed):

    root@host:/etc/apt/sources.list.d# docker stop $(docker ps -a -q)

Remove all containers:

    root@host:/etc/apt/sources.list.d# docker rm $(docker ps -a -q)

## <span>Interface IP Addresses</span>

FRR inherits the IP addresses and any associated routing tables for the
network interfaces from the `/etc/network/interfaces` file. This is the
recommended way to define the addresses; do **not** create interfaces
using FRR. For more information, see [Configuring IP
Addresses](/display/HOSTPACK/Interface+Configuration+and+Management) in
the Cumulus Linux user guide.

## <span>The vtysh Modal CLI</span>

FRR provides a [CLI](http://docs.frrouting.org/en/latest/vtysh.html) –
`vtysh` – for configuring and displaying the state of the protocols. It
is invoked by running:

    root@host:~# vtysh
     
    Hello, this is FRR (version 0.99.23.1+cl3.0).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
     
    host#

`vtysh` provides a Cisco-like modal CLI, and many of the commands are
similar to Cisco IOS commands. By modal CLI, we mean that there are
different modes within the CLI, and certain commands are only available
within a specific mode. Configuration is available with the `configure
terminal` command, which you invoke like this:

    host# configure terminal
    host(config)#

The prompt displays the mode the CLI is in. For example, when the
interface-specific commands are invoked, the prompt changes to:

    host(config)# interface swp1
    host(config-if)#

When the routing protocol specific commands are invoked, the prompt
changes to:

    host(config)# router ospf
    host(config-router)#

At any level, ”?” displays the list of available top-level commands at
that level:

    host(config-if)# ?
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

    host(config-if)# bandwidth ?
    <1-10000000>  Bandwidth in kilobits
    host(config-if)# ip ?
    address  Set the IP address of an interface
    irdp     Alter ICMP Router discovery preference this interface
    ospf     OSPF interface commands
    rip      Routing Information Protocol
    router   IP router interface commands

Displaying state can be done at any level, including the top level. For
example, to see the routing table as seen by `zebra`, you use:

    host# show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP,
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

    host(config-router)# do show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP,
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

    root@host:~# vtysh -c 'sh ip route'
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP,
           > - selected route, * - FIB route
     
    K>* 0.0.0.0/0 via 192.168.0.2, eth0
    C>* 192.0.2.11/24 is directly connected, swp1
    C>* 192.0.2.12/24 is directly connected, swp2
    B>* 203.0.113.30/24 [200/0] via 192.0.2.2, swp1, 11:05:10
    B>* 203.0.113.31/24 [200/0] via 192.0.2.2, swp1, 11:05:10
    B>* 203.0.113.32/24 [200/0] via 192.0.2.2, swp1, 11:05:10
    C>* 127.0.0.0/8 is directly connected, lo
    C>* 192.168.0.0/24 is directly connected, eth0

Running a command multiple levels down is done like this:

    root@host:~# vtysh -c 'configure terminal' -c 'router ospf' -c 'area 0.0.0.1 range 10.10.10.0/24'

Notice that the commands also take a partial command name (for example,
`sh ip route` above) as long as the partial command name is not aliased:

    root@host:~# vtysh -c 'sh ip r'
    % Ambiguous command.

A command or feature can be disabled by prepending the command with
`no`. For example:

    host(config-router)# no area 0.0.0.1 range 10.10.10.0/24

The current state of the configuration can be viewed using the `show
running-config` command:

Click here to see the output ...

    host# show running-config
    Building configuration...
     
    Current configuration:
    !
    hostname frr
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

{{%notice note%}}

If you attempt to configure a routing protocol that has not been
started, `vtysh` silently ignores those commands.

{{%/notice%}}

## <span>Example vtysh Commands</span>

This section illustrates various `vtysh` commands for use when
configuring FRR.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Action</p></th>
<th><p>vtysh Command</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Display the routing table</p></td>
<td><pre><code>host# show ip route</code></pre></td>
</tr>
<tr class="even">
<td><p>Show the running configuration</p></td>
<td><pre><code>host# show running-config</code></pre></td>
</tr>
<tr class="odd">
<td><p>Create a new neighbor</p></td>
<td><pre><code>host(config)# router bgp 65002
host(config-router)# neighbor 14.0.0.22 remote-as 65007</code></pre></td>
</tr>
<tr class="even">
<td><p>Redistribute routing information from static route entries</p></td>
<td><pre><code>host(config)# router bgp 65002
host(config-router)# redistribute static</code></pre></td>
</tr>
<tr class="odd">
<td><p>Define a static route (for static routes, you only need to enable the <code>zebra</code> daemon)</p></td>
<td><pre><code>host(config)# ip route 155.1.2.20/24 br2 45</code></pre></td>
</tr>
<tr class="even">
<td><p>Configure an IPv6 interface</p></td>
<td><pre><code>host(config)# int br3
host(config-if)# ipv6 address  3002:2123:1234:1abc::21/64</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure MTU in IPv6 network discovery for an interface</p></td>
<td><pre><code>host(config)# int swp3
host(config-if)# ipv6 nd mtu 9000</code></pre></td>
</tr>
<tr class="even">
<td><p>Log OSPF adjacency changes</p></td>
<td><pre><code>host(config)# router ospf
host(config-router)# router-id 2.0.0.21
host(config-router)# log-adjacency-changes</code></pre></td>
</tr>
<tr class="odd">
<td><p>Set OSPF interface priority</p></td>
<td><pre><code>host(config)# int swp3
host(config-if)# ip ospf priority  120</code></pre></td>
</tr>
<tr class="even">
<td><p>Configure timing for OSPF SPF calculations</p></td>
<td><pre><code>host(config)# router ospf6
host(config-ospf6)# timer throttle spf 40 50 60</code></pre></td>
</tr>
<tr class="odd">
<td><p>Configure hello packet intervals (in seconds)</p></td>
<td><pre><code>host(config)# int swp4
host(config-if)# ipv6 ospf6 hello-interval  60</code></pre></td>
</tr>
<tr class="even">
<td><p>Display OSPF debugging status</p></td>
<td><pre><code>host# show debugging ospf</code></pre></td>
</tr>
<tr class="odd">
<td><p>Display BGP information</p></td>
<td><pre><code>host# show ip bgp summary</code></pre></td>
</tr>
</tbody>
</table>

## <span>Reload the FRR Configuration</span>

If you make a change to your routing configuration, you need to reload
so your changes take place. *FRR reload* enables you to apply only the
modifications you make to your FRR configuration, synchronizing its
running state with the configuration in `/etc/frr/frr.conf`. This is
useful for optimizing the automation of FRR in your environment or to
apply changes made at runtime.

{{%notice note%}}

FRR reload only applies to an integrated service configuration, where
your FRR configuration is stored in a single `frr.conf` file instead of
one configuration file per FRR daemon (like `zebra` or `bgpd`).

{{%/notice%}}

To reload your FRR configuration after you've modified
`/etc/frr/frr.conf`, on a Cumulus Linux switch, run:

    cumulus@switch:~$ sudo systemctl reload frr

On an Ubuntu host, run this command:

    root@host:~# service frr reload

Examine the running configuration and verify that it matches the config
in `/etc/frr/frr.conf`:

    root@host:~# vtysh -c 'show run'

### <span>Reload FRR in a Container</span>

When you change the FRR configuration, you need to reload FRR for your
changes to take place. Run the following command:

    root@host:# docker exec -it frr /usr/lib/frr/frr-reload.py --reload /etc/frr/frr.conf

## <span>Debug Steps</span>

If the running configuration is not what you expected, please [submit a
support
request](https://support.cumulusnetworks.com/hc/en-us/requests/new) and
supply the following information:

  - The current running configuration (run `sudo vtysh -c 'show run'`
    and output the contents to a file)

  - The contents of `/etc/frr/frr.conf`

  - The contents of the `/var/log/frr/` directory

## <span>Useful Links</span>

  - [FRR BGP
    documentation](http://docs.frrouting.org/en/latest/bgp.html)

  - [FRR IPv6 support
    documentation](http://docs.frrouting.org/en/latest/ipv6.html)

  - [FRR Zebra
    documentation](http://docs.frrouting.org/en/latest/zebra.html)[](https://frrouting.org/user-guide/Zebra.html#Zebra)
