---
title: EVPN Multihoming
author: NVIDIA
weight: 570
toc: 4
---

*EVPN multihoming* (EVPN-MH) provides support for all-active server redundancy. It is a standards-based replacement for MLAG in data centers deploying Clos topologies. Replacing MLAG:

- Eliminates the need for peerlinks or inter-switch links between the top of rack switches
- Allows more than two TOR switches to participate in a redundancy group
- Provides a single BGP-EVPN control plane
- Allows multi-vendor interoperability

EVPN-MH uses {{<link url="#supported-evpn-route-types" text="BGP-EVPN type-1, type-2 and type-4 routes">}} for discovering Ethernet segments (ES) and for forwarding traffic to those Ethernet segments. The MAC and neighbor databases are synced between the Ethernet segment peers via these routes as well. An *{{<exlink url="https://tools.ietf.org/html/rfc7432#section-5" text="Ethernet segment">}}* is a group of switch links that are attached to the same server. Each Ethernet segment has an unique Ethernet segment ID (`es-id`) across the entire PoD.

{{%notice info%}}
EVPN-MH is only supported on Spectrum ASIC based switches.
{{% /notice %}}

Configuring EVPN-MH involves setting an Ethernet segment system MAC address (`es-sys-mac`) and a local Ethernet segment ID (`local-es-id`) on a static or LACP bond. These two parameters are used to automatically generate the unique MAC-based ESI value ({{<exlink url="https://tools.ietf.org/html/rfc7432#section-5" text="type-3">}}):

- The `es-sys-mac` is used for the LACP system identifier.
- The `es-id` configuration defines a local discriminator to uniquely enumerate each bond that shares the same es-sys-mac.
- The resulting 10-byte ESI value has the following format:

      03:MM:MM:MM:MM:MM:MM:XX:XX:XX

  where the MMs denote the 6-byte `es-sys-mac` and the XXs denote the 3-byte `es-id` value.

While you can specify a different `es-sys-mac` on different Ethernet segments attached to the same switch, the `es-sys-mac` must be the same on the downlinks attached to the same server.

{{%notice info%}}
When using Spectrum 2 or Spectrum 3 switches, an Ethernet segment can span more than two switches. Each Ethernet segment is a distinct redundancy group. However, when using Spectrum A1 switches, a maximum of two switches can participate in a redundancy group or Ethernet segment.
{{%/notice%}}

## Required and Supported Features

This section describes features that must be enabled in order to use EVPN multihoming, other supported features and features that are not supported.

### Required Features

The following features must be enabled in order to use EVPN-MH:

- {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge mode">}}
- {{<link url="Basic-Configuration/#arp-and-nd-suppression" text="ARP suppression">}}
- EVPN BUM traffic handling with {{<link title="EVPN BUM Traffic with PIM-SM" text="EVPN-PIM">}} on multihomed sites via Type-4/ESR routes, which includes split-horizon-filtering and designated forwarder election

{{%notice warning%}}
To use EVPN-MH, you must remove any MLAG configuration on the switch:

- Remove the `clag-id` from all interfaces in the `/etc/network/interfaces` file.
- Remove the peerlink interfaces from the `/etc/network/interfaces` file.
- Remove any existing `hwaddress` (from a Cumulus Linux 3.x MLAG configuration) or `address-virtual` (from a Cumulus Linux 4.x MLAG configuration) entries from all SVIs corresponding to a layer 3 VNI in the `/etc/network/interfaces` file.
- Remove any `clagd-vxlan-anycast-ip` configuration in the `/etc/network/interfaces` file.
- Run `sudo ifreload` command to reload the configuration.
{{%/notice%}}

### Other Supported Features

- Known unicast traffic multihoming via type-1/EAD (Ethernet auto discovery) routes and type-2 (non-zero ESI) routes. Includes all-active redundancy via aliasing and support for fast failover.
- {{<link url="LACP-Bypass">}} is supported.
  - When an EVPN-MH bond enters LACP bypass state, BGP stops advertising EVPN type-1 and type-4 routes for that bond. Split-horizon and designated forwarder filters are disabled.
  - When an EVPN-MH bond exits the LACP bypass state, BGP starts advertising EVPN type-1 and type-4 routes for that bond. Split-horizon and designated forwarder filters are enabled.
- EVI (*EVPN virtual instance*). Cumulus Linux supports VLAN-based service only, so the EVI is just a layer 2 VNI.
- Supported {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="ASICs">}} include Mellanox Spectrum A1, Spectrum 2 and Spectrum 3.

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

{{% notice note %}}
- EVPN MH can not coexist in an EVPN network with Broadcom based switches in an MLAG configuration.
- In mixed Broadcom-Spectrum networks EVPN-MH is not supported.
- In networks with all Spectrum based switches, EVPN and MLAG can coexist.
{{% /notice %}}

The following features are not supported with EVPN-MH:
- {{<link url="Traditional-Bridge-Mode" text="Traditional bridge mode">}}
- {{<link url="Inter-subnet-Routing/#asymmetric-routing" text="Distributed asymmetric routing">}}
- Head-end replication; use {{<link title="EVPN BUM Traffic with PIM-SM" text="EVPN-PIM">}} for BUM traffic handling instead
- {{<link url="EVPN-Enhancements/#duplicate-address-detection" text="Duplicate address detection">}}

## Configure EVPN-MH

To configure EVPN-MH, first you need to enable the `evpn.multihoming.enable` variable in `switchd.conf`. Then, you must specify all the following required settings:

- The Ethernet segment ID (`es-id`)
- The Ethernet segment system MAC address (`es-sys-mac`)
- MH Uplinks (`evpn mh uplink`)

These settings are applied to interfaces, typically bonds.

An Ethernet segment configuration has these characteristics:
- The `es-id` is a 24-bit integer (1-16777215).
- Each interface (bond) needs its own `es-id`.
- Static and LACP bonds can be associated with an `es-id`.

A *designated forwarder* (DF) is elected for each Ethernet segment. The DF is responsible for forwarding flooded traffic received via the VXLAN overlay to the locally attached Ethernet segment. We recommend you specify a preference (using the `es-df-pref` option) on an Ethernet segment for the DF election, as this leads to predictable failure scenarios. The EVPN VTEP with the highest `es-df-pref` setting becomes the DF. The `es-df-pref` setting defaults to _32767_.

NCLU generates the EVPN-MH configuration and reloads FRR and `ifupdown2`. The configuration appears in both the `/etc/network/interfaces` file and in `/etc/frr/frr.conf` file.

{{%notice note%}}
When EVPN-MH is enabled, all SVI MAC addresses are advertised as type 2 routes. You no longer need to configure a unique SVI IP address, or configure the BGP EVPN address family with `advertise-svi-ip`.
{{%/notice%}}

### Enable EVPN-MH in switchd

To enable EVPN-MH in `switchd`, set the `evpn.multihoming.enable` variable in `switchd.conf` to _TRUE_, then restart the `switchd` service. The variable is disabled by default.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...

evpn.multihoming.enable = TRUE

...

cumulus@switch:~$ sudo systemctl restart switchd.service
```

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
  bond-slaves swp5
  es-sys-mac 44:38:39:ff:ff:01

interface hostbond2
  bond-slaves swp6
  es-sys-mac 44:38:39:ff:ff:01

interface hostbond3
  bond-slaves swp7
  es-sys-mac 44:38:39:ff:ff:01
```

These commands create the following configuration in the `/etc/frr/frr.conf` file.

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

### Enable Uplink Tracking

When all uplinks go down, the VTEP loses connectivity to the VXLAN overlay. To prevent traffic loss, Cumulus Linux tracks the operational state of the uplink. When all the uplinks are down, the Ethernet segment bonds on the switch are in a protodown or error-disabled state. An MH uplink is any routed interface where locally-encapsulated VXLAN traffic is routed (after encapsulation) or any routed interface receiving VXLAN traffic (before decapsulation) that is decapsulated by the local device.

{{%notice info%}}
Split-horizon and Designated-Forwarder filters are only applied to interfaces configured as MH uplinks.
If you configure EVPN-MH without MH uplinks, BUM traffic might be duplicated or looped back to the same ES where it is received. This can cause MAC flaps or other issues on multihomed devices.
{{%/notice%}}

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

### EVPN MH Global Settings

There are a few global settings for EVPN multihoming you can set, including:

- `mac-holdtime`: MAC hold time, in seconds. This is the duration for which a switch maintains SYNC MAC entries after the Ethernet segment peer's EVPN type-2 route is deleted. During this time, the switch attempts to independently establish reachability of the MAC on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.
- `neigh-holdtime`:  Neighbor entry hold time, in seconds. The duration for which a switch maintains SYNC neigh entries after the Ethernet segment peer's EVPN type-2 route is deleted. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.
- `redirect-off`: **Cumulus VX only.** Disables fast failover of traffic destined to the access port via the VXLAN overlay. This knob only applies to Cumulus VX, since fast failover is only supported on the ASIC.
- `startup-delay`:  Startup delay. The duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. The delay can be between 0 and 216000 seconds. The default is 180 seconds.

To configure a MAC hold time for 1000 seconds, run the following commands:

{{<tabs "MAC hold time">}}
{{<tab "NCLU Commands">}}

    cumulus@switch:~$ net add evpn mh mac-holdtime 1000
    cumulus@switch:~$ net commit

{{</tab>}}
{{<tab "vtysh Commands">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# evpn mh mac-holdtime 1000
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

### Enable FRR Debugging

You can add debug statements to the `/etc/frr/frr.conf` file to debug the Ethernet segments, routes and routing protocols (via Zebra).

{{<tabs "debug">}}
{{<tab "NCLU Commands">}}

To debug Ethernet segments and routes, use the `net add bgp debug evpn mh (es|route)` command. To debug the routing protocols, use `net add evpn mh debug zebra (es|mac|neigh|nh)`.

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

When an Ethernet segment link goes down, the attached VTEP notifies all other VTEPs via a single EAD-ES withdraw. This is done by way of an Ethernet segment bond redirect.

Fast failover also triggers:
- When you reboot a leaf switch or VTEP.
- When there is an uplink failure. When all uplinks are down, the Ethernet segment bonds on the switch are protodowned or error disabled.

### Disable Next Hop Group Sharing in the ASIC

Container sharing for both layer 2 and layer 3 next hop groups is enabled by default when EVPN-MH is configured. These settings are stored in the `evpn.multihoming.shared_l2_groups` and `evpn.multihoming.shared_l3_groups` variables.

Disabling container sharing allows for faster failover when an Ethernet segment link flaps.

To disable either setting, edit `switchd.conf`, set the variable to _FALSE_, then restart the `switchd` service. For example, to disable container sharing for layer 3 next hop groups, do the following:

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

Some third party switch vendors don't advertise EAD-per-EVI routes; they only advertise EAD-per-ES routes. To interoperate with these vendors, you need to disable EAD-per-EVI route advertisements.

To remove the dependency on EAD-per-EVI routes and activate the VTEP upon receiving the EAD-per-ES route, run:

    cumulus@switch:~$ net add bgp l2vpn evpn disable-ead-evi-rx
    cumulus@switch:~$ net commit

To suppress the advertisement of EAD-per-EVI routes, run:

    cumulus@switch:~$ net add bgp l2vpn evpn disable-ead-evi-tx
    cumulus@switch:~$ net commit

## Troubleshooting

You can use the following `net show` commands to troubleshoot your EVPN multihoming configuration.

### Show Ethernet Segment Information

The `net show evpn es` command displays the Ethernet segments across all VNIs.

```
cumulus@switch:~$ net show evpn es
Type: L local, R remote, N non-DF
ESI                            Type ES-IF                 VTEPs
03:44:38:39:ff:ff:01:00:00:01  R    -                     172.0.0.22,172.0.0.23
03:44:38:39:ff:ff:01:00:00:02  LR   hostbond2             172.0.0.22,172.0.0.23
03:44:38:39:ff:ff:01:00:00:03  LR   hostbond3             172.0.0.22,172.0.0.23
03:44:38:39:ff:ff:01:00:00:05  L    hostbond1
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
1002     03:44:38:39:ff:ff:01:00:00:02  L
1002     03:44:38:39:ff:ff:01:00:00:03  L
1002     03:44:38:39:ff:ff:01:00:00:05  L
1001     03:44:38:39:ff:ff:01:00:00:02  L
1001     03:44:38:39:ff:ff:01:00:00:03  L
1001     03:44:38:39:ff:ff:01:00:00:05  L
...
```

### Show BGP Ethernet Segment Information

The `net show bgp l2vpn evpn es` command displays the Ethernet segments across all VNIs learned via type-1 and type-4 routes.

```
cumulus@switch:~$ net show bgp l2vpn evpn es
ES Flags: L local, R remote, I inconsistent
VTEP Flags: E ESR/Type-4, A active nexthop
ESI                            Flags RD                    #VNIs    VTEPs
03:44:38:39:ff:ff:01:00:00:01  LR    172.0.0.9:3            10       172.0.0.10(EA),172.0.0.11(EA)
03:44:38:39:ff:ff:01:00:00:02  LR    172.0.0.9:4            10       172.0.0.10(EA),172.0.0.11(EA)
03:44:38:39:ff:ff:01:00:00:03  LR    172.0.0.9:5            10       172.0.0.10(EA),172.0.0.11(EA)
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
1002     03:44:38:39:ff:ff:01:00:00:01  R     172.0.0.22(EV),172.0.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:02  LR    172.0.0.22(EV),172.0.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:03  LR    172.0.0.22(EV),172.0.0.23(EV)
1002     03:44:38:39:ff:ff:01:00:00:05  L  
1002     03:44:38:39:ff:ff:02:00:00:01  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:02  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1002     03:44:38:39:ff:ff:02:00:00:03  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1001     03:44:38:39:ff:ff:01:00:00:01  R     172.0.0.22(EV),172.0.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:02  LR    172.0.0.22(EV),172.0.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:03  LR    172.0.0.22(EV),172.0.0.23(EV)
1001     03:44:38:39:ff:ff:01:00:00:05  L  
1001     03:44:38:39:ff:ff:02:00:00:01  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:02  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
1001     03:44:38:39:ff:ff:02:00:00:03  R     172.0.0.24(EV),172.0.0.25(EV),172.0.0.26(EV)
...
cumulus@switch:~$
```

### Show EAD Route Types

You can use the `net show bgp l2vpn evpn route` command to view type-1 EAD routes. Just include the `ead` route type option.

```
cumulus@switch:~$ net show bgp l2vpn evpn route type ead
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
*> [1]:[0]:[03:44:38:39:ff:ff:01:00:00:01]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005
*> [1]:[0]:[03:44:38:39:ff:ff:01:00:00:02]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005
*> [1]:[0]:[03:44:38:39:ff:ff:01:00:00:03]:[128]:[0.0.0.0]
                    172.16.0.21                          32768 i
                    ET:8 RT:5556:1005

...

Displayed 198 prefixes (693 paths) (of requested type)
cumulus@switch:~$
```

## Example Configuration

The following example uses the topology illustrated here. It shows one rack for simplicity, but multiple racks can be added to this topology.

{{<img src="/images/cumulus-linux/EVPN-MH-example-config.png">}}

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
net add interface lo,swp1-4 pim
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
net add bond hostbond2 alias Local Node/s leaf01 and Ports swp6 <==> Remote Node/s host02 and Ports swp1
net add bond hostbond2 bridge pvid 1001
net add bond hostbond3 alias Local Node/s leaf01 and Ports swp7 <==> Remote Node/s host03 and Ports swp1
net add bond hostbond3 bridge pvid 1002
net add bond hostbond4 alias Local Node/s leaf01 and Ports swp8 <==> Remote Node/s host04 and Ports swp1
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
net add vxlan vx-1000 vxlan mcastgrp 239.1.1.100
net add vxlan vx-1000-1009,4001-4003 bridge arp-nd-suppress on
net add vxlan vx-1000-1009,4001-4003 bridge learning off
net add vxlan vx-1000-1009,4001-4003 stp bpduguard
net add vxlan vx-1000-1009,4001-4003 stp portbpdufilter
net add vxlan vx-1000-1009,4001-4003 vxlan local-tunnelip 172.16.0.21
net add vxlan vx-1001 bridge access 1001
net add vxlan vx-1001 vxlan mcastgrp 239.1.1.101
net add vxlan vx-1002 bridge access 1002
net add vxlan vx-1002 vxlan mcastgrp 239.1.1.102
net add vxlan vx-1003 bridge access 1003
net add vxlan vx-1003 vxlan mcastgrp 239.1.1.103
net add vxlan vx-1004 bridge access 1004
net add vxlan vx-1004 vxlan mcastgrp 239.1.1.104
net add vxlan vx-1005 bridge access 1005
net add vxlan vx-1005 vxlan mcastgrp 239.1.1.105
net add vxlan vx-1006 bridge access 1006
net add vxlan vx-1006 vxlan mcastgrp 239.1.1.106
net add vxlan vx-1007 bridge access 1007
net add vxlan vx-1007 vxlan mcastgrp 239.1.1.107
net add vxlan vx-1008 bridge access 1008
net add vxlan vx-1008 vxlan mcastgrp 239.1.1.108
net add vxlan vx-1009 bridge access 1009
net add vxlan vx-1009 vxlan mcastgrp 239.1.1.109
net add vxlan vx-4001 bridge access 4001
net add vxlan vx-4002 bridge access 4002
net add vxlan vx-4003 bridge access 4003
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
leaf01(config)# ip pim rp 10.0.0.100 239.1.1.0/24
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
leaf01(config)# interface lo
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
leaf01(config-router-af)# advertise-all-vni
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
net add interface lo,swp1-4 pim
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
net add pim rp 192.0.2.5 239.1.1.0/24
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
net add bgp l2vpn evpn neighbor swp1 activate
net add bgp l2vpn evpn neighbor swp2 activate
net add bgp l2vpn evpn neighbor swp3 activate
net add bgp l2vpn evpn neighbor swp4 activate
net add bgp l2vpn evpn advertise-all-vni
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
net add bond hostbond2 alias Local Node/s leaf02 and Ports swp6 <==> Remote Node/s host02 and Ports swp2
net add bond hostbond2 bridge pvid 1001
net add bond hostbond3 alias Local Node/s leaf02 and Ports swp7 <==> Remote Node/s host03 and Ports swp2
net add bond hostbond3 bridge pvid 1002
net add bond hostbond4 alias Local Node/s leaf02 and Ports swp8 <==> Remote Node/s host04 and Ports swp1
net add bond hostbond1-4 bond lacp-rate 1
net add bridge bridge ports vx-1000,vx-1001,vx-1002,vx-1003,vx-1004,vx-1005,vx-1006,vx-1007,vx-1008,vx-1009,vx-4001,vx-4002,vx-4003,hostbond4,hostbond1,hostbond2,hostbond3
net add bridge bridge pvid 1
net add bridge bridge vids 1000-1009
net add bridge bridge vlan-aware
net add interface eth0 ip address 192.168.0.15/24
net add interface eth0 ip gateway 192.168.0.2
net add interface eth0 vrf mgmt
net add interface swp1 alias Local Node leaf02 and Ports swp1 <==> Remote Node/s spine01 and Ports swp3
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
net add vxlan vx-1000 vxlan mcastgrp 239.1.1.100
net add vxlan vx-1000-1009,4001-4003 bridge arp-nd-suppress on
net add vxlan vx-1000-1009,4001-4003 bridge learning off
net add vxlan vx-1000-1009,4001-4003 stp bpduguard
net add vxlan vx-1000-1009,4001-4003 stp portbpdufilter
net add vxlan vx-1000-1009,4001-4003 vxlan local-tunnelip 172.16.0.22
net add vxlan vx-1001 bridge access 1001
net add vxlan vx-1001 vxlan mcastgrp 239.1.1.101
net add vxlan vx-1002 bridge access 1002
net add vxlan vx-1002 vxlan mcastgrp 239.1.1.102
net add vxlan vx-1003 bridge access 1003
net add vxlan vx-1003 vxlan mcastgrp 239.1.1.103
net add vxlan vx-1004 bridge access 1004
net add vxlan vx-1004 vxlan mcastgrp 239.1.1.104
net add vxlan vx-1005 bridge access 1005
net add vxlan vx-1005 vxlan mcastgrp 239.1.1.105
net add vxlan vx-1006 bridge access 1006
net add vxlan vx-1006 vxlan mcastgrp 239.1.1.106
net add vxlan vx-1007 bridge access 1007
net add vxlan vx-1007 vxlan mcastgrp 239.1.1.107
net add vxlan vx-1008 bridge access 1008
net add vxlan vx-1008 vxlan mcastgrp 239.1.1.108
net add vxlan vx-1009 bridge access 1009
net add vxlan vx-1009 vxlan mcastgrp 239.1.1.109
net add vxlan vx-4001 bridge access 4001
net add vxlan vx-4002 bridge access 4002
net add vxlan vx-4003 bridge access 4003
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
cumulus@leaf02:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

leaf02# configure terminal
leaf02(config)# hostname leaf02
leaf02(config)# log file /var/log/frr/bgpd.log
leaf02(config)# log timestamp precision 6
leaf02(config)# evpn mh startup-delay 30
leaf02(config)# ip forwarding
leaf02(config)# ip pim rp 10.0.0.100 239.1.1.0/24
leaf02(config)# ip pim spt-switchover infinity-and-beyond
leaf02(config)# debug bgp evpn mh es
leaf02(config)# debug bgp evpn mh route
leaf02(config)# debug bgp zebra
leaf02(config)# debug bgp updates
leaf02(config)# debug zebra evpn mh es
leaf02(config)# debug zebra evpn mh mac
leaf02(config)# debug zebra evpn mh neigh
leaf02(config)# debug zebra evpn mh nh
leaf02(config)# debug zebra mlag
leaf02(config)# debug zebra vxlan
leaf02(config)# debug zebra kernel
leaf02(config)# debug zebra events
leaf02(config)# debug pim vxlan
leaf02(config)# debug pim mlag
leaf02(config)# debug pim nht
leaf02(config)# debug pim events
leaf02(config)# debug pim zebra
leaf02(config)# debug pim packets register
leaf02(config)# debug pim packets joins
leaf02(config)# debug pim trace
leaf02(config)# debug mroute
leaf02(config)# debug mroute detail
leaf02(config)# debug msdp events
leaf02(config)# no debug zebra kernel
leaf02(config)# no debug zebra events
leaf02(config)# no debug bgp updates
leaf02(config)# no debug pim events
leaf02(config)# no debug pim zebra
leaf02(config)# no debug pim packets register
leaf02(config)# no debug pim packets joins
leaf02(config)# no debug pim vxlan
leaf02(config)# no debug pim mlag
leaf02(config)# no debug pim nht
leaf02(config)# no debug pim trace
leaf02(config)# no debug mroute
leaf02(config)# no debug mroute detail
leaf02(config)# no debug zebra mlag
leaf02(config)# no debug msdp events
leaf02(config)# enable password cn321
leaf02(config)# password cn321
leaf02(config)# vrf vrf1
leaf02(config-vrf)# vni 4001
leaf02(config-vrf)# exit-vrf
leaf02(config)# vrf vrf2
leaf02(config-vrf)# vni 4002
leaf02(config-vrf)# exit-vrf
leaf02(config)# vrf vrf3
leaf02(config-vrf)# vni 4003
leaf02(config-vrf)# exit-vrf
leaf02(config)# interface hostbond1
leaf02(config-if)# evpn mh es-id 1
leaf02(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf02(config-if)# exit
leaf02(config)# interface hostbond2
leaf02(config-if)# evpn mh es-id 2
leaf02(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf02(config-if)# exit
leaf02(config)# interface hostbond3
leaf02(config-if)# evpn mh es-id 3
leaf02(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf02(config-if)# exit
leaf02(config)# interface lo
leaf02(config-if)# ip pim
leaf02(config-if)# exit
leaf02(config)# interface swp1
leaf02(config-if)# evpn mh uplink
leaf02(config-if)# ip pim
leaf02(config-if)# exit
leaf02(config)# interface swp2
leaf02(config-if)# evpn mh uplink
leaf02(config-if)# ip pim
leaf02(config-if)# exit
leaf02(config)# interface swp3
leaf02(config-if)# evpn mh uplink
leaf02(config-if)# ip pim
leaf02(config-if)# exit
leaf02(config)# interface swp4
leaf02(config-if)# evpn mh uplink
leaf02(config-if)# ip pim
leaf02(config-if)# exit
leaf02(config)# router bgp 5557
leaf02(config-router)# bgp router-id 172.16.0.22
leaf02(config-router)# bgp bestpath as-path multipath-relax
leaf02(config-router)# neighbor swp1 interface v6only remote-as external
leaf02(config-router)# neighbor swp2 interface v6only remote-as external
leaf02(config-router)# neighbor swp3 interface v6only remote-as external
leaf02(config-router)# neighbor swp4 interface v6only remote-as external
leaf02(config-router)# address-family ipv4 unicast
leaf02(config-router-af)# address-family ipv4 unicast
leaf02(config-router-af)# exit-address-family
leaf02(config-router)# address-family ipv6 unicast
leaf02(config-router-af)# redistribute connected
leaf02(config-router-af)# neighbor swp1 activate
leaf02(config-router-af)# neighbor swp2 activate
leaf02(config-router-af)# neighbor swp3 activate
leaf02(config-router-af)# neighbor swp4 activate
leaf02(config-router-af)# exit-address-family
leaf02(config-router)# address-family l2vpn evpn
leaf02(config-router-af)# neighbor swp1 activate
leaf02(config-router-af)# neighbor swp2 activate
leaf02(config-router-af)# neighbor swp3 activate
leaf02(config-router-af)# neighbor swp4 activate
leaf02(config-router-af)# advertise-all-vni
leaf02(config-router-af)# exit-address-family
leaf02(config-router)# exit
leaf02(config)# line vty
leaf02(config-line)# exec-timeout 0 0
leaf02(config-line)# exit
leaf02(config)# write memory
leaf02(config)# exit
leaf02# exit
cumulus@leaf02:~$
```

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
net add interface lo,swp1-4 pim
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
net add pim rp 192.0.2.5 239.1.1.0/24
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
net add bond hostbond2 alias Local Node/s leaf03 and Ports swp6 <==> Remote Node/s host02 and Ports swp3
net add bond hostbond2 bridge pvid 1001
net add bond hostbond3 alias Local Node/s leaf03 and Ports swp7 <==> Remote Node/s host03 and Ports swp3
net add bond hostbond3 bridge pvid 1002
net add bond hostbond4 alias Local Node/s leaf03 and Ports swp8 <==> Remote Node/s host04 and Ports swp1
net add bridge bridge ports vx-1000,vx-1001,vx-1002,vx-1003,vx-1004,vx-1005,vx-1006,vx-1007,vx-1008,vx-1009,vx-4001,vx-4002,vx-4003,hostbond4,hostbond1,hostbond2,hostbond3
net add bridge bridge pvid 1
net add bridge bridge vids 1000-1009
net add bridge bridge vlan-aware
net add interface eth0 ip address 192.168.0.15/24
net add interface eth0 ip gateway 192.168.0.2
net add interface eth0 vrf mgmt
net add interface swp1 alias Local Node leaf03 and Ports swp1 <==> Remote Node/s spine01 and Ports swp5
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
net add vxlan vx-1000 vxlan mcastgrp 239.1.1.100
net add vxlan vx-1000-1009,4001-4003 bridge arp-nd-suppress on
net add vxlan vx-1000-1009,4001-4003 bridge learning off
net add vxlan vx-1000-1009,4001-4003 stp bpduguard
net add vxlan vx-1000-1009,4001-4003 stp portbpdufilter
net add vxlan vx-1000-1009,4001-4003 vxlan local-tunnelip 172.16.0.23
net add vxlan vx-1001 bridge access 1001
net add vxlan vx-1001 vxlan mcastgrp 239.1.1.101
net add vxlan vx-1002 bridge access 1002
net add vxlan vx-1002 vxlan mcastgrp 239.1.1.102
net add vxlan vx-1003 bridge access 1003
net add vxlan vx-1003 vxlan mcastgrp 239.1.1.103
net add vxlan vx-1004 bridge access 1004
net add vxlan vx-1004 vxlan mcastgrp 239.1.1.104
net add vxlan vx-1005 bridge access 1005
net add vxlan vx-1005 vxlan mcastgrp 239.1.1.105
net add vxlan vx-1006 bridge access 1006
net add vxlan vx-1006 vxlan mcastgrp 239.1.1.106
net add vxlan vx-1007 bridge access 1007
net add vxlan vx-1007 vxlan mcastgrp 239.1.1.107
net add vxlan vx-1008 bridge access 1008
net add vxlan vx-1008 vxlan mcastgrp 239.1.1.108
net add vxlan vx-1009 bridge access 1009
net add vxlan vx-1009 vxlan mcastgrp 239.1.1.109
net add vxlan vx-4001 bridge access 4001
net add vxlan vx-4002 bridge access 4002
net add vxlan vx-4003 bridge access 4003
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
cumulus@leaf03:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

leaf03# configure terminal
leaf03(config)# hostname leaf03
leaf03(config)# log file /var/log/frr/zebra.log
leaf03(config)# log file /var/log/frr/bgpd.log
leaf03(config)# log timestamp precision 6
leaf03(config)# evpn mh startup-delay 30
leaf03(config)# ip forwarding
leaf03(config)# ip pim rp 10.0.0.100 239.1.1.0/24
leaf03(config)# ip pim spt-switchover infinity-and-beyond
leaf03(config)# debug bgp zebra
leaf03(config)# debug zebra vxlan
leaf03(config)# debug zebra kernel
leaf03(config)# debug zebra events
leaf03(config)# debug bgp updates
leaf03(config)# debug pim vxlan
leaf03(config)# debug pim mlag
leaf03(config)# debug pim nht
leaf03(config)# debug pim events
leaf03(config)# debug pim zebra
leaf03(config)# debug pim packets register
leaf03(config)# debug pim packets joins
leaf03(config)# debug pim trace
leaf03(config)# debug mroute
leaf03(config)# debug mroute detail
leaf03(config)# debug zebra mlag
leaf03(config)# debug msdp events
leaf03(config)# debug bgp evpn mh es
leaf03(config)# debug bgp evpn mh route
leaf03(config)# debug zebra evpn mh es
leaf03(config)# debug zebra evpn mh mac
leaf03(config)# debug zebra evpn mh neigh
leaf03(config)# debug zebra evpn mh nh
leaf03(config)# no debug zebra kernel
leaf03(config)# no debug zebra events
leaf03(config)# no debug bgp updates
leaf03(config)# no debug pim events
leaf03(config)# no debug pim zebra
leaf03(config)# no debug pim packets register
leaf03(config)# no debug pim packets joins
leaf03(config)# no debug pim vxlan
leaf03(config)# no debug pim mlag
leaf03(config)# no debug pim nht
leaf03(config)# no debug pim trace
leaf03(config)# no debug mroute
leaf03(config)# no debug mroute detail
leaf03(config)# no debug zebra mlag
leaf03(config)# no debug msdp events
leaf03(config)# enable password cn321
leaf03(config)# password cn321
leaf03(config)# vrf vrf1
leaf03(config-vrf)# vni 4001
leaf03(config-vrf)# exit-vrf
leaf03(config)# vrf vrf2
leaf03(config-vrf)# vni 4002
leaf03(config-vrf)# exit-vrf
leaf03(config)# vrf vrf3
leaf03(config-vrf)# vni 4003
leaf03(config-vrf)# exit-vrf
leaf03(config)# interface hostbond1
leaf03(config-if)# evpn mh es-id 1
leaf03(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf03(config-if)# exit
leaf03(config)# interface hostbond2
leaf03(config-if)# evpn mh es-id 2
leaf03(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf03(config-if)# exit
leaf03(config)# interface hostbond3
leaf03(config-if)# evpn mh es-id 3
leaf03(config-if)# evpn mh es-sys-mac 44:38:39:ff:ff:01
leaf03(config-if)# exit
leaf03(config)# interface lo
leaf03(config-if)# ip pim
leaf03(config-if)# exit
leaf03(config)# interface swp1
leaf03(config-if)# evpn mh uplink
leaf03(config-if)# ip pim
leaf03(config-if)# exit
leaf03(config)# interface swp2
leaf03(config-if)# evpn mh uplink
leaf03(config-if)# ip pim
leaf03(config-if)# exit
leaf03(config)# interface swp3
leaf03(config-if)# evpn mh uplink
leaf03(config-if)# ip pim
leaf03(config-if)# exit
leaf03(config)# interface swp4
leaf03(config-if)# evpn mh uplink
leaf03(config-if)# ip pim
leaf03(config-if)# exit
leaf03(config)# router bgp 5557
leaf03(config-router)# bgp router-id 172.16.0.22
leaf03(config-router)# bgp bestpath as-path multipath-relax
leaf03(config-router)# neighbor swp1 interface v6only remote-as external
leaf03(config-router)# neighbor swp2 interface v6only remote-as external
leaf03(config-router)# neighbor swp3 interface v6only remote-as external
leaf03(config-router)# neighbor swp4 interface v6only remote-as external
leaf03(config-router)# address-family ipv4 unicast
leaf03(config-router-af)# address-family ipv4 unicast
leaf03(config-router-af)# redistribute connected
leaf03(config-router-af)# exit-address-family
leaf03(config-router)# address-family ipv6 unicast
leaf03(config-router-af)# redistribute connected
leaf03(config-router-af)# neighbor swp1 activate
leaf03(config-router-af)# neighbor swp2 activate
leaf03(config-router-af)# neighbor swp3 activate
leaf03(config-router-af)# neighbor swp4 activate
leaf03(config-router-af)# exit-address-family
leaf03(config-router)# address-family l2vpn evpn
leaf03(config-router-af)# neighbor swp1 activate
leaf03(config-router-af)# neighbor swp2 activate
leaf03(config-router-af)# neighbor swp3 activate
leaf03(config-router-af)# neighbor swp4 activate
leaf03(config-router-af)# advertise-all-vni
leaf03(config-router-af)# exit-address-family
leaf03(config-router)# exit
leaf03(config)# line vty
leaf03(config-line)# exec-timeout 0 0
leaf03(config-line)# exit
leaf03(config)# write memory
leaf03(config)# exit
leaf03# exit
cumulus@leaf03:~$
```

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
net add interface lo,swp1-6 pim
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
net add pim rp 192.0.2.5 239.1.1.0/24
net add pim spt-switchover infinity-and-beyond
net add bgp bestpath as-path multipath-relax
net add bgp router-id 172.16.0.17
net add bgp neighbor swp1 interface v6only remote-as external
net add bgp neighbor swp2 interface v6only remote-as external
net add bgp neighbor swp3 interface v6only remote-as external
net add bgp neighbor swp4 interface v6only remote-as external
net add bgp neighbor swp5 interface v6only remote-as external
net add bgp neighbor swp6 interface v6only remote-as external
net add bgp ipv4 unicast redistribute connected
net add bgp ipv4 unicast neighbor swp1 allowas-in origin
net add bgp ipv4 unicast neighbor swp2 allowas-in origin
net add bgp ipv4 unicast neighbor swp3 allowas-in origin
net add bgp ipv4 unicast neighbor swp4 allowas-in origin
net add bgp ipv4 unicast neighbor swp5 allowas-in origin
net add bgp ipv4 unicast neighbor swp6 allowas-in origin
net add bgp ipv6 unicast redistribute connected
net add bgp ipv6 unicast neighbor swp1 activate
net add bgp ipv6 unicast neighbor swp2 activate
net add bgp ipv6 unicast neighbor swp3 activate
net add bgp ipv6 unicast neighbor swp4 activate
net add bgp ipv6 unicast neighbor swp5 activate
net add bgp ipv6 unicast neighbor swp6 activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp5 activate
net add bgp l2vpn evpn  neighbor swp6 activate
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
net add interface swp2 alias Local Node spine01 and Ports swp2 <==> Remote Node/s leaf01 and Ports swp2
net add interface swp3 alias Local Node spine01 and Ports swp3 <==> Remote Node/s leaf02 and Ports swp1
net add interface swp4 alias Local Node spine01 and Ports swp4 <==> Remote Node/s leaf02 and Ports swp2
net add interface swp5 alias Local Node spine01 and Ports swp5 <==> Remote Node/s leaf03 and Ports swp1
net add interface swp6 alias Local Node spine01 and Ports swp6 <==> Remote Node/s leaf03 and Ports swp2
net add loopback lo alias MSDP Anycast PIM-SM RP
net add loopback lo ip address 172.16.0.17/32
net add loopback lo ip address 10.0.0.100/32
net add vrf mgmt ip address 172.16.0.1/8
net add vrf mgmt ipv6 address ::1/128
net add vrf mgmt vrf-table auto
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
cumulus@spine01:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

spine01# configure terminal
spine01(config)# hostname spine01
spine01(config)# log file /var/log/frr/zebra.log
spine01(config)# log file /var/log/frr/bgpd.log
spine01(config)# log timestamp precision 6
spine01(config)# ip forwarding
spine01(config)# ip pim rp 10.0.0.100 239.1.1.0/24
spine01(config)# ip pim spt-switchover infinity-and-beyond
spine01(config)# ip msdp mesh-group cumulus member 172.16.0.18
spine01(config)# ip msdp mesh-group cumulus source 172.16.0.17
spine01(config)# debug bgp zebra
spine01(config)# debug zebra vxlan
spine01(config)# debug zebra kernel
spine01(config)# debug zebra events
spine01(config)# debug bgp updates
spine01(config)# debug pim events
spine01(config)# debug pim zebra
spine01(config)# debug pim packets register
spine01(config)# debug pim packets joins
spine01(config)# debug pim vxlan
spine01(config)# debug pim mlag
spine01(config)# debug pim nht
spine01(config)# debug pim trace
spine01(config)# debug mroute
spine01(config)# debug mroute detail
spine01(config)# debug zebra mlag
spine01(config)# debug msdp events
spine01(config)# enable password cn321
spine01(config)# password cn321
spine01(config)# vrf vrf1
spine01(config-vrf)# vni 4001
spine01(config-vrf)# exit-vrf
spine01(config)# vrf vrf2
spine01(config-vrf)# vni 4002
spine01(config-vrf)# exit-vrf
spine01(config)# vrf vrf3
spine01(config-vrf)# vni 4003
spine01(config-vrf)# exit-vrf
spine01(config)# interface lo
spine01(config-if)# ip pim
spine01(config-if)# ip pim use-source 10.0.0.100
spine01(config-if)# exit
spine01(config)# interface swp1
spine01(config-if)# ip pim
spine01(config-if)# exit
spine01(config)# interface swp2
spine01(config-if)# ip pim
spine01(config-if)# exit
spine01(config)# interface swp3
spine01(config-if)# ip pim
spine01(config-if)# exit
spine01(config)# interface swp4
spine01(config-if)# ip pim
spine01(config-if)# exit
spine01(config)# interface swp5
spine01(config-if)# ip pim
spine01(config-if)# exit
spine01(config)# interface swp6
spine01(config-if)# ip pim
spine01(config-if)# exit
spine01(config)# router bgp 4435
spine01(config-router)# bgp router-id 172.16.0.17
spine01(config-router)# bgp bestpath as-path multipath-relax
spine01(config-router)# neighbor swp1 interface v6only remote-as external
spine01(config-router)# neighbor swp2 interface v6only remote-as external
spine01(config-router)# neighbor swp3 interface v6only remote-as external
spine01(config-router)# neighbor swp4 interface v6only remote-as external
spine01(config-router)# neighbor swp5 interface v6only remote-as external
spine01(config-router)# neighbor swp6 interface v6only remote-as external
spine01(config-router)# address-family ipv4 unicast
spine01(config-router-af)# address-family ipv4 unicast
spine01(config-router-af)# redistribute connected
spine01(config-router-af)# neighbor swp1 allowas-in origin
spine01(config-router-af)# neighbor swp2 allowas-in origin
spine01(config-router-af)# neighbor swp3 allowas-in origin
spine01(config-router-af)# neighbor swp4 allowas-in origin
spine01(config-router-af)# neighbor swp5 allowas-in origin
spine01(config-router-af)# neighbor swp6 allowas-in origin
spine01(config-router-af)# exit-address-family
spine01(config-router)# address-family ipv6 unicast
spine01(config-router-af)# redistribute connected
spine01(config-router-af)# neighbor swp1 activate
spine01(config-router-af)# neighbor swp2 activate
spine01(config-router-af)# neighbor swp3 activate
spine01(config-router-af)# neighbor swp4 activate
spine01(config-router-af)# neighbor swp5 activate
spine01(config-router-af)# neighbor swp6 activate
spine01(config-router-af)# exit-address-family
spine01(config-router)# address-family l2vpn evpn
spine01(config-router-af)# neighbor swp1 activate
spine01(config-router-af)# neighbor swp2 activate
spine01(config-router-af)# neighbor swp3 activate
spine01(config-router-af)# neighbor swp4 activate
spine01(config-router-af)# neighbor swp5 activate
spine01(config-router-af)# neighbor swp6 activate
spine01(config-router-af)# advertise-all-vni
spine01(config-router-af)# exit-address-family
spine01(config-router)# exit
spine01(config)# line vty
spine01(config-line)# exec-timeout 0 0
spine01(config-line)# exit
spine01(config)# write memory
spine01(config)# exit
spine01# exit
cumulus@spine01:~$
```

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
net add interface lo,swp1-6 pim
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
net add pim rp 192.0.2.5 239.1.1.0/24
net add pim spt-switchover infinity-and-beyond
net add bgp bestpath as-path multipath-relax
net add bgp router-id 172.16.0.18
net add bgp neighbor swp1 interface v6only remote-as external
net add bgp neighbor swp2 interface v6only remote-as external
net add bgp neighbor swp3 interface v6only remote-as external
net add bgp neighbor swp4 interface v6only remote-as external
net add bgp neighbor swp5 interface v6only remote-as external
net add bgp neighbor swp6 interface v6only remote-as external
net add bgp ipv4 unicast redistribute connected
net add bgp ipv4 unicast neighbor swp1 allowas-in origin
net add bgp ipv4 unicast neighbor swp2 allowas-in origin
net add bgp ipv4 unicast neighbor swp3 allowas-in origin
net add bgp ipv4 unicast neighbor swp4 allowas-in origin
net add bgp ipv4 unicast neighbor swp5 allowas-in origin
net add bgp ipv4 unicast neighbor swp6 allowas-in origin
net add bgp ipv6 unicast redistribute connected
net add bgp ipv6 unicast neighbor swp1 activate
net add bgp ipv6 unicast neighbor swp2 activate
net add bgp ipv6 unicast neighbor swp3 activate
net add bgp ipv6 unicast neighbor swp4 activate
net add bgp ipv6 unicast neighbor swp5 activate
net add bgp ipv6 unicast neighbor swp6 activate
net add bgp l2vpn evpn  neighbor swp1 activate
net add bgp l2vpn evpn  neighbor swp2 activate
net add bgp l2vpn evpn  neighbor swp3 activate
net add bgp l2vpn evpn  neighbor swp4 activate
net add bgp l2vpn evpn  neighbor swp5 activate
net add bgp l2vpn evpn  neighbor swp6 activate
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
net add interface swp2 alias Local Node spine02 and Ports swp2 <==> Remote Node/s leaf01 and Ports swp4
net add interface swp3 alias Local Node spine02 and Ports swp3 <==> Remote Node/s leaf02 and Ports swp3
net add interface swp4 alias Local Node spine02 and Ports swp4 <==> Remote Node/s leaf02 and Ports swp4
net add interface swp5 alias Local Node spine02 and Ports swp5 <==> Remote Node/s leaf03 and Ports swp3
net add interface swp6 alias Local Node spine02 and Ports swp6 <==> Remote Node/s leaf03 and Ports swp4
net add loopback lo alias MSDP Anycast PIM-SM RP
net add loopback lo ip address 172.16.0.18/32
net add loopback lo ip address 10.0.0.100/32
net add vrf mgmt ip address 172.16.0.1/8
net add vrf mgmt ipv6 address ::1/128
net add vrf mgmt vrf-table auto
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
cumulus@spine02:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

spine02# configure terminal
spine02(config)# hostname spine02
spine02(config)# log file /var/log/frr/zebra.log
spine02(config)# log file /var/log/frr/bgpd.log
spine02(config)# log timestamp precision 6
spine02(config)# ip forwarding
spine02(config)# ip pim rp 10.0.0.100 239.1.1.0/24
spine02(config)# ip pim spt-switchover infinity-and-beyond
spine02(config)# ip msdp mesh-group cumulus member 172.16.0.17
spine02(config)# ip msdp mesh-group cumulus source 172.16.0.18
spine02(config)# debug bgp zebra
spine02(config)# debug zebra vxlan
spine02(config)# debug zebra kernel
spine02(config)# debug zebra events
spine02(config)# debug bgp updates
spine02(config)# debug pim events
spine02(config)# debug pim zebra
spine02(config)# debug pim packets register
spine02(config)# debug pim packets joins
spine02(config)# debug pim vxlan
spine02(config)# debug pim mlag
spine02(config)# debug pim nht
spine02(config)# debug pim trace
spine02(config)# debug mroute
spine02(config)# debug mroute detail
spine02(config)# debug zebra mlag
spine02(config)# debug msdp events
spine02(config)# enable password cn321
spine02(config)# password cn321
spine02(config)# vrf vrf1
spine02(config-vrf)# vni 4001
spine02(config-vrf)# exit-vrf
spine02(config)# vrf vrf2
spine02(config-vrf)# vni 4002
spine02(config-vrf)# exit-vrf
spine02(config)# vrf vrf3
spine02(config-vrf)# vni 4003
spine02(config-vrf)# exit-vrf
spine02(config)# interface lo
spine02(config-if)# ip pim
spine02(config-if)# ip pim use-source 10.0.0.100
spine02(config-if)# exit
spine02(config)# interface swp1
spine02(config-if)# ip pim
spine02(config-if)# exit
spine02(config)# interface swp2
spine02(config-if)# ip pim
spine02(config-if)# exit
spine02(config)# interface swp3
spine02(config-if)# ip pim
spine02(config-if)# exit
spine02(config)# interface swp4
spine02(config-if)# ip pim
spine02(config-if)# exit
spine02(config)# interface swp5
spine02(config-if)# ip pim
spine02(config-if)# exit
spine02(config)# interface swp6
spine02(config-if)# ip pim
spine02(config-if)# exit
spine02(config)# router bgp 4435
spine02(config-router)# bgp router-id 172.16.0.18
spine02(config-router)# bgp bestpath as-path multipath-relax
spine02(config-router)# neighbor swp1 interface v6only remote-as external
spine02(config-router)# neighbor swp2 interface v6only remote-as external
spine02(config-router)# neighbor swp3 interface v6only remote-as external
spine02(config-router)# neighbor swp4 interface v6only remote-as external
spine02(config-router)# neighbor swp5 interface v6only remote-as external
spine02(config-router)# neighbor swp6 interface v6only remote-as external
spine02(config-router)# address-family ipv4 unicast
spine02(config-router-af)# address-family ipv4 unicast
spine02(config-router-af)# redistribute connected
spine02(config-router-af)# neighbor swp1 allowas-in origin
spine02(config-router-af)# neighbor swp2 allowas-in origin
spine02(config-router-af)# neighbor swp3 allowas-in origin
spine02(config-router-af)# neighbor swp4 allowas-in origin
spine02(config-router-af)# neighbor swp5 allowas-in origin
spine02(config-router-af)# neighbor swp6 allowas-in origin
spine02(config-router-af)# exit-address-family
spine02(config-router)# address-family ipv6 unicast
spine02(config-router-af)# redistribute connected
spine02(config-router-af)# neighbor swp1 activate
spine02(config-router-af)# neighbor swp2 activate
spine02(config-router-af)# neighbor swp3 activate
spine02(config-router-af)# neighbor swp4 activate
spine02(config-router-af)# neighbor swp5 activate
spine02(config-router-af)# neighbor swp6 activate
spine02(config-router-af)# exit-address-family
spine02(config-router)# address-family l2vpn evpn
spine02(config-router-af)# neighbor swp1 activate
spine02(config-router-af)# neighbor swp2 activate
spine02(config-router-af)# neighbor swp3 activate
spine02(config-router-af)# neighbor swp4 activate
spine02(config-router-af)# neighbor swp5 activate
spine02(config-router-af)# neighbor swp6 activate
spine02(config-router-af)# advertise-all-vni
spine02(config-router-af)# exit-address-family
spine02(config-router)# exit
spine02(config)# line vty
spine02(config-line)# exec-timeout 0 0
spine02(config-line)# exit
spine02(config)# write memory
spine02(config)# exit
spine02# exit
cumulus@spine02:~$
```

{{</tab>}}
{{</tabs>}}

### /etc/network/interfaces

If you are using the {{<link title="#Configuration Commands" text="NCLU commands">}} listed above, they create the following configurations in the `/etc/network/interfaces` files for the leaf and spine switches.

If you are not using NCLU and are configuring the topology on the command line, do the following:

1. For the leaf and spine switch configurations, edit the `daemons` file to enable `pimd` (change *no* to *yes*):

       cumulus@switch:~$ sudo nano /etc/frr/daemons

       ...
       pimd=yes
       ...

1. Copy the configurations below to the appropriate switches or servers.

1. For the leaf and spine switch configurations, reload the new configuration by running `ifreload -a`:

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
    alias Local Node leaf01 and Ports swp1 <==> Remote  Node/s spine01 and Ports swp1

auto swp2
iface swp2
    alias Local Node leaf01 and Ports swp2 <==> Remote  Node/s spine01 and Ports swp2

auto swp3
iface swp3
    alias Local Node leaf01 and Ports swp3 <==> Remote  Node/s spine02 and Ports swp1

auto swp4
iface swp4
    alias Local Node leaf01 and Ports swp4 <==> Remote  Node/s spine02 and Ports swp2

auto swp5
iface swp5

auto swp6
iface swp6

auto swp7
iface swp7

auto swp8
iface swp8

auto hostbond1
iface hostbond1
    bond-slaves swp5
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf01 and Ports swp5 <==> Remote  Node/s host01 and Ports swp1
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1000

auto hostbond2
iface hostbond2
    bond-slaves swp6
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf01 and Ports swp6 <==> Remote  Node/s host02 and Ports swp1
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1001

auto hostbond3
iface hostbond3
    bond-slaves swp7
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf01 and Ports swp7 <==> Remote  Node/s host03 and Ports swp1
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1002

auto hostbond4
iface hostbond4
    bond-slaves swp8
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf01 and Ports swp8 <==> Remote  Node/s host04 and Ports swp1
    bridge-pvid 1000

auto vx-1000
iface vx-1000
    vxlan-id 1000
    bridge-access 1000
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.100
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1001
iface vx-1001
    vxlan-id 1001
    bridge-access 1001
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.101
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1002
iface vx-1002
    vxlan-id 1002
    bridge-access 1002
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.102
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1003
iface vx-1003
    vxlan-id 1003
    bridge-access 1003
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.103
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1004
iface vx-1004
    vxlan-id 1004
    bridge-access 1004
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.104
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1005
iface vx-1005
    vxlan-id 1005
    bridge-access 1005
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.105
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1006
iface vx-1006
    vxlan-id 1006
    bridge-access 1006
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.106
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1007
iface vx-1007
    vxlan-id 1007
    bridge-access 1007
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.107
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1008
iface vx-1008
    vxlan-id 1008
    bridge-access 1008
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.108
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1009
iface vx-1009
    vxlan-id 1009
    bridge-access 1009
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.109
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4001
iface vx-4001
    vxlan-id 4001
    bridge-access 4001
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4002
iface vx-4002
    vxlan-id 4002
    bridge-access 4002
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4003
iface vx-4003
    vxlan-id 4003
    bridge-access 4003
    vxlan-local-tunnelip 172.16.0.21
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

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
    alias Local Node leaf02 and Ports swp1 <==> Remote  Node/s spine01 and Ports swp3

auto swp2
iface swp2
    alias Local Node leaf02 and Ports swp2 <==> Remote  Node/s spine01 and Ports swp4

auto swp3
iface swp3
    alias Local Node leaf02 and Ports swp3 <==> Remote  Node/s spine02 and Ports swp3

auto swp4
iface swp4
    alias Local Node leaf02 and Ports swp4 <==> Remote  Node/s spine02 and Ports swp4

auto swp5
iface swp5

auto swp6
iface swp6

auto swp7
iface swp7

auto swp8
iface swp8

auto hostbond1
iface hostbond1
    bond-slaves swp5
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf02 and Ports swp5 <==> Remote  Node/s host01 and Ports swp2
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1000

auto hostbond2
iface hostbond2
    bond-slaves swp6
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf02 and Ports swp6 <==> Remote  Node/s host02 and Ports swp2
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1001

auto hostbond3
iface hostbond3
    bond-slaves swp7
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf02 and Ports swp7 <==> Remote  Node/s host03 and Ports swp2
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1002

auto hostbond4
iface hostbond4
    bond-slaves swp8
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf02 and Ports swp8 <==> Remote  Node/s host04 and Ports swp1
    bridge-pvid 1000

auto vx-1000
iface vx-1000
    vxlan-id 1000
    bridge-access 1000
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.100
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1001
iface vx-1001
    vxlan-id 1001
    bridge-access 1001
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.101
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1002
iface vx-1002
    vxlan-id 1002
    bridge-access 1002
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.102
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1003
iface vx-1003
    vxlan-id 1003
    bridge-access 1003
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.103
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1004
iface vx-1004
    vxlan-id 1004
    bridge-access 1004
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.104
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1005
iface vx-1005
    vxlan-id 1005
    bridge-access 1005
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.105
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1006
iface vx-1006
    vxlan-id 1006
    bridge-access 1006
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.106
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1007
iface vx-1007
    vxlan-id 1007
    bridge-access 1007
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.107
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1008
iface vx-1008
    vxlan-id 1008
    bridge-access 1008
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.108
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1009
iface vx-1009
    vxlan-id 1009
    bridge-access 1009
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.109
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4001
iface vx-4001
    vxlan-id 4001
    bridge-access 4001
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4002
iface vx-4002
    vxlan-id 4002
    bridge-access 4002
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4003
iface vx-4003
    vxlan-id 4003
    bridge-access 4003
    vxlan-local-tunnelip 172.16.0.22
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

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
    alias Local Node leaf03 and Ports swp1 <==> Remote  Node/s spine01 and Ports swp5

auto swp2
iface swp2
    alias Local Node leaf03 and Ports swp2 <==> Remote  Node/s spine01 and Ports swp6

auto swp3
iface swp3
    alias Local Node leaf03 and Ports swp3 <==> Remote  Node/s spine02 and Ports swp5

auto swp4
iface swp4
    alias Local Node leaf03 and Ports swp4 <==> Remote  Node/s spine02 and Ports swp6

auto swp5
iface swp5

auto swp6
iface swp6

auto swp7
iface swp7

auto swp8
iface swp8

auto hostbond1
iface hostbond1
    bond-slaves swp5
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf03 and Ports swp5 <==> Remote  Node/s host01 and Ports swp3
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1000

auto hostbond2
iface hostbond2
    bond-slaves swp6
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf03 and Ports swp6 <==> Remote  Node/s host02 and Ports swp3
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1001

auto hostbond3
iface hostbond3
    bond-slaves swp7
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf03 and Ports swp7 <==> Remote  Node/s host03 and Ports swp3
    es-sys-mac 44:38:39:ff:ff:01
    bridge-pvid 1002

auto hostbond4
iface hostbond4
    bond-slaves swp8
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s leaf03 and Ports swp8 <==> Remote  Node/s host04 and Ports swp1
    bridge-pvid 1000

auto vx-1000
iface vx-1000
    vxlan-id 1000
    bridge-access 1000
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.100
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1001
iface vx-1001
    vxlan-id 1001
    bridge-access 1001
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.101
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1002
iface vx-1002
    vxlan-id 1002
    bridge-access 1002
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.102
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1003
iface vx-1003
    vxlan-id 1003
    bridge-access 1003
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.103
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1004
iface vx-1004
    vxlan-id 1004
    bridge-access 1004
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.104
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1005
iface vx-1005
    vxlan-id 1005
    bridge-access 1005
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.105
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1006
iface vx-1006
    vxlan-id 1006
    bridge-access 1006
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.106
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1007
iface vx-1007
    vxlan-id 1007
    bridge-access 1007
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.107
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1008
iface vx-1008
    vxlan-id 1008
    bridge-access 1008
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.108
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-1009
iface vx-1009
    vxlan-id 1009
    bridge-access 1009
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    vxlan-mcastgrp 239.1.1.109
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4001
iface vx-4001
    vxlan-id 4001
    bridge-access 4001
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4002
iface vx-4002
    vxlan-id 4002
    bridge-access 4002
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

auto vx-4003
iface vx-4003
    vxlan-id 4003
    bridge-access 4003
    vxlan-local-tunnelip 172.16.0.23
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes

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
    address 10.0.0.100/32
    alias MSDP Anycast PIM-SM RP

auto swp1
iface swp1
    alias Local Node spine01 and Ports swp1 <==> Remote  Node/s leaf01 and Ports swp1

auto swp2
iface swp2
    alias Local Node spine01 and Ports swp2 <==> Remote  Node/s leaf01 and Ports swp2

auto swp3
iface swp3
    alias Local Node spine01 and Ports swp3 <==> Remote  Node/s leaf02 and Ports swp1

auto swp4
iface swp4
    alias Local Node spine01 and Ports swp4 <==> Remote  Node/s leaf02 and Ports swp2

auto swp5
iface swp5
    alias Local Node spine01 and Ports swp5 <==> Remote  Node/s leaf03 and Ports swp1

auto swp6
iface swp6
    alias Local Node spine01 and Ports swp6 <==> Remote  Node/s leaf03 and Ports swp2

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
    address 10.0.0.100/32
    alias MSDP Anycast PIM-SM RP

auto swp1
iface swp1
    alias Local Node spine02 and Ports swp1 <==> Remote  Node/s leaf01 and Ports swp3

auto swp2
iface swp2
    alias Local Node spine02 and Ports swp2 <==> Remote  Node/s leaf01 and Ports swp4

auto swp3
iface swp3
    alias Local Node spine02 and Ports swp3 <==> Remote  Node/s leaf02 and Ports swp3

auto swp4
iface swp4
    alias Local Node spine02 and Ports swp4 <==> Remote  Node/s leaf02 and Ports swp4

auto swp5
iface swp5
    alias Local Node spine02 and Ports swp5 <==> Remote  Node/s leaf03 and Ports swp3

auto swp6
iface swp6
    alias Local Node spine02 and Ports swp6 <==> Remote  Node/s leaf03 and Ports swp4

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

auto swp2
iface swp2

auto swp3
iface swp3

auto torbond1
iface torbond1
    address 172.20.0.9/24
    address 2001:db8::9/64
    bond-slaves swp1 swp2 swp3
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
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

auto swp2
iface swp2

auto swp3
iface swp3

auto torbond1
iface torbond1
    address 172.20.1.10/24
    address 2001:db8:0:1::a/64
    bond-slaves swp1 swp2 swp3
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
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
{{<tab "host03">}}

```
cumulus@host03:~$ cat /etc/network/interfaces
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

auto swp2
iface swp2

auto swp3
iface swp3

auto torbond1
iface torbond1
    address 172.20.1.11/24
    address 2001:db8:0:1::b/64
    bond-slaves swp1 swp2 swp3
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s host03 and Ports swp1 swp2 swp3 <==> Remote  Node/s leaf01 leaf02 leaf03 and Ports swp7 swp7 swp7
    post-up ip route replace default via 172.20.1.1 dev torbond1
    post-up ip -6 route replace default via 2001:db8:0:1::1 dev torbond1

auto torbond1.1000
iface torbond1.1000
    address 172.20.0.11/24
    address 2001:db8::b/64
    alias Vni 1000
    vrf vrf1000
    gateway 172.20.0.1
    gateway 2001:db8::1

auto vrf1000
iface vrf1000
    vrf-table auto

auto torbond1.1002
iface torbond1.1002
    address 172.20.2.11/24
    address 2001:db8:0:2::b/64
    alias Vni 1002
    vrf vrf1002
    gateway 172.20.2.1
    gateway 2001:db8:0:2::1

auto vrf1002
iface vrf1002
    vrf-table auto

auto torbond1.1003
iface torbond1.1003
    address 172.20.3.11/24
    address 2001:db8:0:3::b/64
    alias Vni 1003
    vrf vrf1003
    gateway 172.20.3.1
    gateway 2001:db8:0:3::1

auto vrf1003
iface vrf1003
    vrf-table auto

auto torbond1.1004
iface torbond1.1004
    address 172.20.4.11/24
    address 2001:db8:0:4::b/64
    alias Vni 1004
    vrf vrf1004
    gateway 172.20.4.1
    gateway 2001:db8:0:4::1

auto vrf1004
iface vrf1004
    vrf-table auto

auto torbond1.1005
iface torbond1.1005
    address 172.20.5.11/24
    address 2001:db8:0:5::b/64
    alias Vni 1005
    vrf vrf1005
    gateway 172.20.5.1
    gateway 2001:db8:0:5::1

auto vrf1005
iface vrf1005
    vrf-table auto

auto torbond1.1006
iface torbond1.1006
    address 172.20.6.11/24
    address 2001:db8:0:6::b/64
    alias Vni 1006
    vrf vrf1006
    gateway 172.20.6.1
    gateway 2001:db8:0:6::1

auto vrf1006
iface vrf1006
    vrf-table auto

auto torbond1.1007
iface torbond1.1007
    address 172.20.7.11/24
    address 2001:db8:0:7::b/64
    alias Vni 1007
    vrf vrf1007
    gateway 172.20.7.1
    gateway 2001:db8:0:7::1

auto vrf1007
iface vrf1007
    vrf-table auto

auto torbond1.1008
iface torbond1.1008
    address 172.20.8.11/24
    address 2001:db8:0:8::b/64
    alias Vni 1008
    vrf vrf1008
    gateway 172.20.8.1
    gateway 2001:db8:0:8::1

auto vrf1008
iface vrf1008
    vrf-table auto

auto torbond1.1009
iface torbond1.1009
    address 172.20.9.11/24
    address 2001:db8:0:9::b/64
    alias Vni 1009
    vrf vrf1009
    gateway 172.20.9.1
    gateway 2001:db8:0:9::1

auto vrf1009
iface vrf1009
    vrf-table auto

cumulus@host03:~$
```

{{</tab>}}
{{<tab "host04">}}

```
cumulus@host04:~$ cat /etc/network/interfaces
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

auto swp2
iface swp2

auto swp3
iface swp3

auto torbond1
iface torbond1
    address 172.20.1.10/24
    address 2001:db8:0:1::a/64
    bond-slaves swp1 swp2 swp3
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    alias Local Node/s host04 and Ports swp1 swp2 swp3 <==> Remote  Node/s leaf01 leaf02 leaf03 and Ports swp8 swp8 swp8
    post-up ip route replace default via 172.20.1.1 dev torbond1
    post-up ip -6 route replace default via 2001:db8:0:1::1 dev torbond1

auto torbond1.1000
iface torbond1.1000
    address 172.20.0.12/24
    address 2001:db8::c/64
    alias Vni 1000
    vrf vrf1000
    gateway 172.20.0.1
    gateway 2001:db8::1

auto vrf1000
iface vrf1000
    vrf-table auto

auto torbond1.1002
iface torbond1.1002
    address 172.20.2.12/24
    address 2001:db8:0:2::c/64
    alias Vni 1002
    vrf vrf1002
    gateway 172.20.2.1
    gateway 2001:db8:0:2::1

auto vrf1002
iface vrf1002
    vrf-table auto

auto torbond1.1003
iface torbond1.1003
    address 172.20.3.12/24
    address 2001:db8:0:3::c/64
    alias Vni 1003
    vrf vrf1003
    gateway 172.20.3.1
    gateway 2001:db8:0:3::1

auto vrf1003
iface vrf1003
    vrf-table auto

auto torbond1.1004
iface torbond1.1004
    address 172.20.4.12/24
    address 2001:db8:0:4::c/64
    alias Vni 1004
    vrf vrf1004
    gateway 172.20.4.1
    gateway 2001:db8:0:4::1

auto vrf1004
iface vrf1004
    vrf-table auto

auto torbond1.1005
iface torbond1.1005
    address 172.20.5.12/24
    address 2001:db8:0:5::c/64
    alias Vni 1005
    vrf vrf1005
    gateway 172.20.5.1
    gateway 2001:db8:0:5::1

auto vrf1005
iface vrf1005
    vrf-table auto

auto torbond1.1006
iface torbond1.1006
    address 172.20.6.12/24
    address 2001:db8:0:6::2/64
    alias Vni 1006
    vrf vrf1006
    gateway 172.20.6.1
    gateway 2001:db8:0:6::1

auto vrf1006
iface vrf1006
    vrf-table auto

auto torbond1.1007
iface torbond1.1007
    address 172.20.7.12/24
    address 2001:db8:0:7::c/64
    alias Vni 1007
    vrf vrf1007
    gateway 172.20.7.1
    gateway 2001:db8:0:7::1

auto vrf1007
iface vrf1007
    vrf-table auto

auto torbond1.1008
iface torbond1.1008
    address 172.20.8.12/24
    address 2001:db8:0:8::c/64
    alias Vni 1008
    vrf vrf1008
    gateway 172.20.8.1
    gateway 2001:db8:0:8::1

auto vrf1008
iface vrf1008
    vrf-table auto

auto torbond1.1009
iface torbond1.1009
    address 172.20.9.12/24
    address 2001:db8:0:9::c/64
    alias Vni 1009
    vrf vrf1009
    gateway 172.20.9.1
    gateway 2001:db8:0:9::1

auto vrf1009
iface vrf1009
    vrf-table auto

cumulus@host04:~$
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
ip pim rp 10.0.0.100 239.1.1.0/24
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
interface lo
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
ip pim rp 10.0.0.100 239.1.1.0/24
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
 exit-address-family
!
!
!
interface swp1
 ip pim
!
!
interface swp2
 ip pim
!
!
interface swp3
 ip pim
!
!
interface swp4
 ip pim
!
!
interface lo
 ip pim
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
ip pim rp 10.0.0.100 239.1.1.0/24
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
 exit-address-family
!

!

!
interface swp1
 ip pim
!
!
interface swp2
 ip pim
!
!
interface swp3
 ip pim
!
!
interface swp4
 ip pim
!
!
interface lo
 ip pim
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
ip pim rp 10.0.0.100 239.1.1.0/24
ip pim spt-switchover infinity-and-beyond
ip msdp mesh-group cumulus member 172.16.0.18
ip msdp mesh-group cumulus source 172.16.0.17
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
 ip pim
!
!
interface swp2
 ip pim
!
!
interface swp3
 ip pim
!
!
interface swp4
 ip pim
!
!
interface swp5
 ip pim
!
!
interface swp6
 ip pim
!
!
interface swp7
 ip pim
!
!
interface swp8
 ip pim
!
!
interface swp9
 ip pim
!
!
interface swp10
 ip pim
!
!
interface swp11
 ip pim
!
!
interface swp12
 ip pim
!
!
interface swp13
 ip pim
!
!
interface swp14
 ip pim
!
!
interface swp15
 ip pim
!
!
interface swp16
 ip pim
!
!
interface lo
 ip pim
 ip pim use-source 10.0.0.100
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
ip pim rp 10.0.0.100 239.1.1.0/24
ip pim spt-switchover infinity-and-beyond
ip msdp mesh-group cumulus member 172.16.0.17
ip msdp mesh-group cumulus source 172.16.0.18
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
 ip pim
!
!
interface swp2
 ip pim
!
!
interface swp3
 ip pim
!
!
interface swp4
 ip pim
!
!
interface swp5
 ip pim
!
!
interface swp6
 ip pim
!
!
interface swp7
 ip pim
!
!
interface swp8
 ip pim
!
!
interface swp9
 ip pim
!
!
interface swp10
 ip pim
!
!
interface swp11
 ip pim
!
!
interface swp12
 ip pim
!
!
interface swp13
 ip pim
!
!
interface swp14
 ip pim
!
!
interface swp15
 ip pim
!
!
interface swp16
 ip pim
!
!
interface lo
 ip pim
 ip pim use-source 10.0.0.100
!
line vty
 exec-timeout 0 0
```

{{</tab>}}
{{</tabs>}}
