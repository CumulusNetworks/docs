---
title: NVIDIA Cumulus Linux Configuration Guide for Ethernet Storage Fabrics
author: NVIDIA Networking
weight: 50
product: Cumulus Networks Guides
---

[NVIDIA Spectrum](https://www.nvidia.com/en-us/networking/ethernet-switching/) switches with [Cumulus Linux](https://www.nvidia.com/en-us/networking/ethernet-switching/cumulus-linux/) network operating system allow you to create predictable, low latency and high throughput networks. The combination of best-in-class hardware and software enables the deployment of an efficient, redundant, and ESF ([Ethernet Storage Fabrics](https://www.nvidia.com/en-us/networking/guide-to-ethernet-storage-fabrics/)) optimized network with minimum effort. ESF includes complete, hybrid, or HCI storage fabrics and the storage backend of the AI systems.

This configuration guide demonstrates a generic network configuration of NVIDIA Spectrum switches for ESF using the Cumulus Linux operating system with [NVIDIA User Experience - NVUE]({{<ref "/cumulus-linux-50/System-Configuration/NVIDIA-User-Experience-NVUE" >}}) command-line interface (CLI). We also offer a portfolio of [NVIDIA DGX POD](https://www.nvidia.com/en-us/data-center/dgx-pod/) reference architecture solutions with all our leading partners.  

Cumulus Linux feature set allows you to configure a redundant active-active layer-2 (L2) and layer-3 (L3) environment using [Multi-Chassis Link Aggregation (MLAG)]({{<ref "/cumulus-linux-50/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}) and [Virtual Router Redundancy (VRR)]({{<ref "/cumulus-linux-50/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP" >}}). 

Often ESF environments with NVMe over Fabrics ([NVMeOF](https://nvmexpress.org/wp-content/uploads/NVMe_Over_Fabrics.pdf)) or [GPUDirect](https://developer.nvidia.com/gpudirect) technologies leverage the RDMA over Converged Ethernet ([RoCE](https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet)) to speed up the intensive data movements between nodes by eliminating latency-extensive data copying, CPU or GPU interrupts, and context switching. A fully shared-buffer architecture enables NVIDIA Spectrum switches to deliver a fair, predictable, line-rate throughput with ultra-low port-to-port latency for RoCE traffic. However, most RoCE configurations include multiple steps, and manually configuring them is not trivial and is error-prone. Cumulus Linux simplifies the RoCE configuration to a single command and automatically applies the best-practice settings for optimal performance.

In addition, NVIDIA Spectrum ASIC telemetry capabilities, including the unique What Just Happened ([WJH]({{<ref "/cumulus-linux-50/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH" >}})) feature, provide real-time visibility into the network. It enables you to discover and diagnose network problems by looking at flow latency events, buffer occupancy, and dropped packets, knowing why they dropped and acting accordingly to fix the network. WJH monitoring is supported for all events and traffic types, including Layer-1 (L1), L2, Access-Lists (ACL), L3, Tunneling, Buffers, and RoCE.

Network simulation is essential to avoid manual CLI and copy/paste configuration mistakes. [NVIDIA Air](https://www.nvidia.com/en-us/networking/air/) provides an online cloud-based network simulation platform where you can create a digital twin of your physical environment. You can build, simulate, and experience Cumulus Linux switches in AIR while testing your deployment configuration before applying it to production. Check out the [NVIDIA Air user guide]({{<ref "/guides/nvidia-air/" >}}) for more details.

There might be different specifications for each storage vendor deployment. You can always check out [Cumulus Linux documentation]({{<ref "/cumulus-linux-50" >}}) to explore more details and match the configuration for your deployment. 

Cumulus Linux documentation offers pre-build [**Try It**]({{<ref "/cumulus-linux-50/Try-It-Pre-built-Demos">}}) demos for certain features like MLAG, VRR, VXLAN/EVPN. These demos will automatically spin up a network simulation in Air so you can practice the desired feature configuration.

{{%notice note%}}

Before you proceed, if your switches are still running the [NVIDIA Onyx](https://www.nvidia.com/en-us/networking/ethernet-switching/onyx/), you can migrate to Cumulus Linux by following these guides to [uninstall the Onyx image]({{<ref "/knowledge-base/Installing-and-Upgrading/Installation/Uninstall-the-ONYX-Image">}}) and [installing a new Cumulus Linux image]({{<ref "/cumulus-linux-50/Installation-Management/Installing-a-New-Cumulus-Linux-Image">}}).</br> 
To ease the transition from ONYX to NVUE, you can upload the running configuration file from the Onyx switch with this [NVUE Migration Tool](https://air.nvidia.com/migrate/).

{{%/notice %}}

## Deployment Types

Storage vendors typically use L2 connectivity between the storage arrays and the top-of-rack (ToR or leaf) switches when deploying ESF. 

There are three main network configurations considered:

- **MLAG** - L2 ToR with routed (L3) uplinks to the spines.
- **MLAG over MLAG (a.k.a Back-to-Back MLAG)** - L2 ToR with switched (L2) uplinks to the spines. This scenario can be used for larger L2 domains but works only up to two spines. MLAG is configured in two levels, on the ToR and spine switches. Routing is done on the spine level.
- **Active-Active VXLAN** - An extended L2 domain over L3 networks using VxLAN/EVPN. Such deployments can use VXLAN L2 stretch or routing configurations.

MLAG is an active-active L2 redundancy protocol that allows a redundant ToR L2 network while doubling the bandwidth. But, it also enables the leverage of VRR, the active-active routing instances. With VRR, both ToR (or spines) switches are used to route the storage traffic simultaneously and create a redundant, higher bandwidth L3 network.

Regardless of the ESF network design chosen, when it comes to the ToR L2 redundancy, some vendors prefer or can deploy an active-active bonding (lacp/xor) on the storage Network Interface Cards (NICs) and some active-backup (or alb). In either case, we use the MLAG protocol for L2 or L3 redundancy (or both) in the examples below.

{{%notice note%}}

With RoCEv1, you have to set L2 fabric everywhere, so the routing (VRR) is not required. For RoCEv2, you may go either way. If your network requires inter-subnet routing, you should deploy L3 fabric with VRR gateways (and BGP/EVPN). If not, you may still go with the non-routed L2 domains.   

{{%/notice %}}


## MLAG

This section shows how to configure MLAG on Cumulus Linux using NVUE. 

{{<figure src="images/guides/storage-generic-config/MLAG.PNG">}}

Earlier, we mentioned that to achieve redundant top-of-rack deployment using MLAG, storage array NICs must be configured with active-active bonding. </br> 
But, in most cases, we will use the MLAG protocol set even for non-active-active bonds towards the ToR switches. 

There are two main reasons for that:

- To leverage the VRR functionality and use it as a storage traffic default gateway in case it needs to be routed to other subnets.
- In MLAG over MLAG (back-to-back MLAG) deployments, where the ToR uplinks are set as MLAG port.


{{%notice info%}}

Before starting MLAG configuration, make sure that both peers have the same Cumulus Linux version, preferably the newest one. Use the `cat /etc/lsb-release` or `nv show system` command to verify that.

{{%/notice %}}

### Inter-Chassis Bond (peerlink)

MLAG requires a dedicated link (LAG) between the peers. Cumulus Linux has a reserved name for this bond - *peerlink* with a unique VLAN L3 sub-interface - *peerlink.4094*. The peerlink is used to maintain state information between the MLAG peers and serves as a traffic backup path in case of failures.

When planning for link failures, you need to set a peerlink with enough bandwidth to meet your site strategy for handling failure scenarios. Therefore, we recommend you determine how much bandwidth is sent across the single-connected interfaces and set half of that bandwidth to the peer link.

By default, all VLANs are allowed on the peerlink and automatically added to it when created. The peerlink.4094 sub-interface is also created automatically after the peerlink set and the `mlag peer-ip` command. It uses the interface IPv6 linklocal address that provides L3 connectivity between the peers.

To create the peerlink and peerlink.4094 interfaces:

```
# nv set interface peerlink bond member <int-list> 
# nv set mlag peer-ip linklocal 
```
{{%notice info%}}

Do not use *169.254.0.1* as the MLAG peer-ip address. Cumulus Linux uses this address for [BGP unnumbered]({{<ref "/cumulus-linux-50/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered" >}}) interfaces. 

{{%/notice %}}

### MLAG Backup IP

MLAG uses the backup IP address to maintain the MLAG domain when the peerlink goes down.</br>

To set MLAG backup-ip: 
```
# nv set mlag backup [peer-address] vrf mgmt
```
{{%notice info%}}

Make sure that MLAG backup IP address is different than the peerlink.4094 address and is reachable via the network. Use switches loopback or management IP addresses.

{{%/notice %}}

### MLAG System MAC

MLAG system MAC represents both peers as the same switch in various control protocols such as spanning-tree BPDUs and LACP PDUs.</br> 
Make sure to set an identical MLAG system MAC address both peers.</br> 

To set MLAG system-mac:
```
# nv set mlag mac-address <MAC> 
```
{{%notice info%}}

Use MLAG MAC address from the reserved range of *44:38:39:ff:00:00-44:38:39:ff:ff:ff* only. Always set a unique MAC for different MLAG pairs.

{{%/notice %}}

{{%notice note%}}

In case your ESF environment is based on active-active VXLAN/EVPN fabric, you must also set a `system global anycast-mac` on both peers: 
```
# nv set system global anycast-mac <MAC>
```
{{%/notice %}}


### MLAG Ports 

MLAG port is a bond (LAG) interface set on both MLAG peers and contains the interface(s) connected to the storage NIC as its member(s). Therefore, you must specify each MLAG port with a unique MLAG ID (on both peers). Cumulus Linux uses `lacp` (802.3ad) bond mode by default, but `balance-xor` is also an option.

MLAG ports configuration depends on the bonding type used on the storage arrays NICs. For example, when the NICs are set to active-active bonding mode (lacp/xor), you **must** configure MLAG ports on the ToR switches connected to them. But, if the array NICs are set to active-backup (or alb) bonding, **do not** set MLAG ports. Because in that case, the traffic is sent only via a single switch until link failure (or a different flow/application transmit).

To configure the MLAG port, create bond interface with members and set an MLAG ID (skip if no MLAG ports are needed):
```
# nv set interface <bond-name> bond member <int-list> 
# nv set interface <bond-name> bond mlag id <number> 
```
As most ESF environments use jumbo MTU settings, Cumulus Linux default MTU is 9216B for all physical and logical interfaces. If you need to change it manually, use: 
```
# nv set interface <int-list> link mtu <MTU> 
```
It is optional to define the MLAG master and slave statically by setting the MLAG priority:  
```
# nv set mlag priority <prio>
``` 
Also, you can set `mlag init-delay` to postpone MLAG to be operational after reboot (e.g. to let the servers boot prior to the switches):
```
# nv set mlag init-delay <sec>
```
You can find more details about MLAG configuration in the [documenation]({{<ref "/cumulus-linux-50/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}).

## MLAG over MLAG (Back to Back MLAG)

Sometimes ESF environments require L2 connectivity for many hosts, an amount which will need more than two ToR switches. In that case, the ESF environment scales into a leaf-spine topology to extend the L2 domain. As we saw earlier, in that case, there are two types of network deployments used - MLAG over MLAG or extended L2 domains over L3 fabric with VxLAN/EVPN.

When we use MLAG over MLAG deployment, MLAG is also set on the spines level, and an MLAG port is configured between the ToR and spine switches.

{{<figure src="images/guides/storage-generic-config/mlag-over-mlag.PNG">}}

MLAG configuration on the spines is the same as we set on the ToR switches. As you can see in the diagram above, all physical ports between ToR and spine switches are bonded into a single MLAG port. This bond must have the same MLAG ID on each MLAG peer (it can be a different ID on ToR and spines).

## Bridge and VLANs

The Ethernet bridge enables L2 operation on Cumulus Linux switches by connecting the physical and logical interfaces into a single L2 domain. However, Cumulus Linux doesn’t have a bridge by default, and all physical ports are routed. Therefore, you must create a [VLAN-aware bridge]({{<ref "/cumulus-linux-50/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode" >}}) to enable L2 communication between the storage NICs and the ToR switches. The bridge implements all L2 technologies like STP, MAC address learning, VLANs, trunks, etc.

After creating the bridge, you need to assign ports (swp/MLAG ports). They are automatically added into VLAN 1 as untagged VLAN.</br> 
To create a bridge and assign ports to it, use: 
```
# nv set bridge domain br_default
# nv set interface <int> bridge domain br_default
```
You won’t use the default VLAN1 on the switch in most cases. To add new VLANs to the bridge and set the port as access (untagged):
```
# nv set bridge domain br_default vlan <vlan-list>
# nv set interface <int> bridge domain br_default access <vlan-id>
```
If the storage array NICs use dot1q, set the ToR downlink as trunk ports. Each trunk port works with dot1q tags for specified VLANs and a native VLAN (untagged).</br> 
To set port as trunk with native VLAN:
```
# nv set interface <int> bridge domain br_default vlan <vlan-list>
# nv set interface <int> bridge domain br_default untagged <vlan-id>
```

{{%notice info%}}

When deploying MLAG over MLAG, the configuration of the bridge and VLANs is the same for both MLAG layers (domains). If more than one VLAN is used on the storage NICs, use the same trunk configuration on the MLAG port between the ToR and spine switches.

{{%/notice %}}

## MLAG Configuration Example

{{< tabs "MLAG_config">}}
{{< tab "MLAG">}}
{{< tabs "Bondings">}}
{{< tab "Active-Active NIC Bonding">}}
{{< tabs "switch">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond1 bond mlag id 1
nv set interface bond1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1 bridge domain br_default
nv set interface bond1 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}} 
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond1 bond mlag id 1
nv set interface bond1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1 bridge domain br_default
nv set interface bond1 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "Active-Backup NIC Bonding">}}
{{< tabs "switch1">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface swp1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1 bridge domain br_default
nv set interface swp1 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface swp1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1 bridge domain br_default
nv set interface swp1 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "MLAG over MLAG">}}
{{< tabs "Bondings11">}}
{{< tab "Active-Active NIC Bonding">}}
{{< tabs "1switch">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond2 bond member swp4-swp5
nv set interface bond1 bond mlag id 1
nv set interface bond2 bond mlag id 2
nv set interface bond1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1,bond2 bridge domain br_default
nv set interface bond1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond2 bond member swp4-swp5
nv set interface bond1 bond mlag id 1
nv set interface bond2 bond mlag id 2
nv set interface bond1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1,bond2 bridge domain br_default
nv set interface bond1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.14 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.13 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "Active-Backup NIC Bonding">}}
{{< tabs "1switch1">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond2 bond member swp4-swp5
nv set interface bond2 bond mlag id 2
nv set interface swp1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1,bond2 bridge domain br_default
nv set interface swp1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface bond2 bond member swp4-swp5
nv set interface bond2 bond mlag id 2
nv set interface swp1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1,bond2 bridge domain br_default
nv set interface swp1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.14 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.13 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}

## Routing Configuration

As we already know, VRR serves as the gateway for storage traffic, whether to route between VLANs on the ToR switches level or route traffic between racks in the data center/external networks.</br>
Depending on the network deployment type, we configure VRR instances on the ToR switches level or the spine switches level (MLAG over MLAG). 
For each storage subnet (VLAN), you need to create a VRR instance. This virtual router instance works on top of a Switch Virtual Interface (SVI) and holds a virtual IP address that serves as the gateway of the subnet and virtual MAC address used to reply to ARP requests from the NIC. </br>
VRR is an active-active routing instance, so both MLAG peers must have the same VRR instance configuration to reply to ARP requests and forward routed traffic simultaneously. VRR is different from the Virtual Routing Redundancy Protocol ([VRRP]({{<ref "/cumulus-linux-50/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP#vrrp" >}})) as the instances on both peers are independent of each other and work simultaneously rather than in active-standby mode. 

{{<figure src="images/guides/storage-generic-config/routing-mlag.PNG">}}

To set VRR, you first need to create an SVI (VLAN interface) on each peer and set unique IP addresses within the same subnet (as the NIC subnet). Then on top of each SVIs, the VRR instance is configured. Both peers share the same virtual IP and MAC addresses.

Create an L3 VLAN interface by using the “vlan” keyword followed by the VLAN ID and set a unique IP address:
```
# nv set interface vlan<ID> ip address <address/prefix>
```
Now add VRR addresses on top of the SVI and enable the virtual instance
```
# nv set interface vlan<ID> ip vrr address <address/prefix>
# nv set interface vlan<ID> ip vrr mac-address <address>
# nv set interface vlan<ID> ip vrr state up
```

After VRR is set for the L2 domain (ToR/spine) MLAG peers, you need to configure L3 uplinks, either router ports or SVIs. Then you can use static or dynamic routing to route traffic. The most common routing protocol in data centers is Border Gateway Protocol ([BGP]({{<ref "/cumulus-linux-50/Layer-3/Border-Gateway-Protocol-BGP/" >}})), particularly [eBGP]({{<ref "/cumulus-linux-50/Layer-3/Border-Gateway-Protocol-BGP#ebgp-and-ibgp">}}). 

{{%notice note%}}

Cumulus Linux provides a unique and easy way to configure BGP using [Auto BGP]({{<ref "/cumulus-linux-50/Layer-3/Border-Gateway-Protocol-BGP/#auto-bgp" >}}) and [BGP Unnumbered]({{<ref "/cumulus-linux-50/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered" >}}) features.

{{%/notice %}}

## VRR Configuration Example

{{< tabs "VRR_config">}}
{{< tab "MLAG">}}
{{< tabs "Bondingsvrr">}}
{{< tab "Active-Active NIC Bonding">}}
{{< tabs "vrrrswitch">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond1 bond mlag id 1
nv set interface bond1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1 bridge domain br_default
nv set interface bond1 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.2/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.2/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.2/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}} 
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond1 bond mlag id 1
nv set interface bond1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1 bridge domain br_default
nv set interface bond1 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.3/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.3/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.3/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "Active-Backup NIC Bonding">}}
{{< tabs "vrrswitch1">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface swp1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1 bridge domain br_default
nv set interface swp1 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.2/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.2/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.2/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface swp1 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1 bridge domain br_default
nv set interface swp1 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.3/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.3/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.3/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "MLAG over MLAG">}}
{{< tabs "vrrBondings11">}}
{{< tab "Active-Active NIC Bonding">}}
{{< tabs "vrr1switch">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond2 bond member swp4-swp5
nv set interface bond1 bond mlag id 1
nv set interface bond2 bond mlag id 2
nv set interface bond1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1,bond2 bridge domain br_default
nv set interface bond1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface bond1 bond member swp1
nv set interface bond2 bond member swp4-swp5
nv set interface bond1 bond mlag id 1
nv set interface bond2 bond mlag id 2
nv set interface bond1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond1,bond2 bridge domain br_default
nv set interface bond1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.14 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.2/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.2/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.2/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.13 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.3/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.3/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.3/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "Active-Backup NIC Bonding">}}
{{< tabs "1vrrswitch1">}}
{{< tab "leaf01">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.12 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond2 bond member swp4-swp5
nv set interface bond2 bond mlag id 2
nv set interface swp1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1,bond2 bridge domain br_default
nv set interface swp1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
nv set interface peerlink bond member swp2-3
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.11 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag init-delay 10
nv set interface bond2 bond member swp4-swp5
nv set interface bond2 bond mlag id 2
nv set interface swp1,bond2 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface swp1,bond2 bridge domain br_default
nv set interface swp1,bond2 bridge domain br_default vlan 10,20,30
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.14 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag priority 1000
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.2/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.2/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.2/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
nv set interface peerlink bond member swp3-4
nv set mlag peer-ip linklocal
nv set mlag backup 192.168.200.13 vrf mgmt
nv set mlag mac-address 44:38:39:BE:EF:BB
nv set mlag init-delay 10
nv set interface bond3 bond member swp1-2
nv set interface bond3 bond mlag id 3
nv set interface bond3 link mtu 9000
nv set bridge domain br_default
nv set bridge domain br_default vlan 10,20,30
nv set interface bond3 bridge domain br_default
nv set interface bond3 bridge domain br_default vlan 10,20,30
nv set interface vlan10 ip address 10.1.10.3/24
nv set interface vlan10 ip ip vrr address 10.1.10.1/24
nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
nv set interface vlan10 ip vrr state up
nv set interface vlan20 ip address 10.1.20.3/24
nv set interface vlan20 ip ip vrr address 10.1.20.1/24
nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
nv set interface vlan20 ip vrr state up
nv set interface vlan30 ip address 10.1.30.3/24
nv set interface vlan30 ip ip vrr address 10.1.30.1/24
nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
nv set interface vlan30 ip vrr state up
nv config apply 
nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}

## Configuration Verification

You can verify the configuration with NVUE or Linux commands. 

### MLAG

{{< tabs "mlag_ver">}}
{{< tab "NVUE">}}
{{< tabs "switches_mlag_ver">}}
{{< tab "leaf01">}}
```
cumulus@leaf01:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               10                 The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:be:ef:aa        44:38:39:BE:EF:AA  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:22  linklocal          Peer Ip Address
priority        1000                     1000               Mlag Priority
[backup]        192.168.200.12           192.168.200.12     Set of MLAG backups
backup-active   True                                        Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:21                           Mlag Local Unique Id
local-role      primary                                     Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:22                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   32768                                       Mlag Peer Priority
peer-role       secondary                                   Mlag Peer Role
```
{{< /tab >}}
{{< tab "leaf02">}}
```
cumulus@leaf02:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               10                 The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:be:ef:aa        44:38:39:BE:EF:AA  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:21  linklocal          Peer Ip Address
priority        32768                    32768              Mlag Priority
[backup]        192.168.200.11           192.168.200.11     Set of MLAG backups
backup-active   True                                        Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:22                           Mlag Local Unique Id
local-role      secondary                                   Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:21                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   1000                                        Mlag Peer Priority
peer-role       primary                                     Mlag Peer Role
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "Linux">}}
{{< tabs "switches_mlag_ver_linux">}}
{{< tab "leaf01">}}
```
cumulus@leaf01:mgmt:~$ clagctl
The peer is alive
     Our Priority, ID, and Role: 1000 44:38:39:00:00:21 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:22 secondary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:22 (linklocal)
                      Backup IP: 192.168.200.12 (active)
                     System MAC: 44:38:39:be:ef:aa
CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
           bond1   bond1              1         -                      -
```
{{< /tab >}}
{{< tab "leaf02">}}
```
cumulus@leaf02:mgmt:~$ clagctl
The peer is alive
     Our Priority, ID, and Role: 32768 44:38:39:00:00:22 secondary
    Peer Priority, ID, and Role: 1000 44:38:39:00:00:21 primary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:21 (linklocal)
                      Backup IP: 192.168.200.11 (active)
                     System MAC: 44:38:39:be:ef:aa
CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
           bond1   bond1              1         -                      -
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}

### Bridge and VLANs

{{< tabs "bridge_vlans">}}
{{< tab "NVUE">}}
{{< tabs "switches_br">}}
{{< tab "leaf01">}}
```
cumulus@leaf01:mgmt:~$ nv show bridge domain br_default
               operational  applied     description
-------------  -----------  ----------  ----------------------------------------------------------------------
encap          802.1Q       802.1Q      Interfaces added to this domain will, by default, use this encapsul...
mac-address                 auto        Override global mac address
type           vlan-aware   vlan-aware  Type of bridge domain.
untagged                    1           Interfaces added to this domain will, by default, be trunk interfac...
multicast
  snooping
    enable     on           off         Turn the feature 'on' or 'off'.  The default is 'off'.
    querier
      enable   off                      Turn the feature 'on' or 'off'.  The default is 'off'.
stp
  priority     32768        32768       stp priority. The priority value must be a number between 4096 and...
  state        up           up          The state of STP on the bridge
[vlan]                      10          Set of vlans in the bridge domain.  Only applicable when the domain...
[vlan]                      20
[vlan]                      30
[mdb]                                   Set of mdb entries in the bridge domain
[router-port]  1                        Set of multicast router ports
```
{{< /tab >}}
{{< tab "leaf02">}}
```
cumulus@leaf02:mgmt:~$ nv show bridge domain br_default
               operational  applied     description
-------------  -----------  ----------  ----------------------------------------------------------------------
encap          802.1Q       802.1Q      Interfaces added to this domain will, by default, use this encapsul...
mac-address                 auto        Override global mac address
type           vlan-aware   vlan-aware  Type of bridge domain.
untagged                    1           Interfaces added to this domain will, by default, be trunk interfac...
multicast
  snooping
    enable     on           off         Turn the feature 'on' or 'off'.  The default is 'off'.
    querier
      enable   off                      Turn the feature 'on' or 'off'.  The default is 'off'.
stp
  priority     32768        32768       stp priority. The priority value must be a number between 4096 and...
  state        up           up          The state of STP on the bridge
[vlan]                      10          Set of vlans in the bridge domain.  Only applicable when the domain...
[vlan]                      20
[vlan]                      30
[mdb]                                   Set of mdb entries in the bridge domain
[router-port]  1                        Set of multicast router ports
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "Linux">}}
{{< tabs "switches_br_linux">}}
{{< tab "leaf01">}}
```
cumulus@leaf01:mgmt:~$ bridge vlan show
port        vlan ids
peerlink    1           PVID Egress Untagged
            10
            20
            30
bond1       1           PVID Egress Untagged
            10
            20
            30
br_default  10
            20
            30
```
{{< /tab >}}
{{< tab "leaf02">}}
```
cumulus@leaf02:mgmt:~$ bridge vlan show
port        vlan ids
peerlink    1           PVID Egress Untagged
            10
            20
            30
bond1       1           PVID Egress Untagged
            10
            20
            30
br_default  10
            20
            30
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}

### Interfaces, SVI and VRR

{{< tabs "interfaces_svi_vrr">}}
{{< tab "Interfaces and SVI">}}
{{< tabs "switches_int_svi">}}
{{< tab "leaf01">}}
```
cumulus@leaf01:mgmt:~$ nv show interface
Interface        MTU    Speed  State  Remote Host      Remote Port        Type      Summary
---------------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ bond1          9000   1G     up                                         bond
+ eth0           1500   1G     up     oob-mgmt-switch  swp6               eth       IP Address: 192.168.200.11/24
+ lo             65536         up                                         loopback  IP Address:     10.10.10.1/32
  lo                                                                                IP Address:       127.0.0.1/8
  lo                                                                                IP Address:           ::1/128
+ peerlink       9216   2G     up                                         bond
+ peerlink.4094  9216          up                                         sub
+ swp1           9000   1G     up     server01         44:38:39:00:00:12  swp
+ swp2           9216   1G     up     leaf02           swp2               swp
+ swp3           9216   1G     up     leaf02           swp3               swp
+ swp4           9216   1G     up     spine01          swp1               swp
+ swp5           9216   1G     up     spine02          swp1               swp
+ vlan10         9216          up                                         svi       IP Address:      10.1.10.2/24
+ vlan20         9216          up                                         svi       IP Address:      10.1.20.2/24
+ vlan30         9216          up                                         svi       IP Address:      10.1.30.2/24
```
{{< /tab >}}
{{< tab "leaf02">}}
```
cumulus@leaf02:mgmt:~$ nv show interface
Interface        MTU    Speed  State  Remote Host      Remote Port        Type      Summary
---------------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ bond1          9000   1G     up                                         bond
+ eth0           1500   1G     up     oob-mgmt-switch  swp6               eth       IP Address: 192.168.200.12/24
+ lo             65536         up                                         loopback  IP Address:     10.10.10.2/32
  lo                                                                                IP Address:       127.0.0.1/8
  lo                                                                                IP Address:           ::1/128
+ peerlink       9216   2G     up                                         bond
+ peerlink.4094  9216          up                                         sub
+ swp1           9000   1G     up     server01         44:38:39:00:00:16  swp
+ swp2           9216   1G     up     leaf01           swp2               swp
+ swp3           9216   1G     up     leaf01           swp3               swp
+ swp4           9216   1G     up     spine01          swp2               swp
+ swp5           9216   1G     up     spine02          swp2               swp
+ vlan10         9216          up                                         svi       IP Address:      10.1.10.3/24
+ vlan20         9216          up                                         svi       IP Address:      10.1.20.3/24
+ vlan30         9216          up                                         svi       IP Address:      10.1.30.3/24
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "VRR">}}
{{< tabs "switches_vrr">}}
{{< tab "leaf01">}}
```
cumulus@leaf01:mgmt:~$ nv show interface vlan10 ip vrr
             operational        applied            description
-----------  -----------------  -----------------  ------------------------------------------------------
enable                          on                 Turn the feature 'on' or 'off'.  The default is 'off'.
mac-address  00:00:00:00:00:10  00:00:00:00:00:10  Override anycast-mac
mac-id                          none               Override anycast-id
[address]    10.1.10.1/24       10.1.10.1/24       Virtual addresses with prefixes
state        up                 up                 The state of the interface
```
```
cumulus@leaf01:mgmt:~$ nv show interface vlan20 ip vrr
             operational        applied            description
-----------  -----------------  -----------------  ------------------------------------------------------
enable                          on                 Turn the feature 'on' or 'off'.  The default is 'off'.
mac-address  00:00:00:00:00:20  00:00:00:00:00:20  Override anycast-mac
mac-id                          none               Override anycast-id
[address]    10.1.20.1/24       10.1.20.1/24       Virtual addresses with prefixes
state        up                 up                 The state of the interface
```
```
cumulus@leaf01:mgmt:~$ nv show interface vlan30 ip vrr
             operational        applied            description
-----------  -----------------  -----------------  ------------------------------------------------------
enable                          on                 Turn the feature 'on' or 'off'.  The default is 'off'.
mac-address  00:00:00:00:00:30  00:00:00:00:00:30  Override anycast-mac
mac-id                          none               Override anycast-id
[address]    10.1.30.1/24       10.1.30.1/24       Virtual addresses with prefixes
state        up                 up                 The state of the interface
```
{{< /tab >}}
{{< tab "leaf02">}}
```
cumulus@leaf02:mgmt:~$ nv show interface vlan10 ip vrr
             operational        applied            description
-----------  -----------------  -----------------  ------------------------------------------------------
enable                          on                 Turn the feature 'on' or 'off'.  The default is 'off'.
mac-address  00:00:00:00:00:10  00:00:00:00:00:10  Override anycast-mac
mac-id                          none               Override anycast-id
[address]    10.1.10.1/24       10.1.10.1/24       Virtual addresses with prefixes
state        up                 up                 The state of the interface
```
```
cumulus@leaf02:mgmt:~$ nv show interface vlan20 ip vrr
             operational        applied            description
-----------  -----------------  -----------------  ------------------------------------------------------
enable                          on                 Turn the feature 'on' or 'off'.  The default is 'off'.
mac-address  00:00:00:00:00:20  00:00:00:00:00:20  Override anycast-mac
mac-id                          none               Override anycast-id
[address]    10.1.20.1/24       10.1.20.1/24       Virtual addresses with prefixes
state        up                 up                 The state of the interface
```
```
cumulus@leaf02:mgmt:~$ nv show interface vlan30 ip vrr
             operational        applied            description
-----------  -----------------  -----------------  ------------------------------------------------------
enable                          on                 Turn the feature 'on' or 'off'.  The default is 'off'.
mac-address  00:00:00:00:00:30  00:00:00:00:00:30  Override anycast-mac
mac-id                          none               Override anycast-id
[address]    10.1.30.1/24       10.1.30.1/24       Virtual addresses with prefixes
state        up                 up                 The state of the interface
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< /tabs >}}

## Extended L2 Domain over L3 Fabric (VXLAN/EVPN)

If your ESF environment requires more than two spines in the L2 domain, or you need to tunnel L2 storage traffic over the L3 fabric, use the [VxLAN Active-Active mode]({{<ref "/cumulus-linux-50/Network-Virtualization/VXLAN-Active-Active-Mode" >}}) mode with [EVPN]({{<ref "/cumulus-linux-50/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/" >}}) in your deployment. In this deployment, you must use the BGP protocol to work with the EVPN control plane. 

{{<figure src="images/guides/storage-generic-config/vxlan-mlag.PNG">}}

If your ESF environment only uses a single VLAN or the VLANs do not communicate, you will need to set the [L2 extension]({{<ref "/cumulus-linux-50/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration" >}}) (*L2 stretch*) functionality.</br> 
But if you need to deploy [EVPN inter-subnet routing]({{<ref "/cumulus-linux-50/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing" >}}) in your ESF deployment, Cumulus Linux offers two options:

- **Centralized routing** - A designated VTEPs serves as subnets' L3 gateways and perform routing between them. Rest of the VTEPs just perform bridging.
- **Distributed symmetric routing** - All VTEP perform routing on the ingress and egress.

When working with an EVPN network, you can leverage the EVPN Multihoming ([EVPN MH]({{<ref "/cumulus-linux-50/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming" >}})) standard capabilities to eliminate the need for MLAG in your environment. By removing the MLAG from the ToRs switches, you can use a larger (more than two ToR) L2 redundancy group, and as it uses a standard BGP-EVPN control plane, it allows multi-vendor interoperability, so that you can deploy multi-vendor ToRs. 

{{<figure src="images/guides/storage-generic-config/evpn-mh.PNG">}}

As VXLAN/EVPN in general and EVPN MH, in particular, are rare configurations in ESF networks, we don’t cover a step-by-step configuration in this guide. However, [here]({{<ref "/cumulus-linux-50/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Configuration-Examples" >}}) you can find a few configuration examples.</br>

Check out the [Network Virtualization]({{<ref "/cumulus-linux-50/Network-Virtualization/" >}}) and [EVPN Multihoming]({{<ref "/cumulus-linux-50/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming" >}}) documentation for more detailed information and configuration commands.


{{%notice note%}}

If you use an NSX-T environment, check out this [NVIDIA Cumulus Linux Deployment Guide for VMware NSX-T]({{<ref "/guides/nsxt" >}}) for more information.

{{%/notice %}}

## RDMA over Converged Ethernet (RoCE)

When ESF fabric runs RoCE traffic, we must ensure that all network elements in the traffic path are configured to handle RoCE. Cumulus Linux provides a single RoCE command which automatically sets all RoCE best practices configurations on the switch. It sets all the needed settings to achieve the best performance with RoCE traffic. This configuration includes buffer pools settings, traffic classification and priority mappings, PFC and ECN thresholds, queuing and scheduling settings for regular, RoCE, and CNP packets.

To set the switch work with RoCE:
```
# nv set qos roce
```
Cumulus Linux supports a single command configuration both for RoCEv1 and RoCEv2. The default RoCE mode is lossless with PFC and ECN, but you can also set the lossy mode to use ECN only.

To configure RoCE lossy mode:
```
# nv set qos roce lossy
```

For more information on Cumulus Linux RoCE default best-practice configuration, refer to [RDMA over Converged Ethernet - RoCE]({{<ref "/cumulus-linux-50/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE">}}) documentation page.

{{%notice note%}}

NVIDIA Spectrum ASIC with Cumulus Linux provides a line-rate RoCE traffic on top of VXLAN/EVPN fabrics while keeping all QoS settings over the tunnels end-to-end without any latency impact.

{{%/notice %}}

{{%notice note%}}

 Make sure to configure RoCE on the NICs as well. For NIC RoCE configuration, refer to [MLNX_OFED](https://docs.nvidia.com/networking/pages/viewpage.action?pageId=58757626) documentation. In addition, NVIDIA ConnectX SmartNICs provides seamless RoCE NIC configuration using the zero-touch RoCE ([ZTR](https://developer.nvidia.com/blog/scaling-zero-touch-roce-technology-with-round-trip-time-congestion-control/)) feature. 

{{%/notice %}}

## Configuration Management

Cumulus Linux has a declarative CLI with commit-confirm and configuration management capabilities. Thus, all the configured commands will take effect only after they are applied and remain persistent after they are saved.

To apply the configuration as running-configuration:
```
# nv config apply
```
To save the configuration as a persistent startup-configuration:
```
# nv config save
```
Once the configuration is saved, NVUE creates a *startup.yaml* configuration file. This YAML file will be used as the startup-configuration of the switch. 

NVUE has many useful configuration management options. Check out the [configuration management commands]({{<ref "/cumulus-linux-50/System-Configuration/NVIDIA-User-Experience-NVUE#configuration-management-commands" >}}) section of NVUE documentation for more details.