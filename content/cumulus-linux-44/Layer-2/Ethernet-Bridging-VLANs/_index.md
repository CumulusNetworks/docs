---
title: Ethernet Bridging - VLANs
author: NVIDIA
weight: 420
toc: 3
---
Ethernet bridges enable hosts to communicate through layer 2 by connecting all of the physical and logical interfaces in the system into a single layer 2 domain. The bridge is a logical interface with a MAC address and an {{<link url="Switch-Port-Attributes#mtu" text="MTU">}} (maximum transmission unit). The bridge MTU is the minimum MTU among all its members. By default, the [bridge's MAC address]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Configuration/Cumulus-Linux-Derivation-of-MAC-Address-for-a-Bridge" >}}) is the MAC address of the first port in the `bridge-ports` list. The bridge can also be assigned an IP address, as discussed {{<link url="#bridge-mac-addresses" text="below">}}.

{{%notice note%}}
- Bridge members can be individual physical interfaces, bonds, or logical interfaces that traverse an 802.1Q VLAN trunk.
- Cumulus Linux does not put all ports into a bridge by default.
{{%/notice%}}

## Ethernet Bridge Types

The Cumulus Linux bridge driver supports two configuration modes; one that is VLAN-aware and one that follows a more traditional Linux bridge model.

NVIDIA recommends that you use *{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode">}}* bridges instead of *traditional mode* bridges. The Cumulus Linux bridge driver is capable of VLAN filtering, which allows for configurations that are similar to incumbent network devices. For a comparison of traditional and VLAN-aware modes, see
[this knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" >}}).

You can configure both VLAN-aware and traditional mode bridges on the same network in Cumulus Linux.

- To create a VLAN-aware bridge, see {{<link title="VLAN-aware Bridge Mode">}}.
- To create a traditional mode bridge, see {{<link title="Traditional Bridge Mode">}}.

## Bridge MAC Addresses

The MAC address for a frame is learned when the frame enters the bridge through an interface. The MAC address is recorded in the bridge table and the bridge forwards the frame to its intended destination by looking up the destination MAC address. The MAC entry is then maintained for 1800 seconds (30 minutes). If the frame is seen with the same source MAC address before the MAC entry age is exceeded, the MAC entry age is refreshed; if the MAC entry age is exceeded, the MAC address is deleted from the bridge table.

The following example NCLU command output shows a MAC address table for the bridge.

```
cumulus@switch:~$ net show bridge macs
VLAN      Master    Interface    MAC                  TunnelDest  State      Flags    LastSeen
--------  --------  -----------  -----------------  ------------  ---------  -------  -----------------
untagged  bridge    swp1         44:38:39:00:00:03                                    00:00:15
untagged  bridge    swp1         44:38:39:00:00:04                permanent           20 days, 01:14:03
```

## bridge fdb Command Output

The Linux `bridge fdb` command interacts with the forwarding database table (FDB), which the bridge uses to store the MAC addresses it learns and the ports on which it learns those MAC addresses. The `bridge fdb show` command output contains some specific keywords:

| Keyword| Description |
|--- |--- |
| self | The FDB entry belongs to the FDB on the device referenced by the device.<br>For example, this FDB entry belongs to the VXLAN device:<br>`vx-1000`: `00:02:00:00:00:08 dev vx-1000 dst 27.0.0.10 self` |
| master |The FDB entry belongs to the FDB on the device's master and the FDB entry is pointing to a master's port.<br>For example, this FDB entry is from the master device named bridge and is pointing to the VXLAN bridge port:<br>`vx-1001`: `02:02:00:00:00:08 dev vx-1001 vlan 1001 master bridge` |
| extern_learn | The FDB entry is managed (or offloaded) by an external control plane, such as the BGP control plane for EVPN.|

The following example shows the `bridge fdb show` command output:

```
cumulus@switch:~$ bridge fdb show | grep 02:02:00:00:00:08
02:02:00:00:00:08 dev vx-1001 vlan 1001 extern_learn master bridge
02:02:00:00:00:08 dev vx-1001 dst 27.0.0.10 self extern_learn
```

- *02:02:00:00:00:08* is the MAC address learned with BGP EVPN.
- The first FDB entry points to a Linux bridge entry that points to the VXLAN device *vx-1001*.
- The second FDB entry points to the same entry on the VXLAN device and includes additional remote destination information.
- The VXLAN FDB augments the bridge FDB with additional remote destination information.
- All FDB entries that point to a VXLAN port appear as two entries. The second entry augments the remote destination information.

## Considerations

- A bridge cannot contain multiple subinterfaces of the **same** port. Attempting this configuration results in an error.
- In environments where both VLAN-aware and traditional bridges are used, if a traditional bridge has a subinterface of a bond that is a normal interface in a VLAN-aware bridge, the bridge is flapped when the traditional bridge's bond subinterface is brought down.
- You cannot enslave a VLAN raw device to a different master interface (you cannot edit the `vlan-raw-device` setting in the `/etc/network/interfaces` file). You need to delete the VLAN and recreate it.
- In Cumulus Linux, MAC learning is enabled by default on traditional and VLAN-aware bridge interfaces. Do not disable MAC learning unless you are using EVPN. See {{<link title="Ethernet Virtual Private Network - EVPN">}}.

## Related Information

- {{<exlink url="http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan" text="Linux Foundation - VLANs">}}
- {{<exlink url="http://www.linuxjournal.com/article/8172" text="Linux Journal - Linux as an Ethernet Bridge">}}
- [Comparing Traditional Bridge Mode to VLAN-aware Bridge Mode]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" >}})
