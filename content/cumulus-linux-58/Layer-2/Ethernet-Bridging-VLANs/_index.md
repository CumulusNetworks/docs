---
title: Ethernet Bridging - VLANs
author: NVIDIA
weight: 420
toc: 3
---
Ethernet bridges enable hosts to communicate through layer 2 by connecting the physical and logical interfaces in the system into a single layer 2 domain. The bridge is a logical interface with a MAC address and an {{<link url="Switch-Port-Attributes#mtu" text="MTU">}}. The bridge <span class="a-tooltip">[MTU](## "Maximum Transmission Unit")</span> is the minimum MTU among all its members. By default, the [bridge's MAC address]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Configuration/Cumulus-Linux-Derivation-of-MAC-Address-for-a-Bridge" >}}) is the MAC address of the first port in the `bridge-ports` list in the `/etc/network/interfaces` file. You can also assign an IP address to the bridge; see {{<link url="#bridge-mac-addresses" text="below">}}.

{{%notice note%}}
- Bridge members can be individual physical interfaces, bonds, or logical interfaces that traverse an 802.1Q VLAN trunk.
- Cumulus Linux does not put all ports into a bridge by default.
{{%/notice%}}

## Ethernet Bridge Types

The Cumulus Linux bridge driver supports two configuration modes; one that is VLAN-aware and one that follows a more traditional Linux bridge model.

NVIDIA recommends that you use {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode">}} bridges instead of *traditional mode* bridges. The Cumulus Linux bridge driver is capable of VLAN filtering, which allows for configurations that are similar to incumbent network devices. For a comparison of traditional and VLAN-aware modes, see
[this knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" >}}).

You can configure both VLAN-aware and traditional mode bridges on the same network in Cumulus Linux.

- To create a VLAN-aware bridge, see {{<link title="VLAN-aware Bridge Mode">}}.
- To create a traditional mode bridge, see {{<link title="Traditional Bridge Mode">}}.

## Bridge MAC Addresses

The switch learns the MAC address for a frame when the frame enters the bridge through an interface and records the MAC address in the bridge table. The bridge forwards the frame to its intended destination by looking up the destination MAC address. Cumulus Linux maintains the MAC entry for 1800 seconds (30 minutes). If the switch sees the frame with the same source MAC address before the MAC entry age expires, it refreshes the MAC entry age; if the MAC entry age expires, the switch deletes the MAC address from the bridge table.

The following example NVUE command output shows a MAC address table for the bridge.

```
cumulus@switch:~$ nv show bridge domain br_default mac-table
     age    bridge-domain  entry-type  interface   last-update  mac                src-vni  vlan  vni  Summary
---  -----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ---  ----------------------
+ 0  87699  br_default     permanent   bond3       87699        44:38:39:00:00:35
+ 1  87699  br_default     permanent   bond1       87699        44:38:39:00:00:31
+ 2  87699  br_default     permanent   bond2       87699        44:38:39:00:00:33
+ 3                        permanent   br_default               00:00:00:00:00:10
+ 4                        permanent   br_default               00:00:00:00:00:20
+ 5                        permanent   br_default               00:00:00:00:00:30
+ 6  84130  br_default     permanent   br_default  84130        44:38:39:22:01:b1           30
+ 7  87570  br_default     permanent   vxlan48     87570        42:ff:4d:82:c9:99
+ 8  84130                 permanent   vxlan48     84130        00:00:00:00:00:00  10                  remote-dst: 224.0.0.10
```

## bridge fdb Command Output

The Linux `bridge fdb` command interacts with the <span class="a-tooltip">[FDB](## "Forwarding Database Table")</span>, which the bridge uses to store the MAC addresses it learns and the ports on which it learns those MAC addresses. The `bridge fdb show` command output contains some specific keywords:

| Keyword| Description |
|--- |--- |
| `self` | The FDB entry belongs to the FDB on the device referenced by the device.<br>For example, this FDB entry belongs to the VXLAN device:<br>`vx-1000`: `00:02:00:00:00:08 dev vx-1000 dst 27.0.0.10 self` |
| `master` |The FDB entry belongs to the FDB on the device's master and the FDB entry is pointing to a master's port.<br>For example, this FDB entry is from the master device named bridge and is pointing to the VXLAN bridge port:<br>`vx-1001`: `02:02:00:00:00:08 dev vx-1001 vlan 1001 master bridge` |
| `extern_learn` | An external control plane, such as the <span class="a-tooltip">[BGP](## "Border Gateway Protocol")</span> control plane for <span class="a-tooltip">[EVPN](## "Ethernet Virtual Private Network")</span>, manages (offloads) the FDB entry. |

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
- If you use both VLAN-aware and traditional bridges, if a traditional bridge includes a bond subinterface that is a normal interface in a VLAN-aware bridge, the bridge flaps when you bring down the bond subinterface in the traditional bridge.
- You cannot enslave a VLAN raw device to a different master interface (you cannot edit the `vlan-raw-device` setting in the `/etc/network/interfaces` file). You need to delete the VLAN and recreate it.
- Cumulus Linux enables MAC learning by default on traditional and VLAN-aware bridge interfaces. Do not disable MAC learning unless you are using EVPN. See {{<link title="Ethernet Virtual Private Network - EVPN">}}.

## Related Information

- {{<exlink url="http://www.linuxjournal.com/article/8172" text="Linux Journal - Linux as an Ethernet Bridge">}}
- [Comparing Traditional Bridge Mode to VLAN-aware Bridge Mode]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" >}})
