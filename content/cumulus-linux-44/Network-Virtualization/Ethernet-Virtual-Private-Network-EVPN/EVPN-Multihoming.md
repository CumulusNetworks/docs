---
title: EVPN Multihoming
author: NVIDIA
weight: 570
toc: 4
---

*EVPN multihoming* (EVPN-MH) provides support for all-active server redundancy. It is a standards-based replacement for MLAG in data centers deploying Clos topologies. Replacing MLAG provides these benefits:

- Eliminates the need for peerlinks or inter-switch links between the top of rack switches
- Allows more than two TOR switches to participate in a redundancy group
- Provides a single BGP-EVPN control plane
- Allows multi-vendor interoperability

EVPN-MH uses {{<link url="#supported-evpn-route-types" text="BGP-EVPN type-1, type-2 and type-4 routes">}} to discover Ethernet segments (ES) and to forward traffic to those Ethernet segments. The MAC and neighbor databases are synchronized between the Ethernet segment peers through these routes as well. An *{{<exlink url="https://tools.ietf.org/html/rfc7432#section-5" text="Ethernet segment">}}* is a group of switch links that are attached to the same server. Each Ethernet segment has an unique Ethernet segment ID (`es-id`) across the entire PoD.

To configure EVPN-MH, you set an Ethernet segment system MAC address and a local Ethernet segment ID on a static or LACP bond. These two parameters generate the unique MAC-based ESI value ({{<exlink url="https://tools.ietf.org/html/rfc7432#section-5" text="type-3">}}) automatically:

- The Ethernet segment system MAC address is used for the LACP system identifier.
- The local Ethernet segment ID configuration defines a local discriminator to uniquely enumerate each bond that shares the same Ethernet segment system MAC address.
- The resulting 10-byte ESI value has the following format, where the MMs denote the 6-byte Ethernet segment system MAC address and the XXs denote the 3-byte local Ethernet segment ID value:

      03:MM:MM:MM:MM:MM:MM:XX:XX:XX

While you can specify a different system MAC address on different Ethernet segments attached to the same switch, the Ethernet segment system MAC address must be the same on the downlinks attached to the same server.

{{%notice info%}}
When using Spectrum 2 or Spectrum 3 switches, an Ethernet segment can span more than two switches. Each Ethernet segment is a distinct redundancy group. However, when using Spectrum A1 switches, a maximum of two switches can participate in a redundancy group or Ethernet segment.
{{%/notice%}}

## Required and Supported Features

This section describes features that you must enable to use EVPN multihoming. Other supported and unsupported features are also described.

### Required Features

You must enable the following features to use EVPN-MH:

- {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge mode">}}
- {{<link url="EVPN-Enhancements/#arp-and-nd-suppression" text="ARP suppression">}}

Head End Replication is enabled by default with EVPN multihoming. If you prefer to use EVPN BUM traffic handling with EVPN-PIM on multihomed sites via Type-4/ESR routes, configure EVPN-PIM as described in {{<link title="EVPN BUM Traffic with PIM-SM" text="EVPN BUM Traffic with PIM-SM">}}.

{{%notice warning%}}
To use EVPN-MH, you must remove any MLAG configuration on the switch:
- Remove the `clag-id` from all interfaces in the `/etc/network/interfaces` file.
- Remove the peerlink interfaces in the `/etc/network/interfaces` file.
- Remove any existing `hwaddress` (from a Cumulus Linux 3.x MLAG configuration) or `address-virtual` (from a Cumulus Linux 4.x MLAG configuration) entries from all SVIs corresponding to a layer 3 VNI in the `/etc/network/interfaces` file.
- Remove any `clagd-vxlan-anycast-ip` configuration in the `/etc/network/interfaces` file.
- Run the `sudo ifreload` command to reload the configuration.
{{%/notice%}}

### Supported Features

- Known unicast traffic multihoming through type-1/EAD (Ethernet auto discovery) routes and type-2 (non-zero ESI) routes. Includes all-active redundancy using aliasing and support for fast failover.
- {{<link url="LACP-Bypass">}} is supported.
  - When an EVPN-MH bond enters LACP bypass state, BGP stops advertising EVPN type-1 and type-4 routes for that bond. Split-horizon and designated forwarder filters are disabled.
  - When an EVPN-MH bond exits the LACP bypass state, BGP starts advertising EVPN type-1 and type-4 routes for that bond. Split-horizon and designated forwarder filters are enabled.
- EVI (*EVPN virtual instance*). Cumulus Linux supports VLAN-based service only, so the EVI is just a layer 2 VNI.
- Supported {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="ASICs">}} include NVIDIA Spectrum A1, Spectrum 2 and Spectrum 3.

### Supported EVPN Route Types

EVPN multihoming supports the following route types.

| Route Type | Description | RFC or Draft |
| ---------- | ----------- | ------------ |
| 1 | Ethernet auto-discovery (A-D) route | {{<exlink url="https://tools.ietf.org/html/rfc7432" text="RFC 7432">}} |
| 2 | MAC/IP advertisement route | {{<exlink url="https://tools.ietf.org/html/rfc7432" text="RFC 7432">}} |
| 3 | Inclusive multicast route | {{<exlink url="https://tools.ietf.org/html/rfc7432" text="RFC 7432">}} |
| 4 | Ethernet segment route | {{<exlink url="https://tools.ietf.org/html/rfc7432" text="RFC 7432">}} |
| 5 | IP prefix route | {{<exlink url="https://tools.ietf.org/html/draft-ietf-bess-evpn-prefix-advertisement-04" text="draft-ietf-bess-evpn-prefix-advertisement-04">}} |

### Unsupported Features

The following features are not supported with EVPN-MH:

- {{<link url="Traditional-Bridge-Mode" text="Traditional bridge mode">}}
- {{<link url="Inter-subnet-Routing/#asymmetric-routing" text="Distributed asymmetric routing">}}

## Basic Configuration

To configure EVPN-MH:
1. Enable EVPN multihoming.
2. Set the Ethernet segment ID.
3. Set the Ethernet segment system MAC address.

These settings are applied to interfaces, typically bonds.

An Ethernet segment configuration has these characteristics:

- The Ethernet segment ID is a 24-bit integer (1-16777215).
- Each interface (bond) needs its own Ethernet segment ID.
- Static and LACP bonds can be associated with an Ethernet segment ID.

A *designated forwarder* (DF) is elected for each Ethernet segment. The DF is responsible for forwarding flooded traffic received through the VXLAN overlay to the locally attached Ethernet segment. Specify a preference on an Ethernet segment for the DF election, as this leads to predictable failure scenarios. The EVPN VTEP with the highest DF preference setting becomes the DF. The DF preference setting defaults to _32767_.

NCLU (and NVUE) generates the EVPN-MH configuration and reloads FRR and `ifupdown2`. The configuration appears in both the `/etc/network/interfaces` file and in `/etc/frr/frr.conf` file.

{{%notice note%}}
When EVPN-MH is enabled, all SVI MAC addresses are advertised as type 2 routes. You do not need to configure a unique SVI IP address or configure the BGP EVPN address family with `advertise-svi-ip`.
{{%/notice%}}

### Enable EVPN-MH

{{< tabs "TabID105 ">}}
{{<tab "NCLU Commands">}}

NCLU commands are not supported; use Linux commands.

{{< /tab >}}
{{<tab "NVUE Commands">}}

```
cumulus@leaf01:~$ nv set evpn multihoming enable on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Set the `evpn.multihoming.enable` variable in the `/etc/cumulus/switchd.conf` file to `TRUE`, then restart the `switchd` service. The variable is disabled by default.

```
cumulus@leaf01:~$ sudo nano /etc/cumulus/switchd.conf
...
evpn.multihoming.enable = TRUE
...
```

```
cumulus@leaf01:~$ sudo systemctl restart switchd.service
```

{{< /tab >}}
{{< /tabs >}}

### Configure the EVPN-MH Bonds

To configure bond interfaces for EVPN-MH, run commands similar to the following:

{{<tabs "bond config">}}
{{<tab "NCLU Commands">}}

```
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add bond bond3 bond slaves swp3
cumulus@leaf01:~$ net add bond bond1 evpn mh es-id 1
cumulus@leaf01:~$ net add bond bond2 evpn mh es-id 2
cumulus@leaf01:~$ net add bond bond3 evpn mh es-id 3
cumulus@leaf01:~$ net add bond bond1-3 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add bond bond1-3 evpn mh es-df-pref 50000
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration in the `/etc/network/interfaces` file.

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
interface bond1
  bond-slaves swp1
  es-sys-mac 44:38:39:BE:EF:AA

interface bond2
  bond-slaves swp2
  es-sys-mac 44:38:39:BE:EF:AA

interface bond3
  bond-slaves swp3
  es-sys-mac 44:38:39:BE:EF:AA
```

The NCLU commands also create the following configuration in the `/etc/frr/frr.conf` file.

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
!
interface bond1
 evpn mh es-df-pref 50000
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond2
 evpn mh es-df-pref 50000
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond3
 evpn mh es-df-pref 50000
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
```

{{</tab>}}
{{<tab "NVUE Commands">}}

```
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf01:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf01:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf01:~$ nv config apply
```

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml

```

{{</tab>}}
{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# interface bond1
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 1
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:BE:EF:AA
leaf01(config-if)# exit
leaf01(config)# interface bond2
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 2
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:BE:EF:AA
leaf01(config-if)# exit
leaf01(config)# interface bond3
leaf01(config-if)# evpn mh es-df-pref 50000
leaf01(config-if)# evpn mh es-id 3
leaf01(config-if)# evpn mh es-sys-mac 44:38:39:BE:EF:AA
leaf01(config-if)# exit
leaf01(config)# write memory
leaf01(config)# exit
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands create the following configuration in the `/etc/network/interfaces` file.

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
interface bond1
  bond-slaves swp1
  es-sys-mac 44:38:39:BE:EF:AA

interface bond2
  bond-slaves swp2
  es-sys-mac 44:38:39:BE:EF:AA

interface bond3
  bond-slaves swp3
  es-sys-mac 44:38:39:BE:EF:AA
```

The vtysh commands also create the following configuration in the `/etc/frr/frr.conf` file.

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
!
interface bond1
 evpn mh es-df-pref 50000
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond2
 evpn mh es-df-pref 50000
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond3
 evpn mh es-df-pref 50000
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
```

{{</tab>}}
{{</tabs>}}

## Optional EVPN MH Configuration

### Global Settings

You can set these global settings for EVPN-MH:
- `mac-holdtime` specifies the duration for which a switch maintains SYNC MAC entries after the EVPN type-2 route of the Ethernet segment peer is deleted. During this time, the switch attempts to independently establish reachability of the MAC address on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.
- `neigh-holdtime` specifies the duration for which a switch maintains SYNC neighbor entries after the EVPN type-2 route of the Ethernet segment peer is deleted. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.
- `redirect-off` disables fast failover of traffic destined to the access port via the VXLAN overlay. This only applies to Cumulus VX (fast failover is only supported on the ASIC).
- `startup-delay` specifies the duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. The delay can be between 0 and 216000 seconds. The default is 180 seconds.

To configure a MAC hold time for 1000 seconds, run the following commands:

{{<tabs "MAC hold time">}}
{{<tab "NCLU Commands">}}

```
cumulus@leaf01:~$ net add evpn mh mac-holdtime 1000
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1000
```

{{</tab>}}
{{<tab "NVUE Commands">}}

```
cumulus@leaf01:~$ nv set evpn multihoming mac-holdtime 1000
cumulus@leaf01:~$ nv config apply
```

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
```

{{</tab>}}
{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# evpn mh mac-holdtime 1000
leaf01(config)# exit
leaf01# write memory
```

The vtysh commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1000
```

{{</tab>}}
{{</tabs>}}

To configure a neighbor hold time for 600 seconds, run the following commands:

{{<tabs "Neighbor hold time">}}
{{<tab "NCLU Commands">}}

```
cumulus@leaf01:~$ net add evpn mh neigh-holdtime 600
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh neigh-holdtime 600
```

{{</tab>}}
{{<tab "NVUE Commands">}}

```
cumulus@leaf01:~$ nv set evpn multihoming neighbor-holdtime 600
cumulus@leaf01:~$ nv config apply
```

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
```

{{</tab>}}
{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# evpn mh neigh-holdtime 600
leaf01(config)# exit
leaf01# write memory
```

The vtysh commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh neigh-holdtime 600
```

{{</tab>}}
{{</tabs>}}

To configure a startup delay for 1800 seconds, run the following commands:

{{<tabs "startup delay">}}
{{<tab "NCLU Commands">}}

```
cumulus@leaf01:~$ net add evpn mh startup-delay 1800
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh startup-delay 1800
```

{{</tab>}}
{{<tab "NVUE Commands">}}

```
cumulus@leaf01:~$ nv set evpn multihoming startup-delay 1800
cumulus@leaf01:~$ nv config apply
```

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
```

{{</tab>}}
{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# evpn mh startup-delay 1800
leaf01(config)# exit
leaf01# write memory
```

The vtysh commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh startup-delay 1800
```

{{</tab>}}
{{</tabs>}}

### Enable Uplink Tracking

When all the uplinks go down, the VTEP loses connectivity to the VXLAN overlay. To prevent traffic loss in this state, the uplinks' oper-state is tracked. When all the uplinks are down, the Ethernet segment bonds on the switch are put into a protodown or error-disabled state. You can configure a link as an MH uplink to enable this tracking.

{{<tabs "upink tracking">}}
{{<tab "NCLU Commands">}}

```
cumulus@leaf01:~$ net add interface swp1-4 evpn mh uplink
cumulus@leaf01:~$ net add interface swp1-4 pim
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
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
...
```

{{</tab>}}
{{<tab "NVUE Commands">}}

```
cumulus@leaf01:~$ nv set interface swp51-54 evpn multihoming uplink on
cumulus@leaf01:~$ nv config apply
```

If you are configuring EVPN multihoming with EVPN-PIM, be sure to configure PIM on the interfaces.

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
```

{{</tab>}}
{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

leaf01# configure terminal
leaf01(config)# interface swp51
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# exit
leaf01(config)# interface swp52
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# exit
leaf01(config)# interface swp53
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# exit
leaf01(config)# interface swp54
leaf01(config-if)# evpn mh uplink
leaf01(config-if)# exit
leaf01(config)# write memory
leaf01(config)# exit
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
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
...
```

{{</tab>}}
{{</tabs>}}

### Enable FRR Debugging

You can add debug statements to the `/etc/frr/frr.conf` file to debug the Ethernet segments, routes, and routing protocols (via Zebra).

{{<tabs "debug">}}
{{<tab "NCLU Commands">}}

To debug Ethernet segments and routes, use the `net add bgp debug evpn mh (es|route)` command. To debug the routing protocols, use `net add evpn mh debug zebra (es|mac|neigh|nh)`.

```
cumulus@leaf01:~$ net add bgp debug evpn mh es
cumulus@leaf01:~$ net add bgp debug evpn mh route
cumulus@leaf01:~$ net add evpn mh debug zebra
cumulus@leaf01:~$ net add evpn mh debug zebra es
cumulus@leaf01:~$ net add evpn mh debug zebra mac
cumulus@leaf01:~$ net add evpn mh debug zebra neigh
cumulus@leaf01:~$ net add evpn mh debug zebra nh
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
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

{{</tab>}}
{{<tab "NVUE Commands">}}

NVUE commands are not supported.

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

The vtysh commands create the following configuration in the `/etc/frr/frr.conf` file:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
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

{{</tab>}}
{{</tabs>}}

### Fast Failover

When an Ethernet segment link goes down, the attached VTEP notifies all other VTEPs using a single EAD-ES withdraw. This is done by way of an Ethernet segment bond redirect.

Fast failover also triggers:

- When you reboot a leaf switch or VTEP.
- When there is an uplink failure. When all uplinks are down, the Ethernet segment bonds on the switch are protodowned or error disabled.

### Disable Next Hop Group Sharing in the ASIC

Container sharing for both layer 2 and layer 3 next hop groups is enabled by default when EVPN-MH is configured. These settings are stored in the `evpn.multihoming.shared_l2_groups` and `evpn.multihoming.shared_l3_groups` variables.

Disabling container sharing allows for faster failover when an Ethernet segment link flaps.

To disable either setting, edit the `switchd.conf` file, set the variable to _FALSE_, then restart the `switchd` service. For example, to disable container sharing for layer 3 next hop groups:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
evpn.multihoming.shared_l3_groups = FALSE
...

cumulus@switch:~$ sudo systemctl restart switchd.service
```

### Disable EAD-per-EVI Route Advertisements

{{<exlink url="https://tools.ietf.org/html/rfc7432" text="RFC 7432">}} requires type-1/EAD (Ethernet Auto-discovery) routes to be advertised two ways:

- As EAD-per-ES (Ethernet Auto-discovery per Ethernet segment) routes
- As EAD-per-EVI (Ethernet Auto-discovery per EVPN instance) routes

Some third party switch vendors do not advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.

To remove the dependency on EAD-per-EVI routes and activate the VTEP upon receiving the EAD-per-ES route:

{{< tabs "TabID516 ">}}
{{< tab "NCLU Commands ">}}

To remove the dependency on EAD-per-EVI routes and activate the VTEP upon receiving the EAD-per-ES route, run:

```
cumulus@switch:~$ net add bgp l2vpn evpn disable-ead-evi-rx
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To suppress the advertisement of EAD-per-EVI routes, run:

```
cumulus@switch:~$ net add bgp l2vpn evpn disable-ead-evi-tx
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set evpn multihoming ead-evi-route rx off
cumulus@switch:~$ nv config apply
```

To suppress the advertisement of EAD-per-EVI routes, run:

```
cumulus@switch:~$ nv set evpn multihoming ead-evi-route tx off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# disable-ead-evi-rx
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

To suppress the advertisement of EAD-per-EVI routes, run:

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# disable-ead-evi-tx
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

You can use the following `net show` commands to troubleshoot your EVPN multihoming configuration.

### Show Ethernet Segment Information

The `net show evpn es` command displays the Ethernet segments across all VNIs.

```
cumulus@switch:~$ net show evpn es
Type: L local, R remote, N non-DF
ESI                            Type ES-IF                 VTEPs
03:44:38:39:BE:EF:AA:00:00:01  R    -                     172.0.0.22,172.0.0.23
03:44:38:39:BE:EF:AA:00:00:02  LR   bond2             172.0.0.22,172.0.0.23
03:44:38:39:BE:EF:AA:00:00:03  LR   bond3             172.0.0.22,172.0.0.23
03:44:38:39:BE:EF:AA:00:00:05  L    bond1
03:44:38:39:ff:ff:02:00:00:01  R    -                     172.0.0.24,172.0.0.25,172.0.0.26
03:44:38:39:ff:ff:02:00:00:02  R    -                     172.0.0.24,172.0.0.25,172.0.0.26
03:44:38:39:ff:ff:02:00:00:03  R    -                     172.0.0.24,172.0.0.25,172.0.0.26
```

### Show Ethernet Segment per VNI Information

The `net show evpn es-evi` command displays the Ethernet segments learned for each VNI.

```
cumulus@switch:~$ net show evpn es-evi
Type: L local, R remote
VNI      ESI                            Type
...
1002     03:44:38:39:BE:EF:AA:00:00:02  L
1002     03:44:38:39:BE:EF:AA:00:00:03  L
1002     03:44:38:39:BE:EF:AA:00:00:05  L
1001     03:44:38:39:BE:EF:AA:00:00:02  L
1001     03:44:38:39:BE:EF:AA:00:00:03  L
1001     03:44:38:39:BE:EF:AA:00:00:05  L
...
```

### Show BGP Ethernet Segment Information

The `net show bgp l2vpn evpn es` command displays the Ethernet segments across all VNIs learned via type-1 and type-4 routes.

```
cumulus@switch:~$ net show bgp l2vpn evpn es
ES Flags: L local, R remote, I inconsistent
VTEP Flags: E ESR/Type-4, A active nexthop
ESI                            Flags RD                    #VNIs    VTEPs
03:44:38:39:BE:EF:AA:00:00:01  LR    172.0.0.9:3            10       172.0.0.10(EA),172.0.0.11(EA)
03:44:38:39:BE:EF:AA:00:00:02  LR    172.0.0.9:4            10       172.0.0.10(EA),172.0.0.11(EA)
03:44:38:39:BE:EF:AA:00:00:03  LR    172.0.0.9:5            10       172.0.0.10(EA),172.0.0.11(EA)
cumulus@switch:~$
```

### Show BGP Ethernet Segment per VNI Information

The `net show bgp l2vpn evpn es-evi` command displays the Ethernet segments per VNI learned via type-1 and type-4 routes.

```
cumulus@switch:~$ net show bgp l2vpn evpn es-evi
Flags: L local, R remote, I inconsistent
VTEP-Flags: E EAD-per-ES, V EAD-per-EVI
VNI      ESI                            Flags VTEPs
...
1002     03:44:38:39:BE:EF:AA:00:00:01  R     172.0.0.22(EV),172.0.0.23(EV)
1002     03:44:38:39:BE:EF:AA:00:00:02  LR    172.0.0.22(EV),172.0.0.23(EV)
1002     03:44:38:39:BE:EF:AA:00:00:03  LR    172.0.0.22(EV),172.0.0.23(EV)
1002     03:44:38:39:BE:EF:AA:00:00:05  L  
1002     03:44:38:39:ff:ff:02:00:00:01  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:02  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:03  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1001     03:44:38:39:BE:EF:AA:00:00:01  R     172.0.0.22(EV),172.0.0.23(EV)
1001     03:44:38:39:BE:EF:AA:00:00:02  LR    172.0.0.22(EV),172.0.0.23(EV)
1001     03:44:38:39:BE:EF:AA:00:00:03  LR    172.0.0.22(EV),172.0.0.23(EV)
1001     03:44:38:39:BE:EF:AA:00:00:05  L  
1001     03:44:38:39:ff:ff:02:00:00:01  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:02  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:03  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
...
cumulus@switch:~$
```

### Show EAD Route Types

You can use the `net show bgp l2vpn evpn route` command to view type-1 EAD routes. Just include the `ead` route type option.

```
cumulus@switch:~$ net show bgp evpn l2vpn route type ead
BGP table version is 30, local router ID is 172.16.0.21
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 172.16.0.21:2
*> [1]:[0]:[03:44:38:39:BE:EF:AA:00:00:01]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005
*> [1]:[0]:[03:44:38:39:BE:EF:AA:00:00:02]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005
*> [1]:[0]:[03:44:38:39:BE:EF:AA:00:00:03]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005

...

Displayed 198 prefixes (693 paths) (of requested type)
cumulus@switch:~$
```

## Example Configurations

The following configuration examples use the topology illustrated below.

{{<img src="/images/cumulus-linux/EVPN-MH-example-config-citc.png">}}

### EVPN-MH with Head End Replication

{{< tabs "TabID688 ">}}
{{<tab "NCLU Commands">}}

NCLU commands are not supported.

{{</tab>}}
{{<tab "NVUE Commands">}}

{{< tabs "TabID696 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-3,swp51-52
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond1 link mtu 9000
cumulus@leaf01:~$ nv set interface bond2 link mtu 9000
cumulus@leaf01:~$ nv set interface bond3 link mtu 9000
cumulus@leaf01:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf01:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf01:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf01:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf01:~$ nv set vrf RED
cumulus@leaf01:~$ nv set vrf BLUE
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ nv set vrf RED evpn vni 4001
cumulus@leaf01:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf01:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set evpn enable on
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:~$ nv set evpn multihoming enable on
cumulus@leaf01:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf01:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf01:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf01:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf01:~$ nv config apply
```

{{</tab>}}
{{<tab "leaf02">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1-3,swp51-52
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond1 link mtu 9000
cumulus@leaf02:~$ nv set interface bond2 link mtu 9000
cumulus@leaf02:~$ nv set interface bond3 link mtu 9000
cumulus@leaf02:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf02:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf02:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf02:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf02:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf02:~$ nv set vrf RED
cumulus@leaf02:~$ nv set vrf BLUE
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf02:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf02:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf02:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf02:~$ nv set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf02:~$ nv set vrf RED evpn vni 4001
cumulus@leaf02:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf02:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set evpn enable on
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf02:~$ nv set evpn multihoming enable on
cumulus@leaf02:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf02:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf02:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf02:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf02:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf02:~$ nv config apply
```

{{</tab>}}
{{<tab "leaf03">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1-3,swp51-52
cumulus@leaf03:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:~$ nv set interface bond2 bond member swp2
cumulus@leaf03:~$ nv set interface bond3 bond member swp3
cumulus@leaf03:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond1 link mtu 9000
cumulus@leaf03:~$ nv set interface bond2 link mtu 9000
cumulus@leaf03:~$ nv set interface bond3 link mtu 9000
cumulus@leaf03:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf03:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf03:~$ nv set interface vlan10 ip address 10.1.10.4/24
cumulus@leaf03:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf03:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf03:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf03:~$ nv set interface vlan20 ip address 10.1.20.4/24
cumulus@leaf03:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf03:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf03:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf03:~$ nv set interface vlan30 ip address 10.1.30.4/24
cumulus@leaf03:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf03:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf03:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf03:~$ nv set vrf RED
cumulus@leaf03:~$ nv set vrf BLUE
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf03:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf03:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf03:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf03:~$ nv set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf03:~$ nv set vrf RED evpn vni 4001
cumulus@leaf03:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf03:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf03:~$ nv set evpn enable on
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf03:~$ nv set evpn multihoming enable on
cumulus@leaf03:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf03:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf03:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf03:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf03:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf03:~$ nv config apply
```

{{</tab>}}
{{<tab "leaf04">}}

```
cumulus@leaf04:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ nv set interface swp1-3,swp51-52
cumulus@leaf04:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:~$ nv set interface bond2 bond member swp2
cumulus@leaf04:~$ nv set interface bond3 bond member swp3
cumulus@leaf04:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond1 link mtu 9000
cumulus@leaf04:~$ nv set interface bond2 link mtu 9000
cumulus@leaf04:~$ nv set interface bond3 link mtu 9000
cumulus@leaf04:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf04:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf04:~$ nv set interface vlan10 ip address 10.1.10.5/24
cumulus@leaf04:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf04:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf04:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf04:~$ nv set interface vlan20 ip address 10.1.20.5/24
cumulus@leaf04:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf04:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf04:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf04:~$ nv set interface vlan30 ip address 10.1.30.5/24
cumulus@leaf04:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf04:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf04:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf04:~$ nv set vrf RED
cumulus@leaf04:~$ nv set vrf BLUE
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf04:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf04:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf04:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf04:~$ nv set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf04:~$ nv set vrf RED evpn vni 4001
cumulus@leaf04:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf04:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf04:~$ nv set evpn enable on
cumulus@leaf04:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf04:~$ nv set evpn multihoming enable on
cumulus@leaf04:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf04:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf04:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf04:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf04:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf04:~$ nv config apply
```

{{</tab>}}
{{<tab "spine01">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-4
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine01:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine01:~$ nv config apply
```

{{</tab>}}
{{<tab "spine02">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1-4
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine02:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine02:~$ nv config apply
```

{{</tab>}}
{{</tabs>}}

{{</tab>}}
{{<tab "/etc/network/interfaces">}}

{{< tabs "TabID998 ">}}
{{<tab "leaf01">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.1/32
    vxlan-local-tunnelip 10.10.10.1

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "leaf02">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    vxlan-local-tunnelip 10.10.10.2

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.4/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.4/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.4/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "leaf03">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.3/32
    vxlan-local-tunnelip 10.10.10.3

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.4/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.4/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.4/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "leaf04">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.4/32
    vxlan-local-tunnelip 10.10.10.4

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.5/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.5/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.5/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "spine01">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.101/32

auto eth0
iface eth0
    vrf mgmt
    address 192.168.200.21/24

auto mgmt
iface mgmt
  vrf-table auto
  address 127.0.0.1/8
  address ::1/128

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

{{</tab>}}
{{<tab "spine02">}}

```
cumulus@spine02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto eth0
iface eth0
    vrf mgmt
    address 192.168.200.22/24

auto mgmt
iface mgmt
  vrf-table auto
  address 127.0.0.1/8
  address ::1/128

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

{{</tab>}}
{{<tab "server01">}}

```
cumulus@server01:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.10.101
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.10.1
```

{{</tab>}}
{{<tab "server02">}}

```
cumulus@server02:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.20.102
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.20.1
```

{{</tab>}}
{{<tab "server03">}}

```
cumulus@server03:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.30.103
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.30.1
```

{{</tab>}}
{{<tab "server04">}}

```
cumulus@server04:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.10.104
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.10.1
```

{{</tab>}}
{{</tabs>}}

{{</tab>}}
{{<tab "/etc/frr/frr.conf">}}

{{< tabs "TabID1831 ">}}
{{<tab "leaf01">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1080
evpn mh neigh-holdtime 1080
evpn mh startup-delay 180
interface swp51
evpn mh uplink
interface swp52
evpn mh uplink
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:AA
vrf RED
vni 4001
exit-vrf
vrf BLUE
vni 4002
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
!
router bgp 65101 vrf default
bgp router-id 10.10.10.1
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{<tab "leaf02">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1000
evpn mh neigh-holdtime 600
evpn mh startup-delay 180
interface swp51
evpn mh uplink
interface swp52
evpn mh uplink
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:AA
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65102 vrf default
bgp router-id 10.10.10.2
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{<tab "leaf03">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1000
evpn mh neigh-holdtime 600
evpn mh startup-delay 180
interface swp51
evpn mh uplink
interface swp52
evpn mh uplink
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:BB
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65103 vrf default
bgp router-id 10.10.10.3
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
```

{{</tab>}}
{{<tab "leaf04">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1000
evpn mh neigh-holdtime 600
evpn mh startup-delay 180
interface swp51
evpn mh uplink
interface swp52
evpn mh uplink
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:BB
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65104 vrf default
bgp router-id 10.10.10.4
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
```

{{</tab>}}
{{<tab "spine01">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
vrf mgmt
ip route 0.0.0.0/0 192.168.200.1
exit-vrf
!
router bgp 65100
bgp router-id 10.10.10.101
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp2 interface peer-group underlay
neighbor swp3 interface peer-group underlay
neighbor swp4 interface peer-group underlay
!
address-family ipv4 unicast
redistribute connected
exit-address-family
!
address-family l2vpn evpn
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{<tab "spine02">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
vrf mgmt
 ip route 0.0.0.0/0 192.168.200.1
 exit-vrf
!
router bgp 65100
bgp router-id 10.10.10.102
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp2 interface peer-group underlay
neighbor swp3 interface peer-group underlay
neighbor swp4 interface peer-group underlay
!
!
address-family ipv4 unicast
redistribute connected
exit-address-family
!
address-family l2vpn evpn
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{</tabs>}}

{{</tab>}}
{{</tabs>}}

### EVPN-MH with EVPN-PIM

<!-- NEED COMMANDS for PIM-->

{{< tabs "TabID2213 ">}}
{{<tab "NCLU Commands">}}

{{< tabs "TabID2205 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add interface swp1-3,swp51-52
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add bond bond3 bond slaves swp3
cumulus@leaf01:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf01:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf01:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf01:~$ net add interface swp51-52 alias to spine
cumulus@leaf01:~$ net add bond bond1 bridge access 10
cumulus@leaf01:~$ net add bond bond2 bridge access 20
cumulus@leaf01:~$ net add bond bond3 bridge access 30
cumulus@leaf01:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf01:~$ net add bond bond1-3 mtu 9000
cumulus@leaf01:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf01:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf01:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf01:~$ net add loopback lo pim
cumulus@leaf01:~$ net add pim rp 10.10.100.100 224.0.0.0/4
cumulus@leaf01:~$ net add pim ecmp
cumulus@leaf01:~$ net add pim keep-alive-timer 3600
cumulus@leaf01:~$ net add interface swp51-52 pim
cumulus@leaf01:~$ net add interface swp51-52 evpn mh uplink
cumulus@leaf01:~$ net add evpn mh startup-delay 10
cumulus@leaf01:~$ net add bond bond1 evpn mh es-df-pref 50000
cumulus@leaf01:~$ net add bond bond2 evpn mh es-df-pref 50000
cumulus@leaf01:~$ net add bond bond3 evpn mh es-df-pref 50000
cumulus@leaf01:~$ net add bond bond1 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add bond bond2 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add bond bond3 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add bond bond1 evpn mh es-id 1
cumulus@leaf01:~$ net add bond bond2 evpn mh es-id 2
cumulus@leaf01:~$ net add bond bond3 evpn mh es-id 3
cumulus@leaf01:~$ net add vrf RED vni 4001
cumulus@leaf01:~$ net add vrf BLUE vni 4002
cumulus@leaf01:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf01:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf01:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf01:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf01:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf01:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf01:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf01:~$ net add bridge bridge vlan-aware
cumulus@leaf01:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@leaf01:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf01:~$ net add vlan 10 vlan-id 10
cumulus@leaf01:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 10 vrf RED
cumulus@leaf01:~$ net add vlan 20 ip address 10.1.20.2/24
cumulus@leaf01:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf01:~$ net add vlan 20 vlan-id 20
cumulus@leaf01:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 20 vrf RED
cumulus@leaf01:~$ net add vlan 30 ip address 10.1.30.2/24
cumulus@leaf01:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf01:~$ net add vlan 30 vlan-id 30
cumulus@leaf01:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 30 vrf BLUE
cumulus@leaf01:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf01:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 4001 vrf RED
cumulus@leaf01:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf01:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf01:~$ net add vlan 4002 vrf BLUE
cumulus@leaf01:~$ net add vrf BLUE,mgmt,RED vrf-table auto
cumulus@leaf01:~$ net add vxlan vni10 bridge access 10
cumulus@leaf01:~$ net add vxlan vni10 vxlan mcastgrp 224.0.0.10
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf01:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf01:~$ net add vxlan vni20 bridge access 20
cumulus@leaf01:~$ net add vxlan vni20 vxlan mcastgrp 224.0.0.20
cumulus@leaf01:~$ net add vxlan vni30 bridge access 30
cumulus@leaf01:~$ net add vxlan vni30 vxlan mcastgrp 224.0.0.30
cumulus@leaf01:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf01:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf01:~$ net add loopback lo vxlan local-tunnelip 10.10.10.1
cumulus@leaf01:~$ net add evpn mh startup-delay 30
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp neighbor underlay peer-group
cumulus@leaf01:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf01:~$ net add bgp bestpath as-path multipath-relax
cumulus@leaf01:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf01:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@leaf01:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf01:~$ net add bgp vrf RED autonomous-system 65101
cumulus@leaf01:~$ net add bgp vrf RED router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf01:~$ net add bgp vrf BLUE autonomous-system 65101
cumulus@leaf01:~$ net add bgp vrf BLUE router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf01:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{</tab>}}
{{<tab "leaf02">}}

```
cumulus@leaf02:~$ net add loopback lo ip address 10.10.10.2/32
cumulus@leaf02:~$ net add interface swp1-3,swp51-52
cumulus@leaf02:~$ net add bond bond1 bond slaves swp1
cumulus@leaf02:~$ net add bond bond2 bond slaves swp2
cumulus@leaf02:~$ net add bond bond3 bond slaves swp3
cumulus@leaf02:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf02:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf02:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf02:~$ net add interface swp51-52 alias to spine
cumulus@leaf02:~$ net add bond bond1 bridge access 10
cumulus@leaf02:~$ net add bond bond2 bridge access 20
cumulus@leaf02:~$ net add bond bond3 bridge access 30
cumulus@leaf02:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf02:~$ net add bond bond1-3 mtu 9000
cumulus@leaf02:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf02:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf02:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf02:~$ net add loopback lo pim
cumulus@leaf02:~$ net add pim rp 10.10.100.100 224.0.0.0/4
cumulus@leaf02:~$ net add pim ecmp
cumulus@leaf02:~$ net add pim keep-alive-timer 3600
cumulus@leaf02:~$ net add interface swp51-52 pim
cumulus@leaf02:~$ net add interface swp51-52 evpn mh uplink
cumulus@leaf02:~$ net add evpn mh startup-delay 10
cumulus@leaf02:~$ net add bond bond1 evpn mh es-df-pref 50000
cumulus@leaf02:~$ net add bond bond2 evpn mh es-df-pref 50000
cumulus@leaf02:~$ net add bond bond3 evpn mh es-df-pref 50000
cumulus@leaf02:~$ net add bond bond1 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add bond bond2 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add bond bond3 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add bond bond1 evpn mh es-id 1
cumulus@leaf02:~$ net add bond bond2 evpn mh es-id 2
cumulus@leaf02:~$ net add bond bond3 evpn mh es-id 3
cumulus@leaf02:~$ net add vrf RED vni 4001
cumulus@leaf02:~$ net add vrf BLUE vni 4002
cumulus@leaf02:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf02:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf02:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf02:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf02:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf02:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf02:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf02:~$ net add bridge bridge vlan-aware
cumulus@leaf02:~$ net add vlan 10 ip address 10.1.10.3/24
cumulus@leaf02:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf02:~$ net add vlan 10 vlan-id 10
cumulus@leaf02:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 10 vrf RED
cumulus@leaf02:~$ net add vlan 20 ip address 10.1.20.3/24
cumulus@leaf02:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf02:~$ net add vlan 20 vlan-id 20
cumulus@leaf02:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 20 vrf RED
cumulus@leaf02:~$ net add vlan 30 ip address 10.1.30.3/24
cumulus@leaf02:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf02:~$ net add vlan 30 vlan-id 30
cumulus@leaf02:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 30 vrf BLUE
cumulus@leaf02:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf02:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 4001 vrf RED
cumulus@leaf02:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf02:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf02:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf02:~$ net add vlan 4002 vrf BLUE
cumulus@leaf02:~$ net add vrf BLUE,mgmt,RED vrf-table auto
cumulus@leaf02:~$ net add vxlan vni10 bridge access 10
cumulus@leaf02:~$ net add vxlan vni10 vxlan mcastgrp 224.0.0.10
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf02:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf02:~$ net add vxlan vni20 bridge access 20
cumulus@leaf02:~$ net add vxlan vni20 vxlan mcastgrp 224.0.0.20
cumulus@leaf02:~$ net add vxlan vni30 bridge access 30
cumulus@leaf02:~$ net add vxlan vni30 vxlan mcastgrp 224.0.0.30
cumulus@leaf02:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf02:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf02:~$ net add loopback lo vxlan local-tunnelip 10.10.10.2
cumulus@leaf02:~$ net add evpn mh startup-delay 30
cumulus@leaf02:~$ net add bgp autonomous-system 65102
cumulus@leaf02:~$ net add bgp router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp neighbor underlay peer-group
cumulus@leaf02:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf02:~$ net add bgp bestpath as-path multipath-relax
cumulus@leaf02:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf02:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@leaf02:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf02:~$ net add bgp vrf RED autonomous-system 65102
cumulus@leaf02:~$ net add bgp vrf RED router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf02:~$ net add bgp vrf BLUE autonomous-system 65102
cumulus@leaf02:~$ net add bgp vrf BLUE router-id 10.10.10.2
cumulus@leaf02:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf02:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf02:~$ net pending
cumulus@leaf02:~$ net commit
```

{{</tab>}}
{{<tab "leaf03">}}

```
cumulus@leaf03:~$ net add loopback lo ip address 10.10.10.3/32
cumulus@leaf03:~$ net add interface swp1-3,swp51-52
cumulus@leaf03:~$ net add bond bond1 bond slaves swp1
cumulus@leaf03:~$ net add bond bond2 bond slaves swp2
cumulus@leaf03:~$ net add bond bond3 bond slaves swp3
cumulus@leaf03:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf03:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf03:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf03:~$ net add interface swp51-52 alias to spine
cumulus@leaf03:~$ net add bond bond1 bridge access 10
cumulus@leaf03:~$ net add bond bond2 bridge access 20
cumulus@leaf03:~$ net add bond bond3 bridge access 30
cumulus@leaf03:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf03:~$ net add bond bond1-3 mtu 9000
cumulus@leaf03:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf03:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf03:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf03:~$ net add loopback lo pim
cumulus@leaf03:~$ net add pim rp 10.10.100.100 224.0.0.0/4
cumulus@leaf03:~$ net add pim ecmp
cumulus@leaf03:~$ net add pim keep-alive-timer 3600
cumulus@leaf03:~$ net add interface swp51-52 pim
cumulus@leaf03:~$ net add interface swp51-52 evpn mh uplink
cumulus@leaf03:~$ net add evpn mh startup-delay 10
cumulus@leaf03:~$ net add bond bond1 evpn mh es-df-pref 50000
cumulus@leaf03:~$ net add bond bond2 evpn mh es-df-pref 50000
cumulus@leaf03:~$ net add bond bond3 evpn mh es-df-pref 50000
cumulus@leaf03:~$ net add bond bond1 evpn mh es-sys-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add bond bond2 evpn mh es-sys-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add bond bond3 evpn mh es-sys-mac 44:38:39:BE:EF:BB
cumulus@leaf03:~$ net add bond bond1 evpn mh es-id 1
cumulus@leaf03:~$ net add bond bond2 evpn mh es-id 2
cumulus@leaf03:~$ net add bond bond3 evpn mh es-id 3
cumulus@leaf03:~$ net add vrf RED vni 4001
cumulus@leaf03:~$ net add vrf BLUE vni 4002
cumulus@leaf03:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf03:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf03:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf03:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf03:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf03:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf03:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf03:~$ net add bridge bridge vlan-aware
cumulus@leaf03:~$ net add vlan 10 ip address 10.1.10.4/24
cumulus@leaf03:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf03:~$ net add vlan 10 vlan-id 10
cumulus@leaf03:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 10 vrf RED
cumulus@leaf03:~$ net add vlan 20 ip address 10.1.20.4/24
cumulus@leaf03:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf03:~$ net add vlan 20 vlan-id 20
cumulus@leaf03:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 20 vrf RED
cumulus@leaf03:~$ net add vlan 30 ip address 10.1.30.4/24
cumulus@leaf03:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf03:~$ net add vlan 30 vlan-id 30
cumulus@leaf03:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 30 vrf BLUE
cumulus@leaf03:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf03:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf03:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 4001 vrf RED
cumulus@leaf03:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf03:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf03:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf03:~$ net add vlan 4002 vrf BLUE
cumulus@leaf03:~$ net add vrf BLUE,mgmt,RED vrf-table auto
cumulus@leaf03:~$ net add vxlan vni10 bridge access 10
cumulus@leaf03:~$ net add vxlan vni10 vxlan mcastgrp 224.0.0.10
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf03:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf03:~$ net add vxlan vni20 bridge access 20
cumulus@leaf03:~$ net add vxlan vni20 vxlan mcastgrp 224.0.0.20
cumulus@leaf03:~$ net add vxlan vni30 bridge access 30
cumulus@leaf03:~$ net add vxlan vni30 vxlan mcastgrp 224.0.0.30
cumulus@leaf03:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf03:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf03:~$ net add loopback lo vxlan local-tunnelip 10.10.10.3
cumulus@leaf03:~$ net add evpn mh startup-delay 30
cumulus@leaf03:~$ net add bgp autonomous-system 65103
cumulus@leaf03:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp neighbor underlay peer-group
cumulus@leaf03:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf03:~$ net add bgp bestpath as-path multipath-relax
cumulus@leaf03:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf03:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf03:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@leaf03:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf03:~$ net add bgp vrf RED autonomous-system 65103
cumulus@leaf03:~$ net add bgp vrf RED router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf03:~$ net add bgp vrf BLUE autonomous-system 65103
cumulus@leaf03:~$ net add bgp vrf BLUE router-id 10.10.10.3
cumulus@leaf03:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf03:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf03:~$ net pending
cumulus@leaf03:~$ net commit
```

{{</tab>}}
{{<tab "leaf04">}}

```
cumulus@leaf04:~$ net add loopback lo ip address 10.10.10.4/32
cumulus@leaf04:~$ net add interface swp1-3,swp51-52
cumulus@leaf04:~$ net add bond bond1 bond slaves swp1
cumulus@leaf04:~$ net add bond bond2 bond slaves swp2
cumulus@leaf04:~$ net add bond bond3 bond slaves swp3
cumulus@leaf04:~$ net add interface swp1 alias bond member of bond1
cumulus@leaf04:~$ net add interface swp2 alias bond member of bond2
cumulus@leaf04:~$ net add interface swp3 alias bond member of bond3
cumulus@leaf04:~$ net add interface swp51-52 alias to spine
cumulus@leaf04:~$ net add bond bond1 bridge access 10
cumulus@leaf04:~$ net add bond bond2 bridge access 20
cumulus@leaf04:~$ net add bond bond3 bridge access 30
cumulus@leaf04:~$ net add bond bond1-3 bond lacp-bypass-allow
cumulus@leaf04:~$ net add bond bond1-3 mtu 9000
cumulus@leaf04:~$ net add bond bond1-3 stp bpduguard
cumulus@leaf04:~$ net add bond bond1-3 stp portadminedge
cumulus@leaf04:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@leaf04:~$ net add loopback lo pim
cumulus@leaf04:~$ net add pim rp 10.10.100.100 224.0.0.0/4
cumulus@leaf04:~$ net add pim ecmp
cumulus@leaf04:~$ net add pim keep-alive-timer 3600
cumulus@leaf04:~$ net add interface swp51-52 pim
cumulus@leaf04:~$ net add interface swp51-52 evpn mh uplink
cumulus@leaf04:~$ net add evpn mh startup-delay 10
cumulus@leaf04:~$ net add bond bond1 evpn mh es-df-pref 50000
cumulus@leaf04:~$ net add bond bond2 evpn mh es-df-pref 50000
cumulus@leaf04:~$ net add bond bond3 evpn mh es-df-pref 50000
cumulus@leaf04:~$ net add bond bond1 evpn mh es-sys-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add bond bond2 evpn mh es-sys-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add bond bond3 evpn mh es-sys-mac 44:38:39:BE:EF:BB
cumulus@leaf04:~$ net add bond bond1 evpn mh es-id 1
cumulus@leaf04:~$ net add bond bond2 evpn mh es-id 2
cumulus@leaf04:~$ net add bond bond3 evpn mh es-id 3
cumulus@leaf04:~$ net add vrf RED vni 4001
cumulus@leaf04:~$ net add vrf BLUE vni 4002
cumulus@leaf04:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf04:~$ net add vxlan vni20 vxlan id 20
cumulus@leaf04:~$ net add vxlan vni30 vxlan id 30
cumulus@leaf04:~$ net add vxlan vniBLUE vxlan id 4002
cumulus@leaf04:~$ net add vxlan vniRED vxlan id 4001
cumulus@leaf04:~$ net add bridge bridge ports vni10,vni20,vni30,vniRED,vniBLUE
cumulus@leaf04:~$ net add bridge bridge vids 10,20,30,4001-4002
cumulus@leaf04:~$ net add bridge bridge vlan-aware
cumulus@leaf04:~$ net add vlan 10 ip address 10.1.10.5/24
cumulus@leaf04:~$ net add vlan 10 ip address-virtual 00:00:00:00:00:10 10.1.10.1/24
cumulus@leaf04:~$ net add vlan 10 vlan-id 10
cumulus@leaf04:~$ net add vlan 10 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 10 vrf RED
cumulus@leaf04:~$ net add vlan 20 ip address 10.1.20.5/24
cumulus@leaf04:~$ net add vlan 20 ip address-virtual 00:00:00:00:00:20 10.1.20.1/24
cumulus@leaf04:~$ net add vlan 20 vlan-id 20
cumulus@leaf04:~$ net add vlan 20 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 20 vrf RED
cumulus@leaf04:~$ net add vlan 30 ip address 10.1.30.5/24
cumulus@leaf04:~$ net add vlan 30 ip address-virtual 00:00:00:00:00:30 10.1.30.1/24
cumulus@leaf04:~$ net add vlan 30 vlan-id 30
cumulus@leaf04:~$ net add vlan 30 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 30 vrf BLUE
cumulus@leaf04:~$ net add vlan 4001 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf04:~$ net add vlan 4001 vlan-id 4001
cumulus@leaf04:~$ net add vlan 4001 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 4001 vrf RED
cumulus@leaf04:~$ net add vlan 4002 hwaddress 44:38:39:BE:EF:AA
cumulus@leaf04:~$ net add vlan 4002 vlan-id 4002
cumulus@leaf04:~$ net add vlan 4002 vlan-raw-device bridge
cumulus@leaf04:~$ net add vlan 4002 vrf BLUE
cumulus@leaf04:~$ net add vrf BLUE,mgmt,RED vrf-table auto
cumulus@leaf04:~$ net add vxlan vni10 bridge access 10
cumulus@leaf04:~$ net add vxlan vni10 vxlan mcastgrp 224.0.0.10
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge arp-nd-suppress on
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED bridge learning off
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp bpduguard
cumulus@leaf04:~$ net add vxlan vni10,20,30,vniBLUE,vniRED stp portbpdufilter
cumulus@leaf04:~$ net add vxlan vni20 bridge access 20
cumulus@leaf04:~$ net add vxlan vni20 vxlan mcastgrp 224.0.0.20
cumulus@leaf04:~$ net add vxlan vni30 bridge access 30
cumulus@leaf04:~$ net add vxlan vni30 vxlan mcastgrp 224.0.0.30
cumulus@leaf04:~$ net add vxlan vniBLUE bridge access 4002
cumulus@leaf04:~$ net add vxlan vniRED bridge access 4001
cumulus@leaf04:~$ net add loopback lo vxlan local-tunnelip 10.10.10.4
cumulus@leaf04:~$ net add bgp autonomous-system 65104
cumulus@leaf04:~$ net add bgp router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp neighbor underlay peer-group
cumulus@leaf04:~$ net add bgp neighbor underlay remote-as external
cumulus@leaf04:~$ net add bgp bestpath as-path multipath-relax
cumulus@leaf04:~$ net add bgp neighbor swp51 interface peer-group underlay
cumulus@leaf04:~$ net add bgp neighbor swp52 interface peer-group underlay
cumulus@leaf04:~$ net add bgp ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp l2vpn evpn neighbor underlay activate
cumulus@leaf04:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf04:~$ net add bgp vrf RED autonomous-system 65104
cumulus@leaf04:~$ net add bgp vrf RED router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp vrf RED ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp vrf RED l2vpn evpn  advertise ipv4 unicast
cumulus@leaf04:~$ net add bgp vrf BLUE autonomous-system 65104
cumulus@leaf04:~$ net add bgp vrf BLUE router-id 10.10.10.4
cumulus@leaf04:~$ net add bgp vrf BLUE ipv4 unicast redistribute connected
cumulus@leaf04:~$ net add bgp vrf BLUE l2vpn evpn advertise ipv4 unicast
cumulus@leaf04:~$ net pending
cumulus@leaf04:~$ net commit
```

{{</tab>}}
{{<tab "spine01">}}

```
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net add loopback lo pim
cumulus@spine01:~$ net add loopback lo pim use-source 10.10.10.101
cumulus@spine01:~$ net add interface swp1-4 pim
cumulus@spine01:~$ net add interface swp1-4 alias to leaf
cumulus@spine01:~$ net add pim rp 10.10.100.100 224.0.0.0/4
cumulus@spine01:~$ net add pim ecmp
cumulus@spine01:~$ net add pim keep-alive-timer 3600
cumulus@spine01:~$ net add bgp autonomous-system 65100
cumulus@spine01:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:~$ net add bgp neighbor underlay peer-group
cumulus@spine01:~$ net add bgp neighbor underlay remote-as external
cumulus@spine01:~$ net add bgp bestpath as-path multipath-relax
cumulus@spine01:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine01:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine01:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine01:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{</tab>}}
{{<tab "spine02">}}

```
cumulus@spine02:~$ net add loopback lo ip address 10.10.10.102/32
cumulus@spine02:~$ net add loopback lo pim
cumulus@spine02:~$ net add loopback lo pim use-source 10.10.10.101
cumulus@spine02:~$ net add interface swp1-4 pim
cumulus@spine02:~$ net add interface swp1-4 alias to leaf
cumulus@spine02:~$ net add pim rp 10.10.100.100 224.0.0.0/4
cumulus@spine02:~$ net add pim ecmp
cumulus@spine02:~$ net add pim keep-alive-timer 3600
cumulus@spine02:~$ net add bgp autonomous-system 65100
cumulus@spine02:~$ net add bgp router-id 10.10.10.102
cumulus@spine02:~$ net add bgp neighbor underlay peer-group
cumulus@spine02:~$ net add bgp neighbor underlay remote-as external
cumulus@spine02:~$ net add bgp bestpath as-path multipath-relax
cumulus@spine02:~$ net add bgp neighbor swp1 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp2 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp3 interface peer-group underlay
cumulus@spine02:~$ net add bgp neighbor swp4 interface peer-group underlay
cumulus@spine02:~$ net add bgp ipv4 unicast redistribute connected
cumulus@spine02:~$ net add bgp l2vpn evpn  neighbor underlay activate
cumulus@spine02:~$ net pending
cumulus@spine02:~$ net commit
```

{{</tab>}}
{{</tabs>}}

{{</tab>}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID2698 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-3,swp51-52
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond1 link mtu 9000
cumulus@leaf01:~$ nv set interface bond2 link mtu 9000
cumulus@leaf01:~$ nv set interface bond3 link mtu 9000
cumulus@leaf01:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf01:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf01:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf01:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf01:~$ nv set vrf RED
cumulus@leaf01:~$ nv set vrf BLUE
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ nv set vrf RED evpn vni 4001
cumulus@leaf01:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf01:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set evpn enable on
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:~$ nv set evpn multihoming enable on
cumulus@leaf01:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf01:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf01:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf01:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf01:~$ nv config apply
```

{{</tab>}}
{{<tab "leaf02">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1-3,swp51-52
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf02:~$ nv set interface bond1 link mtu 9000
cumulus@leaf02:~$ nv set interface bond2 link mtu 9000
cumulus@leaf02:~$ nv set interface bond3 link mtu 9000
cumulus@leaf02:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf02:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf02:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf02:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf02:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf02:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf02:~$ nv set vrf RED
cumulus@leaf02:~$ nv set vrf BLUE
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf02:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf02:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf02:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf02:~$ nv set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf02:~$ nv set vrf RED evpn vni 4001
cumulus@leaf02:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf02:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set evpn enable on
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf02:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf02:~$ nv set evpn multihoming enable on
cumulus@leaf02:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf02:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf02:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf02:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf02:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf02:~$ nv config apply
```

{{</tab>}}
{{<tab "leaf03">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1-3,swp51-52
cumulus@leaf03:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:~$ nv set interface bond2 bond member swp2
cumulus@leaf03:~$ nv set interface bond3 bond member swp3
cumulus@leaf03:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf03:~$ nv set interface bond1 link mtu 9000
cumulus@leaf03:~$ nv set interface bond2 link mtu 9000
cumulus@leaf03:~$ nv set interface bond3 link mtu 9000
cumulus@leaf03:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf03:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf03:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf03:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf03:~$ nv set interface vlan10 ip address 10.1.10.4/24
cumulus@leaf03:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf03:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf03:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf03:~$ nv set interface vlan20 ip address 10.1.20.4/24
cumulus@leaf03:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf03:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf03:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf03:~$ nv set interface vlan30 ip address 10.1.30.4/24
cumulus@leaf03:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf03:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf03:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf03:~$ nv set vrf RED
cumulus@leaf03:~$ nv set vrf BLUE
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf03:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf03:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf03:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf03:~$ nv set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf03:~$ nv set vrf RED evpn vni 4001
cumulus@leaf03:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf03:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf03:~$ nv set evpn enable on
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf03:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf03:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf03:~$ nv set evpn multihoming enable on
cumulus@leaf03:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf03:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf03:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf03:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf03:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf03:~$ nv config apply
```

{{</tab>}}
{{<tab "leaf04">}}

```
cumulus@leaf04:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ nv set interface swp1-3,swp51-52
cumulus@leaf04:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:~$ nv set interface bond2 bond member swp2
cumulus@leaf04:~$ nv set interface bond3 bond member swp3
cumulus@leaf04:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf04:~$ nv set interface bond1 link mtu 9000
cumulus@leaf04:~$ nv set interface bond2 link mtu 9000
cumulus@leaf04:~$ nv set interface bond3 link mtu 9000
cumulus@leaf04:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf04:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf04:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf04:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf04:~$ nv set interface vlan10 ip address 10.1.10.5/24
cumulus@leaf04:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf04:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf04:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf04:~$ nv set interface vlan20 ip address 10.1.20.5/24
cumulus@leaf04:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf04:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf04:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf04:~$ nv set interface vlan30 ip address 10.1.30.5/24
cumulus@leaf04:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf04:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf04:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf04:~$ nv set vrf RED
cumulus@leaf04:~$ nv set vrf BLUE
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf04:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf04:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf04:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf04:~$ nv set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf04:~$ nv set vrf RED evpn vni 4001
cumulus@leaf04:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf04:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf04:~$ nv set evpn enable on
cumulus@leaf04:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf04:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf04:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf04:~$ nv set evpn multihoming enable on
cumulus@leaf04:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf04:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf04:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf04:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf04:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf04:~$ nv config apply
```

{{</tab>}}
{{<tab "spine01">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-4
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine01:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine01:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine01:~$ nv config apply
```

{{</tab>}}
{{<tab "spine02">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1-4
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ nv set vrf default router bgp peer swp1 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp2 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp3 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp peer swp4 peer-group underlay
cumulus@spine02:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@spine02:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine02:~$ nv config apply
```

{{</tab>}}
{{</tabs>}}

{{</tab>}}
{{<tab "/etc/network/interfaces">}}

{{< tabs "TabID919 ">}}
{{<tab "leaf01">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.1/32
    vxlan-local-tunnelip 10.10.10.1

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 2
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 3
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10
    vxlan-mcastgrp 224.0.0.10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20
    vxlan-mcastgrp 224.0.0.20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30
    vxlan-mcastgrp 224.0.0.30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "leaf02">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    vxlan-local-tunnelip 10.10.10.2

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.3/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.3/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10
    vxlan-mcastgrp 224.0.0.10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20
    vxlan-mcastgrp 224.0.0.20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30
    vxlan-mcastgrp 224.0.0.30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "leaf03">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.3/32
    vxlan-local-tunnelip 10.10.10.3

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.4/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.4/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.4/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10
    vxlan-mcastgrp 224.0.0.10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20
    vxlan-mcastgrp 224.0.0.20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30
    vxlan-mcastgrp 224.0.0.30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "leaf04">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.4/32
    vxlan-local-tunnelip 10.10.10.4

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:BB
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.5/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.5/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.5/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vni10
iface vni10
    bridge-access 10
    bridge-learning off
    vxlan-id 10
    vxlan-mcastgrp 224.0.0.10

auto vni20
iface vni20
    bridge-access 20
    bridge-learning off
    vxlan-id 20
    vxlan-mcastgrp 224.0.0.20

auto vni30
iface vni30
    bridge-access 30
    bridge-learning off
    vxlan-id 30
    vxlan-mcastgrp 224.0.0.30

auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001

auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220

auto vni4002
iface vni4002
    bridge-access 297
    bridge-learning off
    vxlan-id 4002

auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1

auto br_l3vni
iface br_l3vni
    bridge-ports vni4001 vni4002
    bridge-vlan-aware yes
```

{{</tab>}}
{{<tab "spine01">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.101/32

auto eth0
iface eth0
    vrf mgmt
    address 192.168.200.21/24

auto mgmt
iface mgmt
  vrf-table auto
  address 127.0.0.1/8
  address ::1/128

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

{{</tab>}}
{{<tab "spine02">}}

```
cumulus@spine02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto eth0
iface eth0
    vrf mgmt
    address 192.168.200.22/24

auto mgmt
iface mgmt
  vrf-table auto
  address 127.0.0.1/8
  address ::1/128

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

{{</tab>}}
{{<tab "server01">}}

```
cumulus@server01:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.10.101
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.10.1
```

{{</tab>}}
{{<tab "server02">}}

```
cumulus@server02:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.20.102
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.20.1
```

{{</tab>}}
{{<tab "server03">}}

```
cumulus@server03:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.30.103
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.30.1
```

{{</tab>}}
{{<tab "server04">}}

```
cumulus@server04:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The OOB network interface
auto eth0
iface eth0 inet dhcp

# The data plane network interfaces
auto eth1
iface eth1 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  address 10.1.10.104
  netmask 255.255.255.0
  mtu 9000
  bond-slaves eth1 eth2
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  post-up ip route add 10.0.0.0/8 via 10.1.10.1
```

{{</tab>}}
{{</tabs>}}

{{</tab>}}
{{<tab "/etc/frr/frr.conf">}}

{{< tabs "TabID3846 ">}}
{{<tab "leaf01">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1080
evpn mh neigh-holdtime 1080
evpn mh startup-delay 180
ip pim rp 10.10.100.100 224.0.0.0/4
ip pim ecmp
ip pim keep-alive-timer 3600
interface lo
ip igmp
ip pim
ip pim use-source 10.10.10.1
interface swp51
evpn mh uplink
ip pim
interface swp52
evpn mh uplink
ip pim
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:AA
vrf RED
vni 4001
exit-vrf
vrf BLUE
vni 4002
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
!
router bgp 65101 vrf default
bgp router-id 10.10.10.1
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{<tab "leaf02">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
ip pim rp 10.10.100.100 224.0.0.0/4
evpn mh mac-holdtime 1000
evpn mh neigh-holdtime 600
evpn mh startup-delay 180
interface lo
ip pim
interface swp51
evpn mh uplink
ip pim
interface swp52
evpn mh uplink
ip pim
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:AA
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65102 vrf default
bgp router-id 10.10.10.2
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{<tab "leaf03">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
ip pim rp 10.10.100.100 224.0.0.0/4
evpn mh mac-holdtime 1000
evpn mh neigh-holdtime 600
evpn mh startup-delay 180
interface lo
ip pim
interface swp51
evpn mh uplink
ip pim
interface swp52
evpn mh uplink
ip pim
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:BB
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65103 vrf default
bgp router-id 10.10.10.3
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
```

{{</tab>}}
{{<tab "leaf04">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
ip pim rp 10.10.100.100 224.0.0.0/4
evpn mh mac-holdtime 1000
evpn mh neigh-holdtime 600
evpn mh startup-delay 180
interface lo
ip pim
interface swp51
evpn mh uplink
ip pim
interface swp52
evpn mh uplink
ip pim
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:BB
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:BB
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65104 vrf default
bgp router-id 10.10.10.4
bgp bestpath as-path multipath-relax
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface remote-as external
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface remote-as external
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
```

{{</tab>}}
{{<tab "spine01">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
ip pim rp 10.10.100.100 224.0.0.0/4
ip pim ecmp
ip pim keep-alive-timer 3600
interface lo
ip pim
interface swp1
ip pim
interface swp2
ip pim
interface swp3
ip pim
interface swp4
ip pim
vrf mgmt
ip route 0.0.0.0/0 192.168.200.1
exit-vrf
!
router bgp 65100
bgp router-id 10.10.10.101
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp2 interface peer-group underlay
neighbor swp3 interface peer-group underlay
neighbor swp4 interface peer-group underlay
!
address-family ipv4 unicast
redistribute connected
exit-address-family
!
address-family l2vpn evpn
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{<tab "spine02">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
!
ip pim rp 10.10.100.100 224.0.0.0/4
ip pim ecmp
ip pim keep-alive-timer 3600
interface lo
ip igmp
ip pim
ip pim use-source 10.10.10.102
interface swp1
ip pim
interface swp2
ip pim
interface swp3
ip pim
interface swp4
ip pim
vrf mgmt
ip route 0.0.0.0/0 192.168.200.1
exit-vrf
!
router bgp 65100
bgp router-id 10.10.10.102
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor swp1 interface peer-group underlay
neighbor swp2 interface peer-group underlay
neighbor swp3 interface peer-group underlay
neighbor swp4 interface peer-group underlay
!
address-family ipv4 unicast
redistribute connected
exit-address-family
!
address-family l2vpn evpn
neighbor underlay activate
exit-address-family
!
```

{{</tab>}}
{{</tabs>}}

{{</tab>}}
{{</tabs>}}
