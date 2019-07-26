---
title: VXLAN Scale
author: Cumulus Networks
weight: 153
aliases:
 - /display/CL34/VXLAN+Scale
 - /pages/viewpage.action?pageId=7112536
pageID: 7112536
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
On Broadcom Trident II and Tomahawk hardware running Cumulus Linux,
there is a limit on the amount of VXLANs you can configure
simultaneously. The limit most often given is 2000 VXLANs that can be
run, but network architects want to get more specific and know exactly
the limit for their specific design.

The limit is a Physical to Virtual mappings where we can hold 15,000
mappings in hardware before we hit hash collisions. There is also an
upper limit of around 3000 VLANs you can configure before you hit the
reserved range (3000-3999 by default). When you hear a Cumulus Linux
employee say "around" or use a soft number its because the math is
unique per customer environment. A internal VLAN is consumed p
<span style="color: #222222;"> er L3 Port , per Sub Interface , per
Traditional Bridge and 1 is used for a bridge in vlan-aware mode.. This
means we have a configurable </span>

<span style="color: #222222;"> (Total Configurable 802.1q VLANs) -
(Reserved VLANS) - (Physical or Logical Interfaces) =  
4094-999-eth0-loopback = **3093** by default (without any other
configuration) </span>

The math equation for configurable VXLANs looks like the following:

(Amount of Trunks) \* (VXLAN/VLANs per Trunk) - (Linux Logical and
Physical Interfaces) = 15,000

For a specific example on a 10Gb switch with 48 \* 10 G ports and 6 \*
40G uplinks we can calculate for X (amount of configurable VXLANs)

48 \* X + (48 downlinks + 6 uplinks + 1 loopback + 1 eth0 + 1 bridge) =
15000  
48 \* X = 14943  
X = **311** VXLANs

Similarly this logic can be applied to a 32 \* 100G switch where 16
ports have been broken up to 4 \* 25 Gbps ports (64 \* 25 Gbps ports)

64 \* X + (64 downlinks + 16 uplinks + 1 loopback + 1 eth0 + 1 bridge) =
15000

64 \* X = 14917

X = **233** VXLANs

The problem is not all ports are trunks for all VXLANs (or at least not
all the time). It is much more common for subsets of ports to be used
for different VXLANs.

e.g.  
On a 10Gb (48 \* 10Gb + 6 \* 40Gb uplinks) we have the following
configuration:

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

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
