---
title: VXLAN Scale
author: NVIDIA
weight: 630
toc: 3
---
On Broadcom Trident II and Tomahawk switches running Cumulus Linux, there is a limit to the number of VXLANs you can configure simultaneously. The limit most often given is 2000 VXLANs, but you might want to get more specific and know exactly the limit for your specific design.

{{%notice note%}}

While this limitation does apply to Trident II+, Trident3, or Maverick ASICs, Cumulus Linux supports the same number of VXLANs on these ASICs as it does for Trident II or Tomahawk ASICs.

Mellanox Spectrum ASICs do not have a limitation on the number of VXLANs that they can support.

{{%/notice%}}

The limit is a physical to virtual mapping where a switch can hold 15000 mappings in hardware before you encounter hash collisions. There is also an upper limit of around 3000 VLANs you can configure before you hit the reserved range (Cumulus Linux uses 3600-3999 by default). Cumulus Linux typically uses a soft number because the math is unique to each environment. An internal VLAN is consumed by each layer 3 port, subinterface, {{<link url="Traditional-Bridge-Mode" text="traditional bridge">}}, and the {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}}. Therefore, the number of configurable VLANs is:

<p style="text-align: center;">(total configurable 802.1q VLANs) - (reserved VLANS) - (physical or logical interfaces) = </p>
<p style="text-align: center;">4094-999-eth0-loopback = <b>3093</b> by default (without any other
configuration)</p>

The equation for the number of configurable VXLANs looks like this:

<p style="text-align: center;">(number of trunks) * (VXLAN/VLANs per trunk) = 15000 - (Linux logical and physical interfaces)<p>

For example, on a 10Gb switch with 48 * 10 G ports and 6 * 40G uplinks, you can calculate for X, the amount of configurable VXLANs:

<p style="text-align: center;">48 * X = 15000 - (48 downlinks + 6 uplinks + 1 loopback + 1 eth0 + 1 bridge)</p>
<p style="text-align: center;">48 * X = 14943</p>
<p style="text-align: center;">X = <b>311</b> VXLANs</p>

Similarly, you can apply this logic to a 32 port 100G switch where 16 ports are broken up to 4 \* 25 Gbps ports, for a total of 64 \* 25 Gbps ports:

<p style="text-align: center;">64 * X = 15000 - (64 downlinks + 16 uplinks + 1 loopback + 1 eth0 + 1 bridge)</p>
<p style="text-align: center;">64 * X = 14917</p>
<p style="text-align: center;">X = <b>233</b> VXLANs</p>

However, not all ports are trunks for all VXLANs (or at least not all the time). It is much more common for subsets of ports to be used for different VXLANs. For example, a 10G (48 \* 10G + 6 \* 40G uplinks) can have the following configuration:

| Ports    | Trunks          |
| -------- | --------------- |
| swp1-20  | 100 VXLAN/VLANs |
| swp21-30 | 100 VXLAN/VLANs |
| swp31-48 | X VXLAN/VLANs   |

The equation now looks like this:

<p style="text-align: center;">20 swps * 100 VXLANs + 10 swps * 100 VXLANs + 18 swps * X VXLANs +  (48 downlinks + 6 uplinks + loopback + 1 eth0 + 1 bridge) = 15000</p>
<p style="text-align: center;">20 swps * 100 VXLANs + 10 swps * 100 VXLANs + 18 swps * X VXLANs = 14943</p>
<p style="text-align: center;">18 * X = 11943</p>
<p style="text-align: center;">663 = VXLANS (still configurable) for a total of <b>863</b></p>
