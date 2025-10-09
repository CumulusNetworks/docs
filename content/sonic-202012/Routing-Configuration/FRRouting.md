---
title: FRRouting
author: NVIDIA
weight: 510
product: SONiC
version: 202012
siteSlug: sonic
---

SONiC uses {{<exlink url="https://frrouting.org/" text="FRRouting">}} (FRR) to provide the routing protocols for dynamic routing. SONiC supports the border gateway routing protocol ({{<link url="Border-Gateway-Protocol-BGP" tet="BGP">}}) in FRR.

The FRRouting suite consists of various protocol-specific daemons and a protocol-independent daemon called `zebra`. Each protocol-specific daemon is responsible for running the relevant protocol and building the routing table based on the information exchanged.

## About zebra

`zebra` is the daemon that resolves the routes provided by multiple protocols (including the static routes you specify) and programs these routes in the Linux kernel via `netlink` (in Linux). The {{<exlink url="http://docs.frrouting.org/en/latest/zebra.html" text="FRRouting documentation">}} defines `zebra` as the IP routing manager for FRRouting that "provides kernel routing table updates, interface lookups, and redistribution of routes between different routing protocols."

## About FRR

The FRR configuration is stored in the `bgp` container. From the switch, you can check on the status and change the state of the `bgp` service.

```
admin@switch:~$ sudo systemctl status bgp.service
● bgp.service - BGP container
   Loaded: loaded (/usr/lib/systemd/system/bgp.service; enabled; vendor preset:
   Active: active (running) since Tue 2020-12-15 17:07:25 UTC; 1 day 4h ago
 Main PID: 1474 (bgp.sh)
    Tasks: 7 (limit: 4915)
   Memory: 20.0M
      CPU: 9.190s
   CGroup: /system.slice/bgp.service
           ├─1474 /bin/bash /usr/bin/bgp.sh wait
           └─1477 docker wait bgp

Warning: Journal has been rotated since unit was started. Log output is incomplete.
admin@switch:~$
```

## Configure FRR with the vtysh Modal CLI

FRR provides a command-line interface (CLI) called `vtysh` for configuring and displaying protocol state. To start the CLI, run the `sudo vtysh` command:

```
admin@switch:~$ sudo vtysh

Hello, this is FRRouting (version 0.99.23.1+cl3u2).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

switch#
```

`vtysh` provides a Cisco-like modal CLI and many of the commands are similar to Cisco IOS commands. There are different modes to the CLI and certain commands are only available within a specific mode. Once you enter the shell, you start configuring FRR using the `configure terminal` command:

```
switch# configure terminal
switch(config)#
```

The prompt displays the current CLI mode. For example, when the interface-specific commands are invoked, the prompt changes to:

```
switch(config)# interface swp1
switch(config-if)#
```

When you run routing protocol-specific commands, the prompt changes:

```
switch(config)# router bgp
switch(config-router)#
```

`?` displays the list of available top-level commands:

```
switch(config-if)# ?
  bandwidth    Set bandwidth informational parameter
  description  Interface specific description
  end          End current mode and change to enable mode
  exit         Exit current mode and down to previous mode
  ip           IP Information
  ipv6         IPv6 Information
  isis         IS-IS commands
  link-detect  Enable link detection on interface
  list         Print command list
  mpls-te      MPLS-TE specific commands
  multicast    Set multicast flag to interface
  no           Negate a command or set its defaults
  ptm-enable   Enable neighbor check with specified topology
  quit         Exit current mode and down to previous mode
  shutdown     Shutdown the selected interface
```

?-based completion is also available to see the parameters that a command takes:

```
switch(config-if)# bandwidth ?
<1-10000000>  Bandwidth in kilobits
switch(config-if)# ip ?
address  Set the IP address of an interface
irdp     Alter ICMP Router discovery preference this interface
ospf     OSPF interface commands
rip      Routing Information Protocol
router   IP router interface commands
```

To search for specific `vtysh` commands so that you can identify the correct syntax to use, run the `sudo vtysh -c 'find <term>'` command. For example, to show only commands that include `mlag`:

```
cumulus@leaf01:mgmt:~$ sudo vtysh -c 'find mlag'
  (view)  show ip pim [mlag] vrf all interface [detail|WORD] [json]
  (view)  show ip pim [vrf NAME] interface [mlag] [detail|WORD] [json]
  (view)  show ip pim [vrf NAME] mlag upstream [A.B.C.D [A.B.C.D]] [json]
  (view)  show ip pim mlag summary [json]
  (view)  show ip pim vrf all mlag upstream [json]
  (view)  show zebra mlag
  (enable)  [no$no] debug zebra mlag
  (enable)  debug pim mlag
  (enable)  no debug pim mlag
  (enable)  test zebra mlag <none$none|primary$primary|secondary$secondary>
  (enable)  show ip pim [mlag] vrf all interface [detail|WORD] [json]
  (enable)  show ip pim [vrf NAME] interface [mlag] [detail|WORD] [json]
  (enable)  show ip pim [vrf NAME] mlag upstream [A.B.C.D [A.B.C.D]] [json]
  (enable)  show ip pim mlag summary [json]
  (enable)  show ip pim vrf all mlag upstream [json]
  (enable)  show zebra mlag
  (config)  [no$no] debug zebra mlag
  (config)  debug pim mlag
  (config)  ip pim mlag INTERFACE role [primary|secondary] state [up|down] addr A.B.C.D
  (config)  no debug pim mlag
  (config)  no ip pim mlag
```

To move back up a level, use the `exit` command:

```
leaf01(config)# router bgp
leaf01(config-router)# exit
leaf01(config)#
```

You can display the state at any level, including the top level. For example, to see the routing table as seen by `zebra`:

```
switch# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, T - Table,
       > - selected route, * - FIB route
B>* 0.0.0.0/0 [20/0] via fe80::4638:39ff:fe00:c, swp29, 00:11:57
  *                  via fe80::4638:39ff:fe00:52, swp30, 00:11:57
B>* 10.0.0.1/32 [20/0] via fe80::4638:39ff:fe00:c, swp29, 00:11:57
  *                    via fe80::4638:39ff:fe00:52, swp30, 00:11:57
B>* 10.0.0.11/32 [20/0] via fe80::4638:39ff:fe00:5b, swp1, 00:11:57
B>* 10.0.0.12/32 [20/0] via fe80::4638:39ff:fe00:2e, swp2, 00:11:58
B>* 10.0.0.13/32 [20/0] via fe80::4638:39ff:fe00:57, swp3, 00:11:59
B>* 10.0.0.14/32 [20/0] via fe80::4638:39ff:fe00:43, swp4, 00:11:59
C>* 10.0.0.21/32 is directly connected, lo
B>* 10.0.0.51/32 [20/0] via fe80::4638:39ff:fe00:c, swp29, 00:11:57
  *                     via fe80::4638:39ff:fe00:52, swp30, 00:11:57
B>* 172.16.1.0/24 [20/0] via fe80::4638:39ff:fe00:5b, swp1, 00:11:57
  *                      via fe80::4638:39ff:fe00:2e, swp2, 00:11:57
B>* 172.16.3.0/24 [20/0] via fe80::4638:39ff:fe00:57, swp3, 00:11:59
  *                      via fe80::4638:39ff:fe00:43, swp4, 00:11:59
```

To run the same command at a config level, prepend `do`:

```
switch(config-router)# do show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, T - Table,
       > - selected route, * - FIB route
B>* 0.0.0.0/0 [20/0] via fe80::4638:39ff:fe00:c, swp29, 00:05:17
  *                  via fe80::4638:39ff:fe00:52, swp30, 00:05:17
B>* 10.0.0.1/32 [20/0] via fe80::4638:39ff:fe00:c, swp29, 00:05:17
  *                    via fe80::4638:39ff:fe00:52, swp30, 00:05:17
B>* 10.0.0.11/32 [20/0] via fe80::4638:39ff:fe00:5b, swp1, 00:05:17
B>* 10.0.0.12/32 [20/0] via fe80::4638:39ff:fe00:2e, swp2, 00:05:18
B>* 10.0.0.13/32 [20/0] via fe80::4638:39ff:fe00:57, swp3, 00:05:18
B>* 10.0.0.14/32 [20/0] via fe80::4638:39ff:fe00:43, swp4, 00:05:18
C>* 10.0.0.21/32 is directly connected, lo
B>* 10.0.0.51/32 [20/0] via fe80::4638:39ff:fe00:c, swp29, 00:05:17
  *                     via fe80::4638:39ff:fe00:52, swp30, 00:05:17
B>* 172.16.1.0/24 [20/0] via fe80::4638:39ff:fe00:5b, swp1, 00:05:17
  *                      via fe80::4638:39ff:fe00:2e, swp2, 00:05:17
B>* 172.16.3.0/24 [20/0] via fe80::4638:39ff:fe00:57, swp3, 00:05:18
  *                      via fe80::4638:39ff:fe00:43, swp4, 00:05:18
```

To run single commands with `vtysh`, use the `-c` option:

```
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
```

To run a command multiple levels down:

```
cumulus@switch:~$ sudo vtysh -c 'configure terminal' -c 'router ospf' -c 'area 0.0.0.1 range 10.10.10.0/24'
```

The commands also take a partial command name (for example, `sh ip route`) as long as the partial command name is not aliased:

```
cumulus@switch:~$ sudo vtysh -c 'sh ip r'
% Ambiguous command.
```

To disable a command or feature in FRRouting, prepend the command with `no`. For example:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# no area 0.0.0.1 range 10.10.10.0/24
switch(config-router)# exit
switch(config)# exit
switch# write mem
switch# exit
cumulus@switch:~$
```

To view the current state of the configuration, run the `show running-config` command:

{{< expand "Example command "  >}}

```
switch# show running-config
Building configuration...

Current configuration:
!
username cumulus nopassword
!
service integrated-vtysh-config
!
vrf mgmt
!
interface lo
  link-detect
!
interface swp1
  ipv6 nd ra-interval 10
  link-detect
!
interface swp2
  ipv6 nd ra-interval 10
  link-detect
!
interface swp3
  ipv6 nd ra-interval 10
  link-detect
!
interface swp4
  ipv6 nd ra-interval 10
  link-detect
!
interface swp29
  ipv6 nd ra-interval 10
  link-detect
!
interface swp30
  ipv6 nd ra-interval 10
  link-detect
!
interface swp31
  link-detect
!
interface swp32
  link-detect
!
interface vagrant
  link-detect
!
interface eth0 vrf mgmt
  ipv6 nd suppress-ra
  link-detect
!
interface mgmt vrf mgmt
  link-detect
!
router bgp 65020
  bgp router-id 10.0.0.21
  bgp bestpath as-path multipath-relax
  bgp bestpath compare-routerid
  neighbor fabric peer-group
  neighbor fabric remote-as external
  neighbor fabric description Internal Fabric Network
  neighbor fabric capability extended-nexthop
  neighbor swp1 interface peer-group fabric
  neighbor swp2 interface peer-group fabric
  neighbor swp3 interface peer-group fabric
  neighbor swp4 interface peer-group fabric
  neighbor swp29 interface peer-group fabric
  neighbor swp30 interface peer-group fabric
  !
  address-family ipv4 unicast
  network 10.0.0.21/32
  neighbor fabric activate
  neighbor fabric prefix-list dc-spine in
  neighbor fabric prefix-list dc-spine out
  exit-address-family
!
ip prefix-list dc-spine seq 10 permit 0.0.0.0/0
ip prefix-list dc-spine seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-spine seq 30 permit 172.16.1.0/24
ip prefix-list dc-spine seq 40 permit 172.16.2.0/24
ip prefix-list dc-spine seq 50 permit 172.16.3.0/24
ip prefix-list dc-spine seq 60 permit 172.16.4.0/24
ip prefix-list dc-spine seq 500 deny any
!
ip forwarding
ipv6 forwarding
!
line vty
!
end
```

{{< /expand >}}

{{%notice note%}}

If you try to configure a routing protocol that has not been started, `vtysh` silently ignores those commands.

{{%/notice%}}

## Reload the FRRouting Configuration

If you make a change to your routing configuration, you need to reload FRRouting so your changes take place. *FRRouting reload* enables you to apply only the modifications you make to your FRRouting configuration, synchronizing its running state with the configuration in `/etc/frr/frr.conf`. This is useful for optimizing FRRouting automation in your environment or to apply changes made at runtime.

{{%notice note%}}

FRRouting reload only applies to an integrated service configuration, where your FRRouting configuration is stored in a single `frr.conf` file instead of one configuration file per FRRouting daemon (like `zebra` or `bgpd`).

{{%/notice%}}

To reload your FRRouting configuration after you modify `/etc/frr/frr.conf`, run:

```
cumulus@switch:~$ sudo systemctl reload frr.service
```

Examine the running configuration and verify that it matches the configuration in `/etc/frr/frr.conf`:

```
cumulus@switch:~$ net show configuration
```

If the running configuration is not what you expect, {{<exlink url="https://support.mellanox.com/s/contact-support-page" text="submit a support request">}} and supply the following information:

- The current running configuration (run `net show configuration` and output the contents to a file)
- The contents of `/etc/frr/frr.conf`
- The contents of `/var/log/frr/frr-reload.log`

## Related Information

- {{<exlink url="https://frrouting.org" text="FRRouting website">}}
- {{<exlink url="https://github.com/FRRouting/frr" text="FRRouting project on GitHub">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/bgp.html" text="FRR BGP documentation">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/ipv6.html" text="FRR IPv6 support">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/zebra.html" text="FRR Zebra documentation">}}

