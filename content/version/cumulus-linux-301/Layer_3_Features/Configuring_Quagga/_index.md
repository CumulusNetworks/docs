---
title: Configuring Quagga
author: Cumulus Networks
weight: 135
aliases:
 - /display/CL30/Configuring+Quagga
 - /pages/viewpage.action?pageId=5118386
pageID: 5118386
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
This section provides an overview of configuring Cumulus Quagga, the
Cumulus Networks-enhanced version of the Quagga routing software package
that provides a suite of routing protocols so you can configure routing
on your switch.

## <span>Configuration Files</span>

At startup, Quagga reads a set of files to determine the startup
configuration. The files and what they contain are specified below:

| File        | Description                                                                        |
| ----------- | ---------------------------------------------------------------------------------- |
| Quagga.conf | The default, integrated, single configuration file for all `quagga` daemons.       |
| daemons     | Contains the list of `quagga` daemons that must be started.                        |
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
below](#src-5118386_ConfiguringQuagga-integrated_cfg) for details.

{{%/notice%}}

## <span>Configuring Cumulus Quagga</span>

Cumulus Quagga does not start by default in Cumulus Linux. Before you
run Cumulus Quagga, make sure all you have enabled relevant daemons that
you intend to use — `zebra`, `bgpd`, `ospfd`, `ospf6d`, `ripd`,
`ripngd`, `isisd` — in the `/etc/quagga/daemons` file.

The `zebra` daemon must always be enabled. The others you can enable
according to how you plan to route your network — using
[BGP](/version/cumulus-linux-301/Layer_3_Features/Border_Gateway_Protocol_-_BGP)
for example, instead of
[OSPF](/version/cumulus-linux-301/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol).

Before you start Cumulus Quagga, you need to enable the corresponding
daemons. Edit the `/etc/quagga/daemons` file and set to *yes* each
daemon you are enabling.

    zebra=yes (* this one is mandatory to bring the others up)
    bgpd=yes
    ospfd=no
    ospf6d=no
    ripd=no
    ripngd=no
    isisd=no
    babeld=no

### <span>Enabling and Starting Cumulus Quagga</span>

Once you enable the appropriate daemons, then you need to enable and
start the Cumulus Quagga service.

    cumulus@switch:~$ sudo systemctl enable quagga.service 
    cumulus@switch:~$ sudo systemctl start quagga.service 

{{%notice tip%}}

All the routing protocol daemons (`bgpd`, `ospfd`, `ospf6d`, `ripd`,
`ripngd` and `isisd`) are dependent on `zebra`. When you start `quagga`,
`systemd` determines whether `zebra` is running; if `zebra` is not
running, it starts `zebra`, then starts the dependent service, such as
`bgpd`.

In general, if you restart a service, its dependent services also get
restarted. For example, running `systemctl restart quagga.service`
restarts any of the routing protocol daemons that are enabled and
running.

For more information on the `systemctl` command and changing the state
of daemons, read [Managing Application
Daemons](/version/cumulus-linux-301/System_Management/Managing_Application_Daemons).

{{%/notice%}}

### <span id="src-5118386_ConfiguringQuagga-integrated_cfg" class="confluence-anchor-link"></span><span>Understanding Integrated Configurations</span>

By default in Cumulus Linux, Quagga saves the configuration of all
daemons in a single integrated configuration file, `Quagga.conf`.

You can disable this mode by running:

    switch(config)# no service integrated-vtysh-config

To enable the integrated configuration file mode again, run:

    switch(config)# service integrated-vtysh-config

If you disable the integrated configuration mode, Quagga saves each
daemon-specific configuration file in a separate file. At a minimum for
a daemon to start, that daemon must be enabled and its daemon-specific
configuration file must be present, even if that file is empty.

You can save the current configuration by running:

    switch# write mem
    Building Configuration...
    Integrated configuration saved to /etc/quagga/Quagga.conf
    [OK]

{{%notice note%}}

You can use `write file` instead of `write mem`.

{{%/notice%}}

When the integrated configuration mode disabled, the output looks like
this:

    switch# write mem
    Building Configuration...
    Configuration saved to /etc/quagga/zebra.conf
    Configuration saved to /etc/quagga/bgpd.conf
    [OK]

### <span>Restoring the Default Configuration</span>

If you need to restore the Quagga configuration to the default running
configuration, you need to delete the `Quagga.conf` file and restart the
`quagga` service. You should back up `Quagga.conf` (or any configuration
files you may remove, see the note below) before proceeding.

1.  Confirm `service integrated-vtysh-config` is enabled:
    
    ``` 
    cumulus@switch$ sudo cl-rctl running-config |grep integrated
              service integrated-vtysh-config  
    ```

2.  Remove `/etc/quagga/Quagga.conf`:
    
        cumulus@switch$ sudo rm /etc/quagga/Quagga.conf

3.  Restart Quagga:
    
        cumulus@switch$ sudo systemctl restart quagga.service

{{%notice note%}}

If for some reason `service integrated-vtysh-config` is not configured,
then you should remove all the configuration files (such as `zebra.conf`
or `ospf6d.conf`) instead of `Quagga.conf` in step 2 above.

{{%/notice%}}

## <span>Interface IP Addresses and VRFs</span>

Quagga inherits the IP addresses and any associated routing tables for
the network interfaces from the `/etc/network/interfaces` file. This is
the recommended way to define the addresses; do **not** create
interfaces using Quagga. For more information, see [Configuring IP
Addresses](Configuring_and_Managing_Network_Interfaces.html#src-5118370_ConfiguringandManagingNetworkInterfaces-ip)
and [Virtual Routing and Forwarding -
VRF](/version/cumulus-linux-301/Layer_3_Features/Virtual_Routing_and_Forwarding_-_VRF).

## <span>Using the vtysh Modal CLI</span>

Quagga provides a CLI – `vtysh` – for configuring and displaying the
state of the protocols. It is invoked by running:

    cumulus@switch:~$ sudo vtysh
    
    Hello, this is Quagga (version 0.99.23.1+cl3.0).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
    
    switch#

`vtysh` provides a Cisco-like modal CLI, and many of the commands are
similar to Cisco IOS commands. By modal CLI, we mean that there are
different modes to the CLI, and certain commands are only available
within a specific mode. Configuration is available with the `configure
terminal` command, which is invoked thus:

    switch# configure terminal
    switch(config)#

The prompt displays the mode the CLI is in. For example, when the
interface-specific commands are invoked, the prompt changes to:

    switch(config)# interface swp1
    switch(config-if)#

When the routing protocol specific commands are invoked, the prompt
changes to:

    switch(config)# router ospf
    switch(config-router)#

At any level, ”?” displays the list of available top-level commands at
that level:

    switch(config-if)# ?
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

    switch(config-if)# bandwidth ?
    <1-10000000>  Bandwidth in kilobits
    switch(config-if)# ip ?
    address  Set the IP address of an interface
    irdp     Alter ICMP Router discovery preference this interface
    ospf     OSPF interface commands
    rip      Routing Information Protocol
    router   IP router interface commands

Displaying state can be done at any level, including the top level. For
example, to see the routing table as seen by `zebra`, you use:

    switch# show ip route
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

    switch(config-router)# do show ip route
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

    switch(config-router)# no area 0.0.0.1 range 10.10.10.0/24

The current state of the configuration can be viewed using the `show
running-config` command:

    switch# show running-config
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

{{%notice note%}}

If you attempt to configure a routing protocol that has not been
started, `vtysh` silently ignores those commands.

{{%/notice%}}

## <span id="src-5118386_ConfiguringQuagga-nonmodal" class="confluence-anchor-link"></span><span>Using the Cumulus Linux Non-Modal CLI</span>

Alternately, if you do not want to use a modal CLI to configure Quagga,
you can use a suite of [Cumulus Linux-specific
commands](/version/cumulus-linux-301/Layer_3_Features/Configuring_Quagga/Cumulus_Linux_Quagga_Commands)
instead.

## <span>Reloading the Quagga Configuration</span>

If you make a change to your routing configuration, you need to reload
Quagga so your changes take place. *Quagga reload* enables you to apply
only the modifications you make to your Quagga configuration,
synchronizing its running state with the configuration in
`/etc/quagga/Quagga.conf`. This is useful for optimizing automation of
Quagga in your environment or to apply changes made at runtime.

{{%notice note%}}

Quagga reload only applies to an integrated service configuration, where
your Quagga configuration is stored in a single `Quagga.conf` file
instead of one configuration file per Quagga daemon (like `zebra` or
`bgpd`).

{{%/notice%}}

To reload your Quagga configuration after you've modified
`/etc/quagga/Quagga.conf`, run:

    cumulus@switch:~$ sudo systemctl reload quagga.service

Examine the running configuration and verify that it matches the config
in `/etc/quagga/Quagga.conf`:

    cumulus@switch:~$ sudo cl-rctl running-config

### <span>Debugging</span>

If the running configuration is not what you expected, please [submit a
support
request](https://support.cumulusnetworks.com/hc/en-us/requests/new) and
supply the following information:

  - The current running configuration (run `sudo cl-rctl running-config`
    and output the contents to a file)

  - The contents of `/etc/quagga/Quagga.conf`

  - The contents of `/var/log/quagga/quagga-reload.log`

## <span>Useful Links</span>

  - [www.nongnu.org/quagga/docs/docs-info.html\#BGP](http://www.nongnu.org/quagga/docs/docs-info.html#BGP)

  - [www.nongnu.org/quagga/docs/docs-info.html\#IPv6-Support](http://www.nongnu.org/quagga/docs/docs-info.html#IPv6-Support)

  - [www.nongnu.org/quagga/docs/docs-info.html\#Zebra](http://www.nongnu.org/quagga/docs/docs-info.html#Zebra)
