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
- EVPN BUM traffic handling with {{<link title="EVPN BUM Traffic with PIM-SM" text="EVPN-PIM">}} on multihomed sites via Type-4/ESR routes, which includes split-horizon-filtering and designated forwarder election

{{%notice warning%}}
To use EVPN-MH, you must remove any MLAG configuration on the switch:
- Remove the `clag-id` from all interfaces in the `/etc/network/interfaces` file.
- Remove the peerlink interfaces in the `/etc/network/interfaces` file.
- Remove any existing `hwaddress` (from a Cumulus Linux 3.x MLAG configuration) or `address-virtual` (from a Cumulus Linux 4.x MLAG configuration) entries from all SVIs corresponding to a layer 3 VNI in the `/etc/network/interfaces` file.
- Remove any `clagd-vxlan-anycast-ip` configuration in the `/etc/network/interfaces` file.
- Run the `sudo ifreload` command to reload the configuration.
{{%/notice%}}

### Other Supported Features

- Known unicast traffic multihoming through type-1/EAD (Ethernet auto discovery) routes and type-2 (non-zero ESI) routes. Includes all-active redundancy using aliasing and support for fast failover.
- {{<link url="LACP-Bypass">}} is supported.
  - When an EVPN-MH bond enters LACP bypass state, BGP stops advertising EVPN type-1 and type-4 routes for that bond. Split-horizon and designated forwarder filters are disabled.
  - When an EVPN-MH bond exits the LACP bypass state, BGP starts advertising EVPN type-1 and type-4 routes for that bond. Split-horizon and designated forwarder filters are enabled.
- EVI (*EVPN virtual instance*). Cumulus Linux supports VLAN-based service only, so the EVI is just a layer 2 VNI.
- Supported {{<exlink url="https://cumulusnetworks.com/hcl" text="ASICs">}} include NVIDIA Spectrum A1, Spectrum 2 and Spectrum 3.

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

## Configure EVPN-MH

To configure EVPN-MH:
1. Enable EVPN multihoming.
2. Set the Ethernet segment ID
3. Set the Ethernet segment system MAC address

These settings are applied to interfaces, typically bonds.

An Ethernet segment configuration has these characteristics:

- The Ethernet segment ID is a 24-bit integer (1-16777215).
- Each interface (bond) needs its own Ethernet segment ID.
- Static and LACP bonds can be associated with an Ethernet segment ID.

A *designated forwarder* (DF) is elected for each Ethernet segment. The DF is responsible for forwarding flooded traffic received through the VXLAN overlay to the locally attached Ethernet segment. Specify a preference on an Ethernet segment for the DF election, as this leads to predictable failure scenarios. The EVPN VTEP with the highest DF preference setting becomes the DF. The DF preference setting defaults to _32767_.

NCLU generates the EVPN-MH configuration and reloads FRR and `ifupdown2`. The configuration appears in both the `/etc/network/interfaces` file and in `/etc/frr/frr.conf` file.

{{%notice note%}}
When EVPN-MH is enabled, all SVI MAC addresses are advertised as type 2 routes. You do not need to configure a unique SVI IP address or configure the BGP EVPN address family with `advertise-svi-ip`.
{{%/notice%}}

### Enable EVPN-MH

{{< tabs "TabID105 ">}}
{{<tab "CUE Commands">}}

```
cumulus@switch:~$ cl set evpn multihoming enable on
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Set the `evpn.multihoming.enable` variable in the `/etc/cumulus/switchd.conf` file to `TRUE`, then restart the `switchd` service. The variable is disabled by default.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
evpn.multihoming.enable = TRUE
...

cumulus@switch:~$ sudo systemctl restart switchd.service
```

{{< /tab >}}
{{< /tabs >}}

### Configure the EVPN-MH Bonds

To configure bond interfaces for EVPN multihoming, run commands similar to the following:

{{<tabs "bond config">}}
{{<tab "CUE Commands">}}

```
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond3 bond member swp3
cumulus@leaf01:~$ cl set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf01:~$ cl set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf01:~$ cl set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf01:~$ cl set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf01:~$ cl config apply
```

{{</tab>}}
{{<tab "NCLU Commands">}}

```
cumulus@switch:~$ net add bond bond1 bond slaves swp1
cumulus@switch:~$ net add bond bond2 bond slaves swp2
cumulus@switch:~$ net add bond bond3 bond slaves swp3
cumulus@switch:~$ net add bond bond1 evpn mh es-id 1
cumulus@switch:~$ net add bond bond2 evpn mh es-id 2
cumulus@switch:~$ net add bond bond3 evpn mh es-id 3
cumulus@switch:~$ net add bond bond1-3 evpn mh es-sys-mac 44:38:39:BE:EF:AA
cumulus@switch:~$ net add bond bond1-3 evpn mh es-df-pref 50000
cumulus@switch:~$ net commit
```

{{</tab>}}
{{<tab "vtysh Commands">}}

```
cumulus@leaf01:~$ sudo vtysh

Hello, this is FRRouting (version 7.4+cl4u1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

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

{{</tab>}}
{{</tabs>}}

The NCLU commands create the following configuration in the `/etc/network/interfaces` file. If you are editing the `/etc/network/interfaces` file directly, apply a configuration like the following:

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
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

These commands also create the following configuration in the `/etc/frr/frr.conf` file.

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
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

### EVPN MH Global Settings

You can set these global settings for EVPN multihoming:
- `mac-holdtime` specifies the duration for which a switch maintains SYNC MAC entries after the EVPN type-2 route of the Ethernet segment peer is deleted. During this time, the switch attempts to independently establish reachability of the MAC address on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.
- `neigh-holdtime` specifies the duration for which a switch maintains SYNC neighbor entries after the EVPN type-2 route of the Ethernet segment peer is deleted. During this time, the switch attempts to independently establish reachability of the host on the local Ethernet segment. The hold time can be between 0 and 86400 seconds. The default is 1080 seconds.
- `redirect-off` disables fast failover of traffic destined to the access port via the VXLAN overlay. This only applies to Cumulus VX (fast failover is only supported on the ASIC).
- `startup-delay` specifies the duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart. This allows the initialization of the VXLAN overlay to complete. The delay can be between 0 and 216000 seconds. The default is 180 seconds.

To configure a MAC hold time for 1000 seconds, run the following commands:

{{<tabs "MAC hold time">}}
{{<tab "CUE Commands">}}

```
cumulus@switch:~$ cl set evpn multihoming mac-holdtime 1000
cumulus@switch:~$ cl config apply
```

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
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1000
```

To configure a neighbor hold time for 600 seconds, run the following commands:

{{<tabs "Neighbor hold time">}}
{{<tab "CUE Commands">}}

```
cumulus@switch:~$ cl set evpn multihoming neighbor-holdtime 600
cumulus@switch:~$ cl config apply
```

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
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
evpn mh neigh-holdtime 600
```

To configure a startup delay for 1800 seconds, run the following commands:

{{<tabs "startup delay">}}
{{<tab "CUE Commands">}}

```
cumulus@switch:~$ cl set evpn multihoming startup-delay 1800
cumulus@switch:~$ cl config apply
```

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
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
evpn mh startup-delay 1800
```

### Enable Uplink Tracking

When all the uplinks go down, the VTEP loses connectivity to the VXLAN overlay. To prevent traffic loss in this state, the uplinks' oper-state is tracked. When all the uplinks are down, the Ethernet segment bonds on the switch are put into a protodown or error-disabled state. You can configure a link as an MH uplink to enable this tracking.

{{<tabs "upink tracking">}}
{{<tab "CUE Commands">}}

```
cumulus@switch:~$ cl set interface swp1-3 evpn multihoming uplink on
cumulus@switch:~$ NEED COMMAND 
cumulus@switch:~$ cl config apply
```

{{</tab>}}
{{<tab "NCLU Commands">}}

```
cumulus@switch:~$ net add interface swp1-4 evpn mh uplink
cumulus@switch:~$ net add interface swp1-4 pim
cumulus@switch:~$ net commit
```

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
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
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

You can add debug statements to the `/etc/frr/frr.conf` file to debug the Ethernet segments, routes, and routing protocols (via Zebra).

{{<tabs "debug">}}
{{<tab "CUE Commands">}}

CUE commands are not supported.

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
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set evpn multihoming ead-evi-route rx off
cumulus@switch:~$ cl config apply
```

To suppress the advertisement of EAD-per-EVI routes, run:

```
cumulus@switch:~$ cl set evpn multihoming ead-evi-route tx off
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp l2vpn evpn disable-ead-evi-rx
cumulus@switch:~$ net commit
```

To suppress the advertisement of EAD-per-EVI routes, run:

```
cumulus@switch:~$ net add bgp l2vpn evpn disable-ead-evi-tx
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

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

## Example Configuration

The following example uses the topology illustrated here. It shows one rack for simplicity, but multiple racks can be added to this topology.

{{<img src="/images/cumulus-linux/EVPN-MH-example-config.png">}}

### Configuration Commands

This section lists the CUE commands to configure the switches and the network as well as the `vtysh` commands to configure FRRouting.

If you are not using CUE to configure the `/etc/network/interfaces` file, go to {{<link url="#etcnetworkinterfaces" text="/etc/network/interfaces">}} below and copy the configurations directly into the `interfaces` file on each switch and server in the topology.

{{<tabs "Example Configuration Commands">}}
{{<tab "leaf01">}}

**CUE Commands**

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set interface swp1-3,swp49-54
cumulus@leaf01:~$ cl set interface bond1 bond member swp1
cumulus@leaf01:~$ cl set interface bond2 bond member swp2
cumulus@leaf01:~$ cl set interface bond3 bond member swp3
cumulus@leaf01:~$ cl set interface bond1 bond mlag id 1
cumulus@leaf01:~$ cl set interface bond2 bond mlag id 2
cumulus@leaf01:~$ cl set interface bond3 bond mlag id 3
cumulus@leaf01:~$ cl set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond3 bond lacp-bypass on
cumulus@leaf01:~$ cl set interface bond1 link mtu 9000
cumulus@leaf01:~$ cl set interface bond2 link mtu 9000
cumulus@leaf01:~$ cl set interface bond3 link mtu 9000
cumulus@leaf01:~$ cl set interface bond1-3 bridge domain br_default
cumulus@leaf01:~$ cl set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ cl set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ cl set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ cl set interface lo pim
cumulus@leaf01:~$ cl set interface swp1-3 pim
cumulus@leaf01:~$ cl set pim rp 192.168.0.1 239.1.1.0/24
cumulus@leaf01:~$ cl set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ cl set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ cl set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf01:~$ cl set interface vlan10 ip vrr state up
cumulus@leaf01:~$ cl set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ cl set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ cl set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf01:~$ cl set interface vlan20 ip vrr state up
cumulus@leaf01:~$ cl set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ cl set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:~$ cl set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf01:~$ cl set interface vlan30 ip vrr state up
cumulus@leaf01:~$ cl set vrf RED
cumulus@leaf01:~$ cl set vrf BLUE
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ cl set interface vlan10 ip vrf RED
cumulus@leaf01:~$ cl set interface vlan20 ip vrf RED
cumulus@leaf01:~$ cl set interface vlan30 ip vrf BLUE
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ cl set vrf RED evpn vni 4001
cumulus@leaf01:~$ cl set vrf BLUE evpn vni 4002
cumulus@leaf01:~$ cl set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set evpn enable on
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp52 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp53 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp peer swp54 peer-group underlay
cumulus@leaf01:~$ cl set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@leaf01:~$ cl set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ cl set vrf default router bgp peer peerlink.4094 remote-as internal
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:~$ cl set evpn multihoming enable on
cumulus@leaf01:~$ cl set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf01:~$ cl set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf01:~$ cl set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf01:~$ cl set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ cl set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf01:~$ cl set interface swp1-3 evpn multihoming uplink on
cumulus@leaf01:~$ cl config apply
```

{{</tab>}}
{{<tab "leaf02">}}

```

```

{{</tab>}}
{{<tab "leaf03">}}

```

```

{{</tab>}}
{{<tab "spine01">}}

```

```

{{</tab>}}
{{<tab "spine02">}}

```

```

{{</tab>}}
{{</tabs>}}

### /etc/network/interfaces

{{<tabs "/etc/network/interfaces">}}
{{<tab "leaf01">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

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

auto swp49
iface swp49

auto swp50
iface swp50

auto swp51
iface swp51

auto swp52
iface swp52

auto swp53
iface swp53

auto swp54
iface swp54

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

{{</tab>}}
{{<tab "leaf03">}}

{{</tab>}}
{{<tab "spine01">}}

{{</tab>}}
{{<tab "spine02">}}

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
interface bond1
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond2
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond3
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
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
interface bond1
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond2
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
!
interface bond3
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:BE:EF:AA
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
