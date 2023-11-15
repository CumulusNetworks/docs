---
title: TX Drop Counter Counts Twice for VXLAN Traffic
author: NVIDIA
weight: 393
toc: 4
---
Switches with a Broadcom ASIC reflect BUM traffic as TX drops on a VXLAN-enabled bridge. This behavior stems from the ASIC itself when you configure the switch with a VXLAN-enabled bridge.

## Symptom

When a VXLAN-enabled bridge receives a broadcast, unknown unicast, or multicast (BUM) frame, the ASIC avoids sending the frame back on the same port on which it is originally received to avoid loops. This split-horizon correction causes the `HwIfOutNonQDrops` transmit drop counter to increment twice for each count.

You see the effects of this double count when you run these commands:

- `sudo ethtool -S swpX`
- `net show counters`
- `cl-netstat`

This behavior does not occur on a bridge configured with non-VXLAN ports. However, when you configure VNIs as bridge-ports, the switch no longer treats switch ports in that bridge as regular ports. These switch ports are susceptible to this behavior, and the traffic statistics reflect this split-horizon correction.

You also see the `HwIfOutNonQDrops` counter counting twice on routed uplink ports, which receives VXLAN-encapsulated packets.

## Example

Host11 connects directly to VTEP1 on port swp11 and communicates with Host2, which connects directly to VTEP2 on port swp22. An IP-routed network separates VTEP1 and VTEP2.

For a unidirectional traffic flow from Host11 towards Host22:

- The ingress VTEP counts TX drops on the edge port where it receives traffic (VTEP1, swp11) at a rate equal to the number of BUM packets that the ingress port receives (from the source of the traffic flow).
- The egress VTEP counts TX drops on the routed uplink port (VTEP2, swp22) at a rate equal to number of BUM packets multiplied by number of remote VTEPs in the flood list (per VNI).

In the following example, the host sends 10000 multicast packets:

- The `TX_DRP` column for swp5 shows 10001, which indicates where the `TX_DRP` counter increments because of the split-horizon correction behavior.
- The `RX_OK` column for swp5 shows 10005 and the `TX_OK` column for swp1 shows 20049. These indicate the physical network path for the traffic flow relevant to this example.
- The `TX_OK` column for vni-1010 shows 20007, which indicates the network path across logical ports that are relevant to this example.

On the ingress VTEP:

- The edge port (swp5) receives 10005 packets. 10001 packets show as TX drops on the ingress port because of split-horizon correction.
- The routed uplink (swp1) sends 20049 packets toward the two remote VTEPs (VTEP2 and VTEP3). vni-1010 has two remote VTEPs in the flood list, so 20007 packets show as `TX_OK`; this is normal behavior.

```
cumulus@vtep1:~$ net show counters

Kernel Interface table

Iface       MTU   Met    RX_OK   RX_ERR    RX_DRP   RX_OVR   TX_OK    TX_ERR   TX_DRP   TX_OVR Flg
--------  ----- -----  ------- --------  -------- -------- -------  -------- -------- -------- -----
bridge     1500     0    10011        0         0        0   50023         0        0        0 BMRU
eth0       1500     0       95        0         0        0      14         0        0        0 BMRU
lo        65536     0        0        0         0        0       0         0        0        0 LRU
swp1       1500     0       80        0         0        0   20049         0        6        0 BMRU
swp5       1500     0    10005        0         0        0      54         0    10001        0 BMRU
swp15      1500     0       13        0         0        0      23         0        0        0 BMRU
swp16      1500     0        3        0         0        0   20058         0        0        0 BMRU
swp51      1500     0        0        0         0        0       0         0        0        0 BMU
vni-1010   1500     0        3        0         0        0   20007         0        0        0 BMRU
```

For the egress VTEP:

- The routed uplink port (swp5) receives 10055 packets. 20009 packets show as TX drops on the ingress port (and 20011 packets for the corresponding VNI) because of split-horizon correction.
- The edge port (swp49) sends 10061 packets towards the destination.

```
cumulus@vtep2:~$ net show counters

Kernel Interface table

Iface       MTU   Met    RX_OK   RX_ERR    RX_DRP   RX_OVR   TX_OK    TX_ERR   TX_DRP   TX_OVR Flg
--------  ----- -----  ------- --------  -------- -------- -------  -------- -------- -------- -----
bridge     1500     0    10014        0         0        0   40027         0        0        0 BMRU
eth0       1500     0      133        0         0        0      25         0        0        0 BMRU
lo        65536     0        0        0         0        0       0         0        0        0 LRU
swp5       1500     0    10055        0         0        0      90         0    20009        0 BMRU
swp15      1500     0        3        0         0        0      14         0        0        0 BMRU
swp16      1500     0        3        0         0        0   10060         0        0        0 BMRU
swp49      1500     0        6        0         0        0   10061         0        0        0 BMRU
vni-1010   1500     0    10004        0         0        0   20011         0        0        0 BMRU
vni-1020   1500     0        1        0         0        0       1        0         0        0 BMRU
```
