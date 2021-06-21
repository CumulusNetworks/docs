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
- In an {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG deployment">}} where bond slaves of a host are connected to two switches and the bond is in all-active mode, all the slaves of bond are active on both the primary and secondary MLAG nodes.
- LACP bypass is supported with {{<link url="EVPN-Multihoming/#supported-features" text="EVPN multihoming">}}.
- `priority mode`, `bond-lacp-bypass-period`, `bond-lacp-bypass-priority`, and `bond-lacp-bypass-all-active` are not supported.

{{%/notice%}}

## Configure LACP Bypass

To enable LACP bypass on the host-facing bond:

{{< tabs "TabID28 ">}}

{{< tab "NCLU Commands ">}}

The following commands create a VLAN-aware bridge with LACP bypass enabled:

```
cumulus@switch:~$ net add bond bond1 bond slaves swp51s2,swp51s3
cumulus@switch:~$ net add bond bond1 clag id 1
cumulus@switch:~$ net add bond bond1 bond lacp-bypass-allow
cumulus@switch:~$ net add bond bond1 stp bpduguard
cumulus@switch:~$ net add bridge bridge ports bond1,bond2,bond3,bond4,bond5
cumulus@switch:~$ net add bridge bridge vids 100-105
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the set `bond-lacp-bypass-allow` to yes option, then run the `ifreload -a` command. The following configuration creates a VLAN-aware bridge with LACP bypass enabled:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-lacp-bypass-allow yes
    bond-slaves swp51s2 swp51s3
    clag-id 1
    mstpctl-bpduguard yes
...
auto bridge
iface bridge
    bridge-ports bond1 bond2 bond3 bond4 peer5
    bridge-vids 100-105
    bridge-vlan-aware yes
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface bond1 bond member swp51s2,swp51s3
cumulus@switch:~$ cl set interface bond1 bond mlag id 1
cumulus@switch:~$ cl set interface bond1 bond lacp-bypass on
cumulus@switch:~$ cl set interface bond1,bond2,bond3,bond4,bond5 bridge domain bridge vlan 100-105
cumulus@switch:~$ cl set interface bond1 bridge domain bridge stp bpdu-guard on
cumulus@switch:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

To check the status of the configuration, run the following commands.

{{< tabs "TabID79 ">}}

{{< tab "NCLU Commands ">}}

Run the `net show interface <bond>` command on the bond and its slave interfaces:

```
cumulus@switch:~$ net show interface bond1

    Name   MAC               Speed   MTU   Mode
--  ------ ----------------- ------- ----- ----------
UP  bond1  44:38:39:00:00:5b 1G      1500  Bond/Trunk

Bond Details
------------------ -------------------------
Bond Mode:         LACP
Load Balancing:    Layer3+4
Minimum Links:     1
In CLAG:           CLAG Active
LACP Sys Priority:
LACP Rate:         Fast Timeout
LACP Bypass:       LACP Bypass Not Supported

    Port       Speed     TX   RX   Err   Link Failures
-- --------   ------- ---- ---- ----- ---------------
UP swp51s2(P) 1G         0    0     0               0
UP swp51s3(P) 1G         0    0     0               0


All VLANs on L2 Port
----------------------
100-105

Untagged
----------
1

Vlans in disabled State
-------------------------
100-105

LLDP
--------   ---- ------------------
swp51s2(P) ==== swp1(spine01)
swp51s3(P) ==== swp1(spine02)
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Run the `ip link show` command on the bond and its slave interfaces:

```
cumulus@switch:~$ ip link show bond1
164: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master br0 state UP mode DORMANT group default
    link/ether c4:54:44:f6:44:5a brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show swp51s2
55: swp51s2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT group default qlen 1000
    link/ether c4:54:44:f6:44:5a brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show swp52s3
56: swp51s3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT group default qlen 1000
    link/ether c4:54:44:f6:44:5a brd ff:ff:ff:ff:ff:ff
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl show interface bond1 
```

{{< /tab >}}

{{< /tabs >}}

To verify that LACP bypass is enabled on a bond and its slave interfaces, use the `cat` command:

```
cumulus@switch:~$ cat /sys/class/net/bond1/bonding/lacp_bypass
on 1
cumulus@switch:~$ cat /sys/class/net/bond1/bonding/slaves
swp51 swp52
cumulus@switch:~$ cat /sys/class/net/swp52/bonding_slave/ad_rx_bypass
1
cumulus@switch:~$ cat /sys/class/net/swp51/bonding_slave/ad_rx_bypass
1
```

## Example LACP Bypass Configuration

The following configuration shows LACP bypass enabled for multiple active interfaces (all-active mode) with a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional bridge mode">}}:

```
...
auto bond1
iface bond1
    bond-slaves swp3 swp4
    bond-lacp-bypass-allow 1

auto br0
iface br0
    bridge-ports bond1 bond2 bond3 bond4 peer5
    mstpctl-bpduguard bond1=yes
...
```
