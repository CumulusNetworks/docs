---
title: VXLAN Scale
author: Cumulus Networks
weight: 151
aliases:
 - /display/CL36/VXLAN+Scale
 - /pages/viewpage.action?pageId=8362260
pageID: 8362260
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
On Broadcom Trident II and Tomahawk switches running Cumulus Linux,
there is a limit to the number of VXLANs you can configure
simultaneously. The limit most often given is 2000 VXLANs, but you might
want to get more specific and know exactly the limit for your specific
design.

{{%notice note%}}

While this limitation does apply to Trident II+ or Maverick ASICs,
Cumulus Linux supports the same number of VXLANs on these ASICs as it
does for Trident II or Tomahawk ASICs.

Mellanox Spectrum ASICs do not have a limitation on the number of VXLANs
that they can support.

{{%/notice%}}

The limit is a physical to virtual mapping where a switch can hold 15000
mappings in hardware before you encounter hash collisions. There is also
an upper limit of around 3000 VLANs you can configure before you hit the
reserved range (Cumulus Linux uses 3000-3999 by default). Cumulus
Networks typically uses a soft number because the math is unique to each
environment. An internal VLAN is consumed by each
<span style="color: #222222;"> layer 3 port, subinterface, [traditional
bridge](/version/cumulus-linux-36/Layer_2/Ethernet_Bridging_-_VLANs/Traditional_Bridge_Mode),
and the [VLAN-aware
bridge](/version/cumulus-linux-36/Layer_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments).
Therefore, the number of configurable VXLANs is: </span>

<span style="color: #222222;"> (total configurable 802.1q VLANs) -
(reserved VLANS) - (physical or logical interfaces) =  
4094-999-eth0-loopback = **3093** by default (without any other
configuration) </span>

The equation for the number of configurable VXLANs looks like this:

(number of trunks) \* (VXLAN/VLANs per trunk) - (Linux logical and
physical interfaces) = 15000

For example, on a 10Gb switch with 48 \* 10 G ports and 6 \* 40G
uplinks, you can calculate for X, the amount of configurable VXLANs:

48 \* X + (48 downlinks + 6 uplinks + 1 loopback + 1 eth0 + 1 bridge) =
15000  
48 \* X = 14943  
X = **311** VXLANs

Similarly, you can apply this logic to a 32 port 100G switch where 16
ports are broken up to 4 \* 25 Gbps ports, for a total of 64 \* 25 Gbps
ports:

64 \* X + (64 downlinks + 16 uplinks + 1 loopback + 1 eth0 + 1 bridge) =
15000

64 \* X = 14917

X = **233** VXLANs

However, not all ports are trunks for all VXLANs (or at least not all
the time). It is much more common for subsets of ports to be used for
different VXLANs. For example, a 10G (48 \* 10G + 6 \* 40G uplinks) can
have the following configuration:

| Ports    | Trunks          |
| -------- | --------------- |
| swp1-20  | 100 VXLAN/VLANs |
| swp21-30 | 100 VXLAN/VLANs |
| swp31-48 | X VXLAN/VLANs   |

The equation now looks like this:

20 swps \* 100 VXLANs + 10 swps \* 100 VXLANs + 18 swps \* X VXLANs +
(48 downlinks + 6 uplinks + loopback + 1 eth0 + 1 bridge) = 15000

20 swps \* 100 VXLANs + 10 swps \* 100 VXLANs + 18 swps \* X VXLANs =
14943

18 \* X = 11943

663 = VXLANS (still configurable) for a total of **863**
