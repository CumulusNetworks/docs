---
title: LACP Bypass
author: NVIDIA
weight: 500
toc: 3
---
On Cumulus Linux, *LACP bypass* allows a {{<link url="Bonding-Link-Aggregation" text="bond">}} configured in 802.3ad mode to become active and forward traffic even when there is no LACP partner. For example, you can enable a host that does not have the capability to run LACP to PXE boot while connected to a switch on a bond configured in 802.3ad mode. After the pre-boot process completes and the host is capable of running LACP, the normal 802.3ad link aggregation operation takes over.

## LACP Bypass All-active Mode

In *all-active* mode, when a bond has multiple slave interfaces, each bond slave interface operates as an active link while the bond is in bypass mode. This is useful during PXE boot of a server with multiple NICs, when you cannot determine beforehand which port needs to be active.

{{%notice note%}}
- All-active mode is *not* supported on bonds that are *not* specified as bridge ports on the switch.
- STP does not run on the individual bond slave interfaces when the LACP bond is in all-active mode. Only use all-active mode on host-facing LACP bonds. Configure {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="STP BPDU guard">}} together with all-active mode.
- In an {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG deployment">}} where bond slaves of a host are connected to two switches and the bond is in all-active mode, all the slaves of the bond are active on both the primary and secondary MLAG nodes. If multiple physical NIC interfaces or more than one physical NIC is present on the physical host, NVIDIA recommends that you define which physical NIC or interface runs the PXE boot inside the PXE boot configuration file. If you do not define a specific NIC or interface, a PXE boot request is sent on all the interfaces in the bond and the PXE request fails.

Another point that we might need to do is open an FR and implement behaviour like Arista LACP fallback in case the
- LACP bypass is supported with {{<link url="EVPN-Multihoming/#supported-features" text="EVPN multihoming">}}.
- `priority mode`, `bond-lacp-bypass-period`, `bond-lacp-bypass-priority`, and `bond-lacp-bypass-all-active` are not supported.
{{%/notice%}}

## Configure LACP Bypass

To enable LACP bypass on the host-facing bond:

{{< tabs "TabID28 ">}}
{{< tab "NCLU Commands ">}}

The following commands create a VLAN-aware bridge with LACP bypass enabled:

```
cumulus@switch:~$ net add bond bond1 bond slaves swp1,swp2
cumulus@switch:~$ net add bond bond1 clag id 1
cumulus@switch:~$ net add bond bond1 bond lacp-bypass-allow
cumulus@switch:~$ net add bond bond1 stp bpduguard
cumulus@switch:~$ net add bridge bridge ports bond1,bond2,bond3
cumulus@switch:~$ net add bridge bridge vids 10,20,30
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

The following commands create a VLAN-aware bridge with LACP bypass enabled:

```
cumulus@leaf01:~$ nv set interface bond1 bond member swp1-2
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the set `bond-lacp-bypass-allow` to `yes` option, then run the `ifreload -a` command. The following configuration creates a VLAN-aware bridge with LACP bypass enabled.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-slaves swp1 swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    clag-id 1
...
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3
    bridge-vids 10 20 30
    bridge-vlan-aware yes
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

To check the status of the configuration, run the NCLU `net show interface <bond>` command or the Linux `ip link show` command on the bond and its slave interfaces. The NVUE Command is `nv show interface <bond>`.

```
cumulus@switch:~$ ip link show bond1
164: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master br0 state UP mode DORMANT group default
    link/ether c4:54:44:f6:44:5a brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show swp1
55: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT group default qlen 1000
    link/ether c4:54:44:f6:44:5a brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show swp2
56: swp2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT group default qlen 1000
    link/ether c4:54:44:f6:44:5a brd ff:ff:ff:ff:ff:ff
```
