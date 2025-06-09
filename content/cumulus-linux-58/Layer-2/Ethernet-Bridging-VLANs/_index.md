---
title: Ethernet Bridging - VLANs
author: NVIDIA
weight: 420
toc: 3
---
Ethernet bridges enable hosts to communicate through layer 2 by connecting the physical and logical interfaces in the system into a single layer 2 domain. The bridge is a logical interface with a MAC address and an {{<link url="Switch-Port-Attributes#mtu" text="MTU">}}. The bridge <span class="a-tooltip">[MTU](## "Maximum Transmission Unit")</span> is the minimum MTU among all its members.

When you configure a bridge with NVUE, Cumulus Linux automatically assigns a hardware address to the bridge. When you configure a bridge by editing the `/etc/network/interfaces` file, the bridge MAC address is the MAC address of the first port in the `bridge-ports` list in the `/etc/network/interfaces` file.

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
entry-id  age      bridge-domain  entry-type    interface   last-update  MAC address        remote-dst   src-vni  vlan
--------  -------  -------------  ------------  ----------  -----------  -----------------  -----------  -------  ----
1         0:12:54  br_default                   bond2       0:00:18      48:b0:2d:46:8f:ca                        20  
2         0:13:28  br_default                   bond2       0:01:17      48:b0:2d:66:cd:da                        20  
3         0:13:47  br_default     permanent     bond2       0:13:47      48:b0:2d:6c:f4:fc                            
4         0:12:54  br_default                   bond1       0:00:18      48:b0:2d:97:30:0d                        10  
5         0:13:28  br_default                   bond1       0:00:22      48:b0:2d:fc:d1:7f                        10  
6         0:13:47  br_default     permanent     bond1       0:13:47      48:b0:2d:b0:73:6d                            
7         0:06:36  br_default     extern_learn  vxlan48     0:06:36      44:38:39:be:ef:bb                        4036
8         0:12:53  br_default     extern_learn  vxlan48     0:12:53      48:b0:2d:28:23:1f                        30  
9         0:12:53  br_default     extern_learn  vxlan48     0:12:53      48:b0:2d:9d:37:18                        20  
10        0:12:53  br_default     extern_learn  vxlan48     0:12:53      48:b0:2d:e9:fd:e3                        10  
11        0:12:59  br_default     extern_learn  vxlan48     0:12:59      48:b0:2d:25:1f:8a                        20  
12        0:12:59  br_default     extern_learn  vxlan48     0:12:59      48:b0:2d:8a:2d:b4                        30  
13        0:12:59  br_default     extern_learn  vxlan48     0:12:59      48:b0:2d:8e:fc:0a                        10  
14        0:13:32  br_default     extern_learn  vxlan48     0:13:32      44:38:39:22:01:7c                        4024
15        0:13:32  br_default     extern_learn  vxlan48     0:13:32      44:38:39:22:01:7c                        4036
16        0:13:32  br_default     extern_learn  vxlan48     0:13:32      44:38:39:22:01:74                        4024
17        0:13:32  br_default     extern_learn  vxlan48     0:13:32      44:38:39:22:01:74                        4036
18        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:8a                        4036
19        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:84                        4036
20        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:7a                        4036
21        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:8a                        4024
22        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:84                        4024
23        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:7a                        4024
24        0:13:27  br_default     extern_learn  vxlan48     0:13:27      44:38:39:22:01:84                        10  
25        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:8a                        10  
26        0:13:27  br_default     extern_learn  vxlan48     0:13:27      44:38:39:22:01:84                        30  
27        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:8a                        30  
28        0:13:27  br_default     extern_learn  vxlan48     0:13:27      44:38:39:22:01:84                        20  
29        0:13:33  br_default     extern_learn  vxlan48     0:13:33      44:38:39:22:01:8a                        20  
30        0:13:47  br_default     permanent     vxlan48     0:13:47      4e:8e:1a:31:b7:cc                            
31        0:06:34                 extern_learn  vxlan48     0:13:32      44:38:39:22:01:74  10.10.10.63  4001         
32        0:13:32                 extern_learn  vxlan48     0:13:32      44:38:39:22:01:7c  10.10.10.64  4002         
33        0:13:33                 extern_learn  vxlan48     0:13:33      44:38:39:22:01:84  10.10.10.3   4002         
34        0:13:33                 extern_learn  vxlan48     0:13:33      44:38:39:22:01:7a  10.10.10.1   4002         
35        0:12:53                 extern_learn  vxlan48     0:12:53      48:b0:2d:9d:37:18  10.0.1.34    20           
36        0:13:33                 extern_learn  vxlan48     0:13:27      44:38:39:22:01:84  10.0.1.34    20           
37        0:12:59                 extern_learn  vxlan48     0:12:59      48:b0:2d:8e:fc:0a  10.0.1.34    10           
38        0:13:33                 extern_learn  vxlan48     0:13:33      44:38:39:22:01:8a  10.0.1.34    20           
39        0:13:33                 extern_learn  vxlan48     0:13:33      44:38:39:22:01:8a  10.0.1.34    30        
...
```

{{%notice note%}}
The `age` and `last update` counters in the `nv show bridge domain <domain-id> mac-table` command output are reversed. The `last update` counter shows the `age` data and the `age` counter shows the `last update` data. Cumulus Linux uses the `age` and `update` timers to determine when to remove an old MAC entry.
{{%/notice%}}

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
