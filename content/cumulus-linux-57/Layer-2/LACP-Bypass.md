---
title: LACP Bypass
author: NVIDIA
weight: 500
toc: 3
---
In Cumulus Linux, <span style="background-color:#F5F5DC">[LACP](## "Link Aggregation Control Protocol")</span> bypass allows a {{<link url="Bonding-Link-Aggregation" text="bond">}} configured in 802.3ad mode to become active and forward traffic even when there is no LACP partner. For example, you can enable a host that does not have the capability to run LACP to <span style="background-color:#F5F5DC">[PXE](## "Preboot eXecution Environment")</span> boot while connected to a switch on a bond configured in 802.3ad mode. After the pre-boot process completes and the host is capable of running LACP, the normal 802.3ad link aggregation operation takes over.
<!-- vale off -->
## LACP Bypass All-active Mode
<!-- vale on -->
In *all-active* mode, when a bond has multiple slave interfaces, each bond slave interface operates as an active link while the bond is in bypass mode. This is useful during PXE boot of a server with multiple NICs, when you cannot determine beforehand which port needs to be active.

{{%notice note%}}
- All-active mode is *not* supported on bonds that are *not* specified as bridge ports on the switch.
- <span style="background-color:#F5F5DC">[STP](## "Spanning Tree Protocol")</span> does not run on the individual bond slave interfaces when the LACP bond is in all-active mode. Only use all-active mode on host-facing LACP bonds. Configure {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="STP BPDU guard">}} together with all-active mode.
- In an {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG deployment">}} where bond slaves of a host connect to two switches and the bond is in all-active mode, all the slaves of the bond are active on both the primary and secondary MLAG nodes. If multiple physical NIC interfaces or more than one physical NIC is present on the physical host, NVIDIA recommends that you define which physical NIC or interface runs the PXE boot inside the PXE boot configuration file. If you do not define a specific NIC or interface, the switch sends a PXE boot request on all the interfaces in the bond and the PXE request fails.
- LACP bypass works with {{<link url="EVPN-Multihoming/#supported-features" text="EVPN multihoming">}}.
- Cumulus Linux does not support `priority mode`, `bond-lacp-bypass-period`, `bond-lacp-bypass-priority`, and `bond-lacp-bypass-all-active`.
{{%/notice%}}

## Configure LACP Bypass

To enable LACP bypass on the host-facing bond:

{{< tabs "TabID28 ">}}
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

To show the bond configuration, run the `nv show interface <bond>` command.

```
cumulus@leaf01:mgmt:~$ nv show interface bond1
                         operational        applied     description
-----------------------  -----------------  ----------  ----------------------------------------------------------------------
type                     bond               bond        The type of interface
[acl]                                                   Interface ACL rules
bond
  down-delay             0                  0           bond down delay
  lacp-bypass                               on          lacp bypass
  lacp-rate              fast               fast        lacp rate
  mode                                      lacp        bond mode
  up-delay               0                  0           bond up delay
  [member]               swp1               swp1        Set of bond members
  mlag
    enable                                  on          Turn the feature 'on' or 'off'.  The default is 'off'.
    id                   1                  1           MLAG id
    peer-interface       bond1                          Peer interface
    status               dual                           Mlag Interface status
bridge
  [domain]               br_default         br_default  Bridge domains on this interface
...
```

To check the status of the link, run the Linux `ip link show` command on the bond and its slave interfaces:

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
