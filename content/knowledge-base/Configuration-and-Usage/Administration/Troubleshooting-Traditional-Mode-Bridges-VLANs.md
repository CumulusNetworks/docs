---
title: Troubleshooting Traditional Mode Bridges - VLANs
author: NVIDIA
weight: 315
toc: 4
---

This article presents troubleshooting procedures for bridges in traditional mode.

## Bridge Is not Passing Traffic

### Symptoms

- The bridge looks correct (correct ports are in the bridge, and the swps are admin up, physically up),
- But traffic is not passing through the bridge.

### Solution

`brctl` does not show if the bridge is administratively down:

    cumulus@switch:~ $ brctl show br-untagged
    bridge name bridge id       STP enabled interfaces
    bridge      8000.443839003424   no      swp20
                                        swp22
                                        swp23

This bridge looks fine, but is admin down:

    cumulus@switch:~$ ip link show br-untagged
    63: bridge-untagged: <BROADCAST,MULTICAST> mtu 1500 qdisc noqueue state DOWN mode DEFAULT
        link/ether 44:38:39:00:34:24 brd ff:ff:ff:ff:ff:ff

## Bridge Is not Giving Spanning Tree Output

### Symptoms

- Bridge is up and passing traffic,
- But `mstpctl` is not giving any output on the bridge.

### Solution

No output means that spanning tree is not enabled for that specific bridge.

Example output:

    cumulus@switch:~$ mstpctl showbridge br-untagged
    cumulus@switch:~$

Add `bridge-stp on` under the bridge stanza and `ifup` the bridge. Output now appears when you run the `mstpctl showbridge` command:

    cumulus@switch:~$ mstpctl showbridge br-untagged
    bridge CIST info
      enabled         yes
      bridge id       8.000.44:38:39:00:34:24
      designated root 8.000.44:38:39:00:34:24
      regional root   8.000.44:38:39:00:34:24

## Individual Port Is not Forwarding Traffic despite Being up/up

### Symptoms

- `brctl` output looks fine,
- swp is showing up/up,
- But the swp does not forward traffic.

### Solution

Check if spanning tree has disabled ports by using the `mstpctl showport` command:

    cumulus@sw2:~$ mstpctl showport br-untagged
    *  swp17 8.003 down 8.000.44:38:39:00:25:E8 8.000.44:38:39:00:25:E8 0.000 Disa
    *  swp18 8.001 down 8.000.44:38:39:00:25:E8 8.000.44:38:39:00:25:E8 0.000 Disa
       swp19 8.002 forw 8.000.08:9E:01:CE:DC:D2 8.000.08:9E:01:CE:DC:D2 8.002 Root

{{<img src="/images/knowledge-base/tshoot-trad-mode-bridge.png">}}

In the above example, swp17-19 connect to the same switch. STP disabled two of the connections, as indicated with the "Disa" at the end of each line. This is correct behavior in this scenario. To get all 3 ports working in tandem at the same time, you could bond the ports together to form an LACP EtherChannel.
<!-- vale off -->
## You Do not Remember which Port a Device Is Hooked Into
<!-- vale on -->
### Symptoms

- Bridge is working correctly,
- And you have the MAC address of the device.

### Solution

Check the MAC address table by using the `brctl showmacs` command:

    cumulus@switch:~$ brctl showmacs br-untagged
    port name mac addr      is local?   ageing timer
    swp19     08:9e:01:ce:dc:d4 no         8.69
    swp17     44:38:39:00:25:e8 yes        0.00
    swp18     44:38:39:00:25:e9 yes        0.00
    swp19     44:38:39:00:25:ea yes        0.00
    cumulus@switch:~$

Now you can see all the MAC addresses (machine specific) and their associated front panel ports. With the above output, only swp19 has a device hooked into it, as indicated by the *no* under *is local?*.
<!-- vale off -->
## You Do not Remember which Port a Device Is Hooked up to, or which Bridge
<!-- vale on -->
### Symptoms

- You configured multiple bridges,
- And you have the MAC address of the device.

### Solution

Use the `bridge fdb show` command to see multiple bridges and their associated MAC addresses:

    cumulus@switch:~$ bridge fdb show
    44:38:39:00:25:e8 dev swp17 master br-10 permanent
    08:9e:01:ce:dc:c1 dev swp19 master br-20
    44:38:39:00:25:eb dev swp20 master br-5 permanent
    08:9e:01:ce:dc:d4 dev swp19 master br-20
    44:38:39:00:25:e9 dev swp18 master br-5 permanent
    44:38:39:00:25:ea dev swp19 master br-20 permanent

## See Also

- [Bonding and Link Aggregation on Cumulus Linux]({{<ref "/cumulus-linux-43/Layer-2/Bonding-Link-Aggregation" >}})
- [Configuring Spanning-Tree on Cumulus Linux]({{<ref "/cumulus-linux-43/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}})
- [Ethernet Bridging and VLANs on Cumulus Linux]({{<ref "/cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs" >}})()
