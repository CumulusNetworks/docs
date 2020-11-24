---
title: LACP Bypass
author: NVIDIA
weight: 125
pageID: 8362694
---
On Cumulus Linux, *LACP Bypass* is a feature that allows a
{{<link url="Bonding-Link-Aggregation" text="bond">}} configured in
802.3ad mode to become active and forward traffic even when there is no
LACP partner. A typical use case for this feature is to enable a host,
without the capability to run LACP, to PXE boot while connected to a
switch on a bond configured in 802.3ad mode. Once the pre-boot process
finishes and the host is capable of running LACP, the normal 802.3ad
link aggregation operation takes over.

## LACP Bypass All-active Mode

When a bond has multiple slave interfaces, each bond slave interface
operates as an active link while the bond is in bypass mode. This is
known as *all-active mode*. This is useful during PXE boot of a server
with multiple NICs, when the user cannot determine beforehand which port
needs to be active.

Keep in the mind the following caveats with all-active mode:

- All-active mode is not supported on bonds that are not specified as bridge ports on the switch. To work around this limitation, do one of the following:
- Configure the layer 3 interface on the physical link instead of using a bond
- Configure the LACP bond on the switch port so that the AS has neighbor LACP information
- Configure the bond interface as {{<link url="Bonding-Link-Aggregation#enable-balance-xor-mode" text="balance-xor">}} mode instead of LACP
- Spanning tree protocol (STP) does not run on the individual bond slave interfaces when the LACP bond is in all-active mode. Therefore, only use all-active mode on host-facing LACP bonds. Consider configuring {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree#bpdu-guard" text="STP BPDU guard">}} together with all-active mode.

{{%notice note%}}

The following features are not supported:

- priority mode
- bond-lacp-bypass-period
- bond-lacp-bypass-priority
- bond-lacp-bypass-all-active

{{%/notice%}}

{{%notice note%}}

In an {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG deployment">}}
where bond slaves of a host are connected to two switches and the bond
is in all-active mode, all the slaves of bond are active on both the
primary and secondary MLAG nodes.

{{%/notice%}}

## Configure LACP Bypass

To enable LACP bypass on the host-facing bond, configure `bond-lacp-bypass-allow`
using NCLU. The following commands create a VLAN-aware bridge with LACP bypass
enabled:

```
cumulus@switch:~$ net add bond bond1 bond slaves swp51s2,swp51s3
cumulus@switch:~$ net add bond bond1 clag id 1
cumulus@switch:~$ net add bond bond1 bond lacp-bypass-allow
cumulus@switch:~$ net add bond bond1 stp bpduguard
cumulus@switch:~$ net add bridge bridge ports bond1,bond2,bond3,bond4,peer5
cumulus@switch:~$ net add bridge bridge vids 100-105
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice note%}}

clag-id is not a required parameter in the configuration shown above. While LACP bypass is often configured on bonds involved in MLAG, MLAG is not required to use LACP bypass.

{{%/notice%}}

These commands create the following stanzas in
`/etc/network/interfaces`:

```
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
```

You can check the status of the configuration by running
`net show interface <bond>` on the bond and its slave interfaces:

```
cumulus@switch:~$ net show interface bond1

    Name   MAC               Speed   MTU   Mode
-- ------ ----------------- ------- ----- ----------
UP bond1  44:38:39:00:00:5b 1G      1500  Bond/Trunk

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

Use the `cat` command to verify that LACP bypass is enabled on a bond
and its slave interfaces:

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

The following configuration shows LACP bypass enabled for multiple
active interfaces (all-active mode) with a bridge in 
{{<link url="Traditional-Bridge-Mode" text="traditional bridge mode">}}:

```
auto bond1
iface bond1
    bond-slaves swp3 swp4
    bond-lacp-bypass-allow 1

auto br0
iface br0
    bridge-ports bond1 bond2 bond3 bond4 peer5
    mstpctl-bpduguard bond1=yes
```
