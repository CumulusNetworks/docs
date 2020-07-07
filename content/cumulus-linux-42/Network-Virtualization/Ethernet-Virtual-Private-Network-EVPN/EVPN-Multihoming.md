---
title: EVPN Multihoming
author: Cumulus Networks
weight: 555
toc: 4
---
{{%notice warning%}}

EVPN multihoming is an {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/202933878" text="early access feature">}}.

{{%/notice%}}

*EVPN multihoming* (EVPN-MH) is standards-based replacement for MLAG in data centers deploying Clos topologies. Replacing MLAG removes the final dependency on a layer 2 topology, allowing for:

- Layer 3 virtualization
- Removing complexity
- Increasing scale
- Providing a single control plane
- Multi-vendor interoperability

EVPN-MH routes traffic using BGP-EVPN type-1, type-2 and type-4 routes, and the FDB, MDB and neighbor databases all sync between the Ethernet segment peers via these routes as well. The VTEPs connect to each other over an *{{<exlink url="https://tools.ietf.org/html/rfc7432#section-5" text="Ethernet segment">}}*. An Ethernet segment is a group of switch or server links that share a unique Ethernet segment ID (ESI).

Configuring EVPN-MH involves setting an Ethernet segment system MAC address (`es-sys-mac`) and an Ethernet segment ID (`es-id`) on a static or LACP bond. The `es-id` must be globally unique for all the nodes on the segment. However, if your specific topology does not require a system MAC address for each Ethernet segment, you can configure a global system MAC address that is inherited into all the Ethernet segments. You do this by configuring the same `es-sys-mac` for each interface.

{{%notice note%}}

An Ethernet segment can span more than two switches, unlike MLAG, where the `clag-id` is shared between two switches only. Further, a peerlink is not required to connect the systems on an Ethernet segment. Each Ethernet segment is a distinct redundancy group.

{{%/notice%}}

## Supported Features

- Known unicast traffic multihoming via type-1/EAD (Ethernet auto discovery) routes and type-2 (non-zero ESI) routes. Includes active-active redundancy via aliasing and support for fast failover.
- EVPN BUM traffic handling with {{<link title="EVPN BUM Traffic with PIM-SM" text="EVPN-PIM">}} on multihomed sites via Type-4/ESR routes. Includes split-horizon-filtering and designated forwarder election.
- {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge mode">}} only.
- {{<link url="Inter-subnet-Routing/#symmetric-routing" text="Distributed symmetric routing">}}.
- {{<link url="Basic-Configuration/#arp-and-nd-suppression" text="ARP suppression">}} must be enabled.
- EVI (*EVPN virtual instance*). Cumulus Linux supports VLAN-based service only, so the EVI is just a layer 2 VNI.
- Supported RIOT-capable {{<exlink url="https://cumulusnetworks.com/hcl" text="ASICs">}} include Broadcom Trident3, Trident II+ and Maverick, and Mellanox Spectrum and Spectrum 2.

{{%notice info%}}

EVPN-MH is incompatible with MLAG. In order to use EVPN-MH, you must remove any MLAG configuration. This entails:

- Removing the `clag-id` from all interfaces in the `/etc/network/interfaces` file.
- Removing the peerlink interfaces in the `/etc/network/interfaces` file.
- Stopping and disabling the `clagd` service.
      
      cumulus@switch:~$ sudo systemctl stop clagd.service
      cumulus@switch:~$ sudo systemctl disable clagd.service

{{%/notice%}}

## Configure EVPN-MH

There are two required settings for an EVPN multihoming configuration:

- The Ethernet segment ID (`es-id`)
- The Ethernet segment system MAC address (`es-sys-mac`)

These settings are applied to interfaces, typically bonds.

An Ethernet segment configuration has these characteristics:

- The `es-id` is a 24-bit integer (1-16777215).
- Each interface (bond) needs its own `es-id`.
- Static and LACP bonds can be associated with an `es-id`.
- FRRouting does not prevent association of a switch port with an `es-id`.
- One `es-id` can only be associated with one device. You cannot have swp1->ES-1:1 and swp2->ES-1:1. To allow swp1 and swp2 to be a part of a single Ethernet segment, they would need to be LAG-bonded and then associate the bond with ES-1:1.
- Each rack can have a maximum of 128 Ethernet segments.

You can also specify a *designated forwarder* (`df-pref`) to maximize the load balancing between the VTEPs on an Ethernet segment. The VTEP with the highest `df-pref` setting becomes the designated forwarder. VTEPs that are *not* the DF block BUM traffic received on the VXLAN overlay to the Ethernet segment.

`ifupdown2` generates the FRR EVPN-MH configuration and reloads FRR. The configuration appears in both the `/etc/network/interfaces` file and in `/etc/frr/frr.conf` file.

### Configure the EVPN-MH Bonds

To configure bond interfaces for EVPN multihoming, run commands similar to the following:

{{<tabs "bond config">}}

{{<tab "NCLU Commands">}}

```
cumulus@switch:~$ net add bond hostbond1 bond slaves swp5
cumulus@switch:~$ net add bond hostbond2 bond slaves swp6
cumulus@switch:~$ net add bond hostbond3 bond slaves swp7
cumulus@switch:~$ net add bond hostbond1 evpn mh es-id 1
cumulus@switch:~$ net add bond hostbond2 evpn mh es-id 2
cumulus@switch:~$ net add bond hostbond3 evpn mh es-id 3
cumulus@switch:~$ net add bond hostbond1-3 evpn mh es-sys-mac 44:38:39:ff:ff:01
cumulus@switch:~$ net add bond hostbond1-3 evpn mh es-df-pref 50000
cumulus@switch:~$ net commit
```

{{</tab>}}

{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

leaf01# configure terminal
leaf01(config)# interface hostbond1
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 1
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf01(config-if)# exit
leaf01(config)# interface hostbond2
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 2
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf01(config-if)# exit
leaf01(config)# interface hostbond3
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 3
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf01(config-if)# exit
leaf01(config)# write memory
leaf01(config)# exit
leaf01# exit
cumulus@leaf01:~$
```

{{</tab>}}

{{</tabs>}}

The NCLU commands create the following configuration in the `/etc/network/interfaces` file. If you are editing the `/etc/network/interfaces` file directly, apply a configuration like the following:

```
interface hostbond1
  evpn mh es-df-pref 50000
  evpn mh es-id 1
  evpn mh es-sys-mac 44:38:39:ff:ff:01
  bond-slaves swp5
  es-sys-mac 44:38:39:ff:ff:01

interface hostbond2
  evpn mh es-df-pref 50000
  evpn mh es-id 2
  evpn mh es-sys-mac 44:38:39:ff:ff:01
  bond-slaves swp6
  es-sys-mac 44:38:39:ff:ff:01

interface hostbond3
  evpn mh es-df-pref 50000
  evpn mh es-id 3
  evpn mh es-sys-mac 44:38:39:ff:ff:01
  bond-slaves swp7
  es-sys-mac 44:38:39:ff:ff:01
```

These commands also create the following configuration in the `/etc/frr/frr.conf` file.

```
!
interface hostbond1
 evpn mh es-df-pref 50000
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond2
 evpn mh es-df-pref 50000
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond3
 evpn mh es-df-pref 50000
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
```

### EVPN MH Global Settings

There are a few global settings for EVPN multihoming you can set, including:

- `mac-holdtime`: MAC hold time, in seconds. This is the duration for which a switch maintains SYNC MAC entries after the Ethernet segment peer's EVPN route is deleted. During this time, the switch attempts to independently establish reachability of the MAC on the local Ethernet segment. The hold time can be between 0 and 86400 seconds.
- `neigh-holdtime`:  Neighbor entry hold time, in seconds. The duration for which a switch maintains SYNC neigh entries after the Ethernet segment peer's EVPN route is deleted. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. The hold time can be between 0 and 86400 seconds.
- `redirect-off`: **Cumulus VX only.** Disables fast failover of traffic destined to the access port via the VXLAN overlay. This knob only applies to Cumulus VX, since fast failover is not supported.
- `startup-delay`:  Startup delay. The duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. The delay can be between 0 and 216000 seconds.

To configure a MAC hold time for 1000 seconds, run the following commands:

{{<tabs "MAC hold time">}}

{{<tab "NCLU Commands">}}

    cumulus@switch:~$ net add evpn mh mac-holdtime 1200
    cumulus@switch:~$ net commit

{{</tab>}}

{{<tab "vtysh Commands">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# evpn mh mac-holdtime 1200
switch(config)# exit
switch# write memory
```

{{</tab>}}

{{</tabs>}}

This creates the following configuration in the `/etc/frr/frr.conf` file:

```
evpn mh mac-holdtime 1200
```

To configure a neighbor hold time for 600 seconds, run the following commands:

{{<tabs "Neighbor hold time">}}

{{<tab "NCLU Commands">}}

    cumulus@switch:~$ net add evpn mh neigh-holdtime 600
    cumulus@switch:~$ net commit

{{</tab>}}

{{<tab "vtysh Commands">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# evpn mh neigh-holdtime 600
switch(config)# exit
switch# write memory
```

{{</tab>}}

{{</tabs>}}

This creates the following configuration in the `/etc/frr/frr.conf` file:

```
evpn mh neigh-holdtime 600
```

To configure a startup delay for 1800 seconds, run the following commands:

{{<tabs "startup delay">}}

{{<tab "NCLU Commands">}}

    cumulus@switch:~$ net add evpn mh startup-delay 1800
    cumulus@switch:~$ net commit

{{</tab>}}

{{<tab "vtysh Commands">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# evpn mh startup-delay 1800
switch(config)# exit
switch# write memory
```

{{</tab>}}

{{</tabs>}}

This creates the following configuration in the `/etc/frr/frr.conf` file:

```
evpn mh startup-delay 1800
```

### Enable Uplink Tracking

You can enable uplink tracking on a multihomed bond or switch port. When all uplinks are down, the Ethernet segment bonds on the switch are put into a proto-down or error-disabled state.

{{<tabs "upink tracking">}}

{{<tab "NCLU Commands">}}

    cumulus@switch:~$ net add interface swp1-4 evpn mh uplink
    cumulus@switch:~$ net add interface swp1-4 pim
    cumulus@switch:~$ net commit

{{</tab>}}

{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

leaf01# configure terminal
leaf01(config)# interface swp1
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface swp2
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface swp3
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface swp4
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# write memory
leaf01(config)# exit
leaf01# exit
cumulus@leaf01:~$
```

{{</tab>}}

{{</tabs>}}

These commands create the following configuration in the `/etc/frr/frr.conf` file:

```
...
!
interface swp1
 evpn mh uplink
 ip pim
!
interface swp2
 evpn mh uplink
 ip pim
!
interface swp3
 evpn mh uplink
 ip pim
!
interface swp4
 evpn mh uplink
 ip pim
!
...
```

### Enable FRR Debugging

You can add debug statements to the `/etc/frr/frr.conf` file to debug the Ethernet segments, routes and routing protocols (via Zebra). To debug Ethernet segments and routes, use the `net add bgp debug evpn mh (es|route)` command. To debug the routing protocols

{{<tabs "debug">}}

{{<tab "NCLU Commands">}}

    cumulus@switch:~$ net add bgp debug evpn mh es
    cumulus@switch:~$ net add bgp debug evpn mh route
    cumulus@switch:~$ net add evpn mh debug zebra
    cumulus@switch:~$ net add evpn mh debug zebra es
    cumulus@switch:~$ net add evpn mh debug zebra mac
    cumulus@switch:~$ net add evpn mh debug zebra neigh
    cumulus@switch:~$ net add evpn mh debug zebra nh
    cumulus@switch:~$ net commit

{{</tab>}}

{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

leaf01# configure terminal
leaf01(config)# debug bgp evpn mh es
leaf01(config)# debug bgp evpn mh route
leaf01(config)# debug bgp zebra
leaf01(config)# debug zebra evpn mh es
leaf01(config)# debug zebra evpn mh mac
leaf01(config)# debug zebra evpn mh neigh
leaf01(config)# debug zebra evpn mh nh
leaf01(config)# debug zebra vxlan
leaf01(config)# write memory
leaf01(config)# exit
leaf01# exit
cumulus@leaf01:~$
```

{{</tab>}}

{{</tabs>}}

These commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@switch:~$ cat /etc/frr/frr.conf
frr version 7.4+cl4u1
frr defaults datacenter

...

!
debug bgp evpn mh es
debug bgp evpn mh route
debug bgp zebra
debug zebra evpn mh es
debug zebra evpn mh mac
debug zebra evpn mh neigh
debug zebra evpn mh nh
debug zebra vxlan
!
...
```

### Fast Failover

When an Ethernet segment link goes down, the attached VTEP notifies all other VTEPs via a single EAD-ES withdraw. Via ES bond redirect.

Fast failover is also triggered by:

- Failure of an access port &mdash; the link between a leaf switch and host.
- Rebooting a leaf switch or VTEP.
- Uplink failure. When all uplinks are down, the Ethernet segment bonds on the switch are proto-downed or error disabled.

## Troubleshooting

You can use the following `net show` commands to troubleshoot your EVPN multihoming configuration.

### Show EAD Route Types

You can use the `net show bgp evpn route` command to view type-1 EAD routes. Just include the `ead` route type option.

```
cumulus@switch:~$ net show bgp evpn route type ead
BGP table version is 30, local router ID is 172.16.0.21
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [4]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 172.16.0.21:2
*> [1]:[0]:[03:44:38:39:ff:ff:01:00:00:01]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005
*> [1]:[0]:[03:44:38:39:ff:ff:01:00:00:02]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005
*> [1]:[0]:[03:44:38:39:ff:ff:01:00:00:03]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005
Route Distinguisher: 172.16.0.21:3
*> [1]:[4294967295]:[03:44:38:39:ff:ff:01:00:00:01]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 ESI-label-Rt:AA RT:5556:1005 RT:5556:1003 RT:5556:1008 RT:5556:1000 RT:5556:1007 RT:5556:1009 RT:5556:1002 RT:5556:1006 RT:5556:1004 RT:5556:1001
Route Distinguisher: 172.16.0.21:4
*> [1]:[4294967295]:[03:44:38:39:ff:ff:01:00:00:02]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 ESI-label-Rt:AA RT:5556:1005 RT:5556:1003 RT:5556:1008 RT:5556:1000 RT:5556:1007 RT:5556:1009 RT:5556:1002 RT:5556:1006 RT:5556:1004 RT:5556:1001
Route Distinguisher: 172.16.0.21:5
*> [1]:[4294967295]:[03:44:38:39:ff:ff:01:00:00:03]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 ESI-label-Rt:AA RT:5556:1005 RT:5556:1003 RT:5556:1008 RT:5556:1000 RT:5556:1007 RT:5556:1009

...

Displayed 198 prefixes (693 paths) (of requested type)
cumulus@switch:~$
```

You can add the `detail` option for more detailed output:

```
cumulus@switch:~$ net show bgp evpn route detail type ead
BGP routing table entry for 172.16.0.21:2:[1]:[0]:[03:44:38:39:ff:ff:01:00:00:00]:[128]:[0.0.0.0]
Paths: (0 available, no best path)
  Not advertised to any peer
Route Distinguisher: 172.16.0.21:2
BGP routing table entry for 172.16.0.21:2:[1]:[0]:[03:44:38:39:ff:ff:01:00:00:01]:[128]:[0.0.0.0]
Paths: (1 available, best #1)
  Advertised to non peer-group peers:
  spine01(swp1) spine01(swp2) spine02(swp3) spine02(swp4)
  Route [1]:[0]:[03:44:38:39:ff:ff:01:00:00:01]:[128]:[0.0.0.0] VNI 1005
  Local
    172.16.0.21 from 0.0.0.0 (172.16.0.21)
      Origin IGP, weight 32768, valid, sourced, local, bestpath-from-AS Local, best (First path received)
      Extended Community: ET:8 RT:5556:1005
      Last update: Wed Jun  3 22:51:24 2020
BGP routing table entry for 172.16.0.21:2:[1]:[0]:[03:44:38:39:ff:ff:01:00:00:02]:[128]:[0.0.0.0]
Paths: (0 available, no best path)
  Not advertised to any peer
BGP routing table entry for 172.16.0.21:2:[1]:[0]:[03:44:38:39:ff:ff:01:00:00:02]:[128]:[0.0.0.0]
Paths: (1 available, best #1)
  Advertised to non peer-group peers:
  spine01(swp1) spine01(swp2) spine02(swp3) spine02(swp4)
  Route [1]:[0]:[03:44:38:39:ff:ff:01:00:00:02]:[128]:[0.0.0.0] VNI 1005
  Local
    172.16.0.21 from 0.0.0.0 (172.16.0.21)
      Origin IGP, weight 32768, valid, sourced, local, bestpath-from-AS Local, best (First path received)
      Extended Community: ET:8 RT:5556:1005
      Last update: Wed Jun  3 22:51:24 2020
BGP routing table entry for 172.16.0.21:2:[1]:[0]:[03:44:38:39:ff:ff:01:00:00:03]:[128]:[0.0.0.0]
Paths: (1 available, best #1)
  Advertised to non peer-group peers:
  spine01(swp1) spine01(swp2) spine02(swp3) spine02(swp4)
  Route [1]:[0]:[03:44:38:39:ff:ff:01:00:00:03]:[128]:[0.0.0.0] VNI 1005
  Local
    172.16.0.21 from 0.0.0.0 (172.16.0.21)
      Origin IGP, weight 32768, valid, sourced, local, bestpath-from-AS Local, best (First path received)
      Extended Community: ET:8 RT:5556:1005
      Last update: Wed Jun  3 22:51:24 2020

...

Displayed 198 prefixes (693 paths) (of requested type)
cumulus@switch:~$
```

### Show the Ethernet Segment MAC and IP Addresses

The `net show bgp l2vpn evpn route mac-ip-es` command displays the MAC address and IP address for each Ethernet segment.

```
cumulus@switch:~$ net show bgp l2vpn evpn route mac-ip-es
BGP table version is 0, local router ID is 172.16.0.21
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [4]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
*  [2]:[0]:[48]:[00:02:00:00:00:09]
                    172.16.0.23                              0 4435 5558 i
                    ESI:03:44:38:39:ff:ff:01:00:00:01 VNI: 1001
                    RT:5558:1001 RT:5558:4001 ET:8 Rmac:00:02:00:00:00:68
*  [2]:[0]:[48]:[00:02:00:00:00:09]
                    172.16.0.23                              0 4435 5558 i
                    ESI:03:44:38:39:ff:ff:01:00:00:01 VNI: 1001
                    RT:5558:1001 RT:5558:4001 ET:8 Rmac:00:02:00:00:00:68
*  [2]:[0]:[48]:[00:02:00:00:00:09]
                    172.16.0.23                              0 4435 5558 i
                    ESI:03:44:38:39:ff:ff:01:00:00:01 VNI: 1001
                    RT:5558:1001 RT:5558:4001 ET:8 Rmac:00:02:00:00:00:68
*  [2]:[0]:[48]:[00:02:00:00:00:09]
                    172.16.0.23                              0 4435 5558 i
                    ESI:03:44:38:39:ff:ff:01:00:00:01 VNI: 1001
                    RT:5558:1001 RT:5558:4001 ET:8 Rmac:00:02:00:00:00:68
*> [2]:[0]:[48]:[00:02:00:00:00:09]
                    172.16.0.21                          32768 i
                    ESI:03:44:38:39:ff:ff:01:00:00:01 VNI: 1001
                    ET:8 RT:5556:1001 RT:5556:4001 Rmac:00:02:00:00:00:58
*> [2]:[0]:[48]:[00:02:00:00:00:09]
                    172.16.0.21                          32768 i
                    ESI:03:44:38:39:ff:ff:01:00:00:01 VNI: 1007
                    ET:8 RT:5556:1007 RT:5556:4002 Rmac:00:02:00:00:00:58

...

Displayed 2079 paths
cumulus@switch:~$
```

### Show Ethernet Segment Information

The `net show bgp l2vpn evpn es` command displays route information for the Ethernet segments (type-4 routes).

```
cumulus@switch:~$ net show bgp evpn es
Flags: L local, R remote, I inconsistent
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI
VNI      ESI                            Flags VTEPs
1005     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1005     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1005     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1005     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1005     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1005     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1002     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1002     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1001     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1001     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1006     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1006     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1006     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1006     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1006     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1006     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1000     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1000     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1000     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1000     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1000     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1000     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1003     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1003     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1003     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1003     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1003     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1003     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1004     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1004     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1004     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1004     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1004     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1004     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1007     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1007     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1007     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1007     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1007     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1007     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1008     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1008     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1008     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1008     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1008     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1008     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1009     03:44:38:39:ff:ff:01:00:00:01  LR    172.16.0.22(EV),172.16.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:02  LR    172.16.0.22(EV),172.16.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:03  LR    172.16.0.22(EV),172.16.0.23(EV)
1009     03:44:38:39:ff:ff:02:00:00:01  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1009     03:44:38:39:ff:ff:02:00:00:02  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
1009     03:44:38:39:ff:ff:02:00:00:03  R     172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
cumulus@switch:~$
```

You can add the `detail` option for more detailed output:

```
cumulus@switch:~$ net show bgp evpn es detail
VNI: 1005 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: LR
 Inconsistencies: -
 VTEPs: 172.16.0.22(EV),172.16.0.23(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 172.16.0.22(EV),172.16.0.23(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 172.16.0.22(EV),172.16.0.23(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 172.16.0.24(EV),172.16.0.25(EV),172.16.0.26(EV)
...
cumulus@switch:~$
```

### Show Ethernet Segment Interfaces

The `net show evpn es` command displays the interfaces and VTEPs associated with each Ethernet segment.

```
cumulus@switch:~$ net show evpn es
Type: L local, R remote, N non-DF
ESI                            Type ES-IF                 VTEPs
03:44:38:39:ff:ff:01:00:00:01  R    -                     27.0.0.22,27.0.0.23
03:44:38:39:ff:ff:01:00:00:02  LR   hostbond2             27.0.0.22,27.0.0.23
03:44:38:39:ff:ff:01:00:00:03  LR   hostbond3             27.0.0.22,27.0.0.23
03:44:38:39:ff:ff:01:00:00:05  L    hostbond1
03:44:38:39:ff:ff:02:00:00:01  R    -                     27.0.0.24,27.0.0.25,27.0.0.26
03:44:38:39:ff:ff:02:00:00:02  R    -                     27.0.0.24,27.0.0.25,27.0.0.26
03:44:38:39:ff:ff:02:00:00:03  R    -                     27.0.0.24,27.0.0.25,27.0.0.26
```

You can add the `detail` option for more detailed output:

```
cumulus@switch:~$ net show evpn es detail
ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: Remote
 Interface: -
 Ready for BGP: no
 VNI Count: 0
 MAC Count: 7
 DF: status: df preference: 50000
 Nexthop group: 536870913
 VTEPs:
     27.0.0.22 df_alg: preference df_pref: 32767 nh: 268435467
     27.0.0.23 df_alg: preference df_pref: 32767 nh: 268435464

ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: Local,Remote
 Interface: hostbond2
 State: up
 Bridge port: yes
 Ready for BGP: yes
 VNI Count: 10
 MAC Count: 13
 DF: status: df preference: 50000
 Nexthop group: 536870914
 VTEPs:
     27.0.0.22 df_alg: preference df_pref: 32767 nh: 268435467
     27.0.0.23 df_alg: preference df_pref: 32767 nh: 268435464

ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: Local,Remote
 Interface: hostbond3
 State: up
 Bridge port: yes
 Ready for BGP: yes
 VNI Count: 10
 MAC Count: 13
 DF: status: df preference: 50000
 Nexthop group: 536870915
 VTEPs:
     27.0.0.22 df_alg: preference df_pref: 32767 nh: 268435467
     27.0.0.23 df_alg: preference df_pref: 32767 nh: 268435464

ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: Local
 Interface: hostbond1
 State: up
 Bridge port: yes
 Ready for BGP: yes
 VNI Count: 10
 MAC Count: 4
 DF: status: df preference: 50000
 Nexthop group: 536870924
 VTEPs:

ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: Remote
 Interface: -
 Ready for BGP: no
 VNI Count: 0
 MAC Count: 13
 DF: status: df preference: 0
 Nexthop group: 536870918
 VTEPs:
     27.0.0.24 nh: 268435461
     27.0.0.25 nh: 268435466
     27.0.0.26 nh: 268435465

ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: Remote
 Interface: -
 Ready for BGP: no
 VNI Count: 0
 MAC Count: 13
 DF: status: df preference: 0
 Nexthop group: 536870916
 VTEPs:
     27.0.0.24 nh: 268435461
     27.0.0.25 nh: 268435466
     27.0.0.26 nh: 268435465

ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: Remote
 Interface: -
 Ready for BGP: no
 VNI Count: 0
 MAC Count: 13
 DF: status: df preference: 0
 Nexthop group: 536870919
 VTEPs:
     27.0.0.24 nh: 268435461
     27.0.0.25 nh: 268435466
     27.0.0.26 nh: 268435465
cumulus@switch:~$
```

### Show VNIs for each Ethernet Segment

To see the VNIs associated with each Ethernet segment, run:

```
cumulus@switch:~$ net show evpn es-evi
Type: L local, R remote
VNI      ESI                            Type
1005     03:44:38:39:ff:ff:01:00:00:02  L
1005     03:44:38:39:ff:ff:01:00:00:03  L
1005     03:44:38:39:ff:ff:01:00:00:05  L
1002     03:44:38:39:ff:ff:01:00:00:02  L
1002     03:44:38:39:ff:ff:01:00:00:03  L
1002     03:44:38:39:ff:ff:01:00:00:05  L
1001     03:44:38:39:ff:ff:01:00:00:02  L
1001     03:44:38:39:ff:ff:01:00:00:03  L
1001     03:44:38:39:ff:ff:01:00:00:05  L
1006     03:44:38:39:ff:ff:01:00:00:02  L
1006     03:44:38:39:ff:ff:01:00:00:03  L
1006     03:44:38:39:ff:ff:01:00:00:05  L
1000     03:44:38:39:ff:ff:01:00:00:02  L
1000     03:44:38:39:ff:ff:01:00:00:03  L
1000     03:44:38:39:ff:ff:01:00:00:05  L
1003     03:44:38:39:ff:ff:01:00:00:02  L
1003     03:44:38:39:ff:ff:01:00:00:03  L
1003     03:44:38:39:ff:ff:01:00:00:05  L
1004     03:44:38:39:ff:ff:01:00:00:02  L
1004     03:44:38:39:ff:ff:01:00:00:03  L
1004     03:44:38:39:ff:ff:01:00:00:05  L
1007     03:44:38:39:ff:ff:01:00:00:02  L
1007     03:44:38:39:ff:ff:01:00:00:03  L
1007     03:44:38:39:ff:ff:01:00:00:05  L
1008     03:44:38:39:ff:ff:01:00:00:02  L
1008     03:44:38:39:ff:ff:01:00:00:03  L
1008     03:44:38:39:ff:ff:01:00:00:05  L
1009     03:44:38:39:ff:ff:01:00:00:02  L
1009     03:44:38:39:ff:ff:01:00:00:03  L
1009     03:44:38:39:ff:ff:01:00:00:05  L
```

You can add the `detail` option for more detailed output:

```
cumulus@switch:~$ net show evpn es-evi detail
VNI 1005 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1005 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1005 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1002 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1002 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1002 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1001 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1001 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1001 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1006 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1006 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1006 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1000 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1000 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1000 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1003 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1003 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1003 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1004 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1004 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1004 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1007 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1007 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1007 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1008 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1008 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1008 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes

VNI 1009 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: L
 Ready for BGP: yes

VNI 1009 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: L
 Ready for BGP: yes

VNI 1009 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Ready for BGP: yes
cumulus@switch:~$
```

### Show VTEPs in Ethernet Segments

To show VTEPs for all Ethernet segments for all VNIs, run `net show bgp evpn es-evi`:

```
cumulus@switch:~$ net show bgp evpn es-evi
Flags: L local, R remote, I inconsistent
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI
VNI      ESI                            Flags VTEPs
1005     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1005     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1005     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1005     03:44:38:39:ff:ff:01:00:00:05  L  
1005     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1005     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1005     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1002     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:05  L  
1002     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1001     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:05  L  
1001     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1006     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1006     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1006     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1006     03:44:38:39:ff:ff:01:00:00:05  L  
1006     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1006     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1006     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1000     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1000     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1000     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1000     03:44:38:39:ff:ff:01:00:00:05  L  
1000     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1000     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1000     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1003     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1003     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1003     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1003     03:44:38:39:ff:ff:01:00:00:05  L  
1003     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1003     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1003     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1004     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1004     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1004     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1004     03:44:38:39:ff:ff:01:00:00:05  L  
1004     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1004     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1004     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1007     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1007     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1007     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1007     03:44:38:39:ff:ff:01:00:00:05  L  
1007     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1007     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1007     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1008     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1008     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1008     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1008     03:44:38:39:ff:ff:01:00:00:05  L  
1008     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1008     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1008     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1009     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:05  L  
1009     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1009     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1009     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
cumulus@switch:~$
```

You can add the `detail` option for more detailed output:

```
cumulus@switch:~$ net show bgp evpn es-evi detail
VNI: 1005 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1005 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1005 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1002 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1002 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1002 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1002 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1002 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1002 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1002 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1001 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1001 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1001 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1001 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1001 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1001 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1001 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1006 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1006 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1006 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1006 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1006 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1006 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1006 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1000 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1000 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1000 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1000 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1000 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1000 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1000 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1003 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1003 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1003 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1003 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1003 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1003 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1003 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1004 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1004 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1004 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1004 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1004 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1004 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1004 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1007 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1007 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1007 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1007 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1007 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1007 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1007 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1008 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1008 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1008 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1008 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1008 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1008 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1008 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1009 ESI: 03:44:38:39:ff:ff:01:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1009 ESI: 03:44:38:39:ff:ff:01:00:00:02
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1009 ESI: 03:44:38:39:ff:ff:01:00:00:03
 Type: LR
 Inconsistencies: -
 VTEPs: 27.0.0.22(EV),27.0.0.23(EV)

VNI: 1009 ESI: 03:44:38:39:ff:ff:01:00:00:05
 Type: L
 Inconsistencies: -
 VTEPs: -

VNI: 1009 ESI: 03:44:38:39:ff:ff:02:00:00:01
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1009 ESI: 03:44:38:39:ff:ff:02:00:00:02
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)

VNI: 1009 ESI: 03:44:38:39:ff:ff:02:00:00:03
 Type: R
 Inconsistencies: -
 VTEPs: 27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV) 
cumulus@switch:~$
```

To see the VTEPs for a specific VNI, run `net show bgp evpn es-evi vni`.

```
cumulus@switch:~$ net show bgp evpn es-evi vni 1009
Flags: L local, R remote, I inconsistent
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI
VNI      ESI                            Flags VTEPs
1009     03:44:38:39:ff:ff:01:00:00:01  R     27.0.0.22(EV),27.0.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:02  LR    27.0.0.22(EV),27.0.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:03  LR    27.0.0.22(EV),27.0.0.23(EV)
1009     03:44:38:39:ff:ff:01:00:00:05  L
1009     03:44:38:39:ff:ff:02:00:00:01  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1009     03:44:38:39:ff:ff:02:00:00:02  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
1009     03:44:38:39:ff:ff:02:00:00:03  R     27.0.0.24(EV),27.0.0.25(EV),27.0.0.26(EV)
cumulus@switch:~$
```

## Example Configuration

The following example uses the topology illustrated here.

IMAGE_TO_GO_HERE

### Configuration Commands

This section lists the NCLU commands to configure the switches and the network as well as the `vtysh` commands to configure FRRouting.

If you are not using NCLU to configure the `/etc/network/interfaces` file, go to {{<link url="#etcnetworkinterfaces" text="/etc/network/interfaces">}} below and copy the configurations directly into the `interfaces` file on each switch and server in the topology.

{{<tabs "example config commands">}}

{{<tab "leaf01">}}

**NCLU Commands**

```
cumulus@leaf01:~$ net show configuration commands
net del all
net add dns nameserver ipv4 192.168.0.3 vrf mgmt
net add time ntp server 0.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 1.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 2.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 3.cumulusnetworks.pool.ntp.org iburst
net add time ntp source eth0
net add snmp-server listening-address localhost
net add bgp autonomous-system 5556
net add bond hostbond1-3 evpn mh es-df-pref 50000
net add bond hostbond1-3 evpn mh es-sys-mac 44:38:39:ff:ff:01
net add interface ipmr-lo,lo,swp1-4 pim
net add interface swp1-4 evpn mh uplink
net add bond hostbond1 evpn mh es-id 1
net add bond hostbond2 evpn mh es-id 2
net add bond hostbond3 evpn mh es-id 3
net add interface lo igmp
net add routing defaults datacenter
net add routing log file /var/log/frr/bgpd.log
net add routing log timestamp precision 6
net add routing line vty exec-timeout 0 0
net add vrf vrf2 vni 4002
net add vrf vrf3 vni 4003
net add bgp router-id 172.16.0.21
net add bgp bestpath as-path multipath-relax
net add bgp neighbor swp1 interface v6only remote-as external
net add bgp neighbor swp2 interface v6only remote-as external
net add bgp neighbor swp3 interface v6only remote-as external
net add bgp neighbor swp4 interface v6only remote-as external
net add bgp ipv4 unicast redistribute connected
net add bgp ipv6 unicast redistribute connected
net add bgp ipv6 unicast neighbor swp1 activate
net add bgp ipv6 unicast neighbor swp2 activate
net add bgp ipv6 unicast neighbor swp3 activate
net add bgp ipv6 unicast neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  advertise-all-vni
net add bgp l2vpn evpn  advertise-svi-ip
net add time zone Etc/UTC
net add ptp global slave-only no
net add ptp global priority1 255
net add ptp global priority2 255
net add ptp global domain-number 0
net add ptp global logging-level 5
net add ptp global path-trace-enabled no
net add ptp global use-syslog yes
net add ptp global verbose no
net add ptp global summary-interval 0
net add ptp global time-stamping
net add bond hostbond1 bond slaves swp5
net add bond hostbond2 bond slaves swp6
net add bond hostbond3 bond slaves swp7
net add bond hostbond4 bond slaves swp8
net add vxlan vx-1000 vxlan id 1000
net add vxlan vx-1001 vxlan id 1001
net add vxlan vx-1002 vxlan id 1002
net add vxlan vx-1003 vxlan id 1003
net add vxlan vx-1004 vxlan id 1004
net add vxlan vx-1005 vxlan id 1005
net add vxlan vx-1006 vxlan id 1006
net add vxlan vx-1007 vxlan id 1007
net add vxlan vx-1008 vxlan id 1008
net add vxlan vx-1009 vxlan id 1009
net add vxlan vx-4001 vxlan id 4001
net add vxlan vx-4002 vxlan id 4002
net add vxlan vx-4003 vxlan id 4003
net add bond hostbond1 alias Local Node/s leaf01 and Ports swp5 <==> Remote Node/s host01 and Ports swp1
net add bond hostbond1,4 bridge pvid 1000
net add bond hostbond1-4 bond mode 802.3ad
net add bond hostbond1-4 mtu 9152
net add bond hostbond2 alias Local Node/s leaf01 and Ports swp6 <==> Remote Node/s host02 and Ports swp1
net add bond hostbond2 bridge pvid 1001
net add bond hostbond3 alias Local Node/s leaf01 and Ports swp7 <==> Remote Node/s hostd-13 and Ports swp1
net add bond hostbond3 bridge pvid 1002
net add bond hostbond4 alias Local Node/s leaf01 and Ports swp8 <==> Remote Node/s hosts-m1-14 and Ports swp1
net add evpn mh startup-delay 30
net add bond hostbond1-4 bond lacp-rate 1
net add bond hostbond1-3 es-sys-mac 44:38:39:ff:ff:01
net add bridge bridge ports vx-1000,vx-1001,vx-1002,vx-1003,vx-1004,vx-1005,vx-1006,vx-1007,vx-1008,vx-1009,vx-4001,vx-4002,vx-4003,hostbond4,hostbond1,hostbond2,hostbond3
net add bridge bridge pvid 1
net add bridge bridge vids 1000-1009
net add bridge bridge vlan-aware
net add interface eth0 ip address 192.168.0.15/24
net add interface eth0 ip gateway 192.168.0.2
net add interface eth0 vrf mgmt
net add interface swp1 alias Local Node leaf01 and Ports swp1 <==> Remote Node/s spine01 and Ports swp1
net add interface swp1-4 mtu 9202
net add interface swp1-8 link speed 10000
net add interface swp2 alias Local Node leaf01 and Ports swp2 <==> Remote Node/s spine01 and Ports swp2
net add interface swp3 alias Local Node leaf01 and Ports swp3 <==> Remote Node/s spine02 and Ports swp1
net add interface swp4 alias Local Node leaf01 and Ports swp4 <==> Remote Node/s spine02 and Ports swp2
net add loopback lo alias BGP un-numbered Use for Vxlan Src Tunnel
net add loopback lo ip address 172.16.0.21/32
net add vlan 1000 ip address 172.20.0.12/24
net add vlan 1000 ip address-virtual 00:00:5e:00:01:01 172.20.0.1/24
net add vlan 1000 ipv6 address 2001:db8::c/64
net add vlan 1000 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8::1/64
net add vlan 1000 vlan-id 1000
net add vlan 1000 vlan-raw-device bridge
net add vlan 1000 vrf vrf1
net add vlan 1001 ip address 172.20.1.12/24
net add vlan 1001 ip address-virtual 00:00:5e:00:01:01 172.20.1.1/24
net add vlan 1001 ipv6 address 2001:db8:0:1::c/64
net add vlan 1001 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:1::1/64
net add vlan 1001 vlan-id 1001
net add vlan 1001 vlan-raw-device bridge
net add vlan 1001 vrf vrf1
net add vlan 1002 ip address 172.20.2.12/24
net add vlan 1002 ip address-virtual 00:00:5e:00:01:01 172.20.2.1/24
net add vlan 1002 ipv6 address 2001:db8:0:2::c/64
net add vlan 1002 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:2::1/64
net add vlan 1002 vlan-id 1002
net add vlan 1002 vlan-raw-device bridge
net add vlan 1002 vrf vrf1
net add vlan 1003 ip address 172.20.3.12/24
net add vlan 1003 ip address-virtual 00:00:5e:00:01:01 172.20.3.1/24
net add vlan 1003 ipv6 address 2001:db8:0:3::c/64
net add vlan 1003 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:3::1/64
net add vlan 1003 vlan-id 1003
net add vlan 1003 vlan-raw-device bridge
net add vlan 1003 vrf vrf1
net add vlan 1004 ip address 172.20.4.12/24
net add vlan 1004 ip address-virtual 00:00:5e:00:01:01 172.20.4.1/24
net add vlan 1004 ipv6 address 2001:db8:0:4::c/64
net add vlan 1004 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:4::1/64
net add vlan 1004 vlan-id 1004
net add vlan 1004 vlan-raw-device bridge
net add vlan 1004 vrf vrf2
net add vlan 1005 ip address 172.20.5.12/24
net add vlan 1005 ip address-virtual 00:00:5e:00:01:01 172.20.5.1/24
net add vlan 1005 ipv6 address 2001:db8:0:5::c/64
net add vlan 1005 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:5::1/64
net add vlan 1005 vlan-id 1005
net add vlan 1005 vlan-raw-device bridge
net add vlan 1005 vrf vrf2
net add vlan 1006 ip address 172.20.6.12/24
net add vlan 1006 ip address-virtual 00:00:5e:00:01:01 172.20.6.1/24
net add vlan 1006 ipv6 address 2001:db8:0:6::c/64
net add vlan 1006 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:6::1/64
net add vlan 1006 vlan-id 1006
net add vlan 1006 vlan-raw-device bridge
net add vlan 1006 vrf vrf2
net add vlan 1007 ip address 172.20.7.12/24
net add vlan 1007 ip address-virtual 00:00:5e:00:01:01 172.20.7.1/24
net add vlan 1007 ipv6 address 2001:db8:0:7::c/64
net add vlan 1007 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:7::1/64
net add vlan 1007 vlan-id 1007
net add vlan 1007 vlan-raw-device bridge
net add vlan 1007 vrf vrf2
net add vlan 1008 ip address 172.20.8.12/24
net add vlan 1008 ip address-virtual 00:00:5e:00:01:01 172.20.8.1/24
net add vlan 1008 ipv6 address 2001:db8:0:8::c/64
net add vlan 1008 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:8::1/64
net add vlan 1008 vlan-id 1008
net add vlan 1008 vlan-raw-device bridge
net add vlan 1008 vrf vrf3
net add vlan 1009 ip address 172.20.9.12/24
net add vlan 1009 ip address-virtual 00:00:5e:00:01:01 172.20.9.1/24
net add vlan 1009 ipv6 address 2001:db8:0:9::c/64
net add vlan 1009 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:9::1/64
net add vlan 1009 vlan-id 1009
net add vlan 1009 vlan-raw-device bridge
net add vlan 1009 vrf vrf3
net add vlan 4001 vlan-id 4001
net add vlan 4001 vlan-raw-device bridge
net add vlan 4001 vrf vrf1
net add vlan 4002 vlan-id 4002
net add vlan 4002 vlan-raw-device bridge
net add vlan 4002 vrf vrf2
net add vlan 4003 vlan-id 4003
net add vlan 4003 vlan-raw-device bridge
net add vlan 4003 vrf vrf3
net add vrf mgmt ip address 172.16.0.1/8
net add vrf mgmt ipv6 address ::1/128
net add vrf mgmt,vrf1-3 vrf-table auto
net add vxlan vx-1000 bridge access 1000
net add vxlan vx-1000 vxlan mcastgrp 203.0.113.100
net add vxlan vx-1000-1009,4001-4003 bridge arp-nd-suppress on
net add vxlan vx-1000-1009,4001-4003 bridge learning off
net add vxlan vx-1000-1009,4001-4003 mtu 9152
net add vxlan vx-1000-1009,4001-4003 stp bpduguard
net add vxlan vx-1000-1009,4001-4003 stp portbpdufilter
net add vxlan vx-1000-1009,4001-4003 vxlan local-tunnelip 172.16.0.21
net add vxlan vx-1001 bridge access 1001
net add vxlan vx-1001 vxlan mcastgrp 203.0.113.101
net add vxlan vx-1002 bridge access 1002
net add vxlan vx-1002 vxlan mcastgrp 203.0.113.102
net add vxlan vx-1003 bridge access 1003
net add vxlan vx-1003 vxlan mcastgrp 203.0.113.103
net add vxlan vx-1004 bridge access 1004
net add vxlan vx-1004 vxlan mcastgrp 203.0.113.104
net add vxlan vx-1005 bridge access 1005
net add vxlan vx-1005 vxlan mcastgrp 203.0.113.105
net add vxlan vx-1006 bridge access 1006
net add vxlan vx-1006 vxlan mcastgrp 203.0.113.106
net add vxlan vx-1007 bridge access 1007
net add vxlan vx-1007 vxlan mcastgrp 203.0.113.107
net add vxlan vx-1008 bridge access 1008
net add vxlan vx-1008 vxlan mcastgrp 203.0.113.108
net add vxlan vx-1009 bridge access 1009
net add vxlan vx-1009 vxlan mcastgrp 203.0.113.109
net add vxlan vx-4001 bridge access 4001
net add vxlan vx-4001 vxlan mcastgrp 203.0.13.29
net add vxlan vx-4002 bridge access 4002
net add vxlan vx-4002 vxlan mcastgrp 203.0.13.30
net add vxlan vx-4003 bridge access 4003
net add vxlan vx-4003 vxlan mcastgrp 203.0.13.31
net add dot1x radius accounting-port 1813
net add dot1x eap-reauth-period 0
net add dot1x default-dacl-preauth-filename default_preauth_dacl.rules
net add dot1x radius authentication-port 1812
net add dot1x mab-activation-delay 30
net commit
```

**vtysh Commands**

Use `vtysh` to configure FRRouting:

```
cumulus@leaf01:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

leaf01# configure terminal
leaf01(config)# hostname leaf01
leaf01(config)# log file /var/log/frr/bgpd.log
leaf01(config)# log timestamp precision 6
leaf01(config)# evpn mh startup-delay 30
leaf01(config)# zebra nexthop proto only
leaf01(config)# ip pim rp 192.0.2.5 203.0.113.0/24
leaf01(config)# ip pim spt-switchover infinity-and-beyond
leaf01(config)# service integrated-vtysh-config
leaf01(config)# debug bgp evpn mh es
leaf01(config)# debug bgp evpn mh route
leaf01(config)# debug bgp zebra
leaf01(config)# debug zebra evpn mh es
leaf01(config)# debug zebra evpn mh mac
leaf01(config)# debug zebra evpn mh neigh
leaf01(config)# debug zebra evpn mh nh
leaf01(config)# debug zebra vxlan
leaf01(config)# enable password cn321
leaf01(config)# password cn321
leaf01(config)# vrf vrf1
leaf01(config-vrf)# vni 4001
leaf01(config-vrf)# exit-vrf
leaf01(config)# vrf vrf2
leaf01(config-vrf)# vni 4002
leaf01(config-vrf)# exit-vrf
leaf01(config)# vrf vrf3
leaf01(config-vrf)# vni 4003
leaf01(config-vrf)# exit-vrf
leaf01(config)# interface hostbond1
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 1
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf01(config-if)# exit
leaf01(config)# interface hostbond2
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 2
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf01(config-if)# exit
leaf01(config)# interface hostbond3
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 3
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf01(config-if)# exit
leaf01(config)# interface ipmr-lo
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface lo
leaf01(config-if)# ip igmp
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface swp1
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface swp2
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface swp3
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# interface swp4
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# ip pim
leaf01(config-if)# exit
leaf01(config)# router bgp 5556
leaf01(config-router)# bgp router-id 172.16.0.21
leaf01(config-router)# bgp bestpath as-path multipath-relax
leaf01(config-router)# neighbor swp1 interface v6only remote-as external
leaf01(config-router)# neighbor swp2 interface v6only remote-as external
leaf01(config-router)# neighbor swp3 interface v6only remote-as external
leaf01(config-router)# neighbor swp4 interface v6only remote-as external
leaf01(config-router)# address-family ipv4 unicast
leaf01(config-router-af)# address-family ipv4 unicast
leaf01(config-router-af)# exit-address-family
leaf01(config-router)# address-family ipv6 unicast
leaf01(config-router-af)# redistribute connected
leaf01(config-router-af)# neighbor swp1 activate
leaf01(config-router-af)# neighbor swp2 activate
leaf01(config-router-af)# neighbor swp3 activate
leaf01(config-router-af)# neighbor swp4 activate
leaf01(config-router-af)# exit-address-family
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# neighbor swp1 activate
leaf01(config-router-af)# neighbor swp2 activate
leaf01(config-router-af)# neighbor swp3 activate
leaf01(config-router-af)# neighbor swp4 activate
leaf01(config-router-af)#  advertise-all-vni
leaf01(config-router-af)# advertise-svi-ip
leaf01(config-router-af)# exit-address-family
leaf01(config-router)# exit
leaf01(config)# line vty
leaf01(config-line)# exec-timeout 0 0
leaf01(config-line)# exit
leaf01(config)# write memory
leaf01(config)# exit
leaf01# exit
cumulus@leaf01:~$
```

{{</tab>}}

{{<tab "leaf02">}}

**NCLU Commands**

```
cumulus@leaf02:~$ net show configuration commands
net del all
net add dns nameserver ipv4 192.168.0.3 vrf mgmt
net add time ntp server 0.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 1.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 2.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 3.cumulusnetworks.pool.ntp.org iburst
net add time ntp source eth0
net add snmp-server listening-address localhost
net add bgp autonomous-system 5557
net add interface swp2-4 evpn mh uplink
net add interface lo,swp1-4 pim sm
net add bond hostbond1-3 evpn mh es-sys-mac 44:38:39:ff:ff:01
net add bond hostbond1 evpn mh es-id 1
net add bond hostbond2 evpn mh es-id 2
net add bond hostbond3 evpn mh es-id 3
net add interface lo igmp
net add routing password cn321
net add routing enable password cn321
net add routing log timestamp precision 6
net add routing log file /var/log/frr/zebra.log
net add routing zebra debug vxlan
net add routing zebra debug kernel
net add routing zebra debug events
net add routing mroute debug
net add routing mroute debug detail
net add routing log file /var/log/frr/bgpd.log
net add routing line vty exec-timeout 0 0
net add bgp debug zebra
net add bgp debug updates
net add vrf vrf1 vni 4001
net add vrf vrf2 vni 4002
net add vrf vrf3 vni 4003
net add pim debug events
net add pim debug zebra
net add pim debug packets register
net add pim debug packets joins
net add pim debug trace
net add msdp debug events
net add pim rp 192.0.2.5 203.0.113.0/24
net add pim spt-switchover infinity-and-beyond
net add bgp debug evpn mh es
net add bgp debug evpn mh route
net add bgp bestpath as-path multipath-relax
net add bgp router-id 172.16.0.22
net add bgp neighbor swp1 interface v6only remote-as external
net add bgp neighbor swp2 interface v6only remote-as external
net add bgp neighbor swp3 interface v6only remote-as external
net add bgp neighbor swp4 interface v6only remote-as external
net add bgp ipv4 unicast redistribute connected
net add bgp ipv6 unicast redistribute connected
net add bgp ipv6 unicast neighbor swp1 activate
net add bgp ipv6 unicast neighbor swp2 activate
net add bgp ipv6 unicast neighbor swp3 activate
net add bgp ipv6 unicast neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  advertise-all-vni
net add bgp l2vpn evpn  advertise-svi-ip
net add time zone Etc/UTC
net add ptp global slave-only no
net add ptp global priority1 255
net add ptp global priority2 255
net add ptp global domain-number 0
net add ptp global logging-level 5
net add ptp global path-trace-enabled no
net add ptp global use-syslog yes
net add ptp global verbose no
net add ptp global summary-interval 0
net add ptp global time-stamping
net add bond hostbond1 bond slaves swp5
net add bond hostbond2 bond slaves swp6
net add bond hostbond3 bond slaves swp7
net add bond hostbond4 bond slaves swp8
net add vxlan vx-1000 vxlan id 1000
net add vxlan vx-1001 vxlan id 1001
net add vxlan vx-1002 vxlan id 1002
net add vxlan vx-1003 vxlan id 1003
net add vxlan vx-1004 vxlan id 1004
net add vxlan vx-1005 vxlan id 1005
net add vxlan vx-1006 vxlan id 1006
net add vxlan vx-1007 vxlan id 1007
net add vxlan vx-1008 vxlan id 1008
net add vxlan vx-1009 vxlan id 1009
net add vxlan vx-4001 vxlan id 4001
net add vxlan vx-4002 vxlan id 4002
net add vxlan vx-4003 vxlan id 4003
net add bond hostbond1 alias Local Node/s leaf02 and Ports swp5 <==> Remote Node/s host01 and Ports swp2
net add bond hostbond1,4 bridge pvid 1000
net add bond hostbond1-4 bond mode 802.3ad
net add bond hostbond1-4 mtu 9152
net add bond hostbond2 alias Local Node/s leaf02 and Ports swp6 <==> Remote Node/s host02 and Ports swp2
net add bond hostbond2 bridge pvid 1001
net add bond hostbond3 alias Local Node/s leaf02 and Ports swp7 <==> Remote Node/s hostd-13 and Ports swp2
net add bond hostbond3 bridge pvid 1002
net add bond hostbond4 alias Local Node/s leaf02 and Ports swp8 <==> Remote Node/s hosts-m2-14 and Ports swp1
net add bridge bridge ports vx-1000,vx-1001,vx-1002,vx-1003,vx-1004,vx-1005,vx-1006,vx-1007,vx-1008,vx-1009,vx-4001,vx-4002,vx-4003,hostbond4,hostbond1,hostbond2,hostbond3
net add bridge bridge pvid 1
net add bridge bridge vids 1000-1009
net add bridge bridge vlan-aware
net add interface eth0 ip address 192.168.0.15/24
net add interface eth0 ip gateway 192.168.0.2
net add interface eth0 vrf mgmt
net add interface swp1 alias Local Node leaf02 and Ports swp1 <==> Remote Node/s spine01 and Ports swp3
net add interface swp1-4 mtu 9202
net add interface swp1-8 link speed 10000
net add interface swp2 alias Local Node leaf02 and Ports swp2 <==> Remote Node/s spine01 and Ports swp4
net add interface swp3 alias Local Node leaf02 and Ports swp3 <==> Remote Node/s spine02 and Ports swp3
net add interface swp4 alias Local Node leaf02 and Ports swp4 <==> Remote Node/s spine02 and Ports swp4
net add loopback lo alias BGP un-numbered Use for Vxlan Src Tunnel
net add loopback lo ip address 172.16.0.22/32
net add vlan 1000 ip address 172.20.0.14/24
net add vlan 1000 ip address-virtual 00:00:5e:00:01:01 172.20.0.1/24
net add vlan 1000 ipv6 address 2001:db8::e/64
net add vlan 1000 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8::1/64
net add vlan 1000 vlan-id 1000
net add vlan 1000 vlan-raw-device bridge
net add vlan 1000 vrf vrf1
net add vlan 1001 ip address 172.20.1.14/24
net add vlan 1001 ip address-virtual 00:00:5e:00:01:01 172.20.1.1/24
net add vlan 1001 ipv6 address 2001:db8:0:1::e/64
net add vlan 1001 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:1::1/64
net add vlan 1001 vlan-id 1001
net add vlan 1001 vlan-raw-device bridge
net add vlan 1001 vrf vrf1
net add vlan 1002 ip address 172.20.2.14/24
net add vlan 1002 ip address-virtual 00:00:5e:00:01:01 172.20.2.1/24
net add vlan 1002 ipv6 address 2001:db8:0:2::e/64
net add vlan 1002 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:2::1/64
net add vlan 1002 vlan-id 1002
net add vlan 1002 vlan-raw-device bridge
net add vlan 1002 vrf vrf1
net add vlan 1003 ip address 172.20.3.14/24
net add vlan 1003 ip address-virtual 00:00:5e:00:01:01 172.20.3.1/24
net add vlan 1003 ipv6 address 2001:db8:0:3::e/64
net add vlan 1003 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:3::1/64
net add vlan 1003 vlan-id 1003
net add vlan 1003 vlan-raw-device bridge
net add vlan 1003 vrf vrf1
net add vlan 1004 ip address 172.20.4.14/24
net add vlan 1004 ip address-virtual 00:00:5e:00:01:01 172.20.4.1/24
net add vlan 1004 ipv6 address 2001:db8:0:4::e/64
net add vlan 1004 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:4::1/64
net add vlan 1004 vlan-id 1004
net add vlan 1004 vlan-raw-device bridge
net add vlan 1004 vrf vrf2
net add vlan 1005 ip address 172.20.5.14/24
net add vlan 1005 ip address-virtual 00:00:5e:00:01:01 172.20.5.1/24
net add vlan 1005 ipv6 address 2001:db8:0:5::e/64
net add vlan 1005 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:5::1/64
net add vlan 1005 vlan-id 1005
net add vlan 1005 vlan-raw-device bridge
net add vlan 1005 vrf vrf2
net add vlan 1006 ip address 172.20.6.14/24
net add vlan 1006 ip address-virtual 00:00:5e:00:01:01 172.20.6.1/24
net add vlan 1006 ipv6 address 2001:db8:0:6::e/64
net add vlan 1006 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:6::1/64
net add vlan 1006 vlan-id 1006
net add vlan 1006 vlan-raw-device bridge
net add vlan 1006 vrf vrf2
net add vlan 1007 ip address 172.20.7.14/24
net add vlan 1007 ip address-virtual 00:00:5e:00:01:01 172.20.7.1/24
net add vlan 1007 ipv6 address 2001:db8:0:7::e/64
net add vlan 1007 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:7::1/64
net add vlan 1007 vlan-id 1007
net add vlan 1007 vlan-raw-device bridge
net add vlan 1007 vrf vrf2
net add vlan 1008 ip address 172.20.8.14/24
net add vlan 1008 ip address-virtual 00:00:5e:00:01:01 172.20.8.1/24
net add vlan 1008 ipv6 address 2001:db8:0:8::e/64
net add vlan 1008 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:8::1/64
net add vlan 1008 vlan-id 1008
net add vlan 1008 vlan-raw-device bridge
net add vlan 1008 vrf vrf3
net add vlan 1009 ip address 172.20.9.14/24
net add vlan 1009 ip address-virtual 00:00:5e:00:01:01 172.20.9.1/24
net add vlan 1009 ipv6 address 2001:db8:0:9::e/64
net add vlan 1009 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:9::1/64
net add vlan 1009 vlan-id 1009
net add vlan 1009 vlan-raw-device bridge
net add vlan 1009 vrf vrf3
net add vlan 4001 vlan-id 4001
net add vlan 4001 vlan-raw-device bridge
net add vlan 4001 vrf vrf1
net add vlan 4002 vlan-id 4002
net add vlan 4002 vlan-raw-device bridge
net add vlan 4002 vrf vrf2
net add vlan 4003 vlan-id 4003
net add vlan 4003 vlan-raw-device bridge
net add vlan 4003 vrf vrf3
net add vrf mgmt ip address 172.16.0.1/8
net add vrf mgmt ipv6 address ::1/128
net add vrf mgmt,vrf1-3 vrf-table auto
net add vxlan vx-1000 bridge access 1000
net add vxlan vx-1000 vxlan mcastgrp 203.0.113.100
net add vxlan vx-1000-1009,4001-4003 bridge arp-nd-suppress on
net add vxlan vx-1000-1009,4001-4003 bridge learning off
net add vxlan vx-1000-1009,4001-4003 mtu 9152
net add vxlan vx-1000-1009,4001-4003 stp bpduguard
net add vxlan vx-1000-1009,4001-4003 stp portbpdufilter
net add vxlan vx-1000-1009,4001-4003 vxlan local-tunnelip 172.16.0.22
net add vxlan vx-1001 bridge access 1001
net add vxlan vx-1001 vxlan mcastgrp 203.0.113.101
net add vxlan vx-1002 bridge access 1002
net add vxlan vx-1002 vxlan mcastgrp 203.0.113.102
net add vxlan vx-1003 bridge access 1003
net add vxlan vx-1003 vxlan mcastgrp 203.0.113.103
net add vxlan vx-1004 bridge access 1004
net add vxlan vx-1004 vxlan mcastgrp 203.0.113.104
net add vxlan vx-1005 bridge access 1005
net add vxlan vx-1005 vxlan mcastgrp 203.0.113.105
net add vxlan vx-1006 bridge access 1006
net add vxlan vx-1006 vxlan mcastgrp 203.0.113.106
net add vxlan vx-1007 bridge access 1007
net add vxlan vx-1007 vxlan mcastgrp 203.0.113.107
net add vxlan vx-1008 bridge access 1008
net add vxlan vx-1008 vxlan mcastgrp 203.0.113.108
net add vxlan vx-1009 bridge access 1009
net add vxlan vx-1009 vxlan mcastgrp 203.0.113.109
net add vxlan vx-4001 bridge access 4001
net add vxlan vx-4001 vxlan mcastgrp 203.0.13.29
net add vxlan vx-4002 bridge access 4002
net add vxlan vx-4002 vxlan mcastgrp 203.0.13.30
net add vxlan vx-4003 bridge access 4003
net add vxlan vx-4003 vxlan mcastgrp 203.0.13.31
net add dot1x radius accounting-port 1813
net add dot1x eap-reauth-period 0
net add dot1x default-dacl-preauth-filename default_preauth_dacl.rules
net add dot1x radius authentication-port 1812
net add dot1x mab-activation-delay 30
net commit

# There are some configuration commands that are not yet supported by nclu.
# The following will append those commands to the appropriate files.
# ========================================================================
sudo sh -c "printf 'debug zebra mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh es\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh mac\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh neigh\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh nh\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'ip forwarding\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim vxlan\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim nht\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug zebra kernel\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug zebra events\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug bgp updates\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim events\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim zebra\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim packets register\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim packets joins\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim vxlan\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim nht\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim trace\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug mroute\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug mroute detail\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug zebra mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug msdp events\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'evpn mh startup-delay 30\n  interface swp1\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'evpn mh startup-delay 30\n  evpn mh uplink\n' >> /etc/frr/frr.conf"
net add bond hostbond1-4 bond lacp-rate 1
net add bond hostbond1-3 es-sys-mac 44:38:39:ff:ff:01
```

**vtysh Commands**



{{</tab>}}

{{<tab "leaf03">}}

**NCLU Commands**

```
cumulus@leaf03:~$ net show configuration commands
net del all
net add dns nameserver ipv4 192.168.0.3 vrf mgmt
net add time ntp server 0.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 1.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 2.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 3.cumulusnetworks.pool.ntp.org iburst
net add time ntp source eth0
net add snmp-server listening-address localhost
net add bgp autonomous-system 5558
net add interface swp2-4 evpn mh uplink
net add interface lo,swp1-4 pim sm
net add bond hostbond1-3 evpn mh es-sys-mac 44:38:39:ff:ff:01
net add bond hostbond1 evpn mh es-id 1
net add bond hostbond2 evpn mh es-id 2
net add bond hostbond3 evpn mh es-id 3
net add interface lo igmp
net add routing password cn321
net add routing enable password cn321
net add routing log timestamp precision 6
net add routing log file /var/log/frr/zebra.log
net add routing zebra debug vxlan
net add routing zebra debug kernel
net add routing zebra debug events
net add routing mroute debug
net add routing mroute debug detail
net add routing log file /var/log/frr/bgpd.log
net add routing line vty exec-timeout 0 0
net add bgp debug zebra
net add bgp debug updates
net add vrf vrf1 vni 4001
net add vrf vrf2 vni 4002
net add vrf vrf3 vni 4003
net add pim debug events
net add pim debug zebra
net add pim debug packets register
net add pim debug packets joins
net add pim debug trace
net add msdp debug events
net add pim rp 192.0.2.5 203.0.113.0/24
net add pim spt-switchover infinity-and-beyond
net add bgp debug evpn mh es
net add bgp debug evpn mh route
net add bgp bestpath as-path multipath-relax
net add bgp router-id 172.16.0.23
net add bgp neighbor swp1 interface v6only remote-as external
net add bgp neighbor swp2 interface v6only remote-as external
net add bgp neighbor swp3 interface v6only remote-as external
net add bgp neighbor swp4 interface v6only remote-as external
net add bgp ipv4 unicast redistribute connected
net add bgp ipv6 unicast redistribute connected
net add bgp ipv6 unicast neighbor swp1 activate
net add bgp ipv6 unicast neighbor swp2 activate
net add bgp ipv6 unicast neighbor swp3 activate
net add bgp ipv6 unicast neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  advertise-all-vni
net add bgp l2vpn evpn  advertise-svi-ip
net add time zone Etc/UTC
net add ptp global slave-only no
net add ptp global priority1 255
net add ptp global priority2 255
net add ptp global domain-number 0
net add ptp global logging-level 5
net add ptp global path-trace-enabled no
net add ptp global use-syslog yes
net add ptp global verbose no
net add ptp global summary-interval 0
net add ptp global time-stamping
net add bond hostbond1 bond slaves swp5
net add bond hostbond2 bond slaves swp6
net add bond hostbond3 bond slaves swp7
net add bond hostbond4 bond slaves swp8
net add vxlan vx-1000 vxlan id 1000
net add vxlan vx-1001 vxlan id 1001
net add vxlan vx-1002 vxlan id 1002
net add vxlan vx-1003 vxlan id 1003
net add vxlan vx-1004 vxlan id 1004
net add vxlan vx-1005 vxlan id 1005
net add vxlan vx-1006 vxlan id 1006
net add vxlan vx-1007 vxlan id 1007
net add vxlan vx-1008 vxlan id 1008
net add vxlan vx-1009 vxlan id 1009
net add vxlan vx-4001 vxlan id 4001
net add vxlan vx-4002 vxlan id 4002
net add vxlan vx-4003 vxlan id 4003
net add bond hostbond1 alias Local Node/s leaf03 and Ports swp5 <==> Remote Node/s host01 and Ports swp3
net add bond hostbond1,4 bridge pvid 1000
net add bond hostbond1-4 bond mode 802.3ad
net add bond hostbond1-4 mtu 9152
net add bond hostbond2 alias Local Node/s leaf03 and Ports swp6 <==> Remote Node/s host02 and Ports swp3
net add bond hostbond2 bridge pvid 1001
net add bond hostbond3 alias Local Node/s leaf03 and Ports swp7 <==> Remote Node/s hostd-13 and Ports swp3
net add bond hostbond3 bridge pvid 1002
net add bond hostbond4 alias Local Node/s leaf03 and Ports swp8 <==> Remote Node/s hosts-m3-14 and Ports swp1
net add bridge bridge ports vx-1000,vx-1001,vx-1002,vx-1003,vx-1004,vx-1005,vx-1006,vx-1007,vx-1008,vx-1009,vx-4001,vx-4002,vx-4003,hostbond4,hostbond1,hostbond2,hostbond3
net add bridge bridge pvid 1
net add bridge bridge vids 1000-1009
net add bridge bridge vlan-aware
net add interface eth0 ip address 192.168.0.15/24
net add interface eth0 ip gateway 192.168.0.2
net add interface eth0 vrf mgmt
net add interface swp1 alias Local Node leaf03 and Ports swp1 <==> Remote Node/s spine01 and Ports swp5
net add interface swp1-4 mtu 9202
net add interface swp1-8 link speed 10000
net add interface swp2 alias Local Node leaf03 and Ports swp2 <==> Remote Node/s spine01 and Ports swp6
net add interface swp3 alias Local Node leaf03 and Ports swp3 <==> Remote Node/s spine02 and Ports swp5
net add interface swp4 alias Local Node leaf03 and Ports swp4 <==> Remote Node/s spine02 and Ports swp6
net add loopback lo alias BGP un-numbered Use for Vxlan Src Tunnel
net add loopback lo ip address 172.16.0.23/32
net add vlan 1000 ip address 172.20.0.16/24
net add vlan 1000 ip address-virtual 00:00:5e:00:01:01 172.20.0.1/24
net add vlan 1000 ipv6 address 2001:db8::10/64
net add vlan 1000 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8::1/64
net add vlan 1000 vlan-id 1000
net add vlan 1000 vlan-raw-device bridge
net add vlan 1000 vrf vrf1
net add vlan 1001 ip address 172.20.1.16/24
net add vlan 1001 ip address-virtual 00:00:5e:00:01:01 172.20.1.1/24
net add vlan 1001 ipv6 address 2001:db8:0:1::10/64
net add vlan 1001 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:1::1/64
net add vlan 1001 vlan-id 1001
net add vlan 1001 vlan-raw-device bridge
net add vlan 1001 vrf vrf1
net add vlan 1002 ip address 172.20.2.16/24
net add vlan 1002 ip address-virtual 00:00:5e:00:01:01 172.20.2.1/24
net add vlan 1002 ipv6 address 2001:db8:0:2::10/64
net add vlan 1002 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:2::1/64
net add vlan 1002 vlan-id 1002
net add vlan 1002 vlan-raw-device bridge
net add vlan 1002 vrf vrf1
net add vlan 1003 ip address 172.20.3.16/24
net add vlan 1003 ip address-virtual 00:00:5e:00:01:01 172.20.3.1/24
net add vlan 1003 ipv6 address 2001:db8:0:3::10/64
net add vlan 1003 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:3::1/64
net add vlan 1003 vlan-id 1003
net add vlan 1003 vlan-raw-device bridge
net add vlan 1003 vrf vrf1
net add vlan 1004 ip address 172.20.4.16/24
net add vlan 1004 ip address-virtual 00:00:5e:00:01:01 172.20.4.1/24
net add vlan 1004 ipv6 address 2001:db8:0:4::10/64
net add vlan 1004 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:4::1/64
net add vlan 1004 vlan-id 1004
net add vlan 1004 vlan-raw-device bridge
net add vlan 1004 vrf vrf2
net add vlan 1005 ip address 172.20.5.16/24
net add vlan 1005 ip address-virtual 00:00:5e:00:01:01 172.20.5.1/24
net add vlan 1005 ipv6 address 2001:db8:0:5::10/64
net add vlan 1005 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:5::1/64
net add vlan 1005 vlan-id 1005
net add vlan 1005 vlan-raw-device bridge
net add vlan 1005 vrf vrf2
net add vlan 1006 ip address 172.20.6.16/24
net add vlan 1006 ip address-virtual 00:00:5e:00:01:01 172.20.6.1/24
net add vlan 1006 ipv6 address 2001:db8:0:6::10/64
net add vlan 1006 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:6::1/64
net add vlan 1006 vlan-id 1006
net add vlan 1006 vlan-raw-device bridge
net add vlan 1006 vrf vrf2
net add vlan 1007 ip address 172.20.7.16/24
net add vlan 1007 ip address-virtual 00:00:5e:00:01:01 172.20.7.1/24
net add vlan 1007 ipv6 address 2001:db8:0:7::10/64
net add vlan 1007 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:7::1/64
net add vlan 1007 vlan-id 1007
net add vlan 1007 vlan-raw-device bridge
net add vlan 1007 vrf vrf2
net add vlan 1008 ip address 172.20.8.16/24
net add vlan 1008 ip address-virtual 00:00:5e:00:01:01 172.20.8.1/24
net add vlan 1008 ipv6 address 2001:db8:0:8::10/64
net add vlan 1008 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:8::1/64
net add vlan 1008 vlan-id 1008
net add vlan 1008 vlan-raw-device bridge
net add vlan 1008 vrf vrf3
net add vlan 1009 ip address 172.20.9.16/24
net add vlan 1009 ip address-virtual 00:00:5e:00:01:01 172.20.9.1/24
net add vlan 1009 ipv6 address 2001:db8:0:9::10/64
net add vlan 1009 ipv6 address-virtual 00:00:5e:00:01:01 2001:db8:0:9::1/64
net add vlan 1009 vlan-id 1009
net add vlan 1009 vlan-raw-device bridge
net add vlan 1009 vrf vrf3
net add vlan 4001 vlan-id 4001
net add vlan 4001 vlan-raw-device bridge
net add vlan 4001 vrf vrf1
net add vlan 4002 vlan-id 4002
net add vlan 4002 vlan-raw-device bridge
net add vlan 4002 vrf vrf2
net add vlan 4003 vlan-id 4003
net add vlan 4003 vlan-raw-device bridge
net add vlan 4003 vrf vrf3
net add vrf mgmt ip address 172.16.0.1/8
net add vrf mgmt ipv6 address ::1/128
net add vrf mgmt,vrf1-3 vrf-table auto
net add vxlan vx-1000 bridge access 1000
net add vxlan vx-1000 vxlan mcastgrp 203.0.113.100
net add vxlan vx-1000-1009,4001-4003 bridge arp-nd-suppress on
net add vxlan vx-1000-1009,4001-4003 bridge learning off
net add vxlan vx-1000-1009,4001-4003 mtu 9152
net add vxlan vx-1000-1009,4001-4003 stp bpduguard
net add vxlan vx-1000-1009,4001-4003 stp portbpdufilter
net add vxlan vx-1000-1009,4001-4003 vxlan local-tunnelip 172.16.0.23
net add vxlan vx-1001 bridge access 1001
net add vxlan vx-1001 vxlan mcastgrp 203.0.113.101
net add vxlan vx-1002 bridge access 1002
net add vxlan vx-1002 vxlan mcastgrp 203.0.113.102
net add vxlan vx-1003 bridge access 1003
net add vxlan vx-1003 vxlan mcastgrp 203.0.113.103
net add vxlan vx-1004 bridge access 1004
net add vxlan vx-1004 vxlan mcastgrp 203.0.113.104
net add vxlan vx-1005 bridge access 1005
net add vxlan vx-1005 vxlan mcastgrp 203.0.113.105
net add vxlan vx-1006 bridge access 1006
net add vxlan vx-1006 vxlan mcastgrp 203.0.113.106
net add vxlan vx-1007 bridge access 1007
net add vxlan vx-1007 vxlan mcastgrp 203.0.113.107
net add vxlan vx-1008 bridge access 1008
net add vxlan vx-1008 vxlan mcastgrp 203.0.113.108
net add vxlan vx-1009 bridge access 1009
net add vxlan vx-1009 vxlan mcastgrp 203.0.113.109
net add vxlan vx-4001 bridge access 4001
net add vxlan vx-4001 vxlan mcastgrp 203.0.13.29
net add vxlan vx-4002 bridge access 4002
net add vxlan vx-4002 vxlan mcastgrp 203.0.13.30
net add vxlan vx-4003 bridge access 4003
net add vxlan vx-4003 vxlan mcastgrp 203.0.13.31
net add dot1x radius accounting-port 1813
net add dot1x eap-reauth-period 0
net add dot1x default-dacl-preauth-filename default_preauth_dacl.rules
net add dot1x radius authentication-port 1812
net add dot1x mab-activation-delay 30
net commit

# There are some configuration commands that are not yet supported by nclu.
# The following will append those commands to the appropriate files.
# ========================================================================
sudo sh -c "printf 'debug zebra mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh es\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh mac\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh neigh\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug zebra evpn mh nh\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'ip forwarding\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim vxlan\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim nht\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug zebra kernel\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug zebra events\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug bgp updates\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim events\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim zebra\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim packets register\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim packets joins\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim vxlan\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim nht\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug pim trace\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug mroute\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug mroute detail\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug zebra mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'no debug msdp events\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'evpn mh startup-delay 30\n  interface swp1\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'evpn mh startup-delay 30\n  evpn mh uplink\n' >> /etc/frr/frr.conf"
net add bond hostbond1-4 bond lacp-rate 1
net add bond hostbond1-3 es-sys-mac 44:38:39:ff:ff:01
cumulus@leaf03:~$
```

**vtysh Commands**

{{</tab>}}

{{<tab "spine01">}}

**NCLU Commands**

```
cumulus@spine01:~$ net show configuration commands
net del all
net add dns nameserver ipv4 192.168.0.3 vrf mgmt
net add time ntp server 0.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 1.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 2.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 3.cumulusnetworks.pool.ntp.org iburst
net add time ntp source eth0
net add snmp-server listening-address localhost
net add bgp autonomous-system 4435
net add interface lo,swp1-16 pim sm
net add routing password cn321
net add routing enable password cn321
net add routing log timestamp precision 6
net add routing log file /var/log/frr/zebra.log
net add routing zebra debug vxlan
net add routing zebra debug kernel
net add routing zebra debug events
net add routing mroute debug
net add routing mroute debug detail
net add routing log file /var/log/frr/bgpd.log
net add routing line vty exec-timeout 0 0
net add bgp debug zebra
net add bgp debug updates
net add vrf vrf1 vni 4001
net add vrf vrf2 vni 4002
net add vrf vrf3 vni 4003
net add pim debug events
net add pim debug zebra
net add pim debug packets register
net add pim debug packets joins
net add pim debug trace
net add msdp debug events
net add pim rp 192.0.2.5 203.0.113.0/24
net add pim spt-switchover infinity-and-beyond
net add bgp bestpath as-path multipath-relax
net add bgp router-id 172.16.0.17
net add bgp neighbor swp1 interface v6only remote-as external
net add bgp neighbor swp2 interface v6only remote-as external
net add bgp neighbor swp3 interface v6only remote-as external
net add bgp neighbor swp4 interface v6only remote-as external
net add bgp neighbor swp5 interface v6only remote-as external
net add bgp neighbor swp6 interface v6only remote-as external
net add bgp neighbor swp7 interface v6only remote-as external
net add bgp neighbor swp8 interface v6only remote-as external
net add bgp neighbor swp9 interface v6only remote-as external
net add bgp neighbor swp10 interface v6only remote-as external
net add bgp neighbor swp11 interface v6only remote-as external
net add bgp neighbor swp12 interface v6only remote-as external
net add bgp neighbor swp13 interface v6only remote-as external
net add bgp neighbor swp14 interface v6only remote-as external
net add bgp neighbor swp15 interface v6only remote-as external
net add bgp neighbor swp16 interface v6only remote-as external
net add bgp ipv4 unicast redistribute connected
net add bgp ipv4 unicast neighbor swp1 allowas-in origin
net add bgp ipv4 unicast neighbor swp2 allowas-in origin
net add bgp ipv4 unicast neighbor swp3 allowas-in origin
net add bgp ipv4 unicast neighbor swp4 allowas-in origin
net add bgp ipv4 unicast neighbor swp5 allowas-in origin
net add bgp ipv4 unicast neighbor swp6 allowas-in origin
net add bgp ipv4 unicast neighbor swp7 allowas-in origin
net add bgp ipv4 unicast neighbor swp8 allowas-in origin
net add bgp ipv4 unicast neighbor swp9 allowas-in origin
net add bgp ipv4 unicast neighbor swp10 allowas-in origin
net add bgp ipv4 unicast neighbor swp11 allowas-in origin
net add bgp ipv4 unicast neighbor swp12 allowas-in origin
net add bgp ipv4 unicast neighbor swp13 allowas-in origin
net add bgp ipv4 unicast neighbor swp14 allowas-in origin
net add bgp ipv4 unicast neighbor swp15 allowas-in origin
net add bgp ipv4 unicast neighbor swp16 allowas-in origin
net add bgp ipv6 unicast redistribute connected
net add bgp ipv6 unicast neighbor swp1 activate
net add bgp ipv6 unicast neighbor swp2 activate
net add bgp ipv6 unicast neighbor swp3 activate
net add bgp ipv6 unicast neighbor swp4 activate
net add bgp ipv6 unicast neighbor swp5 activate
net add bgp ipv6 unicast neighbor swp6 activate
net add bgp ipv6 unicast neighbor swp7 activate
net add bgp ipv6 unicast neighbor swp8 activate
net add bgp ipv6 unicast neighbor swp9 activate
net add bgp ipv6 unicast neighbor swp10 activate
net add bgp ipv6 unicast neighbor swp11 activate
net add bgp ipv6 unicast neighbor swp12 activate
net add bgp ipv6 unicast neighbor swp13 activate
net add bgp ipv6 unicast neighbor swp14 activate
net add bgp ipv6 unicast neighbor swp15 activate
net add bgp ipv6 unicast neighbor swp16 activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp5 activate
net add bgp l2vpn evpn  neighbor swp6 activate
net add bgp l2vpn evpn  neighbor swp7 activate
net add bgp l2vpn evpn  neighbor swp8 activate
net add bgp l2vpn evpn  neighbor swp9 activate
net add bgp l2vpn evpn  neighbor swp10 activate
net add bgp l2vpn evpn  neighbor swp11 activate
net add bgp l2vpn evpn  neighbor swp12 activate
net add bgp l2vpn evpn  neighbor swp13 activate
net add bgp l2vpn evpn  neighbor swp14 activate
net add bgp l2vpn evpn  neighbor swp15 activate
net add bgp l2vpn evpn  neighbor swp16 activate
net add time zone Etc/UTC
net add ptp global slave-only no
net add ptp global priority1 255
net add ptp global priority2 255
net add ptp global domain-number 0
net add ptp global logging-level 5
net add ptp global path-trace-enabled no
net add ptp global use-syslog yes
net add ptp global verbose no
net add ptp global summary-interval 0
net add ptp global time-stamping
net add interface eth0 ip address 192.168.0.15/24
net add interface eth0 ip gateway 192.168.0.2
net add interface eth0 vrf mgmt
net add interface swp1 alias Local Node spine01 and Ports swp1 <==> Remote Node/s leaf01 and Ports swp1
net add interface swp1-16 link speed 10000
net add interface swp1-16 mtu 9202
net add interface swp10 alias Local Node spine01 and Ports swp10 <==> Remote Node/s torm-22 and Ports swp2
net add interface swp11 alias Local Node spine01 and Ports swp11 <==> Remote Node/s torm-23 and Ports swp1
net add interface swp12 alias Local Node spine01 and Ports swp12 <==> Remote Node/s torm-23 and Ports swp2
net add interface swp13 alias Local Node spine01 and Ports swp13 <==> Remote Node/s tor-1 and Ports swp1
net add interface swp14 alias Local Node spine01 and Ports swp14 <==> Remote Node/s tor-1 and Ports swp2
net add interface swp15 alias Local Node spine01 and Ports swp15 <==> Remote Node/s tor-2 and Ports swp1
net add interface swp16 alias Local Node spine01 and Ports swp16 <==> Remote Node/s tor-2 and Ports swp2
net add interface swp2 alias Local Node spine01 and Ports swp2 <==> Remote Node/s leaf01 and Ports swp2
net add interface swp3 alias Local Node spine01 and Ports swp3 <==> Remote Node/s leaf02 and Ports swp1
net add interface swp4 alias Local Node spine01 and Ports swp4 <==> Remote Node/s leaf02 and Ports swp2
net add interface swp5 alias Local Node spine01 and Ports swp5 <==> Remote Node/s leaf03 and Ports swp1
net add interface swp6 alias Local Node spine01 and Ports swp6 <==> Remote Node/s leaf03 and Ports swp2
net add interface swp7 alias Local Node spine01 and Ports swp7 <==> Remote Node/s torm-21 and Ports swp1
net add interface swp8 alias Local Node spine01 and Ports swp8 <==> Remote Node/s torm-21 and Ports swp2
net add interface swp9 alias Local Node spine01 and Ports swp9 <==> Remote Node/s torm-22 and Ports swp1
net add loopback lo alias BGP un-numbered Use for Vxlan Src Tunnel
net add loopback lo ip address 172.16.0.17/32
net add vrf mgmt ip address 172.16.0.1/8
net add vrf mgmt ipv6 address ::1/128
net add vrf mgmt vrf-table auto
net add dot1x radius accounting-port 1813
net add dot1x eap-reauth-period 0
net add dot1x default-dacl-preauth-filename default_preauth_dacl.rules
net add dot1x radius authentication-port 1812
net add dot1x mab-activation-delay 30
net commit

# There are some configuration commands that are not yet supported by nclu.
# The following will append those commands to the appropriate files.
# ========================================================================
sudo sh -c "printf 'debug zebra mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'ip forwarding\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim vxlan\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim nht\n' >> /etc/frr/frr.conf"
cumulus@spine01:~$
```

**vtysh Commands**

{{</tab>}}

{{<tab "spine02">}}

**NCLU Commands**

```
cumulus@spine02:~$ net show configuration commands
net del all
net add dns nameserver ipv4 192.168.0.3 vrf mgmt
net add time ntp server 0.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 1.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 2.cumulusnetworks.pool.ntp.org iburst
net add time ntp server 3.cumulusnetworks.pool.ntp.org iburst
net add time ntp source eth0
net add snmp-server listening-address localhost
net add bgp autonomous-system 4435
net add interface lo,swp1-16 pim sm
net add routing password cn321
net add routing enable password cn321
net add routing log timestamp precision 6
net add routing log file /var/log/frr/zebra.log
net add routing zebra debug vxlan
net add routing zebra debug kernel
net add routing zebra debug events
net add routing mroute debug
net add routing mroute debug detail
net add routing log file /var/log/frr/bgpd.log
net add routing line vty exec-timeout 0 0
net add bgp debug zebra
net add bgp debug updates
net add vrf vrf1 vni 4001
net add vrf vrf2 vni 4002
net add vrf vrf3 vni 4003
net add pim debug events
net add pim debug zebra
net add pim debug packets register
net add pim debug packets joins
net add pim debug trace
net add msdp debug events
net add pim rp 192.0.2.5 203.0.113.0/24
net add pim spt-switchover infinity-and-beyond
net add bgp bestpath as-path multipath-relax
net add bgp router-id 172.16.0.18
net add bgp neighbor swp1 interface v6only remote-as external
net add bgp neighbor swp2 interface v6only remote-as external
net add bgp neighbor swp3 interface v6only remote-as external
net add bgp neighbor swp4 interface v6only remote-as external
net add bgp neighbor swp5 interface v6only remote-as external
net add bgp neighbor swp6 interface v6only remote-as external
net add bgp neighbor swp7 interface v6only remote-as external
net add bgp neighbor swp8 interface v6only remote-as external
net add bgp neighbor swp9 interface v6only remote-as external
net add bgp neighbor swp10 interface v6only remote-as external
net add bgp neighbor swp11 interface v6only remote-as external
net add bgp neighbor swp12 interface v6only remote-as external
net add bgp neighbor swp13 interface v6only remote-as external
net add bgp neighbor swp14 interface v6only remote-as external
net add bgp neighbor swp15 interface v6only remote-as external
net add bgp neighbor swp16 interface v6only remote-as external
net add bgp ipv4 unicast redistribute connected
net add bgp ipv4 unicast neighbor swp1 allowas-in origin
net add bgp ipv4 unicast neighbor swp2 allowas-in origin
net add bgp ipv4 unicast neighbor swp3 allowas-in origin
net add bgp ipv4 unicast neighbor swp4 allowas-in origin
net add bgp ipv4 unicast neighbor swp5 allowas-in origin
net add bgp ipv4 unicast neighbor swp6 allowas-in origin
net add bgp ipv4 unicast neighbor swp7 allowas-in origin
net add bgp ipv4 unicast neighbor swp8 allowas-in origin
net add bgp ipv4 unicast neighbor swp9 allowas-in origin
net add bgp ipv4 unicast neighbor swp10 allowas-in origin
net add bgp ipv4 unicast neighbor swp11 allowas-in origin
net add bgp ipv4 unicast neighbor swp12 allowas-in origin
net add bgp ipv4 unicast neighbor swp13 allowas-in origin
net add bgp ipv4 unicast neighbor swp14 allowas-in origin
net add bgp ipv4 unicast neighbor swp15 allowas-in origin
net add bgp ipv4 unicast neighbor swp16 allowas-in origin
net add bgp ipv6 unicast redistribute connected
net add bgp ipv6 unicast neighbor swp1 activate
net add bgp ipv6 unicast neighbor swp2 activate
net add bgp ipv6 unicast neighbor swp3 activate
net add bgp ipv6 unicast neighbor swp4 activate
net add bgp ipv6 unicast neighbor swp5 activate
net add bgp ipv6 unicast neighbor swp6 activate
net add bgp ipv6 unicast neighbor swp7 activate
net add bgp ipv6 unicast neighbor swp8 activate
net add bgp ipv6 unicast neighbor swp9 activate
net add bgp ipv6 unicast neighbor swp10 activate
net add bgp ipv6 unicast neighbor swp11 activate
net add bgp ipv6 unicast neighbor swp12 activate
net add bgp ipv6 unicast neighbor swp13 activate
net add bgp ipv6 unicast neighbor swp14 activate
net add bgp ipv6 unicast neighbor swp15 activate
net add bgp ipv6 unicast neighbor swp16 activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp5 activate
net add bgp l2vpn evpn  neighbor swp6 activate
net add bgp l2vpn evpn  neighbor swp7 activate
net add bgp l2vpn evpn  neighbor swp8 activate
net add bgp l2vpn evpn  neighbor swp9 activate
net add bgp l2vpn evpn  neighbor swp10 activate
net add bgp l2vpn evpn  neighbor swp11 activate
net add bgp l2vpn evpn  neighbor swp12 activate
net add bgp l2vpn evpn  neighbor swp13 activate
net add bgp l2vpn evpn  neighbor swp14 activate
net add bgp l2vpn evpn  neighbor swp15 activate
net add bgp l2vpn evpn  neighbor swp16 activate
net add time zone Etc/UTC
net add ptp global slave-only no
net add ptp global priority1 255
net add ptp global priority2 255
net add ptp global domain-number 0
net add ptp global logging-level 5
net add ptp global path-trace-enabled no
net add ptp global use-syslog yes
net add ptp global verbose no
net add ptp global summary-interval 0
net add ptp global time-stamping
net add interface eth0 ip address 192.168.0.15/24
net add interface eth0 ip gateway 192.168.0.2
net add interface eth0 vrf mgmt
net add interface swp1 alias Local Node spine02 and Ports swp1 <==> Remote Node/s leaf01 and Ports swp3
net add interface swp1-16 link speed 10000
net add interface swp1-16 mtu 9202
net add interface swp10 alias Local Node spine02 and Ports swp10 <==> Remote Node/s torm-22 and Ports swp4
net add interface swp11 alias Local Node spine02 and Ports swp11 <==> Remote Node/s torm-23 and Ports swp3
net add interface swp12 alias Local Node spine02 and Ports swp12 <==> Remote Node/s torm-23 and Ports swp4
net add interface swp13 alias Local Node spine02 and Ports swp13 <==> Remote Node/s tor-1 and Ports swp3
net add interface swp14 alias Local Node spine02 and Ports swp14 <==> Remote Node/s tor-1 and Ports swp4
net add interface swp15 alias Local Node spine02 and Ports swp15 <==> Remote Node/s tor-2 and Ports swp3
net add interface swp16 alias Local Node spine02 and Ports swp16 <==> Remote Node/s tor-2 and Ports swp4
net add interface swp2 alias Local Node spine02 and Ports swp2 <==> Remote Node/s leaf01 and Ports swp4
net add interface swp3 alias Local Node spine02 and Ports swp3 <==> Remote Node/s leaf02 and Ports swp3
net add interface swp4 alias Local Node spine02 and Ports swp4 <==> Remote Node/s leaf02 and Ports swp4
net add interface swp5 alias Local Node spine02 and Ports swp5 <==> Remote Node/s leaf03 and Ports swp3
net add interface swp6 alias Local Node spine02 and Ports swp6 <==> Remote Node/s leaf03 and Ports swp4
net add interface swp7 alias Local Node spine02 and Ports swp7 <==> Remote Node/s torm-21 and Ports swp3
net add interface swp8 alias Local Node spine02 and Ports swp8 <==> Remote Node/s torm-21 and Ports swp4
net add interface swp9 alias Local Node spine02 and Ports swp9 <==> Remote Node/s torm-22 and Ports swp3
net add loopback lo alias BGP un-numbered Use for Vxlan Src Tunnel
net add loopback lo ip address 172.16.0.18/32
net add vrf mgmt ip address 172.16.0.1/8
net add vrf mgmt ipv6 address ::1/128
net add vrf mgmt vrf-table auto
net add dot1x radius accounting-port 1813
net add dot1x eap-reauth-period 0
net add dot1x default-dacl-preauth-filename default_preauth_dacl.rules
net add dot1x radius authentication-port 1812
net add dot1x mab-activation-delay 30
net commit

# There are some configuration commands that are not yet supported by nclu.
# The following will append those commands to the appropriate files.
# ========================================================================
sudo sh -c "printf 'debug zebra mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'ip forwarding\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim vxlan\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim mlag\n' >> /etc/frr/frr.conf"
sudo sh -c "printf 'debug pim nht\n' >> /etc/frr/frr.conf"
cumulus@spine02:~$
```

**vtysh Commands**


{{</tab>}}

{{</tabs>}}

### /etc/network/interfaces

If you are using the {{<link title="#Configuration Commands" text="NCLU commands">}} listed above, they create the following configurations in the `/etc/network/interfaces` files for the leaf and spine switches.

If you are not using NCLU and are configuring the topology on the command line, copy the configurations below to the appropriate switches or servers. For the leaf and spine switch configurations, reload the new configuration by running `ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

{{<tabs "/etc/network/interfaces">}}

{{<tab "leaf01">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
    vrf mgmt

#Enabling Mgmt VRF interface
auto mgmt
iface mgmt
    address 172.16.0.1/8
    address ::1/128
    vrf-table auto

auto lo
iface lo
    address 172.16.0.21/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf01 and Ports swp1 <==> Remote  Node/s spine01 and Ports swp1

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf01 and Ports swp2 <==> Remote  Node/s spine01 and Ports swp2

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf01 and Ports swp3 <==> Remote  Node/s spine02 and Ports swp1

auto swp4
iface swp4
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf01 and Ports swp4 <==> Remote  Node/s spine02 and Ports swp2

auto swp5
iface swp5
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp6
iface swp6
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp7
iface swp7
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp8
iface swp8
    link-speed 10000
    link-duplex full
    link-autoneg off

auto hostbond1
iface hostbond1
        bond-slaves swp5
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf01 and Ports swp5 <==> Remote  Node/s host01 and Ports swp1
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1000

auto hostbond2
iface hostbond2
        bond-slaves swp6
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf01 and Ports swp6 <==> Remote  Node/s host02 and Ports swp1
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1001

auto hostbond3
iface hostbond3
        bond-slaves swp7
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf01 and Ports swp7 <==> Remote  Node/s hostd-13 and Ports swp1
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1002

auto hostbond4
iface hostbond4
        bond-slaves swp8
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf01 and Ports swp8 <==> Remote  Node/s hosts-m1-14 and Ports swp1
    bridge-pvid 1000

auto vx-1000
iface vx-1000
    vxlan-id 1000
    bridge-access 1000
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.100
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1001
iface vx-1001
    vxlan-id 1001
    bridge-access 1001
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.101
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1002
iface vx-1002
    vxlan-id 1002
    bridge-access 1002
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.102
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1003
iface vx-1003
    vxlan-id 1003
    bridge-access 1003
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.103
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1004
iface vx-1004
    vxlan-id 1004
    bridge-access 1004
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.104
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1005
iface vx-1005
    vxlan-id 1005
    bridge-access 1005
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.105
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1006
iface vx-1006
    vxlan-id 1006
    bridge-access 1006
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.106
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1007
iface vx-1007
    vxlan-id 1007
    bridge-access 1007
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.107
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1008
iface vx-1008
    vxlan-id 1008
    bridge-access 1008
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.108
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1009
iface vx-1009
    vxlan-id 1009
    bridge-access 1009
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.109
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4001
iface vx-4001
    vxlan-id 4001
    bridge-access 4001
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.29
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4002
iface vx-4002
    vxlan-id 4002
    bridge-access 4002
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.30
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4003
iface vx-4003
    vxlan-id 4003
    bridge-access 4003
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.31
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-1000 vx-1001 vx-1002 vx-1003 vx-1004 vx-1005 vx-1006 vx-1007 vx-1008 vx-1009 vx-4001 vx-4002 vx-4003 hostbond4 hostbond1 hostbond2 hostbond3
    bridge-stp on
    bridge-vids 1000 1001 1002 1003 1004 1005 1006 1007 1008 1009
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 172.20.0.12/24
    address 2001:db8::c/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.0.1/24 2001:db8::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 172.20.1.12/24
    address 2001:db8:0:1::c/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.1.1/24 2001:db8:0:1::1/64
    vrf vrf1

auto vlan1002
iface vlan1002
    address 172.20.2.12/24
    address 2001:db8:0:2::c/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.2.1/24 2001:db8:0:2::1/64
    vrf vrf1

auto vlan1003
iface vlan1003
    address 172.20.3.12/24
    address 2001:db8:0:3::c/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.3.1/24 2001:db8:0:3::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1004
iface vlan1004
    address 172.20.4.12/24
    address 2001:db8:0:4::c/64
    vlan-id 1004
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.4.1/24 2001:db8:0:4::1/64
    vrf vrf2

auto vlan1005
iface vlan1005
    address 172.20.5.12/24
    address 2001:db8:0:5::c/64
    vlan-id 1005
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.5.1/24 2001:db8:0:5::1/64
    vrf vrf2

auto vlan1006
iface vlan1006
    address 172.20.6.12/24
    address 2001:db8:0:6::c/64
    vlan-id 1006
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.6.1/24 2001:db8:0:6::1/64
    vrf vrf2

auto vlan1007
iface vlan1007
    address 172.20.7.12/24
    address 2001:db8:0:7::c/64
    vlan-id 1007
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.7.1/24 2001:db8:0:7::1/64
    vrf vrf2

auto vrf3
iface vrf3
    vrf-table auto

auto vlan1008
iface vlan1008
    address 172.20.8.12/24
    address 2001:db8:0:8::c/64
    vlan-id 1008
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.8.1/24 2001:db8:0:8::1/64
    vrf vrf3

auto vlan1009
iface vlan1009
    address 172.20.9.12/24
    address 2001:db8:0:9::c/64
    vlan-id 1009
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.9.1/24 2001:db8:0:9::1/64
    vrf vrf3

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2

auto vlan4003
iface vlan4003
    vlan-id 4003
    vlan-raw-device bridge
    vrf vrf3
```

{{</tab>}}

{{<tab "leaf02">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
    vrf mgmt

#Enabling Mgmt VRF interface
auto mgmt
iface mgmt
    address 172.16.0.1/8
    address ::1/128
    vrf-table auto

auto lo
iface lo
    address 172.16.0.22/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf02 and Ports swp1 <==> Remote  Node/s spine01 and Ports swp3

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf02 and Ports swp2 <==> Remote  Node/s spine01 and Ports swp4

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf02 and Ports swp3 <==> Remote  Node/s spine02 and Ports swp3

auto swp4
iface swp4
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf02 and Ports swp4 <==> Remote  Node/s spine02 and Ports swp4

auto swp5
iface swp5
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp6
iface swp6
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp7
iface swp7
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp8
iface swp8
    link-speed 10000
    link-duplex full
    link-autoneg off

auto hostbond1
iface hostbond1
        bond-slaves swp5
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf02 and Ports swp5 <==> Remote  Node/s host01 and Ports swp2
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1000

auto hostbond2
iface hostbond2
        bond-slaves swp6
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf02 and Ports swp6 <==> Remote  Node/s host02 and Ports swp2
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1001

auto hostbond3
iface hostbond3
        bond-slaves swp7
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf02 and Ports swp7 <==> Remote  Node/s hostd-13 and Ports swp2
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1002

auto hostbond4
iface hostbond4
        bond-slaves swp8
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf02 and Ports swp8 <==> Remote  Node/s hosts-m2-14 and Ports swp1
    bridge-pvid 1000

auto vx-1000
iface vx-1000
    vxlan-id 1000
    bridge-access 1000
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.100
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1001
iface vx-1001
    vxlan-id 1001
    bridge-access 1001
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.101
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1002
iface vx-1002
    vxlan-id 1002
    bridge-access 1002
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.102
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1003
iface vx-1003
    vxlan-id 1003
    bridge-access 1003
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.103
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1004
iface vx-1004
    vxlan-id 1004
    bridge-access 1004
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.104
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1005
iface vx-1005
    vxlan-id 1005
    bridge-access 1005
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.105
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1006
iface vx-1006
    vxlan-id 1006
    bridge-access 1006
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.106
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1007
iface vx-1007
    vxlan-id 1007
    bridge-access 1007
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.107
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1008
iface vx-1008
    vxlan-id 1008
    bridge-access 1008
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.108
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1009
iface vx-1009
    vxlan-id 1009
    bridge-access 1009
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.109
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4001
iface vx-4001
    vxlan-id 4001
    bridge-access 4001
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.29
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4002
iface vx-4002
    vxlan-id 4002
    bridge-access 4002
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.30
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4003
iface vx-4003
    vxlan-id 4003
    bridge-access 4003
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.31
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-1000 vx-1001 vx-1002 vx-1003 vx-1004 vx-1005 vx-1006 vx-1007 vx-1008 vx-1009 vx-4001 vx-4002 vx-4003 hostbond4 hostbond1 hostbond2 hostbond3
    bridge-stp on
    bridge-vids 1000 1001 1002 1003 1004 1005 1006 1007 1008 1009
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 172.20.0.14/24
    address 2001:db8::e/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.0.1/24 2001:db8::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 172.20.1.14/24
    address 2001:db8:0:1::e/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.1.1/24 2001:db8:0:1::1/64
    vrf vrf1

auto vlan1002
iface vlan1002
    address 172.20.2.14/24
    address 2001:db8:0:2::e/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.2.1/24 2001:db8:0:2::1/64
    vrf vrf1

auto vlan1003
iface vlan1003
    address 172.20.3.14/24
    address 2001:db8:0:3::e/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.3.1/24 2001:db8:0:3::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1004
iface vlan1004
    address 172.20.4.14/24
    address 2001:db8:0:4::e/64
    vlan-id 1004
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.4.1/24 2001:db8:0:4::1/64
    vrf vrf2

auto vlan1005
iface vlan1005
    address 172.20.5.14/24
    address 2001:db8:0:5::e/64
    vlan-id 1005
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.5.1/24 2001:db8:0:5::1/64
    vrf vrf2

auto vlan1006
iface vlan1006
    address 172.20.6.14/24
    address 2001:db8:0:6::e/64
    vlan-id 1006
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.6.1/24 2001:db8:0:6::1/64
    vrf vrf2

auto vlan1007
iface vlan1007
    address 172.20.7.14/24
    address 2001:db8:0:7::e/64
    vlan-id 1007
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.7.1/24 2001:db8:0:7::1/64
    vrf vrf2

auto vrf3
iface vrf3
    vrf-table auto

auto vlan1008
iface vlan1008
    address 172.20.8.14/24
    address 2001:db8:0:8::e/64
    vlan-id 1008
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.8.1/24 2001:db8:0:8::1/64
    vrf vrf3

auto vlan1009
iface vlan1009
    address 172.20.9.14/24
    address 2001:db8:0:9::e/64
    vlan-id 1009
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.9.1/24 2001:db8:0:9::1/64
    vrf vrf3

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2

auto vlan4003
iface vlan4003
    vlan-id 4003
    vlan-raw-device bridge
    vrf vrf3
```

{{</tab>}}

{{<tab "leaf03">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
    vrf mgmt

#Enabling Mgmt VRF interface
auto mgmt
iface mgmt
    address 172.16.0.1/8
    address ::1/128
    vrf-table auto

auto lo
iface lo
    address 172.16.0.23/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf03 and Ports swp1 <==> Remote  Node/s spine01 and Ports swp5

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf03 and Ports swp2 <==> Remote  Node/s spine01 and Ports swp6

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf03 and Ports swp3 <==> Remote  Node/s spine02 and Ports swp5

auto swp4
iface swp4
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node leaf03 and Ports swp4 <==> Remote  Node/s spine02 and Ports swp6

auto swp5
iface swp5
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp6
iface swp6
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp7
iface swp7
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp8
iface swp8
    link-speed 10000
    link-duplex full
    link-autoneg off

auto hostbond1
iface hostbond1
        bond-slaves swp5
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf03 and Ports swp5 <==> Remote  Node/s host01 and Ports swp3
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1000

auto hostbond2
iface hostbond2
        bond-slaves swp6
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf03 and Ports swp6 <==> Remote  Node/s host02 and Ports swp3
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1001

auto hostbond3
iface hostbond3
        bond-slaves swp7
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf03 and Ports swp7 <==> Remote  Node/s hostd-13 and Ports swp3
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1002

auto hostbond4
iface hostbond4
        bond-slaves swp8
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s leaf03 and Ports swp8 <==> Remote  Node/s hosts-m3-14 and Ports swp1
    bridge-pvid 1000

auto vx-1000
iface vx-1000
    vxlan-id 1000
    bridge-access 1000
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.100
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1001
iface vx-1001
    vxlan-id 1001
    bridge-access 1001
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.101
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1002
iface vx-1002
    vxlan-id 1002
    bridge-access 1002
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.102
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1003
iface vx-1003
    vxlan-id 1003
    bridge-access 1003
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.103
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1004
iface vx-1004
    vxlan-id 1004
    bridge-access 1004
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.104
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1005
iface vx-1005
    vxlan-id 1005
    bridge-access 1005
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.105
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1006
iface vx-1006
    vxlan-id 1006
    bridge-access 1006
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.106
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1007
iface vx-1007
    vxlan-id 1007
    bridge-access 1007
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.107
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1008
iface vx-1008
    vxlan-id 1008
    bridge-access 1008
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.108
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-1009
iface vx-1009
    vxlan-id 1009
    bridge-access 1009
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.113.109
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4001
iface vx-4001
    vxlan-id 4001
    bridge-access 4001
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.29
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4002
iface vx-4002
    vxlan-id 4002
    bridge-access 4002
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.30
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto vx-4003
iface vx-4003
    vxlan-id 4003
    bridge-access 4003
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 203.0.13.31
         mstpctl-portbpdufilter yes
         mstpctl-bpduguard  yes
         mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-1000 vx-1001 vx-1002 vx-1003 vx-1004 vx-1005 vx-1006 vx-1007 vx-1008 vx-1009 vx-4001 vx-4002 vx-4003 hostbond4 hostbond1 hostbond2 hostbond3
    bridge-stp on
    bridge-vids 1000 1001 1002 1003 1004 1005 1006 1007 1008 1009
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 172.20.0.16/24
    address 2001:db8::10/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.0.1/24 2001:db8::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 172.20.1.16/24
    address 2001:db8:0:1::10/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.1.1/24 2001:db8:0:1::1/64
    vrf vrf1

auto vlan1002
iface vlan1002
    address 172.20.2.16/24
    address 2001:db8:0:2::10/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.2.1/24 2001:db8:0:2::1/64
    vrf vrf1

auto vlan1003
iface vlan1003
    address 172.20.3.16/24
    address 2001:db8:0:3::10/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.3.1/24 2001:db8:0:3::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1004
iface vlan1004
    address 172.20.4.16/24
    address 2001:db8:0:4::10/64
    vlan-id 1004
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.4.1/24 2001:db8:0:4::1/64
    vrf vrf2

auto vlan1005
iface vlan1005
    address 172.20.5.16/24
    address 2001:db8:0:5::10/64
    vlan-id 1005
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.5.1/24 2001:db8:0:5::1/64
    vrf vrf2

auto vlan1006
iface vlan1006
    address 172.20.6.16/24
    address 2001:db8:0:6::10/64
    vlan-id 1006
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.6.1/24 2001:db8:0:6::1/64
    vrf vrf2

auto vlan1007
iface vlan1007
    address 172.20.7.16/24
    address 2001:db8:0:7::10/64
    vlan-id 1007
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.7.1/24 2001:db8:0:7::1/64
    vrf vrf2

auto vrf3
iface vrf3
    vrf-table auto

auto vlan1008
iface vlan1008
    address 172.20.8.16/24
    address 2001:db8:0:8::10/64
    vlan-id 1008
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.8.1/24 2001:db8:0:8::1/64
    vrf vrf3

auto vlan1009
iface vlan1009
    address 172.20.9.16/24
    address 2001:db8:0:9::10/64
    vlan-id 1009
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.20.9.1/24 2001:db8:0:9::1/64
    vrf vrf3

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2

auto vlan4003
iface vlan4003
    vlan-id 4003
    vlan-raw-device bridge
    vrf vrf3

cumulus@leaf03:~$ 
```

{{</tab>}}

{{<tab "spine01">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
    vrf mgmt

#Enabling Mgmt VRF interface
auto mgmt
iface mgmt
    address 172.16.0.1/8
    address ::1/128
    vrf-table auto

auto lo
iface lo
    address 172.16.0.17/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp1 <==> Remote  Node/s leaf01 and Ports swp1

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp2 <==> Remote  Node/s leaf01 and Ports swp2

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp3 <==> Remote  Node/s leaf02 and Ports swp1

auto swp4
iface swp4
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp4 <==> Remote  Node/s leaf02 and Ports swp2

auto swp5
iface swp5
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp5 <==> Remote  Node/s leaf03 and Ports swp1

auto swp6
iface swp6
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp6 <==> Remote  Node/s leaf03 and Ports swp2

auto swp7
iface swp7
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp7 <==> Remote  Node/s torm-21 and Ports swp1

auto swp8
iface swp8
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp8 <==> Remote  Node/s torm-21 and Ports swp2

auto swp9
iface swp9
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp9 <==> Remote  Node/s torm-22 and Ports swp1

auto swp10
iface swp10
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp10 <==> Remote  Node/s torm-22 and Ports swp2

auto swp11
iface swp11
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp11 <==> Remote  Node/s torm-23 and Ports swp1

auto swp12
iface swp12
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp12 <==> Remote  Node/s torm-23 and Ports swp2

auto swp13
iface swp13
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp13 <==> Remote  Node/s tor-1 and Ports swp1

auto swp14
iface swp14
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp14 <==> Remote  Node/s tor-1 and Ports swp2

auto swp15
iface swp15
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp15 <==> Remote  Node/s tor-2 and Ports swp1

auto swp16
iface swp16
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine01 and Ports swp16 <==> Remote  Node/s tor-2 and Ports swp2

cumulus@spine01:~$
```

{{</tab>}}

{{<tab "spine02">}}

```
cumulus@spine02:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
    vrf mgmt

#Enabling Mgmt VRF interface
auto mgmt
iface mgmt
    address 172.16.0.1/8
    address ::1/128
    vrf-table auto

auto lo
iface lo
    address 172.16.0.18/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp1 <==> Remote  Node/s leaf01 and Ports swp3

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp2 <==> Remote  Node/s leaf01 and Ports swp4

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp3 <==> Remote  Node/s leaf02 and Ports swp3

auto swp4
iface swp4
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp4 <==> Remote  Node/s leaf02 and Ports swp4

auto swp5
iface swp5
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp5 <==> Remote  Node/s leaf03 and Ports swp3

auto swp6
iface swp6
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp6 <==> Remote  Node/s leaf03 and Ports swp4

auto swp7
iface swp7
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp7 <==> Remote  Node/s torm-21 and Ports swp3

auto swp8
iface swp8
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp8 <==> Remote  Node/s torm-21 and Ports swp4

auto swp9
iface swp9
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp9 <==> Remote  Node/s torm-22 and Ports swp3

auto swp10
iface swp10
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp10 <==> Remote  Node/s torm-22 and Ports swp4

auto swp11
iface swp11
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp11 <==> Remote  Node/s torm-23 and Ports swp3

auto swp12
iface swp12
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp12 <==> Remote  Node/s torm-23 and Ports swp4

auto swp13
iface swp13
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp13 <==> Remote  Node/s tor-1 and Ports swp3

auto swp14
iface swp14
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp14 <==> Remote  Node/s tor-1 and Ports swp4

auto swp15
iface swp15
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp15 <==> Remote  Node/s tor-2 and Ports swp3

auto swp16
iface swp16
    link-speed 10000
    link-duplex full
    link-autoneg off
        mtu  9202
    alias Local Node spine02 and Ports swp16 <==> Remote  Node/s tor-2 and Ports swp4

cumulus@spine02:~$
```

{{</tab>}}

{{<tab "host01">}}

```
cumulus@host01:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
    vrf mgmt

#Enabling Mgmt VRF interface
auto mgmt
iface mgmt
    address 172.16.0.1/8
    address ::1/128
    vrf-table auto

auto lo
iface lo inet loopback
auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off

auto torbond1
iface torbond1
    address 172.20.0.9/24
    address 2001:db8::9/64
        bond-slaves swp1 swp2 swp3
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s host01 and Ports swp1 swp2 swp3 <==> Remote  Node/s leaf01 leaf02 leaf03 and Ports swp5 swp5 swp5
    post-up ip route replace default via 172.20.0.1 dev torbond1
    post-up ip -6 route replace default via 2001:db8::1 dev torbond1

auto torbond1.1001
iface torbond1.1001
    address 172.20.1.9/24
    address 2001:db8:0:1::9/64
    alias Vni 1001
    vrf vrf1001
    gateway 172.20.1.1
    gateway 2001:db8:0:1::1

auto vrf1001
iface vrf1001
    vrf-table auto

auto torbond1.1002
iface torbond1.1002
    address 172.20.2.9/24
    address 2001:db8:0:2::9/64
    alias Vni 1002
    vrf vrf1002
    gateway 172.20.2.1
    gateway 2001:db8:0:2::1

auto vrf1002
iface vrf1002
    vrf-table auto

auto torbond1.1003
iface torbond1.1003
    address 172.20.3.9/24
    address 2001:db8:0:3::9/64
    alias Vni 1003
    vrf vrf1003
    gateway 172.20.3.1
    gateway 2001:db8:0:3::1

auto vrf1003
iface vrf1003
    vrf-table auto

auto torbond1.1004
iface torbond1.1004
    address 172.20.4.9/24
    address 2001:db8:0:4::9/64
    alias Vni 1004
    vrf vrf1004
    gateway 172.20.4.1
    gateway 2001:db8:0:4::1

auto vrf1004
iface vrf1004
    vrf-table auto

auto torbond1.1005
iface torbond1.1005
    address 172.20.5.9/24
    address 2001:db8:0:5::9/64
    alias Vni 1005
    vrf vrf1005
    gateway 172.20.5.1
    gateway 2001:db8:0:5::1

auto vrf1005
iface vrf1005
    vrf-table auto

auto torbond1.1006
iface torbond1.1006
    address 172.20.6.9/24
    address 2001:db8:0:6::9/64
    alias Vni 1006
    vrf vrf1006
    gateway 172.20.6.1
    gateway 2001:db8:0:6::1

auto vrf1006
iface vrf1006
    vrf-table auto

auto torbond1.1007
iface torbond1.1007
    address 172.20.7.9/24
    address 2001:db8:0:7::9/64
    alias Vni 1007
    vrf vrf1007
    gateway 172.20.7.1
    gateway 2001:db8:0:7::1

auto vrf1007
iface vrf1007
    vrf-table auto

auto torbond1.1008
iface torbond1.1008
    address 172.20.8.9/24
    address 2001:db8:0:8::9/64
    alias Vni 1008
    vrf vrf1008
    gateway 172.20.8.1
    gateway 2001:db8:0:8::1

auto vrf1008
iface vrf1008
    vrf-table auto

auto torbond1.1009
iface torbond1.1009
    address 172.20.9.9/24
    address 2001:db8:0:9::9/64
    alias Vni 1009
    vrf vrf1009
    gateway 172.20.9.1
    gateway 2001:db8:0:9::1

auto vrf1009
iface vrf1009
    vrf-table auto

cumulus@host01:~$
```

{{</tab>}}

{{<tab "host02">}}

```
cumulus@host02:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
    vrf mgmt

#Enabling Mgmt VRF interface
auto mgmt
iface mgmt
    address 172.16.0.1/8
    address ::1/128
    vrf-table auto

auto lo
iface lo inet loopback
auto swp1
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp2
iface swp2
    link-speed 10000
    link-duplex full
    link-autoneg off

auto swp3
iface swp3
    link-speed 10000
    link-duplex full
    link-autoneg off

auto torbond1
iface torbond1
    address 172.20.1.10/24
    address 2001:db8:0:1::a/64
        bond-slaves swp1 swp2 swp3
        bond-mode 802.3ad
        bond-min-links 1
        bond-lacp-rate 1
        mtu  9152
    alias Local Node/s host02 and Ports swp1 swp2 swp3 <==> Remote  Node/s leaf01 leaf02 leaf03 and Ports swp6 swp6 swp6
    post-up ip route replace default via 172.20.1.1 dev torbond1
    post-up ip -6 route replace default via 2001:db8:0:1::1 dev torbond1

auto torbond1.1000
iface torbond1.1000
    address 172.20.0.10/24
    address 2001:db8::a/64
    alias Vni 1000
    vrf vrf1000
    gateway 172.20.0.1
    gateway 2001:db8::1

auto vrf1000
iface vrf1000
    vrf-table auto

auto torbond1.1002
iface torbond1.1002
    address 172.20.2.10/24
    address 2001:db8:0:2::a/64
    alias Vni 1002
    vrf vrf1002
    gateway 172.20.2.1
    gateway 2001:db8:0:2::1

auto vrf1002
iface vrf1002
    vrf-table auto

auto torbond1.1003
iface torbond1.1003
    address 172.20.3.10/24
    address 2001:db8:0:3::a/64
    alias Vni 1003
    vrf vrf1003
    gateway 172.20.3.1
    gateway 2001:db8:0:3::1

auto vrf1003
iface vrf1003
    vrf-table auto

auto torbond1.1004
iface torbond1.1004
    address 172.20.4.10/24
    address 2001:db8:0:4::a/64
    alias Vni 1004
    vrf vrf1004
    gateway 172.20.4.1
    gateway 2001:db8:0:4::1

auto vrf1004
iface vrf1004
    vrf-table auto

auto torbond1.1005
iface torbond1.1005
    address 172.20.5.10/24
    address 2001:db8:0:5::a/64
    alias Vni 1005
    vrf vrf1005
    gateway 172.20.5.1
    gateway 2001:db8:0:5::1

auto vrf1005
iface vrf1005
    vrf-table auto

auto torbond1.1006
iface torbond1.1006
    address 172.20.6.10/24
    address 2001:db8:0:6::a/64
    alias Vni 1006
    vrf vrf1006
    gateway 172.20.6.1
    gateway 2001:db8:0:6::1

auto vrf1006
iface vrf1006
    vrf-table auto

auto torbond1.1007
iface torbond1.1007
    address 172.20.7.10/24
    address 2001:db8:0:7::a/64
    alias Vni 1007
    vrf vrf1007
    gateway 172.20.7.1
    gateway 2001:db8:0:7::1

auto vrf1007
iface vrf1007
    vrf-table auto

auto torbond1.1008
iface torbond1.1008
    address 172.20.8.10/24
    address 2001:db8:0:8::a/64
    alias Vni 1008
    vrf vrf1008
    gateway 172.20.8.1
    gateway 2001:db8:0:8::1

auto vrf1008
iface vrf1008
    vrf-table auto

auto torbond1.1009
iface torbond1.1009
    address 172.20.9.10/24
    address 2001:db8:0:9::a/64
    alias Vni 1009
    vrf vrf1009
    gateway 172.20.9.1
    gateway 2001:db8:0:9::1

auto vrf1009
iface vrf1009
    vrf-table auto

cumulus@host02:~$
```

{{</tab>}}

{{</tabs>}}

### /etc/frr/frr.conf

These `vtysh` commands create the following configuration in the `/etc/frr/frr.conf` file:

{{<tabs "frr.conf Files">}}

{{<tab "leaf01">}}

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf
frr version 7.4+cl4u1
frr defaults datacenter
hostname leaf01
log file /var/log/frr/bgpd.log
log timestamp precision 6
evpn mh startup-delay 30
zebra nexthop proto only
ip pim rp 192.0.2.5 203.0.113.0/24
ip pim spt-switchover infinity-and-beyond
service integrated-vtysh-config
!
debug bgp evpn mh es
debug bgp evpn mh route
debug bgp zebra
debug zebra evpn mh es
debug zebra evpn mh mac
debug zebra evpn mh neigh
debug zebra evpn mh nh
debug zebra vxlan
!
enable password cn321
password cn321
!
vrf vrf1
 vni 4001
 exit-vrf
!
vrf vrf2
 vni 4002
 exit-vrf
!
vrf vrf3
 vni 4003
 exit-vrf
!
interface hostbond1
 evpn mh es-df-pref 50000
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond2
 evpn mh es-df-pref 50000
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond3
 evpn mh es-df-pref 50000
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface ipmr-lo
 ip pim
!
interface lo
 ip igmp
 ip pim
!
interface swp1
 evpn mh uplink
 ip pim
!
interface swp2
 evpn mh uplink
 ip pim
!
interface swp3
 evpn mh uplink
 ip pim
!
interface swp4
 evpn mh uplink
 ip pim
!
router bgp 5556
 bgp router-id 172.16.0.21
 bgp bestpath as-path multipath-relax
 neighbor swp1 interface v6only remote-as external
 neighbor swp2 interface v6only remote-as external
 neighbor swp3 interface v6only remote-as external
 neighbor swp4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor swp1 activate
  neighbor swp2 activate
  neighbor swp3 activate
  neighbor swp4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor swp1 activate
  neighbor swp2 activate
  neighbor swp3 activate
  neighbor swp4 activate
  advertise-all-vni
  advertise-svi-ip
 exit-address-family
!
line vty
 exec-timeout 0 0
!
cumulus@leaf01:~$
```

{{</tab>}}

{{<tab "leaf02">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf
!
hostname leaf02
password cn321
enable password cn321
log timestamp precision 6
!
log file /var/log/frr/zebra.log

ip forwarding
debug bgp zebra
debug zebra vxlan
debug zebra kernel
debug zebra events
debug bgp updates
vrf vrf1
vni 4001
exit-vrf
vrf vrf2
vni 4002
exit-vrf
vrf vrf3
vni 4003
exit-vrf
debug pim events
debug pim zebra
debug pim packets register
debug pim packets joins
debug pim vxlan
debug pim mlag
debug pim nht
debug pim trace
debug mroute
debug mroute detail
debug zebra mlag
debug msdp events
ip pim rp 192.0.2.5 203.0.113.0/24
ip pim spt-switchover infinity-and-beyond
no debug zebra kernel
no debug zebra events
no debug bgp updates
no debug pim events
no debug pim zebra
no debug pim packets register
no debug pim packets joins
no debug pim vxlan
no debug pim mlag
no debug pim nht
no debug pim trace
no debug mroute
no debug mroute detail
no debug zebra mlag
no debug msdp events
debug zebra evpn mh es
debug zebra evpn mh mac
debug zebra evpn mh neigh
debug zebra evpn mh nh
debug bgp evpn mh es
debug bgp evpn mh route
evpn mh startup-delay 30
!

interface swp1
 evpn mh uplink
!
interface swp2
 evpn mh uplink
!
interface swp3
 evpn mh uplink
!
interface swp4
 evpn mh uplink
!
!
!
!
!
interface hostbond1
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond2
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond3
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
!

log file /var/log/frr/bgpd.log
!
router bgp 5557
 bgp bestpath as-path multipath-relax
 bgp router-id  172.16.0.22
 neighbor swp1 interface v6only remote-as external
 neighbor swp2 interface v6only remote-as external
 neighbor swp3 interface v6only remote-as external
 neighbor swp4 interface v6only remote-as external
 address-family ipv4 unicast
 redistribute connected
 exit-address-family
 address-family ipv6 unicast
 redistribute connected
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 exit-address-family
 address-family l2vpn evpn
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 advertise-all-vni
 advertise-svi-ip
 exit-address-family
!
!
!
interface swp1
 ip pim sm
!
!
interface swp2
 ip pim sm
!
!
interface swp3
 ip pim sm
!
!
interface swp4
 ip pim sm
!
!
interface lo
 ip pim sm
 ip igmp
!
line vty
 exec-timeout 0 0
!
```

{{</tab>}}

{{<tab "leaf03">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf
!
hostname leaf03
password cn321
enable password cn321
log timestamp precision 6
!
log file /var/log/frr/zebra.log

ip forwarding
debug bgp zebra
debug zebra vxlan
debug zebra kernel
debug zebra events
debug bgp updates
vrf vrf1
vni 4001
exit-vrf
vrf vrf2
vni 4002
exit-vrf
vrf vrf3
vni 4003
exit-vrf
debug pim events
debug pim zebra
debug pim packets register
debug pim packets joins
debug pim vxlan
debug pim mlag
debug pim nht
debug pim trace
debug mroute
debug mroute detail
debug zebra mlag
debug msdp events
ip pim rp 192.0.2.5 203.0.113.0/24
ip pim spt-switchover infinity-and-beyond
no debug zebra kernel
no debug zebra events
no debug bgp updates
no debug pim events
no debug pim zebra
no debug pim packets register
no debug pim packets joins
no debug pim vxlan
no debug pim mlag
no debug pim nht
no debug pim trace
no debug mroute
no debug mroute detail
no debug zebra mlag
no debug msdp events
debug zebra evpn mh es
debug zebra evpn mh mac
debug zebra evpn mh neigh
debug zebra evpn mh nh
debug bgp evpn mh es
debug bgp evpn mh route
evpn mh startup-delay 30
!

interface swp1
 evpn mh uplink
!
interface swp2
 evpn mh uplink
!
interface swp3
 evpn mh uplink
!
interface swp4
 evpn mh uplink
!
!
!
!
!
interface hostbond1
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond2
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
interface hostbond3
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:ff:ff:01
!
log file /var/log/frr/bgpd.log
!
router bgp 5558
 bgp bestpath as-path multipath-relax
 bgp router-id  172.16.0.23
 neighbor swp1 interface v6only remote-as external
 neighbor swp2 interface v6only remote-as external
 neighbor swp3 interface v6only remote-as external
 neighbor swp4 interface v6only remote-as external
 address-family ipv4 unicast
 redistribute connected
 exit-address-family
 address-family ipv6 unicast
 redistribute connected
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 exit-address-family
 address-family l2vpn evpn
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 advertise-all-vni
 advertise-svi-ip
 exit-address-family
!

!

!
interface swp1
 ip pim sm
!
!
interface swp2
 ip pim sm
!
!
interface swp3
 ip pim sm
!
!
interface swp4
 ip pim sm
!
!
interface lo
 ip pim sm
 ip igmp
!
line vty
 exec-timeout 0 0
!
```

{{</tab>}}

{{<tab "spine01">}}

```
cumulus@spine01:~$ cat /etc/frr/frr.conf
!
hostname spine01
password cn321
enable password cn321
log timestamp precision 6
!
log file /var/log/frr/zebra.log

ip forwarding
debug bgp zebra
debug zebra vxlan
debug zebra kernel
debug zebra events
debug bgp updates
vrf vrf1
vni 4001
exit-vrf
vrf vrf2
vni 4002
exit-vrf
vrf vrf3
vni 4003
exit-vrf
debug pim events
debug pim zebra
debug pim packets register
debug pim packets joins
debug pim vxlan
debug pim mlag
debug pim nht
debug pim trace
debug mroute
debug mroute detail
debug zebra mlag
debug msdp events
ip pim rp 192.0.2.5 203.0.113.0/24
ip pim spt-switchover infinity-and-beyond
!
!

log file /var/log/frr/bgpd.log
!
router bgp 4435
 bgp bestpath as-path multipath-relax
 bgp router-id  172.16.0.17
 neighbor swp1 interface v6only remote-as external
 neighbor swp2 interface v6only remote-as external
 neighbor swp3 interface v6only remote-as external
 neighbor swp4 interface v6only remote-as external
 neighbor swp5 interface v6only remote-as external
 neighbor swp6 interface v6only remote-as external
 neighbor swp7 interface v6only remote-as external
 neighbor swp8 interface v6only remote-as external
 neighbor swp9 interface v6only remote-as external
 neighbor swp10 interface v6only remote-as external
 neighbor swp11 interface v6only remote-as external
 neighbor swp12 interface v6only remote-as external
 neighbor swp13 interface v6only remote-as external
 neighbor swp14 interface v6only remote-as external
 neighbor swp15 interface v6only remote-as external
 neighbor swp16 interface v6only remote-as external
 address-family ipv4 unicast
 redistribute connected
 neighbor swp1 allowas-in origin
 neighbor swp2 allowas-in origin
 neighbor swp3 allowas-in origin
 neighbor swp4 allowas-in origin
 neighbor swp5 allowas-in origin
 neighbor swp6 allowas-in origin
 neighbor swp7 allowas-in origin
 neighbor swp8 allowas-in origin
 neighbor swp9 allowas-in origin
 neighbor swp10 allowas-in origin
 neighbor swp11 allowas-in origin
 neighbor swp12 allowas-in origin
 neighbor swp13 allowas-in origin
 neighbor swp14 allowas-in origin
 neighbor swp15 allowas-in origin
 neighbor swp16 allowas-in origin
 exit-address-family
 address-family ipv6 unicast
 redistribute connected
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 neighbor swp5 activate
 neighbor swp6 activate
 neighbor swp7 activate
 neighbor swp8 activate
 neighbor swp9 activate
 neighbor swp10 activate
 neighbor swp11 activate
 neighbor swp12 activate
 neighbor swp13 activate
 neighbor swp14 activate
 neighbor swp15 activate
 neighbor swp16 activate
 exit-address-family
 address-family l2vpn evpn
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 neighbor swp5 activate
 neighbor swp6 activate
 neighbor swp7 activate
 neighbor swp8 activate
 neighbor swp9 activate
 neighbor swp10 activate
 neighbor swp11 activate
 neighbor swp12 activate
 neighbor swp13 activate
 neighbor swp14 activate
 neighbor swp15 activate
 neighbor swp16 activate
 exit-address-family
!

!

!
interface swp1
 ip pim sm
!
!
interface swp2
 ip pim sm
!
!
interface swp3
 ip pim sm
!
!
interface swp4
 ip pim sm
!
!
interface swp5
 ip pim sm
!
!
interface swp6
 ip pim sm
!
!
interface swp7
 ip pim sm
!
!
interface swp8
 ip pim sm
!
!
interface swp9
 ip pim sm
!
!
interface swp10
 ip pim sm
!
!
interface swp11
 ip pim sm
!
!
interface swp12
 ip pim sm
!
!
interface swp13
 ip pim sm
!
!
interface swp14
 ip pim sm
!
!
interface swp15
 ip pim sm
!
!
interface swp16
 ip pim sm
!
!
interface lo
 ip pim sm
!
line vty
 exec-timeout 0 0
!
```

{{</tab>}}

{{<tab "spine02">}}

```
cumulus@spine02:~$ cat /etc/frr/frr.conf
!
hostname spine02
password cn321
enable password cn321
log timestamp precision 6
!
log file /var/log/frr/zebra.log

ip forwarding
debug bgp zebra
debug zebra vxlan
debug zebra kernel
debug zebra events
debug bgp updates
vrf vrf1
vni 4001
exit-vrf
vrf vrf2
vni 4002
exit-vrf
vrf vrf3
vni 4003
exit-vrf
debug pim events
debug pim zebra
debug pim packets register
debug pim packets joins
debug pim vxlan
debug pim mlag
debug pim nht
debug pim trace
debug mroute
debug mroute detail
debug zebra mlag
debug msdp events
ip pim rp 192.0.2.5 203.0.113.0/24
ip pim spt-switchover infinity-and-beyond
!
!
!

log file /var/log/frr/bgpd.log
!
router bgp 4435
 bgp bestpath as-path multipath-relax
 bgp router-id  172.16.0.18
 neighbor swp1 interface v6only remote-as external
 neighbor swp2 interface v6only remote-as external
 neighbor swp3 interface v6only remote-as external
 neighbor swp4 interface v6only remote-as external
 neighbor swp5 interface v6only remote-as external
 neighbor swp6 interface v6only remote-as external
 neighbor swp7 interface v6only remote-as external
 neighbor swp8 interface v6only remote-as external
 neighbor swp9 interface v6only remote-as external
 neighbor swp10 interface v6only remote-as external
 neighbor swp11 interface v6only remote-as external
 neighbor swp12 interface v6only remote-as external
 neighbor swp13 interface v6only remote-as external
 neighbor swp14 interface v6only remote-as external
 neighbor swp15 interface v6only remote-as external
 neighbor swp16 interface v6only remote-as external
 address-family ipv4 unicast
 redistribute connected
 neighbor swp1 allowas-in origin
 neighbor swp2 allowas-in origin
 neighbor swp3 allowas-in origin
 neighbor swp4 allowas-in origin
 neighbor swp5 allowas-in origin
 neighbor swp6 allowas-in origin
 neighbor swp7 allowas-in origin
 neighbor swp8 allowas-in origin
 neighbor swp9 allowas-in origin
 neighbor swp10 allowas-in origin
 neighbor swp11 allowas-in origin
 neighbor swp12 allowas-in origin
 neighbor swp13 allowas-in origin
 neighbor swp14 allowas-in origin
 neighbor swp15 allowas-in origin
 neighbor swp16 allowas-in origin
 exit-address-family
 address-family ipv6 unicast
 redistribute connected
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 neighbor swp5 activate
 neighbor swp6 activate
 neighbor swp7 activate
 neighbor swp8 activate
 neighbor swp9 activate
 neighbor swp10 activate
 neighbor swp11 activate
 neighbor swp12 activate
 neighbor swp13 activate
 neighbor swp14 activate
 neighbor swp15 activate
 neighbor swp16 activate
 exit-address-family
 address-family l2vpn evpn
 neighbor swp1 activate
 neighbor swp2 activate
 neighbor swp3 activate
 neighbor swp4 activate
 neighbor swp5 activate
 neighbor swp6 activate
 neighbor swp7 activate
 neighbor swp8 activate
 neighbor swp9 activate
 neighbor swp10 activate
 neighbor swp11 activate
 neighbor swp12 activate
 neighbor swp13 activate
 neighbor swp14 activate
 neighbor swp15 activate
 neighbor swp16 activate
 exit-address-family
!

!

!
interface swp1
 ip pim sm
!
!
interface swp2
 ip pim sm
!
!
interface swp3
 ip pim sm
!
!
interface swp4
 ip pim sm
!
!
interface swp5
 ip pim sm
!
!
interface swp6
 ip pim sm
!
!
interface swp7
 ip pim sm
!
!
interface swp8
 ip pim sm
!
!
interface swp9
 ip pim sm
!
!
interface swp10
 ip pim sm
!
!
interface swp11
 ip pim sm
!
!
interface swp12
 ip pim sm
!
!
interface swp13
 ip pim sm
!
!
interface swp14
 ip pim sm
!
!
interface swp15
 ip pim sm
!
!
interface swp16
 ip pim sm
!
!
interface lo
 ip pim sm
!
line vty
 exec-timeout 0 0
```

{{</tab>}}

{{</tabs>}}

<!-- 
- Any Linux show commands or just the FRR?
-->
