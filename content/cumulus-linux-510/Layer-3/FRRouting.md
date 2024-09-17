---
title: FRRouting
author: NVIDIA
weight: 810
toc: 3
---
Cumulus Linux uses <span class="a-tooltip">[FRR](## "FRRouting")</span> to provide the routing protocols for dynamic routing and supports the following routing protocols:

- Open Shortest Path First ({{<link url="Open-Shortest-Path-First-v2-OSPFv2" text="v2">}} and {{<link url="Open-Shortest-Path-First-v3-OSPFv3" text="v3">}})
- {{<link url="Border-Gateway-Protocol-BGP" text="Border Gateway Protocol (BGP)">}}
- {{<link url="Protocol-Independent-Multicast-PIM" text="Protocol Independent Multicast (PIM)">}}
- {{<link url="Policy-based-Routing" text="Policy-based Routing (PBR)">}}
## Architecture

{{< img src = "/images/cumulus-linux/frrouting-overview-daemons.png" >}}

The FRR suite consists of various protocol-specific daemons and a protocol-independent daemon called `zebra`. Each of the protocol-specific daemons are responsible for running the relevant protocol and building the routing table based on the information exchanged.

It is not uncommon to have more than one protocol daemon running at the same time. For example, at the edge of an enterprise, protocols internal to an enterprise such as {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} run alongside the protocols that connect an enterprise to the rest of the world such as {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}}.

`zebra` is the daemon that resolves the routes provided by multiple protocols (including the static routes you specify) and programs these routes in the Linux kernel using `netlink` (in Linux). The {{<exlink url="http://docs.frrouting.org/en/latest/zebra.html" text="FRRouting documentation">}} defines `zebra` as the IP routing manager for FRR that provides kernel routing table updates, interface lookups, and redistribution of routes between different routing protocols.

## Configure FRR

{{%notice warning%}}
The information in this section does not apply if you use {{<link url="NVUE-CLI" text="NVUE">}} to configure your switch. NVUE manages FRR daemons and configuration automatically. These instructions are only applicable for users managing FRR directly through linux flat file configurations.
{{%/notice%}}

If you do not configure your system using {{<link url="NVUE-CLI" text="NVUE">}}, FRR does not start by default in Cumulus Linux. Before you run FRR, make sure you have enabled the relevant daemons that you intend to use (`bgpd`, `ospfd`, `ospf6d`, `pimd`, or `pbrd`) in the `/etc/frr/daemons` file.

{{%notice note%}}
NVIDIA has not tested <span class="a-tooltip">[RIP](## "Routing Information Protocol RIP")</span>, RIPv6, <span class="a-tooltip">[IS-IS](## "Intermediate System - Intermediate System")</span>, or <span class="a-tooltip">[Babel](## "a loop-avoiding distance-vector routing protocol")</span>.
{{%/notice%}}

Cumulus Linux enables the `zebra` daemon by default. You can enable the other daemons according to how you plan to route your network.

Before you start FRR, edit the `/etc/frr/daemons` file to enable each daemon you want to use. For example, to enable BGP, set `bgpd` to *yes*:

```
...
bgpd=yes
ospfd=no
ospf6d=no
ripd=no
ripngd=no
isisd=no
fabricd=no
pimd=no
ldpd=no
nhrpd=no
eigrpd=no
babeld=no
sharpd=no
pbrd=no
vrrpd=no
...
```

## Enable and Start FRR

{{%notice warning%}}
The information in this section does not apply if you use {{<link url="NVUE-CLI" text="NVUE">}} to configure your switch. NVUE manages FRR daemons and configuration automatically. These instructions are only applicable for users managing FRR directly through linux flat file configurations.
{{%/notice%}}

After you enable the appropriate daemons, enable and start the FRR service:

```
cumulus@switch:~$ sudo systemctl enable frr.service
cumulus@switch:~$ sudo systemctl start frr.service
```

{{%notice note%}}
- All the routing protocol daemons (`bgpd`, `ospfd`, `ospf6d`, `ripd`, `ripngd`, `isisd` and `pimd`) are dependent on `zebra`. When you start FRR, `systemd` determines whether zebra is running; if zebra is not running, `systemd` starts `zebra`, then starts the dependent service, such as `bgpd`.
- If you restart a service, its dependent services also restart. For example, running `systemctl restart frr.service` restarts any of the enabled routing protocol daemons that are running.
- For more information on the `systemctl` command and changing the state of daemons, see {{<link url="Services-and-Daemons-in-Cumulus-Linux" text="Services and Daemons in Cumulus Linux">}}.
{{%/notice%}}

## Restore the Default Configuration

{{%notice note%}}
The information in this section does not apply if you use NVUE to configure your switch. NVUE manages FRR daemons and configuration automatically. These instructions are only applicable if you manage FRR directly with linux flat file configurations.
{{%/notice%}}

If you need to restore the FRR configuration to the default running configuration, delete the `frr.conf` file and restart the `frr` service.

Back up `frr.conf` (or any configuration files you want to remove) before proceeding.

1. Confirm that `service integrated-vtysh-config` is running.

2. Remove `/etc/frr/frr.conf`:

    ```
    cumulus@switch:~$ sudo rm /etc/frr/frr.conf
    ```

3. Restart FRR with this command:

   ```
   cumulus@switch:~$ sudo systemctl restart frr.service
   ```

   {{%notice warning%}}
   Restarting FRR restarts all the routing protocol daemons that you enable and are running. NVIDIA recommends that you reboot the switch instead of restarting the FRR service to minimize traffic impact when redundant switches are present with MLAG.
   {{%/notice%}}

## Interface IP Addresses and VRFs

FRR inherits the IP addresses and any associated routing tables for the network interfaces from the `/etc/network/interfaces` file. This is the recommended way to define the addresses; do **not** create interfaces using FRR. For more information, see {{<link url="Interface-Configuration-and-Management/#configure-ip-addresses" text="Configure IP Addresses">}} and {{<link url="Virtual-Routing-and-Forwarding-VRF">}}.

## vtysh Modal CLI

FRR provides a command-line interface (CLI) called vtysh for configuring and displaying protocol state. To start the CLI, run the `sudo vtysh` command:

```
cumulus@switch:~$ sudo vtysh

Hello, this is FRRouting (version 8.4.3).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

switch#
```

FRR provides different modes to the CLI and certain commands are only available within a specific mode. Configuration is available with the `configure terminal` command:

```
switch# configure terminal
switch(config)#
```

The prompt displays the current CLI mode. For example, when you run the interface-specific commands, the prompt changes to:

```
switch(config)# interface swp1
switch(config-if)#
```

When you run the routing protocol specific commands, the prompt changes:

```
switch(config)# router ospf
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

In addition to ?-based completion, you can use tab completion to get help with the valid keywords or options as you enter commands. For example, using tab completion with `router ospf` shows the possible options for the command and returns you to the command prompt to complete the command.

```
switch(config)# router ospf vrf<<press tab>>
BLUE     RED      default  mgmt     
switch(config)# router ospf vrf
```

To search for specific vtysh commands so that you can identify the correct syntax to use, run the `sudo vtysh -c 'find <term>'` command. For example, to show only commands that include `mlag`:

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
<!-- vale off -->
To run the same command at a config level, prepend `do`:
<!-- vale on -->
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

To run single commands with vtysh, use the `-c` option:

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

To disable a command or feature in FRR, prepend the command with `no`. For example:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# no area 0.0.0.1 range 10.10.10.0/24
switch(config-router)# exit
switch(config)# exit
switch# write memory
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
If you try to configure a routing protocol that is not running, vtysh ignores those commands.
{{%/notice%}}

## NVUE Show Commands and vtysh Output

NVUE provides the `--output raw` option for certain NVUE show commands to show vtysh native output.

The following example shows the `nv show vrf default router bgp address-family l2vpn-evpn loc-rib` command with the `--output raw` option:

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib -o raw
BGP routing table entry for 6.0.0.6:2:[5]:[0]:[0]:[::]
Paths: (0 available, no best path)
  Not advertised to any peer
BGP routing table entry for 6.0.0.6:2:[5]:[0]:[16]:[21.0.0.0]
Paths: (0 available, no best path)
  Not advertised to any peer
Route Distinguisher: 6.0.0.6:2
BGP routing table entry for 6.0.0.6:2:[5]:[0]:[16]:[21.1.0.0]
Paths: (1 available, best #1)
  Advertised to non peer-group peers:
  spine11(220.10.0.17) spine12(220.11.0.17)
  Route [5]:[0]:[16]:[21.1.0.0] VNI 300011
  Local
    6.0.0.6 (leaf11) from 0.0.0.0 (6.0.0.6)
      Origin incomplete, metric 0, weight 32768, valid, sourced, local, bestpath-from-AS Local, best (First path received)
      Extended Community: ET:8 RT:65011:300011 Rmac:00:01:00:00:06:05
      Last update: Wed Mar  6 12:14:41 2024
BGP routing table entry for 6.0.0.6:2:[5]:[0]:[16]:[21.2.0.0]
Paths: (1 available, best #1)
  Advertised to non peer-group peers:
  spine11(220.10.0.17) spine12(220.11.0.17)
  Route [5]:[0]:[16]:[21.2.0.0] VNI 300011
  Local
    6.0.0.6 (leaf11) from 0.0.0.0 (6.0.0.6)
      Origin incomplete, metric 0, weight 32768, valid, sourced, local, bestpath-from-AS Local, best (First path received)
      Extended Community: ET:8 RT:65011:300011 Rmac:00:01:00:00:06:05
      Last update: Wed Mar  6 12:14:41 2024
BGP routing table entry for 6.0.0.6:2:[5]:[0]:[64]:[2020:0:1::]
Paths: (0 available, no best path)
  Not advertised to any peer
BGP routing table entry for 6.0.0.6:2:[5]:[0]:[64]:[2020:0:1:1::]
Paths: (1 available, best #1)
  Advertised to non peer-group peers:
  spine11(220.10.0.17) spine12(220.11.0.17)
  Route [5]:[0]:[64]:[2020:0:1:1::] VNI 300011
  Local
    6.0.0.6 (leaf11) from 0.0.0.0 (6.0.0.6)
      Origin incomplete, metric 1024, weight 32768, valid, sourced, local, bestpath-from-AS Local, best (First path received)
      Extended Community: ET:8 RT:65011:300011 Rmac:00:01:00:00:06:05
      Last update: Wed Mar  6 12:14:41 2024
```

{{< expand "NVUE Commands that support --output raw" >}}

```
nv show evpn multihoming esi
nv show evpn multihoming esi <esi_id>
nv show evpn vni <vni_id> multihoming esi
nv show evpn vni <vni_id> multihoming esi <esi_id>
nv show evpn vni <vni_id>
nv show vrf <tenant vrf> evpn
nv show vrf <tenant vrf> evpn bgp-info
nv show vrf <vrf> evpn nexthop-vtep <vtep>
nv show evpn vni <vni_id> bgp-info
nv show vrf default router bgp address-family l2vpn-evpn loc-rib
nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd <rd-id>
nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd <rd-id> route-type <type> route
nv show vrf <vrf-id> router bgp address-family <afi-safi> loc-rib
nv show vrf <vrf-id> router bgp address-family <afi-safi> loc-rib route
nv show vrf default router bgp neighbor
nv show vrf default router bgp neighbor <neighbor-id>
nv show vrf <vrf-id> router bgp nexthop
nv show vrf <vrf-id> router bgp nexthop ipv4
nv show vrf <vrf-id> router bgp nexthop ipv4 ip-address
nv show vrf <vrf-id> router bgp nexthop ipv4 ip-address <prefix>
nv show vrf <vrf-id> router bgp nexthop ipv6
nv show vrf <vrf-id> router bgp nexthop ipv6 ip-address
nv show vrf <vrf-id> router bgp nexthop ipv6 ip-address <prefix>
nv show vrf default router rib ipv4 route
nv show vrf default router rib ipv6 route
nv show vrf default router rib
nv show vrf default router rib ipv4
nv show vrf default router rib ipv6
```

{{< /expand >}}

## Next Hop Tracking

Routing daemons track the validity of next hops through notifications from the `zebra` daemon. For example, FRR uninstalls BGP routes that resolve to a next hop over a connected route in `zebra` when `bgpd` receives a next hop tracking (NHT) notification after `zebra` removes the connected route if the associated interface goes down.

The `zebra` daemon does not consider next hops that resolve to a default route as valid by default. You can configure NHT to consider a longest prefix match lookup for next hop addresses resolving to the default route as a valid next hop. The following example configures the default route to be valid for NHT in the default VRF:

{{< tabs "410">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router nexthop-tracking ipv4 resolved-via-default on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# ip nht resolve-via-default
leaf01(config)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

You can apply a route map to NHT for specific routing daemons to permit or deny routes from consideration as valid next hops. The following example applies `ROUTEMAP1` to BGP, preventing NHT from considering next hops resolving to 10.0.0.0/8 in the default VRF as valid:

{{< tabs "436">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy prefix-list PREFIX1 type ipv4
cumulus@leaf01:~$ nv set router policy prefix-list PREFIX1 rule 1 match 10.0.0.0/8
cumulus@leaf01:~$ nv set router policy prefix-list PREFIX1 rule 1 action permit
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 1 match ip-prefix-list PREFIX1
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 1 action deny 
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 2 action permit
cumulus@leaf01:~$ nv set vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1 protocol bgp
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf02# configure terminal
leaf02(config)# ip prefix-list PREFIX1 seq 1 permit 10.0.0.0/8
leaf02(config)# route-map ROUTEMAP1 deny 1
leaf02(config-route-map)#  match ip address prefix-list PREFIX1
leaf02(config-route-map)# route-map ROUTEMAP1 permit 2
leaf02(config-route-map)# ip nht bgp route-map ROUTEMAP1
leaf02(config)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

You can show tracked next hops with the following NVUE commands:
- `nv show vrf <vrf> router nexthop-tracking ipv4`
- `nv show vrf <vrf> router nexthop-tracking ipv4 <ip-address>`
- `nv show vrf <vrf> router nexthop-tracking ipv6`
- `nv show vrf <vrf> router nexthop-tracking ipv6 <ip-address>`

You can also run the vtysh `show ip nht vrf <vrf> <ip-address>` command.

## Reload the FRR Configuration

{{%notice warning%}}
The information in this section does not apply if you use {{<link url="NVUE-CLI" text="NVUE">}} to configure your switch. NVUE manages FRR daemons and configuration automatically. These instructions are only applicable for users managing FRR directly through linux flat file configurations.
{{%/notice%}}

If you make a change to your routing configuration, you need to reload FRR so your changes take place. *FRR reload* enables you to apply only the modifications you make to your FRR configuration, synchronizing its running state with the configuration in `/etc/frr/frr.conf`. This is useful for optimizing FRR automation in your environment or to apply changes made at runtime.

To reload your FRR configuration after you modify `/etc/frr/frr.conf`, run:

```
cumulus@switch:~$ sudo systemctl reload frr.service
```

Examine the running configuration and verify that it matches the configuration in `/etc/frr/frr.conf`.

If the running configuration is not what you expect, {{<exlink url="https://enterprise-support.nvidia.com/s/" text="submit a support request">}} and supply the following information:

- The current running configuration (run `show running-config` and output the contents to a file)
- The contents of `/etc/frr/frr.conf`
- The contents of `/var/log/frr/frr-reload.log`

## FRR Logging

{{%notice warning%}}
The information in this section does not apply if you use {{<link url="NVUE-CLI" text="NVUE">}} to configure your switch. NVUE manages FRR daemons and configuration automatically. These instructions are only applicable for users managing FRR directly through linux flat file configurations.
{{%/notice%}}

By default, Cumulus Linux configures FFR with syslog severity level 6 (informational). Log output writes to the `/var/log/frr/frr.log` file.

{{%notice note%}}
To write debug messages to the log file, you must run the `log syslog debug` command to configure FRR with syslog severity 7 (debug); otherwise, when you issue a debug command such as, `debug bgp neighbor-events`, no output goes to `/var/log/frr/frr.log`. However, when you manually define a log target with the `log file /var/log/frr/debug.log` command, FRR automatically defaults to severity 7 (debug) logging and the output logs to `/var/log/frr/debug.log`.
{{%/notice%}}

## Considerations

### Duplicate Hostnames

The switch can have two hostnames in the FRR configuration. For example:

```
cumulus@spine01:~$ sudo vtysh...
spine01# configure terminal
spine01(config)# hostname spine01-1
spine01-1(config)# do sh run
Building configuration...
Current configuration:
!
frr version 7.0+cl4u3
frr defaults datacenter
hostname spine01
hostname spine01-1
...
```

{{%notice note%}}
If you configure the same numbered BGP neighbor with both the `neighbor x.x.x.x` and `neighbor swp# interface` commands, two neighbor entries are present for the same IP address in the configuration. To correct this issue, update the configuration and restart the FRR service.
{{%/notice%}}

### TCP Sockets and BGP Peering Sessions

The FRR startup configuration includes a setting for the maximum number of open files allowed. For BGP, open files include TCP sockets that BGP connections use. Either BGP speaker can start a BGP peering almost simultaneously; therefore, you can have two TCP sockets for a single BGP peer. These two sockets exist until the BGP protocol determines which socket to use, then the other socket closes.

The default setting of 1024 open files supports up to 512 BGP peering sessions. If you expect your network deployment to have more BGP peering sessions, you need to update this setting.

{{%notice note%}}
NVIDIA recommends you set the value to at least twice the maximum number of BGP peering sessions you expect.
{{%/notice%}}

To update the open files setting:

1. Edit the `/lib/systemd/system/frr.service` file and change the `LimitNOFILE` parameter. The following example sets the `LimitNOFILE` parameter to 4096.

   ```
   cumulus@switch:~$ sudo cat /lib/systemd/system/frr.service
   [Unit]
   Description=FRRouting
   Documentation=https://frrouting.readthedocs.io/en/latest/setup.html
   After=networking.service csmgrd.service
   
   [Service]
   Nice=-5
   Type=forking
   NotifyAccess=all
   StartLimitInterval=3m
   StartLimitBurst=3
   TimeoutSec=2m
   WatchdogSec=60s
   RestartSec=5
   Restart=on-abnormal
   LimitNOFILE=4096
   ...
   ```

2. Restart the FRR service.

   ```
   cumulus@switch:~$ sudo systemctl restart frr.service
   ```

## Related Information

- {{<exlink url="https://frrouting.org" text="FRRouting website">}}
- {{<exlink url="https://github.com/FRRouting/frr" text="FRRouting project on GitHub">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/bgp.html" text="FRR BGP documentation">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/ipv6.html" text="FRR IPv6 support">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/zebra.html" text="FRR Zebra documentation">}}
